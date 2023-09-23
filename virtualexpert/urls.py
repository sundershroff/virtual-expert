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
from profile_manager import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard),
#///////profle manager//////
    path('profile_manager/signup/', views.signup),
    path('profile_manager/signin/', views.signin),
    path('profile_manager/otp/<id>', views.otp),
    path('profile_manager/profile_picture/<id>', views.profile_picture),
    path('profile_manager/upload_acc/<id>', views.upload_acc),
    path('profile_manager/admin_dashboard/<id>', views.admin_dashboard),
    path('profile_manager/profile_account/<id>', views.profile_account),
    path('profile_manager/edit_acc/<id>', views.edit_acc),
    path('profile_manager/acc_balance/<id>', views.acc_balance),
    path('profile_manager/profile_finders/<id>', views.profile_finders),
    path('profile_manager/view_details/<id>', views.view_details),
    path('profile_manager/complaints/<id>', views.complaints),
    path('profile_manager/users/<id>', views.users),
    path('profile_manager/add_user/<id>', views.add_user),
    path('profile_manager/settings/<id>', views.settings),



]
