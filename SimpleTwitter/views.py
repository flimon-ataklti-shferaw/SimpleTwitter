from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import render
from django.views import View

User = get_user_model()


class SearchView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")
        qs = None
        if query:
            qs = User.objects.filter(
                Q(name__icontains=query)
            )
        context = {"users": qs}
        return render(request, "search.html", context)
