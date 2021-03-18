from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def eleitor(request):
    return HttpResponse("Olá, mundo! Vocẽ é o eleitor pioneiro neste aplicativo.")

