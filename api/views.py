from django.http import Http404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(APIView):

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["PATCH"])
def upvote_new(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.amount_upvotes += 1
    post.save()
    serializer = PostSerializer(post)
    return Response(serializer.data)


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentDetail(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

