from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
import datetime as dt
from .models import Post, Author, Tag, Comment
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView


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
        context["read_later_alert"] = False
        return context

    def post(self, request, slug):
        specific_post = get_object_or_404(Post, slug=slug)
        comments = specific_post.comment_set.all().order_by("-date")
        post_tags = specific_post.tags.all()

        if "submit_comment_button" in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                new_data = form.cleaned_data
                name = new_data["user_name"]
                content = new_data["comment_content"]
                new_comment = Comment(
                    user_name=name, comment_content=content, blog_post=specific_post)
                new_comment.save()
                return HttpResponseRedirect(reverse("post", args=[slug]))
            else:
                return render(request, "blog/post.html", {"post": specific_post, "form": form, "comments": comments, "tags": post_tags, "read_later_alert": False})
        elif "read_later_button" in request.POST:
            form = CommentForm()
            post_id = specific_post.id
            if "read_later" not in request.session:
                request.session["read_later"] = list([post_id])
            elif post_id in request.session["read_later"]:
                return render(request, "blog/post.html", {"post": specific_post, "form": form, "comments": comments, "tags": post_tags, "read_later_alert": True})
            else:
                read_later_list = request.session["read_later"]
                read_later_list.append(post_id)
                request.session["read_later"] = read_later_list
            return HttpResponseRedirect(reverse("post", args=[slug]))


class ReadLaterView(TemplateView):
    template_name = "blog/read_later.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        if "read_later" not in request.session:
            post_list = []
        else:
            read_later_list = request.session.get("read_later")
            post_list = []
            for item in read_later_list:
                post = get_object_or_404(Post, pk=item)
                if post not in post_list:
                    post_list.append(post)
        context["read_later_posts"] = post_list
        context["empty_list"] = post_list == []
        return context

    
