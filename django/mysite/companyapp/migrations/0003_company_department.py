# Generated by Django 2.2.1 on 2019-05-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0002_companymodel_department'),
        ('companyapp', '0002_auto_20190527_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='department',
            field=models.ManyToManyField(to='appmain.DepartmentModel', verbose_name='Departman'),
        ),
    ]
