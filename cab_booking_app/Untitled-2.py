
class Destination_categories(models.Model):
    cat_img = models.ImageField(upload_to='categories/cat_image/%y%m%d/')
    cat_name = models.CharField(max_length=200)
    time_stamp = models.DateTimeField(auto_now_add =True)
    update_time = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.cat_name

class Vehicle_type(models.Model):
    car_type_name = models.CharField(max_length= 200)
    vehicle_img = models.ImageField(upload_to='vehicle/vehicle_image/%y%m%d/')

    def __str__(self) -> str:
        return self.car_type_name



class Car_details(models.Model):
    STATUS = (
        ('publish', 'publish'),
        ('draft', 'draft'),
    )
    FACILITY = (('AC','AC'),
                ('Non AC','Non AC'))
    
    car_name = models.CharField(max_length=200)
    car_img = models.ImageField(upload_to='car/car_image/%y%m%d/', blank=True, null=True)
    vehicle_type = models.ForeignKey(Vehicle_type, on_delete=models.CASCADE)
    car_model = models.CharField(max_length = 200, blank=True, null=True)
    seat_capacity = models.CharField(max_length=20, default=4, blank=True, null=True)
    car_facility = models.CharField(choices= FACILITY,max_length=50,null=True, blank=True, default = 'AC')
    status = models.CharField(choices=STATUS, max_length=100, null=True,blank=True)
    bag = models.CharField(max_length = 20, null=True,blank=True, default = '2')

    def __str__(self) -> str:
        return self.car_name


# package Include Exclude
class Package_include(models.Model):
    include_items = models.CharField(max_length=300, null=True,blank=True)

    def __str__(self) -> str:
        return self.include_items


class Package_exclude(models.Model):
    exclude_items = models.CharField(max_length=300,null=True,blank=True)

    def __str__(self) -> str:
        return self.exclude_items



class Package_booking(models.Model):
    STATUS = (
        ('publish', 'publish'),
        ('draft', 'draft'),
    )
    status = models.CharField(choices=STATUS, max_length=100, null=True,blank=True)
    package_name = models.CharField(max_length = 200)
    vehicle_type = models.ForeignKey(Vehicle_type,  on_delete=models.CASCADE)
    contact = models.CharField(max_length = 15)
    pickup_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    pickup_time = models.TimeField(auto_now_add=False, auto_now=False, blank=True)
    return_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    return_time = models.TimeField(auto_now_add=False, auto_now=False, blank=True)

    def __str__(self) -> str:
        return self.package_name
