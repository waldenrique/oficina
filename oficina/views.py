from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def contato(request):
    return render(request,'contato.html')

servicos = {
    1:'Bateria',
    2:'Mecânica em geral',
    3:'Motor',
    4:'Oléo'
}

dados ={
    'nome_servico' : servicos
}


def servico(request):
    return render(request,'servico.html', dados)

def quemsomos(request):
    return render(request,'quemsomos.html')

def blog(request):
    return render(request,'blog.html')

def localizacao(request):
    return render(request,'localizacao.html')

    

