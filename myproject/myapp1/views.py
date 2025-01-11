from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import random
import requests

# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')


""" def cpass(request):
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
                    
        except User.DoesNotExist:
            # Handle case where the user is not found (in case of session issues)
            msg = "User not found"
            return render(request, 'cpass.html', {'msg': msg})

        except Exception as e:
            # Catch any other unexpected exceptions and log them if necessary
            print(f"An error occurred: {e}")
            msg = "An unexpected error occurred"
            return render(request, 'cpass.html', {'msg': msg})
            
    else:
        return render(request,'cpass.html')
 """


from django.shortcuts import render, redirect
from .models import User

def cpass(request):
    if request.method == "POST":
        try:

            user = User.objects.get(email=request.session['email'])

           
            if user.password == request.POST['opassword']:
               
                if request.POST['npassword'] == request.POST['cnpassword']:
                    user.password = request.POST['npassword']
                    user.save()
                    return redirect('logout')  
                else:
                
                    msg = "Password & confirm password do not match"
                    return render(request, 'cpass.html', {'msg': msg})

            else:
                
                msg = "Old Password does not match"
                return render(request, 'cpass.html', {'msg': msg})

       
        except Exception as e:
            
            print("*************",e)
            
            return render(request, 'cpass.html')

    else:
        return render(request, 'cpass.html')



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
            if request.POST['password']==request.POST['password']:
                User.objects.create(
                    
                    name = request.POST['name'],
                    email = request.POST['email'],
                    mobile = request.POST['mobile'],
                    password = request.POST['password'],
                    profile = request.FILES['profile']
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
                request.session['profile']=user.profile.url

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
    del request.session['profile']
    return redirect('login')



def fpass(request):
    if request.method == "POST":
        try:
            user = User.objects.get(mobile=request.POST['mobile'])
            mobile =  request.POST['mobile']
            otp = random.randint(1001,9999) 
            url = "https://www.fast2sms.com/dev/bulkV2"

            querystring = {"authorization":"4FLqt2yEconSrjiDwMvY19AXNB308IKZpWTkehHuxf7bVdG5aOjkV09BWEUrcpAST5JOZQs2dFoYxe8D","variables_values":str(otp),"route":"otp","numbers":str(mobile)}

            headers = {
                'cache-control': "no-cache"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            print(response.text)
           
            request.session['mobile']=user.mobile
            request.session['otp']=otp
            
            return render(request,'otp.html')
        
        except Exception as e:
                msg = "Mobile not found!!"
                print('***************',e) 
                return render(request,'fpass.html',{'msg':msg})
    
           
    else:
        return render(request,'fpass.html')

def otp(request):
    if request.method == "POST":
        
        try:
            uotp = request.POST.get('uotp')  # Get user input OTP as a string
            otp = str(request.session.get('otp'))  # Convert session OTP to a string
            
            print(f"Session OTP: {otp}")
            print(f"User entered OTP: {uotp}")

            
            if otp == uotp:
                del request.session['otp']
                return render(request,'newpass.html')
            else:
                msg = "Invalid OTP!!"
                return render(request,'otp.html',{'msg':msg})
            
            
        except Exception as e:
            print(f"Error during OTP validation: {e}")
            return render(request,'otp.html')
            
def newpass(request):
    if request.method == "POST":
        try:
            user = User.objects.get(mobile=request.session['mobile'])
            if request.POST['npassword']==request.POST['cnpassword']:
                user.password = request.POST['npassword']
                user.save()
                del request.session['mobile']
                return redirect('login')
            else:
                msg = "New password & confirm new passwoerd does not match!!"   
                return render(request,'newpass.html',{'msg':msg})
        except User.DoesNotExist:
            msg = "User does not exist or session expired."
            return render(request, 'newpass.html', {'msg': msg})
        
        except Exception as e:
            print('***************',e)
            msg = "An unexpected error occurred. Please try again."
            return render(request, 'newpass.html', {'msg': msg})
    else:
        return render(request, 'newpass.html')
    
    
def cprofile(request):
    user = User.objects.get(email=request.session['email'])
    
    if request.method == "POST":
    
        user.name=request.POST['name']
        user.mobile=request.POST['mobile']
        try:
            user.profile = request.FILES['profile']
            user.save()
            request.session['uprofile']=user.profile.url
            return redirect('index')
        except Exception as e:
            print(f"Error during profile update: {e}")
        user.save()
        return redirect('index')
        
        
    else:
        return render(request,'cprofile.html',{'user':user})