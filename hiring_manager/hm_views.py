from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
import requests
import json
# Create your views here.
jsondec = json.decoder.JSONDecoder()
def dashboard(request):
    return render(request,"dashboard.html")

def signup(request):
    error = ""
    if request.method == "POST":
        if request.POST['password'] == request.POST['confirm_password']:
                # response = requests.post('http://54.159.186.219:8000/signup/',data=request.POST)
                response = requests.post("http://127.0.0.1:3000/hm_signup/",data=request.POST)
                print(response.status_code)
                print(response.text)
                uidd = (response.text[1:-1])
                print(uidd)
                if response.status_code == 200:
                   return redirect(f"/hiring_manager/otp/{uidd}")
                elif response.status_code == 302:
                    error = "User Already Exist"
        else:
            print("password doesn't match")
    context = {'error':error}
    return render(request,"hm_signup.html",context)

def signin(request):
    error = ""
    if request.method == "POST":
        print(request.POST)
        # response = requests.post("http://54.159.186.219:8000/signin/",data=request.POST)
        response = requests.post("http://127.0.0.1:3000/hm_signin/",data=request.POST)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        print(uidd)
        if response.status_code == 200:
            return redirect(f"/hiring_manager/hm_admin_dashboard/{uidd}")
        else:
          error = "YOUR EMAILID OR PASSWORD IS INCORRECT"
    context = {'error':error}
    return render(request,"hm_signin.html",context)

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
        response = requests.post(f"http://127.0.0.1:3000/hm_otp/{id}", data=data)

       
        print(response)
        print(response.status_code)
        print(data['user_otp'])
        print(response.text)
        uidd = (response.text[1:-1])
        
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            # return redirect(f"/profileidcard/{uidd}")
            return redirect(f"/hiring_manager/profile_picture/{uidd}")
        else:
            invalid = "Invalid OTP"
            context = {'invalid':invalid}
    return render(request,"hm_otpcheck.html",context)

def profile_picture(request,id):
    if request.method == "POST":
        print(request.FILES)
        # response = requests.post(f"http://54.159.186.219:8000/profileidcard/{id}",   files=request.FILES)
        response = requests.post(f"http://127.0.0.1:3000/hm_profile_picture/{id}",   files=request.FILES)
        print(response)
        print(response.status_code)
        print(response.text)
        uidd = (response.text[1:-1])
        if response.status_code == 200:
        # if get["otp"] == data['user_otp']:
            return redirect(f"/hiring_manager/hm_upload_acc/{uidd}")
        else:
            return HttpResponse("INVALId")
    return render(request,"hm_profilepicture.html")

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
            response = requests.post(f"http://127.0.0.1:3000/hm_upload_account/{id}",   data = request.POST,files=request.FILES)
            print(response)
            print(response.status_code)
            print(response.text)
            uidd = (response.text[1:-1])
            if response.status_code == 200:
            # if get["otp"] == data['user_otp']:
                return redirect(f"/hiring_manager/hm_admin_dashboard/{uidd}")
            else:
                pass
        return render(request,"hm_upload_acc.html",context)
    except:
        return render(request,"hm_upload_acc.html")


def admin_dashboard(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]  
    #profile manager
    if requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]['my_profile_manager'] == None:
        pm_data =""
    else:
        pm_data = jsondec.decode(requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]['my_profile_manager'])    

    #ad provider
    if requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]['ad_provider'] == None:
        ad_pro_data =""
    else:
        ad_pro_data = jsondec.decode(requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]['ad_provider']) 


    #sales
    if requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]['sales_manager'] == None:
        sales_data =""
    else:
        sales_data = jsondec.decode(requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]['sales_manager'])

    print(pm_data)

    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'pm_data':pm_data,
        'ad_pro_data':ad_pro_data,
        'sales_data':sales_data,
    }
    return render(request,"hm_admin_dashboard.html",context)


def profile(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]  
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
    }
    return render(request,"hm_profile.html",context)

def edit_acc(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]
    try:
       neww=[]
       response = requests.get('https://api.first.org/data/v1/countries').json()
       all = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
       states = json.dumps(all["data"])
       al = (all["data"])
       for x in al:
          name = (x.get("name"))
          neww.append(name)
       countryname = json.dumps(neww)
   
       context={
           'key':mydata,
           'current_path':request.get_full_path(),
           'response': response, 
           'region': response,'all':al,
           'country': countryname,'states': states
       }
       if request.method == "POST":
           print(request.POST)
           response = requests.post(f"http://127.0.0.1:3000/hm_edit_account/{id}",data=request.POST,files = request.FILES)
           print(response)
           print(response.status_code)
           print(response.text)
       return render(request,"hm_edit_acc.html",context)
    except:
        context={
           'key':mydata,
           'current_path':request.get_full_path(),
       }
        return render(request,"hm_edit_acc.html",context)


def local_admin(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0] 
    if requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]['my_profile_manager'] == None:
        pm_data =""
    else:
        pm_data = jsondec.decode(requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]['my_profile_manager'])    
    if request.method=="POST":
        print("hello")
        if 'uid' in request.POST:
            print(request.POST)
            global uid 
            uid = request.POST['uid']
            return redirect(f"/hiring_manager/hm_local_admin_upload/{id}")
        else:
            print(request.POST)
            print(request.FILES)
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'pm_data':pm_data
    }
    return render(request,"hm_localadmin.html",context)

def local_admin_upload(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]  
    local_admin(request,id)
    pm_data = requests.get(f"http://127.0.0.1:3000/pm_myid/{uid}").json()[0] 
    #country api 
    neww=[]
    response = requests.get('https://api.first.org/data/v1/countries').json()
    all = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
    states = json.dumps(all["data"])
    al = (all["data"])
    for x in al:
       name = (x.get("name"))
       neww.append(name)
    countryname = json.dumps(neww)

    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'pm_data':pm_data,
        'response': response,
        'region': response,
        'all':al,
        'country': countryname,'states': states
    }

    if request.method == "POST":
        response = requests.post(f"http://127.0.0.1:3000/profile_manager_upload_account/{request.POST['uid']}",data=request.POST,files = request.FILES)
        print(response.status_code)
        return redirect(f"/hiring_manager/hm_local_admin/{id}")
    return render(request,"hm_LocaladminDoc.html",context)

def ad_provider(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]  
    #ad provider
    if requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]['ad_provider'] == None:
        ad_pro_data =""
    else:
        ad_pro_data = jsondec.decode(requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json() [0]['ad_provider']) 
    if request.method=="POST":
        if 'uid' in request.POST:
            print(request.POST)
            global uid 
            uid = request.POST['uid']
            return redirect(f"/hiring_manager/hm_adprovider_upload/{id}")
        else:
            print(request.POST)
            print(request.FILES)
        
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'ad_pro_data':ad_pro_data,
    }
    return render(request,"hm_ad_provider.html",context)

def ad_provider_doc(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]  
    ad_provider(request,id)
    print(uid)
    ad_pro_my_data = requests.get(f"http://127.0.0.1:3000/ad_pro_my_data/{uid}").json()[0]  
    #country api
    neww=[]
    response = requests.get('https://api.first.org/data/v1/countries').json()
    all = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
    states = json.dumps(all["data"])
    al = (all["data"])
    for x in al:
       name = (x.get("name"))
       neww.append(name)
    countryname = json.dumps(neww)

    
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'ad_pro_my_data':ad_pro_my_data,
        'response': response,
        'region': response,
        'all':al,
        'country': countryname,'states': states
    }
    
    if request.method == "POST":
        response = requests.post(f"http://127.0.0.1:3000/ad_provider_upload_account/{request.POST['uid']}",data=request.POST,files = request.FILES)
        print(response.status_code)
        return redirect(f"/hiring_manager/hm_ad_provider/{id}")

    return render(request,"hm_adproviderdoc.html",context)

def sales(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]  
    if requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]['sales_manager'] == None:
        sales_data =""
    else:
        sales_data = jsondec.decode(requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]['sales_manager'])
    if request.method=="POST":
        if 'uid' in request.POST:
            global uid 
            uid = request.POST['uid']
            return redirect(f"/hiring_manager/hm_sales_person_doc/{id}")
        else:
            pass
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'sales_data':sales_data,
    }
    
    return render(request,"hm_sales_person.html",context)

def sales_doc(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0] 
    sales(request,id)
    sales_my_data = requests.get(f"http://127.0.0.1:3000/sm_my_data/{uid}").json()[0]  
    #country api
    neww=[]
    response = requests.get('https://api.first.org/data/v1/countries').json()
    all = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
    states = json.dumps(all["data"])
    al = (all["data"])
    for x in al:
       name = (x.get("name"))
       neww.append(name)
    countryname = json.dumps(neww)
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'sales_my_data':sales_my_data,
        'response': response,
        'region': response,
        'all':al,
        'country': countryname,'states': states
    } 
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        response = requests.post(f"http://127.0.0.1:3000/sales_upload_account/{request.POST['uid']}",data=request.POST,files = request.FILES)
        print(response.status_code)
        return redirect(f"/hiring_manager/hm_sales_person/{id}")

    return render(request,"hm_sales_person_doc.html",context)

def hiring_manager(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0] 
    if requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]['hiring_manager'] == None:
        hirinng_data =""
    else:
        hirinng_data = jsondec.decode(requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]['hiring_manager'])

    if request.method=="POST":
        print(request.POST)
        global uid 
        uid = request.POST['uid']
        return redirect(f"/hiring_manager/hm_hiring_manager_doc/{id}")
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'hirinng_data':hirinng_data,
    } 
    return render(request,"hm_hiring_manager.html",context)

def hiring_manager_doc(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]  
    hiring_manager(request,id)
    hiring_my_data = requests.get(f"http://127.0.0.1:3000/hm_my_data/{uid}").json()[0]  
    #country api
    neww=[]
    response = requests.get('https://api.first.org/data/v1/countries').json()
    all = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
    states = json.dumps(all["data"])
    al = (all["data"])
    for x in al:
       name = (x.get("name"))
       neww.append(name)
    countryname = json.dumps(neww)
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'hiring_my_data':hiring_my_data,
        'response': response,
        'region': response,
        'all':al,
        'country': countryname,'states': states
    } 
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        response = requests.post(f"http://127.0.0.1:3000/hiring_upload_account/{request.POST['uid']}",data=request.POST,files = request.FILES)
        print(response.status_code)
        return redirect(f"/hiring_manager/hm_hiring_manager/{id}")
    return render(request,"hm_hiring_manager_doc.html",context)

def setting(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/hm_my_data/{id}").json()[0]  
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
    }
    return render(request,"hm_acc_setting.html",context)




