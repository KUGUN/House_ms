from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets #it is used to create views for the API
from .models import Owner, Tenant, House, MaintenanceRequest # Importing models
from .serializers import OwnerSerializer, TenantSerializer, HouseSerializer, MaintenanceRequestSerializer #it is used to serialize the data from the models to JSON format

class OwnerViewSet(viewsets.ModelViewSet):# ViewSet for Owner model
    """API endpoint that allows owners to be viewed or edited."""
    # ModelViewSet provides default implementations for CRUD operations
    queryset = Owner.objects.all()#it is used to get all the objects from the Owner model
    # queryset is a collection of objects that will be used to populate the API
    serializer_class = OwnerSerializer# it is used to serialize the data from the Owner model to JSON format  

class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class MaintenanceRequestViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer

# This viewset handles maintenance requests, allowing tenants to report issues with houses
# and track the status of their requests.
# It provides endpoints for creating, retrieving, updating, and deleting maintenance requests.
# The viewsets automatically generate the necessary API endpoints based on the defined models and serializers.
# This allows for easy integration with the Django REST Framework, enabling the creation of a RESTful API for the house management system.
# The viewsets are registered in the URLs configuration to make them accessible via HTTP requests.
# The OwnerViewSet, TenantViewSet, HouseViewSet, and MaintainRequestViewSet classes inherit from ModelViewSet,
# which provides a full set of CRUD operations for the respective models.
# The queryset attribute defines the set of objects that will be used for the API endpoints,
# and the serializer_class attribute specifies the serializer that will be used to convert model instances to JSON
# and vice versa.
# This structure allows for a clean separation of concerns, where the models define the data structure,
# the serializers handle the conversion to and from JSON, and the viewsets manage the API endpoints
# for interacting with the data.
# The use of viewsets simplifies the code by automatically providing the necessary methods for handling HTTP requests,
# such as list, create, retrieve, update, and destroy. This reduces boilerplate code
# and makes it easier to maintain and extend the API in the future.