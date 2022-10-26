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

def login(request):
    return render(request,'login.html')

def logout(request):
    return render(request,'logout.html')

def deshdoard(request):
    return render(request,'deshdoard.html')

def servico(request):
    servicos = Servico.objects.all()

    dados ={
        'servicos' : servicos
    }
    return render(request,'servico.html', dados)


