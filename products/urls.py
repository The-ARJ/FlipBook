from django.contrib import admin
from django.urls import path, include
from . import views

# Django admin customization
urlpatterns = [
    path('steve', views.steve),
    path('great', views.great),
    path('EINSTEIN', views.EINSTEIN),
    path('Diary', views.Diary),
    path('Musk', views.Musk),
    path('malibu', views.malibu),
    path('last', views.last),
    path('Beautiful', views.Beautiful),
    path('Project', views.Project),
    path('Lore', views.Lore),
    path('anthropocene', views.anthropocene),
    path('Rule', views.Rule),
    path('Empire', views.Empire),
    path('Hill', views.Hill),
    path('Daughter', views.Daughter),
    path('Sale', views.Sale,name='Sale'),

    path('add', views.add, name="add"),
    path('edit', views.edit, name="edit"),
    path('billing', views.billing, name="billing"),

    path('product_create', views.product_create,name="product_create"),
    path('Payment_create', views.Payment_create,name="Payment_create"),

    path('deleteproduct/<int:p_id>', views.deleteproduct, name="deleteproduct"),

    path('productupdate/<str:p_id>', views.productupdate, name="productupdate"),
    path('ordercancel/<int:p_id>', views.ordercancel, name="ordercancel"),
]
