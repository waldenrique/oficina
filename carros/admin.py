from django.contrib import admin
from .models import Carros

class ListaCarro(admin.ModelAdmin):
    list_display = ('id', 'carro', 'marca','nome')
    list_display_links = ('id', 'carro', 'marca','nome')
    search_fields = ('carro', 'marca','nome')
    list_filter = ('marca','nome')
    list_per_page = 10

admin.site.register(Carros, ListaCarro)
