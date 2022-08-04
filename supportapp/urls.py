from django.contrib import admin
from django.urls import include, path

admin.site.index_title = 'Support Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('support/', include('support.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
