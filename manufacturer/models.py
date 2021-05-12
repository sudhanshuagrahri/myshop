from django.db import models
from order.models import OrderCustItem
from django.contrib.auth.models import User
from shop.models import Category
# Create your models here.

class Dispatch(models.Model):
    order_id = models.ForeignKey(OrderCustItem,
                              related_name='dispatch',
                              on_delete=models.CASCADE)
                              
    sent_on= models.DateTimeField(auto_now_add=True)
    courier_no=models.CharField(max_length=200)
    delivered_on= models.DateField()
    filled= models.BooleanField(default=False)
    exchange= models.BooleanField(default=False)
    
class ProductDetails(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    manufacturer = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    available = models.BooleanField(default=False)
    approved = models.BooleanField(null=True)

    def __str__(self):
        return self.product_name
