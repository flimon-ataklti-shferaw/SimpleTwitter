from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from django.contrib import admin
from django.urls import path, include

from hashtags.views import HashTagView
from tweets.views import TweetListView

urlpatterns = [
    path('admin/', admin.site.urls),

    path(r'', TweetListView.as_view(), name='home'),
    path(r'tweet/', include('tweets.urls', namespace='tweet')),
    path(r'api/tweet/', include('tweets.api.urls', namespace='tweet-api')),
    url(r'^tags/(?P<hashtag>.*)/$', HashTagView.as_view(), name='hashtag'),

    path(r'', include('accounts.urls', namespace='profiles')),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Simple Twitter Admin"
admin.site.site_title = "Simple Twitter Admin Portal"
admin.site.index_title = "Welcome to Simple Twitter Admin Portal"
