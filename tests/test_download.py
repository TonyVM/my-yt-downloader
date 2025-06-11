import os
import pytest
from unittest.mock import patch
import audio_downloader_module as au_dl
import video_downloader_module as vd

TEST_VIDEO_URL = "https://www.youtube.com/watch?v=yO01B8OoXfo"
OUTPUT_DIR = "./downloads"


def is_github_actions():
    return os.environ.get("GITHUB_ACTIONS") == "true"


@pytest.mark.parametrize("mode", ["v", "a"])
def test_download_and_cleanup(mode):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    if is_github_actions():
        # Mock en GitHub Actions
        with patch.object(vd, "video_download") as mock_video, patch.object(
            au_dl, "audio_download"
        ) as mock_audio:
            if mode == "v":
                vd.video_download(TEST_VIDEO_URL, OUTPUT_DIR, quality="best")
                mock_video.assert_called_once_with(
                    TEST_VIDEO_URL, OUTPUT_DIR, quality="best"
                )
            else:
                au_dl.audio_download(TEST_VIDEO_URL, OUTPUT_DIR)
                mock_audio.assert_called_once_with(TEST_VIDEO_URL, OUTPUT_DIR)
    else:
        # Descarga real en local
        if mode == "v":
            vd.video_download(TEST_VIDEO_URL, OUTPUT_DIR, quality="best")
            ext = ".mp4"
        else:
            au_dl.audio_download(TEST_VIDEO_URL, OUTPUT_DIR)
            ext = ".mp3"
        files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(ext)]
        assert files, f"No se encontró archivo descargado con extensión {ext}"
        for f in files:
            os.remove(os.path.join(OUTPUT_DIR, f))
            assert not os.path.exists(os.path.join(OUTPUT_DIR, f)), (
                f"El archivo {f} no fue eliminado"
            )
