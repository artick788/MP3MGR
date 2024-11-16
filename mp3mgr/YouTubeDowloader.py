import uuid
import yt_dlp
import copy, os, shutil
from concurrent.futures import ThreadPoolExecutor
import taglib

import ffmpeg


class MusicFile:
    def __init__(self):
        self.artist: str = ""
        self.song: str = ""
        self.album: str = ""
        self.genre: str = ""

    def __str__(self):
        return self.artist + " - " + self.song + " - " + self.album + " - " + self.genre

    def _get_value(self, field: str, f) -> str:
        if field in f.tags:
            l = f.tags[field]
            if len(l) > 0:
                return str(l[0])

        return ""

    def read_tags(self, file_path: str):
        f = taglib.File(file_path)
        self.artist = self._get_value("ARTIST", f)
        self.song = self._get_value("TITLE", f)
        self.album = self._get_value("ALBUM", f)
        self.genre = self._get_value("GENRE", f)

    def save_tags(self, file_path: str):
        f = taglib.File(file_path)
        f.tags["ARTIST"] = self.artist
        f.tags["TITLE"] = self.song
        f.tags["ALBUM"] = self.album
        f.tags["GENRE"] = self.genre

        f.save()


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

    def _do_download(self, url: str, music_file: MusicFile, output_dir: str = ""):
        rand = str(uuid.uuid4())
        output_file: str = output_dir + "/" + music_file.artist + " - " + music_file.song + "." + self.FILE_FORMAT

        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': rand + '.%(ext)s',
            'addmetadata': True,
            'extractaudio': True,
            'prefer-ffmpeg': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': self.FILE_FORMAT,
                'preferredquality': '320',
            }],
        }
        tries: int = 3
        while tries > 0:
            print(f"Downloading: {url} with {tries} remaining tries")
            try:
                with yt_dlp.YoutubeDL(options) as ydl:
                    ydl.download([url])
                    stream = ffmpeg.input(rand + '.m4a')
                    stream = ffmpeg.output(stream, rand + "." + self.FILE_FORMAT)

                    # rename
                    shutil.move(rand + "." + self.FILE_FORMAT, output_file)

                    # tag file
                    music_file.save_tags(output_file)

                    print("Download successful: " + output_file)
                    return output_file
            except Exception as e:
                print("Download failed: " + str(e) + " \nTries: " + str(tries))
                tries -= 1
            except KeyboardInterrupt:
                print("Download interrupted\nTries: " + str(tries))
                tries -= 1
            except:
                print("Download failed: no further details, \nTries: " + str(tries))
                tries -= 1

        return None

    def download_from_youtube(self, url: str, music_file: MusicFile, output_dir: str = ""):
        print(f"Submitted URL: {url} to download queue.")
        # deep copy to avoid reference
        c_url = copy.deepcopy(url)
        c_music_file = copy.deepcopy(music_file)
        c_output_dir = copy.deepcopy(output_dir)
        self.thread_pool.submit(self._do_download, c_url, c_music_file, c_output_dir)



