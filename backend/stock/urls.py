from django.urls import path
from stock.views import (home)


app_name = 'stock'


urlpatterns = [
    path('', home),
]
