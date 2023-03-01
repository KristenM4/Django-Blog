from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=75)

    def __str__(self):
        return f"Full name: {self.first_name} {self.last_name}, {self.email_address}"
