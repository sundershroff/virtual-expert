from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
import requests
import json


# Create your views here.
def dashboard(request):
    return render(request,"dashboard.html")

def signup(request):
    error = ""
    if request.method == "POST":
        if request.POST['password'] == request.POST['confirm_password']:
                # response = requests.post('http://54.159.186.219:8000/signup/',data=request.POST)
                response = requests.post("http://127.0.0.1:3000/pm_signup/",data=request.POST)
                print(response.status_code)
                print(response.text)
                uidd = (response.text[1:-1])
                print(uidd)
                if response.status_code == 200:
                   return redirect(f"/profile_manager/otp/{uidd}")
                elif response.status_code == 302:
                    error = "User Already Exist"
        else:
            print("password doesn't match")
    context = {'error':error}
    return render(request,"signup.html",context)

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
            return redirect(f"/profile_manager/admin_dashboard/{uidd}")
        else:
          error = "YOUR EMAILID OR PASSWORD IS INCORRECT"
    context = {'error':error}
    return render(request,"signin.html",context)

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
        response = requests.post(f"http://127.0.0.1:3000/pm_otp/{id}", data=data)

       
        print(response)
        print(response.status_code)
        print(data['user_otp'])
        print(response.text)
        uidd = (response.text[1:-1])
        
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            # return redirect(f"/profileidcard/{uidd}")
            return redirect(f"/profile_manager/profile_picture/{uidd}")
        else:
            invalid = "Invalid OTP"
            context = {'invalid':invalid}
    return render(request,"otpcheck.html",context)

def profile_picture(request,id):
    if request.method == "POST":
        print(request.FILES)
        # response = requests.post(f"http://54.159.186.219:8000/profileidcard/{id}",   files=request.FILES)
        response = requests.post(f"http://127.0.0.1:3000/pm_profile_picture/{id}",   files=request.FILES)
        print(response)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/profile_manager/upload_acc/{uidd}")
        else:
            return HttpResponse("INVALId")
    return render(request,"profilepicture.html")

def upload_acc(request,id):
    neww=[]
    response = requests.get('https://api.first.org/data/v1/countries').json()
    # region = (requests.get('https://api.first.org/data/v1/countries').json())
    all = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
    # statess = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
    states = json.dumps(all["data"])
    al = (all["data"])
    for x in al:
       name = (x.get("name"))
       neww.append(name)
    countryname = json.dumps(neww)

    context = {'response': response, 'region': response,'all':al,
                                          'country': countryname,'states': states}
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        # response = requests.post(f"http://54.159.186.219:8000/profileidcard/{id}",   files=request.FILES)
        response = requests.post(f"http://127.0.0.1:3000/pm_edit_account/{id}",   data = request.POST,files=request.FILES)
        print(response)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/profile_manager/admin_dashboard/{uidd}")
        else:
            return HttpResponse("INVALId")
    return render(request,"upload_acc.html",context)

def admin_dashboard(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/pm_my_data/{id}").json()[0]  
    context={
        'key':mydata,
        'current_path':request.get_full_path()

    }
    return render(request,"admin_dashboard.html",context)

def profile_account(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/pm_my_data/{id}").json()[0]  
    context={
        'key':mydata,
        'current_path':request.get_full_path()

    }
    return render(request,"profile_account.html",context)

def edit_acc(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/pm_my_data/{id}").json()[0]  
    context={
        'key':mydata,
        'current_path':request.get_full_path()

    }
    return render(request,"edit_acc.html",context)

def acc_balance(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/pm_my_data/{id}").json()[0]  
    context={
        'key':mydata,
        'current_path':request.get_full_path()

    }
    return render(request,"acc_balance.html",context)

def profile_finders(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/pm_my_data/{id}").json()[0]  
    context={
        'key':mydata,
        'current_path':request.get_full_path()

    }
    return render(request,"profile_finders.html",context)
    
def view_details(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/pm_my_data/{id}").json()[0]  
    context={
        'key':mydata,
        'current_path':request.get_full_path()

    }
    return render(request,"view_details.html",context)

def complaints(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/pm_my_data/{id}").json()[0]  
    context={
        'key':mydata,
        'current_path':request.get_full_path()

    }
    return render(request,"complaints.html",context)

def users(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/pm_my_data/{id}").json()[0]  
    context={
        'key':mydata,
        'current_path':request.get_full_path()

    }
    return render(request,"users.html",context)

def add_user(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/pm_my_data/{id}").json()[0]  
    context={
        'key':mydata,
        'current_path':request.get_full_path()

    }
    return render(request,"add_user.html",context)

def settings(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/pm_my_data/{id}").json()[0]  
    context={
        'key':mydata,
        'current_path':request.get_full_path()

    }
    return render(request,"settings.html",context)