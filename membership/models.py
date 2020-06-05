from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import datetime

# Create your models here.

MEMBERSHIP_CHOICES = (
    ('Silver', 'silver'),
    ('Gold', 'gold'),
    ('Free', 'free')
)

MOVIE_CATEGORY = (
    ('Hollywood', 'holly'),
    ('Bollywood', 'bolly'),
    ('Dual audio', 'dual'),
    ('Uncategorized', 'uncategorized')
)

class Membership(models.Model):
    slug = models.SlugField()
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, max_length=50, default='Free')
    desc = models.TextField(null=True)
    price = models.IntegerField(default=15)

    def __str__(self):
        return self.membership_type

class UserMembership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True, default=1)
    date_added = models.DateTimeField(default=datetime.now, null=True)
    expired = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.user.username


class Movie(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    video_url = models.CharField(max_length=200, null=True)
    thumbnail = models.ImageField(null=True)
    imdb = models.FloatField(default=5)
    category = models.CharField(choices=MOVIE_CATEGORY, max_length=20, default='Uncategorized')
    allowed_memberships = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

