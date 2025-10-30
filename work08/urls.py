from django.urls import path
from . import views

urlpatterns = [
    path('', views.memo_list, name='memo_list'),
    path('edit/<int:memo_id>/', views.memo_edit, name='memo_edit'),
    path('create/', views.memo_create, name='memo_create'),
    path('delete/<int:memo_id>/', views.memo_delete, name='memo_delete'),
]
