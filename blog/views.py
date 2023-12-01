from django.shortcuts import render
from .models import Post, Categoria
from django.contrib.auth.decorators import login_required

@login_required
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html',
    {'posts':posts})

@login_required
def cartao(request):
    return render(request, 'cartao.html',
    )
    

# Create your views here.
