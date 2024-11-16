from PyQt5.QtWidgets import QMainWindow, QFileDialog
from mp3mgr.ui.ui_MainWindow import Ui_MainWindow
from mp3mgr.YouTubeDowloader import YouTubeDownloader, MusicFile


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("MP3MGR")

        # Connect signals to slots
        self.ui.OpenSaveFolder.clicked.connect(self.open_folder)
        self.ui.DownloadButton.clicked.connect(self.download)
        self.ui.ResetButton.clicked.connect(self.reset)

        self.ytd = YouTubeDownloader()

    def open_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        self.ui.SaveFolderLabel.setText(folder + "/")

    def download(self):
        print("Download")

    def reset(self):
        if self.ui.ResetArtist.isChecked():
            self.ui.ArtistInput.clear()
        if self.ui.ResetSong.isChecked():
            self.ui.SongInput.clear()
        if self.ui.ResetAlbum.isChecked():
            self.ui.AlbumInput_2.clear()
        if self.ui.ResetGenre.isChecked():
            self.ui.GenreInput.clear()

        self.ui.URLInput.clear()