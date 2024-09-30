from django.contrib import admin
from .models import(
    Biodata,
    Profession_Video,

    
)

@admin.register(Biodata)
class BiodataModelAdmin(admin.ModelAdmin):
    list_display = ['id','pdf']

@admin.register(Profession_Video)
class Profession_VideoModelAdmin(admin.ModelAdmin):
    list_display = ['id','url']    