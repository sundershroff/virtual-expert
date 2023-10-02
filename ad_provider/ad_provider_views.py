from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
import requests

# Create your views here.
def dashboard(request):
    return render(request,"dashboard.html")

def signup(request):
    error = ""
    if request.method == "POST":
        if request.POST['password'] == request.POST['confirm_password']:
                # response = requests.post('http://54.159.186.219:8000/signup/',data=request.POST)
                response = requests.post("http://127.0.0.1:3000/ad_pro_signup/",data=request.POST)
                print(response.status_code)
                print(response.text)
                uidd = (response.text[1:-1])
                print(uidd)
                if response.status_code == 200:
                   return redirect(f"/ad_provider/otp/{uidd}")
                elif response.status_code == 302:
                    error = "User Already Exist"
        else:
            print("password doesn't match")
    context = {'error':error}
    return render(request,"ad_provider_signup.html",context)

def signin(request):
    error = ""
    if request.method == "POST":
        print(request.POST)
        # response = requests.post("http://54.159.186.219:8000/signin/",data=request.POST)
        response = requests.post("http://127.0.0.1:3000/ad_pro_signin/",data=request.POST)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        print(uidd)
        if response.status_code == 200:
            return redirect(f"/ad_provider/dashboard/{uidd}")
        else:
          error = "YOUR EMAILID OR PASSWORD IS INCORRECT"
    context = {'error':error}
    return render(request,"ad_provider_signin.html",context)

def otp(request,id):
    context = {'invalid':"invalid"}
    new=[]
    if request.method == "POST":
        new.append(request.POST["otp1"])
        new.append(request.POST["otp2"])
        new.append(request.POST["otp3"])
        new.append(request.POST["otp4"])
        data = {
            'user_otp':int(''.join(new).strip())
           
        }
        print(data)
        # response = requests.post(f"http://54.159.186.219:8000/otp/{id}",   data=data)
        response = requests.post(f"http://127.0.0.1:3000/ad_pro_otp/{id}", data=data)

       
        print(response)
        print(response.status_code)
        print(data['user_otp'])
        print(response.text)
        uidd = (response.text[1:-1])
        
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            # return redirect(f"/profileidcard/{uidd}")
            return redirect(f"/ad_provider/profile_picture/{uidd}")
        else:
            invalid = "Invalid OTP"
            context = {'invalid':invalid}
    return render(request,"ad_provider_otpcheck.html",context)

def profile_picture(request,id):
    if request.method == "POST":
        print(request.FILES)
        # response = requests.post(f"http://54.159.186.219:8000/profileidcard/{id}",   files=request.FILES)
        response = requests.post(f"http://127.0.0.1:3000/ad_pro_profile_picture/{id}",   files=request.FILES)
        print(response)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/ad_provider/upload_acc/{uidd}")
        else:
            return HttpResponse("INVALId")
    return render(request,"ad_provider_profilepicture.html")

def upload_acc(request,id):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        # response = requests.post(f"http://54.159.186.219:8000/profileidcard/{id}",   files=request.FILES)
        response = requests.post(f"http://127.0.0.1:3000/ad_pro_upload_account/{id}",   data = request.POST,files=request.FILES)
        print(response)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:

            return redirect(f"/ad_distributor/ad_provider_admin_dashboard/{uidd}")
        else:
            return HttpResponse("INVALId")
    return render(request,"ad_ptovider_upload_acc.html")

def admin_dashboard(request,id):
    return render(request,"ad_provider_admin_dashboard.html")

def account(request,id):
    return render(request,"ad_pro_account.html")

def edit_account(request,id):
    return render(request,"ad_pro_editAccount.html")


def acc_balance(request,id):
    return render(request,"ad_pro_accntBalance.html")

def add_funds(request,id):
    return render(request,"ad_pro_adFunds.html")

def ads_list_all(request,id):
    return render(request,"ad_pro_list.html")

def ads_active(request,id):
    return render(request,"ad_pro_active.html")

def ads_pending(request,id):
    return render(request,"ad_pro_pending.html")

def ads_deactive(request,id):
    return render(request,"ad_pro_deactive.html")

def ads_closed(request,id):
    return render(request,"ad_pro_closed.html")

def ad_pro_createAd(request,id):
    if request.POST:
        return redirect("/ad_provider/ad_pro_payment/<id>")
    return render(request,"ad_pro_createAd.html")

def ad_pro_payment(request,id):
    return render(request,"ad_pro_payment.html")

def ad_pro_editAd(request,id):
    if request.POST:
        return redirect("/ad_provider/ad_pro_payment/<id>")
    return render(request,"ad_pro_editad.html")

def ad_pro_adDetails(request,id):
    if request.POST:
        return redirect("/ad_provider/ad_pro_payment/<id>")
    return render(request,"ad_pro_adDetails.html")

def ad_pro_users(request,id):
    return render(request,"ad_pro_users.html")


def ad_pro_addusers(request,id):
    return render(request,"ad_pro_addusers.html")

def ad_pro_settings(request,id):
    return render(request,"ad_pro_settings.html")







