import yt_dlp
import os

# Example: Download best quality video and audio, merge to MP4
video_url = input("Enter the YouTube video URL: ")  # Example URL 
output_dir = './downloads'
os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Select best video and best audio
    
    'merge_output_format': 'mp4',          # Output format
    'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # Custom output 
    # path
    # 'ffmpeg_location': '/path/to/ffmpeg/bin/ffmpeg.exe' # Specify FFmpeg
    # path if not in system PATH [12]
    'quiet': False
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Initiating download for: {video_url}")
        ydl.download([video_url])
    print("Video downloaded successfully!")
except Exception as e:
    print(f"An error occurred during download: {e}")
