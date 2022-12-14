from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, get_object_or_404,redirect

from .forms import BookForCustomer


class CustomerBookView(generic.CreateView):

    form_class = BookForCustomer
    template_name = 'customer/booking.html'




