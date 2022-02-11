from django.db import models



# Create your models here.
class Product(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    image = models.FileField(upload_to='product_images')
    bookname = models.CharField(max_length=100)
    authorname = models.CharField(max_length=100)
    bookdesc = models.CharField(max_length=200)
    price = models.CharField(max_length=100)

    class Meta:
        db_table = "product"


class Payment(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    fullname = models.CharField(max_length=100)
    expiry = models.CharField(max_length=100)
    security = models.CharField(max_length=200)
    postal = models.CharField(max_length=100)
    delivery = models.CharField(max_length=100)


    class Meta:
        db_table = "Orders and Payments"
