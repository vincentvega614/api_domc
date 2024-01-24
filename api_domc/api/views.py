from rest_framework import viewsets

from domc.models import (ApartmentBuilding, ManagementCompany,
                         ManagementCompanySite)
from .serializers import (ApartmentBuildingSerializer,
                          ManagementCompanySerializer,
                          ManagementCompanySiteSerializer)


class ApartmentBuildingViewSet(viewsets.ModelViewSet):
    queryset = ApartmentBuilding.objects.all()
    serializer_class = ApartmentBuildingSerializer


class ManagementCompanyViewSet(viewsets.ModelViewSet):
    queryset = ManagementCompany.objects.all()
    serializer_class = ManagementCompanySerializer


class MAnagementCompanySiteViewSet(viewsets.ModelViewSet):
    queryset = ManagementCompanySite.objects.all()
    serializer_class = ManagementCompanySiteSerializer
