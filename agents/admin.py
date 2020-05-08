from django.contrib import admin
from .models import Agent
# Register your models here.


class AgentListing(admin.ModelAdmin):
    list_display = ('name', 'title', 'email','linkedIn')
    list_filter = ('name','title')
    search_fields = ('name', 'title')
    list_per_page = 10

admin.site.register(Agent, AgentListing)
