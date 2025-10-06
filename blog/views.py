<<<<<<< HEAD
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
=======
from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})
>>>>>>> 897569da6c95a69cb4e8923559d0948e980bed1a
