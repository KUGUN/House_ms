from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OwnerViewSet, TenantViewSet, HouseViewSet, MaintenanceRequestViewSet

router = DefaultRouter()
router.register(r'owners', OwnerViewSet)
router.register(r'tenants', TenantViewSet)
router.register(r'houses', HouseViewSet)
router.register(r'maintenance-requests', MaintenanceRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]