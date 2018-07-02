from django.contrib import admin

# Register your models here.
from .models import Status, Order


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Status)
admin.site.register(Order, OrderAdmin)
