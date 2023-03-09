from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
import datetime as dt
from .models import Post, Author, Tag, Comment
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView


class IndexView(ListView):
    model = Post
    context_object_name = "latest_posts"
    template_name = "blog/index.html"

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-date')[:3]
        return queryset


class PostsView(ListView):
    model = Post
    context_object_name = "all_posts"
    template_name = "blog/posts.html"

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-date')
        return queryset


class GetPost(DetailView):
    model = Post
    template_name = "blog/post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["comments"] = self.object.comment_set.all().order_by("-date")
        context["tags"] = self.object.tags.all()
        return context

    def post(self, request, slug):
        specific_post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)
        comments = specific_post.comment_set.all().order_by("-date")
        post_tags = specific_post.tags.all()

        if "submit_comment_button" in request.POST:
            if form.is_valid():
                new_data = form.cleaned_data
                name = new_data["user_name"]
                content = new_data["comment_content"]
                new_comment = Comment(
                    user_name=name, comment_content=content, blog_post=specific_post)
                new_comment.save()
                return HttpResponseRedirect(reverse("post", args=[slug]))
            else:
                return render(request, "blog/post.html", {"post": specific_post, "form": form, "comments": comments, "tags": post_tags})
        elif "read_later_button" in request.POST:
            print("added to read later list")
            return HttpResponseRedirect(reverse("post", args=[slug]))
