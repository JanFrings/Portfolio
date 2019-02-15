from django.urls import path
from . import views

app_name = 'emailcontact'

urlpatterns=[
    path('', views.email_contact, name='email_contact' ),
    path('sending/success', views.sending_success, name='sending_success'),
]
