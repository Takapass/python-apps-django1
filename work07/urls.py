from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),           # トップページ
    path('omikuji/', views.omikuji, name='omikuji'),
    path('janken/', views.janken, name='janken'),
    path('hilow/', views.hilow, name='hilow'),
]
