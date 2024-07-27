from django.db import models

# Create your models here.

class Service(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField(upload_to="service/images/")

    def __str__(self):
        return self.name
    