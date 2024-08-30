from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>soy el index de la app3<h1>")

def pagina3(request):
    html="""
        <p>soy el parrafo de la app3</p>
        <h2>soy un subtitulo de la app3</h2>
    """
    return HttpResponse(html)
    