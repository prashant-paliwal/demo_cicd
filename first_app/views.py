from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the index page of CICD Project!!")