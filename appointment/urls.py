from rest_framework.routers import DefaultRouter
from .import views
from django.urls import path,include
Router=DefaultRouter()

Router.register('',views.AppointmentViewset)

urlpatterns = [
    path('',include(Router.urls)),
]
