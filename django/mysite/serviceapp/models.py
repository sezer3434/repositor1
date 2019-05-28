from django.db import models

# Create your models here.

#-------------------------------------------

class EditTool(models.Model):
    name = models.CharField(verbose_name='Araclar', max_length=100)

    class Meta:
        verbose_name_plural = 'Araclar'
        verbose_name = 'Araclar'

    def __str__(self):
        return self.name

class Technology(models.Model):
    parent = models.ForeignKey('serviceapp.Technology', verbose_name='Ana Sektor', blank=True, null=True,
                               on_delete=models.DO_NOTHING)
    name = models.CharField(verbose_name='Teknoloji', max_length=100)

    class Meta:
        verbose_name_plural = 'Teknolojiler'
        verbose_name = 'Teknologi'

    def __str__(self):
        return self.name

#----------------------------------------------------------------------------------------------------------------------
class WebDesign(models.Model):
    name = models.CharField(verbose_name='Web Tasarim',max_length=100)
    technology = models.ManyToManyField('serviceapp.Technology',verbose_name='teknolojiler')

    class Meta:
        verbose_name_plural = 'Web Tasarimlar'
        verbose_name = 'Web Tasarim'

    def __str__(self):
        return self.name

class MobileApplication(models.Model):
    name = models.CharField(verbose_name='Mobile Uygulama', max_length=100)

    class Meta:
        verbose_name_plural = 'Mobile Uygulamalar'
        verbose_name = 'Mobile Uygulama'

    def __str__(self):
        return self.name

class GraphicDesign(models.Model):
    name = models.CharField(verbose_name='Grafik Tasarım', max_length=100)
    editTool = models.ManyToManyField('serviceapp.EditTool', verbose_name='program')

    class Meta:
        verbose_name_plural = 'Grafik Tasarimlar'
        verbose_name = 'Grafik Tasarim'

    def __str__(self):
        return self.name