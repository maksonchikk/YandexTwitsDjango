from django.contrib.auth.models import User
from rest_framework import serializers
from tutorial.quickstart.models import Tweet
from tutorial.quickstart.models import Follower

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email',"last_name","first_name"]
        extra_kwargs = {'url': {'lookup_field': 'username'}}


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = ['url','id','text', 'photo','created','author']

class FollowSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Follower
        fields = []

class UserFollowsSerializer(serializers.HyperlinkedModelSerializer):
    follows = UserSerializer

    class Meta:
        model = Follower
        fields = ['follows', 'followed']

class UserFollowerSerializer(serializers.HyperlinkedModelSerializer):
    follower = UserSerializer

    class Meta:
        model = Follower
        fields = ['follower', 'followed']