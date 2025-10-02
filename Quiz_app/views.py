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
    questions = Python_Question.objects.all()
    return render(request,'python.html',{'questions': questions})

def php(request):
    questions = PHP_Question.objects.all()
    return render(request,'php.html',{'questions': questions})

def qhtml(request):
    questions = HTML_Question.objects.all()
    return render(request,'qhtml.html',{'questions': questions})

def qjavascript(request):
    questions = Javascript_Question.objects.all()
    return render(request,'qjavascript.html',{'questions': questions})

def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')