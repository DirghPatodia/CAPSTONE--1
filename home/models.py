from django.db import models

# Create your models here.
class Userdata(models.Model):
     username= models.CharField(max_length=30)
     email= models.EmailField()
     password= models.CharField(max_length=30)
     conf_pass = models.CharField(max_length=30)