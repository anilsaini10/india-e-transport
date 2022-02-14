import email
import random
import string
import datetime
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash

from .models import Dealers_Form, Drivers_Form
from django.core.mail import send_mail
from django.contrib.auth.models import User


# Create your views here.

def home(request):

    all_vechicle = Drivers_Form.objects.all()

    context = {"all_vechicle": all_vechicle}

    return render(request, 'dealer/home.html', context)


def driver(request):

    if(request.method == 'POST'):
        email = request.POST.get('email')
        username = email
        name = request.POST.get('name')
        age = request.POST.get('age')
        contact = request.POST.get('contact')

        truck_number = request.POST.get('truck_number')
        truck_capacity = request.POST.get('truck_capacity')
        transporter_name = request.POST.get('truck_name')
        driving_experience = request.POST.get('driving_exp')
     
        city1 = request.POST.get('city1')
        state1 = request.POST.get('state1')
        city2 = request.POST.get('city2')
        state2 = request.POST.get('state2')
        city3 = request.POST.get('city3')
        state3 = request.POST.get('state3')

        if(Drivers_Form.objects.filter(email = email).exists()):
            old_user = Drivers_Form( username=username, email=email, name=name,age=age,contact=contact,
                                   truck_number=truck_number, truck_capacity=truck_capacity, transporter_name=transporter_name, driving_experience=driving_experience,
                                   city1=city1, city2=city2, city3=city3, state1=state1, state2=state2, state3=state3 )
            old_user.save()
            return render(request, 'dealer/home.html')
        else:
            new_user = Drivers_Form( username=username, email=email, name=name,age=age,contact=contact,
                                   truck_number=truck_number, truck_capacity=truck_capacity, transporter_name=transporter_name, driving_experience=driving_experience,
                                  city1=city1, city2=city2, city3=city3, state1=state1, state2=state2, state3=state3 )
            
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
            user = User.objects.create_user(username,email,password)
            user = authenticate ( username=email, password=password )
            login(request,user)
            return render(request, 'dealer/home.html')

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
            return render(request, 'dealer/home.html')
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
            user = User.objects.create_user(username,email,password)
            user = authenticate ( username=email, password=password )
            login(request,user)
            return render(request, 'dealer/home.html')


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