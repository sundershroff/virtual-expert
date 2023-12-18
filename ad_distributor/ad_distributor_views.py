from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
import requests
from datetime import datetime, date
from django.contrib import messages
import json

jsondec = json.decoder.JSONDecoder()
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
        print(access_Privileges)
        print("main/user")
        if response.status_code == 200:
            return redirect(f"/ad_distributor/ad_distributor_admin_dashboard/{uid}")
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
    try:
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
        return render(request,"ad_dis_upload_acc.html",context)
    except:
        print("no data")
        return render(request,"ad_dis_upload_acc.html")


def admin_dashboard(request,id):
    jsondec=json.decoder.JSONDecoder()
    new=[]
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0]  
    all_profile_finder = requests.get("http://127.0.0.1:3000/alluserdata/").json()
    all_data=requests.get("http://127.0.0.1:3000/all_ads_data/").json()
    signin(request)
    a = access_Privileges

    for i in all_data:
        uid=jsondec.decode(i.get("ad_dis")) 
        id_value = uid['uid']
        if id_value == id:
            new.append(i)
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'all_profile_finder':all_profile_finder[::-1],
        'all_data':new,
        'user_access':a,

    }

    for dict_data in all_data:
        end_date=dict_data['days_required']
        ads_id=dict_data['ad_id']
        last_date= datetime.strptime(end_date,"%Y-%m-%d")
        if last_date <= datetime.today():
            print(ads_id)
            response = requests.post(f"http://127.0.0.1:3000/ad_dis_deactive_update/{ads_id}",data=request.POST )
            print(response)
        else:
            pass
    return render(request,"ad_dis_admin_dashboard.html",context)

    

def account(request,id):
    signin(request)
    a = access_Privileges
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0] 
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'user_access' : access_Privileges

    }

    return render(request,"ad_dis_account.html",context)

def edit_account(request,id):
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0]  
        
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
    
        context = {'key':mydata,'current_path':request.get_full_path(),
                   'response': response, 'region': response,'all':al,
                    'country': countryname,'states': states,'key':mydata,
                    'current_path':request.get_full_path()}
        
        if request.method == "POST":
            print(request.POST)
            response = requests.post(f"http://127.0.0.1:3000/ad_dis_edit_account/{id}", data = request.POST,files=request.FILES)
            print(response)
            print(response.status_code)
            print(response.text)
            return render(request,"ad_dis_account.html",context)
    
        return render(request,"ad_dis_editAccount.html",context)
    except:
        return render(request,"ad_dis_editAccount.html")


def acc_balance(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0] 
    context={
        'key':mydata,
        'current_path':request.get_full_path()

    }

    return render(request,"ad_dis_accntBalance.html",context)

def add_funds(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0] 
    context={
        'key':mydata,
        'current_path':request.get_full_path()

    }

    return render(request,"ad_dis_adFunds.html",context)


def ad_dis_coins(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0] 
    context={
        'key':mydata,
        'current_path':request.get_full_path()

    }

    return render(request,"ad_dis_coins.html",context)


def ads_list_all(request,id):
    signin(request)
    a = access_Privileges
    jsondec=json.decoder.JSONDecoder()
    new=[]
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0]
    all_data=requests.get("http://127.0.0.1:3000/all_ads_data/").json()
    print(id)
    for i in all_data:
        uid=jsondec.decode(i.get("ad_dis")) 
        id_value = uid['uid']
        if id_value == id:
            new.append(i)
        
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'all_data':new,
        'user_access':a,
          }
    
    if "detail" in request.POST:
        print(request.POST)
        global ads_id
        ads_id=request.POST['detail']
        print(ads_id)
        return redirect(f"/ad_distributor/ad_dis_adDetails/{id}")
    
    elif "edi_ad" in request.POST:
        print(request.POST)
        global dis_id
        dis_id = request.POST['edi_ad']
        print(dis_id)
        return redirect(f"/ad_distributor/ad_dis_editAd/{id}")
    else:
        print(request.POST)
        
    return render(request,"ad_dis_list.html",context)
    
    

def ads_active(request,id):
    jsondec=json.decoder.JSONDecoder()
    new=[]
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0] 
    all_data=requests.get("http://127.0.0.1:3000/all_ads_data/").json()
    for i in all_data:
        uid=jsondec.decode(i.get("ad_dis"))
        id_value = uid['uid']
        if id_value == id:
            new.append(i)
    context={'key':mydata,
            'current_path':request.get_full_path(),
            'all_data':new}
    
    if "detail" in request.POST:
        print(request.POST)
        global ads_id
        ads_id=request.POST['detail']
        print(ads_id)
        return redirect(f"/ad_distributor/ad_dis_adDetails/{id}")

   
    else:
        print("no data")
    
    return render(request,"ad_dis_active.html",context)

def ads_pending(request,id):
    jsondec=json.decoder.JSONDecoder()
    new=[]
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0] 
    all_data=requests.get("http://127.0.0.1:3000/all_ads_data/").json()
    
    for i in all_data:
        uid=jsondec.decode(i.get("ad_dis"))
        id_value = uid['uid']
        if id_value == id:
            new.append(i)
    print(new)

    context={'key':mydata,
            'current_path':request.get_full_path(),
            'al_data':new }
    
    if "detail" in request.POST:
        print(request.POST)
        global ads_id
        ads_id=request.POST['detail']
        print(ads_id)
        return redirect(f"/ad_distributor/ad_dis_adDetails/{id}")
    
    return render(request,"ad_dis_pending.html",context)

def ads_deactive(request,id):
    jsondec=json.decoder.JSONDecoder()
    new=[]
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0] 
    all_data=requests.get("http://127.0.0.1:3000/all_ads_data/").json()
    for i in all_data:
        uid=jsondec.decode(i.get("ad_dis"))
        id_value = uid['uid']
        
       
        if id_value == id:
            new.append(i)
    context={'key':mydata,
            'current_path':request.get_full_path(),
            'all_data':new}
    
    if "detail" in request.POST:
        print(request.POST)
        global ads_id
        ads_id=request.POST['detail']
        print(ads_id)
        return redirect(f"/ad_distributor/ad_dis_adDetails/{id}")
    
    
    return render(request,"ad_dis_deactive.html",context)

def ads_closed(request,id):
    jsondec=json.decoder.JSONDecoder()
    new=[]
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0] 
    all_data=requests.get("http://127.0.0.1:3000/all_ads_data/").json()
    for i in all_data:
        uid=jsondec.decode(i.get("ad_dis"))
        id_value = uid['uid']
        if id_value == id:
            new.append(i)

    context={'key':mydata,
            'current_path':request.get_full_path(),
            'all_data':new}
    
    if "detail" in request.POST:
        print(request.POST)
        global ads_id
        ads_id=request.POST['detail']
        print(ads_id)
        return redirect(f"/ad_distributor/ad_dis_adDetails/{id}")
    
    
    return render(request,"ad_dis_closed.html",context)

def ad_dis_createAd(request,id):
    try:
        jsondec=json.decoder.JSONDecoder()
        mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0] 
        # all_data=requests.get("http://127.0.0.1:3000/all_ads_data/").json()
        neww=[]
        new=[]
        response = requests.get('https://api.first.org/data/v1/countries').json()
        
        all = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()

        # dist=requests.get('https://countriesnow.space/api/v0.1/countries/capital').json()
        # statess = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
        # for i in all_data:
        #     uid=jsondec.decode(i.get("ad_dis"))
        #     id_value = uid['uid']
        #     if id_value == uid:
        #         new.append(i)

        states = json.dumps(all["data"])
        
        al = (all["data"])
        for x in al:
            name = (x.get("name"))
            neww.append(name)
        countryname = json.dumps(neww)

        context = {'key':mydata,'current_path':request.get_full_path(),
                    'response': response, 'region': response,'all':al,
                    'country': countryname,'states': states,   'all_data': new}
        
        if "office_state" in request.POST:
            city = request.POST['office_state']
        else:
            city = "None"

        if request.method == "POST":
            print(request.POST)
            data = {
            'ad_name': request.POST['ad_name'],
            'ad_dis': id,
            'category': request.POST['category'],
            'ad_type': request.POST['ad_type'],
            'languages': request.POST['languages'],
            'office_country': request.POST['office_country'],
            'office_state':city,
            'office_district': request.POST['office_district'],
            'gender': request.POST['gender'],
            'age_range': request.POST['age_range'],
             'age_to': request.POST['age_to'],          
            # 'id_card': request.FILES['id_card'],
            'no_views':request.POST['no_views'],
            'days_required':request.POST['days_required'],
            'times_repeat':request.POST['times_repeat'],
            'ad_details':request.POST['ad_details'],
            # 'other_ads':request.FILES['other_ads'],
            'action_name':request.POST['action_name'],
            'action_url':request.POST['action_url']
            # 'reason':request.POST['reason'],   
            }
            print(data)
            response = requests.post(f"http://127.0.0.1:3000/create_ads/{id}", data = data,files=request.FILES)
            # print(response)
            # print(response.status_code)
            # print(response.text)
            return render(request,"ad_dis_payment.html",context)
        return render(request,"ad_dis_createAd.html",context)
    except:
        return render(request,"ad_dis_createAd.html")
    
       

def ad_dis_payment(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()
    context={
        'key':mydata,
        'current_path':request.get_full_path()

    }


    return render(request,"ad_dis_payment.html",context)

def ad_dis_editAd(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0]
    ads_list_all(request,id)
    print(dis_id)
    ads_data=requests.get(f"http://127.0.0.1:3000/ad_dis_ad_details/{dis_id}").json()
    
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'ad_data':ads_data

         }
    
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        response = requests.post(f"http://127.0.0.1:3000/ad_dis_edit_ads/{dis_id}", data = request.POST,files=request.FILES)
        print(response)
        # print(response.status_code)
        # print(response.text)
        return redirect(f"/ad_distributor/ad_dis_list/{id}")

    return render(request,"ad_dis_editad.html",context)

def ad_dis_adDetails(request,id):
    signin(request)
    a=access_Privileges
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0]
    ads_list_all(request,id)
    print(ads_id)
    ads_data=requests.get(f"http://127.0.0.1:3000/ad_dis_ad_details/{ads_id}").json()
    
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'ad_data':ads_data,
        'user_access':a,
         }

    if request.method == "POST":
        print(request.POST)

        if "submit" in request.POST:
            response = requests.post(f"http://127.0.0.1:3000/ad_dis_status_close/{ads_id}", data = request.POST)
            print(response)
            return redirect(f"/ad_distributor/ad_dis_closed/{id}")

        elif "reset" in request.POST:
            print("reset")
            return redirect(f"/ad_distributor/ad_dis_adDetails/{id}")
        
        else:
            print("---")
         
    #     return redirect(f"/ad_distributor/ad_dis_payment/{id}")
    
    return render(request,"ad_dis_adDetails.html",context)

def ad_dis_users(request,id):
    signin(request) 
    a = access_Privileges
    error = ""
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0]
    my_user = requests.get(f"http://127.0.0.1:3000/ad_dis_my_users_data/{id}").json()

    if request.method== "POST":
        print(request.POST)
        if "delete" in request.POST:
           response = requests.post(f"http://127.0.0.1:3000/ad_dis_add_user/{id}",data=request.POST)
           print(response.text)
           print(response.status_code)
           return redirect(f"/ad_distributor/ad_dis_users/{id}")

        elif "edit" in request.POST:
            global user_uid
            user_uid = request.POST['edit']
            return redirect(f"/ad_distributor/ad_dis_user_edit/{id}")
        
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
            response = requests.post(f"http://127.0.0.1:3000/ad_dis_add_user/{id}",data=data)
            # print(response.text)
            # print(response.status_code)
            if response.status_code == 200:
                return redirect(f"http://127.0.0.1:8001/ad_distributor/ad_dis_users/{id}")
            elif response.status_code == 203:
                print("user already exist")
                error = "User Already Exixts"

   

    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'my_user':my_user,
        'error':error,
        'user_access': a

     }
         
     
    return render(request,"ad_dis_users.html",context)



def ad_dis_addusers(request,id):
    error=""
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0]  
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
                             'work':"ad_distributor",
                             'creator':id
            }
           print(data)
           response = requests.post(f"http://127.0.0.1:3000/ad_dis_add_user/{id}",data=data)
           print(response.text)
           print(response.status_code)
           if response.status_code == 200:
              return redirect(f"http://127.0.0.1:8001/ad_distributor/ad_dis_users/{id}")
           elif response.status_code == 203:
              print("user already exist")
              error = "User Already Exixts"
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'error':error,

    }

    return render(request,"ad_dis_addusers.html",context)

def ad_dis_user_edit(request,id):
    ad_dis_users(request,id)
    print(user_uid)
    error=""
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0]
    single_data = requests.get(f"http://127.0.0.1:3000/ad_dis_single_users_data/{user_uid}").json()[0]
    print(single_data)
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
           response = requests.post(f"http://127.0.0.1:3000/ad_dis_add_user/{id}",data=data)
           print(response.text)
           print(response.status_code)
           if response.status_code == 200:
              return redirect(f"http://127.0.0.1:8001/ad_distributor/ad_dis_users/{id}")
           elif response.status_code == 203:
              print("user already exist")
              error = "User Already Exixts"
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'error':error,
        'single_data':single_data,

    }

    return render(request,"ad_dis_user_edit.html",context)

def ad_dis_settings(request,id):
    
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0] 
    context={
        'key':mydata,
        'current_path':request.get_full_path()

    }
    if request.method=="POST":
        print(request.POST)
        if 'pass_reset' in request.POST:
            a=request.POST["pass_reset"]
            print(a)
            response = requests.post(f"http://127.0.0.1:3000/ad_dis_password_reset/{id}",data=request.POST )
        else:
            print(request.POST)
            response = requests.post(f"http://127.0.0.1:3000/ad_dis_email_update/{id}", data = request.POST)
            print(response)
            # print(response.status_code)
            # print(response.text)
            return render(request,"ad_dis_settings.html",context)

    return render(request,"ad_dis_settings.html",context)

def ad_dis_password_reset(request,id):
    print(id)
    if request.method=="POST":
        print(request.POST)
        if 'pass_reset' in request.POST:
            
            a=request.POST["pass_reset"]
            print(a)
        if request.POST['password'] == request.POST['confirm_password']:

            response = requests.post(f"http://127.0.0.1:3000/ad_dis_password_update/{id}",data=request.POST )
            messages.info(request,"Password Successfully Updated")
        else:
            messages.info(request,"Password Incorrect")
    return render(request,"ad_dis_password_reset.html")






    
    


