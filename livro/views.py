from django.shortcuts import render

def livro(request):
    return render(request, 'books.html')
# Create your views here.
