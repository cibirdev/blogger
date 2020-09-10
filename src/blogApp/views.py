from django.shortcuts import render


def home(request):
    return render(request, "template\index.html", {"title": "home"})
