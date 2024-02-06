from django.urls import path

from . import views

urlpatterns = [
    path("pin-enter", views.pin_enter),
    path("pin-verification", views.verify_pin, name="pin_verify"),
    path("register", views.register_customer),
    path("check-username", views.verify_user),
    path("login", views.login_customer),
    path("signout", views.logout_customer, name="signout"),
    path("home", views.home, name="home"),
    path("get_balance", views.get_balance),
    path("cash-withdraw", views.cash_withdraw, name="cash_withdraw"),
]
