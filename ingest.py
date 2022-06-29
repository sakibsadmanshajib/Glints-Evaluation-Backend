
import json
import urllib.request
import datetime
import django
from sys import path
import os
from django.conf import settings
path.append(os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'settings.py'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GlintsEval.settings")
django.setup()
from backend.models import *


with urllib.request.urlopen("https://gist.githubusercontent.com/seahyc/b9ebbe264f8633a1bf167cc6a90d4b57/raw/021d2e0d2c56217bad524119d1c31419b2938505/restaurant_with_menu.json") as url:
    restaurants = json.loads(url.read().decode())

for restaurant in restaurants:
    cashBalance = restaurant['cashBalance']
    openingHours = restaurant['openingHours']
    restaurantName = restaurant['restaurantName']
    restaurant_data = Restaurant(
        cashBalance=cashBalance, openingHours=openingHours, restaurantName=restaurantName)
    restaurant_data.save()
    menu = restaurant['menu']
    for dish in menu:
        dishName = dish['dishName']
        price = dish['price']
        menu_data = Menu(restaurant=restaurant_data,
                         dishName=dishName, price=price)
        menu_data.save()

with urllib.request.urlopen("https://gist.githubusercontent.com/seahyc/de33162db680c3d595e955752178d57d/raw/785007bc91c543f847b87d705499e86e16961379/users_with_purchase_history.json") as url:
    consumers = json.loads(url.read().decode())

for consumer in consumers:
    cashBalance = consumer['cashBalance']
    name = consumer['name']
    customer_data = Customer(cashBalance=cashBalance, name=name)
    customer_data.save()
    transactions = consumer['transactions']
    for transaction in transactions:
        dishName = transaction['dishName']
        restaurantName = transaction['restaurantName']
        transactionAmount = transaction['transactionAmount']
        transactionDate = datetime.strptime(transaction['transactionDate'], "%m/%d/%Y %I:%M %p")
        transaction_data = Transaction(customer=customer_data, dishName=dishName, restaurantName=restaurantName,
                                       transactionAmount=transactionAmount, transactionDate=transactionDate)
        transaction_data.save()
