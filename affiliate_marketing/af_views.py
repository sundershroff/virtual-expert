from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
import requests
import json

# Create your views here.
def dashboard(request):
    return render(request,"dashboard.html")

def signin(request):
    error = ""
    if request.method == "POST":
        print(request.POST)
        # response = requests.post("http://54.159.186.219:8000/signin/",data=request.POST)
        response = requests.post("http://127.0.0.1:3000/am_signin/",data=request.POST)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        print(uidd)
        if response.status_code == 200:
            return redirect(f"/affiliate_marketing/af_profile/{uidd}")
        else:
          error = "YOUR EMAILID OR PASSWORD IS INCORRECT"
    context = {'error':error}
    return render(request,"af_signin.html",context)

def signup(request):
    error = ""
    if request.method == "POST":
        if request.POST['password'] == request.POST['confirm_password']:
                # response = requests.post('http://54.159.186.219:8000/signup/',data=request.POST)
                response = requests.post("http://127.0.0.1:3000/am_signup/",data=request.POST)
                print(response.status_code)
                print(response.text)
                uidd = (response.text[1:-1])
                print(uidd)
                if response.status_code == 200:
                   return redirect(f"/affiliate_marketing/otp/{uidd}")
                elif response.status_code == 302:
                    error = "User Already Exist"
        else:
            print("password doesn't match")
    context = {'error':error}
    return render(request,"af_signup.html",context)

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
        response = requests.post(f"http://127.0.0.1:3000/am_otp/{id}", data=data)

       
        print(response)
        print(response.status_code)
        print(data['user_otp'])
        print(response.text)
        uidd = (response.text[1:-1])
        
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            # return redirect(f"/profileidcard/{uidd}")
            return redirect(f"/affiliate_marketing/profile_picture/{uidd}")
        else:
            invalid = "Invalid OTP"
            context = {'invalid':invalid}
    return render(request,"af_otpcheck.html",context)

def profile_picture(request,id):
    if request.method == "POST":
        print(request.FILES)
        # response = requests.post(f"http://54.159.186.219:8000/profileidcard/{id}",   files=request.FILES)
        response = requests.post(f"http://127.0.0.1:3000/am_profile_picture/{id}",   files=request.FILES)
        print(response)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/affiliate_marketing/af_uploadprofile/{uidd}")
        else:
            return HttpResponse("INVALId")
    return render(request,"af_profilepicture.html")

def upload_acc(request,id):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        # response = requests.post(f"http://54.159.186.219:8000/profileidcard/{id}",   files=request.FILES)
        response = requests.post(f"http://127.0.0.1:3000/am_upload_account/{id}",   data = request.POST,files=request.FILES)
        print(response)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/affiliate_marketing/af_profile/{uidd}")
        else:
            return HttpResponse("INVALId")
    return render(request,"af_uploadprofile.html")

def profile(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/my_aff_data/{id}").json()[0] 
    context={
        'key':mydata,
        'current_path':request.get_full_path()
    }
    return render(request,"af_profile.html",context)

def edit_profile(request,id):
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/my_aff_data/{id}").json()[0]       
        neww=[]
        response = requests.get('https://api.first.org/data/v1/countries').json()
        all = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
        # statess = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
        states = json.dumps(all["data"])
        al = (all["data"])
        for x in al:
            name = (x.get("name"))
            neww.append(name)
        countryname = json.dumps(neww)
            

        context = {"key":mydata,
                'current_path':request.get_full_path(),'response': response, 'region': response,'all':al,
                    'country': countryname,'states': states,'key':mydata,
                    'current_path':request.get_full_path()}
        
        if request.method=="POST":
            print(request.POST)
            response = requests.post(f"http://127.0.0.1:3000/am_edit_account/{id}", data = request.POST,files=request.FILES)
            print(response)
            print(response.status_code)
            print(response.text)
            return render(request,"af_editprofile.html",context)

        return render(request,"af_editprofile.html",context)
        
            
    except:
        return render(request,"af_editprofile.html")


def commisions(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/my_aff_data/{id}").json()[0]
    context={
        'key':mydata,
        'current_path':request.get_full_path()
    }
    return render(request,"af_commisions.html",context)

def setting(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/my_aff_data/{id}").json()[0]
    context={
        'key':mydata,
        'current_path':request.get_full_path()
    }
    if request.method=="POST":
        print(request.POST)
        response = requests.post(f"http://127.0.0.1:3000/aff_email_update/{id}", data = request.POST)
        print(response)
        print(response.status_code)
        print(response.text)
        return render(request,"af_setting.html",context)


    return render(request,"af_setting.html",context)

