from django.contrib import auth
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from authentication.forms import CustomerForm
from authentication.models import Customer
from authentication.models import Contact

# Create your views here.
from products.models import Product, Payment


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
    return render(request, "Dashboard/show.html", {'contact': cont, 'customer': cust, 'products': pro, 'order': buy})


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
