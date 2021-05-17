from django.urls import path, re_path
from home import views

app_name = "home"
urlpatterns = [
    path('create-contact/', views.CreateContactView.as_view(), name='create-contact'),
]