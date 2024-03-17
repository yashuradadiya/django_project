from django.db import models
from django.forms import ModelForm
from admin_ultras.models import *

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100,default="")
    email = models.CharField(max_length=100,unique=True,default="")
    password = models.CharField(max_length=100,default="")
    contact = models.CharField(max_length=10,default="")
    city = models.CharField(max_length=300,default="")
    status = models.CharField(max_length=10,default="")
    country = models.CharField(max_length=50,default="")
    address1 = models.CharField(max_length=100,default="")
    address2 = models.CharField(max_length=100,default="")
    state = models.CharField(max_length=50,default="")
    pincode = models.IntegerField(default=0)

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["name","email","password","contact","status"]

class Users_Form(ModelForm):
    class Meta:
        model = User
        fields = ["name","email","contact","city","country","address1","address2","state","pincode"]
    
class Cart(models.Model):
    user_id = models.ForeignKey(Profile,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.IntegerField(default=100)
    amount = models.IntegerField(default=100)

class Wishlist(models.Model):
    wishlist = models.ForeignKey(Product,on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile,on_delete=models.CASCADE)

class CheckOut(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    note = models.CharField(max_length=500,default="")
    shipping_method = models.CharField(max_length=100,default="")
