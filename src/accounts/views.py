from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, FormView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import View

from .forms import RegisterForm, LoginForm
from .models import User, Profile



class LoginView(FormView):
    form_class = LoginForm
    success_url = "/tweet/"
    template_name = "accounts/login.html"

    def form_valid(self, form):
        request = self.request
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "BUG HINT: only users with admin permission can log in, please use email = 'dubai@gmail.com', password = 'dubai' .....BUG WILL BE FIXED SOON ")
        return super(LoginView, self).form_valid(form)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = "/"


class UserDetailView(DetailView):
    template_name = 'accounts/user_detail.html'
    queryset = User.objects.all()

    def get_object(self):
        return get_object_or_404(
            User,
            email__iexact=self.kwargs.get("email")
        )

    def get_context_data(self, *args, **kwargs):
        context = super(UserDetailView, self).get_context_data(*args, **kwargs)
        following = Profile.objects.is_following(self.request.user, self.get_object())
        context['following'] = following
        context['recommended'] = Profile.objects.recommended(self.request.user)
        return context


class UserFollowView(View):
    def get(self, request, email, *args, **kwargs):
        toggle_user = get_object_or_404(User, email__iexact=email)
        if request.user.is_authenticated:
            is_following = Profile.objects.toggle_follow(request.user, toggle_user)
        return redirect("profiles:detail", email=email)
