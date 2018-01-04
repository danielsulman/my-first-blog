from django.shortcuts import render,get_list_or_404,get_object_or_404,redirect  
from .models import Post
from .forms import PostForm
from django.utils import timezone

# Create your views here.


def post_list(request):
    posts = get_list_or_404(Post)
    return render(request,'blog/post_list.html',{'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'blog/post_detail.html',{'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})