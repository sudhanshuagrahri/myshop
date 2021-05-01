from django import forms
from django.contrib.auth.models import User
from .models import Master,Manufacturers,Designers



class DesignerForm(forms.ModelForm):
    class Meta:
        model = Designers
        fields = ['name','product_code','nop' ,'uplpics','desc' ,'price']

class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturers
        fields = ['name','Qty','Courier_number','comments']


class UserForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
