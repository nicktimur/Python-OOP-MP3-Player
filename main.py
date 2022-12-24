import os
import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from UI import *
from Songs import Songs
from Workers import Worker, TimeSetter
import sqlite3

class Main():
    def __init__(self) -> None: 
        self.app = QApplication(sys.argv)
        self.Frame = QtWidgets.QFrame()
        self.ui = Ui_Frame()
        self.ui.setupUi(self.Frame)
        self.Frame.show()
        self.DB_DIR = os.path.join(os.getcwd() + "/path.db")
        self.song = Songs(self.ui)
        self.timeSetter = TimeSetter(self.song)
        self.thread = Worker(self.song)


    def Create_Table(self):
        with sqlite3.connect(self.DB_DIR) as db:
            cur = db.cursor()
            cmd = "CREATE TABLE IF NOT EXISTS path(path TEXT)"
            cur.execute(cmd)

    def about_us(self):
        QMessageBox.about(self.Frame, "Hakkımızda", "<html><head/><body><p align=\"center\"><span style=\" color:#c2c2c2;\"></br><br></br>Alp Doruk Şengün - 20217170015<br></br> Timur Karakaş - 20217170062</span></p></p></body></html>")

    def main(self):   
        #butonlar
        self.ui.play.clicked.connect(self.song.play_clicked)
        self.ui.find_path.clicked.connect(self.song.AddMusic)
        self.ui.nextButton.clicked.connect(self.song.PlayNext)
        self.ui.backButton.clicked.connect(self.song.PlayLast)
        self.ui.SoundSlider.valueChanged.connect(self.song.setVolume)
        self.ui.songs_list.doubleClicked.connect(self.song.play_clicked)
        self.ui.PlaySlider.sliderPressed.connect(self.song.sliderPress)
        self.ui.PlaySlider.sliderReleased.connect(self.song.sliderRelease)
        self.ui.Backward.clicked.connect(self.song.backward)
        self.ui.Forward.clicked.connect(self.song.forward)
        self.ui.about_us.clicked.connect(self.about_us)

        self.timeSetter.start()
        self.thread.start()

        sys.exit(self.app.exec_())

main = Main()
main.Create_Table()
main.main()

