from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomerBookView.as_view(),name='booking'),
    ]
