from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.views.decorators.vary import vary_on_headers


# adds on vary values for response headers for p1
@vary_on_headers("Accept-Language, User-Agent")
def p1(request):
    return render(request, "p1.html")


# disables caching on p2
@cache_control(private=True)
def p2(request):
    return render(request, "p2.html")
