from django.contrib import admin
from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title','is_published','address', 'contract', 'list_date','price', 'agent')
    list_filter = ('agent',)
    list_editable = ('is_published',)
    search_fields = ('title','address', 'price', 'agent')
    list_per_page = 20
admin.site.register(Listing, ListingAdmin)