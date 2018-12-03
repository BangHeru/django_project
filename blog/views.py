from django.shortcuts import render

posts = [
    {
            'author': 'CoreyMS',
            'title': 'Blog Post 1',
            'content': 'First post content',
            'date_posted': 'August 27, 2018'
    },
    {
            'author': 'Jane Doe',
            'title': 'Blog Post 2',
            'content': 'Second post content',
            'date_posted': 'August 28, 2018'
    }
]
def home(req):
    context = {
        'posts': posts
    }
    return render(req, 'blog/home.html', context)

def about(req):
    return render(req, 'blog/about.html')