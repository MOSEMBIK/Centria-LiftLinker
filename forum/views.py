from django.shortcuts import render, redirect

# Import users models
from .models import Post, Comment

# Create your views here.
def forumindex(request):
    posts = Post.objects.filter(status=0)
    return render(request, 'forumindex.html', {'posts': posts, 'session': request.session})


def newpost(request):
    if request.method == 'POST' and request.session.get('username'):
        try :
            title = Post.objects.filter(title=request.POST['title'])
            content = Post.objects.filter(content=request.POST['content'])
            for i in title:
                if i in content :
                    return redirect('index')
        except :
            pass

        author = request.session.get('username')
        title = request.POST['title']
        content = request.POST['content']
        category = request.POST['category']
        subcategory = request.POST['subcategory']
        
        post = Post(author=author, title=title, content=content, category=category, subcategory=subcategory)
        post.save()
        return redirect('forumindex')
    else:
        return render(request, 'new_post.html', {'session': request.session})

def post(request, postID):
    if request.method == 'POST' and request.session.get('username'):
        try :
            samepcomments = Comment.objects.filter(parentID=request.POST['parentID'])
            samecontent = Comment.objects.filter(content=request.POST['content'])
            for i in samepcomments:
                if i in samecontent :
                    return redirect('index')
        except :
            pass

        parentID = request.POST['parentID']
        author = request.session.get('username')
        content = request.POST['content']
        
        comment = Comment(parentID=parentID, author=author, content=content)
        comment.save()

    post = Post.objects.get(postID=postID)
    comments = Comment.objects.filter(parentID=postID)
    return render(request, 'post_page.html', {'post': post, 'comments': comments, 'session': request.session})