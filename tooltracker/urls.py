from django.contrib import admin
from django.urls import path
from tools.views import dashboard

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", dashboard, name="dashboard"),   # domov = prehľad náradia
]

from tools.views import dashboard, tool_detail

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", dashboard, name="dashboard"),
    path("tool/<int:pk>/", tool_detail, name="tool_detail"),
]
