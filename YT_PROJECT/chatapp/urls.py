from django.urls import path
from . import views

appname = 'chatapp'

urlpatterns = [
    path('',views.chat_home),
    path('join/',views.join, name='join'),
    path('make_room/',views.make_room, name='make_room/'),
    path('db_insert_room/', views.db_insert_room),
]