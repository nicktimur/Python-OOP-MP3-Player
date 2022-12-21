from PyQt5.QtCore import QThread

class Worker(QThread):
    def __init__(self, song) -> None:
        super().__init__()
        self.song = song
        
    
    def run(self):
        try:
            while True:
                if(self.song.status == "Playing"):
                    self.song.check_event()
        except:
            pass

class TimeSetter(Worker):
    def run(self):
        while True:
            if(self.song.status == "Playing"):
                try:
                    self.song.set_time()
                except:
                    pass