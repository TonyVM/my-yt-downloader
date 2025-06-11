import yt_dlp
import os


def audio_download(video_url: str, output_dir: str):

    AUDIO_OPTS = {
        "format": "bestaudio/best",  # Select best audio
        "audio_format": "mp3",  # Specify audio format
        "extractaudio": True,  # Extract audio only
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),  # Custom output path
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",  # Extract audio using FFmpeg
                "preferredcodec": "mp3",  # Preferred audio codec
                "preferredquality": "192",  # Preferred audio quality
            }
        ],
        "quiet": False,
    }

    try:
        with yt_dlp.YoutubeDL(AUDIO_OPTS) as ydl:
            print(f"Initiating audio download for: {video_url}")
            ydl.download([video_url])
        print("Audio downloaded successfully!")
    except Exception as e:
        print(f"An error occurred during audio download: {e}")
