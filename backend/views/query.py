from rest_framework import generics, status, permissions
from ..models import *
from datetime import datetime
from ..serializer import *

# TODO: Create a List (GET) API to get all the restaurants
# that are open in the certain time
# using search parameter to search for the restaurantName field

class OpenRestaurants(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RestaurantSerializer

    def get_time(self, sec, n):
        start = datetime.strptime(f'{sec[n]} {sec[n+1]}', "%I:%M %p")
        end = datetime.strptime(f'{sec[n+3]} {sec[n+4]}', "%I:%M %p")
        return start, end

    def opening_time(self, restaurant):
        days = ['Mon', 'Tues', 'Weds', 'Thurs', 'Fri', 'Sat', 'Sun']
        open_time = {}
        for sec in restaurant.openingHours.split('/'):
            sec = sec.split(' ')
            if sec[0] in days:
                if sec[1] == '-':
                    days_list = days[days.index(sec[0]):(days.index(sec[2])+1)]
                    for day in days_list:
                        open_time[day] = self.get_time(sec, 2)
                elif sec[1] == ',':
                    start, end = self.get_time(sec, 3)
                    open_time[sec[0]] = [start, end]
                    open_time[sec[2]] = [start, end]
                else:
                    start, end = self.get_time(sec, 1)
                    open_time[sec[0]] = [start, end]

        return open_time

    def check_if_open(self, restaurant, time):
        open_time = self.opening_time(restaurant)
        day_name = {
            'Monday': 'Mon',
            'Tuesday': 'Tues',
            'Wednesday': 'Weds',
            'Thursday': 'Thurs',
            'Friday': 'Fri',
            'Saturday': 'Sat',
            'Sunday': 'Sun'
        }
        day = day_name[time.strftime('%A')]
        if day in open_time:
            start, end = open_time[day]
            if start <= time.time() <= end:
                return True
        return False
        
    def get_queryset(self):
        time = self.request.query_params.get('time', None)
        if time is None:
            time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        restaurants = Restaurant.objects.all()
        return [restaurant for restaurant in restaurants if self.check_if_open(restaurant, time)]

class DishesInRange(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RestaurantSerializer

    def restaurant_name(self, restaurant):
        return restaurant.restaurantName

    def get_queryset(self):
        top = self.request.query_params.get('top', 5)
        price_start = self.request.query_params.get('price_start', 0)
        price_end = self.request.query_params.get('price_end', 100)
        num_of_dishes = self.request.query_params.get('num_of_dishes', 5)
        more_or_less = self.request.query_params.get('more_or_less', 'more')

        restaurant_list = []
        restaurants = Restaurant.objects.all()
        for restaurant in restaurants:
            dishes = Menu.objects.filter(restaurant=restaurant)
            dishes_list = [dish for dish in dishes if dish.price >= float(price_start) and dish.price <= float(price_end)]

            if more_or_less == 'more':
                restaurant_list.append(restaurant) if len(dishes_list) > int(num_of_dishes) else None
            else:
                restaurant_list.append(restaurant) if len(dishes_list) < int(num_of_dishes) else None

        if len(restaurant_list) > int(top):
            restaurant_list = restaurant_list[:int(top)]
        return sorted(restaurant_list, key=self.restaurant_name)
        