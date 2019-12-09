from django.urls import path, include
from django.contrib import admin

from apps.sspanel.views import index

urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls, name="admin"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("prom/", include("django_prometheus.urls")),
    path("api/", include("apps.api.urls", namespace="api")),
    path("sspanel/", include("apps.sspanel.urls", namespace="sspanel")),
]
