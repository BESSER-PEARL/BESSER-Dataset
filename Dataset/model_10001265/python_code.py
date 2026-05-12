from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Room:

    def __init__(self, floor: int, door: int, capacity: str, price: float, hotel1: "Hotel" = None, customer5: set["Customer"] = None):
        self.floor = floor
        self.door = door
        self.capacity = capacity
        self.price = price
        self.hotel1 = hotel1
        self.customer5 = customer5 if customer5 is not None else set()
        
        pass
    @property
    def door(self):
        return self.__door
    @door.setter
    def door(self, door: int):
        self.__door = door

    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self, capacity: str):
        self.__capacity = capacity

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

    @property
    def customer5(self):
        return self.__customer5
    @customer5.setter
    def customer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__customer5", None)
        self.__customer5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room4"):
                    opp_val = getattr(item, "room4", None)
                    
                    if opp_val == self:
                        setattr(item, "room4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room4"):
                    opp_val = getattr(item, "room4", None)
                    
                    setattr(item, "room4", self)
                    



class Hotel:

    def __init__(self, street: str, city: str, zip: int, coordinates: int, name: str, phoneNumber: int, website: str, room0: set["Room"] = None, service3: set["Service"] = None):
        self.street = street
        self.city = city
        self.zip = zip
        self.coordinates = coordinates
        self.name = name
        self.phoneNumber = phoneNumber
        self.website = website
        self.room0 = room0 if room0 is not None else set()
        self.service3 = service3 if service3 is not None else set()
        
        pass
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def coordinates(self):
        return self.__coordinates
    @coordinates.setter
    def coordinates(self, coordinates: int):
        self.__coordinates = coordinates

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
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: int):
        self.__phoneNumber = phoneNumber

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
                    

    @property
    def service3(self):
        return self.__service3
    @service3.setter
    def service3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hotel__service3", None)
        self.__service3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hotel2"):
                    opp_val = getattr(item, "hotel2", None)
                    
                    if opp_val == self:
                        setattr(item, "hotel2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hotel2"):
                    opp_val = getattr(item, "hotel2", None)
                    
                    setattr(item, "hotel2", self)
                    



class Customer:

    def __init__(self, name: str, surname: str, phoneNumber: int, ident: str, email: str, room4: "Room" = None):
        self.name = name
        self.surname = surname
        self.phoneNumber = phoneNumber
        self.ident = ident
        self.email = email
        self.room4 = room4
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname

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
    def ident(self):
        return self.__ident
    @ident.setter
    def ident(self, ident: str):
        self.__ident = ident

    @property
    def room4(self):
        return self.__room4
    @room4.setter
    def room4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__room4", None)
        self.__room4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer5"):
                opp_val = getattr(old_value, "customer5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer5"):
                opp_val = getattr(value, "customer5", None)
                if opp_val is None:
                    setattr(value, "customer5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Service:

    def __init__(self, name: str, description: str, basePrice: str, hotel2: "Hotel" = None):
        self.name = name
        self.description = description
        self.basePrice = basePrice
        self.hotel2 = hotel2
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def basePrice(self):
        return self.__basePrice
    @basePrice.setter
    def basePrice(self, basePrice: str):
        self.__basePrice = basePrice

    @property
    def hotel2(self):
        return self.__hotel2
    @hotel2.setter
    def hotel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Service__hotel2", None)
        self.__hotel2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service3"):
                opp_val = getattr(old_value, "service3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service3"):
                opp_val = getattr(value, "service3", None)
                if opp_val is None:
                    setattr(value, "service3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

