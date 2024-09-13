from django.shortcuts import render

# Create your views here.
def home(request):
    view = 'info.html'
    return render(request, view)

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def experiencias(request):
    return render(request, 'experiencias.html')