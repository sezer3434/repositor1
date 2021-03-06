# Generated by Django 2.2.1 on 2019-05-27 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='Sehir')),
                ('district', models.CharField(max_length=50, verbose_name='mahalle')),
                ('street', models.CharField(max_length=50, verbose_name='sokak')),
                ('home', models.CharField(max_length=50, verbose_name='Ev No')),
            ],
            options={
                'verbose_name': 'Adres',
                'verbose_name_plural': 'Adresler',
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Banka')),
                ('branch', models.CharField(max_length=50, verbose_name='Sube')),
                ('account', models.TextField(max_length=255, verbose_name='Hesap No')),
            ],
            options={
                'verbose_name': 'Banka Hesabi',
                'verbose_name_plural': 'Banka Hesaplari',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Sirket ')),
                ('company_reference', models.IntegerField(verbose_name='Referans')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companyapp.Address', verbose_name='Adres')),
                ('bank', models.ForeignKey(max_length=250, on_delete=django.db.models.deletion.CASCADE, to='companyapp.Bank', verbose_name='Banka Hesap')),
            ],
            options={
                'verbose_name': 'Sirket',
                'verbose_name_plural': 'Sirketler',
            },
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Sektor')),
            ],
            options={
                'verbose_name': 'Sektor',
                'verbose_name_plural': 'Sektorler',
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administration', models.CharField(max_length=100, verbose_name='Vergi Dairesi')),
                ('taxNo', models.BigIntegerField(verbose_name='Vergi No')),
            ],
            options={
                'verbose_name': 'Vergi',
                'verbose_name_plural': 'Vergi Bilgileri',
            },
        ),
        migrations.DeleteModel(
            name='AllCompany',
        ),
        migrations.AddField(
            model_name='company',
            name='industry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companyapp.Industry'),
        ),
        migrations.AddField(
            model_name='company',
            name='tax',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companyapp.Tax', verbose_name='Vergi Dairesi'),
        ),
    ]
