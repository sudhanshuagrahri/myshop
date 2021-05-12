from django.db import models
from django.conf import settings
from shop.models import Category
from django.urls import reverse
from django.contrib.auth.models import Group

class Person(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)   
    grp = models.ForeignKey(Group, on_delete=models.CASCADE) 
    gender = models.CharField(max_length=10,
                              choices=GENDER_CHOICES,
                              default='male')
    phone_no = models.CharField(max_length=12)
    address = models.TextField(blank=True,null=True)
    info = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.user.first_name

class SCategory(models.Model):
    subcategory = models.ForeignKey(Category, related_name='assigned', on_delete=models.CASCADE)
    person = models.ForeignKey(Person,related_name='produces', on_delete=models.CASCADE)
    
    
class PromoCode(models.Model):
    name = models.CharField(max_length=20)
    typeOfOrg = models.CharField(max_length=50)
    promocode = models.CharField(max_length=20, unique=True)
    percentageOfDis = models.DecimalField(default=0,max_digits=4, decimal_places=2)
    validUpto = models.DateField()
    info = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name
        
class RefearlCode(models.Model):
    name = models.CharField(max_length=20)
    typeOf = models.CharField(max_length=50)
    code = models.CharField(max_length=20, unique=True)
    points = models.IntegerField(default=0)
    validUpto = models.DateField()
    info = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name
    