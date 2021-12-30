from django.urls import path
from django.conf.urls import url, include
from django.views.generic.base import RedirectView

from .views import (
    UserDetailView,
    UserFollowView,
    activate_user_view
)

app_name = 'profiles'
urlpatterns = [
    url(r'^(?P<name>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'),  # /tweet/1/
    url(r'^(?P<name>[\w.@+-]+)/follow/$', UserFollowView.as_view(), name='follow'),
    url(r'^activate/(?P<code>[a-zA-Z0-9].*)/$', activate_user_view, name='activate_user_view'),
]
