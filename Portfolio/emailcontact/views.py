from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms
from .forms import EmailContactForm
from .models import EmailContact


# //////////////////////////////EmailContact////////////////////////////////

def email_contact(request):

    form = forms.EmailContactForm()
    dic_form = {'form':form}

    if request.method == 'POST':
        form = forms.EmailContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['Jan-frings@gmx.de'])
            except BadHeaderError:
                return HttpResponse('Bad Header found, please try again.')
            return redirect('emailcontact:sending_success')

    return render(request, 'emailcontact.html', dic_form)

def sending_success(request):
    return HttpResponse('Sending successfull. Thank you for your message!')
