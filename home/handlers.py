from django.shortcuts import render
from django.urls import reverse
import my_portfolio.core_lib as core_lib
from django.http import Http404
from home.models import OperationType
from django.db.models import F
import home.models as home_models
import home.forms as home_forms
from django.http import HttpResponseServerError
from django.template.loader import render_to_string
from django.db import transaction
import datetime
import pytz
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

utc = pytz.UTC


# def create_edit_contact_renderer(request, operation, current_affairs_id=None):
#     errors = dict()
#     errors['__all__'] = list()
#     cv = dict()
#
#     try:
#         if operation == OperationType.CREATE:
#             pass
#
#         return render(request, 'contact/add_contact.html', {'cv': cv})
#
#     except Exception as ex:
#         core_lib.handle_exception(exception_object=ex, raise_exception=True, print_exception=True, http_response=True)


@transaction.atomic
def create_edit_delete_contact_handler(request, operation, contact_id=None):
    errors = dict()
    errors['__all__'] = list()
    try:
        cv = dict()
        print(request)

        form = home_forms.ContactForm(request.POST)
        if form.is_valid():
            if operation == OperationType.CREATE:
                contact_obj = home_models.ContactDetails(
                    name=form.cleaned_data.get('name'),
                    email=form.cleaned_data.get('email'),
                    subject=form.cleaned_data.get('subject'),
                    message=form.cleaned_data.get('message'),
                    created_on=timezone.now(),
                )
                contact_obj.save()

                return core_lib.return_multi_key_json_response(['success'],
                                                   ['Your message with the contact details have been successfully sent. Thank You!'])
        else:
            return core_lib.return_multi_key_json_response(['errors'], [form.errors])

    except Exception as ex:
        core_lib.handle_exception(exception_object=ex, raise_exception=True, print_exception=True, http_response=True)




