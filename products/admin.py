from django.contrib import admin
from .models import Products
from .models import Offers
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display= ('name','price','stock')

class OfferAdmin(admin.ModelAdmin):
    list_display=('code','description','discount')

admin.site.register(Products,ProductAdmin)
admin.site.register(Offers,OfferAdmin)