from django.contrib import admin

# Register your models here.
from django.db import models
from .models import Post, Company
class MyCompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = ('name' , 'slug' , 'description' , 'pe_ratio')

admin.site.register(Company , MyCompanyAdmin)

#username for admin:hp
#password :hp