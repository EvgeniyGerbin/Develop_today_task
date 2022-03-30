from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    link = models.URLField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)
    amount_upvotes = models.PositiveIntegerField(default=0)
    author_name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.title} by {self.author_name}'


class Comment(models.Model):
    author = models.CharField(max_length=50, default='Guest')
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'comment by {self.author} about {self.post}'
