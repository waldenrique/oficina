from django.shortcuts import render
from servico.models import Servico

def index(request):
    return render(request,'index.html')

def contato(request):
    return render(request,'contato.html')

def quemsomos(request):
    return render(request,'quemsomos.html')

def blog(request):
    return render(request,'blog.html')

def localizacao(request):
    return render(request,'localizacao.html')

def servico(request):
    servicos = Servico.objects.all()

    dados ={
        'servicos' : servicos
    }
    return render(request,'servico.html', dados)


