import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from geo.models import Provider,ServiceArea
from .serializers import ProviderSerialzier,GetServiceAreaSerialzier,PostServiceAreaSerialzier


class ProviderTestCase(APITestCase):
    def test_Provider(self):
        data ={"name": "testcase" , "email":"test@localhost.com",
        "phone_number": "010055","language": "english","currency":"dollar"}
        response= self.client.post("/provider/new/",data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


