from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request, "main.html")

def fire(request):
    return render(request, "fire.html")

def wind(request):
    return render(request, "wind.html")

def ice(request):
    return render(request, "ice.html")

def lightning(request):
    return render(request, "lightning.html")

# Create your views here.
