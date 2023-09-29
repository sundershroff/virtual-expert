"""
URL configuration for virtualexpert project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from profile_manager import pm_views
from sales_manager import sm_views
from hiring_manager import hm_views
from ad_provider import ad_provider_views
from ad_distributor import ad_dis_views
from affiliate_marketing import af_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pm_views.dashboard),
#///////profle manager//////
    path('profile_manager/signup/', pm_views.signup),
    path('profile_manager/signin/', pm_views.signin),
    path('profile_manager/otp/<id>', pm_views.otp),
    path('profile_manager/profile_picture/<id>', pm_views.profile_picture),
    path('profile_manager/upload_acc/<id>', pm_views.upload_acc),
    path('profile_manager/admin_dashboard/<id>', pm_views.admin_dashboard),
    path('profile_manager/profile_account/<id>', pm_views.profile_account),
    path('profile_manager/edit_acc/<id>', pm_views.edit_acc),
    path('profile_manager/acc_balance/<id>', pm_views.acc_balance),
    path('profile_manager/profile_finders/<id>', pm_views.profile_finders),
    path('profile_manager/view_details/<id>', pm_views.view_details),
    path('profile_manager/complaints/<id>', pm_views.complaints),
    path('profile_manager/users/<id>', pm_views.users),
    path('profile_manager/add_user/<id>', pm_views.add_user),
    path('profile_manager/settings/<id>', pm_views.settings),

#///////sales manager//////
    path('sales_manager/signup/', sm_views.signup),
    path('sales_manager/signin/', sm_views.signin),
    path('sales_manager/otp/<id>', sm_views.otp),
    path('sales_manager/profile_picture/<id>', sm_views.profile_picture),
    path('sales_manager/sm_upload_profile/<id>', sm_views.upload_acc),
    path('sales_manager/sm_verification_fee/<id>', sm_views.verification_fee),
    path('sales_manager/sm_salesdashboard/<id>', sm_views.admin_dashboard),
    path('sales_manager/sm_sales_profile/<id>', sm_views.profile),
    path('sales_manager/sm_editprofile/<id>', sm_views.edit_profile),
    path('sales_manager/sm_accountbalance/<id>', sm_views.account_balance),
    path('sales_manager/sm_coindetails/<id>', sm_views.coin_details),
    path('sales_manager/sm_hand_list/<id>', sm_views.hand_list),
    path('sales_manager/sm_ads_list/<id>', sm_views.ads_list),
    path('sales_manager/sm_ad_details/<id>', sm_views.ad_details),
    path('sales_manager/sm_edit_adDetail/<id>', sm_views.edit_ad_details),
    path('sales_manager/sm_accountsetting/<id>', sm_views.setting),
    path('sales_manager/sm_users/<id>', sm_views.users),
    path('sales_manager/sm_addusers/<id>', sm_views.add_users),










#///////hiring manager//////
    path('hiring_manager/signup/', hm_views.signup),
    path('hiring_manager/signin/', hm_views.signin),
    path('hiring_manager/otp/<id>', hm_views.otp),
    path('hiring_manager/profile_picture/<id>', hm_views.profile_picture),
    path('hiring_manager/hm_upload_acc/<id>', hm_views.upload_acc),


#///////ad_provider manager//////
    path('ad_provider/signup/', ad_provider_views.signup),
    path('ad_provider/signin/', ad_provider_views.signin),
    path('ad_provider/otp/<id>', ad_provider_views.otp),
    path('ad_provider/profile_picture/<id>', ad_provider_views.profile_picture),

#///////ad_distributor manager//////
    path('ad_distributor/signup/', ad_dis_views.signup),
    path('ad_distributor/signin/', ad_dis_views.signin),
    path('ad_distributor/otp/<id>', ad_dis_views.otp),
    path('ad_distributor/profile_picture/<id>', ad_dis_views.profile_picture),

#///////affiliate_marketing manager//////
    path('affiliate_marketing/signup/', af_views.signup),
    path('affiliate_marketing/signin/', af_views.signin),
    path('affiliate_marketing/otp/<id>', af_views.otp),
    path('affiliate_marketing/profile_picture/<id>', af_views.profile_picture),
    path('affiliate_marketing/af_uploadprofile/<id>', af_views.upload_acc),
    path('affiliate_marketing/af_profile/<id>', af_views.profile),
    path('affiliate_marketing/af_editprofile/<id>', af_views.edit_profile),
    path('affiliate_marketing/af_commisions/<id>', af_views.commisions),
    path('affiliate_marketing/af_setting/<id>', af_views.setting),






]
