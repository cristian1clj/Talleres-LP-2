from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Members


def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template("index.html")
    context = {
        'mymembers': mymembers
    }
    
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template("add.html")
    
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    
    member = Members(firstname=x, lastname=y)
    member.save()
    
    return HttpResponseRedirect(reverse('index'))


def update(request, id):
    member = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    
    context = {
        'member': member
    }
    
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    x = request.POST['first']
    y = request.POST['last']
    
    member = Members.objects.get(id=id)
    member.firstname = x
    member.lastname = y
    member.save()
    
    return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    
    return HttpResponseRedirect(reverse('index'))


def test(request):
    members = Members.objects.all().values()
    template = loader.get_template('test.html')
    
    context = {
        'members': members
    }
    
    return HttpResponse(template.render(context, request))