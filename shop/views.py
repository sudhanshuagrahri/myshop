from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Profile
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import HttpResponse
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm, ProfileRegistrationForm, LoginForm
from cart.forms import CartAddProductForm
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import login, authenticate
from django.contrib.contenttypes.models import ContentType



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
                                
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                  'cart_product_form': cart_product_form})


def loginUser(request):
    if request.method == 'POST':
        # print(request.POST.get('username'))
        form = LoginForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            # print(user)
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            print('-----',user)
            # if request.user.Group.all()[0] == 'customer':
            #     print('here')
            if user is not None:
                if user.is_active:
                    login(request, user)
                    
                    if str(request.user.groups.all()[0]) == 'superadmin':
                        pass
                    elif str(request.user.groups.all()[0]) == 'master':
                        return redirect('master:registerPerson')

                    elif str(request.user.groups.all()[0]) == 'manufacturer':
                        return redirect('manufacturer:create_products')

                    elif str(request.user.groups.all()[0]) == 'designer':
                        return redirect('designer:manufacturer_list')
                        
                    else:
                        return redirect('shop:product_list')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
            return redirect('shop:login')
    else:
        form = LoginForm()
    return render(request,'registration/login.html', {'form':form})



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form=ProfileRegistrationForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():

            # Create a new user object but avoid saving it yet
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
            my_group = Group.objects.get(name='customer')
            my_group.user_set.add(new_user)

            content_type = ContentType.objects.get_for_models(Product, Profile, Category)
            con = list(content_type.values())
            per1 = Permission.objects.get(codename="view_category", content_type=con[0])
            per2 = Permission.objects.get(codename="view_product", content_type=con[1])
            per3 = Permission.objects.filter(content_type=con[2])
            new_user.user_permissions.add(per1)
            new_user.user_permissions.add(per2)
            for permission in per3:
                new_user.user_permissions.add(permission)
            return render(request,'shop/account/register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileRegistrationForm()
    return render(request,'shop/account/register.html',{'user_form': user_form,'profile_form': profile_form})


@permission_required('shop.change_profile')
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'shop/account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})

