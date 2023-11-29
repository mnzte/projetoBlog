from django.shortcuts import render

def filme(request):
    return render(request, 'filmes.html')

# Create your views here.
