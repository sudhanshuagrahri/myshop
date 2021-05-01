from django.shortcuts import render
from cart.models import CartItem
from .models import OrderCustItem, Pincode
from .forms import OrderCreateForm


def order_create(request):
    cart = CartItem.objects.filter(user=request.user)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            pincode=form.cleaned_data['postal_code']
            try:
                Pincode.get.objects(pincode=pincode)
                order = form.save()
                for item in cart:
                    OrderCustItem.objects.create(order=order, cart=item)
                    item.delete()
                # clear the cart
            
                # launch asynchronous task
                #order_created.delay(order.id)
                return render(request,'orders/order/created.html',{'order': order})
    
            except:
                return render(request,'orders/order/discard.html')
                
                
    else:
        form = OrderCreateForm()
        s= sum(item.totPrice() for item in cart)
        return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form, 'sum':s})
