from django.db import models
from django import forms
from django.contrib.auth.models import User
from sorl.thumbnail.fields import ImageWithThumbnailsField

# Create your models here.

SEX_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('U', 'Bit of Both'),
    ('A', 'Yes Please'),
    ('B', 'On Tuesdays'),
    ('C', 'Captain Malcolm Reynolds'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)

    sex = models.CharField(max_length=1, choices=SEX_CHOICES, null=True,
        blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    location = models.CharField(max_length=200, null=True, blank=True)
    about_me = models.TextField(null=True, blank=True)

    def display_name(self):
        if self.user.get_full_name() != "":
            return self.user.get_full_name()
        else:
            return self.user.username

    def __unicode__(self):
        return u"Profile for %s" % self.user

class ProfilePicture(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    original_image = ImageWithThumbnailsField(upload_to="uploads/profile_pictures/", thumbnail={'size': (50, 50), 'options': ('crop',)})

    def __unicode__(self):
        return u"Profile Picture for %s" % self.user.username
