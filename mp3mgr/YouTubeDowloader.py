import uuid
import yt_dlp
import copy, os, shutil
from concurrent.futures import ThreadPoolExecutor


class MusicFile:
    def __init__(self):
        self.artist: str = ""
        self.song: str = ""
        self.album: str = ""
        self.genre: str = ""

    def __str__(self):
        return self.artist + " - " + self.song + " - " + self.album + " - " + self.genre


class YouTubeDownloader:
    BIN_DIR: str = "./bin"
    BINARIES: dict = {
        "FFMPEG": "ffmpeg.exe",
        "FFPLAY": "ffplay.exe",
        "FFPROBE": "ffprobe.exe",
        "MP3GAIN": "mp3gain.exe",
    }
    FILE_FORMAT: str = "mp3"

    def __init__(self):
        self._check_binaries()
        self.thread_pool = ThreadPoolExecutor(max_workers=5, thread_name_prefix="MusicFactory")

    def __del__(self):
        self.thread_pool.shutdown(wait=True)

    def _check_binaries(self):
        for binary in self.BINARIES.values():
            if not os.path.isfile(binary):
                # File not found in root
                self._move_binary(binary)

    def _move_binary(self, binary: str):
        if not os.path.isfile(self.BIN_DIR + "/" + binary):
            raise Exception("Binary not found")

        try:
            shutil.copy(self.BIN_DIR + "/" + binary, binary)
        except Exception as e:
            raise Exception("Error copying binary: " + binary + ", Exception: " + str(e))

        except:
            raise Exception("Error copying binary: " + binary)

    def _do_download(self, url: str, music_file: MusicFile, output_dir: str = "./"):
        pass


    def download_from_youtube(self, url: str, music_file: MusicFile, output_dir: str = "./"):
        pass



