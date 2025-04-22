from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
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
    filterset_fields = ('building_adress', 'technician',)
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

    @action(detail=False, methods=['patch'])
    def bulk_partial_update(self, request):
        data = request.data
        if not isinstance(data, list):
            return Response({"error": "Expected a list"}, status=400)
        updated_objects = []
        for item in data:
            instance = ManagementCompanySite.objects.get(pk=item['id'])
            serializer = self.get_serializer(instance, data=item, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            updated_objects.append(serializer.data)

        return Response(updated_objects, status=200)


class ManagementCompanyViewSet(viewsets.ModelViewSet):
    queryset = ManagementCompany.objects.all()
    serializer_class = ManagementCompanySerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('management_company',)
    search_fields = ('management_company',)

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

    @action(detail=False, methods=['patch'])
    def bulk_partial_update(self, request):
        data = request.data
        if not isinstance(data, list):
            return Response({"error": "Expected a list"}, status=400)
        updated_objects = []
        for item in data:
            instance = ManagementCompanySite.objects.get(pk=item['id'])
            serializer = self.get_serializer(instance, data=item, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            updated_objects.append(serializer.data)

        return Response(updated_objects, status=200)


class ManagementCompanySiteViewSet(viewsets.ModelViewSet):
    queryset = ManagementCompanySite.objects.all()
    serializer_class = ManagementCompanySiteSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('management_company', 'management_company_site',)
    search_fields = ('management_company_site',)

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

    @action(detail=False, methods=['patch'])
    def bulk_partial_update(self, request):
        data = request.data
        if not isinstance(data, list):
            return Response({"error": "Expected a list"}, status=400)
        updated_objects = []
        for item in data:
            instance = ManagementCompanySite.objects.get(pk=item['id'])
            serializer = self.get_serializer(instance, data=item, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            updated_objects.append(serializer.data)

        return Response(updated_objects, status=200)
