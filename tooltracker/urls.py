from django.contrib import admin
from django.urls import path
from tools.views import dashboard

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", dashboard, name="dashboard"),   # domov = prehľad náradia
]
