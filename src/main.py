from downloader import download_video

   
        
if __name__ == "__main__":
    url = input("Enter the video URL: ")
    name = input("Enter the desired filename (without extension): ")
    download_video(url, name)