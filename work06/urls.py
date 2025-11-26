from django.contrib import admin
from django.urls import path
from . import views  # views.py が同じアプリにある場合

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # 例: views.index を呼び出す
]
