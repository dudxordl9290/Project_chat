from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from chatapp.forms import UserForm

from django.http import HttpResponse
from chatapp.models import Room


# Create your views here.

def chat_home(request):
    context = {}
    return render(request, 'chatapp/login.html', context=context)

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            # login(request, user)  # 로그인
            return render(request, '/chatapp/login.html', {})
    else:
        form = UserForm()
    return render(request, '/chatapp/login.html', {})

@login_required
def join(request):
    context = {}
    return render(request, 'chatapp/join.html', context=context)

def room_list(request):
    room_object = Room.objects.all()
    context = {'objects': room_object}
    return render(request, 'chatapp/room_list.html', context=context)

def make_room(request):
    context = {}
    return render(request, 'chatapp/create_account.html', context=context)

def db_insert_room(request):
     print(request)
     if request.method == 'POST':
        room_name = request.POST['room_name']
        room_subject = request.POST['room_subject']
        limit_people = request.POST['limit_people']
        limit_date = request.POST['limit_date']
        print(room_name, room_subject, limit_date, limit_people)
        Room.objects.create(room_name=room_name, room_subject=room_subject, limit_people=limit_people, limit_date=limit_date)

        context = {'result':'succeed'}
        return render(request, 'chatapp/join.html',context=context)
     
     else:
        context = {}
        return render(request, 'chatapp/make_room.html',context=context)