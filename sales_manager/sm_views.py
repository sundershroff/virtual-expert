from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
import requests
import json
from rest_framework.response import Response

# Create your views here.
def dashboard(request):
    return render(request,"dashboard.html")

def signup(request):
    error = ""
    if request.method == "POST":
        if request.POST['password'] == request.POST['confirm_password']:
                # response = requests.post('http://54.159.186.219:8000/signup/',data=request.POST)
                response = requests.post("http://127.0.0.1:3000/sm_signup/",data=request.POST)
                print(response.status_code)
                print(response.text)
                uidd = (response.text[1:-1])
                print(uidd)
                if response.status_code == 200:
                   return redirect(f"/sales_manager/otp/{uidd}")
                elif response.status_code == 302:
                    error = "User Already Exist"
        else:
            print("password doesn't match")
    context = {'error':error}
    return render(request,"sm_signup.html",context)

def signin(request):
    error = ""
    if request.method == "POST":
        print(request.POST)
        # response = requests.post("http://54.159.186.219:8000/signin/",data=request.POST)
        response = requests.post("http://127.0.0.1:3000/sm_signin/",data=request.POST)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        print(uidd)
        if response.status_code == 200:
            return redirect(f"/sales_manager/sm_salesdashboard/{uidd}")
        else:
          error = "YOUR EMAILID OR PASSWORD IS INCORRECT"
    context = {'error':error}
    return render(request,"sm_signin.html",context)

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
        response = requests.post(f"http://127.0.0.1:3000/sm_otp/{id}", data=data)

       
        print(response)
        print(response.status_code)
        print(data['user_otp'])
        print(response.text)
        uidd = (response.text[1:-1])
        
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            # return redirect(f"/profileidcard/{uidd}")
            return redirect(f"/sales_manager/profile_picture/{uidd}")
        else:
            invalid = "Invalid OTP"
            context = {'invalid':invalid}
    return render(request,"sm_otpcheck.html",context)

def profile_picture(request,id):
    if request.method == "POST":
        print(request.FILES)
        # response = requests.post(f"http://54.159.186.219:8000/profileidcard/{id}",   files=request.FILES)
        response = requests.post(f"http://127.0.0.1:3000/sm_profile_picture/{id}",   files=request.FILES)
        print(response)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/sales_manager/sm_upload_profile/{uidd}")
        else:
            return HttpResponse("INVALId")
    return render(request,"sm_profilepicture.html")

def upload_acc(request,id):
    try:
        #hiring manager list
        hiring_manager = requests.get("http://127.0.0.1:3000/all_hm_data/").json()
        neww=[]
        response = requests.get('https://api.first.org/data/v1/countries').json()
        all = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
        states = json.dumps(all["data"])
        al = (all["data"])
        for x in al:
           name = (x.get("name"))
           neww.append(name)
        countryname = json.dumps(neww)
    
        context = {'response': response, 'region': response,'all':al,
                    'country': countryname,'states': states,'hiring_manager':hiring_manager}
        if request.method == "POST":
            print(request.POST)
            print(request.FILES)
            # response = requests.post(f"http://54.159.186.219:8000/profileidcard/{id}",   files=request.FILES)
            response = requests.post(f"http://127.0.0.1:3000/sm_upload_account/{id}",   data = request.POST,files=request.FILES)
            print(response)
            print(response.status_code)
            print(response.text)
            uidd = (response.text[1:-1])
            if response.status_code == 200:
            # if get["otp"] == data['user_otp']:
                return redirect(f"/sales_manager/sm_salesdashboard/{uidd}")
            else:
                pass
        return render(request,"sm_upload_profile.html",context)
    except:
        return render(request,"sm_upload_profile.html")

    

def verification_fee(request,id):
    return render(request,"sm_verification_fee.html")

def admin_dashboard(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/sm_my_data/{id}").json()[0]  
    all_profile_finder = requests.get("http://127.0.0.1:3000/alluserdata/").json()
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'all_profile_finder':all_profile_finder[::-1],
    }
    return render(request,"sm_salesdashboard.html",context)


def profile(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/sm_my_data/{id}").json()[0]
    print(mydata)  
    context={
        'key':mydata,
        'current_path':request.get_full_path()
    }
    return render(request,"sm_sales_profile.html",context)

def edit_profile(request,id):
        
        try:
            mydata = requests.get(f"http://127.0.0.1:3000/sm_my_data/{id}").json()[0] 
           
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
                response = requests.post(f"http://127.0.0.1:3000/sm_edit_data/{id}", data = request.POST,files=request.FILES)
                print(response)
                print(response.status_code)
                print(response.text)
                return render(request,"sm_sales_profile.html",context)
            return render(request,"sm_editprofile.html",context)
        
            
        except:
            return render(request,"sm_editprofile.html")


def account_balance(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/sm_my_data/{id}").json()[0]  
    context={
        'key':mydata,
        'current_path':request.get_full_path()
    }
    return render(request,"sm_accountbalance.html",context)




def coin_details(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/sm_my_data/{id}").json()[0]  
    context={
        'key':mydata,
        'current_path':request.get_full_path()
    }
    return render(request,"sm_coindetails.html",context)

def hand_list(request,id):

    jsondec = json.decoder.JSONDecoder()

    c=[]
    mydata = requests.get(f"http://127.0.0.1:3000/sm_my_data/{id}").json()[0] 
    all_client_data= requests.get("http://127.0.0.1:3000/all_client_data/").json()
    # sales=requests.get("http://127.0.0.1:3000/all_sm_data/").json()
    # for i in sales:
    #     uid=(i.get("uid"))
    #     s.append(uid)
    # print(s)
    for i in all_client_data:
        uid=jsondec.decode(i.get("sales_id"))
        id_value = uid["uid"]
        if id_value==id:
            c.append(i)


   
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'all_client_data':c,
        
    }
   
   
    if request.method == "POST":
        
        if 'view' in request.POST:
            print(request.POST)
            global uid_view
            uid_view = request.POST['view']
            return redirect(f"/sales_manager/sm_ad_details/{id}")
        
        elif 'active' in request.POST:
            a=request.POST["active"]
            print(a)
            response = requests.post(f"http://127.0.0.1:3000/add_client_data/{id}",data=request.POST )

            
        else:     
            print(request.POST)
            print(request.FILES)
            data={
                "sales_id":id,
                'client_type':request.POST['client_type'],
                'client_name':request.POST['client_name'],
                'client_location':request.POST['client_location'],
                'category':request.POST['category'],
                'google_map':request.POST['google_map'],
                'phone_number':request.POST['phone_number'],
                'email':request.POST['email'],
                'picture':request.FILES


            }

           
            response = requests.post(f"http://127.0.0.1:3000/add_client_data/{id}", data =data,files=request.FILES)

            print(response.status_code)
            print(response.text)
            uidd = (response.text[1:-1])
            if response.status_code == 200:
            # if get["otp"] == data['user_otp']:
                # return redirect(f"/sales_manager/add_client/{uidd}")
                return redirect(f"/sales_manager/sm_hand_list/{uidd}")
            
            else:
                print("invalid")
                return render(request,"sm_hand_list.html",context)
        
    return render(request,"sm_hand_list.html",context)






def otp_client(request,id):
    context = {'invalid':"invalid"}
    new=[]
    if request.method == "POST":
        new.append(request.POST["otp1"])
        new.append(request.POST["otp2"])
        new.append(request.POST["otp3"])
        new.append(request.POST["otp4"])
        new.append(request.POST["otp5"])
        new.append(request.POST["otp6"])

        data = {
            'user_otp':int(''.join(new).strip())
           
        }
        print(data)
        response = requests.post(f"http://127.0.0.1:3000/client_otp/{id}", data=data)

       
        print(response)
        print(response.status_code)
        print(data['user_otp'])
        print(response.text)
        uidd = (response.text[1:-1])
        
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            # return redirect(f"/profileidcard/{uidd}")
            return redirect(f"/sales_manager/sm_hand_list/{uidd}")

        else:
            invalid = "Invalid OTP"
            context = {'invalid':invalid}
    return render(request,"sm_hand_list.html",context)


     
def ads_list(request,id):
    jsondec = json.decoder.JSONDecoder()
    c=[]
    mydata = requests.get(f"http://127.0.0.1:3000/sm_my_data/{id}").json()[0]
    client_activities=requests.get("http://127.0.0.1:3000/all_activities/").json()
    all_client_data= requests.get("http://127.0.0.1:3000/all_client_data/").json()

    for i in all_client_data:
        uid=jsondec.decode(i.get("sales_id"))
        id_value = uid["uid"]
        if id_value==id:
            c.append(i)

    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'all_client_data':c,
        'client_activities':client_activities,
        
        
        }
    if request.method == "POST":     
        print(request.POST)
        data={
            
            'types_of_activities':request.POST['types_of_activities'],
            'date':request.POST['date'],
            'time':request.POST['time'],
            'notes':request.POST['notes'],
            
            
        }
    
        response = requests.post(f"http://127.0.0.1:3000/add_client_activities/{request.POST['client_name']}", data =data)
        print(response.status_code)
        print(response.text)
        return redirect(f"/sales_manager/sm_ads_list/{id}")
    return render(request,"sm_ads_list.html",context)




def ad_details(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/sm_my_data/{id}").json()[0]
    hand_list(request,id)
    print(uid_view)
    viewid=requests.get(f"http://127.0.0.1:3000/view_client_id/{uid_view}").json()
    print(viewid)
    context={

        'key':mydata,
        'current_path':request.get_full_path(),
        'viewid':viewid,
        
    }
    return render(request,"sm_ad_details.html",context)


def edit_ad_details(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/sm_my_data/{id}").json()  
    context={
        'key':mydata,
        'current_path':request.get_full_path()
    }
    return render(request,"sm_edit_adDetail.html",context)

def users(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/sm_my_data/{id}").json()[0]  
    context={
        'key':mydata,
        'current_path':request.get_full_path()
    }
    return render(request,"sm_users.html",context)

def add_users(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/sm_my_data/{id}").json()[0]
    context={
        'key':mydata,
        'current_path':request.get_full_path()
    }
    return render(request,"sm_addusers.html",context)


def setting(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/sm_my_data/{id}").json()[0]  
    context={
        'key':mydata,
        'current_path':request.get_full_path()
    }
    return render(request,"sm_accountsetting.html",context)

