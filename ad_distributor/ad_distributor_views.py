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
                response = requests.post("http://127.0.0.1:3000/ad_dis_signup/",data=request.POST)
                print(response.status_code)
                print(response.text)
                uidd = (response.text[1:-1])
                print(uidd)
                if response.status_code == 200:
                   return redirect(f"/ad_distributor/otp/{uidd}")
                elif response.status_code == 302:
                    error = "User Already Exist"
        else:
            print("password doesn't match")
    context = {'error':error}
    return render(request,"ad_dis_signup.html",context)

def signin(request):
    error = ""
    if request.method == "POST":
        print(request.POST)
        # response = requests.post("http://54.159.186.219:8000/signin/",data=request.POST)
        response = requests.post("http://127.0.0.1:3000/ad_dis_signin/",data=request.POST)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        print(uidd)
        if response.status_code == 200:
            return redirect(f"/ad_distributor/dashboard/{uidd}")
        else:
          error = "YOUR EMAILID OR PASSWORD IS INCORRECT"
    context = {'error':error}
    return render(request,"ad_dis_signin.html",context)

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
        response = requests.post(f"http://127.0.0.1:3000/ad_dis_otp/{id}", data=data)

       
        print(response)
        print(response.status_code)
        print(data['user_otp'])
        print(response.text)
        uidd = (response.text[1:-1])
        
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            # return redirect(f"/profileidcard/{uidd}")
            return redirect(f"/ad_distributor/profile_picture/{uidd}")
        else:
            invalid = "Invalid OTP"
            context = {'invalid':invalid}
    return render(request,"ad_dis_otpcheck.html",context)

def profile_picture(request,id):
    if request.method == "POST":
        print(request.FILES)
        # response = requests.post(f"http://54.159.186.219:8000/profileidcard/{id}",   files=request.FILES)
        response = requests.post(f"http://127.0.0.1:3000/ad_dis_profile_picture/{id}",   files=request.FILES)
        print(response)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/ad_distributor/upload_acc/{uidd}")
        else:
            return HttpResponse("INVALId")
    return render(request,"ad_dis_profilepicture.html")

def upload_acc(request,id):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        # response = requests.post(f"http://54.159.186.219:8000/profileidcard/{id}",   files=request.FILES)
        response = requests.post(f"http://127.0.0.1:3000/ad_dis_upload_account/{id}",   data = request.POST,files=request.FILES)
        print(response)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/ad_distributor/ad_distributor_admin_dashboard/{uidd}")
        else:
            return HttpResponse("INVALId")
    return render(request,"ad_dis_upload_acc.html")


def admin_dashboard(request,id):
    return render(request,"ad_dis_admin_dashboard.html")

def account(request,id):
    return render(request,"ad_dis_account.html")

def edit_account(request,id):
    return render(request,"ad_dis_editAccount.html")


def acc_balance(request,id):
    return render(request,"ad_dis_accntBalance.html")

def add_funds(request,id):
    return render(request,"ad_dis_adFunds.html")

def ads_list_all(request,id):
    return render(request,"ad_dis_list.html")

def ads_active(request,id):
    return render(request,"ad_dis_active.html")

def ads_pending(request,id):
    return render(request,"ad_dis_pending.html")

def ads_deactive(request,id):
    return render(request,"ad_dis_deactive.html")

def ads_closed(request,id):
    return render(request,"ad_dis_closed.html")

def ad_dis_createAd(request,id):
    if request.POST:
        return redirect("/ad_distributor/ad_dis_payment/<id>")
    return render(request,"ad_dis_createAd.html")

def ad_dis_payment(request,id):
    return render(request,"ad_dis_payment.html")

def ad_dis_editAd(request,id):
    if request.POST:
        return redirect("/ad_distributor/ad_dis_payment/<id>")
    return render(request,"ad_dis_editad.html")

def ad_dis_adDetails(request,id):
    if request.POST:
        return redirect("/ad_disvider/ad_dis_payment/<id>")
    return render(request,"ad_dis_adDetails.html")

def ad_dis_users(request,id):
    return render(request,"ad_dis_users.html")


def ad_dis_addusers(request,id):
    return render(request,"ad_dis_addusers.html")

def ad_dis_settings(request,id):
    return render(request,"ad_dis_settings.html")



