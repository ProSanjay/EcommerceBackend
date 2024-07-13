from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', demo , name="demo"),
    path('getProduct/', getProduct ,  name="getProduct"),
]