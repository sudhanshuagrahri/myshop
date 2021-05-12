from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from order.models import OrderCustItem
from .models import Dispatch
from .forms import DispatchForm, ProductDetailsForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('manufacturer.view_productdetails', 'manufacturer.add_productdetails', 'manufacturer.change_productdetails')
def show_order(request):
    products=OrderCustItem.objects.filter(product__manufacturer=request.user)
    
    return render(request,'manufacturer/order/show.html',{'products': products})

@login_required
@permission_required('manufacturer.view_productdetails', 'manufacturer.add_productdetails', 'manufacturer.change_productdetails')
def dispatch_order(request, id=None):
    #order_id=17
    orderCustItem=OrderCustItem.objects.get(order_id=id)
    if request.method == 'POST':
        dispatch_form = DispatchForm(request.POST)
        if dispatch_form.is_valid():
            new_dispatch = dispatch_form.save(commit=False)
            new_dispatch.filled=True
            new_dispatch.order_id=orderCustItem.order_id
            new_dispatch.save()
           
            return render(request,'manufacturer/order/filled.html',{'new_dispatch': new_dispatch})
    else:
        dispatch_form = DispatchForm()
        print(id)
        try:
            dispatched=Dispatch.objects.get(order_id__order__id=id)
            return render(request,'manufacturer/order/fill.html',{'dispatch_form': dispatch_form, 'dispatched':dispatched})
        except:
            pass
    return render(request,'manufacturer/order/fill.html',{'dispatch_form': dispatch_form})
    
@login_required
@permission_required('manufacturer.view_productdetails', 'manufacturer.add_productdetails', 'manufacturer.change_productdetails')
def create_products(request):
    # order_id=17
    if request.method == 'POST':
        productDetails_form = ProductDetailsForm(request.POST, request.FILES)
        # print(productDetails_form)
        if productDetails_form.is_valid():
            new_productDetails = productDetails_form.save(commit=False)
            print(new_productDetails)
            new_productDetails.manufacturer=request.user
            new_productDetails.save()
            return render(request,'manufacturer/product/added.html')
    else:
        productDetails_form = ProductDetailsForm()
    return render(request,'manufacturer/product/add.html',{'productDetails_form': productDetails_form})

