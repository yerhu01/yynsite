from django.contrib import admin
from django.urls import path

from .views import index, art

urlpatterns = [
    path('', index, name='about'),
    path('art/', art, name='art'),
]