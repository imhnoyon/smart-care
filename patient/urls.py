from rest_framework.routers import DefaultRouter
from .views import PatientViewset
from django.urls import path,include
from . import views
Router=DefaultRouter()

Router.register('list',PatientViewset)

urlpatterns = [
    path('',include(Router.urls)),
    path('register/',views.RegistrationViewset.as_view(),name='register'),
    path('active/<uid64>/<token>/',views.activate,name='activate'),
    path('login/',views.UserLoginAPIview.as_view(),name='login'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
]
