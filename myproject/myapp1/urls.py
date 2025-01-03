"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from myapp1 import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),  # This will map the home view to the root URL
    path('about', views.about, name='about'),
    path('cpass', views.cpass, name='cpass'),
    path('signup', views.signup, name='signup'),
    path('login' ,views.login, name='login'),
    path('logout' ,views.logout, name='logout'),
    path('fpass' ,views.fpass, name='fpass'),
]

