
from django.urls import path
from .views import cart_detail_view,add_to_cart_view

urlpatterns = [
   path('', cart_detail_view, name='cart_detail'),
   path('add/<int:service_id>/', add_to_cart_view, name='cart_add'),
]