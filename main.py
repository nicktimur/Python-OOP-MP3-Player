import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from UI import *
from Songs import Songs
from Workers import Worker, TimeSetter

class Main():
    def __init__(self) -> None: 
        self.app = QApplication(sys.argv)
        self.Frame = QtWidgets.QFrame()
        self.ui = Ui_Frame()
        self.ui.setupUi(self.Frame)
        self.Frame.show()
        self.song = Songs(self.ui)
        self.timeSetter = TimeSetter(self.song)
        self.thread = Worker(self.song)


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

        self.timeSetter.start()

        self.thread.start()

        sys.exit(self.app.exec_())

main = Main()
main.main() # al sana beş class bro

