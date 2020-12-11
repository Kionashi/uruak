""" Home views. """
# Django
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from io import BytesIO
from django.template.loader import get_template, render_to_string
from django.db import transaction
import os


def home(request):
    """ Load home view """
    context = {}
    return render(request, 'index.html', context)

def about(request):
    """ Load about view """
    context = {}
    return render(request, 'about.html', context)

def contact(request):
    """ Load contact view """
    if request.method == 'POST':
        context = {
            'email': request.POST['email'],
            'name': request.POST['name'],
            'message': request.POST['message']
        }
        message = render_to_string('emails/contact.html', context, request=request)
        subject = '[Contacto Uruak]'+request.POST['subject']
        email_address = 'luisdabe@gmail.com'
        email = EmailMessage(subject, message, 'cardozo.anibal@gmail.com', [email_address])
        email.content_subtype = 'html'
        email.send()
    context = {}
    return render(request, 'contact.html', context)

def products(request):
    """ Load products view """
    context = {}
    return render(request, 'products.html', context)

