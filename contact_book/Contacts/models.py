from django.db import models
from django.forms import ModelForm

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    contact = models.CharField(max_length = 10)

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["name","email","password","contact"]

class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    contact = models.CharField(max_length = 10)
    user_id = models.CharField(max_length = 100)

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name","email","address","contact","user_id"]