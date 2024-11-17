from PyQt5.QtWidgets import QMainWindow, QFileDialog
from mp3mgr.ui.ui_MainWindow import Ui_MainWindow
from mp3mgr.YouTubeDowloader import YouTubeDownloader, MusicFile


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("MP3MGR")

        # Download From YouTube Page
        self.ui.OpenSaveFolder.clicked.connect(self.open_folder)
        self.ui.DownloadButton.clicked.connect(self.download)
        self.ui.ResetButton.clicked.connect(self.reset)

        self.ytd = YouTubeDownloader()

        # Tag File Page
        self.ui.OpenFileButton.clicked.connect(self.open_file)
        self.ui.SaveButton.clicked.connect(self.save_file)

        self.file_tag = None

    def open_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        self.ui.SaveFolderLabel.setText(folder)

    def download(self):
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
