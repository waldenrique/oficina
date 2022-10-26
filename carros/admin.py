from django.contrib import admin
from .models import Carros

class ListaCarro(admin.ModelAdmin):
    list_display = ('id', 'carro', 'marca')
    list_display_links = ('id', 'carro', 'marca')
    search_fields = ('carro', 'marca')
    list_filter = ('marca',)
    list_per_page = 10

admin.site.register(Carros, ListaCarro)
