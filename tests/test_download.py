import os
import pytest
import audio_downloader_module as au_dl
import video_downloader_module as vd

TEST_VIDEO_URL = (
    "https://www.youtube.com/watch?v=yO01B8OoXfo"  # Video de prueba de yt-dlp
)
OUTPUT_DIR = "./downloads"


@pytest.mark.parametrize("mode", ["v", "a"])
def test_download_and_cleanup(mode):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    if mode == "v":
        vd.video_download(TEST_VIDEO_URL, OUTPUT_DIR, quality="best")
        ext = ".mp4"
    else:
        au_dl.audio_download(TEST_VIDEO_URL, OUTPUT_DIR)
        ext = ".mp3"
    # Buscar el archivo descargado
    files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(ext)]
    assert files, f"No se encontró archivo descargado con extensión {ext}"
    # Eliminar el archivo descargado
    for f in files:
        os.remove(os.path.join(OUTPUT_DIR, f))
        assert not os.path.exists(
            os.path.join(OUTPUT_DIR, f)
        ), f"El archivo {f} no fue eliminado"
