from django.urls import path
from . import views

appname = 'chatapp'

urlpatterns = [
    path('',views.chat_home),
    path('create_account/',views.create_account),
    path('join/',views.join, name='join'),
    path('room_list/',views.room_list),
    path('make_room/',views.make_room, name='make_room/'),
    path('db_insert_room/', views.db_insert_room),
]