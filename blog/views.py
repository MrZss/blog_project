#!/usr/bin/python
#encoding:utf-8
from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.http import HttpResponse

def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', context={'post': post})