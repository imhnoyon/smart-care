from django.contrib import admin
from .models import Service
# Register your models here.


class ServiceAdminModel(admin.ModelAdmin):
    list_display=['name','description','image']
admin.site.register(Service,ServiceAdminModel)
