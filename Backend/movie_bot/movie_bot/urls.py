from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movieadmin/', include('movie_admin.urls')),
    path('', RedirectView.as_view(url='movieadmin/')),
    path('userapi/', include('userapi.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
