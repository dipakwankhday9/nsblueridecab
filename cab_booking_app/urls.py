from django.urls import path

from cab_booking_app.views import home,about,contact,base,packages,package_detail,categories,booking,payment,fleet,day_package1,day_package2,account_booking,driver_apply, gallery,testimonial

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('base/',base, name='base'),
    path('',home, name='home'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('packages/',packages, name='packages'),
    path('package_detail/<str:id>/',package_detail, name='package_detail'),
    path('categories',categories,name='categories'),
    path('booking/', booking,name='booking'),
    path('payment/', payment,name='payment'),
    path('fleet/',fleet),
    path('day_package1/', day_package1, name='day_package1'),
    path('day_package2/', day_package2, name='day_package2'),
    path('account_booking/', account_booking, name='account_booking'),
    path('driver_apply/', driver_apply, name='driver_apply'),
    path('gallery/', gallery, name='gallery'),
    path('testimonial/',testimonial, name='testimonial')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
