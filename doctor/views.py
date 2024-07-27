from django.shortcuts import render
from . import models
from rest_framework import viewsets,filters,pagination
from . import serializers
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

class SpecializationViewset(viewsets.ModelViewSet):
    queryset=models.Specialization.objects.all()
    serializer_class=serializers.SpecializationSerializer

class DesignationViewset(viewsets.ModelViewSet):
    queryset=models.Designation.objects.all()
    serializer_class=serializers.DesignationSerializer



class AvailableTimeForSpacificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id=request.query_params.get("doctor_id")
        if doctor_id:
            return queryset.filter(doctor=doctor_id)
        return queryset


class AvailableTimeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset=models.AvailableTime.objects.all()
    serializer_class=serializers.AvailableTimeSerializer
    filter_backends=[AvailableTimeForSpacificDoctor]

# pagination add 
class doctorPagination(pagination.PageNumberPagination):
    page_size=1
    page_size_query_param=page_size
    max_page_size=100


class DoctorViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset=models.Doctor.objects.all()
    serializer_class=serializers.DoctorSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class=doctorPagination

class ReviewViewset(viewsets.ModelViewSet):
    queryset=models.Review.objects.all()
    serializer_class=serializers.ReviewSerializer
