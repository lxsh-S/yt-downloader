import os
import yt_dlp 
from main import name


def download_video(url, output_path="Downloads"):
    try:    
            ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(output_path, name),
            'noplaylist': True,
            'merge_output_format': 'mp4',
            'quiet': True,
        }
    
            if not os.path.exists(output_path):
                os.makedirs(output_path)
                
                
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print(f"Video downloaded successfully to {output_path}")
            
    except yt_dlp.YoutubeDownloadError as De:
        print(f"An error occurred: {De}")
        
        try:
            with yt_dlp.YoutubeDL({'listformats': True}) as ydl:
                ydl.download([url])
        except Exception as e:
            print(f"Failed to retrieve formats: {e}")
            
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
     