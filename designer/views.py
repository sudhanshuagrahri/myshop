from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required, permission_required
from shop.models import Profile, Product
from manufacturer.models import ProductDetails
from django.template.defaultfilters import slugify


@login_required
@permission_required('designer.view_designerper', 'designer.add_designerper', 'designer.change_designerper' )
def manufacturer_list(request):
    grp = Group.objects.get(name='manufacturer')
    qs = grp.user_set.all()
    print(qs)
    # lis = []
    # for i in qs:
    #     dic = {}
    #     print(i.first_name)
    #     dic['id'] = i.id
    #     dic['first_name'] = i.first_name
    #     dic['last_name'] = i.last_name
    #     lis.append(dic)
    # print(lis)
    context={'qs': qs}
    return render(request, 'designer/manufacturer.html', context)

@login_required
@permission_required('designer.view_designerper', 'designer.add_designerper', 'designer.change_designerper' )
def manufacturer_detail(request, pk):
    qs = User.objects.get(pk=pk)
    print(qs.id)
    profile = Profile.objects.get(user_id=qs)
    print(profile)
    return render(request, 'designer/manufacturer_detail.html', {'qs': qs, 'profile': profile})

@login_required
@permission_required('designer.view_designerper', 'designer.add_designerper', 'designer.change_designerper' )
def manufacturer_products(request, pk):
    try:
        qs = ProductDetails.objects.filter(manufacturer=pk)
    except:
        qs = 'This manufacturer not uploaded the product!'

    return render(request, 'designer/product_list.html', {'qs': qs})

@login_required
@permission_required('designer.view_designerper', 'designer.add_designerper', 'designer.change_designerper' )
def product_approved(request, id):
    print(id)
    qs = ProductDetails.objects.filter(id=id)
    print('this: ',qs)
    qs.update(approved=True)
    for i in qs:
        Product.objects.create(name=i.product_name, slug=slugify(i.product_name) , image=i.image, category=i.category, manufacturer=i.manufacturer, description=i.description, price=i.selling_price, quantity=i.quantity, available=i.available)

    return render(request, 'designer/product_confirmation.html', {'context': 'You have successfully added the product to the inventory!'})

@login_required
@permission_required('designer.view_designerper', 'designer.add_designerper', 'designer.change_designerper' )
def product_decline(request, id):
    qs = ProductDetails.objects.filter(id=id)
    print(qs)
    qs.update(approved=False)
    return render(request, 'designer/product_confirmation.html', {'context': 'You have declined the product!'})
