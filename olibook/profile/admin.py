from django.contrib import admin

from profile.models import *

admin.site.register(UserProfile)
admin.site.register(ProfilePicture)
