# Generated by Django 2.2.1 on 2019-05-27 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('serviceapp', '0002_delete_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraphicDesign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Mobile Uygulama')),
            ],
            options={
                'verbose_name': 'Grafik Tasarim',
                'verbose_name_plural': 'Grafik Tasarimlar',
            },
        ),
        migrations.CreateModel(
            name='MobileApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Mobile Uygulama')),
            ],
            options={
                'verbose_name': 'Mobile Uygulama',
                'verbose_name_plural': 'Mobile Uygulamalar',
            },
        ),
        migrations.CreateModel(
            name='WebDesign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Web Tasarim')),
            ],
            options={
                'verbose_name': 'Web Tasarim',
                'verbose_name_plural': 'Web Tasarimlar',
            },
        ),
    ]
