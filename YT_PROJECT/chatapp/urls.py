from django.urls import path
from .views import room_views, review_views
from django.contrib.auth import views as auth_views


app_name = 'chatapp'

urlpatterns = [
    path('',room_views.chat_home),
    path('login/', auth_views.LoginView.as_view(template_name='chatapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='chatapp/login.html'), name='logout'),
    path('signup/',room_views.signup, name='signup'),

    path('join/',room_views.join, name='join'),
    path('room_list/',room_views.room_list),
    path('make_room/',room_views.make_room, name='make_room'),
    path('detail_room/<int:pk>/', room_views.detail_room, name='detail_room'),
    path('delete_room/<int:pk>/', room_views.delete_room, name='delete_room'),

    path('make_review/<int:pk>/', review_views.make_review, name='make_review'),
]