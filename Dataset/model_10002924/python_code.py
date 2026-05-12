from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Hotel_Manager_Actor:

    pass


class Receptionist_Actor:

    pass


class Guest_Actor:

    pass


class Look_up_Reservation_UseCase:

    pass


class Register_as_new_customer_UseCase:

    pass


class View_Month_s_Statistics_UseCase:

    pass


class Check_out_Guest_UseCase:

    pass


class Check_in_Guest_UseCase:

    pass





class Make__Reservation_external:

    pass


class inte:

    pass


class Room:

    def __init__(self, Number: int, Guests: int, reservation11: set["Reservation"] = None):
        self.Number = Number
        self.Guests = Guests
        self.reservation11 = reservation11 if reservation11 is not None else set()
        
        pass
    @property
    def Number(self):
        return self.__Number
    @Number.setter
    def Number(self, Number: int):
        self.__Number = Number

    @property
    def Guests(self):
        return self.__Guests
    @Guests.setter
    def Guests(self, Guests: int):
        self.__Guests = Guests

    @property
    def reservation11(self):
        return self.__reservation11
    @reservation11.setter
    def reservation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__reservation11", None)
        self.__reservation11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room10"):
                    opp_val = getattr(item, "room10", None)
                    
                    if opp_val == self:
                        setattr(item, "room10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room10"):
                    opp_val = getattr(item, "room10", None)
                    
                    setattr(item, "room10", self)
                    



class Reservation:

    def __init__(self, Reservation_id: int, Start: str, End: str, guest9: set["Guest"] = None, room10: "Room" = None):
        self.Reservation_id = Reservation_id
        self.Start = Start
        self.End = End
        self.guest9 = guest9 if guest9 is not None else set()
        self.room10 = room10
        
        pass
    @property
    def End(self):
        return self.__End
    @End.setter
    def End(self, End: str):
        self.__End = End

    @property
    def Reservation_id(self):
        return self.__Reservation_id
    @Reservation_id.setter
    def Reservation_id(self, Reservation_id: int):
        self.__Reservation_id = Reservation_id

    @property
    def Start(self):
        return self.__Start
    @Start.setter
    def Start(self, Start: str):
        self.__Start = Start

    @property
    def room10(self):
        return self.__room10
    @room10.setter
    def room10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reservation__room10", None)
        self.__room10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservation11"):
                opp_val = getattr(old_value, "reservation11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservation11"):
                opp_val = getattr(value, "reservation11", None)
                if opp_val is None:
                    setattr(value, "reservation11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def guest9(self):
        return self.__guest9
    @guest9.setter
    def guest9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reservation__guest9", None)
        self.__guest9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reservation8"):
                    opp_val = getattr(item, "reservation8", None)
                    
                    if opp_val == self:
                        setattr(item, "reservation8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reservation8"):
                    opp_val = getattr(item, "reservation8", None)
                    
                    setattr(item, "reservation8", self)
                    



class Guest:

    def __init__(self, Name: str, Address: str, reservation8: "Reservation" = None):
        self.Name = Name
        self.Address = Address
        self.reservation8 = reservation8
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def reservation8(self):
        return self.__reservation8
    @reservation8.setter
    def reservation8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Guest__reservation8", None)
        self.__reservation8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "guest9"):
                opp_val = getattr(old_value, "guest9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "guest9"):
                opp_val = getattr(value, "guest9", None)
                if opp_val is None:
                    setattr(value, "guest9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Hotel_System_Component:

    pass
