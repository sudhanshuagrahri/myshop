from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import Manufacturers,Designers,Master
from django.views.decorators.csrf import csrf_exempt
from .forms import DesignerForm,ManufacturerForm,UserForm



from django.contrib.auth.models import User



# Create your views here.
@csrf_exempt
def base(r):
    users = User.objects.all()
    return render(r,'usertables/base.html',{'users':users})


@csrf_exempt
def manufacturers(request):
    a = Manufacturers.objects.all()
    return render(request,'usertables/manufacturers/base32.html',{'a':a})



@csrf_exempt
def designers(r):
    a = Designers.objects.all()
    return render(r,'usertables/designers/base32.html',{'a':a})



@csrf_exempt
def locate(r):
    user_form = UserForm(r.POST)
    if user_form.is_valid():
        user_form.save()
        base(r)
    else:
        user_form = UserForm(r.POST)
    return render(r,'usertables/UserForm.html',{'uf':user_form})