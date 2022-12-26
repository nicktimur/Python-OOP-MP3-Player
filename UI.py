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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Designbolts-Free-Multimedia-Mp3-Player.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Frame.setWindowIcon(icon)
        Frame.setAutoFillBackground(False)
        Frame.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);\n"
"border-color: rgb(80, 80, 80);\n"
"background-color: rgb(24, 24, 24);\n"
"")
        self.frame = QtWidgets.QFrame(Frame)
        self.frame.setGeometry(QtCore.QRect(0, 570, 1221, 101))
        self.frame.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.play = QtWidgets.QPushButton(self.frame)
        self.play.setGeometry(QtCore.QRect(560, 10, 41, 41))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(20)
        self.play.setFont(font)
        self.play.setStyleSheet("QPushButton {\n"
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
        self.play.setText("▶")
        self.play.setObjectName("play")
        self.nowPlaying = QtWidgets.QLineEdit(self.frame)
        self.nowPlaying.setGeometry(QtCore.QRect(10, 10, 291, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.nowPlaying.setFont(font)
        self.nowPlaying.setStyleSheet("background-color:  rgb(75, 75, 75);\n"
"color: #c2c2c2;\n"
"border: 2px solid #313131;\n"
"border-radius: 5px;\n"
"border-style: outset;\n"
"")
        self.nowPlaying.setText("")
        self.nowPlaying.setReadOnly(True)
        self.nowPlaying.setObjectName("nowPlaying")
        self.nextButton = QtWidgets.QPushButton(self.frame)
        self.nextButton.setGeometry(QtCore.QRect(620, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.nextButton.setFont(font)
        self.nextButton.setStyleSheet("QPushButton {\n"
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
        self.nextButton.setObjectName("nextButton")
        self.backButton = QtWidgets.QPushButton(self.frame)
        self.backButton.setGeometry(QtCore.QRect(510, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("QPushButton {\n"
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
        self.backButton.setObjectName("backButton")
        self.Shuffle = QtWidgets.QPushButton(self.frame)
        self.Shuffle.setGeometry(QtCore.QRect(10, 40, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.Shuffle.setFont(font)
        self.Shuffle.setStyleSheet("QPushButton {\n"
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
        self.Shuffle.setCheckable(True)
        self.Shuffle.setObjectName("Shuffle")
        self.SoundSlider = QtWidgets.QSlider(self.frame)
        self.SoundSlider.setGeometry(QtCore.QRect(1000, 50, 160, 22))
        self.SoundSlider.setStyleSheet("QSlider::groove:horizontal {\n"
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
        self.SoundSlider.setMaximum(100)
        self.SoundSlider.setSingleStep(1)
        self.SoundSlider.setPageStep(10)
        self.SoundSlider.setProperty("value", 100)
        self.SoundSlider.setSliderPosition(100)
        self.SoundSlider.setTracking(True)
        self.SoundSlider.setOrientation(QtCore.Qt.Horizontal)
        self.SoundSlider.setObjectName("SoundSlider")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(1040, 30, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: #c2c2c2;\n"
"    border: 2px solid #313131;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"    background:  rgb(50, 50, 50);\n"
"    }\n"
"")
        self.label.setObjectName("label")
        self.PlaySlider = QtWidgets.QSlider(self.frame)
        self.PlaySlider.setGeometry(QtCore.QRect(350, 60, 461, 22))
        self.PlaySlider.setMouseTracking(False)
        self.PlaySlider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.PlaySlider.setStyleSheet("QSlider::groove:horizontal {\n"
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
        self.PlaySlider.setMaximum(0)
        self.PlaySlider.setSingleStep(1)
        self.PlaySlider.setPageStep(10)
        self.PlaySlider.setProperty("value", 0)
        self.PlaySlider.setSliderPosition(0)
        self.PlaySlider.setTracking(True)
        self.PlaySlider.setOrientation(QtCore.Qt.Horizontal)
        self.PlaySlider.setInvertedAppearance(False)
        self.PlaySlider.setInvertedControls(False)
        self.PlaySlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.PlaySlider.setObjectName("PlaySlider")
        self.time = QtWidgets.QLabel(self.frame)
        self.time.setGeometry(QtCore.QRect(306, 60, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(9)
        self.time.setFont(font)
        self.time.setStyleSheet("")
        self.time.setObjectName("time")
        self.Backward = QtWidgets.QPushButton(self.frame)
        self.Backward.setGeometry(QtCore.QRect(470, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.Backward.setFont(font)
        self.Backward.setStyleSheet("QPushButton {\n"
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
        self.Backward.setObjectName("Backward")
        self.Forward = QtWidgets.QPushButton(self.frame)
        self.Forward.setGeometry(QtCore.QRect(660, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.Forward.setFont(font)
        self.Forward.setStyleSheet("QPushButton {\n"
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
        self.Forward.setObjectName("Forward")
        self.fullTime = QtWidgets.QLabel(self.frame)
        self.fullTime.setGeometry(QtCore.QRect(820, 60, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(9)
        self.fullTime.setFont(font)
        self.fullTime.setStyleSheet("")
        self.fullTime.setObjectName("fullTime")
        self.songs_list = QtWidgets.QTableWidget(Frame)
        self.songs_list.setGeometry(QtCore.QRect(200, 0, 781, 571))
        self.songs_list.setMinimumSize(QtCore.QSize(781, 0))
        self.songs_list.setStyleSheet("QWidget {\n"
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
        self.songs_list.setLineWidth(1)
        self.songs_list.setMidLineWidth(1)
        self.songs_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.songs_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.songs_list.setRowCount(0)
        self.songs_list.setColumnCount(1)
        self.songs_list.setObjectName("songs_list")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(8)
        font.setUnderline(False)
        item.setFont(font)
        self.songs_list.setHorizontalHeaderItem(0, item)
        self.songs_list.horizontalHeader().setDefaultSectionSize(780)
        self.about_us = QtWidgets.QPushButton(Frame)
        self.about_us.setGeometry(QtCore.QRect(120, 540, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.about_us.setFont(font)
        self.about_us.setStyleSheet("QPushButton {\n"
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
        self.about_us.setObjectName("about_us")
        self.BlackBull = QtWidgets.QPushButton(Frame)
        self.BlackBull.setGeometry(QtCore.QRect(990, 90, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.BlackBull.setFont(font)
        self.BlackBull.setStyleSheet("QPushButton {\n"
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
        self.BlackBull.setObjectName("BlackBull")
        self.themes = QtWidgets.QLabel(Frame)
        self.themes.setGeometry(QtCore.QRect(990, 20, 211, 61))
        self.themes.setStyleSheet("color:#c2c2c2;")
        self.themes.setObjectName("themes")
        self.find_path = QtWidgets.QPushButton(Frame)
        self.find_path.setGeometry(QtCore.QRect(10, 540, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.find_path.setFont(font)
        self.find_path.setStyleSheet("QPushButton {\n"
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
        self.find_path.setObjectName("find_path")
        self.Default = QtWidgets.QPushButton(Frame)
        self.Default.setGeometry(QtCore.QRect(990, 150, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.Default.setFont(font)
        self.Default.setStyleSheet("QPushButton {\n"
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
        self.Default.setObjectName("Default")
        self.Indian_Rush = QtWidgets.QPushButton(Frame)
        self.Indian_Rush.setGeometry(QtCore.QRect(990, 210, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.Indian_Rush.setFont(font)
        self.Indian_Rush.setStyleSheet("QPushButton {\n"
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
        self.Indian_Rush.setObjectName("Indian_Rush")
        self.White_Chocolate = QtWidgets.QPushButton(Frame)
        self.White_Chocolate.setGeometry(QtCore.QRect(990, 270, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.White_Chocolate.setFont(font)
        self.White_Chocolate.setStyleSheet("QPushButton {\n"
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
        self.White_Chocolate.setObjectName("White_Chocolate")
        self.Bleeding_Rose = QtWidgets.QPushButton(Frame)
        self.Bleeding_Rose.setGeometry(QtCore.QRect(990, 330, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.Bleeding_Rose.setFont(font)
        self.Bleeding_Rose.setStyleSheet("QPushButton {\n"
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
        self.Bleeding_Rose.setObjectName("Bleeding_Rose")
        self.Turkey_Edition = QtWidgets.QPushButton(Frame)
        self.Turkey_Edition.setGeometry(QtCore.QRect(990, 390, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.Turkey_Edition.setFont(font)
        self.Turkey_Edition.setStyleSheet("QPushButton {\n"
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
        self.Turkey_Edition.setObjectName("Turkey_Edition")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Mp3 Oynatıcı"))
        self.nextButton.setText(_translate("Frame", ">>|"))
        self.backButton.setText(_translate("Frame", "|<<"))
        self.Shuffle.setText(_translate("Frame", "Shuffle"))
        self.label.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Ses Seviyesi</p></body></html>"))
        self.time.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Backward.setText(_translate("Frame", "↩"))
        self.Forward.setText(_translate("Frame", "↪"))
        self.fullTime.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        item = self.songs_list.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "Şarkı İsmi"))
        self.about_us.setText(_translate("Frame", "Hakkımızda"))
        self.BlackBull.setText(_translate("Frame", "BlackBull"))
        self.themes.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Temalar</span></p></body></html>"))
        self.find_path.setText(_translate("Frame", "Şarkıları Ekle"))
        self.Default.setText(_translate("Frame", "Default"))
        self.Indian_Rush.setText(_translate("Frame", "Indian Rush"))
        self.White_Chocolate.setText(_translate("Frame", "White Chocolate"))
        self.Bleeding_Rose.setText(_translate("Frame", "Bleeding Rose"))
        self.Turkey_Edition.setText(_translate("Frame", "Turkey Edition"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
