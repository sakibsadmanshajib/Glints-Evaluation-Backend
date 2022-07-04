from django.db import models

# Create your models here.
class Restaurant(models.Model):
    cashBalance = models.DecimalField(max_digits=10, decimal_places=2)
    openingHours = models.CharField(max_length=256)
    restaurantName = models.CharField(max_length=256)

    def __str__(self):
        return self.restaurantName

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dishName = models.CharField(max_length=512)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.dishName

class Customer(models.Model):
    cashBalance = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=256)

class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dishName = models.ForeignKey(Menu, on_delete=models.CASCADE)
    restaurantName = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    transactionAmount = models.DecimalField(max_digits=10, decimal_places=2)
    transactionDate = models.DateTimeField(auto_now_add=True)