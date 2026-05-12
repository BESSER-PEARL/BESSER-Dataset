from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Service:

    def __init__(self, name: str, description: str, basePrice: str, hotel2: "Hotel" = None):
        self.name = name
        self.description = description
        self.basePrice = basePrice
        self.hotel2 = hotel2
        
        pass
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
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

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



class Room:

    def __init__(self, room_id: int, room_name: str, room_rent_night: float, room_no_bedroom: int, room_no_bathroom: int, room_size_interior: int, hotel1: "Hotel" = None, customer5: set["Users"] = None):
        self.room_id = room_id
        self.room_name = room_name
        self.room_rent_night = room_rent_night
        self.room_no_bedroom = room_no_bedroom
        self.room_no_bathroom = room_no_bathroom
        self.room_size_interior = room_size_interior
        self.hotel1 = hotel1
        self.customer5 = customer5 if customer5 is not None else set()
        
        pass
    @property
    def room_no_bathroom(self):
        return self.__room_no_bathroom
    @room_no_bathroom.setter
    def room_no_bathroom(self, room_no_bathroom: int):
        self.__room_no_bathroom = room_no_bathroom

    @property
    def room_name(self):
        return self.__room_name
    @room_name.setter
    def room_name(self, room_name: str):
        self.__room_name = room_name

    @property
    def room_no_bedroom(self):
        return self.__room_no_bedroom
    @room_no_bedroom.setter
    def room_no_bedroom(self, room_no_bedroom: int):
        self.__room_no_bedroom = room_no_bedroom

    @property
    def room_rent_night(self):
        return self.__room_rent_night
    @room_rent_night.setter
    def room_rent_night(self, room_rent_night: float):
        self.__room_rent_night = room_rent_night

    @property
    def room_id(self):
        return self.__room_id
    @room_id.setter
    def room_id(self, room_id: int):
        self.__room_id = room_id

    @property
    def room_size_interior(self):
        return self.__room_size_interior
    @room_size_interior.setter
    def room_size_interior(self, room_size_interior: int):
        self.__room_size_interior = room_size_interior

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

    def __init__(self, name: str, street: str, city: str, zip: int, coordinates: int, phoneNumber: int, website: str, room0: set["Room"] = None, service3: set["Service"] = None):
        self.name = name
        self.street = street
        self.city = city
        self.zip = zip
        self.coordinates = coordinates
        self.phoneNumber = phoneNumber
        self.website = website
        self.room0 = room0 if room0 is not None else set()
        self.service3 = service3 if service3 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def street(self):
        return self.__street
    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: int):
        self.__phoneNumber = phoneNumber

    @property
    def coordinates(self):
        return self.__coordinates
    @coordinates.setter
    def coordinates(self, coordinates: int):
        self.__coordinates = coordinates

    @property
    def zip(self):
        return self.__zip
    @zip.setter
    def zip(self, zip: int):
        self.__zip = zip

    @property
    def website(self):
        return self.__website
    @website.setter
    def website(self, website: str):
        self.__website = website

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
                    



class Users:

    def __init__(self, user_mail: str, first_name: str, last_name: int, user_role: str, user_address: str, user_phone_no: int, user_addr_state: str, user_addr_city: str, user_address1: str, room4: "Room" = None):
        self.user_mail = user_mail
        self.first_name = first_name
        self.last_name = last_name
        self.user_role = user_role
        self.user_address = user_address
        self.user_phone_no = user_phone_no
        self.user_addr_state = user_addr_state
        self.user_addr_city = user_addr_city
        self.user_address1 = user_address1
        self.room4 = room4
        
        pass
    @property
    def user_role(self):
        return self.__user_role
    @user_role.setter
    def user_role(self, user_role: str):
        self.__user_role = user_role

    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, last_name: int):
        self.__last_name = last_name

    @property
    def user_phone_no(self):
        return self.__user_phone_no
    @user_phone_no.setter
    def user_phone_no(self, user_phone_no: int):
        self.__user_phone_no = user_phone_no

    @property
    def user_address(self):
        return self.__user_address
    @user_address.setter
    def user_address(self, user_address: str):
        self.__user_address = user_address

    @property
    def user_addr_city(self):
        return self.__user_addr_city
    @user_addr_city.setter
    def user_addr_city(self, user_addr_city: str):
        self.__user_addr_city = user_addr_city

    @property
    def user_mail(self):
        return self.__user_mail
    @user_mail.setter
    def user_mail(self, user_mail: str):
        self.__user_mail = user_mail

    @property
    def user_addr_state(self):
        return self.__user_addr_state
    @user_addr_state.setter
    def user_addr_state(self, user_addr_state: str):
        self.__user_addr_state = user_addr_state

    @property
    def user_address1(self):
        return self.__user_address1
    @user_address1.setter
    def user_address1(self, user_address1: str):
        self.__user_address1 = user_address1

    @property
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self, first_name: str):
        self.__first_name = first_name

    @property
    def room4(self):
        return self.__room4
    @room4.setter
    def room4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Users__room4", None)
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

