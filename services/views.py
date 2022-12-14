from django.shortcuts import render,reverse,redirect
# from .models import

from django.contrib.auth.models import User

from django.views import generic
from django.urls import reverse_lazy
from .models import Services
from cart.forms import AddToCartProductForm

def get_context_data(self,**kwargs):
    context=super.get_context_data(**kwargs)
    context['add_to_cart_form']=AddToCartProductForm()
    return context




class getallservicesview(generic.ListView):
    template_name = 'services/services.html'
    context_object_name ='services'


    def get_queryset(self):
        return Services.objects.filter(status='pub').order_by('-date_modified')



class ServiceDetailView(generic.DetailView):

    model=Services
    template_name = 'services/service_detail.html'
    context_object_name = 'services'



class ServiceCreateView(generic.CreateView):

     model = Services
     fields = ['title','text','price','author','status']
     template_name = 'services/services_create.html'







