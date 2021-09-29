from django.shortcuts import render
from .models import Project
# Create your views here.


def home(request):
    context = {'projects': Project.objects.all()}
    return render(request, 'portfolio/home.html', context)
