# Generated by Django 2.2.1 on 2019-05-27 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyapp', '0003_company_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Departmen')),
            ],
            options={
                'verbose_name': 'Departman',
                'verbose_name_plural': 'Departmanlar',
            },
        ),
        migrations.AlterField(
            model_name='company',
            name='department',
            field=models.ManyToManyField(to='companyapp.Department', verbose_name='Departman'),
        ),
    ]
