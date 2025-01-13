from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework.response import Response

from domc.models import (ApartmentBuilding, ManagementCompany,
                         ManagementCompanySite)
from .serializers import (ApartmentBuildingSerializer,
                          ManagementCompanySerializer,
                          ManagementCompanySiteSerializer)


class ApartmentBuildingViewSet(viewsets.ModelViewSet):
    queryset = ApartmentBuilding.objects.all()
    serializer_class = ApartmentBuildingSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('building_adress',)
    search_fields = ('building_adress',)

    def create(self, request, *args, **kwargs):
        data = request.data
        if isinstance(data, list):
            serializer = self.get_serializer(data=data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if isinstance(data, dict):
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {"error": "Data should be a list"},
            status=status.HTTP_400_BAD_REQUEST
        )


class ManagementCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ManagementCompany.objects.all()
    serializer_class = ManagementCompanySerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        if isinstance(data, list):
            serializer = self.get_serializer(data=data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if isinstance(data, dict):
            serializer = self.get_serializer(data=data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {"error": "Data should be a list"},
            status=status.HTTP_400_BAD_REQUEST
        )


class MAnagementCompanySiteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ManagementCompanySite.objects.all()
    serializer_class = ManagementCompanySiteSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        if isinstance(data, list):
            serializer = self.get_serializer(data=data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if isinstance(data, dict):
            serializer = self.get_serializer(data=data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {"error": "Data should be a list"},
            status=status.HTTP_400_BAD_REQUEST
        )
