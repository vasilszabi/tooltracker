from django.shortcuts import render
from .models import Tool

def dashboard(request):
    tools = Tool.objects.all().order_by('name')
    return render(request, "dashboard.html", {"tools": tools})
