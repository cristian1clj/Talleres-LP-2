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


def search(request):
    video_title = request.GET['search-navbar']
    video_searched = get_object_or_404(Video, title=video_title)
    videos_list = Video.objects.filter(~Q(id=video_searched.id))
    
    template = 'home/detail.html'
    context = {
        'video_selected': video_searched, 
        'videos_list': videos_list, 
    }
    
    return HttpResponse(render(request, template, context))


def post_comment(request, video_id):
    new_comment = request.POST['commentInput']
    vid = get_object_or_404(Video, id=video_id)
    videos_list = Video.objects.filter(~Q(id=vid.id))
    
    vid.comment_set.create(
        video = vid, 
        comment_text = new_comment
    )
    comments_list = vid.comment_set.all()
    
    template = 'home/detail.html'
    context = {
        'video_selected': vid, 
        'videos_list': videos_list, 
        'comments_list': comments_list, 
    }
    
    return HttpResponse(render(request, template, context))