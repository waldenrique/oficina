from operator import index
from django.urls import path

from.import views

urlpatterns = [
    path('', views.index, name='index'),
    path('servico', views.servico, name='servico'),
    path('contato', views.contato, name='contato'),
    path('quemsomos', views.quemsomos, name='quemsomos'),
    path('localizacao', views.localizacao, name='localizacao'),
    path('blog', views.blog, name='blog'),
    path('login', views.blog, name='login'),
    path('logout', views.blog, name='logout'),
    path('dashboard', views.blog, name='dashboard'),
    
    
]