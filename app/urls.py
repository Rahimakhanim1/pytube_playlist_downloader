from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('showVideos',views.showVideos,name='show-videos'),
    path('download/',views.download_video_audio,name='download-video-audio')
]