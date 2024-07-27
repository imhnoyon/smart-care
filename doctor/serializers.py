from rest_framework import serializers
from . import models

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Specialization
        fields='__all__'

class DesignationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.Designation
        fields='__all__'

class AvailableTimeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model=models.AvailableTime
        fields='__all__'

class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    designation = serializers.StringRelatedField(many=True)
    specialization = serializers.StringRelatedField(many=True)
    availabletime = serializers.StringRelatedField(many=True)
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model=models.Doctor
        fields='__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model=models.Review
        fields='__all__'
