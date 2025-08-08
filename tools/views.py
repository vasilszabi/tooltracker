from django.shortcuts import render
from .models import Tool

def dashboard(request):
    tools = Tool.objects.all().order_by('name')
    return render(request, "dashboard.html", {"tools": tools})

from django.shortcuts import render, get_object_or_404
from .models import Tool

def tool_detail(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    services = tool.services.order_by('-service_date')  # related_name="services"
    # ak si nepoužil related_name, tak daj: tool.servicerecord_set.all()
    return render(request, "tool_detail.html", {"tool": tool, "services": services})
