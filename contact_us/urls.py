from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ContactViewset

Router=DefaultRouter() # amder router toiri korlam

Router.register('contact_us',ContactViewset) # router er antena 
urlpatterns = [
    path('',include(Router.urls)),
]
