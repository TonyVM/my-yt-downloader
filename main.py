import os
import audio_downloader_module as au_dl
import video_downloader_module as vd

# Example: Download best quality video and audio, merge to MP4
video_url = input("Enter the YouTube video URL: ")  # Example URL
audio_video = (
    input('Enter "v" for video download or "a" for audio download: ').strip().lower()
)
OUTPUT_DIR = "./downloads"  # Default output directory
os.makedirs(OUTPUT_DIR, exist_ok=True)  # Ensure output directory exists


while audio_video not in ["v", "a"]:
    audio_video = (
        input('Invalid input. Enter "v" for video download or "a" for audio download: ')
        .strip()
        .lower()
    )
    if audio_video == "v":
        vd.video_download(video_url, OUTPUT_DIR, quality="best")
    else:
        au_dl.audio_download(video_url, OUTPUT_DIR)
