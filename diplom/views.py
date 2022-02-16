from django.shortcuts import render


def home(request, pk=None):

    name = request.user
    return render(request, "home.html", {"name": name})


def about(request):
    return render(request, "about.html")
