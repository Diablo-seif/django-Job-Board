from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('accounts/', include('accounts.urls', namespace= 'accounts')),
    path('contact/', include('contact.urls', namespace= 'contact')),
    path('home/', include('home.urls', namespace= 'home')),
    path('job/', include('job.urls', namespace= 'job')),

    ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 



