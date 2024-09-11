from django.contrib import admin
from .models import Product,Cart,Orders
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "userid",
        "productid",
        "productname",
        "category",
        "description",
        "price",
        "images",
    ]
admin.site.register(Product, ProductAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = [
        "userid",
        "productid",
        "qty",
    ]
admin.site.register(Cart, CartAdmin)


class OrdersAdmin(admin.ModelAdmin):
    list_display = [
        "orderid",
        "userid",
        "productid",
        "qty",
    ]
admin.site.register(Orders, OrdersAdmin)