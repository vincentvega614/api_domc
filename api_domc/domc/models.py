from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ManagementCompany(models.Model):
    management_company = models.CharField(
        max_length=100,
        verbose_name='Наименование управляющей компании'
    )
    adress_management_company = models.CharField(
        max_length=200,
        verbose_name='Адрес управляющей компании'
    )
    navigation_link_to_the_company = models.URLField(
        max_length=200,
        verbose_name='Ссылка для построения маршрута к управляющей компании'
    )

    class Meta:
        verbose_name = 'Управляющая компания'
        verbose_name_plural = 'Управляющие компании'

    def __str__(self):
        return self.management_company


class ManagementCompanySite(models.Model):
    management_company_site = models.CharField(
        max_length=50,
        verbose_name='Наименование участка управляющей компании'
    )
    site_adress = models.CharField(
        max_length=200,
        verbose_name='Адрес участка управляющей компании'
    )
    note = models.TextField(
        verbose_name='Примечание'
    )
    management_company = models.ForeignKey(
        ManagementCompany,
        on_delete=models.CASCADE,
        related_name='all_site',
        verbose_name='Наименование управляющей компании'
    )
    navigation_link_to_the_site = models.URLField(
        max_length=200,
        verbose_name='Ссылка для построения маршрута к участку'
    )

    class Meta:
        verbose_name = 'Участок управляющей компании'
        verbose_name_plural = 'Участки управляющей компании'

    def __str__(self):
        return f'{self.management_company_site} - {self.site_adress}'


class ApartmentBuilding(models.Model):
    building_adress = models.CharField(
        max_length=200,
        verbose_name='Адрес МКД'
    )
    management_company = models.ForeignKey(
        ManagementCompany,
        on_delete=models.CASCADE,
        related_name='building',
        verbose_name='Наименование управляющей компании'
    )
    management_company_site = models.ForeignKey(
        ManagementCompanySite,
        on_delete=models.CASCADE,
        related_name='site_building',
        verbose_name='Наименование участка'
    )
    navigation_link_to_the_building = models.URLField(
        max_length=200,
        verbose_name='Ссылка для построения маршрута к МКД'
    )

    class Meta:
        verbose_name = 'Многоквартирный жилой дом'
        verbose_name_plural = 'Многоквартирные жилые дома'

    def __str__(self):
        return self.building_adress
