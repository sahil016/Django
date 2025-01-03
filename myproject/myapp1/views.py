from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')


def cpass(request):
    if request.method=="POST":
        try:
            user = User.objects.get(email=request.session['email'])

            if user.password==request.POST['opassword']:
                if request.POST['npassword']==request.POST['cnpassword']:
                    user.password=request.POST['npassword']
                    user.save()
                    return redirect('logout')
                else:
                    msg = "Password & confirm password does not match"
                    return render(request, 'cpass.html',{'msg':msg})
            else:
                msg = "Old Password does not match"
                return render(request, 'cpass.html',{'msg':msg})
                    
        except Exception as e:
            msg = f"An error occurred: {e}"
            return render(request, 'cpass.html', {'msg': msg})
            
    else:
        return render(request,'cpass.html')


def about(request):
    return render(request, 'about.html')

 
def contact(request):
    return render(request, 'contact.html')

def signup(request):
    if request.method=="POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            msg = "Email already exists!!"
            return render(request,'signup.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    
                    name = request.POST['name'],
                    email = request.POST['email'],
                    mobile = request.POST['mobile'],
                    password = request.POST['password']
                )

                msg = "Signup Succesfuly"
                return render(request,'login.html',{'msg':msg})
            else:
                msg = "Password & confirm password does not match"
                return render(request,'signup.html',{'msg':msg})
    else:  # Handle GET request
        return render(request, 'signup.html')  # Render the signup page with no messages

def login(request):
    if request.method=="POST":
        try:
            user = User.objects.get(email=request.POST['email'])

            if user.password == request.POST['password']:
                request.session['email']=user.email

                return redirect('index')
            else:
                msg = "Invalid Password!!"
                return render(request,'login.html',{'msg':msg})
            
        except:
            msg = "Invalid Email!!"
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')


def logout(request):
    del request.session['email']
    return redirect('login')



def fpass(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            msg = "Password sent to your email"
            return render(request,'fpass.html',{'msg':msg})
        except:
            msg = "Invalid Email!!"
            return render(request,'fpass.html',{'msg':msg})
    else:
        msg = "Email not found!!"
        return render(request,'fpass.html',{'msg':msg})
