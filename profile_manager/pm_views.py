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
            response = requests.post(f"http://127.0.0.1:3000/pm_complete_account/{id}",   data = request.POST,files=request.FILES)
            print(response)
            print(response.status_code)
            print(response.text)
            uidd = (response.text[1:-1])
            if response.status_code == 200:
            # if get["otp"] == data['user_otp']:
                return redirect(f"/profile_manager/admin_dashboard/{uidd}")
            else:
               return redirect(f"/profile_manager/upload_acc/{uidd}")
        return render(request,"upload_acc.html",context)
    except:
        context = {'response': "response", 'region': "response",'all':"al",
                    'country': "countryname",'states': "states",'hiring_manager':"hiring_manager"}
        return render(request,"upload_acc.html",context)

def admin_dashboard(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/pm_my_data/{id}").json()[0]  
    all_profile_finder = requests.get("http://127.0.0.1:3000/alluserdata/").json()
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'all_profile_finder':all_profile_finder[::-1],

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
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/pm_my_data/{id}").json()[0] 
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
                    'country': countryname,'states': states,'key':mydata,
                    'current_path':request.get_full_path()}
        
        if request.method=="POST":
            print(request.POST)
            response = requests.post(f"http://127.0.0.1:3000/pm_edit_account/{id}",   data = request.POST,files=request.FILES)
            print(response)
            print(response.status_code)
            print(response.text)
    
        return render(request,"edit_acc.html",context)
    except:
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
    all_profile_finder = requests.get("http://127.0.0.1:3000/alluserdata/").json()
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'all_profile_finder':all_profile_finder,
    }
    if request.method == "POST":
        print(request.POST)
        global uid
        uid = request.POST['uid']
        return redirect(f"/profile_manager/view_details/{mydata['uid']}")
    return render(request,"profile_finders.html",context)
    
def view_details(request,id):
    mydata = requests.get(f"http://127.0.0.1:3000/pm_my_data/{id}").json()[0] 
    profile_finders(request,id)
    print(uid) 
    specific_data = requests.get(f"http://127.0.0.1:3000/alldata/{uid}").json()
    my = requests.get(f"http://127.0.0.1:3000/alldata/{uid}").json()
    #sibling details
    sibling_name_value=[]
    sibling_relation_value=[]
    sibling_occupation_value=[]
    sibling_name = my['sibling_name'][1:-1].split(", ")
    sibling_relation = my['sibling_relation'][1:-1].split(", ")
    sibling_occupation = my['sibling_occupation'][1:-1].split(", ")
    for sibling_name_x in sibling_name:
        sibling_name_value.append(sibling_name_x[1:-1])
    for sibling_relation_x in sibling_relation:
        sibling_relation_value.append(sibling_relation_x[1:-1])
    for sibling_occupation_x in sibling_occupation:
        sibling_occupation_value.append(sibling_occupation_x[1:-1])
    sibling={}
    sib = [sibling]
    for i, sibling_name_data in enumerate(sibling_name_value):
            sibling[f'sibling_name_{i}'] = sibling_name_data
    for i, sibling_relation_data in enumerate(sibling_relation_value):
            sibling[f'sibling_relation_{i}'] = sibling_relation_data
    for i, sibling_occupation_data in enumerate(sibling_occupation_value):
            sibling[f'sibling_occupation_{i}'] = sibling_occupation_data
    
    print(sib)

#education
    education_school_value=[]
    education_year_value=[]
    education_course_value=[]
    education_school = my['education_school'][1:-1].split(", ")
    education_year = my['education_year'][1:-1].split(", ")
    education_course = my['education_course'][1:-1].split(", ")
    for education_school_x in education_school:
        education_school_value.append(education_school_x[1:-1])
    for education_year_x in education_year:
        education_year_value.append(education_year_x[1:-1])
    for education_course_x in education_course:
        education_course_value.append(education_course_x[1:-1])
    education={}
    edu = [education]
    for i, education_school_data in enumerate(education_school_value):
            education[f'education_school_{i}'] = education_school_data
    for i, education_year_data in enumerate(education_year_value):
            education[f'education_year_{i}'] = education_year_data
    for i, education_course_data in enumerate(education_course_value):
            education[f'education_course_{i}'] = education_course_data
    
    # print(edu)

#working experience
    company_name_value=[]
    position_value=[]
    salary_range_value=[]
    profession_value = []
    company_name = my['company_name'][1:-1].split(", ")
    position = my['position'][1:-1].split(", ")
    salary_range = my['salary_range'][1:-1].split(", ")
    profession = my['profession'][1:-1].split(", ")
    for company_name_x in company_name:
        company_name_value.append(company_name_x[1:-1])
    for position_x in position:
        position_value.append(position_x[1:-1])
    for salary_range_x in salary_range:
        salary_range_value.append(salary_range_x[1:-1])
    for profession_x in profession:
        profession_value.append(profession_x[1:-1])
    working={}
    wor = [working]
    for i, company_name_data in enumerate(company_name_value):
            working[f'company_name_{i}'] = company_name_data
    for i, position_data in enumerate(position_value):
            working[f'position_{i}'] = position_data
    for i, salary_range_data in enumerate(salary_range_value):
            working[f'salary_range_{i}'] = salary_range_data
    for i, profession_data in enumerate(profession_value):
            working[f'profession_{i}'] = profession_data
    # print(wor)

#intrest
    
    
    your_intrest_value=[]
    your_intrest = my['your_intrest'][1:-1].split(", ")
    for i, your_intrest_data in enumerate(your_intrest):
            your_intrest_value.append({'intrest':your_intrest_data[1:-1]})
 
    inte=your_intrest_value
    # print(your_intrest_value)

    yourinterest = my['your_intrest']
    x = yourinterest.replace("[", "").replace("]","").replace("'","").replace(" ","")
    lengthyourinterest = x.split(",")
    # print(lengthyourinterest)

    interestlist = ["Music","Travel","Gaming","Reading","Photograph","Writing","Sports","Artist",
                    "Singing","Custom","Dancer","Speaking"]

#non intrest
    
    
    non_intrest_value=[]
    non_intrest = my['non_intrest'][1:-1].split(", ")
    for i, non_intrest_data in enumerate(non_intrest):
            non_intrest_value.append({'non_intrest':non_intrest_data[1:-1]})
 
    non_inte=non_intrest_value
    # print(non_inte)

    yournoninterest = my['non_intrest']
    non = yournoninterest.replace("[", "").replace("]","").replace("'","").replace(" ","")
    lengthyournoninterest = non.split(",")

#complexion
    complexion = my['complexion']
    com = complexion.replace("[", "").replace("]","").replace("'","").replace(" ","")
    lengthcomplexion= com.split(",")
    # print(lengthcomplexion)

    complexionlist = ["Dark","Medium","ModerateFaIr","FaIr","VeryFair"]

#food taste
    food_taste = my['food_taste']
    ft = food_taste.replace("[", "").replace("]","").replace("'","").replace(" ","")
    lengthfood_taste= ft.split(",")
    # print(lengthfood_taste)

    food_tastelist = ["Sweezt","Bitter","UmamI","Salt","Sour","Spicy"]

#gallery

    gall = my['gallery']
    ga = gall.replace("[", "").replace("]","").replace("'","").replace(" ","")
    lengthgallery= ga.split(",")

    
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'specific_data':specific_data,
        'sibling':sib,
      'education':edu,
      'working':wor,
      'intrest':inte,
      'interestlist':interestlist,
      'lengthyourinterest':lengthyourinterest,
      'non_intrest':non_inte,
      'lengthyournoninterest':lengthyournoninterest,
      'complexionlist':complexionlist,
      'lengthcomplexion':lengthcomplexion,
      'lengthfood_taste':lengthfood_taste,
      'food_tastelist':food_tastelist,
        'lengthgallery':lengthgallery,

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