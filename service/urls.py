from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewset

Router=DefaultRouter()

Router.register('services',ServiceViewset)

urlpatterns = [
    path('',include(Router.urls)),
]
