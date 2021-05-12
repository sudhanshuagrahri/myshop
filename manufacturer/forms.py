from django import forms
from .models import Dispatch, ProductDetails


class DispatchForm(forms.ModelForm):
    class Meta:
        model = Dispatch
        fields = ['courier_no', 'delivered_on', 'exchange']
        
class ProductDetailsForm(forms.ModelForm):
    class Meta:
        model = ProductDetails
        fields = ['category','product_name', 'selling_price', 'available', 'quantity', 'description', 'image']