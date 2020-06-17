from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name='post-list'),
    path('<id>/', views.post, name='post-detail'),
]