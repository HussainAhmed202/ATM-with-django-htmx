from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Customer

# Create your views here.


def cash_withdraw(request):
    return render(request, "withdraw.html")


def get_balance(request):
    if request.method == "GET":
        user = Customer.objects.get(pk=request.session["_auth_user_id"])
        return HttpResponse(user.get_balance())


# @login_required(login_url="/atm/login")
def home(request):
    return render(request, "home.html")


# @login_required(login_url="/atm/login")
def pin_enter(request):
    return render(request, "pin-enter.html")


def verify_pin(request):
    if request.method == "POST":
        pin = request.POST["pin"]
        if len(pin) == 4:
            user = Customer.objects.get(pk=request.session["_auth_user_id"])
            if user.check_pin(pin):
                return HttpResponseRedirect(reverse("home"))
            else:
                return HttpResponseRedirect(reverse("signout"))


def register_customer(request):
    if request.user.is_authenticated:
        return HttpResponse("User already logged in")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        pin = request.POST["pin"]
        balance = request.POST["balance"]
        try:
            Customer.objects.get(username=username)
        except Customer.DoesNotExist:
            cust = Customer.objects.create(username=username, balance=balance)
            cust.set_password(password)
            cust.set_pin(pin)
            cust.save()
            login(request, cust)
            return HttpResponseRedirect("pin-enter")
        else:
            return HttpResponse("Customer already exists")

    return render(
        request, "register.html", {"include_pin": True, "include_balance": True}
    )


def verify_user(request):
    if request.method == "GET":
        username = request.GET["username"]
        try:
            Customer.objects.get(username=username)
        except Customer.DoesNotExist:
            return HttpResponse("valid username")
        return HttpResponse("User already exists")


def login_customer(request):
    if request.user.is_authenticated:
        return HttpResponse("User already logged in")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("pin-enter")
        else:
            return render(request, "login.html", {"message": True})
    return render(request, "login.html", {"message": False})


@login_required(login_url="/atm/pin-enter")
def logout_customer(request):
    # del request.session["username"]
    logout(request)
    return HttpResponseRedirect("login")
