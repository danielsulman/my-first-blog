from django.shortcuts import render,get_list_or_404,get_object_or_404,redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login

# Create your views here.


def post_list(request):
    posts = get_list_or_404(Post, published_date__lte=timezone.now())
    return render(request,'blog/post_list.html',{'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'blog/post_detail.html',{'post': post})

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_new.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = get_list_or_404(Post, published_date__isnull=True, author=request.user)

    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:post_list')

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        #esse POST abaixo se refere ao method, não o model
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/add_comment_to_post.html',{'form': form})

@login_required
def comment_remove(request, pk):
   comment = get_object_or_404(Comment, pk=pk)
   comment.delete()
   return redirect('blog:post_detail', pk=comment.post.pk)

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog:post_detail', pk=comment.post.pk)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('blog:post_list')
    else:
        form = UserCreationForm()

    return render(request, 'blog/signup.html', {'form': form})