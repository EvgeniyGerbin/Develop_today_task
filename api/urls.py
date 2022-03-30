from django.urls import path
from .views import PostDetail, PostList, CommentList, CommentDetail, upvote_new

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('<int:pk>/upvote', upvote_new, name='upvote'),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
]

