from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ManagementCompany(models.Model):
    management_company = models.CharField(
        max_length=100, unique=True,
        verbose_name='Наименование управляющей компании',
        help_text='Введите наименование управляющей компании'
    )
    adress_management_company = models.CharField(
        max_length=200, verbose_name='Адрес управляющей компании',
        help_text='Ведите адрес управляющей компании'
    )
    contact = models.TextField(
        blank=True, null=True, verbose_name='Контакты управляющей компании',
        help_text='Введите контактные данные управляющей компании'
    )
    navigation_link_to_the_company = models.URLField(
        max_length=200,
        # Временно может быть пустым, пока АП в урезанном виде (только парсинг с сайта ЖКС)
        blank=True, null=True,
        verbose_name='Ссылка для построения маршрута к управляющей компании',
        help_text='Укажите ссылку для построения маршрута к управляющей компании'
    )

    class Meta:
        verbose_name = 'Управляющая компания'
        verbose_name_plural = 'Управляющие компании'

    def __str__(self):
        return self.management_company


class ManagementCompanySite(models.Model):
    management_company_site = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Наименование участка управляющей компании',
        help_text='Введите наименование участка управляющей компании'
    )
    site_adress = models.CharField(
        max_length=200,
        verbose_name='Адрес участка управляющей компании',
        help_text='Введите адрес участка управляющей компании'
    )
    office_phone = models.TextField(
        blank=True, null=True,
        verbose_name='Телефон эксплуатационного участка',
        help_text='Введите телефон эксплуатационного участка'
    )
    # technician = models.TextField(
    #     blank=True, null=True,
    #     verbose_name='Техник эксплуатационного участка',
    #     help_text='Введите ФИО техника эксплуатационного участка'
    # )
    # technician_phone = models.TextField(
    #     blank=True, null=True,
    #     verbose_name='Телефон техника эксплуатационного участка',
    #     help_text='Введите номер телефона техника эксплуатационного участка'
    # )
    # note = models.TextField(
    #     verbose_name='Примечание'
    # )
    management_company = models.ForeignKey(
        ManagementCompany,
        on_delete=models.CASCADE,
        related_name='all_site',
        verbose_name='Наименование управляющей компании',
        help_text='Выберите управляющую компанию'
    )
    navigation_link_to_the_site = models.URLField(
        max_length=200,
        # Временно может быть пустым, пока АП в урезанном виде (только парсинг с сайта ЖКС)
        blank=True, null=True,
        verbose_name='Ссылка для построения маршрута к участку',
        help_text='Укажите ссылку для построения маршрута к участку упарвляющей компании'
    )

    class Meta:
        verbose_name = 'Участок управляющей компании'
        verbose_name_plural = 'Участки управляющей компании'

    def __str__(self):
        return self.management_company_site


# class Note(models.Model):
#     text = models.TextField(
#         blank=True, null=True,
#         verbose_name='Контакты и примечание по доступу',
#         help_text='Введите контаты и примечание по доступу'
#     )

#     class Meta:
#         verbose_name = 'Комментарий по доступу на МКД'
#         verbose_name_plural = 'Комментарии по доступу на МКД'
    
#     def __str__(self):
#         return self.text


class ApartmentBuilding(models.Model):
    building_adress = models.CharField(
        max_length=200, unique=True, verbose_name='Адрес МКД',
        help_text='Введите адрес МКД'
    )
    # Закомментированно так как связь МКД с УК реализована через модель Участка
    # management_company = models.ForeignKey(
    #     ManagementCompany,
    #     on_delete=models.CASCADE, related_name='buildings',
    #     verbose_name='Наименование управляющей компании',
    #     help_text='Выберите управляющую компанию'
    # )
    management_company_site = models.ForeignKey(
        ManagementCompanySite,
        on_delete=models.CASCADE, related_name='site_buildings',
        verbose_name='Наименование участка управляющей компании',
        help_text='Выберите участок управляющей компании'
    )
    navigation_link_to_the_building = models.URLField(
        max_length=200,
        # Временно может быть пустым, пока АП в урезанном виде (только парсинг с сайта ЖКС)
        blank=True, null=True,
        verbose_name='Ссылка для построения маршрута к МКД',
        help_text='Укажите ссылку для построения маршрута к МКД'
    )
    technician = models.TextField(
        blank=True, null=True,
        verbose_name='Техник эксплуатационного участка',
        help_text='Введите ФИО техника эксплуатационного участка'
    )
    technician_phone = models.TextField(
        blank=True, null=True,
        verbose_name='Телефон техника эксплуатационного участка',
        help_text='Введите номер телефона техника эксплуатационного участка'
    )
    # note = models.ForeignKey(
    #     Note,
    #     on_delete=models.CASCADE, related_name='access_contact',
    #     blank=True, null=True,
    #     verbose_name='Контакты и примечание по доступу',
    #     help_text='Введите контаты и примечание по доступу'
    # )
    in_contract = models.BooleanField(
        blank=True, null=True,
        verbose_name='Наличие МКД в договоре с УК',
        help_text='Укажите есть ли МКД в договоре с УК'
    )
    pipe_support_aria = models.BooleanField(
        blank=True, null=True,
        verbose_name='Наличие стоки(ек) Ария ТВ на МКД',
        help_text='Укажите есть ли на МКД стойки Ария ТВ'
    )
    pipe_support_build = models.BooleanField(
        blank=True, null=True,
        verbose_name='Наличие стоки(ек) по проекту дома',
        help_text='Укажите есть ли на МКД стойки по проект у дома'
    )
    pipe_support_oyster = models.BooleanField(
        blank=True, null=True,
        verbose_name='Наличие стоки(ек) Объединённых сетей на МКД',
        help_text='Укажите есть ли на МКД стойки Объединённых сетей'
    )
    pipe_support_comlink = models.BooleanField(
        blank=True, null=True,
        verbose_name='Наличие стоки(ек) Комлинк на МКД',
        help_text='Укажите есть ли на МКД стойки Комлинк'
    )
    wall_mount_aria = models.BooleanField(
        blank=True, null=True,
        verbose_name='Наличие стенового крепления Ария ТВ на МКД',
        help_text='Укажите есть ли на МКД стеновое крепление Ария ТВ'
    )
    wall_mount_oyster = models.BooleanField(
        blank=True, null=True,
        verbose_name='Наличие стенового крепления Объединённых сетей на МКД',
        help_text='Укажите есть ли на МКД стеновое крепление Объединённых сетей'
    )
    wall_mount_comlink = models.BooleanField(
        blank=True, null=True,
        verbose_name='Наличие стенового крепления Комлинк на МКД',
        help_text='Укажите есть ли на МКД стеновое крепление Комлинк'
    )

    class Meta:
        verbose_name = 'Многоквартирный жилой дом'
        verbose_name_plural = 'Многоквартирные жилые дома'

    def __str__(self):
        return self.building_adress


class Note(models.Model):
    apartment_building = models.ForeignKey(
        ApartmentBuilding,
        on_delete=models.CASCADE, related_name='notes',
        verbose_name='Адрес МКД', help_text='Выберите адрес МКД'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, related_name='notes',
        verbose_name='Автор заметки', help_text='Укажите автора заметки'
    )
    text = models.TextField(
        verbose_name='Текст заметки', help_text='Введите текст заметки'
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.text
