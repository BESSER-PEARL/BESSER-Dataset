from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class RESERVATION_SYSTEM:

    def __init__(self, Reservation_ID: int, Reservation_Date: int, RESERVATION_SYSTEM1: "FLIGHT" = None):
        self.Reservation_ID = Reservation_ID
        self.Reservation_Date = Reservation_Date
        self.RESERVATION_SYSTEM1 = RESERVATION_SYSTEM1
        
        pass
    @property
    def Reservation_Date(self):
        return self.__Reservation_Date
    @Reservation_Date.setter
    def Reservation_Date(self, Reservation_Date: int):
        self.__Reservation_Date = Reservation_Date

    @property
    def Reservation_ID(self):
        return self.__Reservation_ID
    @Reservation_ID.setter
    def Reservation_ID(self, Reservation_ID: int):
        self.__Reservation_ID = Reservation_ID

    @property
    def RESERVATION_SYSTEM1(self):
        return self.__RESERVATION_SYSTEM1
    @RESERVATION_SYSTEM1.setter
    def RESERVATION_SYSTEM1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RESERVATION_SYSTEM__RESERVATION_SYSTEM1", None)
        self.__RESERVATION_SYSTEM1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FLIGHT_RESERVATION_SYSTEM_00"):
                opp_val = getattr(old_value, "FLIGHT_RESERVATION_SYSTEM_00", None)
                if opp_val == self:
                    setattr(old_value, "FLIGHT_RESERVATION_SYSTEM_00", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FLIGHT_RESERVATION_SYSTEM_00"):
                opp_val = getattr(value, "FLIGHT_RESERVATION_SYSTEM_00", None)
                setattr(value, "FLIGHT_RESERVATION_SYSTEM_00", self)



class FLIGHT:

    def __init__(self, Flight_No_: int, Flight_Name: str, FLIGHT_RESERVATION_SYSTEM_00: "RESERVATION_SYSTEM" = None):
        self.Flight_No_ = Flight_No_
        self.Flight_Name = Flight_Name
        self.FLIGHT_RESERVATION_SYSTEM_00 = FLIGHT_RESERVATION_SYSTEM_00
        
        pass
    @property
    def Flight_No_(self):
        return self.__Flight_No_
    @Flight_No_.setter
    def Flight_No_(self, Flight_No_: int):
        self.__Flight_No_ = Flight_No_

    @property
    def Flight_Name(self):
        return self.__Flight_Name
    @Flight_Name.setter
    def Flight_Name(self, Flight_Name: str):
        self.__Flight_Name = Flight_Name

    @property
    def FLIGHT_RESERVATION_SYSTEM_00(self):
        return self.__FLIGHT_RESERVATION_SYSTEM_00
    @FLIGHT_RESERVATION_SYSTEM_00.setter
    def FLIGHT_RESERVATION_SYSTEM_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FLIGHT__FLIGHT_RESERVATION_SYSTEM_00", None)
        self.__FLIGHT_RESERVATION_SYSTEM_00 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RESERVATION_SYSTEM1"):
                opp_val = getattr(old_value, "RESERVATION_SYSTEM1", None)
                if opp_val == self:
                    setattr(old_value, "RESERVATION_SYSTEM1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RESERVATION_SYSTEM1"):
                opp_val = getattr(value, "RESERVATION_SYSTEM1", None)
                setattr(value, "RESERVATION_SYSTEM1", self)



class PASSENGER:

    def __init__(self, Pass_Name: str, Pass_ID: int, Pass_Address: str):
        self.Pass_Name = Pass_Name
        self.Pass_ID = Pass_ID
        self.Pass_Address = Pass_Address
        
        pass
    @property
    def Pass_ID(self):
        return self.__Pass_ID
    @Pass_ID.setter
    def Pass_ID(self, Pass_ID: int):
        self.__Pass_ID = Pass_ID

    @property
    def Pass_Address(self):
        return self.__Pass_Address
    @Pass_Address.setter
    def Pass_Address(self, Pass_Address: str):
        self.__Pass_Address = Pass_Address

    @property
    def Pass_Name(self):
        return self.__Pass_Name
    @Pass_Name.setter
    def Pass_Name(self, Pass_Name: str):
        self.__Pass_Name = Pass_Name

