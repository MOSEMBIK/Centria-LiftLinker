from django.shortcuts import render, redirect
from django.db.models import Q

# Import users models
from users.models import User
from forum.models import Post

# Create your views here.
def index(request):
    return render(request, 'index.html', {'session': request.session})

def about(request):
    if request.method == 'POST':
        return redirect('index')
    return render(request, 'about.html', {'session': request.session})

# Serching user
def search(request):
    if request.method == 'POST':
        search_input = request.POST['search_input']

        users = User.objects.filter(Q(username__icontains=search_input))
        posts = Post.objects.filter(Q(title__icontains=search_input))
        posts2 = Post.objects.filter(Q(author__icontains=search_input))

        posts = posts.union(posts2)

        return render(request, 'search.html', {'users': users, 'posts': posts, 'session': request.session, 'user_profil': False})
    else:
        return redirect('index')
