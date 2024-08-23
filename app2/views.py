from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def titulo(request):
    return HttpResponse("<p>Soy un parrafo de la app2 <p>")


def contenido(request):
    contenido= "<h1>aqui esta todo el contenido de la app1<h1>"

    return HttpResponse(contenido)