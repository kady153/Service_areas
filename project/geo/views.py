from django.shortcuts import render
from django.http.response import JsonResponse

from .models import Provider,ServiceArea
from rest_framework.decorators import api_view
from .serializers import ProviderSerialzier,GetServiceAreaSerialzier,PostServiceAreaSerialzier
from rest_framework import status, filters
from rest_framework.response import Response
from django.contrib.gis.geos import Point



#display all avaiable providers

@api_view(['GET'])
def All_providers(request):
    if request.method == 'GET':
        providers = Provider.objects.all()
        serializer = ProviderSerialzier(providers,many=True)
        return Response(serializer.data)


#create a new provider

@api_view(['POST'])
def New_provider(request):
    if request.method == 'POST':
        serializer=ProviderSerialzier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response("bad request",status=status.HTTP_400_BAD_REQUEST)

# Edit a certain provider using id

@api_view(['GET','PUT','DELETE'])
def Provider_edit(request,pk):
    try:
        provider= Provider.objects.get(pk=pk)
    except :
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProviderSerialzier(provider)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer=ProviderSerialzier(provider, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        provider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        


#display all avaiable service areas

@api_view(['GET'])
def SA_all(request):
    if request.method == 'GET':
        areas = ServiceArea.objects.all()
        serializer = GetServiceAreaSerialzier(areas,many=True)
        return Response(serializer.data)


#create a new Service area

@api_view(['POST'])
def Area_new(request):

    if request.method == 'POST':
        serializer=PostServiceAreaSerialzier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response("bad request",status=status.HTTP_400_BAD_REQUEST)

# Edit a certain service area using id

@api_view(['GET','PUT','DELETE'])
def Area_edit(request,pk):
    try:
        area= ServiceArea.objects.get(pk=pk)
    except :
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = GetServiceAreaSerialzier(area)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer=PostServiceAreaSerialzier(area, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        area.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        

# find if a point is in any service area

@api_view(['GET'])
def Point_check(request,lat,lng):
    pnt = Point(float(lat),float(lng))
    if request.method == 'GET':
        areas = ServiceArea.objects.filter(geo__intersects=pnt)
        serializer = GetServiceAreaSerialzier(areas,many=True)
        return Response(serializer.data)


