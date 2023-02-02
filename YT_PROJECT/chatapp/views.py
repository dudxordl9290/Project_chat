from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView

# Create your views here.

def chat_home(request):
    context = {}
    return render(request, 'chatapp/login.html', context=context)

def join(request):
    context = {}
    return render(request, 'chatapp/join.html', context=context)