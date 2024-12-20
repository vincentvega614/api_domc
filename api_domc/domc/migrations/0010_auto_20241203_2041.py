# Generated by Django 3.2 on 2024-12-03 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domc', '0009_auto_20241202_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentbuilding',
            name='in_contract',
            field=models.BooleanField(blank=True, help_text='Укажите есть ли МКД в договоре с управляющей компание', null=True, verbose_name='Наличие МКД в договоре с управляющей компанией'),
        ),
        migrations.AlterField(
            model_name='apartmentbuilding',
            name='navigation_link_to_the_building',
            field=models.URLField(help_text='Укажите ссылку для построения маршрута к МКД', verbose_name='Ссылка для построения маршрута к МКД'),
        ),
        migrations.AlterField(
            model_name='managementcompany',
            name='navigation_link_to_the_company',
            field=models.URLField(help_text='Укажите ссылку для построения маршрута к управляющей компании', verbose_name='Ссылка для построения маршрута к управляющей компании'),
        ),
        migrations.AlterField(
            model_name='managementcompanysite',
            name='navigation_link_to_the_site',
            field=models.URLField(help_text='Укажите ссылку для построения маршрута к участку упарвляющей компании', verbose_name='Ссылка для построения маршрута к участку'),
        ),
    ]
