from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404
from django.template.loader import render_to_string

# Create your views here.
blogs = {
    "my first post": "hello this is my first post",
    "my second post": "hello this is my second post",
    "my third post": "hello this is my third post"
}

def index(request):
    return render(request, "blog/index.html")


def posts(request):
    blog_list = list(blogs.keys())
    return render(request, "blog/posts.html", { "blogs": blog_list })


def get_post(request, slug):
    blog_ids = list(blogs.keys())
    if slug in blog_ids:
        post_text = blogs[slug]
        return render(request, "blog/post.html", { "post_text": post_text })
    else:
        error_page = render_to_string("404.html")
        return HttpResponseNotFound(error_page)