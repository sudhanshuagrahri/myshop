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
            # print(Pincode.objects.get(pincode=pincode))
            try:
                Pincode.objects.get(pincode=pincode)
                order = form.save()
                print(order)
                for item in cart:
                    OrderCustItem.objects.create(order=order, customer=request.user, product=item.product,price=item.totPrice(),quantity=item.quantity)
                    item.delete()
                    # print("order completed")
                    # print(OrderCustItem.objects.all())
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
