# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 648)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.URLInput = QtWidgets.QLineEdit(self.tab)
        self.URLInput.setObjectName("URLInput")
        self.horizontalLayout.addWidget(self.URLInput)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.GenreInput = QtWidgets.QLineEdit(self.tab)
        self.GenreInput.setObjectName("GenreInput")
        self.gridLayout_2.addWidget(self.GenreInput, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.ArtistInput = QtWidgets.QLineEdit(self.tab)
        self.ArtistInput.setObjectName("ArtistInput")
        self.gridLayout_2.addWidget(self.ArtistInput, 0, 1, 1, 1)
        self.SongInput = QtWidgets.QLineEdit(self.tab)
        self.SongInput.setObjectName("SongInput")
        self.gridLayout_2.addWidget(self.SongInput, 1, 1, 1, 1)
        self.AlbumInput = QtWidgets.QLineEdit(self.tab)
        self.AlbumInput.setObjectName("AlbumInput")
        self.gridLayout_2.addWidget(self.AlbumInput, 2, 1, 1, 1)
        self.ResetArtist = QtWidgets.QCheckBox(self.tab)
        self.ResetArtist.setChecked(True)
        self.ResetArtist.setObjectName("ResetArtist")
        self.gridLayout_2.addWidget(self.ResetArtist, 0, 2, 1, 1)
        self.ResetSong = QtWidgets.QCheckBox(self.tab)
        self.ResetSong.setChecked(True)
        self.ResetSong.setObjectName("ResetSong")
        self.gridLayout_2.addWidget(self.ResetSong, 1, 2, 1, 1)
        self.ResetAlbum = QtWidgets.QCheckBox(self.tab)
        self.ResetAlbum.setChecked(True)
        self.ResetAlbum.setObjectName("ResetAlbum")
        self.gridLayout_2.addWidget(self.ResetAlbum, 2, 2, 1, 1)
        self.ResetGenre = QtWidgets.QCheckBox(self.tab)
        self.ResetGenre.setChecked(True)
        self.ResetGenre.setObjectName("ResetGenre")
        self.gridLayout_2.addWidget(self.ResetGenre, 3, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.OpenSaveFolder = QtWidgets.QPushButton(self.tab)
        self.OpenSaveFolder.setObjectName("OpenSaveFolder")
        self.horizontalLayout_3.addWidget(self.OpenSaveFolder)
        self.SaveFolderLabel = QtWidgets.QLabel(self.tab)
        self.SaveFolderLabel.setText("")
        self.SaveFolderLabel.setObjectName("SaveFolderLabel")
        self.horizontalLayout_3.addWidget(self.SaveFolderLabel)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.DownloadButton = QtWidgets.QPushButton(self.tab)
        self.DownloadButton.setObjectName("DownloadButton")
        self.horizontalLayout_4.addWidget(self.DownloadButton)
        self.ResetButton = QtWidgets.QPushButton(self.tab)
        self.ResetButton.setObjectName("ResetButton")
        self.horizontalLayout_4.addWidget(self.ResetButton)
        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Paste the URL of your YouTube Video, click on Download and the tool will convert the audio of your video into an MP3."))
        self.label_2.setText(_translate("MainWindow", "YouTube URL"))
        self.label_7.setText(_translate("MainWindow", "Album"))
        self.label_6.setText(_translate("MainWindow", "Genre"))
        self.label_4.setText(_translate("MainWindow", "Song"))
        self.label_3.setText(_translate("MainWindow", "Artist"))
        self.ResetArtist.setText(_translate("MainWindow", "Reset"))
        self.ResetSong.setText(_translate("MainWindow", "Reset"))
        self.ResetAlbum.setText(_translate("MainWindow", "Reset"))
        self.ResetGenre.setText(_translate("MainWindow", "Reset"))
        self.label_5.setText(_translate("MainWindow", "Choose where to save the MP3"))
        self.OpenSaveFolder.setText(_translate("MainWindow", "Open Folder"))
        self.DownloadButton.setText(_translate("MainWindow", "Download"))
        self.ResetButton.setText(_translate("MainWindow", "Reset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Download from YouTube"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
