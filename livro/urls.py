from django.urls import path,include
from . import views

urlpatterns = [
  path('biblioteca', views.livro,name='livro')
]