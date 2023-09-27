from django.shortcuts import render,redirect
from django.http import JsonResponse
import requests


# Create your views here.
def dashboard(request):
    return render(request,"dashboard.html")

def signup(request):
    
    if request.method == "POST":
        if request.POST['password'] == request.POST['confirm_password']:
                # response = requests.post('http://54.159.186.219:8000/signup/',data=request.POST)
                response = requests.post("profile_manager/signup/",data=request.POST)
                print(response.status_code)
                print(response.text)
                uidd = (response.text[1:-1])
                print(uidd)
                return redirect(f"http://127.0.0.1:3000/profile_manager/otp/{uidd}")
        else:
            print("password doesn't match")
    return render(request,"signup.html")

def signin(request):
    # a= requests.get("http://127.0.0.1:3000/pm_alldata/").json()
    # print("YBJ2FMOZN2P" in a)
    # current_path =  request.get_full_path()
    # print(current_path)
    # form1 = ProfileSigninForm()
    error = ""
    if request.method == "POST":
        print(request.POST)
        # response = requests.post("http://54.159.186.219:8000/signin/",data=request.POST)
        response = requests.post("http://127.0.0.1:3000/pm_signin/",data=request.POST)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        print(uidd)
        if response.status_code == 200:
            return redirect(f"/profile_page/{uidd}")
        else:
          error = "YOUR EMAILID OR PASSWORD IS INCORRECT"
    context = {'error':error}
    return render(request,"signin.html",context)

def otp(request,id):
    return render(request,"otpcheck.html")

def profile_picture(request,id):
    return render(request,"profilepicture.html")

def upload_acc(request,id):
    return render(request,"upload_acc.html")

def admin_dashboard(request,id):
    context={
        'admin_dashboard':"admin_dashboard",
    }
    return render(request,"admin_dashboard.html",context)

def profile_account(request,id):
    context={
        'profile_account':"profile_account",
    }
    return render(request,"profile_account.html",context)

def edit_acc(request,id):
    return render(request,"edit_acc.html")

def acc_balance(request,id):
    return render(request,"acc_balance.html")

def profile_finders(request,id):
    return render(request,"profile_finders.html")
    
def view_details(request,id):
    return render(request,"view_details.html")

def complaints(request,id):
    return render(request,"complaints.html")

def users(request,id):
    return render(request,"users.html")

def add_user(request,id):
    return render(request,"add_user.html")

def settings(request,id):
    return render(request,"settings.html")