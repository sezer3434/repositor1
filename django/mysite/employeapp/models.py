from django.db import models

# Create your models here.
#-------------------------------------------------------------------
class Employee(models.Model):
    fullName=models.CharField(max_length=50,verbose_name='Ad')
    salary = models.FloatField(verbose_name='Maas Bilgisi')
    company = models.ForeignKey('companyapp.Company',verbose_name='Sirket', on_delete=models.CASCADE)
    department = models.ManyToManyField('companyapp.Department', verbose_name='Departman')
    price = models.OneToOneField('priceapp.Price',verbose_name='Ucret/gun', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Calisanlar'
        verbose_name = 'Calisan'
        ordering = ['fullName']

#------------------------------------------------------------------------