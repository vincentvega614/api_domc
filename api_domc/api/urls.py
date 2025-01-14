from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (ApartmentBuildingViewSet, ManagementCompanySiteViewSet,
                    ManagementCompanyViewSet)

app_name = 'api'

router = DefaultRouter()
router.register('apartment-buildings', ApartmentBuildingViewSet)
router.register('management-companies', ManagementCompanyViewSet)
router.register('management-company-sites', ManagementCompanySiteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
