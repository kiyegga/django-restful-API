from blog.models import Post
from rest_framework import generics
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    # queryset = Post.objects.all() 
    queryset = Post.PostObjects.all()
    serializer_class = PostSerializer
    

class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
 
