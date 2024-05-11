import isodate
from pytube import YouTube
def parse_youtube_duration(duration_str):
                duration = isodate.parse_duration(duration_str)
                hours = duration.days * 24 + duration.seconds // 3600
                minutes = (duration.seconds % 3600) // 60
                seconds = duration.seconds % 60
                return str(hours)+':'+str(minutes)+':'+str(seconds)



# def get_video_qualities(video_url):
#     try:
#         yt = YouTube(video_url)
#         # Get available streams
#         video_streams = yt.streams.filter(file_extension='mp4').all()
#         audio_streams = yt.streams.filter(only_audio=True).all()
#         return video_streams, audio_streams
#     except:
#         pass