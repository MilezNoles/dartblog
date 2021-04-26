from django.shortcuts import render
from rest_framework.decorators import api_view
from blog.models import Post
from api.serializers import PostSerializer, ThinPostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
#can use ^ mixins + GenericAPi to get rid of gef get,post etc

#class + mixins based
class PostList(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        self.serializer_class = ThinPostSerializer       #for thinner get json
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(self, request, *args, **kwargs)


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"




#class based
# class PostList(APIView):
#     def get(self,request, format=None):
#         posts = Post.objects.all()
#         context = {'request': request}
#         serializer = ThinPostSerializer(posts, many=True, context=context)
#         return Response(serializer.data)
#
#     def post(self,request, format=None):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PostDetail(APIView):
#
#     def get_object(self, slug):
#         try:
#             return Post.objects.get(slug=slug)
#
#         except Post.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, slug, format=None):
#         post = self.get_object(slug)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     def put(self, request, slug, format=None):
#         post = self.get_object(slug)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, slug, format=None):
#         post = self.get_object(slug)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# func based
# @api_view(["GET","POST"])
# def posts_list(request, format=None):
#     if request.method == "GET":
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         #   many stands for multiple posts in Post.objects.all()
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#             # if serializer is not valid  we need to rerurn .errors and bad request
#
#
# @api_view(["GET","PUT","DELETE"])
# def posts_detail(request,slug,format=None):
#     try:
#         post = Post.objects.get(slug=slug)
#
#     except Post.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == "GET":
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     elif request.method == "PUT":
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == "DELETE":
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)