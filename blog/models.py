from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Post(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='media')
    feedbcak = models.TextField(blank=False)   

    def __str__(self):
        return self.nome