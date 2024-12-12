from django.contrib import admin
from .models import *

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')
    
class EmpolyeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmpolyeeAdmin)