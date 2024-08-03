from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('contact/', include('contact.urls')),
    path('home/', include('home.urls')),
    path('job/', include('job.urls')),
    ]
urlpatterns =+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns =+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
