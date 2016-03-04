from django.shortcuts import render, render_to_response
from datetime import datetime
from blog.models import Review

def hello(request):
    return render(request, "hello.html", { })


def hello_name(request, yourname):
    return render(request, "hello_name.html", { "yourname": yourname })


def dolittle(request):
    return render (request, "dolittle.html", {"dolittle.html": dolittle })

def time(request):
    return render (request, "time.html", {"time": datetime.now() })

def number(request):
    return render (request, "number.html", {"random num": number.random})

def all_reviews(request):
    return render (request, "all_review.html",{"reviews": Review.objects.all()})