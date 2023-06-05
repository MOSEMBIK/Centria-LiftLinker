from django.shortcuts import render

# Import users models
from .models import User
# Import forum models
from forum.models import Post, Comment

# Create your views here.
def forumindex(request):
    return render(request, 'forum/forumindex.html')