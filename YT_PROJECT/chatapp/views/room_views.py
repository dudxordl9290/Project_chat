from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from chatapp.forms import UserForm

from django.http import HttpResponse
from chatapp.models import Room, Review

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
    room_object = Room.objects.all().order_by('-room_date')
    context = {'objects': room_object}
    return render(request, 'chatapp/room_list.html', context=context)

# 방 생성
@login_required
def make_room(request):
    
    if request.method == 'GET':
        context = {}
        return render(request, 'chatapp/make_room.html', context=context)

    elif request.method == 'POST':
        print(request.FILES.getlist('room_image'))
        if request.method == 'POST':
            room_title = request.POST['room_title']
            room_content = request.POST['room_content']
            room_image = []
            for n in [0,1,2]:
                try:
                    room_image.append(request.FILES.getlist('room_image')[n])
                except:
                    room_image.append('')
            room_date = datetime.today().strftime("%Y/%m/%d %H:%M:%S")  

            Room.objects.create(room_title=room_title, room_content=room_content, 
                                room_image1=room_image[0], room_image2=room_image[1], room_image3=room_image[2], 
                                room_creater=request.user, room_date=room_date)

            context = {'result':'succeed'}
            return render(request, 'chatapp/join.html',context=context)
     
        else:
            context = {}
            return render(request, 'chatapp/make_room.html',context=context)

#방 상세페이지
def detail_room(request, pk):
    room_info = Room.objects.get(id=pk)

    try:
        review_info = Review.objects.filter(review_room=pk).order_by('-review_date')
    except:
        review_info = ''

    print(room_info)
    context = {"room":room_info, "review":review_info, "user":str(request.user)}

    return render(request,'chatapp/detail_room.html', context=context)

# 방 삭제
def delete_room(request, pk):
    Room.objects.get(id=pk).delete()

    return redirect('/room_list/')

# 방 수정
def modify_room(request, pk):
    room_info = Room.objects.get(id=pk)

    if request.method == 'GET':
        context = {'room':room_info}

        return render(request,'chatapp/modify_room.html', context=context)
    
    else:
        room_image = []
        for n in [0,1,2]:
            try:
                room_image.append(request.FILES.getlist('room_image')[n])
            except:
                room_image.append('')
        
        room_info.room_image1=room_image[0]
        room_info.room_image2=room_image[1]
        room_info.room_image3=room_image[2]
        room_info.room_title = request.POST['room_title']
        room_info.room_content = request.POST['room_content']

        room_info.save()

        return redirect('/detail_room/'+str(pk))
        