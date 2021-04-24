from django.contrib import admin
from django.urls import include, path
from rest_framework_extensions.routers import ExtendedDefaultRouter
from tutorial.quickstart import views
from tutorial.quickstart.views import UserTweetViewSet, UserFollowsViwset, UserFollowerViwset
from tutorial.quickstart.router import SwitchDetailRouter
from tutorial.quickstart.views import UserTweetFollowViewSet

switch_router = SwitchDetailRouter()
router = ExtendedDefaultRouter()
user_route = router.register(r'users', views.UserViewSet).register('tweets', UserTweetViewSet, 'user-tweets', ['username'])
user_route.register = (r'follows', views.UserFollowsViwset, 'user-follow', ['username'])
user_route.register = (r'follower', views.UserFollowerViwset, 'user-follower', ['username'])
router.register(r'tweets', views.TweetViewSet)
router.register(r'feed', views.FeedViewSet)
# router.register(r'fallows', views.UserFollowsViwset)
switch_router.register(r'follower', views.UserTweetFollowViewSet)

urlpatterns = [
        path('v1/', include(switch_router.urls)),
        path('v1/', include(router.urls)),
        path('admin/', admin.site.urls),
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]