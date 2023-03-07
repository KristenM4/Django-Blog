from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    model = Comment
    fields = "__all__"
    exclude = ["date"]
    labels = {"user_name": "Your Name", "comment_content": "Your Commment"}