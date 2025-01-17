from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse
from .models import User
# Create your views here.


def index(request):
    return render(request, "index.html")

def courses(request):
    return render(request, "courses.html")

def challenges(request):
    return render(request, "challenges.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "error": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")


def join_to_login(request):
    return render(request, "login_after_join.html")

def user_login_after_join(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "join.html")
        else:
            return render(request, "login.html", {
                "error": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")
    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))




def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation_pass = request.POST["confirmation"]
        if password != confirmation_pass:
            return render(request, "signup.html", {"error": "Passwords don't match."})
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "signup.html", {"error": "Username already taken."})
        if User.objects.filter(email=email).exists():
            return render(request, "signup.html", {"error": "Email already taken."})
        login(request, user)
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "signup.html")
    


def profile(request):
    return render(request, "profile.html")

def learn(request):
    return render(request, "join.html")