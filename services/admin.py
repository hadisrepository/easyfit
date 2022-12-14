from django.contrib import admin
from .models import Services



@admin.register(Services)


class ServicesAdmin(admin.ModelAdmin):

    list_display = ('title','author','price' )
    ordering = ('title', )