from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import home, productos, producto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('productos/', productos, name='productos'),
    path('producto/tshirt', producto, name='producto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
