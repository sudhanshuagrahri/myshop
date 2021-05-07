from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import Designers,Master
from django.views.decorators.csrf import csrf_exempt
from .forms import DesignerForm,UserForm,MasterForm,



from django.contrib.auth.models import User


# Create your views here.


def masterpanel(r):
    users = Master.objects.all()
    return render(r,'usertables/base.html',{'ceo':'ceo page',
                                            'manu':'manufacturer page',
                                            'des':'designer page',
                                            'users':users})













def manufacturers(r):
    return render(r,'usertables/manufacturers/basepage.html',{})

def designers(r):
    a = Designers.objects.all()
    return render(r,'usertables/designers/list.html',{'a':a})









@csrf_exempt
def des(request):
    if request.method == 'POST':
        user_form = DesignerForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.save()
            return render(request,'usertables/designers/register_done.html',{'new_user': new_user})
    else:
        user_form = DesignerForm()
    return render(request,'usertables/designers/create.html',{'user_form': user_form})


@csrf_exempt
def manu(request):
    if request.method == 'POST':
        user_form = ManufacturerForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.save()
            return render(request,'usertables/manufacturers/register_done.html',{'new_user': new_user})
    else:
        user_form = ManufacturerForm()
    return render(request,'usertables/manufacturers/create.html',{'user_form': user_form})


@csrf_exempt
def masterenroll(request):
    if request.method == 'POST':
        user_form = MasterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.save()
            return render(request,'usertables/Master/register_done.html',{'new_user': new_user})
    else:
        user_form = MasterForm()
    return render(request,'usertables/Master/create.html',{'user_form': user_form})



