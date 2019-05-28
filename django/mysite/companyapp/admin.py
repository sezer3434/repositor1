from django.contrib import admin
from .models import Company,Address,Department,Tax,Industry
# Register your models here.

admin.site.register(Company)
admin.site.register(Address)
admin.site.register(Department)
admin.site.register(Tax)
admin.site.register(Industry)
