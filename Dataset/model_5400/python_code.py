from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class CoachBusWithEDataType_Coach:

    def __init__(self, noOfSeats: int):
        self.noOfSeats = noOfSeats
        
    @property
    def noOfSeats(self) -> int:
        return self.__noOfSeats

    @noOfSeats.setter
    def noOfSeats(self, noOfSeats: int):
        self.__noOfSeats = noOfSeats
