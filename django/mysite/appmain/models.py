from django.db import models

# Create your models here.
from django.db import models
#from mysite.employeapp.models import Personel,Manager


#1------------------------------------------------------------------------
class DepartmentModel(models.Model):
    name = models.CharField(max_length=50,verbose_name='Departmen')
    #fore = models.ForeignKey('employeapp.Manager',on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Departmanlar'
        verbose_name = 'Departman'

    def __str__(self):
        return self.name

#2------------------------------------------------------------------------
class BankModel(models.Model):
    name = models.CharField(verbose_name='Banka',max_length=50)
    branch = models.CharField(verbose_name='Sube',max_length=50)
    account = models.TextField(verbose_name='Hesap No',max_length=255)

    class Meta:
        verbose_name_plural = 'Banka Hesaplari'
        verbose_name = 'Banka Hesabi'

    def __str__(self):
        return self.name

#3------------------------------------------------------------------------
class TaxModel(models.Model):
    administration = models.CharField(verbose_name='Vergi Dairesi',max_length=100)
    taxNo = models.BigIntegerField(verbose_name='Vergi No')


    class Meta:
        verbose_name_plural = 'Vergi Bilgileri'
        verbose_name = 'Vergi'

    def __str__(self):
        return str(self.taxNo)+ ''+self.administration
#4----------------------------------------------------------------------------------
class PriceModel(models.Model):
    daily_wage = models.FloatField(verbose_name='Birim Fiyat')

    class Meta:
        verbose_name_plural='Fiyatlar'
        verbose_name = 'Fiyat'

    def __str__(self):
        return str(self.daily_wage)

#-----------------------------------------------------------------------------------------------
#               Service
#5----------------------------------------------------------------------------------------------
class ServiceModel(models.Model):
    #hizmetin adi
    name = models.CharField(verbose_name='Hizmet',max_length=100)
    #hangi birim bu hizmeti saglayacaksa
    department = models.ForeignKey(DepartmentModel,verbose_name='Departman',on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Hizmetler'
        verbose_name = 'Hizmet'

    def __str__(self):
        return self.name

#6-------------address--------------------------------------------------------------
class AddressModel(models.Model):
    city = models.CharField(verbose_name='Sehir',max_length=50)
    district = models.CharField(verbose_name='mahalle',max_length=50)
    street =   models.CharField(verbose_name='sokak',max_length=50)
    home = models.CharField(verbose_name='Ev No',max_length=50)

    class Meta:
        verbose_name_plural='Adresler'
        verbose_name = 'Adres'

    def __str__(self):
        return self.city+' '+self.district


#7-------------ındustry-------------------------------------------------------------
class IndustryModel(models.Model):
    #parent = models.ForeignKey(IndustryModel)
    name = models.CharField(verbose_name='Sektor',max_length=100)

    class Meta:
        verbose_name_plural='Sektorler'
        verbose_name = 'Sektor'

    def __str__(self):
        return str(self.name)

#8------------------------------------------------------------------------------------------------
class CompanyModel(models.Model):
    name    = models.CharField(max_length=50,verbose_name='Sirket ')
    address = models.ForeignKey(AddressModel,verbose_name='Adres',on_delete=models.CASCADE)
    bank    = models.ForeignKey(BankModel,max_length=250,verbose_name='Banka Hesap',on_delete=models.CASCADE)
    industry = models.ForeignKey(IndustryModel,on_delete=models.CASCADE)
    tax      = models.ForeignKey(TaxModel,verbose_name='Vergi Dairesi',on_delete=models.CASCADE)
    department = models.ManyToManyField(DepartmentModel,verbose_name='Departman')
    company_reference= models.IntegerField(verbose_name='Referans')
    #company_logo = models.ImageField('/...')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Sirketler'
        verbose_name = 'Sirket'

#9---------OrderModel--------------------------------------------
class OrderModel(models.Model):
    orderType = models.IntegerField(verbose_name='Teklif tipi')

    def __str__(self):
        return str(self.orderType)

    class Meta:
        verbose_name_plural='Teklifler'
        verbose_name = 'Teklif'

#10----------------------------------------------------------------
class ContactModel(models.Model):
     mobile  = models.FloatField(max_length=10,verbose_name='Birim Fiyat')
     email   = models.EmailField(verbose_name='E posta',max_length=100)
     website = models.URLField(verbose_name='web',max_length=100)

     class Meta:
        verbose_name_plural='iletisim Bilgileri'
        verbose_name = 'iletisim'

     def __str__(self):
        return str(self.mobile)+'-'+ str(self.email)

#11------------------------------------------------------------------
class EmployeeModel(models.Model):
    emp_firstname=models.CharField(max_length=50,verbose_name='Ad')
    emp_lastname=models.CharField(max_length=50,verbose_name='Soyad')
    #her calisan bir veya daha fazla birimde calÄ±sabilir
    department = models.ForeignKey(DepartmentModel,verbose_name='Departman',on_delete=models.CASCADE)
    #her calÄ±san sadece bir sirkette calÄ±sabilir
    company    = models.ForeignKey(CompanyModel,on_delete=models.CASCADE,verbose_name='Sirket')
    #her calisanin calÄ±sma ucreti farkli olsun
    price = models.OneToOneField(PriceModel,on_delete=models.CASCADE,verbose_name='Ucret')
    #service = models.ManyToManyField(Service,verbose_name='Service/Hizmet')


    class Meta:
        verbose_name_plural='Calisanlar'
        verbose_name = 'Calisan'

    def __str__(self):
        return self.emp_firstname+ ' '+self.emp_lastname