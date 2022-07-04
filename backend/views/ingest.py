from rest_framework import generics, status, permissions
from rest_framework.response import Response
from ..models import *
from datetime import datetime

# TODO: Create an API to process the restaurant JSON data containing the following fields:
# restaurantName, openingHours, cashBalance, menu
# The restaurantName field is a string, the openingHours field is a string, the cashBalance field is a decimal, and the menu field is a list of dictionaries containing the following fields:
# dishName, price
# The dishName field is a string, the price field is a decimal.
# The menu field is a list of dictionaries.

class AddRestaurantData(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        for restaurant in data:
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

        return Response(status=status.HTTP_200_OK)

class AddCustomerData(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        for consumer in data:
            cashBalance = consumer['cashBalance']
            name = consumer['name']
            customer_data = Customer(cashBalance=cashBalance, name=name)
            customer_data.save()
            transactions = consumer['purchaseHistory']
            for transaction in transactions:
                dishName = transaction['dishName']
                restaurantName = transaction['restaurantName']
                transactionAmount = transaction['transactionAmount']
                transactionDate = datetime.strptime(transaction['transactionDate'], "%m/%d/%Y %I:%M %p")
                transaction_data = Transaction(customer=customer_data, dishName=dishName, restaurantName=restaurantName,
                                            transactionAmount=transactionAmount, transactionDate=transactionDate)
                transaction_data.save()

        return Response(status=status.HTTP_200_OK)