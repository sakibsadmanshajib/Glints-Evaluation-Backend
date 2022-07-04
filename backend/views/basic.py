from rest_framework import viewsets, status, permissions
from ..serializer import *


# TODO: Basic CRUD API to work with the models

class RestaurantViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name is None:
            return Restaurant.objects.all()
        return Restaurant.objects.filter(restaurantName__trigram_similar=name)

class MenuViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MenuSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name is None:
            return Menu.objects.all()
        return Menu.objects.filter(dishName__trigram_similar=name)

class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
