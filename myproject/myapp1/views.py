from django.shortcuts import render,redirect
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
    if request.method=="POST":
        try:
            user = User.objacts.get(email=request.POST['email'])
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
            else:
                return render(request,'signup.html')
            

def login(request):
    if request.method=="POST":
        try:
            user = User.objects.get(email=request.POST['email'])

            if user.password == request.POST['password']:
                request.session['email']=user.email

                return redirect('index')
            else:
                msg = "Invalid Password!!
                return redirect(request,'login.html',('msg':msg))
            
        except:
