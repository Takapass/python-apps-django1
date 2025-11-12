from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ai/', views.ai_suggestion, name='ai_suggestion'),
]
