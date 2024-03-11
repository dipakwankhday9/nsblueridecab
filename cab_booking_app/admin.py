from django.contrib import admin
from cab_booking_app.models import Contact,Categories,Package,Car,Car_type,Package_exclude,Package_include,Booking,Journey_type,Driver_apply,Photo,Testimonial
# Register your models here.



admin.site.site_header = "NS Blue Ride Cab"

admin.site.site_title = "NS Blue Ride Cab"

admin.site.index_title = "NS Blue Ride Cab"

# @admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','email','contact','message']


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id','cat_img','cat_name']

# class PackageAdmin(admin.ModelAdmin):
#     list_display = ['id', 'package_name','package_km','package_img','categories','description']



class Package_includeTabularInline(admin.TabularInline):
    model=Package_include

class Package_excludeTabularInline(admin.TabularInline):
    model = Package_exclude

class CarTabularInline(admin.TabularInline):
    model = Car



class  PackageAdmin(admin.ModelAdmin):
    inlines = [Package_excludeTabularInline,Package_includeTabularInline, CarTabularInline]


admin.site.register(Booking)
admin.site.register(Car)
admin.site.register(Car_type)

admin.site.register(Package_exclude)
admin.site.register(Package_include)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Categories,CategoriesAdmin)
admin.site.register(Package,PackageAdmin)
admin.site.register(Journey_type)
admin.site.register(Driver_apply)
admin.site.register(Photo)
admin.site.register(Testimonial)