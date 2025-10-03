"""
URL configuration for Quiz_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Quiz_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('home',views.home,name="home"),
    path('c',views.c,name='cprogram'),
    path('cpp',views.cpp,name='cpp'),
    path('java',views.java,name='java'),
    path('python',views.python,name='python'),
    path('php',views.php,name='php'),
    path('html',views.qhtml,name='html'),
    path('javascript',views.qjavascript,name='javascript'),
    path('login',views.user_login,name='login'),
    path('registration',views.registration,name='registration'),
    path('logout_view', views.logOut,name='logout_view'),
]
