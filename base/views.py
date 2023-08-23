from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    try:
        #Username Spliting for Homepage
        if request.user:
            str1 = request.user.username
            if "@" in str1:
                x = str1.split("@")
                username = x[1].split(".")
                username = username[0] + ' ' + username[1]
            else:
                username = request.user.username
    except Exception as e:
        username = request.user.username

    return render(request,'index.html',{'username':username})

#Custom Django Login Settings

def login_page(request):
    if request.method=='POST':
        username= request.POST.get('username').lower()    
        password= request.POST.get('password') 
        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'login.html')

def registerpage(request):
    if request.method=='POST':
        username= request.POST.get('username').lower() 
        password= request.POST.get('password1')
        firstname= request.POST.get('firstname')
        lastname= request.POST.get('lastname')
        email= request.POST.get('email')
        user = User(username=username,first_name=firstname,last_name=lastname,email=email)
        user.set_password(password)
        user.save()
        return redirect('home')
    return render(request,'register.html') 

def handleLogout(request):
    logout(request)
    return redirect("/") 