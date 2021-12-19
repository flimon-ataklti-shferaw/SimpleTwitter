from django.contrib.auth import login, get_user_model, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import FormView

from .forms import UserCreationForm, UserLoginForm
from .models import UserProfile

User = get_user_model()


def register(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/login')
    return render(request, "accounts/registration/register.html", {"form": form})


def login_view(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        email_ = form.cleaned_data.get('email')
        user_obj = User.objects.get(email__iexact=email_)
        login(request, user_obj)
        return HttpResponseRedirect('/')

    return render(request, "accounts/registration/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')

class UserDetailView(DetailView):
    template_name = 'accounts/user_detail.html'
    queryset = User.objects.all()

    def get_object(self):
        return get_object_or_404(
            User,
            name__iexact=self.kwargs.get("name")
        )

    def get_context_data(self, *args, **kwargs):
        context = super(UserDetailView, self).get_context_data(*args, **kwargs)
        following = UserProfile.objects.is_following(self.request.user, self.get_object())
        context['following'] = following
        context['recommended'] = UserProfile.objects.recommended(self.request.user)
        return context


class UserFollowView(View):
    def get(self, request, name, *args, **kwargs):
        toggle_user = get_object_or_404(User, name__iexact=name)
        if request.user.is_authenticated:
            is_following = UserProfile.objects.toggle_follow(request.user, toggle_user)
        return redirect("profiles:detail", name=name)
