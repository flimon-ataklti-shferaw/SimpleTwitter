from django.urls import path
from django.conf.urls import url, include
from django.views.generic.base import RedirectView

from .views import (
    UserDetailView,
    UserFollowView,
    LoginView,
    RegisterView
)

app_name = 'profiles'
urlpatterns = [
    url(r'^(?P<email>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'),
    url(r'^(?P<email>[\w.@+-]+)/follow/$', UserFollowView.as_view(), name='follow'),
    path(r'login/', LoginView.as_view, name='login'),
    path(r'register/', RegisterView.as_view, name='register'),
]
