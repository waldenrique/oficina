from django.contrib import admin
from .models import Carros

class ListaCarro(admin.ModelAdmin):
    list_display = ('id', 'carro')
    list_display_links = ('id', 'carro', 'modelo')
    search_fields = ('carro', 'modelo')
    list_per_page = 10

admin.site.register(Carros, ListaCarro)
