
# I have created this website-abhaysinghpython
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def removepunc(request):
    print(request.GET.get('text','default'))
    return HttpResponse("remove punc")


def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("newline remove first")


def spaceremove(request):
    return HttpResponse("space remover back")

def charcount(request):
    return HttpResponse("charcount ")