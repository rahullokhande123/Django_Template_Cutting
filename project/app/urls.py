from django.urls import path
from app import views

urlpatterns=[
    path('', views.home, name='home'),
    path('my_link/', views.my_link, name='my_link')
]