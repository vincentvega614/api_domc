from domc.models import (ApartmentBuilding, ManagementCompany,
                         ManagementCompanySite)
from rest_framework import serializers


class ManagementCompanySiteSerializer(serializers.ModelSerializer):
    management_company = serializers.StringRelatedField(read_only=True)
    site_building = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = ManagementCompanySite
        fields = (
            'id', 'management_company_site', 'site_adress', 'note',
            'management_company', 'navigation_link_to_the_site',
            'site_building'
        )


class ApartmentBuildingSerializer(serializers.ModelSerializer):
    management_company = serializers.StringRelatedField(
        read_only=True
    )
    management_company_site = serializers.StringRelatedField(
        read_only=True
    )
    site_adress = serializers.CharField(
        source='management_company_site.site_adress'
    )

    class Meta:
        model = ApartmentBuilding
        fields = (
            'id', 'building_adress', 'management_company',
            'management_company_site', 'site_adress',
            'navigation_link_to_the_building'
        )


class ManagementCompanySerializer(serializers.ModelSerializer):
    all_site = serializers.StringRelatedField(many=True, read_only=True)
    building = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = ManagementCompany
        fields = (
            'id', 'management_company', 'adress_management_company',
            'navigation_link_to_the_company', 'all_site', 'building'
        )


# class ManagementCompanySiteSerializer(serializers.ModelSerializer):
#     management_company = serializers.StringRelatedField(read_only=True)
#     site_building = serializers.StringRelatedField(many=True, read_only=True)

#     class Meta:
#         model = ManagementCompanySite
#         fields = (
#             'id', 'management_company_site', 'site_adress', 'note',
#             'management_company', 'navigation_link_to_the_site',
#             'site_building'
#         )
