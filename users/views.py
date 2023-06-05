from django.shortcuts import render

# Import users models
from .models import User
# Import forum models
from forum.models import Post, Comment

# Import usefull libraries
import hashlib

# Create your views here.
# Index view
def appindex(request):
    return render(request, 'appindex.html', {'session': request.session})

# User view
def user(request, username):
    user = User.objects.get(username=username)
    return render(request, 'user.html', {'user': user, 'session': request.session})

def search_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        try:
            user = User.objects.get(username=username)
            return render(request, 'user.html', {'user': user, 'session': request.session})
        except:
            return render(request, 'user_search.html', {'message': 'User not found', 'session': request.session})
    else:
        return render(request, 'user_search.html', {'message': 'Welcome on user search page', 'session': request.session})

# User registration with sha256 password encryption
def register(request):
    if request.session.get('username') :
        return render(request, 'register.html', {'message': 'You aleready have an account.', 'isLogged': True})
    if request.method == 'POST':
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
            return render(request, 'login.html', {'message': 'User logged in successfully'})
        else:
            return render(request, 'login.html', {'message': 'Wrong password'})
    else:
        return render(request, 'login.html', {'message': 'Welcome on login page'})
    
# User logout
def logout(request):
    if request.session.get('username') :
        del request.session['username']
        return render(request, 'logout.html', {'message': 'User logged out successfully'})
    else:
        return render(request, 'logout.html', {'message': 'You are not logged in.'})
    
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
    
