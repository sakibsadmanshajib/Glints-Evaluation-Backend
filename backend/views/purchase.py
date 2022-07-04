from rest_framework import viewsets, status, permissions, generics
from rest_framework.response import Response
from ..models import *
from datetime import datetime

class Purchase(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        restaurant = Restaurant.objects.get(restaurantName=data['restaurant'])
        customer = Customer.objects.get(name=data['customer'])
        dish = Menu.objects.get(dishName=data['dish'])

        if customer.cashBalance >= dish.price:
            customer.cashBalance -= dish.price
            customer.save()
            transaction = Transaction(customer=customer, dishName=dish, restaurantName=restaurant,
                                    transactionAmount=dish.price, transactionDate=datetime.now())
            transaction.save()
            restaurant.cashBalance += dish.price
            restaurant.save()
            return Response(status=status.HTTP_200_OK)