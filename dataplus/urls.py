from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from doc_send import views as send_view
from moderator_panel import views as moder_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('doc_send/', send_view.Send, name='home'),
    path('moderator_panel/', moder_view.Send, name='moder_home'),
    url(r'^logout', send_view.logout, name='logout'),
]
