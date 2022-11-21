from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q

from .models import Video


def index(request):
    videos_list = Video.objects.all()
    template = 'home/index.html'
    context = {
        'videos_list': videos_list
    }
    
    return HttpResponse(render(request, template, context))


def detail(request, video_id):
    video_selected = get_object_or_404(Video, id=video_id)
    videos_list = Video.objects.filter(~Q(id=video_id))
    template = 'home/detail.html'
    context = {
        'video_selected': video_selected, 
        'videos_list': videos_list, 
    }
    
    return HttpResponse(render(request, template, context))