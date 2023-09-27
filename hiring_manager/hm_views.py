from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request,"dashboard.html")

def signup(request):
    return render(request,"hm_signup.html")

def signin(request):
    return render(request,"hm_signin.html")

def otp(request,id):
    return render(request,"hm_otpcheck.html")

def profile_picture(request,id):
    return render(request,"hm_profilepicture.html")

def upload_acc(request,id):
    return render(request,"hm_upload_acc.html")

# def admin_dashboard(request,id):
#     context={
#         'admin_dashboard':"admin_dashboard",
#     }
#     return render(request,"admin_dashboard.html",context)
