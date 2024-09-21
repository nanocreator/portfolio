from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='home')),
    path('blog/', include('blog.urls', namespace='blog')),
    # path('work', include('work.urls')),
    path('about/', include('about.urls')),
    path('projects/', include('project.urls', namespace='projects')),
] + debug_toolbar_urls()
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
