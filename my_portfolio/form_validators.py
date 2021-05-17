from django.core.validators import RegexValidator
from django import forms


pincode_validator = RegexValidator(r'^[0-9]{6}$', 'Please provide a valid 6 digit pincode')

student_mobile_no_validator = RegexValidator(
    r'^[0-9]{10}$',
    'Please provide a valid 10 digit mobile number without any '
    'prefixes (+91 or 0), spaces and dashes.')


def password_validator(password):
    if password.find(' ') >= 0:
        raise forms.ValidationError('No spaces allowed in password')


def positive_integer_validator(value):
    if value < 0:
        raise forms.ValidationError('Value must be a positive integer')