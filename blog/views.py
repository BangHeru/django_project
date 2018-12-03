from django.shortcuts import render


def home(req):
    return render(req, 'blog/home.html')

def about(req):
    return render(req, 'blog/about.html')