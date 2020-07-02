from django.contrib.admin.models import LogEntry
from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import *
admin.site.unregister(Group)
admin.site.unregister(User)
LogEntry.objects.all().delete()

class Att_Report(admin.ModelAdmin):
    change_list_template='custom.html'
    def has_add_permission(self, request):
        return False


class hdate(admin.ModelAdmin):
    list_display=['Description','Holiday_Date']

class Adjustment_Att(admin.ModelAdmin):
    list_display=['Reason','Date']
    def has_add_permission(self, request):
        return False    

class ldate(admin.ModelAdmin):
    list_display=['Applied_Reason','Applied_Date']    


# Register your models here.
admin.site.register(Employee)
admin.site.register(Attendance_Report,Att_Report)
admin.site.register(Attendance)
admin.site.register(Holidays,hdate)
admin.site.register(notice_all)
admin.site.register(Manager)
admin.site.register(Leaves,ldate)
admin.site.register(Attendance_Adjustment_Request,Adjustment_Att)