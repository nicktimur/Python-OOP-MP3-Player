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




def play_clicked():
    if (song.isChanged() == False):
        try:
            if (ui.play.text() == "▶" and song.playing):
                song.PlayMusic()
                ui.play.setText("||")

            elif (ui.play.text() == "▶"and not song.playing):
                song.UnpauseMusic()
                ui.play.setText("||")

            elif (ui.play.text() == "||"):
                song.PauseMusic()
                ui.play.setText("▶")
                
        except:
            ui.play.setText("▶")

    else:
        try:
            ui.play.setText("||")
            song.PlayMusic()
        except:
            ui.play.setText("▶")


#butonlar
ui.play.clicked.connect(play_clicked)
ui.find_path.clicked.connect(song.AddMusic)
ui.nextButton.clicked.connect(song.PlayNext)
ui.backButton.clicked.connect(song.PlayLast)
ui.SoundSlider.valueChanged.connect(song.setVolume)
ui.SoundSlider.value

sys.exit(app.exec_())



