import yt_dlp
import os


def video_download(video_url, output_dir: str, quality='best'):
    '''Download video from YouTube using yt-dlp.'''

    downloader_video_opts = {
        'format': f'bestvideo+bestaudio/{quality}',  # Select best video and best audio
        'merge_output_format': 'mp4',          # Output format
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # Custom output
        # path
        # 'ffmpeg_location': '/path/to/ffmpeg/bin/ffmpeg.exe' # Specify FFmpeg
        # path if not in system PATH [12]
        'quiet': False
    }
    try:
        with yt_dlp.YoutubeDL(downloader_video_opts) as downloader:
            print(f'Initiating video download for: {video_url}')
            downloader.download([video_url])
    except Exception as e:
        print(f'An error occurred during video download: {e}')
