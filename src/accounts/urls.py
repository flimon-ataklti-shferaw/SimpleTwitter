from django.urls import path
from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import (
    UserDetailView,
    UserFollowView
)

app_name = 'accounts'
urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'),  # /tweet/1/
    url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view(), name='follow'),
]
