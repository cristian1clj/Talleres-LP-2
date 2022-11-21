from django.urls import path

from . import views


app_name = 'acount'
urlpatterns = [
    path("login/", views.login, name="login"), 
    path("signup/logincheck/", views.logincheck, name="logincheck"), 
    path("signup/", views.signup, name="signup"), 
    path("signup/signuprecord/", views.signuprecord, name="signuprecord")
]
