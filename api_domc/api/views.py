from rest_framework import viewsets, filters

from django_filters.rest_framework import DjangoFilterBackend

from domc.models import (ApartmentBuilding, ManagementCompany,
                         ManagementCompanySite)
from .serializers import (ApartmentBuildingSerializer,
                          ManagementCompanySerializer,
                          ManagementCompanySiteSerializer)


class ApartmentBuildingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ApartmentBuilding.objects.all()
    serializer_class = ApartmentBuildingSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('building_adress',)
    # search_fields = ('building_adress',
    #                  'management_company__management_company',
    #                  'management_company_site__management_company_site'
    # )
    search_fields = ('building_adress',)


class ManagementCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ManagementCompany.objects.all()
    serializer_class = ManagementCompanySerializer


class MAnagementCompanySiteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ManagementCompanySite.objects.all()
    serializer_class = ManagementCompanySiteSerializer
