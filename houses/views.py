from django.shortcuts import render #it is used to render the HTML templates
# Create your views here.
from rest_framework import viewsets #it is used to create views for the API
from .models import Owner, Tenant, House, MaintenanceRequest # Importing models
from .serializers import OwnerSerializer, TenantSerializer, HouseSerializer, MaintenanceRequestSerializer, LoginSerializer, SignupSerializer #it is used to serialize the data from the models to JSON format
from rest_framework.decorators import api_view #it is used to create API views
from rest_framework.response import Response #it is used to return the response from the API views
from rest_framework import status #it is used to return the status of the response from the API views
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated #it is used to set the permissions for the API views
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def signup_api(request):
    if request.method == 'POST':
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
@api_view(['POST'])
@permission_classes([AllowAny])
def login_api(request):
    serializer = LoginSerializer(data=request.data)
   
    if serializer.is_valid():
        user = serializer.validated_data.get('user', None)
       
        if user is None:
            raise AuthenticationFailed('Email does not exist.')  
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': {
                'username': user.username,
                'email': user.email,
            },
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def fetch_owners(request):
    owners= Owner.objects.all()  # Fetch all owners from the database
    serializer = OwnerSerializer(owners, many=True)  # Serialize the owner data
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def fetch_owner(request, id):
    owner = Owner.objects.get(id=id)  # Fetch a specific owner by ID
    serializer = OwnerSerializer(owner)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_owner(request):
    serializer = OwnerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE']) #
@permission_classes([IsAuthenticated])
def delete_owner(request, id):
    owner = Owner.objects.get(id=id)  # Fetch the owner to be deleted
    owner.delete()  # Delete the owner from the database
    return Response(status=status.HTTP_204_NO_CONTENT)  # Return a 204 No Content response

@api_view(['PUT']) # Update an existing owner
@permission_classes([IsAuthenticated])
def update_owner(request, id):
    owner = Owner.objects.get(id=id)  # Fetch the owner to be updated
    serializer = OwnerSerializer(owner, data=request.data)  # Serialize the updated data
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return the updated data
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if validation fails

@api_view(['GET'])
def fetch_tenants(request):
    tenants = Tenant.objects.all()  # Fetch all tenants from the database
    serializer = TenantSerializer(tenants, many=True)  # Serialize the tenant data      
    return Response(serializer.data, status=status.HTTP_200_OK)  # Return the serialized data as a response
@api_view(['GET'])
def fetch_tenant(request, id):
    tenant = Tenant.objects.get(id=id)  # Fetch a specific tenant by ID
    serializer = TenantSerializer(tenant)  # Serialize the tenant data  
    return Response(serializer.data, status=status.HTTP_200_OK)  # Return the serialized data as a response
@api_view(['POST'])
@permission_classes([IsAuthenticated])  
def create_tenant(request):
    serializer = TenantSerializer(data=request.data)    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the created tenant data
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if validation fails
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_tenant(request, id):
    tenant = Tenant.objects.get(id=id)  # Fetch the tenant to be deleted
    tenant.delete()  # Delete the tenant from the database
    return Response(status=status.HTTP_204_NO_CONTENT)  # Return a 204 No Content response
@api_view(['PUT'])
@permission_classes([IsAuthenticated])  
def update_tenant(request, id):
    tenant = Tenant.objects.get(id=id)
    serializer = TenantSerializer(tenant, data=request.data)  # Serialize the updated data
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return the updated tenant data
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if validation fails

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_houses(request):
    houses = House.objects.all()
    serializer = HouseSerializer(houses, many=True)  # Serialize the house data
    return Response(serializer.data, status=status.HTTP_200_OK)  # Return the serialized data
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_house(request, id):
    house = House.objects.get(id=id)
    serializer = HouseSerializer(house)  # Serialize the house data
    return Response(serializer.data, status=status.HTTP_200_OK)  # Return the serialized data
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_house(request):
    serializer = HouseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the created house
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if validation fails
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_house(request, id):
    house = House.objects.get(id=id)
    house.delete()  # Delete the house from the database
    return Response(status=status.HTTP_204_NO_CONTENT)  # Return a 204 No Content
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_house(request, id):
    house = House.objects.get(id=id)
    serializer = HouseSerializer(house, data=request.data)  # Serialize the updated data
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if validation fails
@api_view(['GET'])
def fetch_maintenance_requests(request):
    maintenance_requests = MaintenanceRequest.objects.all()
    serializer = MaintenanceRequestSerializer(maintenance_requests, many=True)  # Serialize the maintenance request data
    return Response(serializer.data, status=status.HTTP_200_OK)  # Return the serialized data as a response
@api_view(['GET'])
def fetch_maintenance_request(request, id):
    maintenance_request = MaintenanceRequest.objects.get(id=id)
    serializer = MaintenanceRequestSerializer(maintenance_request)  # Serialize the maintenance request data
    return Response(serializer.data, status=status.HTTP_200_OK)  # Return the serialized data as a response
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_maintenance_request(request):
    serializer = MaintenanceRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the created maintenance request
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if validation fails
  # Return the serialized data as a response
    
# class OwnerViewSet(viewsets.ModelViewSet):# ViewSet for Owner model
#     """API endpoint that allows owners to be viewed or edited."""
#     # ModelViewSet provides default implementations for CRUD operations
#     queryset = Owner.objects.all()#it is used to get all the objects from the Owner model
#     # queryset is a collection of objects that will be used to populate the API
#     serializer_class = OwnerSerializer# it is used to serialize the data from the Owner model to JSON format  

# class TenantViewSet(viewsets.ModelViewSet):
#     queryset = Tenant.objects.all()
#     serializer_class = TenantSerializer

# class HouseViewSet(viewsets.ModelViewSet):
#     queryset = House.objects.all()
#     serializer_class = HouseSerializer

# class MaintenanceRequestViewSet(viewsets.ModelViewSet):
#     queryset = MaintenanceRequest.objects.all()
#     serializer_class = MaintenanceRequestSerializer

# # This viewset handles maintenance requests, allowing tenants to report issues with houses
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