from django.shortcuts import render
from .models import Post, Categoria

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html',
    {'posts':posts})

def detalhes(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'detalhes.html',{'post':post})
    

# Create your views here.
