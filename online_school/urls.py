from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from lms_system.views import *
from online_school import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('lms_system.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found
handler500 = page_error_view
handler403 = permission_denied_view
handler400 = bad_request_view
