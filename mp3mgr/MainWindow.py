from PyQt5.QtWidgets import QMainWindow
from mp3mgr.ui.ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("MP3MGR")