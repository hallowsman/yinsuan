from django.shortcuts import render
from django.http import *
from .models import *


# Create your views here.

def index(request):
    indexBanner_list = IndexBanner.objects.all()
    context = {'indexBanner_list': indexBanner_list}
    return render(request, 'introduce/index.html', context)
