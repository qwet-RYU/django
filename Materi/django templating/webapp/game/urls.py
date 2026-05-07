from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # url homepage
    path("", TemplateView.as_view(template_name="portal.html"), name="portal"),
    # url index
    path('', views.index),
    # url ml
    path('moba/', views.moba_view),
    # url genshin
    path('genshin/', views.genshin_view),
    # url dota
    path('dota/', views.dota_view),
]