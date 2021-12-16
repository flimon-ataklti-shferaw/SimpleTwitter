from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from tweets.views import TweetListView

urlpatterns = [
    path(r'', TweetListView.as_view(), name='home'),
    path(r'tweet/', include('tweets.urls', namespace='tweet')),
    path(r'api/tweet/', include('tweets.api.urls', namespace='tweet-api')),

    path(r'', include('accounts.urls', namespace='profiles')),

    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Simple Twitter Admin"
admin.site.site_title = "Simple Twitter Admin Portal"
admin.site.index_title = "Welcome to Simple Twitter Admin Portal"
