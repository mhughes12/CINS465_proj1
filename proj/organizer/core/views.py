from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return HttpResponse("Dashboard page")

def join(request):
    return HttpResponse("Join page")

def user_login(request):
    return HttpResponse("Login page")

def user_logout(request):
    return HttpResponse("Logout page")