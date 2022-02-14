from django.contrib import auth
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from authentication.forms import CustomerForm
from authentication.models import Customer
from authentication.models import Contact

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
from products.models import Product, Payment
from django.core.paginator import Paginator


def home(request):  # login page or index page

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            customer = Customer.objects.get(username=username, password=password)
            return redirect('MainHome')

        except:
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                return redirect('show/')
            return render(request, 'authentication/index.html')

    else:
        form = CustomerForm()
        return render(request, "authentication/index.html", {'form': form})


def MainHome(request):
    return render(request, "navbar/MainHome.html")


def signup(request):
    if request.method == "POST":
        if request.method == "POST":

            print(request.POST)
            form = CustomerForm(request.POST)
            form.save()

            return redirect('home')

        else:
            form = CustomerForm()
        return render(request, "Dashboard/show.html", {'form': form})
    return render(request, "authentication/signup.html")


def contactus(request):
    context = {'success': False}
    if request.method == "POST":
        fullname = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        emailmessage = EmailMessage(
            "New Message From " + email,
            message,
            "oceanofbooks.web@gmail.com",
            ["oceanofbooks.web@gmail.com"],

        )
        emailmessage.send()

        print(fullname, email, message)
        ins = Contact(fname=fullname, email=email, message=message)
        ins.save()
        print("data is created on db")
        context = {'success': True}
    return render(request, "authentication/contact.html", context)


def show(request):
    cont = Contact.objects.all()
    cust = Customer.objects.all()
    pro = Product.objects.all()
    buy = Payment.objects.all()

    p = Paginator(Product.objects.all(), 3)
    page = request.GET.get('page')
    prod = p.get_page(page)

    cu = Paginator(Customer.objects.all(), 10)
    cus = cu.get_page(page)

    co = Paginator(Contact.objects.all(), 10)
    con = co.get_page(page)

    pa = Paginator(Payment.objects.all(), 10)
    pay = pa.get_page(page)

    return render(request, "Dashboard/show.html",
                  {'contact': cont, 'customer': cust, 'products': pro, 'order': buy, "prods": prod, 'cus': cus,'con':con,'pay':pay})


def adminpanel(request):
    return render(request, 'Dashboard/show.html', )


def signout(request):
    logout(request)
    request.session.clear()
    print("Logged Out Successfully!!")
    return redirect('home')


def Books(request):
    return render(request, "navbar/Books.html")


def aboutus(request):
    return render(request, "authentication/aboutus.html")


def aboutus2(request):
    return render(request, "navbar/aboutus.html")


def contactus2(request):
    return render(request, "navbar/contact.html")


# Create your views here.
def delete_contact(request, P_id):
    con = Contact.objects.get(id=P_id)
    con.delete()
    print("delete successfully")
    return redirect("/show/#section1")


def delete_customer(request, P_id):
    cus = Customer.objects.get(id=P_id)
    cus.delete()
    return redirect("/show/#section2")


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        items = Product.objects.filter(bookname__contains=searched)
        return render(request, "Dashboard/show.html", {'searched': searched, 'items': items})
    else:
        return render(request, "Dashboard/show.html")


def searchproduct(request):
    return redirect("/show/#section3")


# Pagination
def Page_next(request, ):
    return redirect("/show/#section3")
