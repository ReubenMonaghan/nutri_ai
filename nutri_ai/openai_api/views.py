from django.shortcuts import render
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'openai_api/home.html')