from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
        