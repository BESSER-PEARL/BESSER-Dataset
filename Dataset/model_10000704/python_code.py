from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Room:

    def __init__(self, roomID: int, floor: int, door: int, capacity: str, price: float, hotel1: "Hotel" = None, customer3: set["Customer"] = None):
        self.roomID = roomID
        self.floor = floor
        self.door = door
        self.capacity = capacity
        self.price = price
        self.hotel1 = hotel1
        self.customer3 = customer3 if customer3 is not None else set()
        
        pass
    @property
    def roomID(self):
        return self.__roomID
    @roomID.setter
    def roomID(self, roomID: int):
        self.__roomID = roomID

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def floor(self):
        return self.__floor
    @floor.setter
    def floor(self, floor: int):
        self.__floor = floor

    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self, capacity: str):
        self.__capacity = capacity

    @property
    def door(self):
        return self.__door
    @door.setter
    def door(self, door: int):
        self.__door = door

    @property
    def customer3(self):
        return self.__customer3
    @customer3.setter
    def customer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__customer3", None)
        self.__customer3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room2"):
                    opp_val = getattr(item, "room2", None)
                    
                    if opp_val == self:
                        setattr(item, "room2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room2"):
                    opp_val = getattr(item, "room2", None)
                    
                    setattr(item, "room2", self)
                    

    @property
    def hotel1(self):
        return self.__hotel1
    @hotel1.setter
    def hotel1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__hotel1", None)
        self.__hotel1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room0"):
                opp_val = getattr(old_value, "room0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room0"):
                opp_val = getattr(value, "room0", None)
                if opp_val is None:
                    setattr(value, "room0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Hotel:

    def __init__(self, street: str, city: str, zip: int, name: str, phoneNumber: int, website: str, room0: set["Room"] = None):
        self.street = street
        self.city = city
        self.zip = zip
        self.name = name
        self.phoneNumber = phoneNumber
        self.website = website
        self.room0 = room0 if room0 is not None else set()
        
        pass
    @property
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: int):
        self.__phoneNumber = phoneNumber

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def website(self):
        return self.__website
    @website.setter
    def website(self, website: str):
        self.__website = website

    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def zip(self):
        return self.__zip
    @zip.setter
    def zip(self, zip: int):
        self.__zip = zip

    @property
    def street(self):
        return self.__street
    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def room0(self):
        return self.__room0
    @room0.setter
    def room0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hotel__room0", None)
        self.__room0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hotel1"):
                    opp_val = getattr(item, "hotel1", None)
                    
                    if opp_val == self:
                        setattr(item, "hotel1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hotel1"):
                    opp_val = getattr(item, "hotel1", None)
                    
                    setattr(item, "hotel1", self)
                    



class Customer:

    def __init__(self, name: str, phoneNumber: int, ident: str, email: str, roomID: int, room2: "Room" = None):
        self.name = name
        self.phoneNumber = phoneNumber
        self.ident = ident
        self.email = email
        self.roomID = roomID
        self.room2 = room2
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ident(self):
        return self.__ident
    @ident.setter
    def ident(self, ident: str):
        self.__ident = ident

    @property
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: int):
        self.__phoneNumber = phoneNumber

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def roomID(self):
        return self.__roomID
    @roomID.setter
    def roomID(self, roomID: int):
        self.__roomID = roomID

    @property
    def room2(self):
        return self.__room2
    @room2.setter
    def room2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__room2", None)
        self.__room2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer3"):
                opp_val = getattr(old_value, "customer3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer3"):
                opp_val = getattr(value, "customer3", None)
                if opp_val is None:
                    setattr(value, "customer3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

