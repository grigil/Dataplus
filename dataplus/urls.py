from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from doc_send import views as send_view
from moderator_panel import views as moder_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('doc_send/', send_view.Send, name='home'),
    path('moderator_panel/', moder_view.Send, name='moder_home'),
    url(r'^logout', send_view.logout, name='logout'),
]
# Serving the media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()