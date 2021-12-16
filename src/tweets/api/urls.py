from django.urls import path
from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import (
    RetweetAPIView,
    TweetCreateAPIView,
    TweetListAPIView,
)

app_name = 'tweet-api'
urlpatterns = [
    path(r'', TweetListAPIView.as_view(), name='list'),  # /api/tweet/
    path(r'create/', TweetCreateAPIView.as_view(), name='create'),  # /tweet/create/
    url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view(), name='retweet')  # /api/tweet/id/tweet/
]
