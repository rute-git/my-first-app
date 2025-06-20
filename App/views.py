from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    Posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'App/post_list.html', {'Posts':Posts})
