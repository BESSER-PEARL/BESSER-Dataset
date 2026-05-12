from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BookingStatus(Enum):
    pass

############################################
# Definition of Classes
############################################







class Guest_Check_out_UseCase:

    pass


class Guest_Check_in_UseCase:

    pass


class Cancel_Booking_UseCase:

    pass


class Make_Booking_UseCase:

    pass


class Manage_Rooms_UseCase:

    pass


class Manage_Room_Types_UseCase:

    pass


class Manage_Hotels_UseCase:

    pass


class Administrator_Actor:

    pass


class Manager_Actor:

    pass


class Receptionist_Actor:

    pass


class Guest_Actor:

    pass





class HotelBusiness:

    pass


class Contact:

    def __init__(self, name: str, address: str, email: str, phone: str, booking29: "Booking" = None):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.booking29 = booking29
        
        pass
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def booking29(self):
        return self.__booking29
    @booking29.setter
    def booking29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contact__booking29", None)
        self.__booking29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookedBy28"):
                opp_val = getattr(old_value, "bookedBy28", None)
                if opp_val == self:
                    setattr(old_value, "bookedBy28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookedBy28"):
                opp_val = getattr(value, "bookedBy28", None)
                setattr(value, "bookedBy28", self)



class Hotel:

    def __init__(self, name: str, hotelBusiness1: "HotelBusiness" = None, roomType2: set["RoomType"] = None, booking9: set["Booking"] = None):
        self.name = name
        self.hotelBusiness1 = hotelBusiness1
        self.roomType2 = roomType2 if roomType2 is not None else set()
        self.booking9 = booking9 if booking9 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hotelBusiness1(self):
        return self.__hotelBusiness1
    @hotelBusiness1.setter
    def hotelBusiness1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hotel__hotelBusiness1", None)
        self.__hotelBusiness1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hotel0"):
                opp_val = getattr(old_value, "hotel0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hotel0"):
                opp_val = getattr(value, "hotel0", None)
                if opp_val is None:
                    setattr(value, "hotel0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def roomType2(self):
        return self.__roomType2
    @roomType2.setter
    def roomType2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hotel__roomType2", None)
        self.__roomType2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hotel3"):
                    opp_val = getattr(item, "hotel3", None)
                    
                    if opp_val == self:
                        setattr(item, "hotel3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hotel3"):
                    opp_val = getattr(item, "hotel3", None)
                    
                    setattr(item, "hotel3", self)
                    

    @property
    def booking9(self):
        return self.__booking9
    @booking9.setter
    def booking9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hotel__booking9", None)
        self.__booking9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hotel8"):
                    opp_val = getattr(item, "hotel8", None)
                    
                    if opp_val == self:
                        setattr(item, "hotel8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hotel8"):
                    opp_val = getattr(item, "hotel8", None)
                    
                    setattr(item, "hotel8", self)
                    



class Booking:

    def __init__(self, bookingDate: str, checkInDate: str, checkOutDate: str, _numberOfNights: int, hotel8: "Hotel" = None, bookedBy28: "Contact" = None):
        self.bookingDate = bookingDate
        self.checkInDate = checkInDate
        self.checkOutDate = checkOutDate
        self._numberOfNights = _numberOfNights
        self.hotel8 = hotel8
        self.bookedBy28 = bookedBy28
        
        pass
    @property
    def bookingDate(self):
        return self.__bookingDate
    @bookingDate.setter
    def bookingDate(self, bookingDate: str):
        self.__bookingDate = bookingDate

    @property
    def checkOutDate(self):
        return self.__checkOutDate
    @checkOutDate.setter
    def checkOutDate(self, checkOutDate: str):
        self.__checkOutDate = checkOutDate

    @property
    def _numberOfNights(self):
        return self.___numberOfNights
    @_numberOfNights.setter
    def _numberOfNights(self, _numberOfNights: int):
        self.___numberOfNights = _numberOfNights

    @property
    def checkInDate(self):
        return self.__checkInDate
    @checkInDate.setter
    def checkInDate(self, checkInDate: str):
        self.__checkInDate = checkInDate

    @property
    def bookedBy28(self):
        return self.__bookedBy28
    @bookedBy28.setter
    def bookedBy28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__bookedBy28", None)
        self.__bookedBy28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booking29"):
                opp_val = getattr(old_value, "booking29", None)
                if opp_val == self:
                    setattr(old_value, "booking29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booking29"):
                opp_val = getattr(value, "booking29", None)
                setattr(value, "booking29", self)

    @property
    def hotel8(self):
        return self.__hotel8
    @hotel8.setter
    def hotel8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__hotel8", None)
        self.__hotel8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booking9"):
                opp_val = getattr(old_value, "booking9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booking9"):
                opp_val = getattr(value, "booking9", None)
                if opp_val is None:
                    setattr(value, "booking9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class RoomType:

    def __init__(self, name: str, pricePerNight: str, hotel3: "Hotel" = None, room4: set["Room"] = None):
        self.name = name
        self.pricePerNight = pricePerNight
        self.hotel3 = hotel3
        self.room4 = room4 if room4 is not None else set()
        
        pass
    @property
    def pricePerNight(self):
        return self.__pricePerNight
    @pricePerNight.setter
    def pricePerNight(self, pricePerNight: str):
        self.__pricePerNight = pricePerNight

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room4(self):
        return self.__room4
    @room4.setter
    def room4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoomType__room4", None)
        self.__room4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "roomType5"):
                    opp_val = getattr(item, "roomType5", None)
                    
                    if opp_val == self:
                        setattr(item, "roomType5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "roomType5"):
                    opp_val = getattr(item, "roomType5", None)
                    
                    setattr(item, "roomType5", self)
                    

    @property
    def hotel3(self):
        return self.__hotel3
    @hotel3.setter
    def hotel3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoomType__hotel3", None)
        self.__hotel3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roomType2"):
                opp_val = getattr(old_value, "roomType2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roomType2"):
                opp_val = getattr(value, "roomType2", None)
                if opp_val is None:
                    setattr(value, "roomType2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Room:

    def __init__(self, name: str, roomType5: "RoomType" = None, occupant7: "Guest" = None):
        self.name = name
        self.roomType5 = roomType5
        self.occupant7 = occupant7
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def occupant7(self):
        return self.__occupant7
    @occupant7.setter
    def occupant7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__occupant7", None)
        self.__occupant7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occupied6"):
                opp_val = getattr(old_value, "occupied6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occupied6"):
                opp_val = getattr(value, "occupied6", None)
                if opp_val is None:
                    setattr(value, "occupied6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def roomType5(self):
        return self.__roomType5
    @roomType5.setter
    def roomType5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__roomType5", None)
        self.__roomType5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room4"):
                opp_val = getattr(old_value, "room4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room4"):
                opp_val = getattr(value, "room4", None)
                if opp_val is None:
                    setattr(value, "room4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Guest:

    pass
