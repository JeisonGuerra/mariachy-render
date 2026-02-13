from django.contrib import admin
from django.urls import path
from . import views

app_name='mexicano'
urlpatterns = [
    path('', views.index, name='index'),
    path('noticias/', views.noticias, name='noticias'),
    path('resenas/', views.resenas, name='resenas'),
    path('imagenes/<int:foto_id>/', views.imagen, name='imagen'),
    path('videos/<int:video_id>/', views.video, name='video'),
    path('proxima_imagen/<str:proxima>/<int:img_id>/', views.proxima_imagen, name="proxima_imagen"),
    path('proximo_video/<str:proxima>/<int:vid_id>/', views.proximo_video, name="proximo_video"),
]