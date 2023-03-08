from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    model = Comment
    fields = "__all__"
    exclude = ["date", "post_id"]
    labels = {"user_name": "Your Name", "comment_content": "Your Commment"}