from django.contrib import admin
from .models import Ordens

class ListaOrdens(admin.ModelAdmin):
    list_display = ('id', 'nome', 'carro', 'ordem')
    list_display_links = ('id', 'nome', 'carro', 'ordem')
    list_filter = ('ordem',)
    search_fields = ('carro', 'marca','nome')
    list_per_page = 10
    

admin.site.register(Ordens, ListaOrdens)