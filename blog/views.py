from django.shortcuts import render, get_object_or_404
from .models import Blog



def all_blogs(request):

    blogs = Blog.objects.order_by('pk')[:7]
    return render(request, 'blog/blogs.html/', {'blogs': blogs})

def detail(request, blog_id):
    detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'detail': detail})