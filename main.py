import os
import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from UI import *
from Songs import Songs

    


app = QApplication(sys.argv)
Frame = QtWidgets.QFrame()
ui = Ui_Frame()
ui.setupUi(Frame)
Frame.show()
song = Songs(ui)




#butonlar
ui.play.clicked.connect(song.play_clicked)
ui.find_path.clicked.connect(song.AddMusic)
ui.nextButton.clicked.connect(song.PlayNext)
ui.backButton.clicked.connect(song.PlayLast)
ui.SoundSlider.valueChanged.connect(song.setVolume)
ui.SoundSlider.value

sys.exit(app.exec_())



