from django.urls import path

from django.views.generic.base import RedirectView

from .views import (
    TweetCreateAPIView,
    TweetListAPIView,
)

app_name = 'tweet-api'
urlpatterns = [
    path(r'', TweetListAPIView.as_view(), name='list'),  # /api/tweet/
    path(r'create/', TweetCreateAPIView.as_view(), name='create'),  # /tweet/create/
]
