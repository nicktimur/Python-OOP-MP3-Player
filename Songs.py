import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from tkinter import filedialog
from UI import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QImage
import pygame
import random
import mutagen
from io import BytesIO


class Songs:
    
    def __init__(self,ui):
        pygame.init()
        self.songList = []
        self.shuffled_list = []
        self.shuffleRow = 0
        self.playingRow = 0
        self.playing = False
        self.ui = ui
        self.path = ""
        self.SONG_END = pygame.USEREVENT+1
        
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

    def play_clicked(self):
        if (not self.isChanged()):
            try:
                if (self.ui.play.text() == "▶" and not self.playing):
                    self.PlayMusic()
                    self.ui.play.setText("||")

                elif (self.ui.play.text() == "▶"and self.playing):
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
        self.ui.songs_list.horizontalHeader().resizeSection(0, 730)
        for i in range(len(songsList)):
                self.ui.songs_list.setItem(i,0,QTableWidgetItem(songsList[i]))

    def AddMusic(self):
        del self.songs
        self.StopMusic()
        self.path = filedialog.askdirectory()
        if self.path:
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
        pygame.mixer.music.load(self.songs[self.playingRow])
        pygame.mixer.music.play()
        self.playing = True
        self.ui.nowPlaying.setText("Çalan Şarkı: {}".format(self.songs[self.playingRow]))


    def PlayNext(self):
        try:
            self.playingRow = self.ui.songs_list.currentRow()
            if(self.playingRow+2 > len(self.songs)):
                return 0
            self.PauseMusic()
            if(self.ui.Shuffle.isChecked()):
                shuffled_song = self.songs[random.randint(0,len(self.songs))]
                self.shuffled_list.append(shuffled_song)
                self.shuffleRow = len(self.shuffled_list) - 1
                pygame.mixer.music.load(shuffled_song)
                self.ui.nowPlaying.setText("Çalan Şarkı: {}".format(shuffled_song))
                self.ui.songs_list.selectRow(self.songs.index(shuffled_song))
            else:
                self.playingRow = self.playingRow + 1
                pygame.mixer.music.load(self.songs[self.playingRow])
                self.ui.nowPlaying.setText("Çalan Şarkı: {}".format(self.songs[self.playingRow]))
                self.ui.songs_list.selectRow(self.playingRow)
            pygame.mixer.music.play()
            self.playing = True
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
                pygame.mixer.music.load(self.shuffled_list[self.shuffleRow])
                self.ui.nowPlaying.setText("Çalan Şarkı: {}".format(self.shuffled_list[self.shuffleRow]))
                self.ui.songs_list.selectRow(self.songs.index(self.shuffled_list[self.shuffleRow]))
            else:
                self.playingRow = self.playingRow - 1
                pygame.mixer.music.load(self.songs[self.playingRow])
                self.ui.nowPlaying.setText("Çalan Şarkı: {}".format(self.songs[self.playingRow]))
                self.ui.songs_list.selectRow(self.playingRow)
            pygame.mixer.music.play()
            self.playing = True
        except:
            pass

    def PauseMusic(self):
        pygame.mixer.music.pause()
        self.playing = True

    def UnpauseMusic(self):
        pygame.mixer.music.unpause()
        self.playing = True

    def StopMusic(self):
        try:
            pygame.mixer.music.stop()
            self.playing = False
        except:
            pass

    def isChanged(self):
        if (self.ui.songs_list.currentRow() != self.playingRow):
            return True
        else:
            return False

    def check_event(self):
        while True:
            for event in pygame.event.get():
                if event.type == self.SONG_END:
                    self.PlayNext()
