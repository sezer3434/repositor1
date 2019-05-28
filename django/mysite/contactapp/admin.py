from django.contrib import admin
from .models import City,District,Street,Quarter
# Register your models here.
admin.site.register(City)
admin.site.register(District)
admin.site.register(Quarter)
admin.site.register(Street)
