from __future__ import division
from bson import ObjectId
import os
from django.http import HttpResponse
import json
import datetime
from rest_framework.response import Response
from rest_framework import status
import base64
from django.urls import reverse
from django.conf import settings
import io


def init_response_dict():
    return {'status': False,
            'cv': {},
            'ud': {},
            'errors': {'__all__': list()}}

def generate_unique_object_id():
    return str(ObjectId())


def return_rest_response(data, response_status=status.HTTP_200_OK):
    return Response(data=data, status=response_status)


def return_multi_key_json_response(keys, values, http_response=True):
    data = dict(zip(keys, values))
    if http_response is True:
        return HttpResponse(json.dumps(data))
    else:
        return data

def return_multi_key_json_rest_response(keys, values, rest_response=True, response_status=status.HTTP_200_OK):
    data = dict(zip(keys, values))

    error_description = list()
    if response_status != status.HTTP_200_OK:
        if 'errors' in data:
            for key, value in data['errors'].items():
                if type(value) is list:
                    for err in value:
                        error_description.append(err)
                else:
                    error_description.append(value)

        data['error_description'] = error_description if len(error_description) > 0 else ["Something went wrong"]

    if rest_response is True:
        return Response(data=data, status=response_status)
    else:
        return data


def handle_exception(exception_object=None, raise_exception=False, print_exception=False, http_response=True,
                     rest_response=False):
    errors = dict()
    errors['__all__'] = list()

    # logger = logging.getLogger(__name__)
    # logger.error(traceback.format_exc())

    if print_exception is True and settings.IS_PRODUCTION_SERVER is False:
        # print(traceback.format_exc())
        errors['__all__'].append(str(exception_object))
    else:
        errors['__all__'].append("Something Went Wrong")

    if raise_exception is True and exception_object is not None:
        raise exception_object

    if rest_response is True:
        return return_multi_key_json_rest_response(['errors'], [errors], rest_response,
                                                   response_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif http_response is True:
        return return_multi_key_json_response(['errors'], [errors], http_response)
    else:
        return return_multi_key_json_response(['errors'], [errors], http_response=False)


def float_to_integer(float_no):
    try:

        if float_no is None or str(float_no).strip() == "":
            return 0

        if float_no == 0:
            return 0
        if float_no/int(float_no) == 1:
            return int(float_no)
        else:
            return round(float_no, 2)
    except ZeroDivisionError:
        return float_no


def seconds_to_minutes_conversion(seconds):
    try:

        if seconds is None or str(seconds).strip() == "":
            # logger.warning("seconds_to_minutes_conversion function received seconds: %s" % seconds)
            return "0 min"

        minutes = int(seconds//60)
        remaining_seconds = seconds % 60
        remaining_seconds = float_to_integer(remaining_seconds)
        if minutes == 0:
            if remaining_seconds == 1:
                time_str = str(remaining_seconds) + ' sec'
            else:
                time_str = str(remaining_seconds) + ' secs'
        elif minutes == 1:
                if remaining_seconds == 0:
                    time_str = str(minutes) + ' min'
                elif remaining_seconds == 1:
                    time_str = str(minutes) + ' m ' + str(remaining_seconds) + ' s'
                else:
                    time_str = str(minutes) + ' m ' + str(remaining_seconds) + ' s'
        else:
            if remaining_seconds == 0:
                time_str = str(minutes) + ' mins'
            elif remaining_seconds == 1:
                time_str = str(minutes) + ' m ' + str(remaining_seconds) + ' s'
            else:
                time_str = str(minutes) + ' m ' + str(remaining_seconds) + ' s'
        return time_str
    except Exception as ex:
        # logger.warning("exception block:seconds_to_minutes_conversion function received seconds: %s" % seconds)
        handle_exception(exception_object=ex, raise_exception=False, print_exception=True)
        return "1 min"


