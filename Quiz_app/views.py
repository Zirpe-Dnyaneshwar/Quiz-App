from django.shortcuts import render ,redirect,HttpResponse
from .models import *
from .form import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

def user_login(request):
    if request.method == "POST":
        form = Userloginform(request.POST)
        if form.is_valid():
            username1 = request.POST.get('username')
            password1 = request.POST.get('password')
            user1 = authenticate(request, username=username1, password=password1)
            if user1:
                if user1.is_active:
                    login(request, user1)   
                    return redirect('home')
                else:
                    return HttpResponse("Invalid Person")
            else:
                return HttpResponse("Not Allowed To visit Website")
        else:
            return HttpResponse("Invalid Details")          
    else:
        form = Userloginform()
        return render(request, 'login.html', {'form': form})

def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():   
            new_user = form.save(commit=False)  
            new_user.save()  
            return redirect("login")  
        else:
            print(form.errors)   
    else:
        form = UserCreationForm()
    return render(request, "registration.html", {"form": form})

def logOut(request):
    logout(request)
    return redirect('home')