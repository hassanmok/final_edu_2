from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("courses", views.courses, name="courses"),
    path("challenges", views.challenges, name="challenges"),
    path("login", views.user_login, name="login"),
    path("login_after_join", views.user_login_after_join, name="login_after_join"),
    path("join_to_login", views.join_to_login, name="join_to_login"),
    path("signup", views.signup, name="signup"),
    path("logout", views.user_logout, name="logout"),
    path("profile", views.profile, name="profile"),
    path("learn", views.learn, name="learn"),
]