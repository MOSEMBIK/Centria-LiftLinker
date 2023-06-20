from django.shortcuts import render, redirect

# Import users models
from forum.models import Post, Comment
from .models import User

# Import usefull libraries
import hashlib

# Create your views here.
# Index view
def userindex(request):
    if request.session.get('username') :
        user = User.objects.get(username=request.session.get('username'))
        username = request.session.get('username')
        filtered =  {
            'favorites': [], 
            'opened': [], 
            'archives': [],
        }
        #filtered['favorites'] = Post.objects.filter(status=0, author=username).order_by('-date')
        filtered['opened'] = Post.objects.filter(status=0, author=username).order_by('-date')
        filtered['archives'] = Post.objects.filter(status=1, author=username).order_by('-date')
        
        return render(request, 'userindex.html', {'user': user, 'filtered': filtered, 'session': request.session, 'user_profil': True})
    else :
        return redirect('login')

# User view
def user(request, username):
    try :
        user = User.objects.get(username=username)
    except :
        user = {'username': 'User not found.', 'profil_bio': 'User not found.', 'score': 0, 'profile_pic': None}
        filtered =  {
            'favorites': [], 
            'opened': [], 
            'archives': [],
        }
        return render(request, 'userindex.html', {'user': user, 'filtered': filtered, 'session': request.session, 'user_profil': False})

    filtered =  {
        'favorites': [], 
        'opened': [], 
        'archives': [],
    }
    #filtered['favorites'] = Post.objects.filter(status=0, category=cat, subcategory=sub).order_by('-date')
    filtered['opened'] = Post.objects.filter(status=0, author=username).order_by('-date')
    filtered['archives'] = Post.objects.filter(status=1, author=username).order_by('-date')
    
    if username == request.session.get('username') :
        return redirect('userindex')
    else :
        return render(request, 'userindex.html', {'user': user, 'filtered': filtered, 'session': request.session, 'user_profil': False})

# User registration with sha256 password encryption
def register(request):
    if request.session.get('username') :
        return render(request, 'register.html', {'message': 'You aleready have an account.', 'isLogged': True})
    if request.method == 'POST' :
        username = request.POST['username']
        try:
            user = User.objects.get(username=username)
            return  render(request, 'register.html', {'message': 'Username aleready used', 'session': request.session})
        except:
            pass

        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            return render(request, 'register.html', {'message': 'Passwords do not match', 'session': request.session})
        # encode password
        encoded_password = password.encode('utf-8')
        hashed_password = hashlib.sha256(encoded_password).hexdigest()
        # create user
        user = User(username=username, password=hashed_password)
        # save user
        user.save()
        return render(request, 'register.html', {'message': 'User created successfully', 'session': request.session})
    else:
        return render(request, 'register.html', {'message': 'Welcome on registration page', 'session': request.session})
    
# User login with sha256 password encryption and session
def login(request):
    if request.session.get('username') :
        return render(request, 'login.html', {'message': 'You are aleready logged in.', 'isLogged': True})

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # encode password
        encoded_password = password.encode('utf-8')
        hashed_password = hashlib.sha256(encoded_password).hexdigest()
        # get user
        user = User.objects.get(username=username)
        # check password
        if user.password == hashed_password:
            # create session
            request.session['username'] = username
            return redirect('userindex')
        else:
            return render(request, 'login.html', {'message': 'Wrong password'})
    else:
        return render(request, 'login.html', {'message': 'Welcome on login page'})
    
# User logout
def logout(request):
    if request.session.get('username') :
        del request.session['username']
        return redirect('index')
    else:
        return redirect('index')
    
# Deleting account and session
def delete(request):
    if not request.session.get('username') :
        return render(request, 'delete.html', {'message': 'You need to be logged in.', 'isLogged': False})
    if request.method == 'POST':
        username = request.session['username']
        password = request.POST['password']
        # encode password
        encoded_password = password.encode('utf-8')
        hashed_password = hashlib.sha256(encoded_password).hexdigest()
        # get user
        user = User.objects.get(username=username)
        # check password
        if user.password == hashed_password:
            # delete user
            user = User.objects.get(username=username)
            user.delete()
            # delete session
            del request.session['username']
            return render(request, 'delete.html', {'message': 'User successfully deleted.'})
        else:
            return render(request, 'delete.html', {'message': 'Wrong password'})
    else:
        return render(request, 'delete.html', {'message': 'If you really want to delete your account, please enter your password.'})
    
