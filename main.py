import os
import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from UI import *
from Songs import Songs




app = QtWidgets.QApplication(sys.argv)
Frame = QtWidgets.QFrame()
ui = Ui_Frame()
ui.setupUi(Frame)
Frame.show()



song = Songs(ui)


def play_clicked():
    if (song.isChanged() == False):
        try:
            if (ui.play.text() == "▶" and song.status == ""):
                song.PlayMusic()
                ui.play.setText("||")
                song.check_event()

            elif (ui.play.text() == "▶"and song.status == "Paused"):
                song.UnpauseMusic()
                ui.play.setText("||")
                song.check_event()

            elif (ui.play.text() == "||"):
                song.PauseMusic()
                ui.play.setText("▶")
                
        except:
            ui.play.setText("▶")

    else:
        try:
            ui.play.setText("||")
            song.PlayMusic()
            song.check_event()
        except:
            ui.play.setText("▶")


#butonlar
ui.play.clicked.connect(play_clicked)
ui.find_path.clicked.connect(song.AddMusic)
ui.nextButton.clicked.connect(song.PlayNext)
ui.backButton.clicked.connect(song.PlayLast)

song.check_event()
sys.exit(app.exec_())


