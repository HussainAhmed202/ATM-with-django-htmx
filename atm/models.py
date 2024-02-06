from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Customer(User):
    pin = models.CharField(max_length=255)
    balance = models.IntegerField(default=10000)

    def get_balance(self):
        return self.balance

    def update_balance(self, value):
        self.balance += value

    def set_pin(self, pin_code):
        self.pin = make_password(pin_code)

    def check_pin(self, pin_code):
        encoded_pin = self.pin
        return check_password(pin_code, encoded_pin)

    def __str__(self) -> str:
        return f"username={self.username} password={self.password} pin={self.pin}  balance={self.balance}"
