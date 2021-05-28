from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello world! <br>Welcome to the most boring blog on the web. <br>Made by me Curtis')