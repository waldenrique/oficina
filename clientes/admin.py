from django.contrib import admin
from .models import Clientes

class ListaClientes(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'email')
    list_per_page = 10

admin.site.register(Clientes, ListaClientes)


