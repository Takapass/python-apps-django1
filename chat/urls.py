from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("rooms/", views.room_list, name="room_list"),
    path("rooms/<int:room_id>/", views.chat_room, name="chat_room"),
    path("rooms/<int:room_id>/send/", views.send_message, name="send_message"),
    path('profile/', views.profile_view, name='profile'),
    path('rooms/create/', views.create_room, name='create_room'),
]
