from rest_framework import serializers

from domc.models import (ApartmentBuilding, ManagementCompany,
                         ManagementCompanySite)


class ManagementCompanySerializer(serializers.ModelSerializer):
    all_site = serializers.StringRelatedField(many=True, read_only=True)
    buildings = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = ManagementCompany
        fields = (
            'id', 'management_company', 'adress_management_company', 'contact',
            'navigation_link_to_the_company', 'all_site', 'buildings'
        )


class ManagementCompanySiteSerializer(serializers.ModelSerializer):
    management_company_str = serializers.StringRelatedField(
        source='management_company', read_only=True
    )
    management_company = serializers.PrimaryKeyRelatedField(
        queryset=ManagementCompany.objects.all(), write_only=True
    )
    site_buildings = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = ManagementCompanySite
        fields = (
            'id', 'management_company_site', 'site_adress',
            'management_company_str', 'management_company',
            'navigation_link_to_the_site', 'site_buildings'
        )


# class ApartmentBuildingSerializer(serializers.ModelSerializer):
#     management_company_str = serializers.StringRelatedField(
#         source='management_company', read_only=True
#     )
#     # management_company = serializers.SerializerMethodField()
#     management_company_site_str = serializers.StringRelatedField(
#         source='management_company_site', read_only=True
#     )
#     # management_company_site = serializers.SerializerMethodField()
#     # note = serializers.StringRelatedField(read_only=True)
#     management_company = serializers.PrimaryKeyRelatedField(
#         queryset=ManagementCompany.objects.all(), write_only=True
#     )
#     management_company_site = serializers.PrimaryKeyRelatedField(
#         queryset=ManagementCompanySite.objects.all(), write_only=True
#     )
#     site_adress = serializers.CharField(
#         source='management_company_site.site_adress', read_only=True
#     )
#     navigation_link_to_the_site = serializers.CharField(
#         source='management_company_site.navigation_link_to_the_site',
#         read_only=True
#     )

#     class Meta:
#         model = ApartmentBuilding
#         fields = (
#             'id', 'building_adress', 'management_company_str',
#             'management_company_site_str', 'management_company',
#             'management_company_site', 'navigation_link_to_the_building',
#             'in_contract', 'pipe_support_aria', 'pipe_support_oyster',
#             'pipe_support_comlink', 'wall_mount_aria', 'wall_mount_oyster',
#             'wall_mount_comlink', 'site_adress', 'navigation_link_to_the_site'
#         )

#     # def get_management_company(self, obj):
#     #     return str(getattr(obj, 'management_company', None))

#     # def get_management_company_site(self, obj):
#     #     return str(getattr(obj, 'management_company_site', None))

#     # def create(self, validated_data):
#     #     validated_data['management_company'] = validated_data.pop(
#     #         'management_company_id', None
#     #     )
#     #     validated_data['management_company_site'] = validated_data.pop(
#     #         'management_company_site_id', None
#     #     )
#     #     return super().create(validated_data)


class ApartmentBuildingSerializer(serializers.ModelSerializer):
    management_company_str = serializers.StringRelatedField(
        source='management_company_site.management_company', read_only=True
    )
    # management_company = serializers.SerializerMethodField()
    management_company_site_str = serializers.StringRelatedField(
        source='management_company_site', read_only=True
    )
    # Закомментированно так как связь МКД с УК реализована через модель Участка
    # management_company_site = serializers.SerializerMethodField()
    
    # Пока не реализовано
    # note = serializers.StringRelatedField(read_only=True)
    # management_company = serializers.PrimaryKeyRelatedField(
    #     queryset=ManagementCompany.objects.all(), write_only=True
    # )
    management_company_site = serializers.PrimaryKeyRelatedField(
        queryset=ManagementCompanySite.objects.all(), write_only=True
    )
    site_adress = serializers.CharField(
        source='management_company_site.site_adress', read_only=True
    )
    navigation_link_to_the_site = serializers.CharField(
        source='management_company_site.navigation_link_to_the_site',
        read_only=True
    )

    class Meta:
        model = ApartmentBuilding
        fields = (
            'id', 'building_adress', 'management_company_str',
            'management_company_site_str',
            # Закомментированно так как связь МКД с УК реализована через модель Участка
            # 'management_company',
            'management_company_site', 'navigation_link_to_the_building',
            'in_contract', 'pipe_support_aria', 'pipe_support_oyster',
            'pipe_support_comlink', 'wall_mount_aria', 'wall_mount_oyster',
            'wall_mount_comlink', 'site_adress', 'navigation_link_to_the_site'
        )

    # def get_management_company(self, obj):
    #     return str(getattr(obj, 'management_company', None))

    # def get_management_company_site(self, obj):
    #     return str(getattr(obj, 'management_company_site', None))

    # def create(self, validated_data):
    #     validated_data['management_company'] = validated_data.pop(
    #         'management_company_id', None
    #     )
    #     validated_data['management_company_site'] = validated_data.pop(
    #         'management_company_site_id', None
    #     )
    #     return super().create(validated_data)
