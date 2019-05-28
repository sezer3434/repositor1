from django.db import models
# Create your models here.
from smart_selects.db_fields import ChainedForeignKey

#-----------------------------------------------------------------------------------------------------------------------
class Address(models.Model):
    city = models.ForeignKey('contactapp.City', verbose_name='IL', on_delete=models.DO_NOTHING)
    district = models.ForeignKey('contactapp.District', verbose_name='ILCE', on_delete=models.DO_NOTHING)
    quarter = models.ForeignKey('contactapp.Quarter', verbose_name='MAHALLE', on_delete=models.DO_NOTHING)
    street = models.ForeignKey('contactapp.Street', verbose_name='SOKAK', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Adresler"
        verbose_name = "Adres"

    def __str__(self):
        return self.street

#2------------------------------------------------------------------------
class Bank(models.Model):
    name = models.CharField(verbose_name='Banka',max_length=50)
    branch = models.CharField(verbose_name='Sube',max_length=50)
    account = models.TextField(verbose_name='Hesap No',max_length=255)

    class Meta:
        verbose_name_plural = 'Banka Hesaplari'
        verbose_name = 'Banka Hesabi'

    def __str__(self):
        return self.name


#7-------------ındustry-------------------------------------------------------------
class Industry(models.Model):
    parent = models.ForeignKey('companyapp.Industry',verbose_name='Ana Sektor',blank=True, null=True,on_delete=models.DO_NOTHING)
    name = models.CharField(verbose_name='Sektor Adi',max_length=100)

    class Meta:
        verbose_name_plural='Sektorler'
        verbose_name = 'Sektor'

    def __str__(self):
        if self.parent:
            return "{}-{}".format(self.parent.name, self.name)
        else:
            return "{}".format(self.name)

#3------------------------------------------------------------------------
class Tax(models.Model):
    administration = models.CharField(verbose_name='Vergi Dairesi',max_length=100)
    taxNo = models.BigIntegerField(verbose_name='Vergi No')


    class Meta:
        verbose_name_plural = 'Vergi Bilgileri'
        verbose_name = 'Vergi'

    def __str__(self):
        return str(self.taxNo)+ ''+self.administration

#-----------------------------------------------------
#1------------------------------------------------------------------------
class Department(models.Model):
    name = models.CharField(max_length=50,verbose_name='Departmen')
    #fore = models.ForeignKey('employeapp.Manager',on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Departmanlar'
        verbose_name = 'Departman'

    def __str__(self):
        return self.name

#-----------------------------------------------------------------------------------------------------------------
class Company(models.Model):
    name = models.CharField(max_length=50, verbose_name='Sirket ')
    address = models.ForeignKey('companyapp.Address', verbose_name='Adres', on_delete=models.CASCADE)
    bank = models.ForeignKey('companyapp.Bank', max_length=250, verbose_name='Banka Hesap', on_delete=models.CASCADE)
    industry = models.ForeignKey('companyapp.Industry', verbose_name="Sektor", on_delete=models.DO_NOTHING)
    tax = models.ForeignKey('companyapp.Tax', verbose_name='Vergi Dairesi', on_delete=models.CASCADE)

    company_reference = models.IntegerField(verbose_name='Referans')

    # company_logo = models.ImageField('/...')

    def __str__(self):
        return self.name+' '+str(self.industry)

    class Meta:
        verbose_name_plural = 'Sirketler'
        verbose_name = 'Sirket'