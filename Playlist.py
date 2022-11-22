class Playlist:
    
    def __init__(self,songsFromPath = []):
        self.plist = songsFromPath

    @property
    def plist(self):
        return self.plist

    @plist.setter
    def plist(self, value):
        self.plist.clear()
        self.plist.extend(value)

    