from django.db import models

# Create your models here.

def email_default():
    return {"email": "to1@example.com"}

class demodata(models.Model):
    firstname = models.CharField(max_length=200, default=None)
    lastname = models.CharField(max_length=150, default=None)
    email = models.EmailField(max_length=500,default=email_default)