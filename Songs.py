
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import platform
import random
import sqlite3

import pygame
from UI import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from Theme import theme_changer

if platform.system() == "Windows":
    from tkinter import filedialog


class Songs:

    def __init__(self, ui, DB_DIR):
        pygame.init()

        self.songList = []
        self.shuffled_list = []
        self.shuffleRow = 0
        self.playingRow = 0
        self.status = "Waiting"
        self.songlen = 0
        self.ui = ui
        self.path = ""
        self.SONG_END = pygame.USEREVENT + 1
        self.diff = 0
        self.isAdded = False
        self.DB_DIR = DB_DIR

        self.AddMusicWithDb()

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

    def _song_path(self, song):
        return os.path.join(self.path, song)

    def _get_mp3_files(self, folder):
        return sorted(
            [
                name for name in os.listdir(folder)
                if name.lower().endswith(".mp3")
                and os.path.isfile(os.path.join(folder, name))
            ],
            key=str.casefold
        )

    def _load_folder(self, folder):
        folder = os.path.abspath(os.path.expanduser(folder))

        if not os.path.isdir(folder):
            raise FileNotFoundError(folder)

        song_files = self._get_mp3_files(folder)

        self.StopMusic()
        self.path = folder
        self.songs = song_files

        self.shuffled_list.clear()
        self.shuffleRow = 0
        self.playingRow = 0
        self.diff = 0
        self.songlen = 0
        self.isAdded = bool(song_files)

        self.ui.play.setText("▶")
        self.ui.PlaySlider.setValue(0)

        if song_files:
            self.ui.songs_list.selectRow(0)

    def AddMusicWithDb(self):
        try:
            with sqlite3.connect(self.DB_DIR) as db:
                cur = db.cursor()
                cur.execute("SELECT path FROM path LIMIT 1")
                result = cur.fetchone()

            if result and result[0]:
                self._load_folder(result[0])

        except (sqlite3.Error, OSError) as error:
            print("Kayıtlı müzik klasörü yüklenemedi:", error)

    def _select_folder(self):
        system = platform.system()

        if system == "Darwin":
            return QFileDialog.getExistingDirectory(
                None,
                "Müzik Klasörünü Seç",
                self.path or os.path.expanduser("~"),
                QFileDialog.ShowDirsOnly
            )

        elif system == "Windows":
            return filedialog.askdirectory(
                title="Müzik Klasörünü Seç",
                initialdir=self.path or os.path.expanduser("~")
            )

        return QFileDialog.getExistingDirectory(
            None,
            "Müzik Klasörünü Seç",
            self.path or os.path.expanduser("~")
        )

    def AddMusic(self):
        selected_path = self._select_folder()

        # Kullanıcı seçimi iptal ederse hiçbir şeyi değiştirme.
        if not selected_path:
            return

        selected_path = os.path.abspath(
            os.path.expanduser(selected_path)
        )

        if not os.path.isdir(selected_path):
            print("Geçersiz klasör:", selected_path)
            return

        try:
            # Önce klasörün okunabildiğini doğrula.
            self._get_mp3_files(selected_path)

            # Seçilen klasörü veritabanına kaydet.
            with sqlite3.connect(self.DB_DIR) as db:
                cur = db.cursor()
                cur.execute("DELETE FROM path")
                cur.execute(
                    "INSERT INTO path VALUES (?)",
                    (selected_path,)
                )

            self._load_folder(selected_path)

        except (OSError, sqlite3.Error) as error:
            print("Müzik klasörü yüklenemedi:", error)

    def AddtoTable(self, songsList):
        self.ui.songs_list.setRowCount(len(songsList))
        self.ui.songs_list.horizontalHeader().resizeSection(0, 736)

        for i, song in enumerate(songsList):
            self.ui.songs_list.setItem(
                i, 0, QTableWidgetItem(song)
            )

        self.isAdded = bool(songsList)

    def setVolume(self):
        new_volume = self.ui.SoundSlider.value() / 100
        pygame.mixer.music.set_volume(new_volume)

    def play_clicked(self):
        if not self.songs:
            return

        try:
            if self.isChanged():
                self.PlayMusic()
                return

            if self.status in ("Waiting",):
                self.PlayMusic()

            elif self.status == "Paused":
                self.UnpauseMusic()

            elif self.status == "Playing":
                self.PauseMusic()

        except (pygame.error, OSError, IndexError) as error:
            print("Müzik oynatma hatası:", error)
            self.ui.play.setText("▶")

    def _play_index(self, index):
        if not self.songs:
            return

        if not 0 <= index < len(self.songs):
            return

        song = self.songs[index]
        song_path = self._song_path(song)

        pygame.mixer.music.set_endevent(self.SONG_END)
        pygame.mixer.music.load(song_path)

        self.songlen = pygame.mixer.Sound(
            song_path
        ).get_length()

        pygame.mixer.music.play()

        self.playingRow = index
        self.diff = 0
        self.status = "Playing"

        self.ui.songs_list.selectRow(index)
        self.ui.play.setText("||")
        self.ui.nowPlaying.setText(
            "Çalan Şarkı: {}".format(song)
        )

    def PlayMusic(self):
        if not self.songs:
            return

        index = self.ui.songs_list.currentRow()

        if index < 0:
            index = 0

        self._play_index(index)

    def PlayNext(self):
        if not self.songs:
            return

        try:
            if self.ui.Shuffle.isChecked():
                next_index = random.randrange(len(self.songs))
                self.shuffled_list.append(self.songs[next_index])
                self.shuffleRow = len(self.shuffled_list) - 1
            else:
                next_index = (self.playingRow + 1) % len(self.songs)

            self._play_index(next_index)

        except (pygame.error, OSError, IndexError) as error:
            print("Sonraki şarkı hatası:", error)

    def PlayLast(self):
        if not self.songs:
            return

        try:
            if self.ui.Shuffle.isChecked():
                if self.shuffleRow <= 0:
                    return

                self.shuffleRow -= 1
                previous_song = self.shuffled_list[self.shuffleRow]
                previous_index = self.songs.index(previous_song)
            else:
                if self.playingRow <= 0:
                    return

                previous_index = self.playingRow - 1

            self._play_index(previous_index)

        except (pygame.error, OSError, IndexError, ValueError) as error:
            print("Önceki şarkı hatası:", error)

    def PauseMusic(self):
        pygame.mixer.music.pause()
        self.status = "Paused"
        self.ui.play.setText("▶")

    def UnpauseMusic(self):
        pygame.mixer.music.unpause()
        self.status = "Playing"
        self.ui.play.setText("||")

    def StopMusic(self):
        try:
            pygame.mixer.music.stop()
            self.status = "Waiting"
            self.diff = 0
            self.ui.PlaySlider.setMaximum(0)
            self.ui.play.setText("▶")

        except pygame.error as error:
            print("Müzik durdurma hatası:", error)

    def isChanged(self):
        return self.ui.songs_list.currentRow() != self.playingRow

    def check_event(self):
        for event in pygame.event.get():
            if event.type == self.SONG_END:
                self.PlayNext()

    def sliderPress(self):
        if self.status == "Playing":
            self.status = "Setting"
        else:
            self.status = "Paused"

    def set_slider(self):
        pass

    def sliderRelease(self):
        if not self.songs:
            return

        newtime = self.ui.PlaySlider.value()

        try:
            pygame.mixer.music.set_pos(newtime)
            self.diff = 0

            if self.status == "Setting":
                self.status = "Playing"

        except pygame.error as error:
            print("Şarkı konumu değiştirilemedi:", error)

    def set_time(self):
        if self.status != "Playing":
            return

        sec = (pygame.mixer.music.get_pos() / 1000) + self.diff
        sec = max(0, min(sec, self.songlen))
        remaining = max(0, self.songlen - sec)

        self.ui.PlaySlider.setMaximum(int(self.songlen))
        self.ui.PlaySlider.setSliderPosition(int(sec))

        elapsed_min, elapsed_sec = divmod(int(sec), 60)
        remaining_min, remaining_sec = divmod(int(remaining), 60)

        light_themes = (
            "White Chocolate",
            "Turkey Edition",
            "Indian Rush"
        )

        if theme_changer.theme in light_themes:
            color = "#000000"
        else:
            color = "#c2c2c2"

        elapsed_text = "{:02}:{:02}".format(
            elapsed_min, elapsed_sec
        )

        remaining_text = "{:02}:{:02}".format(
            remaining_min, remaining_sec
        )

        def time_html(value):
            return (
                '<html><head/><body>'
                '<p align="center">'
                '<span style="color:{};">{}</span>'
                '</p></body></html>'
            ).format(color, value)

        self.ui.time.setText(
            QtCore.QCoreApplication.translate(
                "Frame", time_html(elapsed_text)
            )
        )

        self.ui.fullTime.setText(
            QtCore.QCoreApplication.translate(
                "Frame", time_html(remaining_text)
            )
        )

    def forward(self):
        if not self.songs:
            return

        pos = self.ui.PlaySlider.value()
        new_pos = min(pos + 10, int(self.songlen))
        self._seek(new_pos)

    def backward(self):
        if not self.songs:
            return

        pos = self.ui.PlaySlider.value()
        new_pos = max(0, pos - 10)
        self._seek(new_pos)

    def _seek(self, position):
        try:
            pygame.mixer.music.set_pos(position)
            self.diff = 0
            self.ui.PlaySlider.setSliderPosition(position)

        except pygame.error as error:
            print("İleri/geri sarma hatası:", error)
