from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.


def home(request):
    context = {'blogs': Blog.objects.order_by('-date')}
    return render(request, 'blog/all_blogs.html', context)


def detail(request, id):

    return render(request, 'blog/detail.html', {'blog': get_object_or_404(Blog, id=id)})
