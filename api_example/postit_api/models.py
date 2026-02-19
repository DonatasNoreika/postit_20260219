from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField()
    body = models.TextField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']


class Comment(models.Model):
    post = models.ForeignKey(to="Post", on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']


class PostLike(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(to="Post", on_delete=models.CASCADE)


class CommentLike(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    comment = models.ForeignKey(to="Comment", on_delete=models.CASCADE)
