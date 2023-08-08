from django.contrib import admin
from liquorList.models import Liquor
# Register your models here.

class LiquorAdmin(admin.ModelAdmin):
    list_filter = ['brand']
    search_fields = ('name', 'brand')

admin.site.register(Liquor, LiquorAdmin)