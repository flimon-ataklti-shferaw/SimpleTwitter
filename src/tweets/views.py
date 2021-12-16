from django.shortcuts import render

def list(request):
    context = {
    }
    return render(request, "tweets/list.html", context)

def detail(request):
    context = {
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