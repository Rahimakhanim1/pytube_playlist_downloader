from django.shortcuts import render, redirect
from pyyoutube import Api
from pytube import YouTube
from . import customyoutube
import json
from django.http import HttpResponse, JsonResponse
import os
from django.conf import settings
import json

def home(request):
    return render(request, 'index.html')


def showVideos(request):
    if request.method == "POST":
        playlist_link = request.POST['link-input']
        video_obj = customyoutube.CustomYoutube(playlist_link)   
        print(video_obj)
        videos_details = video_obj.videos_details()
        return render(request, 'index.html', {'videos_details': videos_details.values()})


def download_video_audio(request):
      if request.method == 'POST':
        data = json.loads(request.body)
        video_urls = data['video_urls'].split(',')
      
        for i in video_urls:
            def download_video(url, output_directory):
                try:
                    current_directory = os.getcwd()
                    os.chdir(output_directory)
                    yt = YouTube(url)
                    if data['type']=="mp3":
                        audio_stream = yt.streams.filter(only_audio=True).first()
                        audio_stream.download()
                    else:
                        video = yt.streams.get_highest_resolution()
                        video.download()

                    os.chdir(current_directory)
                    print("Download successful!")
                except Exception as e:
                    print("Error:", e)
            url = i
            output_directory = os.path.join(os.path.expanduser("~"), "Downloads")
            if data['type']=="mp3":
                output_directory_music = os.path.join(os.path.expanduser("~"), "Music")
            else:
                output_directory_music = os.path.join(os.path.expanduser("~"), "Videos")

            
            download_video(url, output_directory)
            download_video(url, output_directory_music)
  

        return render(request, 'index.html')