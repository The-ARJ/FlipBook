from django.shortcuts import render
import os

from django.shortcuts import render, redirect

from products.models import Product, Payment

from products.forms import ProductForm, PaymentForm


# Create your views here.
def steve(request):
    return render(request, "books/Stevejobs.html")


def great(request):
    return render(request, "books/TheGreatGatsby.html")


def EINSTEIN(request):
    return render(request, "books/EINSTEIN.html")


def Diary(request):
    return render(request, "books/THE DIARY OF A YOUNG GIRL.html")


def Musk(request):
    return render(request, "books/ELON MUSK.html")


def malibu(request):
    return render(request, "books/MALIBU RISING.html")


def last(request):
    return render(request, "books/THE LAST THING HE TOLD ME.html")


def Beautiful(request):
    return render(request, "books/BEAUTIFUL WORLD, WHERE ARE YOU.html")


def Project(request):
    return render(request, "books/PROJECT HAIL MARY.html")


def Lore(request):
    return render(request, "books/LORE OLYMPUS VOLUME ONE.html")


def anthropocene(request):
    return render(request, "books/THE ANTHROPOCENE REVIEWED.html")


def Daughter(request):
    return render(request, "books/DAUGHTER OF THE DEEP.html")


def Hill(request):
    return render(request, "books/THE HILL WE CLIMB.html")


def Rule(request):
    return render(request, "books/RULE OF WOLVES.html")


def Empire(request):
    return render(request, "books/EMPIRE OF PAIN.html")


def Sale(request):
    pro = Product.objects.all()
    return render(request, "navbar/paidbooks.html", {'product': pro})


def add(request):
    return render(request, "Dashboard/addproduct.html")


def edit(request):
    return render(request, "Dashboard/edit.html")


def billing(request):
    return render(request, "navbar/billing.html")


def product_create(request):
    if request.method == "POST":
        print(request.POST)
        form = ProductForm(request.POST, request.FILES)
        form.save()
        print("uploaded to database")
        return redirect("/add")
    else:
        form = ProductForm()
    return render(request, "Dashboard/show.html", {'form': form})


def Payment_create(request):
    context = {'success': False}
    if request.method == "POST":
        print(request.POST)
        form = PaymentForm(request.POST, request.FILES)
        form.save()
        print("uploaded to database")
        context = {'success': True}
        return redirect("/billing", {'context': context})
    else:
        form = PaymentForm()
    return render(request, "navbar/paidbooks.html", {'form': form})


# def show(request):
#     pro = Product.objects.all()
#     return render(request, "Dashboard/show.html", {'products': pro})


def deleteproduct(request, p_id):
    product = Product.objects.get(id=p_id)
    product.delete()
    return redirect("/show/#section3")


def ordercancel(request, p_id):
    order = Payment.objects.get(id=p_id)
    order.delete()
    return redirect("/show/#section4")


