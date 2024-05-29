from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'landing/index.html', {})

def about(request):
    return render(request, 'landing/about.html', {})