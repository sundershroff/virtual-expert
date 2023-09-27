from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request,"dashboard.html")

def signup(request):
    return render(request,"sm_signup.html")

def signin(request):
    return render(request,"sm_signin.html")

def otp(request,id):
    return render(request,"sm_otpcheck.html")

def profile_picture(request,id):
    return render(request,"sm_profilepicture.html")

def upload_acc(request,id):
    return render(request,"sm_upload_profile.html")

def verification_fee(request,id):
    return render(request,"sm_verification_fee.html")

def admin_dashboard(request,id):

    return render(request,"sm_salesdashboard.html")


def profile(request,id):
    return render(request,"sm_sales_profile.html")


def edit_profile(request,id):
    return render(request,"sm_editprofile.html")

def account_balance(request,id):
    return render(request,"sm_accountbalance.html")

def coin_details(request,id):
    return render(request,"sm_coindetails.html")

def hand_list(request,id):
    return render(request,"sm_hand_list.html")

def ads_list(request,id):
    return render(request,"sm_ads_list.html")

def ad_details(request,id):
    return render(request,"sm_ad_details.html")

def edit_ad_details(request,id):
    return render(request,"sm_edit_adDetail.html")

def users(request,id):
    return render(request,"sm_users.html")

def add_users(request,id):
    return render(request,"sm_addusers.html")


def setting(request,id):
    return render(request,"sm_accountsetting.html")

