from django.contrib import admin
# Register your models here.
from .models import GraphicDesign,WebDesign,MobileApplication,Technology,EditTool

admin.site.register(GraphicDesign)
admin.site.register(WebDesign)
admin.site.register(MobileApplication)
admin.site.register(Technology)
admin.site.register(EditTool)
