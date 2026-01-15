from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class example_Player:

    def __init__(self, compression: str):
        self.compression = compression
        
    @property
    def compression(self) -> str:
        return self.__compression

    @compression.setter
    def compression(self, compression: str):
        self.__compression = compression

    def setCompression(self) -> str:
        # TODO: Implement setCompression method
        pass
