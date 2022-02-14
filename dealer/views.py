import email
import random
import string
import datetime
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash

from .models import Dealers_Form, Drivers_Form
from django.core.mail import send_mail


# Create your views here.

def home(request):
    return render(request, 'dealer/home.html')


def driver(request):

    if(request.method == 'POST'):
        email = request.POST.get('email')
        name = request.POST.get('name')
        contact = request.POST.get('contact')
    return render(request, 'dealer/driver-form.html')


def dealer(request):

    if(request.method == 'POST'):
        email = request.POST.get('email')
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        nature_of_material = request.POST.get('nature_of_material')
        weight_of_material = request.POST.get('weight_of_material')
        quantity = request.POST.get('quantity')
        city = request.POST.get('city')
        state = request.POST.get('state')

        username = email

        if(Dealers_Form.objects.filter(username = username).exists()):
            old_user = Dealers_Form(username=username, name=name, email=email,contact=contact,
            nature_of_material=nature_of_material,weight_of_material=weight_of_material,
            quantity=quantity,city=city, state=state)
            old_user.save()
        else:
            new_user = Dealers_Form(username=username, name=name, email=email, contact=contact,
            nature_of_material=nature_of_material,weight_of_material=weight_of_material,
            quantity=quantity,city=city, state=state)

            characters = string.ascii_letters + string.digits
            password = ''.join ( random.choice ( characters ) for i in range ( 8 ) )
            send_mail(
                'Login Credentials',
                password,
                'from@example.com',
                [email],
                fail_silently=False,
                )
            # new_user.set_password(password)
            new_user.save()
            
            user = authenticate ( username=email, password=password )
            login(request,user)


    return render(request, 'dealer/dealer-form.html')



def signin(request):
    if(request.method == 'POST'):
        username = request.POST.get('email')
        password = request.POST.get('password')

        if(Dealers_Form.objects.filter(username=username).exists() 
           or Drivers_Form.objects.filter(username=username).exists()):
           login(username, password)
        else:
            return render(request, 'dealer/login.html')
    return render(request, 'dealer/login.html')   

def signout(request):
    logout(request)
    return render(request, 'dealer/login.html')