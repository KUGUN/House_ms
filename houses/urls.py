# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import OwnerViewSet, TenantViewSet, HouseViewSet, MaintenanceRequestViewSet

# router = DefaultRouter()
# router.register(r'owners', OwnerViewSet)
# router.register(r'tenants', TenantViewSet)
# router.register(r'houses', HouseViewSet)
# router.register(r'maintenance-requests', MaintenanceRequestViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path
from django.conf import settings
from.import views

urlpatterns = [
    path('signup/', views.signup_api, name='signup'),
    path('login/', views.login_api, name='login'),
    path('view/', views.fetch_owners, name='fetch_owners'),
    path('create/', views.create_owner, name='create_owner'),
    path('view/<int:id>', views.fetch_owner, name='fetch_owner'),
    path('update/<int:id>', views.update_owner, name='update_owner'),
    path('delete/<int:id>', views.delete_owner, name='delete_owner'),
    path('house/create/', views.create_house, name='create_house'),
    path('house/view/', views.fetch_houses, name='fetch_houses'),
    path('house/view/<int:id>', views.fetch_house, name='fetch_house'),
    path('house/update/<int:id>', views.update_house, name='update_house'),
    path('house/delete/<int:id>', views.delete_house, name='delete_house'),
    path('tenant/create/', views.create_tenant, name='create_tenant'),
    path('tenant/view/', views.fetch_tenants, name='fetch_tenants'),
    path('tenant/view/<int:id>', views.fetch_tenant, name='fetch_tenant'),
    path('tenant/update/<int:id>', views.update_tenant, name='update_tenant'),
    path('tenant/delete/<int:id>', views.delete_tenant, name='delete_tenant'),
    path('maintenance/create/', views.create_maintenance_request, name='create_maintenance_request'),
    path('maintenance/view/', views.fetch_maintenance_requests, name='fetch_maintenance_requests'),
    path('maintenance/view/<int:id>', views.fetch_maintenance_request, name='fetch_maintenance_request'),
    ]