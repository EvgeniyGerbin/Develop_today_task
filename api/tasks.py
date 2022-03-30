from develop_today_task.celery import app
from .models import Post


@app.task
def upvote_reset():
    post_list = Post.objects.all()
    for post in post_list:
        post.upvote_reset = 0
        post.save()
        print(f"Successfully reset upvotes {post.id}")