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
            return redirect(f"/ad_distributor/ad_distributor_admin_dashboard/{uidd}")
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
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0]  
    all_profile_finder = requests.get("http://127.0.0.1:3000/alluserdata/").json()
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'all_profile_finder':all_profile_finder[::-1],

    }
    return render(request,"ad_dis_admin_dashboard.html",context)

    

def account(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0] 
    context={
        'key':mydata,
        'current_path':request.get_full_path()

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

def ads_list_all(request,id):
    jsondec=json.decoder.JSONDecoder()
    new=[]
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0]
    all_data=requests.get("http://127.0.0.1:3000/all_ads_data/").json()
    for i in all_data:
        uid=jsondec.decode(i.get("ad_dis"))
        id_value = uid['uid']
        if id_value == id:
            new.append(i)

    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'all_data':new,

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
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0] 
    all_data=requests.get("http://127.0.0.1:3000/all_ads_data/").json()
    context={'key':mydata,
            'current_path':request.get_full_path(),}
    for dict_data in all_data:
        status=dict_data['status']
        
        if status == "Active" or status == "active":
            context1={
            'key':mydata,
            'current_path':request.get_full_path(),
            'all_data':all_data

            }
            return render(request,"ad_dis_active.html",context1)
    else:
        print("no data")
    return render(request,"ad_dis_active.html",context)

def ads_pending(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0]
    all_data=requests.get("http://127.0.0.1:3000/all_ads_data/").json()
    context={'key':mydata,
            'current_path':request.get_full_path(),}
    for dict_data in all_data:
        status=dict_data['status']
        
        if status == "Pending" or status == "pending":
            context1={
            'key':mydata,
            'current_path':request.get_full_path(),
            'all_data':all_data

            }
            return render(request,"ad_dis_pending.html",context1)
    return render(request,"ad_dis_pending.html",context)

def ads_deactive(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0] 
    all_data=requests.get("http://127.0.0.1:3000/all_ads_data/").json()
    context={'key':mydata,
            'current_path':request.get_full_path(),}
    for dict_data in all_data:
        status=dict_data['status']        
        if status == "deactive" or status == "Deactive":
            context1={
            'key':mydata,
            'current_path':request.get_full_path(),
            'all_data':all_data

            }
            return render(request,"ad_dis_deactive.html",context1)
    return render(request,"ad_dis_deactive.html",context)

def ads_closed(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0] 
    all_data=requests.get("http://127.0.0.1:3000/all_ads_data/").json()
    context={'key':mydata,
            'current_path':request.get_full_path(),}
    for dict_data in all_data:
        status=dict_data['status']        
        if status == "Closed" or status == "closed":
            context1={
            'key':mydata,
            'current_path':request.get_full_path(),
            'all_data':all_data

            }
            return render(request,"ad_dis_closed.html",context1)
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
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0]
    ads_list_all(request,id)
    print(ads_id)
    ads_data=requests.get(f"http://127.0.0.1:3000/ad_dis_ad_details/{ads_id}").json()
    
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'ad_data':ads_data

         }

    # if request.POST:
    #     return redirect(f"/ad_distributor/ad_dis_payment/{id}")
    
    return render(request,"ad_dis_adDetails.html",context)

def ad_dis_users(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0] 
    context={
        'key':mydata,
        'current_path':request.get_full_path()

    }

    return render(request,"ad_dis_users.html",context)


def ad_dis_addusers(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0] 
    context={
        'key':mydata,
        'current_path':request.get_full_path()

    }


    return render(request,"ad_dis_addusers.html",context)


def ad_dis_settings(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{id}").json()[0] 
    context={
        'key':mydata,
        'current_path':request.get_full_path()

    }

    return render(request,"ad_dis_settings.html",context)



