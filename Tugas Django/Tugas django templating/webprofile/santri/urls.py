from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
     # url homepage
    # path("", TemplateView.as_view(template_name="portal.html"), name="portal"),
    # url index
    path('index/', views.santri_home, name="santri_home"),
    # url biodata
    path('biodata/', views.biodata, name="biodata"),
    # url jadwal
    path('jadwal/', views.jadwal, name="jadwal"),
    # url galeri
    path('galeri/', views.galeri, name="galeri"),
    # url feedback
    path('feedback/', views.feedback, name="feedback"),
]