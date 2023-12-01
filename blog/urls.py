from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.cartao, name='cartao'),
    path('blog/',views.blog, name='blog'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('livro/', include('livro.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)