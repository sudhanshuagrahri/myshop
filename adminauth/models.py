
from django.db import models

# Create your models here.


class Master(models.Model):
    name = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(default='uremail@gmail.com')
    role = models.CharField(max_length=20,blank=True,null=True)




    def __str__(self):
        return self.name


class Designers(models.Model):
    name = models.CharField(max_length=10)
    product_code = models.CharField(max_length=10)
    nop = models.IntegerField(default=0)
    uplpics = models.BooleanField(default=True)
    desc = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    #Promo_appl = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Manufacturers(models.Model):
    name = models.CharField(primary_key=True,max_length=20)
    Qty = models.IntegerField(default=0)
    TimeFrame = models.DateTimeField(auto_now=True)
    Courier_number = models.IntegerField(default=0)
    Dated = models.DateField(auto_now=True,blank=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.name





