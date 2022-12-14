from django.db import models
from django.shortcuts import reverse


class Services (models.Model):




     STATUSE_CHOISES=(
       ('pub','Publishes'),
       ('drf','Draft'),
      )

     title= models.CharField(max_length=100)
     text= models.TextField()
     author= models.ForeignKey('auth.user',on_delete=models.CASCADE,blank=True)
     date_created =models.DateTimeField(auto_now_add=True)
     date_modified = models.DateTimeField(auto_now=True)
     status= models.CharField(choices=STATUSE_CHOISES,max_length=3)
     price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)


     def __str__(self):
         return   str(self.price)




     def __str__(self):
         return self.title



     def get_absolute_url(self):
        return reverse('service_detail',args=[self.id])




