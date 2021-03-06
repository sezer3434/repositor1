# Generated by Django 2.2.1 on 2019-05-27 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=50, verbose_name='Ad')),
                ('salary', models.FloatField(verbose_name='Maas Bilgisi')),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
            ],
            options={
                'verbose_name': 'Yonetici',
                'verbose_name_plural': 'Yoneticiler',
            },
        ),
        migrations.CreateModel(
            name='Personel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=50, verbose_name='Ad')),
                ('salary', models.FloatField(verbose_name='Maas Bilgisi')),
                ('department', models.CharField(max_length=100, verbose_name='Departman')),
            ],
            options={
                'verbose_name': 'Personel',
                'verbose_name_plural': 'Personeller',
            },
        ),
    ]
