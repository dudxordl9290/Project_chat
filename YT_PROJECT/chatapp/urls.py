from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'chatapp'

urlpatterns = [
    path('',views.chat_home),
    path('login/', auth_views.LoginView.as_view(template_name='chatapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='chatapp/login.html'), name='logout'),
    path('signup/',views.signup, name='signup'),

    path('join/',views.join, name='join'),
    path('room_list/',views.room_list),
    path('make_room/',views.make_room, name='make_room/'),
    path('db_insert_room/', views.db_insert_room),
]