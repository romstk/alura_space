from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #a rota abaixo está sendo importada do arquivo galeria.urls, que é onde está definida a rota para o app galeria,
    path('', include('galeria.urls')),
]
