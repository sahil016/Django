from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
""" 
def signup(request):
    if request.methos=="POST":
        
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['cpassword']
        if password==confirm_password:
            user=user.objects.create_user(username,email,password)
            user.save()
            return render(request,'login.html')
        else:
            return render(request,'signup.html',{'error':'password and confirm password do not match'})
    
    return render(request, 'signup.html') """
    
def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['cpassword']

        if password == confirm_password:
            if User.objects.filter(name=name).exists():
                return render(request, 'signup.html', {'error': 'Username already exists'})
            if User.objects.filter(email=email).exists():
                return render(request, 'signup.html', {'error': 'Email already exists'})

            user = User.objects.create_user(name=name, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            ##  # Redirect to the login page after successful signup
        else:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})

    return render(request, 'signup.html')