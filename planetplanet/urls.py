from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, re_path

urlpatterns = [
    re_path('^$', lambda request: redirect('^planet/', permanent=False)),
    re_path(r'^planet/', include('planet.urls')),
    re_path(r'^admin/', admin.site.urls),
]
