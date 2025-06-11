import os
import audio_downloader_module as au_dl
import video_downloader_module as vd
import subprocess


def update_yt_dlp():
    """Update yt-dlp to the latest version using uv."""
    try:
        subprocess.check_call(["uv", "pip", "install", "-U", "yt-dlp"])
        print("yt-dlp updated successfully.")
    except FileNotFoundError:
        print(
            "Error: 'uv' command not found. Please ensure 'uv' is installed and in your system's PATH."
        )
        print(
            "You can usually install it via 'pip install uv' or refer to uv's official documentation."
        )
    except subprocess.CalledProcessError as e:
        print(f"Error updating yt-dlp: {e}")
        print(
            "Please ensure you have an active internet connection and correct permissions."
        )
    except Exception as e:
        print(f"An unexpected error occurred during yt-dlp update: {e}")


def download_process():
    # Example: Download best quality video and audio, merge to MP4
    video_url = input("Enter the YouTube video URL: ")  # Example URL
    audio_video = (
        input('Enter "v" for video download or "a" for audio download: ')
        .strip()
        .lower()
    )
    OUTPUT_DIR = "./downloads"  # Default output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)  # Ensure output directory exists
    if audio_video not in ["v", "a"]:

        while audio_video not in ["v", "a"]:
            audio_video = (
                input(
                    'Invalid input. Enter "v" for video download or "a" for audio download: '
                )
                .strip()
                .lower()
            )
            print(audio_video)
            if audio_video == "v":
                vd.video_download(video_url, OUTPUT_DIR, quality="best")
            else:
                au_dl.audio_download(video_url, OUTPUT_DIR)
    else:
        if audio_video == "v":
            vd.video_download(video_url, OUTPUT_DIR, quality="best")
        else:
            au_dl.audio_download(video_url, OUTPUT_DIR)


if __name__ == "__main__":
    update_yt_dlp()  # Update yt-dlp before downloading
    download_process()  # Start the download process
    print("Download process completed.")
