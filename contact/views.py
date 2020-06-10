from django.shortcuts import render,redirect
from django.core.mail import send_mail
import os

# Create your views here.
def sendmail(request):
    if request.method == "POST":
        prop_name = request.POST.get('property')
        agentmail = request.POST.get('agentmail').replace('/','')
        customer_name = request.POST.get('name')
        message = request.POST.get('message')
        property_id = request.POST.get('propertyid').replace('/','')
        customer_email = request.POST.get('email').replace('/','')

    send_mail(
        'New Property Listing',
        'You property ' + prop_name + ' has a new inquiry from '+ customer_name + ' & email' + customer_email + 'with the message '+ message,
        'hello@maxnimble.com',
        ['larteyelvis@outlook.com'],
        fail_silently=True
    )
    return redirect('/listings/'+property_id)