from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("posts/", views.PostsView.as_view(), name="posts"),
    path("posts/<slug:slug>/", views.GetPost.as_view(), name="post"),
    path("read-later/", views.ReadLaterView.as_view(), name="read_later")
]
