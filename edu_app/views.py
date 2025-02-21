from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse
from .models import User, Course, Comment, Random_problem
from django.shortcuts import redirect, render
import random
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
    



def test(request):
    return render(request, "test.html")



def result(request):
    if request.method == "POST":
        count = 0
        falses = []
        q_1 = request.POST.get("booleanValue1")
        q_2 = request.POST.get("2.")
        q_3 = request.POST.get("3.")
        q_4 = request.POST.get("4.")
        q_5 = request.POST.get("5.")
        q_6 = request.POST.get("6.")
        q_7 = request.POST.get("7.").strip()
        q_8 = request.POST.get("8.")
        q_9 = request.POST.get("9.")
        q_10 = request.POST.get("10.")
        q_11 = request.POST.get("11.")
        q_12 = request.POST.get("12.")
        if q_1 == "False":
            count += 1
        else:
            falses.append("The first question is flase not true :(")
        if q_2 == "x = 10":
            count += 1
        else:
            falses.append("The correct answer of second question is x = 10")
        if q_3 == "HelloHelloHello":
            count += 1
        else:
            falses.append("The correct answer of third question is HelloHelloHello")
        if q_4 == "False":
            count += 1
        else:
            falses.append("The correct answer of fourth question is False")

        if q_5 == "input()":
            count += 1
        else:
            falses.append("The correct answer of fifth question is input()")
        if q_6 == "15":
            count += 1
        else:
            falses.append("The correct answer of sixth question is 15")
        if q_7 == "0 2 4":
            count += 1
        else:
            falses.append("The correct answer of seventh question is:\n0\n2\n4")
        if q_8 == "def":
            count += 1
        else:
            falses.append("The correct answer of eighth question is def")
        if q_9 == "2":
            count += 1
        else:
            falses.append("The correct answer of 9. question is 2")
        if q_10 == "y":
            count += 1
        else:
            falses.append("The correct answer of 10. question is y")
        if q_11 == "HAHW":
            count += 1
        else:
            falses.append("The correct answer of 11. question is Hello, Alice! Hello, World!")
        if q_12 == "True":
            count += 1
        else:
            falses.append("The correct answer of 12. question is True")
        return render(request, "result.html",{
            "count": count,
            "falses": falses
        })
        
        
    return render(request, "test.html")




def random_problem(request):
    course_name = request.GET.get("course_name")
    problems = []
    ff = Random_problem.objects.filter(course_name="python")
    
    return render(request, "random_problem.html", {"course_name": course_name,
                                                   "ff": ff})

