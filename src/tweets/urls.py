from django.urls import path
from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import (
    TweetCreateView,
    TweetDeleteView,
    TweetDetailView,
    TweetListView,
    TweetUpdateView
)

app_name = 'tweet'
urlpatterns = [
    path(r'', RedirectView.as_view(url="/")),
    path(r'search/', TweetListView.as_view(), name='list'),  # /tweet/
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),  # /tweet/1/
    path(r'create/', TweetCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),  # /tweet/1/update/
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),  # /tweet/1/delete/
]
