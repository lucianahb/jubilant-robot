from django.contrib import admin
from .models import Seller
# from .models import Product


class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
admin.site.register(Seller, SellerAdmin)
