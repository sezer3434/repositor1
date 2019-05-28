from django.db import models

# Create your models here.
class Price(models.Model):
    class PriceModel(models.Model):
        daily_wage = models.FloatField(verbose_name='Birim Fiyat')

        class Meta:
            verbose_name_plural = 'Fiyatlar'
            verbose_name = 'Fiyat'

        def __str__(self):
            return str(self.daily_wage)
