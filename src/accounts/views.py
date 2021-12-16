from django.shortcuts import render

def home(request):
    context = {
    }
    return render(request, "accounts/index.html", context)
