from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib import messages
from cab_booking_app.models import Booking, Car, Car_type, Contact,Categories, Driver_apply, Journey_type,Package,Photo,Testimonial

from django.db.models import Max

from django.core.mail import send_mail

from django.core.mail import send_mail,EmailMultiAlternatives
from tourism_project.settings import EMAIL_HOST_USER

from django.http import Http404

# Create your views here.
def base(request):
    return render(request,'base/base.html')

def fleet(request):
    car = Car.objects.all()
    print(car)

    context ={
        'car':car
    }
    return render(request,'cab_booking_app/fleet.html', context)

def home(request):
#     send_mail(
#     "Testing Mail",
#     "Wel Come To NS Blue Ride Cab",
#     "nsblueridecab@gmail.com",
#     ["dmrudeep26@gmail.com"],
#     fail_silently=False,
# )
    
    category = Categories.objects.all()
    cat_count = Categories.objects.all().count()
    print(cat_count)
    car = Car.objects.all()[:8]
    # print(car)
    package = Package.objects.all()[:6]

    package_day1 = Package.objects.filter(package_day =1)[:6]
    # print("Package day1",package_day)

    package_day2 = Package.objects.filter(package_day = 2)[:6]

    testimonial = Testimonial.objects.all()[:3]

    context ={
        'category':category,
        'cat_count':cat_count,
        'car':car,
        'package':package,
        'package_day1': package_day1,
        'package_day2':package_day2,
        'testimonial':testimonial
    }
    return render(request,'cab_booking_app/home.html', context)
    
def day_package1(request):
    
    package_day1 = Package.objects.filter(package_day = 1)
    print("Package day1",package_day1)


    context ={
        'package_day1': package_day1
    }
    return render(request,'cab_booking_app/day_package1.html', context)

def day_package2(request):
    
    package_day2 = Package.objects.filter(package_day = 2)
    print("Package day1",package_day2)


    context ={
        'package_day2': package_day2
    }
    return render(request,'cab_booking_app/day_package2.html', context)

def categories(request):
    
    category = Categories.objects.all()
    cat_count = Categories.objects.all().count()

    
    context ={
        'category':category,
        'cat_count':cat_count
    }
    return render(request,'cab_booking_app/categories.html', context)




def packages(request):
    package = Package.objects.filter(status ='Publish')
    cat_id = request.GET.get('category')
    if cat_id:
        package = Package.objects.filter(categories =cat_id)
    else:
        package = Package.objects.filter(status ='Publish')

    
    
    context = {
        'package':package,
        
    }
    return render(request,'cab_booking_app/packages.html', context)

def package_detail(request, id):
    pack_detail = Package.objects.filter(id= id).first()
    print(pack_detail)
    
    context ={
        'pack_detail': pack_detail,
       
    }
    return render(request,'cab_booking_app/package_detail.html', context)

def about(request):
    return render(request,'cab_booking_app/about.html')

def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        message = request.POST.get('message')

        contact_data =Contact(full_name=full_name,contact=contact,email=email,message=message)

        contact_data.save()
        messages.success(request,"Your message sent successfully")

        send_mail("NS Blue Ride Cab: ",f"We have received your message and would like to thank you for writing to us. If your inquiry is urgent, please use this 9370702118 telephone number to talk to one of our staff members. ",EMAIL_HOST_USER,[email],fail_silently=True)
        # return redirect('home')

    return render(request,'cab_booking_app/contact.html')


def booking(request):
    car_type =  Car_type.objects.all()
    journey_type = Journey_type.objects.all()
   
    if request.method == "POST":
        booking_id = request.POST.get('booking_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('phone')
        pick_up_location = request.POST.get('pick_up_location')
        drop_off_location = request.POST.get('drop_off_location')
        pick_up_date = request.POST.get('pick_up_date')
        pick_up_time = request.POST.get('pick_up_time')
        return_date = request.POST.get('return_date')
        return_time = request.POST.get('return_time')
        journey_id = request.POST.get('journey_id')
        car_id = request.POST.get('car_id')


        journey_id = Journey_type.objects.get(id = journey_id)
        car_id = Car_type.objects.get(id = car_id)

        booking_data = Booking(first_name=first_name,last_name=last_name,email=email,contact=contact,pick_up_location=pick_up_location, drop_off_location= drop_off_location,pick_up_date=pick_up_date, pick_up_time= pick_up_time,return_date=return_date,return_time=return_time,journey_type = journey_id, car_type=car_id, booking_id= booking_id )

        

        booking_data.save()
        print(booking_data)
        return redirect('payment')
        # messages.success(request,"Your booking confirmed successfully")

    context ={
        'car_type':car_type,
        'journey_type':journey_type
    }    

    return render(request, 'cab_booking_app/booking.html',context)

def payment(request):
    return render(request,'cab_booking_app/payment.html')


def account_booking(request):
      account_booking = Booking.objects.all()

      context ={
          'account_booking':account_booking
      }
      return render(request,'cab_booking_app/account_booking.html',context)


def driver_apply(request):
      if request.method == 'POST':
          first_name = request.POST.get('first_name')
          last_name = request.POST.get('last_name')
          email = request.POST.get('email')
          contact = request.POST.get('contact')
          city = request.POST.get('city')
          car_name = request.POST.get('car_name')
          car_registration = request.FILES.get('car_registration')
          driving_license_front = request.FILES.get('driving_license_front')
          driving_license_back = request.FILES.get('driving_license_back')
          aadhar_front = request.FILES.get('aadhar_front')
          aadhar_back = request.FILES.get('aadhar_back')
          car_permit = request.FILES.get('car_permit')
          car_insurance = request.FILES.get('car_insurance')

          driver_data = Driver_apply(first_name = first_name, last_name = last_name, email = email, contact=contact, city=city, car_name=car_name, car_registration=car_registration,   driver_license_front= driving_license_front,  driver_license_back=driving_license_back, aadhar_front=aadhar_front,  aadhar_back= aadhar_back, car_permit=car_permit,car_insurance=car_insurance)

          print(driver_data)

          driver_data.save()

          messages.success(request, first_name + " " + last_name + " " + "Are Data Send Successfully Our Team Contact Soon" )


      context ={
         
      }
      return render(request,'cab_booking_app/driver_apply.html',context)


def gallery(request):
    image = Photo.objects.all()
    context ={
        'image':image
    }
    return render(request,'cab_booking_app/gallery.html',context)

def testimonial(request):
    testimonial = Testimonial.objects.all()
    context ={
        'testimonial':testimonial
        
    }
    return render(request,'cab_booking_app/testimonial.html',context)
