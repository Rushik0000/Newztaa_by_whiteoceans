from django.db import models
from django.contrib.auth import get_user_model

#from authsysproject import users

#from authsysproject.users.views import register


User = get_user_model()

# Create your models here.
class ProfileSetting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)
    Category = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class LikeNews(models.Model):
    username = models.CharField(max_length=100)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.username
