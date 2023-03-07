from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=75)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email_address}"


class Tag(models.Model):
    caption = models.CharField(max_length=75)

    def __str__(self):
        return f"{self.caption}"
    

class Post(models.Model):
    title = models.CharField(max_length=140)
    excerpt = models.CharField(max_length=300)
    image_name = models.CharField(max_length=140)
    date = models.DateField()
    slug = models.CharField(max_length=200, default="", unique=True, db_index=True)
    content = models.TextField()
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"{self.title} - {self.author}, {self.date}: {self.excerpt}"
    

class Comment(models.Model):
    user_name = models.CharField(max_length=30)
    comment = models.TextField(max_length=200)
    date = models.DateField(auto_now=True)
    
