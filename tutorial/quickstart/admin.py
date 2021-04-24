from django.contrib import admin
from tutorial.quickstart.models import Tweet
from tutorial.quickstart.models import Follower
# Register your models here.
admin.site.register(Tweet)
admin.site.register(Follower)