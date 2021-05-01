from django.db import models
from django.conf import settings
from shop.models import Product
from .forms import CartAddProductForm

class CartItem(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='UserCart')
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Items')
    quantity=models.IntegerField(default=1)
    override_quantity=models.BooleanField(default=False)
    
    def totPrice(self):
        return self.quantity * self.product.price
        
    def name(self):
        return self.product.name
        
    def itemUpdate(self):
        return (CartAddProductForm(initial={'quantity': self.quantity,'override':True}))
        
    def get_total_cost(self):
        cart= CartItem.objects.filter(user=self.user)
        return (sum(item.totPrice() for item in cart))