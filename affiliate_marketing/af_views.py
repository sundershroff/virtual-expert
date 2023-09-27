from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request,"dashboard.html")

def signup(request):
    return render(request,"af_signup.html")

def signin(request):
    return render(request,"af_signin.html")

def otp(request,id):
    return render(request,"af_otpcheck.html")

def profile_picture(request,id):
    return render(request,"af_profilepicture.html")

def upload_acc(request,id):
    return render(request,"af_uploadprofile.html")

def profile(request,id):
    return render(request,"af_profile.html")

def edit_profile(request,id):
    return render(request,"af_editprofile.html")

def commisions(request,id):
    return render(request,"af_commisions.html")

def setting(request,id):
    return render(request,"af_setting.html")