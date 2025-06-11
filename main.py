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
            "Error: 'uv' command not found. Please ensure 'uv' is installed and "
            "in your system's PATH."
        )
        print(
            "You can usually install it via 'pip install uv' or refer to uv's official "
            "documentation."
        )
    except subprocess.CalledProcessError as e:
        print(f"Error updating yt-dlp: {e}")
        print(
            "Please ensure you have an active internet connection and correct permissions."
        )
    except Exception as e:
        print(f"An unexpected error occurred during yt-dlp update: {e}")


def download_process():
    video_url = input("Enter the YouTube video URL: ")
    OUTPUT_DIR = "./downloads"
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    while True:
        audio_video = (
            input('Enter "v" for video download or "a" for audio download: ')
            .strip()
            .lower()
        )
        if audio_video in ["v", "a"]:
            break
        print('Invalid input. Please enter "v" for video or "a" for audio.')

    if audio_video == "v":
        vd.video_download(video_url, OUTPUT_DIR, quality="best")
    else:
        au_dl.audio_download(video_url, OUTPUT_DIR)


if __name__ == "__main__":
    update_yt_dlp()  # Update yt-dlp before downloading
    download_process()  # Start the download process
    print("Download process completed.")
