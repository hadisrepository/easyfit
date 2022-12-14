from django.shortcuts import render, get_object_or_404,redirect
from.cart import Cart
from .forms import AddToCartProductForm
from services.models import Services


def cart_detail_view(request):
    cart= Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart},)


def add_to_cart_view(request, service_id):
    cart= Cart(request)
    service= get_object_or_404(Services, id=service_id)
    form= AddToCartProductForm(request.POST)
    if form.is_valid():
        cleaned_date = form.cleaned_data
        quantity = cleaned_date['quantity']
        cart.add(service,quantity)
    return  redirect('cart_detail')







