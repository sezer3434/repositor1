from django.db import models

# Create your models here.
from smart_selects.db_fields import ChainedForeignKey


class City(models.Model):
    order = models.IntegerField(verbose_name="Siparis")
    name = models.CharField(max_length=255, verbose_name="Sehir Ad")
    value = models.CharField(max_length=255, verbose_name="Deger", blank=True)
    coordinates = models.TextField(verbose_name="Koordinat", null=True, blank=True)

    class Meta:
        verbose_name_plural = "1 - Sehirler"
        verbose_name = "Sehir"
        ordering = ['name']

    def __str__(self):
        return self.name

class District(models.Model):
    city = models.ForeignKey(City, verbose_name="City", on_delete=models.CASCADE)
    order = models.IntegerField(verbose_name="Siparis")
    name = models.CharField(max_length=255, verbose_name="Ilce")
    value = models.CharField(max_length=255, verbose_name="Deger", null=True)
    coordinates = models.TextField(verbose_name="Koordinat", null=True, blank=True)

    class Meta:
        verbose_name_plural = "2 - Ilceler"
        verbose_name = "Ilce"
        ordering = ['city__name', 'name']

    def __str__(self):
        return "{0} - {1}".format(
            self.city.name,
            self.name,
        )

class Quarter(models.Model):
    city = models.ForeignKey(City, verbose_name="Sehir", default="", on_delete=models.CASCADE)
    district = models.ForeignKey(District, verbose_name="İlce", null=True, on_delete=models.CASCADE)
    order = models.IntegerField(verbose_name="Siparis")
    name = models.CharField(max_length=255, verbose_name="Mahalle")
    coordinates = models.TextField(verbose_name="Kordinat", null=True, blank=True)

    class Meta:
        verbose_name_plural = "3 - Mahalleler"
        verbose_name = "Mahalle"
        ordering = ['district__name', 'name']

    def __str__(self):
        return "{0} - {1} - {2}".format(
            self.district.city.name,
            self.district.name,
            self.name,
        )

class Street(models.Model):
    city = models.ForeignKey('contactapp.City', verbose_name="City", null=True, on_delete=models.CASCADE)
    district = ChainedForeignKey('contactapp.District', chained_field='city', chained_model_field='city',
                                 verbose_name="Ilce", null=True)
    quarter = ChainedForeignKey('contactapp.Quarter', chained_field='district', chained_model_field='district',
                                verbose_name="Mahalle", null=True)
    order = models.IntegerField(verbose_name="Siparis")
    name = models.CharField(max_length=255, verbose_name="Sokak")

    class Meta:
        verbose_name_plural = "4 - Sokaklar"
        verbose_name = "Sokak"
        ordering = ['quarter__name', 'name']

    def __str__(self):
        return "{0} - {1} - {2} - {3}".format(
            self.city.name,
            self.district.name,
            self.quarter.name,
            self.name,
        )

