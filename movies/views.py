from django.http import HttpResponse


def movies(request):
    return HttpResponse("Hello Noah")

def home(request):
    return HttpResponse("I am home")