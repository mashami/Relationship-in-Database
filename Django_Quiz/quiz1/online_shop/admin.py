from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import*

# Register your models here.
admin.site.register(Web_user)
admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(shopping_cart)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Product)
admin.site.register(line_item)
