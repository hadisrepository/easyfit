from django.db import models
from django.shortcuts import reverse



class Customer(models.Model):

     # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname= models.CharField(max_length=100)

    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, null=True, blank=True)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.surname


    def get_absolute_url(self):
        return reverse('showbook.html')



