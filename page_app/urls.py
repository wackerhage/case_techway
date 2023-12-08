from django.urls import path
from page_app.views import index, contato, services

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Cadastrar URLs aqui
    path('', index),
    path('services/', services),
    path('contato/', contato),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
