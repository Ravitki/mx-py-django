from django.urls import path
from django.http import JsonResponse

def ping_view(request):
    return JsonResponse({"pong": True})

urlpatterns = [
    path('ping/', ping_view),
]
