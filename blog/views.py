from django.shortcuts import render,get_list_or_404
from .models import Post

# Create your views here.


def post_list(request):
    posts = get_list_or_404(Post)
    return render(request,'blog/post_list.html',{'posts': posts})
