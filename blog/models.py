from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(default='')
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Comment(models.Model):
    #Related_name define como o Post irá referenciar os comments.
    #Ao invés de usar Post.comment_set.all(), usará Post.comments.all()
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField(default='')
    created_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def approve(self):
        self.approved_date = timezone.now()
        self.save()