from typing import Any
from django.contrib import admin
from .models import Appointment
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.

class AppointmentModelAdmin(admin.ModelAdmin):
    list_display=['D_first_name','D_last_name','P_first_name','P_last_name','appointment_type','appointment_status','symptom','time','cancel']

    def D_first_name(self,obj):
        return obj.doctor.user.first_name
    
    def D_last_name(self,obj):
        return obj.doctor.user.last_name
    
    def P_first_name(self,obj):
        return obj.patient.user.last_name
    
    def P_last_name(self,obj):
        return obj.patient.user.last_name
    
    def time(self,obj):
        return obj.time.name
    
    def save_model(self, request, obj, form,change):
        obj.save()
        if obj.appointment_status=="Running" and obj.appointment_type=="Online":
            email_subject="Your online appointment is running.."
            email_body=render_to_string('admin_email.html',{'patient':obj.patient.user,'doctor':obj.doctor})
            email=EmailMultiAlternatives(email_subject,'',to=[obj.patient.user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()
        
    

admin.site.register(Appointment,AppointmentModelAdmin)