# Generated by Django 4.2.4 on 2023-08-17 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delightsapp', '0007_menuitem_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='description',
            field=models.TextField(default='Description', max_length=100),
        ),
    ]
