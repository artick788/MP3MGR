from PyQt5.QtWidgets import QApplication, QMainWindow
from mp3mgr.MainWindow import MainWindow
import sys


def window():
    app = QApplication(sys.argv)
    main = MainWindow(app)
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()