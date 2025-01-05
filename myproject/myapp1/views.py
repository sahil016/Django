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
            # Check if the email is in the session, and handle accordingly
            if 'email' not in request.session:
                msg = "You must be logged in to change your password."
                return redirect('login')  # Redirect to the login page if email is not found in session

            # Get the user from the session email
            user = User.objects.get(email=request.session['email'])

            # Check if the old password matches
            if user.password == request.POST['opassword']:
                # Check if the new password and confirm new password match
                if request.POST['npassword'] == request.POST['cnpassword']:
                    user.password = request.POST['npassword']
                    user.save()
                    return redirect('logout')  # Redirect to logout after successful password change
                else:
                    # Passwords don't match, return error message
                    msg = "Password & confirm password do not match"
                    return render(request, 'cpass.html', {'msg': msg})

            else:
                # Old password does not match, return error message
                msg = "Old Password does not match"
                return render(request, 'cpass.html', {'msg': msg})

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
        # Handle GET request (render the form)
        if 'email' not in request.session:
            # Redirect to login page if the user is not logged in
            return redirect('login')
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
            uotp=request.POST['uotp']
            otp= int(request.session['otp'])
            
            if otp == uotp:
                del request.session['otp']
                return render(request,'newpass.html')
            else:
                msg = "Invalid OTP!!"
                return render(request,'otp.html',{'msg':msg})
            
            
        except Exception as e:
            print("*****************",e)
            return render(request,'otp.html')
            
def newpass(request):
    if request.method == "POST":
        try:
            user = User.objects.get(mmobile=request.session['mobile'])
            if request.POST['npassword']==request.POST['cpassword']:
                user.password = request.POST['npassword']
                user.save()
                del request.session['mobile']
                return redirect('login')
            else:
                msg = "New password & confirm new passwoerd does not match!!"
                
                return render(request,'newpass.html',{'msg':msg})
            
        except Exception as e:
            print('***************',e)