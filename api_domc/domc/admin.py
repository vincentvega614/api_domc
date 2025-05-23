from django.contrib import admin

from .models import (ApartmentBuilding, ManagementCompany,
                     ManagementCompanySite, Note)


class ApartmentBuildingAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'building_adress', 'management_company_site',
        'navigation_link_to_the_building', 'technician', 'technician_phone',
        'in_contract', 'pipe_support_aria', 'pipe_support_build',
        'pipe_support_oyster', 'pipe_support_comlink', 'wall_mount_aria',
        'wall_mount_oyster', 'wall_mount_comlink'
    )
    search_fields = ('building_adress',)
    list_filter = ('building_adress',)
    empty_value_display = '-пусто-'


class ManagementCompanyAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'management_company', 'adress_management_company', 'contact',
        'navigation_link_to_the_company'
    )
    search_field = ('management_company',)
    list_filter = ('management_company',)
    empty_value_display = '-пусто-'


class ManagementCompantSiteAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'management_company_site', 'site_adress', 'office_phone',
        'management_company', 'navigation_link_to_the_site'
    )
    search_field = ('management_company_site',)
    list_filter = ('management_company_site',)
    empty_value_display = '-пусто-'


class NoteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'apartment_building', 'author', 'text', 'created')
    search_fields = ('text',)
    list_filter = ('text',)
    empty_value_display = '-пусто-'


admin.site.register(ApartmentBuilding, ApartmentBuildingAdmin)
admin.site.register(ManagementCompany, ManagementCompanyAdmin)
admin.site.register(ManagementCompanySite, ManagementCompantSiteAdmin)
admin.site.register(Note, NoteAdmin)
