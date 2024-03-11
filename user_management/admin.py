from re import I
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user_management.models import CustomUser
# Register your models here.
class UserModel(UserAdmin):
    list_display = ['username', 'user_type']
admin.site.register(CustomUser, UserModel)
