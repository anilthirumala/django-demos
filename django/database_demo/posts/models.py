from django.db import models

# Create your models here.
class Posts(models.Model):
    post_title = models.CharField(max_length=50)
    post_content=models.TextField()
    published_date=models.DateTimeField(auto_now=True)
