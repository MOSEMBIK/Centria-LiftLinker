from django.shortcuts import render, redirect

# Import users models
from .models import Post, Comment

# Create your views here.
def forumindex(request):
    posts = Post.objects.filter(status=0).order_by('-date')
    filtered =  {
        'nutrition': {
            'questions': [], 
            'recepies': [], 
            'suplements': [], 
        },
        
        'weight': {
            'questions': [], 
            'freeweights': [], 
            'machines': [], 
        },

        'calisthenics': {
            'questions': [], 
            'equipments': [], 
            'routines': [], 
        },

        'crossfit': {
            'questions': [], 
            'circuits': [], 
        },

        'other': {
            'questions': [],
            'other': [],
        },
    }
    for cat in filtered.keys():
        for sub in filtered[cat].keys() :
            filtered[cat][sub] = Post.objects.filter(status=0, category=cat, subcategory=sub).order_by('-date')
    return render(request, 'forumindex.html', {'posts': posts, 'filtered': filtered, 'session': request.session})

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

            parentID = request.POST['parentID']
            parent = Post.objects.get(postID=parentID)

            author = request.session.get('username')
            content = request.POST['content']

            if parent.status == 1 :
                return redirect('index')
                
            comment = Comment(parentID=parentID, author=author, content=content)
            comment.save()
        except :
            return redirect('index')
    try :
        post = Post.objects.get(postID=postID)
        comments = Comment.objects.filter(parentID=postID)
    except :
        post = {'title': 'Error 404', 'content': 'Post not found', 'author': 'System'}
        comments = {}
    return render(request, 'post_page.html', {'post': post, 'comments': comments, 'session': request.session})

def archive(request):
    if request.method == 'POST' and request.session.get('username'):
        post = Post.objects.get(postID=request.POST['postID'])
        if post.author == request.session.get('username'):
            post.status = 1
            post.save()
            return redirect('forumindex')
    return redirect('index')
            
def user_posts(request, username):
   return render(request, 'post_page.html', {'filtered': filtered, 'session': request.session})