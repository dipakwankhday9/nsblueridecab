from email.policy import default
from django.db import models
from datetime import datetime, date
from uuid import UUID
from django.utils import timezone

from django.utils.text import slugify
from autoslug import AutoSlugField

from ckeditor.fields import RichTextField

# Create your models here.

class Journey_type(models.Model):
    journey_type = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.journey_type


class Categories(models.Model):
    cat_img = models.ImageField(upload_to='media/categories/cat_image/%y%m%d/')
    cat_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.cat_name
    
class Package(models.Model):
    STATUS = (('Publish','Publish'),('Draft','Draft'))
    status = models.CharField(choices=STATUS, max_length=100)
    package_name = models.CharField(max_length=200)
    package_day = models.CharField(max_length=200, default ='1', blank=True, null=True)
    package_img = models.ImageField(upload_to='media/package/package_image/%y%m%d/')
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    # description = models.TextField()
    description = RichTextField(null=True, blank=True)
    journey_type = models.ForeignKey(Journey_type,on_delete=models.CASCADE , null=True,blank=True)
    
       
    def __str__(self) -> str:
        return self.package_name
    

class Car_type(models.Model):
    car_type = models.CharField(max_length=200)
    rate = models.CharField(max_length=200,blank=True,null=True)
    extra_per_km = models.CharField(max_length=50,blank=True,null=True)
    day_package = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self) -> str:
        return self.car_type
    
class Car(models.Model):
    STATUS = (
        ('publish', 'publish'),
        ('draft', 'draft'),
    )
    FACILITY = (('AC','AC'),
                ('Non AC','Non AC'))
    package = models.ForeignKey(Package , on_delete = models.CASCADE)
    car_name = models.CharField(max_length = 200)
    car_img = models.ImageField(upload_to='media/car/car_image/%y%m%d/', blank=True, null=True)
    car_type = models.ForeignKey(Car_type, on_delete=models.CASCADE)
    seat_capacity = models.CharField(max_length = 30,blank=True, null=True )
    car_facility = models.CharField(choices= FACILITY,max_length=50,null=True, blank=True, default = 'AC')
    status = models.CharField(choices=STATUS, max_length=100, null=True,blank=True)
    bag = models.CharField(max_length = 20, null=True,blank=True, default = '2')

    def __str__(self) -> str:
        return self.car_name


# package Include Exclude
class Package_include(models.Model):
    include_items = models.CharField(max_length=300, null=True,blank=True)
    package = models.ForeignKey(Package , on_delete = models.CASCADE)


class Package_exclude(models.Model):
    exclude_items = models.CharField(max_length=300,null=True,blank=True)
    package = models.ForeignKey(Package , on_delete = models.CASCADE)



class Contact(models.Model):
    full_name = models.CharField(max_length = 200)
    email = models.EmailField()
    contact = models.CharField(max_length=12)
    message = models.TextField()

    def __str__(self) -> str:
        return self.full_name
    


class Booking(models.Model):
    
    booking_id = models.IntegerField(unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    pick_up_location = models.CharField(max_length=500)
    drop_off_location = models.CharField(max_length=500)
    pick_up_date =models.CharField(max_length = 70)
    pick_up_time =models.CharField(max_length = 70)
    return_date =models.CharField(max_length = 70)
    return_time =models.CharField(max_length = 70)
    car_type = models.ForeignKey(Car_type, on_delete=models.CASCADE,blank=True, null=True)
    journey_type = models.ForeignKey(Journey_type,on_delete=models.CASCADE,blank=True, null=True)
    contact = models.CharField(max_length = 20, default = '123456789')
    email = models.EmailField(default='email@email.com')
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null= True)
    updated_date = models.DateTimeField(auto_now=True,blank=True, null= True)


    def save(self,*args,**kwargs):
        if self.booking_id is None and self.created_date and self.booking_id:
            self.booking_id = self.created_date.strftime('000%y%m%d00') + str(self.booking_id)
        return super().save(*args,**kwargs)
    
    def __str__(self) -> str:
        return self.first_name
    

class Driver_apply(models.Model):
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    email = models.EmailField()
    contact = models.CharField(max_length=12)
    city = models.CharField(max_length = 60)
    car_name = models.CharField(max_length = 60)
    car_registration = models.FileField(upload_to='media/driver_document/car_registration/%Y-%m-%d')
    driver_license_front = models.FileField(upload_to='media/driver_document/driver_license_front/%Y-%m-%d')
    driver_license_back = models.FileField(upload_to='media/driver_document/driver_license/%Y-%m-%d')
    aadhar_front = models.FileField(upload_to='media/driver_document/aadhar_card/%Y-%m-%d')
    aadhar_back = models.FileField(upload_to='media/driver_document/aadhar_card/%Y-%m-%d')
    car_permit = models.FileField(upload_to='media/driver_document/car_permit/%Y-%m-%d')
    car_insurance = models.FileField(upload_to='media/driver_document/car_insurance/%Y-%m-%d')
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null= True)
    updated_date = models.DateTimeField(auto_now=True,blank=True, null= True)




    def __str__(self) -> str:
        return self.first_name


class Photo(models.Model):
    title = models.CharField(max_length = 200, blank=True, null=True)
    image = models.ImageField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null= True)
    updated_date = models.DateTimeField(auto_now=True,blank=True, null= True)

class Testimonial(models.Model):
    title = models.CharField(max_length = 200, blank=True, null=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    customer_name = models.CharField(max_length = 200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null= True)
    updated_date = models.DateTimeField(auto_now=True,blank=True, null= True)

   
   