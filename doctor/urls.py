from rest_framework.routers import DefaultRouter
from .views import DesignationViewset,SpecializationViewset,AvailableTimeViewset,ReviewViewset,DoctorViewset
from django.urls import path,include

Router=DefaultRouter()

Router.register('list',DoctorViewset)
Router.register('Designation',DesignationViewset)
Router.register('Specialization',SpecializationViewset)
Router.register('AvailableTime',AvailableTimeViewset)
Router.register('Reviewer',ReviewViewset)


urlpatterns = [
    path('',include(Router.urls)),
]