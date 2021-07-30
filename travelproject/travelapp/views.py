from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from .models import Picture

# Create your views here.


def demo(request):
    obj=Place.objects.all()
    res=Picture.objects.all()
    return render(request,"index.html",{'result':obj,'output':res})