from datetime import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Restaurant, Menu, Customer, Transaction

class RestaurantTests(APITestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(cashBalance=100.00, openingHours='10:00-20:00', restaurantName='Test Restaurant')

    def test_create_restaurant(self):
        url = '/api/v1/restaurant/'
        prev_count = Restaurant.objects.count()
        data = {'cashBalance': '100.00', 'openingHours': '10:00-20:00', 'restaurantName': 'Test Restaurant'}
        response = self.client.post(url, data, format='json')
        now_count = Restaurant.objects.count()
        diff = now_count - prev_count
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(diff, 1)

    def test_list_restaurants(self):
        url = '/api/v1/restaurant/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_restaurant(self):
        url = f'/api/v1/restaurant/{str(self.restaurant.id)}/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_restaurant(self):
        url = f'/api/v1/restaurant/{str(self.restaurant.id)}/'
        data = {'cashBalance': '100.00', 'openingHours': '10:00-20:00', 'restaurantName': 'Test Restaurant'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_restaurant(self):
        url = f'/api/v1/restaurant/{str(self.restaurant.id)}/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class MenuTests(APITestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(restaurantName='Test Restaurant', cashBalance='100.00', openingHours='10:00-20:00')
        self.menu = Menu.objects.create(restaurant=self.restaurant, dishName='Test Dish', price='100.00')
        
    def test_create_menu(self):
        url = '/api/v1/menu/'
        prev_count = Menu.objects.count()
        data = {'restaurant': self.restaurant.id, 'dishName': 'Test Dish', 'price': '100.00'}
        response = self.client.post(url, data, format='json')
        now_count = Menu.objects.count()
        diff = now_count - prev_count
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(diff, 1)

    def test_list_menus(self):
        url = '/api/v1/menu/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_retrieve_menu(self):
        url = f'/api/v1/menu/{str(self.menu.id)}/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_menu(self):
        url = f'/api/v1/menu/{str(self.menu.id)}/'
        data = {'restaurant': self.restaurant.id, 'dishName': 'Test Dish', 'price': '100.00'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_menu(self):
        url = f'/api/v1/menu/{str(self.menu.id)}/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CustomerTests(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name='Test Customer', cashBalance='100.00')

    def test_create_customer(self):
        url = '/api/v1/customer/'
        prev_count = Customer.objects.count()
        data = {'name': 'Test Customer', 'cashBalance': '100.00'}
        response = self.client.post(url, data, format='json')
        now_count = Customer.objects.count()
        diff = now_count - prev_count
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(diff, 1)

    def test_list_customers(self):
        url = '/api/v1/customer/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_retrieve_customer(self):
        url = f'/api/v1/customer/{str(self.customer.id)}/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_customer(self):
        url = f'/api/v1/customer/{str(self.customer.id)}/'
        data = {'name': 'Test Customer', 'cashBalance': '100.00'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_customer(self):
        url = f'/api/v1/customer/{str(self.customer.id)}/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class TransactionTests(APITestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(cashBalance='100.00', openingHours='10:00-20:00', restaurantName='Test Restaurant')
        self.menu = Menu.objects.create(restaurant=self.restaurant, dishName='Test Dish', price='100.00')
        self.customer = Customer.objects.create(name='Test Customer', cashBalance='100.00')
        self.transaction = Transaction.objects.create(customer=self.customer, dishName=self.menu, restaurantName=self.restaurant, transactionAmount=self.menu.price, transactionDate=datetime.now())

    def test_create_transaction(self):
        url = '/api/v1/transaction/'
        prev_count = Transaction.objects.count()
        data = {'customer': self.customer.id, 'restaurantName': self.restaurant.id, 'dishName': self.menu.id, 'transactionAmount': self.menu.price, 'transactionDate': datetime.now()}
        response = self.client.post(url, data, format='json')
        now_count = Transaction.objects.count()
        diff = now_count - prev_count
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(diff, 1)

    def test_list_transactions(self):
        url = '/api/v1/transaction/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_transaction(self):
        url = f'/api/v1/transaction/{str(self.transaction.id)}/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_transaction(self):
        url = f'/api/v1/transaction/{str(self.transaction.id)}/'
        data = {'customer': self.customer.id, 'restaurantName': self.restaurant.id, 'dishName': self.menu.id, 'transactionAmount': self.menu.price, 'transactionDate': datetime.now()}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_transaction(self):
        url = f'/api/v1/transaction/{str(self.transaction.id)}/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CustomTests(APITestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(cashBalance='100.00', openingHours='10:00-20:00', restaurantName='Test Restaurant')
        self.menu = Menu.objects.create(restaurant=self.restaurant, dishName='Test Dish', price='100.00')
        self.customer = Customer.objects.create(name='Test Customer', cashBalance='100.00')

    def test_open_restaurants(self):
        url = reverse('open_restaurants')
        response = self.client.get(f'{url}?time=2022-07-06 2:24:35', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_dishes_in_range(self):
        url = reverse('dishes_in_range')
        response = self.client.get(f'{url}?top=10&price_start=2&price_end=40&num_of_dishes=3&more_or_less=more', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_restaurants(self):
        url = '/api/v1/restaurant/'
        response = self.client.get(f'{url}?name=burger', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_dishes(self):
        url = '/api/v1/menu/'
        response = self.client.get(f'{url}?name=burger', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_purchase(self):
        url = reverse('purchase')
        data = {'customer': 'Test Customer', 'restaurant': 'Test Restaurant', 'dish': 'Test Dish'}
        response = self.client.post(url, data, format='json')