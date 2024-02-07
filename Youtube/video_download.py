from pytube import YouTube
video_url = 'https://www.youtube.com/watch?v=Pl3NBhMgDZs'
yt = YouTube(video_url)
video_stream = yt.streams.get_highest_resolution()
video_stream.download()
print(f"Video downloaded successfully in {video_stream.resolution} resolution.")
