from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PersonForm, SCategoryForm, PersonForm, PromoCodeForm, RefearlCodeForm
from shop.forms import UserRegistrationForm
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from manufacturer.models import Dispatch, ProductDetails


@login_required
def registerPerson(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form=PersonForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():

            # Create a new user object but avoid saving it yet
            if str(profile_form.cleaned_data['grp']) != "master" and str(profile_form.cleaned_data['grp']) != "superadmin" and str(profile_form.cleaned_data['grp']) != "customer":
                new_user = user_form.save(commit=False)
                p_user = profile_form.save(commit=False)

                # Set the chosen password
                new_user.set_password(user_form.cleaned_data['password'])

                # Save the User object
                new_user.save()
                p_user.user=new_user

                # Create the user profile
                #Profile.objects.create(user=new_user,)
                p_user.save()
                my_group = Group.objects.get(name=p_user.grp)
                my_group.user_set.add(new_user)
                if str(p_user.grp) == "manufacturer":
                    content_type = ContentType.objects.get_for_models(Dispatch, ProductDetails)
                    con = list(content_type.values())
                    per1 = Permission.objects.filter(content_type=con[0])
                    per2 = Permission.objects.filter(content_type=con[1])
                    for permission in per1:
                        new_user.user_permissions.add(permission)
                    for permission in per2:
                        new_user.user_permissions.add(permission)
                elif str(p_user.grp) == "designer":
                    per1 = Permission.objects.get(codename="view_designerper")
                    per2 = Permission.objects.get(codename="add_designerper")
                    per3 = Permission.objects.get(codename="change_designerper")
                    per4 = Permission.objects.get(codename="delete_designerper")
                    new_user.user_permissions.add(per1)
                    new_user.user_permissions.add(per2)
                    new_user.user_permissions.add(per3)
                    new_user.user_permissions.add(per4)           
                
                
                return render(request,'shop/account/register_done.html',{'new_user': new_user})
                return render(request,'master/add/appointed.html',{'new_user': new_user})
            else:
                user_form = UserRegistrationForm()
                profile_form = PersonForm()
                message = "You have no permissions to assigned this role!"
                return render(request,'master/add/appoint.html',{'user_form': user_form,'profile_form': profile_form, 'message': message})
    else:
        user_form = UserRegistrationForm()
        profile_form = PersonForm()
    return render(request,'master/add/appoint.html',{'user_form': user_form,'profile_form': profile_form})
    

@login_required    
def addPC(request):
    if request.method == 'POST':
        promoCode_form=PromoCodeForm(request.POST)
        if promoCode_form.is_valid():

            # Create a new user object but avoid saving it yet
            promoCode= promoCode_form.save(commit=True)
            return render(request,'master/add/PCodeAdded.html')
    else:
        promoCode_form=PromoCodeForm()
    return render(request,'master/add/PCodeAdd.html',{'promoCode_form': promoCode_form})

@login_required    
def addRC(request):
    if request.method == 'POST':
        refearlCode_form=RefearlCodeForm(request.POST)
        if refearlCode_form.is_valid():

            # Create a new user object but avoid saving it yet
            refearlCode= refearlCode_form.save(commit=True)
            return render(request,'master/add/RCodeAdded.html')
    else:
        refearlCode_form=RefearlCodeForm()
    return render(request,'master/add/RCodeAdd.html',{'refearlCode_form': refearlCode_form})