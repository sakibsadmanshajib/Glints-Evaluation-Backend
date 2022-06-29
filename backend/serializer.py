from rest_framework import serializers
from .models import Restaurant, Menu, Customer, Transaction

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = (
            'dishName',
            'price',
        )

class AddMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
    
class AddRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(many=True)
    class Meta:
        model = Restaurant
        fields = (
            'cashBalance',
            'openingHours',
            'restaurantName',
            'menu',
        )

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            'dishName',
            'restaurantName',
            'transactionAmount',
            'transactionDate',
        )

class AddCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    purchaseHistory = TransactionSerializer(many=True)
    class Meta:
        model = Customer
        fields = (
            'cashBalance',
            'name',
            'purchaseHistory'
        )