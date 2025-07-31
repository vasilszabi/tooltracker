from django.contrib import admin
from .models import Tool, Branch, ServiceRecord, ToolHistory

admin.site.register(Tool)
admin.site.register(Branch)
admin.site.register(ServiceRecord)
admin.site.register(ToolHistory)
