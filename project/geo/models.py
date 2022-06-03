from django.contrib.gis.db import models
from phone_field import PhoneField

class Provider(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone_number = PhoneField(help_text='Contact phone number')
    language=models.CharField(max_length=20)
    currency=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class ServiceArea(models.Model):
    provider=models.ForeignKey(Provider,related_name='servicearea',on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    price=models.FloatField(default=0)
    geo = models.MultiPolygonField()
    def __str__(self):
        return self.name


