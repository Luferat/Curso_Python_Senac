from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def metodoProduto (request):
    # return HttpResponse('Esta é a produto!')

    # Carrega o template html como retorno do método
    return render(request, 'produtox/index.html')
