"""salman1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from mainapp import views
from profiles.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        url(r'^admin/', admin.site.urls),
        # url(r'^$/', admin.site.urls),
        # url(r'login1',views.holiday,name='login'),
        url(r'home/$',views.home,name='home'),
        url(r'custom/',views.monthleave,name='custom'),
        url(r'Adjust_Att',views.Adjust_Att,name='Adjust_Attendance'),
        url(r'^Att_approve/',include(('att_adjust_approve.urls','att_adjust_approve'),namespace='Att_approve')),
        url(r'^att_adjust_final_approve',views.m_att_adjust_approve,name='att_adjust_final_approve'),
        url(r'^change_password',include(('password_change_app.urls','password_change_app'),namespace='change_password')),
        url(r'^changed_password',views.changed_pass,name='changed_pass'),
        
        url(r'login_page/',include('login_app.urls'),name='login_page'),
        url(r'^login_auth1/',include(('login_auth.urls','login_auth'),namespace='login_auth')),
        url(r'^holiday/',include('holiday_app.urls'),name='holiday_list'),
        url(r'^leave/',include(('leave_app.urls','leave_app'),namespace='leave')),
        url(r'^leave3',views.submit_leave,name='leave3'),
        url(r'^leave_approve/',include(('leave_approve.urls','leave_approve'),namespace='leave_approve')),
        url(r'^Attendance/',include(('adjustment_attendance.urls','adjustment_attendance'),namespace='Attendance')),
        url(r'^profile',include(('profiles.urls','profiles'),namespace='profile1')),
        url(r'^final_approve',views.m_approve,name='final_approve'),
        url(r'^create_users/',views.create_users,name='create_users'),
        url(r'logout/$',views.log_out,name='logout'),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
