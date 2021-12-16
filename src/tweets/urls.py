from django.urls import path


from .views import list, detail, create, delete, update

urlpatterns = [
    path(r'', list, name='list'),
    path(r'detail/', detail, name='detail'),
    path(r'create/', create, name='create'),
    path(r'delete/', delete, name='delete'),
    path(r'update/', update, name='update'),
]