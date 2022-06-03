from rest_framework import serializers
from geo.models import Provider,ServiceArea

class ProviderSerialzier (serializers.ModelSerializer):
    servicearea = serializers.StringRelatedField(many=True)

    class Meta:
        model=Provider
        fields=['pk','servicearea','name','email','phone_number','language','currency']



class GetServiceAreaSerialzier (serializers.ModelSerializer):
    provider = serializers.StringRelatedField(source='provider.name')
    class Meta:
        model=ServiceArea
        fields='__all__'


class PostServiceAreaSerialzier (serializers.ModelSerializer):
    class Meta:
        model=ServiceArea
        fields='__all__'

