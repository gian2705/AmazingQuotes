from urllib.parse import unquote

from django.contrib.auth.models import User
from django.db import models
from gdstorage.storage import GoogleDriveStorage
gd_storage = GoogleDriveStorage()

# Create your models here.


class Post(models.Model):
    post_category = {
        ('RELATIONSHIP', 'Relationship'),
        ('LIFE COACHING', 'Life Coaching'),
        ('LEADERSHIP', 'Leadership'),
        ('ENTREPRENEURSHIP', 'Entrepreneurship')
    }
    featured = {
        ('YES', "Yes"),
        ('NO', "No")
    }
    user_post = models.ForeignKey(User, on_delete=models.CASCADE, auto_created=True, default=1)
    title = models.CharField(max_length=128)
    category = models.CharField(max_length=64, verbose_name="Post Category", choices=post_category, default='LIFE')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='blog_posts', storage=gd_storage, )
    feature = models.CharField(max_length=5, default='NO', choices=featured, verbose_name='Featured?')
    image_url = models.URLField(auto_created=True, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_image_url(self):
        image_id = unquote(self.image.url).split("/")[-2]
        print(image_id)
        return image_id

    def save(self, *args, **kwargs):
        self.image_url = self.get_image_url()
        super().save(*args, **kwargs)