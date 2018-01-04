from django.shortcuts import render,get_list_or_404,get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.


def post_list(request):
    posts = get_list_or_404(Post)
    return render(request,'blog/post_list.html',{'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'blog/post_detail.html',{'post': post})


def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})