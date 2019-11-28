from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200);
    description = models.CharField(max_length=500) 
    created = models.DateTimeField(auto_now_add=True)

  

    def get_latest_date(self):
        if self.comment_set.count() > 0:
            return self.comment_set.latest('created_date').created_date
        return self.created


    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey('comment', on_delete=models.CASCADE, null=True, related_name="replies")
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    