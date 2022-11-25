# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setWindowModality(QtCore.Qt.ApplicationModal)
        Frame.setEnabled(True)
        Frame.resize(1214, 669)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        Frame.setMinimumSize(QtCore.QSize(1214, 669))
        Frame.setMaximumSize(QtCore.QSize(1214, 669))
        Frame.setAutoFillBackground(False)
        Frame.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);\n"
"border-color: rgb(80, 80, 80);\n"
"background-color: rgb(136, 136, 136);")
        self.frame = QtWidgets.QFrame(Frame)
        self.frame.setGeometry(QtCore.QRect(0, 570, 1221, 101))
        self.frame.setStyleSheet("background-color: rgb(71, 71, 71);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.play = QtWidgets.QPushButton(self.frame)
        self.play.setGeometry(QtCore.QRect(560, 50, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.play.setFont(font)
        self.play.setStyleSheet("QPushButton {\n"
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
        self.play.setText("▶")
        self.play.setObjectName("play")
        self.nowPlaying = QtWidgets.QLineEdit(self.frame)
        self.nowPlaying.setGeometry(QtCore.QRect(340, 19, 501, 21))
        self.nowPlaying.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.nowPlaying.setText("")
        self.nowPlaying.setReadOnly(True)
        self.nowPlaying.setObjectName("nowPlaying")
        self.nextButton = QtWidgets.QPushButton(self.frame)
        self.nextButton.setGeometry(QtCore.QRect(620, 50, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.nextButton.setFont(font)
        self.nextButton.setStyleSheet("QPushButton {\n"
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
        self.nextButton.setObjectName("nextButton")
        self.backButton = QtWidgets.QPushButton(self.frame)
        self.backButton.setGeometry(QtCore.QRect(510, 50, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("QPushButton {\n"
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
        self.backButton.setObjectName("backButton")
        self.Shuffle = QtWidgets.QPushButton(self.frame)
        self.Shuffle.setGeometry(QtCore.QRect(440, 50, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.Shuffle.setFont(font)
        self.Shuffle.setStyleSheet("QPushButton {\n"
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
        self.Shuffle.setCheckable(True)
        self.Shuffle.setObjectName("Shuffle")
        self.SoundSlider = QtWidgets.QSlider(self.frame)
        self.SoundSlider.setGeometry(QtCore.QRect(1000, 60, 160, 22))
        self.SoundSlider.setStyleSheet("QSlider::groove:horizontal {\n"
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
        self.SoundSlider.setMaximum(100)
        self.SoundSlider.setProperty("value", 100)
        self.SoundSlider.setSliderPosition(100)
        self.SoundSlider.setOrientation(QtCore.Qt.Horizontal)
        self.SoundSlider.setObjectName("SoundSlider")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(1050, 40, 71, 16))
        self.label.setStyleSheet("QLabel {\n"
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
        self.label.setObjectName("label")
        self.songs_list = QtWidgets.QTableWidget(Frame)
        self.songs_list.setGeometry(QtCore.QRect(200, 0, 781, 571))
        self.songs_list.setMinimumSize(QtCore.QSize(781, 0))
        self.songs_list.setStyleSheet("\n"
"background-color: rgb(193, 193, 193);")
        self.songs_list.setLineWidth(1)
        self.songs_list.setMidLineWidth(1)
        self.songs_list.setRowCount(0)
        self.songs_list.setColumnCount(1)
        self.songs_list.setObjectName("songs_list")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(8)
        font.setUnderline(False)
        item.setFont(font)
        self.songs_list.setHorizontalHeaderItem(0, item)
        self.songs_list.horizontalHeader().setDefaultSectionSize(780)
        self.find_path = QtWidgets.QPushButton(Frame)
        self.find_path.setGeometry(QtCore.QRect(60, 510, 75, 23))
        self.find_path.setStyleSheet("background-color: rgb(136, 136, 136);")
        self.find_path.setObjectName("find_path")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Mp3 Oynatıcı"))
        self.nextButton.setText(_translate("Frame", ">>|"))
        self.backButton.setText(_translate("Frame", "|<<"))
        self.Shuffle.setText(_translate("Frame", "Shuffle"))
        self.label.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Ses Seviyesi</p></body></html>"))
        item = self.songs_list.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "Şarkı İsmi"))
        self.find_path.setText(_translate("Frame", "Şarkıları Ekle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
