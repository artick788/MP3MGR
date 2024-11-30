from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication
from PyQt5.QtCore import QThread, pyqtSignal
from mp3mgr.ui.ui_MainWindow import Ui_MainWindow
from mp3mgr.YouTubeDowloader import YouTubeDownloader, MusicFile
from mp3mgr.SearchGenre import search_genre
import qdarktheme


class SearchGenreThread(QThread):
    result = pyqtSignal(list)

    def __init__(self, artist: str, song: str):
        super().__init__()
        self.artist = artist
        self.song = song

    def run(self):
        print(f"Searching genres for {self.artist} - {self.song}...")
        genres = search_genre(self.artist, self.song)
        print(f"found genres: {genres}")
        self.result.emit(genres)


class MainWindow(QMainWindow):
    def __init__(self, app: QApplication):
        super().__init__()
        self.app = app
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("MP3MGR")

        # Download From YouTube Page
        self.ui.OpenSaveFolder.clicked.connect(self.open_folder)
        self.ui.DownloadButton.clicked.connect(self.download)
        self.ui.ResetButton.clicked.connect(self.reset)
        self.ui.FindGenre.clicked.connect(self.find_genre)

        self.ytd = YouTubeDownloader()

        # Tag File Page
        self.ui.OpenFileButton.clicked.connect(self.open_file)
        self.ui.SaveButton.clicked.connect(self.save_file)
        self.ui.FindGenre_2.clicked.connect(self.find_genre_2)

        self.file_tag = None

        self.search_thread = None

        self.set_dark_mode()

    def open_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        self.ui.SaveFolderLabel.setText(folder)

    def download(self):
        if self.ui.URLInput.text() == "":
            return
        file = MusicFile()
        file.artist = self.ui.ArtistInput.text()
        file.song = self.ui.SongInput.text()
        file.album = self.ui.AlbumInput.text()
        file.genre = self.ui.GenreInput.text()

        url = self.ui.URLInput.text()
        output_dir = self.ui.SaveFolderLabel.text()

        self.ytd.download_from_youtube(url, file, output_dir)
        self.reset()

    def reset(self):
        if self.ui.ResetArtist.isChecked():
            self.ui.ArtistInput.clear()
        if self.ui.ResetSong.isChecked():
            self.ui.SongInput.clear()
        if self.ui.ResetAlbum.isChecked():
            self.ui.AlbumInput.clear()
        if self.ui.ResetGenre.isChecked():
            self.ui.GenreInput.clear()

        self.ui.URLInput.clear()

    def open_file(self):
        file = QFileDialog.getOpenFileName(self, "Select File")
        self.ui.FileLocationLabel.setText(file[0])
        self.file_tag = MusicFile()
        self.file_tag.read_tags(file[0])
        self.ui.ArtistInput_2.setText(self.file_tag.artist)
        self.ui.SongInput_2.setText(self.file_tag.song)
        self.ui.AlbumInput_2.setText(self.file_tag.album)
        self.ui.GenreInput_2.setText(self.file_tag.genre)

    def save_file(self):
        if self.file_tag is None:
            return

        self.file_tag.artist = self.ui.ArtistInput_2.text()
        self.file_tag.song = self.ui.SongInput_2.text()
        self.file_tag.album = self.ui.AlbumInput_2.text()
        self.file_tag.genre = self.ui.GenreInput_2.text()

        self.file_tag.save_tags(self.ui.FileLocationLabel.text())

    def set_dark_mode(self):
        qdarktheme.setup_theme("auto")

    def set_genres(self, genres):
        self.ui.GenreInput.setText(", ".join(genres))
        self.ui.FindGenre.setEnabled(True)
        self.ui.GenreInput.setEnabled(True)
        self.ui.FindGenre_2.setEnabled(True)

    # freezes the UI
    def find_genre(self):
        if self.ui.ArtistInput.text() == "" or self.ui.SongInput.text() == "":
            return
        self.ui.FindGenre.setEnabled(False)
        self.ui.GenreInput.setEnabled(False)

        # Start the search thread
        self.search_thread = SearchGenreThread(self.ui.ArtistInput.text(), self.ui.SongInput.text())
        self.search_thread.result.connect(self.set_genres)
        self.search_thread.start()

    def find_genre_2(self):
        if self.ui.ArtistInput_2.text() == "" or self.ui.SongInput_2.text() == "":
            return
        self.ui.FindGenre_2.setEnabled(False)
        self.ui.GenreInput_2.setEnabled(False)

        # Start the search thread
        self.search_thread = SearchGenreThread(self.ui.ArtistInput_2.text(), self.ui.SongInput_2.text())
        self.search_thread.result.connect(self.set_genres)
        self.search_thread.start()


