from django.urls import path
from django.conf.urls import url

from .views import TweetListView, TweetDetailView, create, delete, update

urlpatterns = [
    path(r'', TweetListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),  # /tweet/1/
    path(r'create/', create, name='create'),
    path(r'delete/', delete, name='delete'),
    path(r'update/', update, name='update'),
]