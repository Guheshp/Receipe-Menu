
from django.contrib import admin
from django.urls import path, include


from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('webapp.urls')),

    path('r_home/',include('menu.urls'),name='my-r_home')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)