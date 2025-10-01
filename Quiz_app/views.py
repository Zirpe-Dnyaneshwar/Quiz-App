from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def c(request):
    return render(request,'c.html',)

def cpp(request):
    return render(request,'cpp.html')

def java(request):
    return render(request,'java.html')

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