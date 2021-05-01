from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .models import CartItem
from .forms import CartAddProductForm
from django.contrib.auth.decorators import login_required

@login_required
@require_POST
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    j=True
    try:
       cart =CartItem.objects.get(user=request.user,product=product)
    except:
        j= False
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        if j:
            cart.quantity=cd['quantity']
            cart.save()
        else:
            CartItem.objects.create(user=request.user,product=product,quantity=cd['quantity'],override_quantity=cd['override'],)
        #cart.add(product=product,quantity=cd['quantitoverride_quantity=cd['override'])
    return redirect('cart:cart_detail')

@login_required
@require_POST
def cart_remove(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart= CartItem.objects.filter(user=request.user,product=product)
    cart.delete()
    #cart.remove(product)
    return redirect('cart:cart_detail')

@login_required
def cart_detail(request):
    cart= CartItem.objects.filter(user=request.user)
    sum= 0
    for item in cart:
            sum= sum + item.totPrice()
    return render(request, 'cart/detail.html', {'cart': cart, 'sum':sum})
