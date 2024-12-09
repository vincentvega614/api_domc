from domc.models import (ApartmentBuilding, ManagementCompany,
                         ManagementCompanySite)
from rest_framework import serializers


class ManagementCompanySiteSerializer(serializers.ModelSerializer):
    management_company = serializers.StringRelatedField(read_only=True)
    site_building = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = ManagementCompanySite
        fields = (
            'id', 'management_company_site', 'site_adress',
            'management_company', 'navigation_link_to_the_site',
            'site_building'
        )


# class ApartmentBuildingSerializer(serializers.ModelSerializer):
#     management_company = serializers.StringRelatedField(
#         read_only=True
#     )
#     management_company_site = serializers.StringRelatedField(
#         read_only=True
#     )
#     site_adress = serializers.CharField(
#         source='management_company_site.site_adress'
#     )
#     note = serializers.StringRelatedField(read_only=True)

#     class Meta:
#         model = ApartmentBuilding
#         fields = (
#             'id', 'building_adress', 'management_company',
#             'management_company_site', 'site_adress',
#             'navigation_link_to_the_building', 'note', 'in_contract',
#             'pipe_support_aria', 'pipe_support_oyster', 'pipe_support_comlink',
#             'wall_mount_aria', 'wall_mount_oyster', 'wall_mount_comlink'
#         )


# Сериализатор для записи новых объектов
class ApartmentBuildingSerializer(serializers.ModelSerializer):
    # management_company = serializers.StringRelatedField(
    #     read_only=True
    # )
    # management_company_site = serializers.StringRelatedField(
    #     read_only=True
    # )
    # note = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ApartmentBuilding
        fields = (
            'id', 'building_adress', 'management_company',
            'management_company_site',
            'navigation_link_to_the_building', 'in_contract',
            'pipe_support_aria', 'pipe_support_oyster', 'pipe_support_comlink',
            'wall_mount_aria', 'wall_mount_oyster', 'wall_mount_comlink'
        )


class ManagementCompanySerializer(serializers.ModelSerializer):
    all_site = serializers.StringRelatedField(many=True, read_only=True)
    building = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = ManagementCompany
        fields = (
            'id', 'management_company', 'adress_management_company', 'contact',
            'navigation_link_to_the_company', 'all_site', 'building'
        )
