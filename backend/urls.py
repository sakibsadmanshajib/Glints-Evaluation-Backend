from django.urls import path
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('restaurant', views.RestaurantViewSet)

urlpatterns = []
urlpatterns += routers.urls