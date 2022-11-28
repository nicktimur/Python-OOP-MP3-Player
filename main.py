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
song = Songs(ui)

class Worker(QThread):
    def run(self):
        try:
            while True:
                if(song.status == "Playing"):
                    song.check_event()
        except:
            pass

class TimeSetter(Worker):
    def run(self):
        while True:
            if(song.status == "Playing"):
                try:
                    song.set_time()
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
ui.Backward.clicked.connect(song.backward)
ui.Forward.clicked.connect(song.forward)



timeSetter = TimeSetter()
timeSetter.start()


thread = Worker()
thread.start()



sys.exit(app.exec_())



