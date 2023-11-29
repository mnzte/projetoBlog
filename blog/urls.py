from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.blog, name='blog'),
    path('detalhes/<int:id>',views.detalhes, name='detalhes'),
    path('cartao/', views.cartao, name='cartao'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('filme/', include('filme.urls')),
    path('series/', include('series.urls')),
    path('livro/', include('livro.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)