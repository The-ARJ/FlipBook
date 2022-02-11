from django.contrib import admin

# Register your models here.
from authentication.models import Customer, Contact
from products.models import Product
admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(Product)

