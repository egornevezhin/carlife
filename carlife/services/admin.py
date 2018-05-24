from django.contrib import admin

from .models import Service, Master
# Register your models here.


class MasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'work')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost')


admin.site.register(Master, MasterAdmin)
admin.site.register(Service, ServiceAdmin)