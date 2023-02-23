from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.posts, name="posts"),
    path("posts/<slug:slug>/", views.get_post, name="post")
]
