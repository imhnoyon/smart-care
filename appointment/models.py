from django.db import models
from patient.models import Patient
from doctor.models import Doctor,AvailableTime
# Create your models here.

APPOINTMENT_STATUS=[
    ('Completed','Completed'),
    ('Pending','Pending'),
    ('Running','Running'),
]

APPOINTMENT_TYPE=[
    ('Offline','Offline'),
    ('Online','Online'),
]
class Appointment(models.Model):
    patient = models.ForeignKey(Patient,related_name='patient' ,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,related_name='doctor', on_delete=models.CASCADE)
    appointment_type=models.CharField(max_length=10,choices=APPOINTMENT_TYPE )
    appointment_status=models.CharField(max_length=10,choices=APPOINTMENT_STATUS,default="Pending")
    symptom=models.TextField()
    time=models.ForeignKey(AvailableTime,related_name='time', on_delete=models.CASCADE)
    cancel=models.BooleanField(default=False)

    def __str__(self):
        return f"Doctor:  {self.doctor.user.first_name} {self.doctor.user.last_name} -> Patient:{self.patient.user.first_name} {self.patient.user.last_name}"