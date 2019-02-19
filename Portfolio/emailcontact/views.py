from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms
from .forms import EmailContactForm
from .models import EmailContact

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *

import (
    'fmt'
    'github.com/sendgrid/sendgrid-go'
    'os'
)

# //////////////////////////////EmailContact////////////////////////////////

def email_contact(request):
    form = forms.EmailContactForm()
    dic_form = {'form':form}

    if request.method == 'POST':
        form = forms.EmailContactForm(request.POST)
        if form.is_valid():
            try:
                sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
                #grabing the essential information of the form to wrap it up in the sendgrid syntax
                #//////////////problem: ends up in junk inbox///////////////////////////////////
                from_email = Email(form.cleaned_data['from_email'])
                to_email = Email("Jan-frings@gmx.de")
                # to_email = User.objects.filter(is_active=True).values_list('email', flat=True)
                # this query gets necessary as soon as I'm activly putting out content for my users
                subject = form.cleaned_data['subject']
                content = Content("text/plain", form.cleaned_data['content'])
                #actual mail command through the sendgrid functionality
                mail = Mail(from_email, subject, to_email, content)
                response = sg.client.mail.send.post(request_body=mail.get())
                # print commands to review the process if needed
                # print(response.status_code)
                # print(response.body)
                # print(response.headers)
                return redirect('emailcontact:sending_success')
            except BadHeaderError:
                return HttpResponse('Bad Header found, please try again.')
    return render(request, 'emailcontact.html', dic_form)



def sending_success(request):
    return render(request, 'sending_success.html')
