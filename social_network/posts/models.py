from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


# User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def likes_count(self):
        return self.likes.all().count()
       
    def __str__(self):
        return f'{self.user} {self.text} {self.created_at}'   


# для доп. задания
# class PostImage(models.Model):
#     ...


class Like(models.Model):
    like = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    
    def __str__(self):
        return f'{self.like} {self.user} {self.post}'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return f'{self.author} {self.text} {self.post} {self.created_at}'
