from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Url config for django-debug-toolbar
if settings.DEBUG:
    urlpatterns = [
        path('__debug__', include(debug_toolbar.urls)),
    ] + urlpatterns
