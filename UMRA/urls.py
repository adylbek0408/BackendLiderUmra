
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tour/', include('apps.tour.urls')),
    path('api/crm/', include('apps.crm.urls')),
    path('api/blog/', include('apps.blog.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

