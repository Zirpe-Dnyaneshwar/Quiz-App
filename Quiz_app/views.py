from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    questions = Question.objects.all()
    return render(request,'home.html',{'questions': questions})

def c(request):
    questions = Clanguage_Question.objects.all()
    return render(request,'c.html',{'questions': questions})

def cpp(request):
    questions = Cpp_Question.objects.all()
    return render(request,'cpp.html',{'questions': questions})

def java(request):
    questions = Java_Question.objects.all()
    return render(request,'java.html',{'questions': questions})

def python(request):
    return render(request,'python.html')

def php(request):
    return render(request,'php.html')

def qhtml(request):
    return render(request,'qhtml.html')

def qjavascript(request):
    return render(request,'qjavascript.html')

def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')