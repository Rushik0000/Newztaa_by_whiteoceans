from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q

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



class ProfileManager(models.Manager):

    def get_all_profiles_to_invite(self, sender):
        profiles = Profile.objects.all().exclude(user = sender)
        profile = Profile.objects.get(user= sender)
        qs = Relationship.objects.filter(Q(sender = profile) | Q(receiver = profile))
        print(qs)

        accepted = []
        for rel in qs:
            if rel.status == 'accepted':
                accepted.append(rel.receiver)
                accepted.append(rel.sender)
        print('This is on the list:',accepted)

        available = [profile for profile in profiles if profile not in accepted]
        print('This is not on the list:',available)
        return available

    def get_all_profiles(self, me):
        profiles = Profile.objects.all().exclude(user = me)
        return profiles


class Profile(models.Model):
    user             = models.OneToOneField(User,on_delete = models.CASCADE)
    friends          = models.ManyToManyField(User, related_name='friends', blank=True)
    updated          = models.DateTimeField(auto_now=True)
    created          = models.DateTimeField(auto_now_add= True)

    objects = ProfileManager()

    def get_friends(self):
        return self.friends.all()

    def get_friends_no(self):
        return self.friends.all().count()

    def __str__(self):
        return str(self.user)

STATUS_CHOICES  = (('send','send'),
                    ('accepted','accepted'),
                    )

class RelationshipManager(models.Manager):
    def invitations_received(self, receiver):
        qs      = Relationship.objects.filter(receiver=receiver , status ='send') 
        return qs

    

class Relationship(models.Model):
    sender          = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver        = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status          = models.CharField(max_length=8 , choices=STATUS_CHOICES)
    updated         = models.DateTimeField(auto_now=True)
    created          = models.DateTimeField(auto_now_add= True)
    objects = RelationshipManager()

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"


