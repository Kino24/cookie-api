from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Post
from django.views.decorators.csrf import csrf_exempt
import json

def get_users(request):
    try:
        users = list(User.objects.values('id', 'username','email','created_at'))
        return JsonResponse(users, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
@csrf_exempt
def create_user(request):
    try:
        data = json.loads(request.body)
        user = User.objects.create(username=data['username'], email=data['email'])
        return JsonResponse({'id': user.id, 'message': 'User created successfully'}, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def get_posts(request):
    try:
        posts = list(Post.objects.values('id','content', 'created_at'))
        return JsonResponse(posts, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def create_post(request):
    try:
        data = json.loads(request.body)
        author = User.objects.get(id=data['author_id'])
        post = Post.objects.create(content=data['content'], author=author)
        return JsonResponse({'id': post.id, 'message': 'Post created successfully'}, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)