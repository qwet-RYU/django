
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # lempar data ke template
    context = {
        'Portal_Name': 'Portal Game'
    }
    return render(request, 'portal.html', context)

# jangan lupa hubungkan url nya
def moba_view(request):
    return render(request, 'moba.html')

def genshin_view(request):
    return render(request, 'genshin.html')

def dota_view(request):
    return render(request, 'dota.html')
