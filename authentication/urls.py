from django.contrib import admin
from django.urls import path, include
from . import views

# Django admin customization
urlpatterns = [
    path('', views.home, name='home'),  # signin as well
    path('signup', views.signup, name='signup'),  # signup is creating a Customer as well
    path('signout', views.signout, name='sign-out'),
    path('MainHome', views.MainHome, name='MainHome'),
    path('Books', views.Books, name='Books'),
    path('aboutus', views.aboutus, name='aboutus'),

    path('contactus', views.contactus, name='contactus'),
    path('aboutus2', views.aboutus2, name='aboutus2'),
    path('contactus2', views.contactus2, name='contactus2'),
    path('adminpanel', views.adminpanel, name="adminpanel"),
    path('show/', views.show,name='show'),

    path('delete_contact/<int:P_id>', views.delete_contact, name="delete_contact"),
    path('delete_costumer/<int:P_id>', views.delete_customer, name="delete_customer"),


    path('search', views.search, name="search"),
    path('searchproduct', views.searchproduct, name="searchproduct"),
    path('Page_next/', views.Page_next, name="Page_next"),

]
