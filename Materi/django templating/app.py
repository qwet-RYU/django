print("Hello, World!")

# ctrl +c baut matiin server (arahin ke link)
# cd .. loncat ke atas folder
# > django-admin startproject webapp

# loncat ke folder webapp: 
# > cd webapp

# jalankan project nya:
# > python manage.py runserver

# akses url di browser: 
# > http://127.0.0.1:8000/  
# >> boleh di copas atau tekan ctrl + click kiri di terminal

# matikan local server: 
# > ctrl + c

# buat app game
# > django-admin startapp game

# daftarkan app baru ke settings.py di folder webapp pada list INSTALLED_APPS

# petakan url route di settingan globals
# buka urls.py di folder webapp
#  path('game/', include('game.urls/)),
# jgn lupa import include nya juga
# from django.urls import path, include


# buat file urls.py di folder game
# hubungkan dengan view.NAMA_METHOD nya

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index)
# ]

# # buat method index di views.py

# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     html_content = "<h1>Portal Game!</h1>"
#     return HttpResponse(html_content)


# ke halaman game
# http://127.0.0.1:8000/game
# http://127.0.0.1:8000/game/moba
# ke halaman blog
# http://127.0.0.1:8000/blog

# memanggil file .html di view
# buat folder templates di dalam folder game 
# copas file-file .html nya ke folder templates

# cara menampilkan konten di view.py
# metode 1: sisipkan kode html di view
# metode 2: panggil file .html lewat render()


# membuat tampilan homepage
# buat folder templates di folder utama
# sejajar dengan webapp dan game
# setup templates di settings.py

# 'DIRS': [BASE_DIR / "templates"],

# lanjut..

# sisipkan kode ini di urls.py di folder webapp

# from django.views.generic import TemplateView

# ...
# ...
# # taruh di atas atau bawah admin path

# path("", TemplateView.as_view(template_name="home.html"), name="home"),