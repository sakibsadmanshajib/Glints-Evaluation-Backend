from django.urls import path
from .views import basic, ingest, query, purchase
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('restaurant', basic.RestaurantViewSet, 'restaurant')
routers.register('menu', basic.MenuViewSet, 'menu')
routers.register('customer', basic.CustomerViewSet, 'customer')
routers.register('transaction', basic.TransactionViewSet, 'transaction')

urlpatterns = [
    path('add-restaurants/', ingest.AddRestaurantData.as_view(), name='add_restaurant_data'),
    path('add-customers/', ingest.AddCustomerData.as_view(), name='add_customer_data'),
    path('open-restaurants/', query.OpenRestaurants.as_view(), name='open_restaurants'),
    path('dishes-in-range/', query.DishesInRange.as_view(), name='dishes_in_range'),
    path('purchase/', purchase.Purchase.as_view(), name='purchase'),
]
urlpatterns += routers.urls