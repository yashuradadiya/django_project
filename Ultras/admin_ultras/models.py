from django.db import models
from django.forms import ModelForm

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100,default="")
    email = models.CharField(max_length=100,unique=True,default="")
    contact = models.CharField(max_length=10,default="")
    password = models.CharField(max_length=10,default="")
    gender = models.CharField(max_length=6,default="")
    bdate = models.CharField(max_length=10,default="")
    address1 = models.CharField(max_length=100,default="")
    address2 = models.CharField(max_length=100,default="")
    city = models.CharField(max_length=20,default="")
    state = models.CharField(max_length=30,default="")
    country = models.CharField(max_length=30,default="")
    pincode = models.CharField(max_length=6,default="")
    skills = models.CharField(max_length=100,default="")
    image = models.FileField(upload_to="media/",default="")

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["name","email","contact","password","gender","bdate","address1","address2","city","state","country","pincode","skills","image"]


class Slider(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image = models.FileField(upload_to="media/",default="")

class SliderFrom(ModelForm):
    class Meta:
        model = Slider
        fields = ["title","description","image"]

class Category(models.Model):
    category = models.CharField(max_length=30)
    image = models.FileField(upload_to="media/",default="")
    def __str__(self):
        return self.category

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["category","image"]


class Tag(models.Model):
    tag = models.CharField(max_length=30)
    def __str__(self):
        return self.tag

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ["tag"]

class Brand(models.Model):
    brand = models.CharField(max_length=30)
    def __str__(self):
        return self.brand

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ["brand"]


class Product(models.Model):
    product_name = models.CharField(max_length=100,default="")
    description = models.CharField(max_length=500,default="")
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    size = models.CharField(max_length=30,default="")
    color = models.CharField(max_length=100,default="")
    material = models.CharField(max_length=200,default="")
    quantity = models.IntegerField(default=0)
    images = models.FileField(upload_to="media/",default="")

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["product_name","description","price","category","tag","brand","size","color","material","quantity","images"]

