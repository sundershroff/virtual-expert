from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
import requests
import json
from rest_framework.response import Response
from django.contrib import messages

# Create your views here.
jsondec = json.decoder.JSONDecoder()


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
        print(type(jsondec.decode(response.text)))
        print(jsondec.decode(response.text))
        uidd = jsondec.decode(response.text)
        global access_Privileges
        try:
            access_Privileges = uidd['access_Privileges']
            uid = uidd['uid']

        except:
            access_Privileges = ""
            uid = uidd
        if response.status_code == 200:
            return redirect(f"/sales_manager/sm_salesdashboard/{uid}")
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
    signin(request)
    jsondec = json.decoder.JSONDecoder()
    c=[]
    mydata = requests.get(f"http://127.0.0.1:3000/sm_my_data/{id}").json()[0]  
    all_profile_finder = requests.get("http://127.0.0.1:3000/alluserdata/").json()
    all_client_data=requests.get("http://127.0.0.1:3000/all_client_data/").json()
    for i in all_client_data:
        uid=jsondec.decode(i.get("sales_id"))
        id_value = uid["uid"]
        if id_value==id:
            c.append(i)
    

    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'all_profile_finder':all_profile_finder[::-1],
        'all_client_data':c,
        'access':access_Privileges,
    }
    return render(request,"sm_salesdashboard.html",context)


def profile(request,id):
    signin(request)
    mydata = requests.get(f"http://127.0.0.1:3000/sm_my_data/{id}").json()[0]
    print(mydata)
    print(access_Privileges)
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'access':access_Privileges,
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
                        'current_path':request.get_full_path(),}
            
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
    signin(request)
    jsondec = json.decoder.JSONDecoder()

    c=[]
    mydata = requests.get(f"http://127.0.0.1:3000/sm_my_data/{id}").json()[0] 
    all_client_data= requests.get("http://127.0.0.1:3000/all_client_data/").json()
    # sales=requests.get("http://127.0.0.1:3000/all_sm_data/").json()
    # for i in sales:
    #     uid=(i.get("uid"))
    #     s.append(uid)
    # print(s)
    count=0
    for i in all_client_data:
        
        uid=jsondec.decode(i.get("sales_id"))
        id_value = uid["uid"]
        if id_value==id:
            c.append(i)
            count+=1
        

   
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'all_client_data':c,
        'access':access_Privileges,
        
        
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
        if 'semail' in request.POST:
            print(request.POST['semail'])

            response=requests.post(f"http://127.0.0.1:3000/sendmail/{request.POST['semail']}",data=request.POST)

        
        else:        
            print(request.POST)
            data={
                
                'types_of_activities':request.POST['types_of_activities'],
                'date':request.POST['date'],
                'time':request.POST['time'],
                'notes':request.POST['notes'],
                # 'status':request.POST['status'],       
                
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
    signin(request)
    
    error = ""
    mydata = requests.get(f"http://127.0.0.1:3000/sm_my_data/{id}").json()[0]  
    my_user = requests.get(f"http://127.0.0.1:3000/sm_my_users_data/{id}").json()
    print(my_user)
    if request.method== "POST":
        print(request.POST)
        if "delete" in request.POST:
           response = requests.post(f"http://127.0.0.1:3000/add_user/{id}",data=request.POST)
           print(response.text)
           print(response.status_code)
        elif "edit" in request.POST:
            print(request.POST)
            global user_uid
            user_uid = request.POST['edit']
            return redirect(f"/sales_manager/sm_user_edit/{id}")
        elif "edit_user" in request.POST:
            print(request.POST)
            if request.POST['password'] == request.POST['confirm_password']:
                data={
                    'first_name': request.POST['first_name'],
                    'last_name':request.POST['last_name'],
                        'email': request.POST['email'],
                        'mobile':request.POST['mobile'],
                        'password': request.POST['password'],
                                'access_Privileges':  request.POST.getlist('access_Privileges'),
                                'edit':request.POST['edit_user'],
                }
            print(data)
            response = requests.post(f"http://127.0.0.1:3000/add_user/{id}",data=data)
            # print(response.text)
            # print(response.status_code)
            if response.status_code == 200:
                return redirect(f"http://127.0.0.1:8001/sales_manager/sm_users/{id}")
            elif response.status_code == 203:
                print("user already exist")
                error = "User Already Exixts"

    


    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'my_user':my_user,
        'error':error,
        'access':access_Privileges,


    
    }
    return render(request,"sm_users.html",context)


def add_users(request,id):
    
    print(access_Privileges)
    error=""
    mydata = requests.get(f"http://127.0.0.1:3000/sm_my_data/{id}").json()[0]
    if request.method=="POST":
        print(request.POST)
        if request.POST['password'] == request.POST['confirm_password']:
           data={
                 'first_name': request.POST['first_name'],
                   'last_name':request.POST['last_name'],
                     'email': request.POST['email'],
                       'mobile':request.POST['mobile'],
                         'password': request.POST['password'],
                             'access_Privileges':  request.POST.getlist('access_Privileges'),
                             'work':"sales_manager",
                             'creator':id,
                                # 'location':request.POST['location']
            }
           print(data)
           response = requests.post(f"http://127.0.0.1:3000/add_user/{id}",data=data)
           print(response.text)
           print(response.status_code)
           if response.status_code == 200:
              return redirect(f"http://127.0.0.1:8001/sales_manager/sm_users/{id}")
           elif response.status_code == 203:
              print("user already exist")
              error = "User Already Exixts"
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'error':error,   

    }

    return render(request,"sm_addusers.html",context)


def sm_user_edit(request,id):
    users(request,id)
    print(user_uid)
    error=""
    mydata = requests.get(f"http://127.0.0.1:3000/sm_my_data/{id}").json()[0]
    sm_my_users_data   = requests.get(f"http://127.0.0.1:3000/single_users_data/{user_uid}").json()[0]
    print(sm_my_users_data)
    if request.method=="POST":
        print(request.POST)
        if request.POST['password'] == request.POST['confirm_password']:
           data={
                 'first_name': request.POST['first_name'],
                   'last_name':request.POST['last_name'],
                     'email': request.POST['email'],
                       'mobile':request.POST['mobile'],
                         'password': request.POST['password'],
                             'access_Privileges':  request.POST.getlist('access_Privileges'),
                             'edit':request.POST['edit_user'],
            }
           print(data)
           response = requests.post(f"http://127.0.0.1:3000/add_user/{id}",data=data)
           print(response.text)
           print(response.status_code)
           if response.status_code == 200:
              return redirect(f"http://127.0.0.1:8001/sales_manager/sm_users/{id}")
           elif response.status_code == 203:
              print("user already exist")
              error = "User Already Exixts"
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'error':error,
        'sm_my_users_data':sm_my_users_data,
        

    }

    return render(request,"sm_user_edit.html",context)




def setting(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/sm_my_data/{id}").json()[0]  
    context={
        'key':mydata,
        'current_path':request.get_full_path()
    }


    if request.method=="POST":
        print(request.POST)
        if 'pass_reset' in request.POST:
            
            a=request.POST["pass_reset"]
            print(a)
       
            response = requests.post(f"http://127.0.0.1:3000/password_reset/{id}",data=request.POST )
        else:
            # print(request.POST)
            response = requests.post(f"http://127.0.0.1:3000/sm_email_update/{id}", data = request.POST)
            print(response)
            print(response.status_code)
            print(response.text)
            return render(request,"sm_accountsetting.html",context)

    return render(request,"sm_accountsetting.html",context)


def password_reset(request,id):
    print(id)
    if request.method=="POST":
        print(request.POST)
        if 'pass_reset' in request.POST:
            
            a=request.POST["pass_reset"]
            print(a)
        if request.POST['password'] == request.POST['confirm_password']:

            response = requests.post(f"http://127.0.0.1:3000/pass_sales_update/{id}",data=request.POST )
            messages.info(request,"Password Successfully Updated")
        else:
            messages.info(request,"Password Incorrect")
    return render(request,"password_reset.html")