import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from tkinter import filedialog
from UI import *
from PyQt5.QtWidgets import *
import pygame
import random
import sqlite3
from Theme import theme_changer



class Songs:
    
    def __init__(self,ui, DB_DIR):
        pygame.init()
        self.songList = []
        self.shuffled_list = []
        self.shuffleRow = 0
        self.playingRow = 0
        self.status = "Waiting"
        self.songlen = 0
        self.ui = ui
        self.path = ""
        self.SONG_END = pygame.USEREVENT+1
        self.diff = 0
        self.isAdded = False
        self.DB_DIR = DB_DIR
        self.AddMusicWithDb()

    def AddMusicWithDb(self):
        try:
            with sqlite3.connect(self.DB_DIR) as db:
                cur = db.cursor()
                cmd = "SELECT path FROM path"
                cur.execute(cmd)
                self.path = cur.fetchone()[0]
            self.ui.play.setText("▶")
            self.ui.songs_list.setRowCount(0)
            os.chdir(self.path)
            temp = os.listdir(self.path)
            for song in temp:
                if song.endswith(".mp3"):
                    self.songs.append(song)
            del temp
            self.AddtoTable(self.songs)
            self.playingRow = 0
            self.isAdded = True
        except:
            pass

    @property
    def songs(self):
        return self.songList

    @songs.setter
    def songs(self, value):
        self.songList.clear()
        self.songList.extend(value)
        self.AddtoTable(value)


    @songs.deleter
    def songs(self):
        self.songList.clear()

    def setVolume(self):
        new_volume = self.ui.SoundSlider.value() # 0-100 arası bir değer alıyor
        new_volume = new_volume / 100
        pygame.mixer.music.set_volume(new_volume) # 0-1 arası float değerler istiyor
        print(new_volume)

    def play_clicked(self):
        if (not self.isChanged()):
            try:
                if (self.ui.play.text() == "▶" and self.status == "Waiting"):
                    self.PlayMusic()
                    self.ui.play.setText("||")

                elif (self.ui.play.text() == "▶"and self.status == "Paused"):
                    self.UnpauseMusic()
                    self.ui.play.setText("||")

                elif (self.ui.play.text() == "||"):
                    self.PauseMusic()
                    self.ui.play.setText("▶")
                
            except:
                self.ui.play.setText("▶")

        else:
            try:
                self.ui.play.setText("||")
                self.PlayMusic()
            except:
                self.ui.play.setText("▶")

    def AddtoTable(self, songsList):
        self.ui.songs_list.setRowCount(len(songsList))
        self.ui.songs_list.horizontalHeader().resizeSection(0, 736)
        for i in range(len(songsList)):
                self.ui.songs_list.setItem(i,0,QTableWidgetItem(songsList[i]))
        self.isAdded = True

    def AddMusic(self):
        del self.songs
        self.StopMusic()
        self.ui.play.setText("▶")
        temp = self.path
        self.path = filedialog.askdirectory()
        self.ui.songs_list.setRowCount(0)
        if self.path:
            with sqlite3.connect(self.DB_DIR) as db:
                cur = db.cursor()
                cmd = "DELETE FROM path"
                cur.execute(cmd)
                cmd = "INSERT INTO path VALUES ('{}')".format(self.path)
                cur.execute(cmd)

            os.chdir(self.path)
            temp = os.listdir(self.path)
            for song in temp:
                if song.endswith(".mp3"):
                    self.songs.append(song)
            del temp
            self.AddtoTable(self.songs)
            self.playingRow = 0
        else:
            self.path = temp
            os.chdir(self.path)
            temp = os.listdir(self.path)
            for song in temp:
                if song.endswith(".mp3"):
                    self.songs.append(song)
            del temp
            self.AddtoTable(self.songs)
            self.playingRow = 0

    def PlayMusic(self):
        self.playingRow = self.ui.songs_list.currentRow()
        pygame.mixer.music.set_endevent(self.SONG_END)
        self.songlen = pygame.mixer.Sound(self.songs[self.playingRow]).get_length()
        pygame.mixer.music.load(self.songs[self.playingRow])
        pygame.mixer.music.play()
        self.diff = 0
        self.status = "Playing"
        self.ui.nowPlaying.setText("Çalan Şarkı: {}".format(self.songs[self.playingRow]))


    def PlayNext(self):
        try:
            self.playingRow = self.ui.songs_list.currentRow()
            if(self.playingRow+2 > len(self.songs)):
                self.playingRow = -1
            self.PauseMusic()
            if(self.ui.Shuffle.isChecked()):
                shuffled_song = self.songs[random.randint(0,len(self.songs))]
                self.shuffled_list.append(shuffled_song)
                self.shuffleRow = len(self.shuffled_list) - 1
                self.songlen = pygame.mixer.Sound(shuffled_song).get_length()
                pygame.mixer.music.load(shuffled_song)
                self.ui.nowPlaying.setText("Çalan Şarkı: {}".format(shuffled_song))
                self.ui.songs_list.selectRow(self.songs.index(shuffled_song))
            else:
                self.playingRow = self.playingRow + 1
                self.songlen = pygame.mixer.Sound(self.songs[self.playingRow]).get_length()
                pygame.mixer.music.load(self.songs[self.playingRow])
                self.ui.nowPlaying.setText("Çalan Şarkı: {}".format(self.songs[self.playingRow]))
                self.ui.songs_list.selectRow(self.playingRow)
            pygame.mixer.music.play()
            self.diff = 0
            self.status = "Playing"
        except:
            pass

    def PlayLast(self):
        self.playingRow = self.ui.songs_list.currentRow()
        if(self.playingRow - 1 < 0):
            return 0
        self.PauseMusic()
        try:
            if(self.ui.Shuffle.isChecked()):
                self.shuffleRow -= 1
                self.songlen = pygame.mixer.Sound(self.shuffled_list[self.shuffleRow]).get_length()
                pygame.mixer.music.load(self.shuffled_list[self.shuffleRow])
                self.ui.nowPlaying.setText("Çalan Şarkı: {}".format(self.shuffled_list[self.shuffleRow]))
                self.ui.songs_list.selectRow(self.songs.index(self.shuffled_list[self.shuffleRow]))
            else:
                self.playingRow = self.playingRow - 1
                self.songlen = pygame.mixer.Sound(self.songs[self.playingRow]).get_length()
                pygame.mixer.music.load(self.songs[self.playingRow])
                self.ui.nowPlaying.setText("Çalan Şarkı: {}".format(self.songs[self.playingRow]))
                self.ui.songs_list.selectRow(self.playingRow)
            pygame.mixer.music.play()
            self.diff = 0
            self.status = "Playing"
        except:
            pass

    def PauseMusic(self):
        pygame.mixer.music.pause()
        self.status = "Paused"

    def UnpauseMusic(self):
        pygame.mixer.music.unpause()
        self.status = "Playing"

    def StopMusic(self):
        try:
            pygame.mixer.music.stop()
            self.status = "Waiting"
            self.ui.PlaySlider.setMaximum(0)
        except:
            pass

    def isChanged(self):
        if (self.ui.songs_list.currentRow() != self.playingRow):
            return True
        else:
            return False

    def check_event(self):
        for event in pygame.event.get():
            if event.type == self.SONG_END:
                self.PlayNext()
    
    def sliderPress(self):
        if(self.status == "Playing"):    
            self.status = "Setting"
        else:
            self.status = "Paused"

    def set_slider(self):
        pass

    def sliderRelease(self):
        newtime = self.ui.PlaySlider.value()
        realtime = (pygame.mixer.music.get_pos() / 1000)
        self.diff = newtime - realtime
        pygame.mixer.music.set_pos(newtime)
        if self.status == "Setting":
            self.status = "Playing"

    def set_time(self):
        if(self.status == "Playing"):
            sec = (pygame.mixer.music.get_pos() / 1000) + self.diff # Saniye dönüşümü ve fark ekleme
            remaining = self.songlen - sec #Kalan saniyeyi hesaplar
            self.ui.PlaySlider.setMaximum(int(self.songlen))
            self.ui.PlaySlider.setSliderPosition(int(sec))
            temp = divmod(int(sec), 60)
            min = temp[0]
            sec = temp[1]
            if theme_changer.theme == "White Chocolate" or theme_changer.theme == "Turkey Edition" or theme_changer.theme == "Indian Rush":
                self.ui.time.setText(QtCore.QCoreApplication.translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">"+ "{:02}:{:02}".format(min, sec)  +"</span></p></p></body></html>"))
                temp = divmod(int(remaining), 60) #Kalan sürenin hesabı
                min = temp[0]#Kalan sürenin dakikası
                sec = temp[1]#Kalan sürenin saniyesi
                self.ui.fullTime.setText(QtCore.QCoreApplication.translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">"+ "{:02}:{:02}".format(min, sec)  +"</span></p></p></body></html>"))
            else:
                self.ui.time.setText(QtCore.QCoreApplication.translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" color:#c2c2c2;\">"+ "{:02}:{:02}".format(min, sec)  +"</span></p></p></body></html>"))
                temp = divmod(int(remaining), 60) #Kalan sürenin hesabı
                min = temp[0]#Kalan sürenin dakikası
                sec = temp[1]#Kalan sürenin saniyesi
                self.ui.fullTime.setText(QtCore.QCoreApplication.translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" color:#c2c2c2;\">"+ "{:02}:{:02}".format(min, sec)  +"</span></p></p></body></html>"))
        else:
            pass

    def forward(self):
        pos = self.ui.PlaySlider.value()
        self.ui.PlaySlider.setSliderPosition(pos + 10) #Slider pozisyonunu 10 saniye ileri alıyorum
        self.diff += 10 #Gerçek çalma zamanıyla aradaki fark 10 saniye açıldı
        pygame.mixer.music.set_pos(pos + 10) #Şarkı 10 saniye ileri alındı

    def backward(self):
        pos = self.ui.PlaySlider.value()
        if (pos - 10 >= 0):
            self.ui.PlaySlider.setSliderPosition(pos - 10) #Slider pozisyonunu 10 saniye geri alıyorum
            self.diff -= 10 #Gerçek çalma zamanıyla aradaki fark 10 saniye kapandı
            pygame.mixer.music.set_pos(pos - 10) #Şarkı 10 saniye geri alındı
        else:
            self.ui.PlaySlider.setSliderPosition(0) #Slider pozisyonunu 0 yapıyorum
            self.diff -= pos #Gerçek çalma zamanıyla aradaki fark pos kadar saniye kapandı
            pygame.mixer.music.set_pos(0) #Şarkı başa alındı.