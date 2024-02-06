from django.urls import path

from . import views

urlpatterns = [
    path("pin-enter", views.pin_enter),
    path("pin-verification", views.verify_pin),
    path("register", views.register_customer),
    path("check-username", views.verify_user),
    path("login", views.login_customer),
    path("signout", views.logout_customer),
    path("home", views.home),
    path("get_balance", views.get_balance),
]
