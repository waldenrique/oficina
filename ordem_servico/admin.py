from django.contrib import admin
from .models import Ordens

class ListaOrdens(admin.ModelAdmin):
    list_display = ('id', 'nome', 'carro', 'ordem')
    list_display_links = ('id', 'nome', 'carro', 'ordem')
    search_fields = ('ordem',)
    list_filter = ('ordem',)
    list_per_page = 10
    

admin.site.register(Ordens, ListaOrdens)