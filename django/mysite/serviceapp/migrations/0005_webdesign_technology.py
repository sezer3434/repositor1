# Generated by Django 2.2.1 on 2019-05-27 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0004_auto_20190527_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='webdesign',
            name='technology',
            field=models.ManyToManyField(to='serviceapp.Technology', verbose_name='teknolojiler'),
        ),
    ]
