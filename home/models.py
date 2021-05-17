from django.db import models
from my_portfolio import core_lib
from django.utils import timezone


# Create your models here.

class OperationType:
    CREATE = 'C'
    EDIT = 'E'
    DELETE = 'D'


class ContactDetails(models.Model):
    id = models.CharField(max_length=24, primary_key=True, default=core_lib.generate_unique_object_id)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, db_index=True)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_on = models.DateTimeField(default=timezone.now, db_index=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_on', 'name']
        verbose_name_plural = 'Contact Details'

    def __str__(self):
        return f'Name: {self.name}  Email:{self.email}'

    @staticmethod
    def get_contact_details_by_id(contact_id):
        try:
            return ContactDetails.objects.get(id=contact_id)
        except ContactDetails.DoesNotExist:
            return None
