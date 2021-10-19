from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path

urlpatterns = patterns('',
    path('^$', lambda request: redirect('^planet/', permanent=False)),
    path(r'^planet/', include('planetplanet.planet.urls')),
    path(r'^admin/', admin.site.urls),
)
