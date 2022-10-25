from django.contrib import admin
from .models import Servico

class ListaServicos(admin.ModelAdmin):
    list_display = ('id', 'nome_servico')
    list_display_links = ('id', 'nome_servico')
    search_fields = ('id', 'nome_servico')
    list_filter = ('id', 'nome_servico')
    list_per_page = 10
    
admin.site.register(Servico, ListaServicos)
