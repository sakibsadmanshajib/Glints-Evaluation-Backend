from rest_framework import viewsets, status, permissions
from .serializer import *

class RestaurantViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Restaurant.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return RestaurantSerializer
        return AddRestaurantSerializer
