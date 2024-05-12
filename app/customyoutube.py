from dotenv import load_dotenv
from pyyoutube import Api
from . import utilits
import os
import re
load_dotenv()

# Access SECRET_KEY
secret_key = os.getenv('API')

class CustomYoutube:
    def __init__(self,playlist_link,api_key=secret_key):
        self.playlist_link = playlist_link
        self.api_key = Api(api_key=api_key)
     
    def extract_playlist_id(self):
        pattern = r'list=([a-zA-Z0-9_-]+)'
        match = re.search(pattern, self.playlist_link)
        if match:
            playlist_id = match.group(1)
            return playlist_id
        else:
            return None

    def get_items_from_playlist(self):
        playlist_id = self.extract_playlist_id()

        if playlist_id:
            playlist_item_by_playlist = self.api_key.get_playlist_items(playlist_id=playlist_id, count= None)    
        return playlist_item_by_playlist
      
    def videos_details(self):
        video_urls = {}
        print(self.get_items_from_playlist().items)
       
        for item in self.get_items_from_playlist().items:
            try:
                video_id = item.contentDetails.videoId
                video_name = item.snippet.title
                video_thumbnails = item.snippet.thumbnails       
                video_details = self.api_key.get_video_by_id(video_id=video_id)
                duration = video_details.items[0].contentDetails.duration   
                
                video_url = f'https://www.youtube.com/watch?v={video_id}'
                resolutions = []
                audio_quality = []
                # if utilits.get_video_qualities(video_url):
                #     video_streams, audio_streams = utilits.get_video_qualities(video_url)
           
                #     resolutions = set([stream.resolution for stream in video_streams if stream.resolution])
               
                #     audio_quality = set([stream.abr for stream in audio_streams if stream.abr])
               

                video_urls[item.id] = {
                    'video_id':video_id,
                    'video_name':video_name[:25],
                    'video_thumbnail':video_thumbnails.default.url,
                    'video_duration':utilits.parse_youtube_duration(duration),
                    'video_url':video_url,
                    'video_mp3':[0],
                    'video_mp4':[0]
                }
                
                
            except IndexError:
                print('Listdə səhv var!')
            continue
        return video_urls