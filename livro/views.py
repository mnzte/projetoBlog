from django.shortcuts import render

def livro(request):
    return render(request, 'livros.html')
# Create your views here.
