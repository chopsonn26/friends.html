from django.http import HttpResponse
from django.template.loader import render_to_string


def home(request):
    html = render_to_string("home.html")
    return HttpResponse(content=html)

def season1(request):
    html1 = render_to_string("season1.html")
    return HttpResponse(content=html1)

def season2(request):
    html2 = render_to_string("season2.html")
    return HttpResponse(content=html2)

def season3(request):
    html3 = render_to_string("season3.html")
    return HttpResponse(content=html3)

def season4(request):
    html4 = render_to_string("season4.html")
    return HttpResponse(content=html4)

def season5(request):
    html5 = render_to_string("season5.html")
    return HttpResponse(content=html5)

def tobecontinued(request):
    html5 = render_to_string("tobecontinued.html")
    return HttpResponse(content=html5)