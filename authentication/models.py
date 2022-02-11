from django.db import models

from django.db import models


# Create your models here.
class Customer(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    username = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)

    last_login = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "customer"


class Contact(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    fname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    # lname = models.CharField(max_length=100)

    class Meta:
        db_table = "contact"
