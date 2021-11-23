from django.shortcuts import render

# Create your views here.


def index(request, name):
    """
    This function returns an HTTP response of plaintext "Hello world!"
    """
    return render(request, "hello/index.html", {"name": name.capitalize()})
