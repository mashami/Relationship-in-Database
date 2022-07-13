
from tkinter import CASCADE
from django.db import models
import uuid
# Create your models here.

userState=[
    ('NEW','new'),
    ('ACTIVE','active'),
    ('BLOCKED','blocked'),
    ('BANNER','banner'),
]

orderStatus=[
    ('NEW','new'),
    ('HOLD','hold'),
    ('SHIPPER','shipper'),
    ('DELIVERED','delived'),
    ('CLOSED','closed'),
]

class Web_user(models.Model):
    log_id=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    password=models.CharField(max_length=10,null=True,blank=True)
    state=models.CharField(max_length=100,null=True,blank=False,choices=userState)
    
    def __str__(self):
        return f"{self.password} to {self.state}"
    
class Customer(models.Model):
    id=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    address=models.CharField(max_length=100,null=True,blank=False)
    phone=models.IntegerField()
    web=models.OneToOneField(Web_user,related_name='customer_web',on_delete=models.CASCADE)
   
    def __str__(self):
        return f"{self.address} to {self.phone} to {self.web}"
    
class Account(models.Model):
    id_account=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    billing_address=models.CharField(max_length=100,null=True,blank=False)
    isclosed=models.BooleanField()
    open=models.DateTimeField(auto_now_add=True)
    closed=models.DateField(auto_now_add=True)
    customer=models.OneToOneField(Customer,related_name="customer_account",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.billing_address}: {self.isclosed}: {self.open}: {self.closed}: {self.customer}"
    
    
    
class shopping_cart(models.Model):
    created_Date=models.DateField(auto_now_add=True)
    webUser=models.OneToOneField(Web_user,related_name='shopping_web',on_delete=models.CASCADE)
    account=models.OneToOneField(Account,related_name="account_shop",on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.webUser} to {self.created_Date}: {self.account}"
    
    

class Order(models.Model):
    number=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    ordered=models.DateTimeField(auto_now_add=True)
    shipped=models.DateField()
    total=models.IntegerField()
    ship_to=models.CharField(max_length=100,null=False,blank=True)
    status=models.CharField(max_length=100,null=True,blank=False,choices=orderStatus)
    account=models.ForeignKey(Account,related_name='account_order',on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.ordered} to {self.shipped} to {self.ship_to} to {self.status} to {self.account}"
    
    
class Payment(models.Model):
    id_payment=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    paid=models.DateField(auto_now_add=True)
    total_payment=models.IntegerField()
    account=models.ForeignKey(Account,related_name='customer_payment',on_delete=models.CASCADE)
    order=models.ForeignKey(Order,related_name='order_payment',on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.paid} to {self.total_payment} to {self.account} to {self.order}"
    
    
class Product(models.Model):
    id_product=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name=models.CharField(max_length=100,null=True,blank=False)
    supplier=models.CharField(max_length=100,null=True,blank=False) 
    
    def __str__(self):
        return f"{self.name} to {self.supplier}"
    
    
class line_item(models.Model):
    Quantity=models.IntegerField()
    price=models.IntegerField()
    shoping=models.ForeignKey(shopping_cart,related_name="shop_line_item",on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='product_line_item',on_delete=models.CASCADE)
    order=models.ForeignKey(Order,related_name='order_line_item',on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.Quantity} to {self.price} to {self.shoping} to {self.product} to {self.order}"

    
    

    
    
    
    
    
    
