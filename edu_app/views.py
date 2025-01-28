from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse
from .models import User, Course, Comment
# Create your views here.


def index(request):
    return render(request, "index.html")

def courses(request):
    all_comment = Comment.objects.all()
    return render(request, 'courses.html', {'all_comment': all_comment})

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
    course = Course.objects.get(course_name="python_for_begginer")
    document = course.course_document

    document_lines = document.splitlines()
    paginator = Paginator(document_lines, 20)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, "join.html", {"page_obj": page_obj})


def add_comment(request):
    if request.method == "POST":
        user = request.user
        comment = request.POST["comment"]
        course = Course.objects.get(course_name="python_for_begginer")
        the_comment = Comment(user = user, comment_text = comment, course = course)
        the_comment.save()
        return HttpResponseRedirect(reverse('courses'))
    return HttpResponseRedirect(reverse('courses'))
    

