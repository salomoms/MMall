from django.contrib import admin
from .models import *

class CartItemAdmin(admin.TabularInline):
    model = CartItem

class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemAdmin, ]

admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart, CartAdmin)
admin.site.site_header = 'E-Commerce CMS'
admin.site.site_title = 'E-Commerce CMS'

