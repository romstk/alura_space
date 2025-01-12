from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #a rota abaixo está sendo importada do arquivo galeria.urls, que é onde está definida as rotas para o app galeria,
    path('', include('galeria.urls')),
    path('', include('usuarios.urls')),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
