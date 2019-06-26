from django.shortcuts import render


def index(request):
    """ A view to display the index page """
    return render(request, "index.html")
