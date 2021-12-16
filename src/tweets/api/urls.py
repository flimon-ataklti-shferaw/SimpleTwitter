from django.urls import path

from django.views.generic.base import RedirectView

from .views import (
    TweetListAPIView
)

app_name='tweet-api'
urlpatterns = [
 path(r'', TweetListAPIView.as_view(), name='list'), # /api/tweet/
]
