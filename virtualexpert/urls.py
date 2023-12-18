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
from ad_distributor import ad_distributor_views
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
    path('profile_manager/user_edit/<id>', pm_views.user_edit),
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
    path('sales_manager/otp_client/<id>',sm_views.otp_client),

    # path('sales_manager/add_client/<id>',sm_views.add_client),










#///////hiring manager//////
    path('hiring_manager/signup/', hm_views.signup),
    path('hiring_manager/signin/', hm_views.signin),
    path('hiring_manager/otp/<id>', hm_views.otp),
    path('hiring_manager/profile_picture/<id>', hm_views.profile_picture),
    path('hiring_manager/hm_upload_acc/<id>', hm_views.upload_acc),
    path('hiring_manager/hm_admin_dashboard/<id>', hm_views.admin_dashboard),
    path('hiring_manager/hm_profile/<id>', hm_views.profile),
    path('hiring_manager/hm_edit_acc/<id>', hm_views.edit_acc),
    path('hiring_manager/hm_local_admin/<id>', hm_views.local_admin),
    path('hiring_manager/hm_local_admin_upload/<id>', hm_views.local_admin_upload),
    path('hiring_manager/hm_ad_provider/<id>', hm_views.ad_provider),
    path('hiring_manager/hm_adprovider_upload/<id>', hm_views.ad_provider_doc),
    path('hiring_manager/hm_ad_distributor/<id>', hm_views.ad_distributor),
    path('hiring_manager/hm_ad_distributor_upload/<id>', hm_views.ad_distributor_doc),
    path('hiring_manager/hm_sales_person/<id>', hm_views.sales),
    path('hiring_manager/hm_sales_person_doc/<id>', hm_views.sales_doc),
    path('hiring_manager/hm_affiliate_marketing/<id>', hm_views.affiliate_marketing),
    path('hiring_manager/hm_affiliate_marketing_upload/<id>', hm_views.affiliate_marketing_doc),
    path('hiring_manager/hm_private_investigator/<id>', hm_views.private_investigator),
    path('hiring_manager/hm_private_investigator_upload/<id>', hm_views.private_investigator_doc),

    path('hiring_manager/hm_hiring_manager/<id>', hm_views.hiring_manager),
    path('hiring_manager/hm_hiring_manager_doc/<id>', hm_views.hiring_manager_doc),
    path('hiring_manager/hm_settings/<id>', hm_views.setting),









#///////ad_provider manager//////
    path('ad_provider/signup/', ad_provider_views.signup),
    path('ad_provider/signin/', ad_provider_views.signin),
    path('ad_provider/otp/<id>', ad_provider_views.otp),
    path('ad_provider/profile_picture/<id>', ad_provider_views.profile_picture),
    path('ad_provider/upload_acc/<id>', ad_provider_views.upload_acc),
    path('ad_provider/ad_provider_admin_dashboard/<id>', ad_provider_views.admin_dashboard),
    path('ad_provider/ad_pro_account/<id>', ad_provider_views.account),
    path('ad_provider/ad_pro_editAccount/<id>', ad_provider_views.edit_account),
    path('ad_provider/ad_pro_acc_balance/<id>', ad_provider_views.acc_balance),
    path('ad_provider/ad_pro_adFunds/<id>', ad_provider_views.add_funds),
    path('ad_provider/ad_pro_list/<id>', ad_provider_views.ads_list_all),
    path('ad_provider/ad_pro_active/<id>', ad_provider_views.ads_active),
    path('ad_provider/ad_pro_pending/<id>', ad_provider_views.ads_pending),
    path('ad_provider/ad_pro_deactive/<id>', ad_provider_views.ads_deactive),
    path('ad_provider/ad_pro_closed/<id>', ad_provider_views.ads_closed),
    path('ad_provider/ad_pro_createAd/<id>', ad_provider_views.ad_pro_createAd),
    path('ad_provider/ad_pro_payment/<id>', ad_provider_views.ad_pro_payment),
    path('ad_provider/ad_pro_editAd/<id>', ad_provider_views.ad_pro_editAd),
    path('ad_provider/ad_pro_adDetails/<id>', ad_provider_views.ad_pro_adDetails),
    path('ad_provider/ad_pro_users/<id>', ad_provider_views.ad_pro_users),
    path('ad_provider/ad_pro_addusers/<id>', ad_provider_views.ad_pro_addusers),
    path('ad_provider/ad_pro_user_edit/<id>', ad_provider_views.ad_pro_user_edit),
    path('ad_provider/ad_pro_settings/<id>', ad_provider_views.ad_pro_settings),
    path('ad_pro_password_reset/<id>',ad_provider_views.ad_pro_password_reset),
    path('ad_provider/ad_pro_coins/<id>',ad_provider_views.ad_pro_coins),





#///////ad_distributor manager//////
    path('ad_distributor/signup/', ad_distributor_views.signup),
    path('ad_distributor/signin/', ad_distributor_views.signin),
    path('ad_distributor/otp/<id>', ad_distributor_views.otp),
    path('ad_distributor/profile_picture/<id>', ad_distributor_views.profile_picture),
    path('ad_distributor/upload_acc/<id>', ad_distributor_views.upload_acc),
    path('ad_distributor/ad_distributor_admin_dashboard/<id>', ad_distributor_views.admin_dashboard),
    path('ad_distributor/ad_dis_account/<id>', ad_distributor_views.account),
    path('ad_distributor/ad_dis_editAccount/<id>', ad_distributor_views.edit_account),
    path('ad_distributor/ad_dis_acc_balance/<id>', ad_distributor_views.acc_balance),
    path('ad_distributor/ad_dis_adFunds/<id>', ad_distributor_views.add_funds),
    path('ad_distributor/ad_dis_list/<id>', ad_distributor_views.ads_list_all),
    path('ad_distributor/ad_dis_active/<id>', ad_distributor_views.ads_active),
    path('ad_distributor/ad_dis_pending/<id>', ad_distributor_views.ads_pending),
    path('ad_distributor/ad_dis_deactive/<id>', ad_distributor_views.ads_deactive),
    path('ad_distributor/ad_dis_closed/<id>', ad_distributor_views.ads_closed),
    path('ad_distributor/ad_dis_createAd/<id>', ad_distributor_views.ad_dis_createAd),
    path('ad_distributor/ad_dis_payment/<id>', ad_distributor_views.ad_dis_payment),
    path('ad_distributor/ad_dis_editAd/<id>', ad_distributor_views.ad_dis_editAd),
    path('ad_distributor/ad_dis_adDetails/<id>', ad_distributor_views.ad_dis_adDetails),
    path('ad_distributor/ad_dis_users/<id>', ad_distributor_views.ad_dis_users),
    path('ad_distributor/ad_dis_addusers/<id>', ad_distributor_views.ad_dis_addusers),
    path('ad_distributor/ad_dis_user_edit/<id>', ad_distributor_views.ad_dis_user_edit),
    path('ad_distributor/ad_dis_settings/<id>', ad_distributor_views.ad_dis_settings),
    path('ad_dis_password_reset/<id>',ad_distributor_views.ad_dis_password_reset),
    path('ad_distributor/ad_dis_coins/<id>', ad_distributor_views.ad_dis_coins),

    


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
    path('affiliate_marketing/af_marketingdashboard/<id>',af_views.admin_dashboard),
    path('password_reset/<id>',af_views.password_rest)






]
