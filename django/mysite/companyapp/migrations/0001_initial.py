# Generated by Django 2.2.1 on 2019-05-27 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all', models.CharField(max_length=100, verbose_name='Tum sirketler')),
            ],
            options={
                'verbose_name': 'Tum Sirket',
                'verbose_name_plural': 'Tum Sirketler',
            },
        ),
    ]
