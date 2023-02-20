from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from chatapp.forms import UserForm

from django.http import HttpResponse
from chatapp.models import Room

from datetime import datetime

# Create your views here.

# home view (로그인 상태: join.html, 미로그인 상태:login.html)
def chat_home(request):
    if not request.user.is_authenticated:
        return render(request, 'chatapp/login.html',{})
    else:
        return render(request, 'chatapp/join.html', {})

#계정 생성 view
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            authenticate(username=username, password=raw_password)  # 사용자 인증
            # login(request, user)  # 로그인
            return render(request,'chatapp/login.html',context={})
    else:
        form = UserForm()
    return render(request, 'chatapp/signup.html', {'form':form})

#방 참가 view
@login_required
def join(request):
    context = {}
    return render(request, 'chatapp/join.html', context=context)

#방 리스트 view
@login_required
def room_list(request):
    room_object = Room.objects.all()
    context = {'objects': room_object}
    return render(request, 'chatapp/room_list.html', context=context)

@login_required
def make_room(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'chatapp/make_room.html', context=context)

    elif request.method == 'POST':
        print(request.user)
        if request.method == 'POST':
            room_title = request.POST['room_title']
            room_content = request.POST['room_content']
            # room_creater = request.POST['room_creater']
            room_date = datetime.today().strftime("%Y/%m/%d %H:%M:%S")  

            Room.objects.create(room_title=room_title, room_content=room_content, room_creater=request.user, room_date=room_date)

            context = {'result':'succeed'}
            return render(request, 'chatapp/join.html',context=context)
     
        else:
            context = {}
            return render(request, 'chatapp/make_room.html',context=context)

def detail_room(request, pk):
    openroom = Room.objects.filter(id=pk)
    context = {"roominfo":openroom}
    print(context)
    return render(request,'chatapp/detail_room.html', context=context)