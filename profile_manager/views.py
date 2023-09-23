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

def profile_picture(request,id):
    return render(request,"profilepicture.html")

def upload_acc(request,id):
    return render(request,"upload_acc.html")

def admin_dashboard(request,id):
    return render(request,"admin_dashboard.html")

def profile_account(request,id):
    return render(request,"profile_account.html")

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