from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404
from django.template.loader import render_to_string
import datetime as dt
from .models import Post, Author, Tag, Comment
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView


def index(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    latest_post = latest_posts[0]
    new_tag = Tag.objects.get(caption="New")
    if new_tag not in latest_post.tags.all():
        latest_post.tags.add(new_tag)
    return render(request, "blog/index.html", {"latest_posts": latest_posts})


def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request, "blog/posts.html", {"all_posts": all_posts})


class GetPost(DetailView):
    model = Post
    template_name = "blog/post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["comments"] = Comment.objects.filter(post_id=self.object.id)
        context["tags"] = self.object.tags.all()
        loaded_post = self.object
        return context
    
    def post(self, request, slug):
        specific_post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)
        comments = Comment.objects.filter(post_id=specific_post.id)
        post_tags = specific_post.tags.all()

        if form.is_valid():
            new_data = form.cleaned_data
            name = new_data["user_name"]
            content = new_data["comment_content"]
            post_id = specific_post.id
            new_comment = Comment(user_name=name, comment_content=content, post_id=post_id)
            new_comment.save()
            form = CommentForm()
            return render(request, "blog/post.html", {"post": specific_post, "form": form, "comments": comments, "tags": post_tags})
        else:
            return render(request, "blog/post.html", {"post": specific_post, "form": form, "comments": comments, "tags": post_tags})
