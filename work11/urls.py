from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # views.index は作る必要があります
]
