from rest_framework import serializers
from .models import Owner, Tenant, House, MaintenanceRequest

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)
    tenants = TenantSerializer(many=True, read_only=True)

    class Meta:
        model = House
        fields = '__all__'

class MaintenanceRequestSerializer(serializers.ModelSerializer):
    house = HouseSerializer(read_only=True)
    tenant = TenantSerializer(read_only=True)

    class Meta:
        model = MaintenanceRequest
        fields = '__all__'