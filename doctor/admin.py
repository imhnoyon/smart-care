from django.contrib import admin
from .models import Designation,Specialization,AvailableTime,Doctor,Review

# Register your models here.
class SpecilizationAdmin(admin.ModelAdmin):
     prepopulated_fields = {"slug": ["name",]}

admin.site.register(Specialization,SpecilizationAdmin)

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name",]}

admin.site.register(Designation,DesignationAdmin)

admin.site.register(AvailableTime)
admin.site.register(Review)


class DoctorModelAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','designation','specialization','image','availabletime','fee','meet_link']

    def first_name(self,obj):
        return obj.user.first_name
    
    def last_name(self,obj):
        return obj.user.last_name
    
    def designation(self,obj):
        return obj.designation.name
    
    def specialization(self,obj):
        return obj.specialization.name
    
    def availabletime(self,obj):
        return obj.availabletime.name

admin.site.register(Doctor,DoctorModelAdmin)