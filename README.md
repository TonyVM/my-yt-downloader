# YouTube Downloader (yt-dlp)

This project is a command-line tool in Python to download YouTube videos or audio using the [yt-dlp](https://github.com/yt-dlp/yt-dlp) library. It allows the user to choose whether to download the full video (with audio) or just the audio, saving the files in a local folder.

## Motivation
I created this project to avoid using online services that offer the same functionality but are filled with intrusive advertisements and pop-ups. With this tool, you can download YouTube videos or audio directly from your terminal, ad-free and with full control over the output.

## Features
- Download YouTube videos in the best available quality (video + audio, MP4 format).
- Download audio only in MP3 format.
- Configurable downloads folder (`./downloads`).
- Modular and easy-to-maintain code.
- Automated tests with `pytest` to verify download and file cleanup functionality.

## Project Structure
```
├── audio_downloader_module.py         # Logic for audio-only downloads
├── video_downloader_module.py         # Logic for video (and audio) downloads
├── main.py                           # Main script for user interaction
├── tests/
│   └── test_download.py              # Automated tests for download and cleanup
├── downloads/                        # Folder where downloaded files are saved
├── requirements.txt                  # Project dependencies
├── pytest.ini                        # Pytest configuration
└── .gitignore                        # Files and folders ignored by git
```

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the main script:
   ```bash
   python main.py
   ```
3. Enter the YouTube video URL when prompted.
4. Choose whether to download the full video (`v`) or just the audio (`a`).
5. The file will be saved in the `downloads/` folder.

## Testing
To run the automated tests:
```bash
pytest
```
The tests verify that both video and audio downloads work correctly and that downloaded files are deleted after each test.

## Notes
- This project uses `yt-dlp`, which requires `ffmpeg` to be installed on your system for file conversion and merging.
- You can customize the downloads folder and quality by modifying the parameters in the code.

## License
This project is for educational and personal use only. Always respect YouTube's terms of service and copyright laws.
