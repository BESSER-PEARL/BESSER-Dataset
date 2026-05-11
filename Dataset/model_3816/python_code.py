from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class example_Player:

    def __init__(self, volume: str):
        self.volume = volume
        
        pass
    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume

