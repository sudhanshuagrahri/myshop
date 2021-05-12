from django import forms
from .models import Person, SCategory, PromoCode, RefearlCode


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields =('grp', 'gender', 'phone_no', 'address', 'info')
        
class SCategoryForm(forms.ModelForm):
    class Meta:
        model = SCategory
        fields = ('subcategory',)
    
class PromoCodeForm(forms.ModelForm):
    class Meta:
        model = PromoCode
        fields = ('name', 'typeOfOrg', 'promocode', 'percentageOfDis', 'validUpto', 'info')
        
class RefearlCodeForm(forms.ModelForm):
    class Meta:
        model = RefearlCode
        fields = ('name', 'typeOf', 'code', 'points', 'validUpto', 'info')