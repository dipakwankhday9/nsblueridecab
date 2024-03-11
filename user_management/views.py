from django.shortcuts import render, redirect, HttpResponse
from user_management.EmailBackEnd import EmailBackEnd, ModelBackend
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user_management.models import CustomUser

from cab_booking_app.models import Driver_apply


# Create your views here.

def LOGIN(request):
    return render(request, 'user_management/login.html')


def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))

        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                # return HttpResponse("Hod Home")
                return redirect('hod_home')
            elif user_type == '2':
                return HttpResponse("Driver")
                # return redirect('driver_home')
            elif user_type == '3':
                return HttpResponse("Customer")
                # return redirect('student_home')
            else:
                messages.error(request, 'Incorrect Email or Password')
                return redirect('login')    
        else:
            messages.error(request, 'Incorrect Email or Password')
            return redirect('login')
        

def do_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/')
def hod_home(request):
    return render(request, 'user_management/hod_home.html')

def user_base(request):
    return render(request, 'user_management/base/base.html')


def driver_details(request):
    driver_data = Driver_apply.objects.all()
    print(driver_data)
    context ={
        'driver_data':driver_data
    }
    return render(request, 'user_management/driver_detail.html',context)

