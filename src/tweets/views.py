from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Tweet


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()


class TweetListView(ListView):
    template_name = "tweets/list.html"
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context


def tweet_detail_view(request, pk=None):  # pk == id
    obj = get_object_or_404(Tweet, pk=pk)
    print(obj)
    context = {
        "object": obj
    }
    return render(request, "tweets/detail.html", context)


def create(request):
    context = {
    }
    return render(request, "tweets/create.html", context)

def delete(request):
    context = {
    }
    return render(request, "tweets/delete.html", context)

def update(request):
    context = {
    }
    return render(request, "tweets/update.html", context)
