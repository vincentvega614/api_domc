from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import (ApartmentBuildingViewSet, MAnagementCompanySiteViewSet,
                    ManagementCompanyViewSet)

app_name = 'api'

router = DefaultRouter()
router.register('apartment-buildings', ApartmentBuildingViewSet)
router.register('management-companies', ManagementCompanyViewSet)
router.register('management-company-sites', MAnagementCompanySiteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
