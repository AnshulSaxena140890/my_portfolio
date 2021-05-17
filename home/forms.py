from django import forms
from my_portfolio import core_lib
import datetime


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=3, error_messages={
        'required': 'Please provide your name.',
        'max_length': 'Name should not exceed 100 characters.',
        'min_length': 'Name should have atleast 10 characters.'
    })

    subject = forms.CharField(max_length=150, min_length= 10, error_messages={
        'required': 'Please provide a subject.',
        'max_length': 'Subject should not exceed 150 characters.',
        'min_length': 'Subject should have atleast 10 characters.'
    })

    message = forms.CharField(max_length=500, min_length=10, error_messages={
        'required': 'Please provide a subject.',
        'max_length': 'Message should not exceed 500 characters.',
        'min_length': 'Message should have atleast 10 characters.'
    })

    email = forms.EmailField(max_length=200, error_messages={
        'required': 'Please provide a subject.',
        'max_length': 'Email should not exceed 500 characters.',
        'invalid': 'Please enter a valid email'
    })