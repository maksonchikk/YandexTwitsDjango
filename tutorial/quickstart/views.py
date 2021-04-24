#import self as self
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, serializers
from rest_framework.viewsets import GenericViewSet
from tutorial.quickstart.permission import IsAutorOrReadOnly
#from tutorial.quickstart.permission import IsAunthificated
from tutorial.quickstart.serializers import UserSerializer,TweetSerializer, FollowSerializer,UserFollowsSerializer, UserFollowerSerializer
from tutorial.quickstart.models import Tweet
from tutorial.quickstart.models import Follower

class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    lookup_field = 'username'

class TweetViewSet(viewsets.ModelViewSet):

    queryset = Tweet.objects.all().order_by()
    serializer_class = TweetSerializer
    permission_classes = [IsAutorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserTweetViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Tweet.objects
    serializer_class = TweetSerializer

    def get_queryset(self):
        return self.queryset.filter(author__username=self.kwargs['parent_lookup_username'])


class UserTweetFollowViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Follower.objects
    serializer_class = FollowSerializer
    permission_classes = [IsAutorOrReadOnly]

    def preform_create(self, serializer):
        serializer.save(follower=self.request.user,
                        follows=User.objects.get(username=self.kwargs[self.lookup_field]))

    def get_object(self):
        return self.queryset.filter(follower=self.request.user,
                                    follows__username=self.kwargs[self.lookup_field])

    # def __str__(self):
    #     return f'[{self.follower}]->{self.follows}'


class FeedViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Tweet.objects
    serializer_class = TweetSerializer
    permission_classes = [IsAutorOrReadOnly]

    def qwery_set(self):
        # return self.queryset.filter(author__ufollower__follows=self.request.user)
        return Tweet.objects.filter(author__follower__follows=self.request.user)

class UserFollowsViwset(viewsets.ReadOnlyModelViewSet):

    queryset = Follower.objects
    serializer_class = UserFollowsSerializer

    def get_qweriset(self):
        username = self.kwargs['parent_lookup_username']
        return self.queryset.filter(follower__username=username)

class UserFollowerViwset(viewsets.ReadOnlyModelViewSet):

    queryset = Follower.objects
    serializer_class = UserFollowerSerializer

    def get_qweriset(self):
        username = self.kwargs['parent_lookup_username']
        return self.queryset.filter(follows__username=username)

