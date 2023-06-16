from django.shortcuts import render

# Import users models
from .models import Post, Comment

# Create your views here.
def forumindex(request):
    return render(request, 'forumindex.html', {'session': request.session})