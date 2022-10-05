from django.contrib import admin
from .models import Userdata
# Register your models here.
@admin.register(Userdata)

class Userdetails(admin.ModelAdmin):
    list_display = ['username','email','password','conf_pass']