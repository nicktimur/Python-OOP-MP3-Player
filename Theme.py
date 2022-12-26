from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import os

class theme_changer:
    theme = "default"
    def __init__(self, Frame, ui, song, DB_DIR):
        self.Frame = Frame
        self.ui = ui
        self.song = song
        self.theme = "default"
        self.DB_DIR = DB_DIR
        with sqlite3.connect(self.DB_DIR) as db:
            try:
                cur = db.cursor()
                cmd = "SELECT theme FROM theme"
                cur.execute(cmd)
                self.theme = cur.fetchone()[0]
                theme_changer.theme = self.theme
            except:
                pass
        match self.theme:
            case "BlackBull":
                self.BlackBull()
            case "default":
                self.Default()
            case "Indian Rush":
                self.Indian_Rush()
            case "White Chocolate":
                self.White_Chocolate()
            case "Bleeding Rose":
                self.Bleeding_Rose()

    def Bleeding_Rose(self):
        # Veri tabanına son kullanılan temayı ekleme
        self.theme = "Bleeding Rose"
        theme_changer.theme = self.theme
        with sqlite3.connect(self.DB_DIR) as db:
                cur = db.cursor()
                cmd = "DELETE FROM theme"
                cur.execute(cmd)
                cmd = "INSERT INTO theme VALUES ('{}')".format(self.theme)
                cur.execute(cmd)

        # Frame'in ayarlanması
        self.Frame.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);\n"
"border-color: rgb(80, 80, 80);\n"
"background-color: #340000;\n"
"")
        self.ui.frame.setStyleSheet("background-color: #4b0001;\n""")


        # Rose tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.ui.Bleeding_Rose.setFont(font)
        self.ui.Bleeding_Rose.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #630001;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: #820002;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: #720002;\n"
"    border: 2px solid #630001;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: #5d0003\n"
"    }")

        # Play tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(20)
        self.ui.play.setFont(font)
        self.ui.play.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #630001;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: #820002;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: #720002;\n"
"    border: 2px solid #630001;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: #5d0003\n"
"    }")

        # Now Playing kısmının ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.ui.nowPlaying.setFont(font)
        self.ui.nowPlaying.setStyleSheet("background-color: #820002;\n"
"color: #c2c2c2;\n"
"border: 2px solid #630001;\n"
"border-radius: 5px;\n"
"border-style: outset;\n"
"")

        # İleri Tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ui.nextButton.setFont(font)
        self.ui.nextButton.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #630001;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: #820002;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: #720002;\n"
"    border: 2px solid #630001;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: #5d0003\n"
"    }")

        # Geri tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.ui.backButton.setFont(font)
        self.ui.backButton.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #630001;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: #820002;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: #720002;\n"
"    border: 2px solid #630001;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: #5d0003\n"
"    }")

        # Shuffle tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.ui.Shuffle.setFont(font)
        self.ui.Shuffle.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #630001;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: #820002;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: #720002;\n"
"    border: 2px solid #630001;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: #5d0003\n"
"    }")

        # Ses seviyesi slider'ının ayarlanması
        self.ui.SoundSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: black;\n"
"height: 4px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background:  qlineargradient(spread:pad, x1:0.488636, y1:1, x2:0.483, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.534091 rgba(255, 0, 0, 255));\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal {\n"
"border: 2px solid qlineargradient(spread:pad, x1:0.523, y1:0, x2:0.517, y2:1, stop:0.590909 rgba(0, 0, 0, 255), stop:1 rgba(255, 18, 18, 255));\n"
"height: 10px;\n"
"border-radius: 2.5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background-color: #820002;\n"
"border: 1px solid #630001;\n"
"width: 17px;\n"
"height: 30px;\n"
"margin-top: -7px;\n"
"margin-bottom: -7px;\n"
"border-radius: 9px;\n"
"border-style: outset;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background-color: #720002;\n"
"border: 1px solid #630001;\n"
"width: 17px;\n"
"height: 30px;\n"
"margin-top: -7px;\n"
"margin-bottom: -7px;\n"
"border-radius: 9px;\n"
"border-style: outset;\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed{\n"
"    border-style: inset;\n"
"    background: #5d0003;\n"
"}\n"
"\n"
"\n"
"")

        # Ses seviyesi label'ının ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.ui.label.setFont(font)
        self.ui.label.setStyleSheet("QLabel {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #630001;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: #820002;\n"
"    }\n"
"")
        # Çalma slider'ının ayarlanması
        self.ui.PlaySlider.setMouseTracking(False)
        self.ui.PlaySlider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ui.PlaySlider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: black;\n"
"height: 4px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background:  qlineargradient(spread:pad, x1:0.488636, y1:1, x2:0.483, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.534091 rgba(255, 0, 0, 255));\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal {\n"
"border: 2px solid qlineargradient(spread:pad, x1:0.523, y1:0, x2:0.517, y2:1, stop:0.590909 rgba(0, 0, 0, 255), stop:1 rgba(255, 18, 18, 255));\n"
"height: 10px;\n"
"border-radius: 2.5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background-color: #820002;\n"
"border: 1px solid #630001;\n"
"width: 17px;\n"
"height: 30px;\n"
"margin-top: -7px;\n"
"margin-bottom: -7px;\n"
"border-radius: 9px;\n"
"border-style: outset;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background-color: #720002;\n"
"border: 1px solid #630001;\n"
"width: 17px;\n"
"height: 30px;\n"
"margin-top: -7px;\n"
"margin-bottom: -7px;\n"
"border-radius: 9px;\n"
"border-style: outset;\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed{\n"
"    border-style: inset;\n"
"    background: #5d0003;\n"
"}\n"
"\n"
"\n"
"")

        # İleri al tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.ui.Forward.setFont(font)
        self.ui.Forward.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #630001;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: #820002;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: #720002;\n"
"    border: 2px solid #630001;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: #5d0003\n"
"    }")


        # Geri al tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.ui.Backward.setFont(font)
        self.ui.Backward.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #630001;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: #820002;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: #720002;\n"
"    border: 2px solid #630001;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: #5d0003\n"
"    }")

        # Zaman göstergesinin ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(9)
        self.ui.fullTime.setFont(font)
        self.ui.fullTime.setStyleSheet("")
        font.setFamily("Yu Gothic UI")
        font.setPointSize(9)
        self.ui.time.setFont(font)
        self.ui.time.setStyleSheet("")
        self.ui.time.setObjectName("time")

        # Şarkı listesi'nin ayarlanması
        self.ui.songs_list.setMinimumSize(QtCore.QSize(781, 0))
        self.ui.songs_list.setStyleSheet("QWidget {\n"
"    background-color: #420000;\n"
"    color: #000000;\n"
"    border-radius: 3px;\n"
"}\n"
"QTableView {\n"
"    selection-background-color: #980002;\n"
"    color: #c2c2c2;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #720002;\n"
"    border: 1px solid #630001;\n"
"    border-radius: 2px;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: #630001;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #720002;\n"
"    border: 1px solid  #630001;\n"
"    border-radius: 2px;\n"
"}")
        self.ui.songs_list.setLineWidth(1)
        self.ui.songs_list.setMidLineWidth(1)
        self.ui.songs_list.setObjectName("songs_list")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(8)
        font.setUnderline(False)
        item.setFont(font)
        self.ui.songs_list.setHorizontalHeaderItem(0, item)
        if self.song.isAdded:  
            self.ui.songs_list.horizontalHeader().setDefaultSectionSize(736)
        else:
            self.ui.songs_list.horizontalHeader().setDefaultSectionSize(780)

        # Şarkıları ekle tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.ui.find_path.setFont(font)
        self.ui.find_path.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #630001;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: #820002;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: #720002;\n"
"    border: 2px solid #630001;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: #5d0003\n"
"    }")

        # Hakkımızda tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.ui.about_us.setFont(font)
        self.ui.about_us.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #630001;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: #820002;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: #720002;\n"
"    border: 2px solid #630001;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: #5d0003\n"
"    }")

        # Tema tuşunun ayarlanması
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setFamily("Yu Gothic UI")
        self.ui.BlackBull.setFont(font)
        self.ui.BlackBull.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #630001;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: #820002;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: #720002;\n"
"    border: 2px solid #630001;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: #5d0003\n"
"    }")

        #Temalar label'ının ayarlanması
        self.themes = QtWidgets.QLabel(self.Frame)
        self.themes.setStyleSheet("color:#c2c2c2;")
        self.themes.setObjectName("themes")

        # Default tema tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.ui.Default.setFont(font)
        self.ui.Default.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #630001;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: #820002;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: #720002;\n"
"    border: 2px solid #630001;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: #5d0003\n"
"    }")

        # Alp'in temasına geçen tuşun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.ui.Indian_Rush.setFont(font)
        self.ui.Indian_Rush.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #630001;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: #820002;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: #720002;\n"
"    border: 2px solid #630001;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: #5d0003\n"
"    }")


        # White Chocolate tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.ui.White_Chocolate.setFont(font)
        self.ui.White_Chocolate.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #630001;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: #820002;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: #720002;\n"
"    border: 2px solid #630001;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: #5d0003\n"
"    }")

        # İsim değişiklikleri'nin yapılması
        _translate = QtCore.QCoreApplication.translate
        self.Frame.setWindowTitle(_translate("Frame", "Mp3 Oynatıcı"))
        self.ui.nextButton.setText(_translate("Frame", ">>|"))
        self.ui.backButton.setText(_translate("Frame", "|<<"))
        self.ui.Shuffle.setText(_translate("Frame", "Shuffle"))
        self.ui.label.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Ses Seviyesi</p></body></html>"))
        self.ui.time.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.ui.Backward.setText(_translate("Frame", "↩"))
        self.ui.Forward.setText(_translate("Frame", "↪"))
        self.ui.fullTime.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        item = self.ui.songs_list.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "Şarkı İsmi"))
        self.ui.find_path.setText(_translate("Frame", "Şarkıları Ekle"))
        self.ui.about_us.setText(_translate("Frame", "Hakkımızda"))
        self.ui.BlackBull.setText(_translate("Frame", "BlackBull"))
        self.ui.themes.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color: #c2c2c2\">Temalar</span></p></body></html>"))
 

    def BlackBull(self):
        # Veri tabanına son kullanılan temayı ekleme
        self.theme = "BlackBull"
        theme_changer.theme = self.theme
        with sqlite3.connect(self.DB_DIR) as db:
                cur = db.cursor()
                cmd = "DELETE FROM theme"
                cur.execute(cmd)
                cmd = "INSERT INTO theme VALUES ('{}')".format(self.theme)
                cur.execute(cmd)

        # Frame'in ayarlanması
        self.Frame.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);\n"
"border-color: rgb(80, 80, 80);\n"
"background-color: rgb(136, 136, 136);\n"
"background-color: rgb(24, 24, 24);")
        self.ui.frame.setStyleSheet("background-color: rgb(33, 33, 33);\n")

        # Rose tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.ui.Bleeding_Rose.setFont(font)
        self.ui.Bleeding_Rose.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #313131;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  rgb(50, 50, 50);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(30, 30, 30);\n"
"    border: 2px solid #2a2a2a;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(15, 15, 15);\n"
"    }")

        # Play tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(20)
        self.ui.play.setFont(font)
        self.ui.play.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #313131;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background:  rgb(50, 50, 50);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(30, 30, 30);\n"
"    border: 2px solid #2a2a2a;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(15, 15, 15);\n"
"    }")

        # Now Playing kısmının ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.ui.nowPlaying.setFont(font)
        self.ui.nowPlaying.setStyleSheet("background-color:  rgb(75, 75, 75);\n"
"color: #c2c2c2;\n"
"border: 2px solid #313131;\n"
"border-radius: 5px;\n"
"border-style: outset;\n"
"")

        # İleri Tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ui.nextButton.setFont(font)
        self.ui.nextButton.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #313131;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  rgb(50, 50, 50);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(30, 30, 30);\n"
"    border: 2px solid #2a2a2a;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(15, 15, 15);\n"
"    }")

        # Geri tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.ui.backButton.setFont(font)
        self.ui.backButton.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #313131;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  rgb(50, 50, 50);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(30, 30, 30);\n"
"    border: 2px solid #2a2a2a;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(15, 15, 15);\n"
"    }")

        # Shuffle tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.ui.Shuffle.setFont(font)
        self.ui.Shuffle.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #313131;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  rgb(50, 50, 50);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(75, 75, 75);\n"
"    }\n"
"\n"
"QPushButton:checked {\n"
"    border-style: inset;\n"
"    background: rgb(55, 55, 55);\n"
"    }")

        # Ses seviyesi slider'ının ayarlanması
        self.ui.SoundSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 4px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #151515, stop: 1 #505050);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 3px solid #777;\n"
"height: 10px;\n"
"border-radius: 2.5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background-color: rgb(50, 50, 50);\n"
"border: 1px solid #313131;;\n"
"width: 17px;\n"
"height: 30px;\n"
"margin-top: -7px;\n"
"margin-bottom: -7px;\n"
"border-radius: 9px;\n"
"border-style: outset;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background-color: rgb(30, 30, 30);\n"
"border: 1px solid #2a2a2a;\n"
"width: 17px;\n"
"height: 30px;\n"
"margin-top: -7px;\n"
"margin-bottom: -7px;\n"
"border-radius: 9px;\n"
"border-style: outset;\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed{\n"
"    border-style: inset;\n"
"    background: rgb(15, 15, 15);\n"
"}\n"
"\n"
"\n"
"")

        # Ses seviyesi label'ının ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.ui.label.setFont(font)
        self.ui.label.setStyleSheet("QLabel {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #313131;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  rgb(50, 50, 50);\n"
"    }\n"
"")

        # Çalma slider'ının ayarlanması
        self.ui.PlaySlider.setMouseTracking(False)
        self.ui.PlaySlider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ui.PlaySlider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 4px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #151515, stop: 1 #505050);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 3px solid #777;\n"
"height: 10px;\n"
"border-radius: 2.5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background-color: rgb(50, 50, 50);\n"
"border: 1px solid #313131;;\n"
"width: 17px;\n"
"height: 30px;\n"
"margin-top: -7px;\n"
"margin-bottom: -7px;\n"
"border-radius: 9px;\n"
"border-style: outset;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background-color: rgb(30, 30, 30);\n"
"border: 1px solid #2a2a2a;\n"
"width: 17px;\n"
"height: 30px;\n"
"margin-top: -7px;\n"
"margin-bottom: -7px;\n"
"border-radius: 9px;\n"
"border-style: outset;\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed{\n"
"    border-style: inset;\n"
"    background: rgb(15, 15, 15);\n"
"}\n"
"\n"
"\n"
"")

        # İleri al tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.ui.Forward.setFont(font)
        self.ui.Forward.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #313131;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  rgb(50, 50, 50);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(30, 30, 30);\n"
"    border: 2px solid #2a2a2a;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(15, 15, 15);\n"
"    }")


        # Geri al tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.ui.Backward.setFont(font)
        self.ui.Backward.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #313131;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  rgb(50, 50, 50);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(30, 30, 30);\n"
"    border: 2px solid #2a2a2a;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(15, 15, 15);\n"
"    }")

        # Zaman göstergesinin ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(9)
        self.ui.fullTime.setFont(font)
        self.ui.fullTime.setStyleSheet("")
        font.setFamily("Yu Gothic UI")
        font.setPointSize(9)
        self.ui.time.setFont(font)
        self.ui.time.setStyleSheet("")
        self.ui.time.setObjectName("time")

        # Şarkı listesi'nin ayarlanması
        self.ui.songs_list.setMinimumSize(QtCore.QSize(781, 0))
        self.ui.songs_list.setStyleSheet("QWidget {\n"
"    background-color: #313131;\n"
"    color: #c2c2c2;\n"
"    border-radius: 3px;\n"
"}\n"
"QTableView {\n"
"    selection-background-color: #9c9c9c;\n"
"    color: #c2c2c2;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(100, 100, 100);\n"
"    border: 1px solid #181818;\n"
"    border-radius: 1px;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: #272727;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #646464;\n"
"    border: 1px solid #272727;\n"
"    border-radius: 2px;\n"
"}")
        self.ui.songs_list.setLineWidth(1)
        self.ui.songs_list.setMidLineWidth(1)
        self.ui.songs_list.setObjectName("songs_list")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(8)
        font.setUnderline(False)
        item.setFont(font)
        self.ui.songs_list.setHorizontalHeaderItem(0, item)
        if self.song.isAdded:  
            self.ui.songs_list.horizontalHeader().setDefaultSectionSize(736)
        else:
            self.ui.songs_list.horizontalHeader().setDefaultSectionSize(780)

        # Şarkıları ekle tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.ui.find_path.setFont(font)
        self.ui.find_path.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #313131;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  rgb(50, 50, 50);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(30, 30, 30);\n"
"    border: 2px solid #2a2a2a;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(15, 15, 15);\n"
"    }")

        # Hakkımızda tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.ui.about_us.setFont(font)
        self.ui.about_us.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #313131;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  rgb(50, 50, 50);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(30, 30, 30);\n"
"    border: 2px solid #2a2a2a;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(15, 15, 15);\n"
"    }")

        # Tema tuşunun ayarlanması
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setFamily("Yu Gothic UI")
        self.ui.BlackBull.setFont(font)
        self.ui.BlackBull.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #313131;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  rgb(50, 50, 50);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(30, 30, 30);\n"
"    border: 2px solid #2a2a2a;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(15, 15, 15);\n"
"    }")

        #Temalar label'ının ayarlanması
        self.themes = QtWidgets.QLabel(self.Frame)
        self.themes.setStyleSheet("color:#c2c2c2;")
        self.themes.setObjectName("themes")

        # Default tema tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.ui.Default.setFont(font)
        self.ui.Default.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #313131;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  rgb(50, 50, 50);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(30, 30, 30);\n"
"    border: 2px solid #2a2a2a;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(15, 15, 15);\n"
"    }")

        # Alp'in temasına geçen tuşun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.ui.Indian_Rush.setFont(font)
        self.ui.Indian_Rush.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #313131;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  rgb(50, 50, 50);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(30, 30, 30);\n"
"    border: 2px solid #2a2a2a;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(15, 15, 15);\n"
"    }")


        # White Chocolate tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.ui.White_Chocolate.setFont(font)
        self.ui.White_Chocolate.setStyleSheet("QPushButton {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #313131;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  rgb(50, 50, 50);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(30, 30, 30);\n"
"    border: 2px solid #2a2a2a;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(15, 15, 15);\n"
"    }")

        # İsim değişiklikleri'nin yapılması
        _translate = QtCore.QCoreApplication.translate
        self.Frame.setWindowTitle(_translate("Frame", "Mp3 Oynatıcı"))
        self.ui.nextButton.setText(_translate("Frame", ">>|"))
        self.ui.backButton.setText(_translate("Frame", "|<<"))
        self.ui.Shuffle.setText(_translate("Frame", "Shuffle"))
        self.ui.label.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Ses Seviyesi</p></body></html>"))
        self.ui.time.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.ui.Backward.setText(_translate("Frame", "↩"))
        self.ui.Forward.setText(_translate("Frame", "↪"))
        self.ui.fullTime.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        item = self.ui.songs_list.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "Şarkı İsmi"))
        self.ui.find_path.setText(_translate("Frame", "Şarkıları Ekle"))
        self.ui.about_us.setText(_translate("Frame", "Hakkımızda"))
        self.ui.BlackBull.setText(_translate("Frame", "BlackBull"))
        self.ui.themes.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color: #c2c2c2\">Temalar</span></p></body></html>"))

    def Default(self):
        # Veri tabanına son kullanılan temayı ekleme
        self.theme = "default"
        theme_changer.theme = self.theme
        with sqlite3.connect(self.DB_DIR) as db:
                cur = db.cursor()
                cmd = "DELETE FROM theme"
                cur.execute(cmd)
                cmd = "INSERT INTO theme VALUES ('{}')".format(self.theme)
                cur.execute(cmd)

        # Frame'in ayarlanması
        self.Frame.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);\n"
"border-color: rgb(80, 80, 80);\n"
"background-color: rgb(136, 136, 136);")
        self.ui.frame.setStyleSheet("background-color: rgb(71, 71, 71);\n"
"")

        # Play tuşunun ayarlanması
        font = QtGui.QFont()
        font.setPointSize(22)
        self.ui.play.setFont(font)
        self.ui.play.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")

        # Now Playing kısmının ayarlanması
        self.ui.nowPlaying.setStyleSheet("background-color: rgb(157, 157, 157);\n"
"border: 2px solid #555;\n"
"border-radius: 5px;\n"
"border-style: outset;")

        # İleri Tuşunun ayarlanması
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ui.nextButton.setFont(font)
        self.ui.nextButton.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")

        # Geri tuşunun ayarlanması
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.ui.backButton.setFont(font)
        self.ui.backButton.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius:5px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")

        # Shuffle tuşunun ayarlanması
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.ui.Shuffle.setFont(font)
        self.ui.Shuffle.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:checked {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")

        # Ses seviyesi slider'ının ayarlanması
        self.ui.SoundSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #005f00, stop: 1 #66ff00);\n"
"\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background-color: rgb(11, 144, 27);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")

        # Ses seviyesi label'ının ayarlanması
        self.ui.label.setStyleSheet("QLabel {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    }\n"
"")

        # Çalma slider'ının ayarlanması
        self.ui.PlaySlider.setMouseTracking(False)
        self.ui.PlaySlider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ui.PlaySlider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 5px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #151515, stop: 1 #505050);\n"
"\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 3px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid #777;\n"
"width: 17px;\n"
"height: 30px;\n"
"margin-top: -7px;\n"
"margin-bottom: -7px;\n"
"border-radius: 9px;\n"
"}\n"
"\n"
"\n"
"")

        # İleri al tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.ui.Forward.setFont(font)
        self.ui.Forward.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")


        # Geri al tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.ui.Backward.setFont(font)
        self.ui.Backward.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")


        # Zaman göstergesinin ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(9)
        self.ui.fullTime.setFont(font)
        self.ui.fullTime.setStyleSheet("")
        

        # Şarkı listesi'nin ayarlanması
        self.ui.songs_list.setMinimumSize(QtCore.QSize(781, 0))
        self.ui.songs_list.setStyleSheet("\n"
"background-color: rgb(193, 193, 193);")
        self.ui.songs_list.setLineWidth(1)
        self.ui.songs_list.setMidLineWidth(1)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(8)
        font.setUnderline(False)
        item.setFont(font)
        self.ui.songs_list.setHorizontalHeaderItem(0, item)
        if self.song.isAdded:  
            self.ui.songs_list.horizontalHeader().setDefaultSectionSize(730)
        else:
            self.ui.songs_list.horizontalHeader().setDefaultSectionSize(780)

        # Şarkıları ekle tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(8)
        self.ui.find_path.setFont(font)
        self.ui.find_path.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")

        # Hakkımızda tuşunun ayarlanması
        self.ui.about_us.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")

        # Tema tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.ui.BlackBull.setFont(font)
        self.ui.BlackBull.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")

        # Rose tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.ui.Bleeding_Rose.setFont(font)
        self.ui.Bleeding_Rose.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")

        #Temalar label'ının ayarlanması
        self.themes = QtWidgets.QLabel(self.Frame)
        self.themes.setStyleSheet("color:#c2c2c2;")
        self.themes.setObjectName("themes")

        # Default tema tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.ui.Default.setFont(font)
        self.ui.Default.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")

        # Alp'in temasına geçen tuşun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.ui.Indian_Rush.setFont(font)
        self.ui.Indian_Rush.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")

        # White Chocolate tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.ui.White_Chocolate.setFont(font)
        self.ui.White_Chocolate.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")

        # İsim değişiklikleri'nin yapılması
        _translate = QtCore.QCoreApplication.translate
        self.Frame.setWindowTitle(_translate("Frame", "Mp3 Oynatıcı"))
        self.ui.nextButton.setText(_translate("Frame", ">>|"))
        self.ui.backButton.setText(_translate("Frame", "|<<"))
        self.ui.Shuffle.setText(_translate("Frame", "Shuffle"))
        self.ui.label.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Ses Seviyesi</p></body></html>"))
        self.ui.time.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.ui.Backward.setText(_translate("Frame", "↩"))
        self.ui.Forward.setText(_translate("Frame", "↪"))
        self.ui.fullTime.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        item = self.ui.songs_list.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "Şarkı İsmi"))
        self.ui.find_path.setText(_translate("Frame", "Şarkıları Ekle"))
        self.ui.about_us.setText(_translate("Frame", "Hakkımızda"))
        self.ui.BlackBull.setText(_translate("Frame", "BlackBull"))
        self.ui.themes.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color: #c2c2c2\">Temalar</span></p></body></html>"))

    def Indian_Rush(self):
        # Veri tabanına son kullanılan temayı ekleme
        self.theme = "Indian Rush"
        theme_changer.theme = self.theme
        with sqlite3.connect(self.DB_DIR) as db:
                cur = db.cursor()
                cmd = "DELETE FROM theme"
                cur.execute(cmd)
                cmd = "INSERT INTO theme VALUES ('{}')".format(self.theme)
                cur.execute(cmd)

        # Frame'in ayarlanması
        self.Frame.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
"gridline-color: rgb(0, 0, 0);\n"
"border-color: rgb(80, 80, 80);\n"
"")
        self.ui.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")

        # Play tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(20)
        self.ui.play.setFont(font)
        self.ui.play.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")

        # Now Playing kısmının ayarlanması
        self.ui.nowPlaying.setStyleSheet("background-color: rgb(157, 157, 157);")

        # İleri Tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ui.nextButton.setFont(font)
        self.ui.nextButton.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")

        # Geri tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.ui.backButton.setFont(font)
        self.ui.backButton.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")

        # Shuffle tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.ui.Shuffle.setFont(font)
        self.ui.Shuffle.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:checked {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")

        # Ses seviyesi slider'ının ayarlanması
        self.ui.SoundSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #005f00, stop: 1 #66ff00);\n"
"\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background-color: rgb(11, 144, 27);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")

        # Ses seviyesi label'ının ayarlanması
        self.ui.label.setStyleSheet("QLabel {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    }\n"
"")

        # Çalma slider'ının ayarlanması
        self.ui.PlaySlider.setMouseTracking(False)
        self.ui.PlaySlider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ui.PlaySlider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 5px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #151515, stop: 1 #505050);\n"
"\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid #777;\n"
"width: 17px;\n"
"height: 30px;\n"
"margin-top: -7px;\n"
"margin-bottom: -7px;\n"
"border-radius: 9px;\n"
"}\n"
"\n"
"\n"
"")

        # İleri al tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.ui.Forward.setFont(font)
        self.ui.Forward.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")


        # Geri al tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.ui.Backward.setFont(font)
        self.ui.Backward.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")


        # Zaman göstergesinin ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(9)
        self.ui.fullTime.setFont(font)
        self.ui.fullTime.setStyleSheet("background-color: rgb(255, 255, 255);")
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(9)
        self.ui.time.setFont(font)
        self.ui.time.setStyleSheet("background-color: rgb(255, 255, 255);")
        

        # Şarkı listesi'nin ayarlanması
        self.ui.songs_list.setMinimumSize(QtCore.QSize(781, 0))
        self.ui.songs_list.setStyleSheet("\n"
"background-color: rgb(125, 125, 125);")
        self.ui.songs_list.setLineWidth(1)
        self.ui.songs_list.setMidLineWidth(1)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(8)
        font.setUnderline(False)
        item.setFont(font)
        self.ui.songs_list.setHorizontalHeaderItem(0, item)
        if self.song.isAdded:  
            self.ui.songs_list.horizontalHeader().setDefaultSectionSize(730)
        else:
            self.ui.songs_list.horizontalHeader().setDefaultSectionSize(780)

        # Şarkıları ekle tuşunun ayarlanması
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ui.find_path.setFont(font)
        self.ui.find_path.setStyleSheet("QPushButton {\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:7px;\n"
"}")

        # Hakkımızda tuşunun ayarlanması
        self.ui.about_us.setStyleSheet("QPushButton {\n"
"\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:7px;\n"
"}")

        # Tema tuşunun ayarlanması
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(20)
        self.ui.BlackBull.setFont(font)
        self.ui.BlackBull.setStyleSheet("QPushButton {\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:12px;\n"
"}")

        # Rose tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.ui.Bleeding_Rose.setFont(font)
        self.ui.Bleeding_Rose.setStyleSheet("QPushButton {\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:12px;\n"
"}")

        #Temalar label'ının ayarlanması
        self.themes = QtWidgets.QLabel(self.Frame)
        self.themes.setStyleSheet("color:#c2c2c2;")
        self.themes.setObjectName("themes")

        # Default tema tuşunun ayarlanması
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(20)
        self.ui.Default.setFont(font)
        self.ui.Default.setStyleSheet("QPushButton {\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:12px;\n"
"}")

        # HİNTLİ TELAŞININ AYARLANMASI
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(20)
        self.ui.Indian_Rush.setFont(font)
        self.ui.Indian_Rush.setStyleSheet("QPushButton {\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:12px;\n"
"}")

        # White Chocolate tuşunun ayarlanması
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(20)
        self.ui.White_Chocolate.setFont(font)
        self.ui.White_Chocolate.setStyleSheet("QPushButton {\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:12px;\n"
"}")


        # İsim değişiklikleri'nin yapılması
        _translate = QtCore.QCoreApplication.translate
        self.Frame.setWindowTitle(_translate("Frame", "Mp3 Oynatıcı"))
        self.ui.nextButton.setText(_translate("Frame", ">>|"))
        self.ui.backButton.setText(_translate("Frame", "|<<"))
        self.ui.Shuffle.setText(_translate("Frame", "Shuffle"))
        self.ui.label.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Ses Seviyesi</p></body></html>"))
        self.ui.time.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.ui.Backward.setText(_translate("Frame", "↩"))
        self.ui.Forward.setText(_translate("Frame", "↪"))
        self.ui.fullTime.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        item = self.ui.songs_list.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "Şarkı İsmi"))
        self.ui.about_us.setText(_translate("Frame", "Hakkımızda"))
        self.ui.BlackBull.setText(_translate("Frame", "BlackBull"))
        self.themes.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:c2c2c2;\">Temalar</span></p></body></html>"))
        self.ui.find_path.setText(_translate("Frame", "Şarkıları Ekle"))
        self.ui.Default.setText(_translate("Frame", "Default"))
        self.ui.Indian_Rush.setText(_translate("Frame", "Indian Rush"))
        
    def White_Chocolate(self):
        # Veri tabanına son kullanılan temayı ekleme
        self.theme = "White Chocolate"
        theme_changer.theme = self.theme
        with sqlite3.connect(self.DB_DIR) as db:
                cur = db.cursor()
                cmd = "DELETE FROM theme"
                cur.execute(cmd)
                cmd = "INSERT INTO theme VALUES ('{}')".format(self.theme)
                cur.execute(cmd)

        # Frame'in ayarlanması
        self.Frame.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);\n"
"border-color: rgb(80, 80, 80);\n"
"background-color: rgb(220, 220, 220);\n"
"")
        self.ui.frame.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"")

        # Play tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(20)
        self.ui.play.setFont(font)
        self.ui.play.setStyleSheet("QPushButton {\n"
"    color: rgb(50, 50, 50);\n"
"    border: 2px solid #c2c2c2;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background:  #cccccc;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(214, 214, 214);\n"
"    border: 2px solid  rgb(165, 165, 165);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(240, 240, 240);\n"
"    }")

        # Now Playing kısmının ayarlanması
        self.ui.nowPlaying.setStyleSheet("background-color: #cccccc;\n"
"color: rgb(50, 50, 50);\n"
"border: 2px solid #c2c2c2;\n"
"border-radius: 5px;\n"
"border-style: outset;\n"
"")

        # İleri Tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ui.nextButton.setFont(font)
        self.ui.nextButton.setStyleSheet("QPushButton {\n"
"    color: rgb(50, 50, 50);\n"
"    border: 2px solid #c2c2c2;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  #cccccc;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(214, 214, 214);\n"
"    border: 2px solid  rgb(165, 165, 165);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(240, 240, 240);\n"
"    }")

        # Geri tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.ui.backButton.setFont(font)
        self.ui.backButton.setStyleSheet("QPushButton {\n"
"    color: rgb(50, 50, 50);\n"
"    border: 2px solid #c2c2c2;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  #cccccc;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(214, 214, 214);\n"
"    border: 2px solid  rgb(165, 165, 165);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(240, 240, 240);\n"
"    }")

        # Shuffle tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.ui.Shuffle.setFont(font)
        self.ui.Shuffle.setStyleSheet("QPushButton {\n"
"    color: rgb(50, 50, 50);\n"
"    border: 2px solid #c2c2c2;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  #cccccc;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(214, 214, 214);\n"
"    border: 2px solid  rgb(165, 165, 165);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(240, 240, 240);\n"
"    }")

        # Ses seviyesi slider'ının ayarlanması
        self.ui.SoundSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid rgb(50, 50, 50);\n"
"background: black;\n"
"height: 4px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(spread:pad, x1:0.415, y1:1, x2:0.409, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.238636 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #000000;\n"
"border: 3px solid #c2c2c2;\n"
"height: 10px;\n"
"border-radius: 2.5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background-color:#cccccc;\n"
"border: 1px solid #bfbfbf;\n"
"width: 17px;\n"
"height: 30px;\n"
"margin-top: -7px;\n"
"margin-bottom: -7px;\n"
"border-radius: 9px;\n"
"border-style: outset;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background-color: rgb(214, 214, 214);\n"
"border: 1px solid rgb(165, 165, 165);\n"
"width: 17px;\n"
"height: 30px;\n"
"margin-top: -7px;\n"
"margin-bottom: -7px;\n"
"border-radius: 9px;\n"
"border-style: outset;\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed{\n"
"    border-style: inset;\n"
"    background: rgb(240, 240, 240);\n"
"}\n"
"\n"
"\n"
"")

        # Ses seviyesi label'ının ayarlanması
        self.ui.label.setStyleSheet("QLabel {\n"
"    color: rgb(50, 50, 50);\n"
"    border: 2px solid #c2c2c2;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  #cccccc;\n"
"}\n")

        # Çalma slider'ının ayarlanması
        self.ui.PlaySlider.setMouseTracking(False)
        self.ui.PlaySlider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ui.PlaySlider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid rgb(50, 50, 50);\n"
"background: black;\n"
"height: 4px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(spread:pad, x1:0.415, y1:1, x2:0.409, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.238636 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #000000;\n"
"border: 3px solid #c2c2c2;\n"
"height: 10px;\n"
"border-radius: 2.5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background-color:#cccccc;\n"
"border: 1px solid #bfbfbf;\n"
"width: 17px;\n"
"height: 30px;\n"
"margin-top: -7px;\n"
"margin-bottom: -7px;\n"
"border-radius: 9px;\n"
"border-style: outset;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background-color: rgb(214, 214, 214);\n"
"border: 1px solid rgb(165, 165, 165);\n"
"width: 17px;\n"
"height: 30px;\n"
"margin-top: -7px;\n"
"margin-bottom: -7px;\n"
"border-radius: 9px;\n"
"border-style: outset;\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed{\n"
"    border-style: inset;\n"
"    background: rgb(240, 240, 240);\n"
"}\n"
"\n"
"\n"
"")

        # İleri al tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.ui.Forward.setFont(font)
        self.ui.Forward.setStyleSheet("QPushButton {\n"
"    color: rgb(50, 50, 50);\n"
"    border: 2px solid #c2c2c2;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  #cccccc;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(214, 214, 214);\n"
"    border: 2px solid  rgb(165, 165, 165);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(240, 240, 240);\n"
"    }")


        # Geri al tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.ui.Backward.setFont(font)
        self.ui.Backward.setStyleSheet("QPushButton {\n"
"    color: rgb(50, 50, 50);\n"
"    border: 2px solid #c2c2c2;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  #cccccc;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(214, 214, 214);\n"
"    border: 2px solid  rgb(165, 165, 165);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(240, 240, 240);\n"
"    }")


        # Zaman göstergesinin ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(9)
        self.ui.fullTime.setFont(font)
        self.ui.fullTime.setStyleSheet("")
        

        # Şarkı listesi'nin ayarlanması
        self.ui.songs_list.setMinimumSize(QtCore.QSize(781, 0))
        self.ui.songs_list.setStyleSheet("QWidget {\n"
"    background-color: #c5c5c5;\n"
"    color: rgb(50, 50, 50);\n"
"    border-radius: 3px;\n"
"}\n"
"QTableView {\n"
"    selection-background-color: #9c9c9c;\n"
"    color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #cccccc;\n"
"    border: 1px solid rgb(165, 165, 165);\n"
"    border-radius: 2px;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: #a2a2a2;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #cccccc;\n"
"    border: 1px solid rgb(165, 165, 165);\n"
"    border-radius: 2px;\n"
"}")
        self.ui.songs_list.setLineWidth(1)
        self.ui.songs_list.setMidLineWidth(1)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(8)
        font.setUnderline(False)
        item.setFont(font)
        self.ui.songs_list.setHorizontalHeaderItem(0, item)
        if self.song.isAdded:  
            self.ui.songs_list.horizontalHeader().setDefaultSectionSize(730)
        else:
            self.ui.songs_list.horizontalHeader().setDefaultSectionSize(780)

        # Şarkıları ekle tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.ui.find_path.setFont(font)
        self.ui.find_path.setStyleSheet("QPushButton {\n"
"    color: rgb(50, 50, 50);\n"
"    border: 2px solid #c2c2c2;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  #cccccc;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(214, 214, 214);\n"
"    border: 2px solid  rgb(165, 165, 165);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(240, 240, 240);\n"
"    }")

        # Hakkımızda tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.ui.about_us.setFont(font)
        self.ui.about_us.setStyleSheet("QPushButton {\n"
"    color: rgb(50, 50, 50);\n"
"    border: 2px solid #c2c2c2;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  #cccccc;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(214, 214, 214);\n"
"    border: 2px solid  rgb(165, 165, 165);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(240, 240, 240);\n"
"    }")

        # Tema tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.ui.BlackBull.setFont(font)
        self.ui.BlackBull.setStyleSheet("QPushButton {\n"
"    color: rgb(50, 50, 50);\n"
"    border: 2px solid #c2c2c2;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  #cccccc;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(214, 214, 214);\n"
"    border: 2px solid  rgb(165, 165, 165);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(240, 240, 240);\n"
"    }")

        # Rose tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.ui.Bleeding_Rose.setFont(font)
        self.ui.Bleeding_Rose.setStyleSheet("QPushButton {\n"
"    color: rgb(50, 50, 50);\n"
"    border: 2px solid #c2c2c2;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  #cccccc;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(214, 214, 214);\n"
"    border: 2px solid  rgb(165, 165, 165);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(240, 240, 240);\n"
"    }")

        #Temalar label'ının ayarlanması
        self.themes = QtWidgets.QLabel(self.Frame)
        self.themes.setStyleSheet("")
        self.themes.setObjectName("themes")

        # Default tema tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.ui.Default.setFont(font)
        self.ui.Default.setStyleSheet("QPushButton {\n"
"    color: rgb(50, 50, 50);\n"
"    border: 2px solid #c2c2c2;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  #cccccc;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(214, 214, 214);\n"
"    border: 2px solid  rgb(165, 165, 165);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(240, 240, 240);\n"
"    }")

        # Alp'in temasına geçen tuşun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.ui.Indian_Rush.setFont(font)
        self.ui.Indian_Rush.setStyleSheet("QPushButton {\n"
"    color: rgb(50, 50, 50);\n"
"    border: 2px solid #c2c2c2;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  #cccccc;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(214, 214, 214);\n"
"    border: 2px solid  rgb(165, 165, 165);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(240, 240, 240);\n"
"    }")

        # White Chocolate tuşunun ayarlanması
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.ui.White_Chocolate.setFont(font)
        self.ui.White_Chocolate.setStyleSheet("QPushButton {\n"
"    color: rgb(50, 50, 50);\n"
"    border: 2px solid #c2c2c2;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  #cccccc;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:  rgb(214, 214, 214);\n"
"    border: 2px solid  rgb(165, 165, 165);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(240, 240, 240);\n"
"    }")


        # translate işlemi işte üşendim resmi yazmaya
        _translate = QtCore.QCoreApplication.translate
        self.Frame.setWindowTitle(_translate("Frame", "Mp3 Oynatıcı"))
        self.ui.nextButton.setText(_translate("Frame", ">>|"))
        self.ui.backButton.setText(_translate("Frame", "|<<"))
        self.ui.Shuffle.setText(_translate("Frame", "Shuffle"))
        self.ui.label.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Ses Seviyesi</p></body></html>"))
        self.ui.time.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.ui.Backward.setText(_translate("Frame", "↩"))
        self.ui.Forward.setText(_translate("Frame", "↪"))
        self.ui.fullTime.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        item = self.ui.songs_list.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "Şarkı İsmi"))
        self.ui.about_us.setText(_translate("Frame", "Hakkımızda"))
        self.ui.BlackBull.setText(_translate("Frame", "BlackBull"))
        self.ui.themes.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color: #000000\">Temalar</span></p></body></html>"))
        self.ui.find_path.setText(_translate("Frame", "Şarkıları Ekle"))
        self.ui.Default.setText(_translate("Frame", "Default"))
        self.ui.Indian_Rush.setText(_translate("Frame", "Indian Rush"))
        self.ui.White_Chocolate.setText(_translate("Frame", "White Chocolate"))

