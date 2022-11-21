from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from .models import User


def login(request):
    template = 'acount/login.html'
    
    return HttpResponse(render(request, template, {}))


def logincheck(request):
    pass


def signup(request):
    template = 'acount/signup.html'
    
    return HttpResponse(render(request, template, {}))


def signuprecord(request):
    un = request.POST['username']
    em = request.POST['email_address']
    pw = request.POST['password']
    
    user = User(
        username = un, 
        email_address = em, 
        password = pw
    )
    user.save()
    
    return HttpResponse(render(request, "acount/login.html", {}))