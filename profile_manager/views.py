from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request,"dashboard.html")

def signup(request):
    return render(request,"signup.html")

def signin(request):
    return render(request,"signin.html")

def otp(request,id):
    return render(request,"otpcheck.html")

