import os
import sys
from PyQt5 import *
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import *
import time
from UI import *
from Songs import Songs



app = QApplication(sys.argv)
Frame = QtWidgets.QFrame()
ui = Ui_Frame()
ui.setupUi(Frame)
Frame.show()
Frame.addAction
song = Songs(ui)

class Worker(QThread):
    def __init__(self, song):
        super().__init__()
        self.song = song

    def run(self):
        try:
            while True:
                if(self.song.status == "Playing"):
                    time.sleep(0.5)
                    self.song.check_event()
        except:
            pass

class TimeSetter(Worker):
    def run(self):
        while True:
            if(self.song.status == "Playing"):
                try:
                    self.song.set_time()
                except:
                    pass
        




#butonlar
ui.play.clicked.connect(song.play_clicked)
ui.find_path.clicked.connect(song.AddMusic)
ui.nextButton.clicked.connect(song.PlayNext)
ui.backButton.clicked.connect(song.PlayLast)
ui.SoundSlider.valueChanged.connect(song.setVolume)
ui.songs_list.doubleClicked.connect(song.play_clicked)
ui.PlaySlider.sliderPressed.connect(song.sliderPress)
ui.PlaySlider.sliderReleased.connect(song.sliderRelease)


timeSetter = TimeSetter(song)
timeSetter.start()


thread = Worker(song)
thread.start()



sys.exit(app.exec_())



