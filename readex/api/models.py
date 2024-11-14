from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    avatar = models.TextField(max_length=50)
    read_day = models.DateField()
    post_reads = models.IntegerField(default=0)
    comment_reads = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)

class Community(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_communities')
    post_reads = models.IntegerField(default=0)
    comment_reads = models.IntegerField(default=0)
    rules = models.TextField(max_length=2000)

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memberships')
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='memberships')
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'community')


class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=12000)
    post_reads = models.IntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    discussions = models.IntegerField(default=0)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    parent = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE,related_name="replies")
    comment = models.TextField(max_length=5000)
    comment_reads = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)



