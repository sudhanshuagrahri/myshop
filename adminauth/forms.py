from django import forms
from django.contrib.auth.models import User
from .models import Master,Designers

class MasterForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = ('name','email','role','mobile','address','info','s_status')

class DesignerForm(forms.ModelForm):
    class Meta:
        model = Designers
        fields = ('id','name','number_of_pics' ,'uplpics','desc','imgs')






class UserForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
