from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from chatapp.models import Room

# Create your views here.

def chat_home(request):
    context = {}
    return render(request, 'chatapp/login.html', context=context)

def create_account(request):
    context = {}
    return render(request, 'chatapp/create_account.html', context=context)

def join(request):
    context = {}
    return render(request, 'chatapp/join.html', context=context)

def room_list(request):
    room_object = Room.objects.all()
    context = {'objects': room_object}
    return render(request, 'chatapp/room_list.html', context=context)

def make_room(request):
    context = {'people_number': range(2,21), 'date_number': range(1,11)}
    return render(request, 'chatapp/make_room.html', context=context)

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