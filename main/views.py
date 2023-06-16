from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'session': request.session})

def news(request):
    return render(request, 'news.html', {'session': request.session})

def places(request):
    return render(request, 'places.html', {'session': request.session})

def about(request):
    return render(request, 'about.html', {'session': request.session})

def aboutcontact(request):
    return render(request, 'about_contact.html', {'session': request.session})