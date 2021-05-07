from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse
# Create your models here.





class Master(models.Model):
    TARGET = [
        ('ceo','CEO'),
        ('manufacturer','Manufacturer'),
        ('designer','Designer')
    ]
    name = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField()
    role = models.CharField(max_length=20,blank=True,primary_key=True,choices=TARGET)
    mobile = models.IntegerField(blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    info = models.TextField(blank=True,null=True)
    s_status = models.BooleanField(default=False,blank=True,null=True)





    def __str__(self):
        return self.name




class Designers(models.Model):
    name = models.CharField(max_length=10,blank=True)
    number_of_pics = models.IntegerField(default=0,blank=True)
    imgs = models.ImageField(upload_to='products',blank=True)
    uplpics = models.BooleanField(default=True,blank=True)
    desc = models.TextField(blank=True)
    email = models.EmailField(blank=True)


    def __str__(self):
        return self.name






