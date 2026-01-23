from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to Chaste Essentials API")


urlpatterns = [
    path('', home),  # Root URL
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
]

if settings.DEBUG:
    # Serve static and media files during development
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
