from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ["date", "blog_post"]
        labels = {"user_name": "Your Name", "comment_content": "Your Comment"}