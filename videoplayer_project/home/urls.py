from django.urls import path

from . import views


app_name = 'home'
urlpatterns = [
    path("", views.index, name="index"), 
    path("<int:video_id>/", views.detail, name="detail"), 
    path("<int:video_id>/post_comment/", views.post_comment, name="post_comment"), 
    path("search/", views.search, name="search"), 
]
