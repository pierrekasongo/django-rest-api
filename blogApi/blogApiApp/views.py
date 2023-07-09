from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def index(request):
    return Response({"Success": "The setup was successful"})

@api_view(['GET'])
def get_all_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def create_post(request):
    data = request.data
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success":"The post was successfully created"}, status=201)
    
    else:
        return Response(serializer.errors, status=400)
    
@api_view(['DELETE'])
def delete_post(request):
    post_id = request.data.get('post_id')
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response({"Success":"The post was successfully deleted successfully"}, status=200)
    except Post.DoesNotExist:
        return Response({"Success":"The post does not exist"}, status=404)


@api_view(['GET'])
def get_post(request):
    post_id = request.data.get('post_id')
    try:
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post) # only one item returned
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response({"Success":"The post does not exist"}, status=404)
    
@api_view(['PUT'])
def update_post(request):
    post_id = request.data.get('post_id')
    title = request.data.get('title')
    content = request.data.get('content')
    try:
        post = Post.objects.get(id=post_id)
        if title:
            post.title = title
        if content:
            post.content = content
        post.save()
        return Response({"Success":"The post was successfully updated"}, status=200)
    except Post.DoesNotExist:
        return Response({"Success":"The post does not exist"}, status=404)