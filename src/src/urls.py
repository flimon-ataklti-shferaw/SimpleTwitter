from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from django.contrib import admin
from django.urls import path, include

from accounts.views import register, login_view

from hashtags.api.views import TagTweetAPIView
from hashtags.views import HashTagView

from tweets.api.views import SearchTweetAPIView
from tweets.views import TweetListView

from .views import SearchView

urlpatterns = [
    path('admin/', admin.site.urls),

    path(r'', TweetListView.as_view(), name='home'),
    path(r'tweet/', include('tweets.urls', namespace='tweet')),
    path(r'api/tweet/', include('tweets.api.urls', namespace='tweet-api')),
    url(r'^api/tags/(?P<hashtag>.*)/$', TagTweetAPIView.as_view(), name='tag-tweet-api'),

    path(r'search/', SearchView.as_view(), name='search'),
    url(r'^tags/(?P<hashtag>.*)/$', HashTagView.as_view(), name='hashtag'),
    path(r'api/search/', SearchTweetAPIView.as_view(), name='search-api'),

    path(r'login/', login_view, name='login'),
    path(r'register/', register, name='register'),
    path(r'', include('django.contrib.auth.urls')),

    path(r'api/', include('accounts.api.urls', namespace='profiles-api')),
    path(r'', include('accounts.urls', namespace='profiles')),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Simple Twitter Admin"
admin.site.site_title = "Simple Twitter Admin Portal"
admin.site.index_title = "Welcome to Simple Twitter Admin Portal"
