from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class occupancy:

    def __init__(self, booking_id: int, occupancy_Booking_010: "Booking" = None):
        self.booking_id = booking_id
        self.occupancy_Booking_010 = occupancy_Booking_010
        
        pass
    @property
    def booking_id(self):
        return self.__booking_id
    @booking_id.setter
    def booking_id(self, booking_id: int):
        self.__booking_id = booking_id

    @property
    def occupancy_Booking_010(self):
        return self.__occupancy_Booking_010
    @occupancy_Booking_010.setter
    def occupancy_Booking_010(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occupancy__occupancy_Booking_010", None)
        self.__occupancy_Booking_010 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occupancy_Booking_111"):
                opp_val = getattr(old_value, "occupancy_Booking_111", None)
                if opp_val == self:
                    setattr(old_value, "occupancy_Booking_111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occupancy_Booking_111"):
                opp_val = getattr(value, "occupancy_Booking_111", None)
                setattr(value, "occupancy_Booking_111", self)



class Booking:

    def __init__(self, booking_id: int, user_id: int, guest_name: int, guest_id: int, guestphn_no: int, guest_adress: str, occupancy_Booking_111: "occupancy" = None, User_Booking_15: "User" = None, rooms9: "Rooms" = None):
        self.booking_id = booking_id
        self.user_id = user_id
        self.guest_name = guest_name
        self.guest_id = guest_id
        self.guestphn_no = guestphn_no
        self.guest_adress = guest_adress
        self.occupancy_Booking_111 = occupancy_Booking_111
        self.User_Booking_15 = User_Booking_15
        self.rooms9 = rooms9
        
        pass
    @property
    def guest_adress(self):
        return self.__guest_adress
    @guest_adress.setter
    def guest_adress(self, guest_adress: str):
        self.__guest_adress = guest_adress

    @property
    def guest_name(self):
        return self.__guest_name
    @guest_name.setter
    def guest_name(self, guest_name: int):
        self.__guest_name = guest_name

    @property
    def guestphn_no(self):
        return self.__guestphn_no
    @guestphn_no.setter
    def guestphn_no(self, guestphn_no: int):
        self.__guestphn_no = guestphn_no

    @property
    def booking_id(self):
        return self.__booking_id
    @booking_id.setter
    def booking_id(self, booking_id: int):
        self.__booking_id = booking_id

    @property
    def guest_id(self):
        return self.__guest_id
    @guest_id.setter
    def guest_id(self, guest_id: int):
        self.__guest_id = guest_id

    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    @property
    def occupancy_Booking_111(self):
        return self.__occupancy_Booking_111
    @occupancy_Booking_111.setter
    def occupancy_Booking_111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__occupancy_Booking_111", None)
        self.__occupancy_Booking_111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occupancy_Booking_010"):
                opp_val = getattr(old_value, "occupancy_Booking_010", None)
                if opp_val == self:
                    setattr(old_value, "occupancy_Booking_010", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occupancy_Booking_010"):
                opp_val = getattr(value, "occupancy_Booking_010", None)
                setattr(value, "occupancy_Booking_010", self)

    @property
    def User_Booking_15(self):
        return self.__User_Booking_15
    @User_Booking_15.setter
    def User_Booking_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__User_Booking_15", None)
        self.__User_Booking_15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User_Booking_04"):
                opp_val = getattr(old_value, "User_Booking_04", None)
                if opp_val == self:
                    setattr(old_value, "User_Booking_04", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User_Booking_04"):
                opp_val = getattr(value, "User_Booking_04", None)
                setattr(value, "User_Booking_04", self)

    @property
    def rooms9(self):
        return self.__rooms9
    @rooms9.setter
    def rooms9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__rooms9", None)
        self.__rooms9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booking8"):
                opp_val = getattr(old_value, "booking8", None)
                if opp_val == self:
                    setattr(old_value, "booking8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booking8"):
                opp_val = getattr(value, "booking8", None)
                setattr(value, "booking8", self)



class User:

    def __init__(self, Name: str, phn_no: int, id: int, mail_id: str, address: str, password: int, User_Booking_04: "Booking" = None):
        self.Name = Name
        self.phn_no = phn_no
        self.id = id
        self.mail_id = mail_id
        self.address = address
        self.password = password
        self.User_Booking_04 = User_Booking_04
        
        pass
    @property
    def phn_no(self):
        return self.__phn_no
    @phn_no.setter
    def phn_no(self, phn_no: int):
        self.__phn_no = phn_no

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def mail_id(self):
        return self.__mail_id
    @mail_id.setter
    def mail_id(self, mail_id: str):
        self.__mail_id = mail_id

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: int):
        self.__password = password

    @property
    def User_Booking_04(self):
        return self.__User_Booking_04
    @User_Booking_04.setter
    def User_Booking_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__User_Booking_04", None)
        self.__User_Booking_04 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User_Booking_15"):
                opp_val = getattr(old_value, "User_Booking_15", None)
                if opp_val == self:
                    setattr(old_value, "User_Booking_15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User_Booking_15"):
                opp_val = getattr(value, "User_Booking_15", None)
                setattr(value, "User_Booking_15", self)



class Location:

    def __init__(self, loc_name: str, loc_id: int, attribute: str, hotels0: "Hotels" = None):
        self.loc_name = loc_name
        self.loc_id = loc_id
        self.attribute = attribute
        self.hotels0 = hotels0
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def loc_name(self):
        return self.__loc_name
    @loc_name.setter
    def loc_name(self, loc_name: str):
        self.__loc_name = loc_name

    @property
    def loc_id(self):
        return self.__loc_id
    @loc_id.setter
    def loc_id(self, loc_id: int):
        self.__loc_id = loc_id

    @property
    def hotels0(self):
        return self.__hotels0
    @hotels0.setter
    def hotels0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Location__hotels0", None)
        self.__hotels0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "city1"):
                opp_val = getattr(old_value, "city1", None)
                if opp_val == self:
                    setattr(old_value, "city1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "city1"):
                opp_val = getattr(value, "city1", None)
                setattr(value, "city1", self)



class Rooms:

    def __init__(self, id: int, name: str, room_description: str, price: int, checkin_date: int, checkout_date: int, hotels3: "Hotels" = None, booking8: "Booking" = None):
        self.id = id
        self.name = name
        self.room_description = room_description
        self.price = price
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date
        self.hotels3 = hotels3
        self.booking8 = booking8
        
        pass
    @property
    def room_description(self):
        return self.__room_description
    @room_description.setter
    def room_description(self, room_description: str):
        self.__room_description = room_description

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def checkout_date(self):
        return self.__checkout_date
    @checkout_date.setter
    def checkout_date(self, checkout_date: int):
        self.__checkout_date = checkout_date

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def checkin_date(self):
        return self.__checkin_date
    @checkin_date.setter
    def checkin_date(self, checkin_date: int):
        self.__checkin_date = checkin_date

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hotels3(self):
        return self.__hotels3
    @hotels3.setter
    def hotels3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rooms__hotels3", None)
        self.__hotels3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rooms2"):
                opp_val = getattr(old_value, "rooms2", None)
                if opp_val == self:
                    setattr(old_value, "rooms2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rooms2"):
                opp_val = getattr(value, "rooms2", None)
                setattr(value, "rooms2", self)

    @property
    def booking8(self):
        return self.__booking8
    @booking8.setter
    def booking8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rooms__booking8", None)
        self.__booking8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rooms9"):
                opp_val = getattr(old_value, "rooms9", None)
                if opp_val == self:
                    setattr(old_value, "rooms9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rooms9"):
                opp_val = getattr(value, "rooms9", None)
                setattr(value, "rooms9", self)



class Hotels:

    def __init__(self, id: int, name: int, hotel_description: int, city1: "Location" = None, rooms2: "Rooms" = None, owner6: "Owner" = None):
        self.id = id
        self.name = name
        self.hotel_description = hotel_description
        self.city1 = city1
        self.rooms2 = rooms2
        self.owner6 = owner6
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: int):
        self.__name = name

    @property
    def hotel_description(self):
        return self.__hotel_description
    @hotel_description.setter
    def hotel_description(self, hotel_description: int):
        self.__hotel_description = hotel_description

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def owner6(self):
        return self.__owner6
    @owner6.setter
    def owner6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hotels__owner6", None)
        self.__owner6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hotels7"):
                opp_val = getattr(old_value, "hotels7", None)
                if opp_val == self:
                    setattr(old_value, "hotels7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hotels7"):
                opp_val = getattr(value, "hotels7", None)
                setattr(value, "hotels7", self)

    @property
    def city1(self):
        return self.__city1
    @city1.setter
    def city1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hotels__city1", None)
        self.__city1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hotels0"):
                opp_val = getattr(old_value, "hotels0", None)
                if opp_val == self:
                    setattr(old_value, "hotels0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hotels0"):
                opp_val = getattr(value, "hotels0", None)
                setattr(value, "hotels0", self)

    @property
    def rooms2(self):
        return self.__rooms2
    @rooms2.setter
    def rooms2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hotels__rooms2", None)
        self.__rooms2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hotels3"):
                opp_val = getattr(old_value, "hotels3", None)
                if opp_val == self:
                    setattr(old_value, "hotels3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hotels3"):
                opp_val = getattr(value, "hotels3", None)
                setattr(value, "hotels3", self)



class Owner:

    def __init__(self, Name: str, ID: int, Phn_no_: Owner, Address: str, email_id: int, password: int, hotels7: "Hotels" = None):
        self.Name = Name
        self.ID = ID
        self.Phn_no_ = Phn_no_
        self.Address = Address
        self.email_id = email_id
        self.password = password
        self.hotels7 = hotels7
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Phn_no_(self):
        return self.__Phn_no_
    @Phn_no_.setter
    def Phn_no_(self, Phn_no_: Owner):
        self.__Phn_no_ = Phn_no_

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: int):
        self.__password = password

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def email_id(self):
        return self.__email_id
    @email_id.setter
    def email_id(self, email_id: int):
        self.__email_id = email_id

    @property
    def hotels7(self):
        return self.__hotels7
    @hotels7.setter
    def hotels7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Owner__hotels7", None)
        self.__hotels7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner6"):
                opp_val = getattr(old_value, "owner6", None)
                if opp_val == self:
                    setattr(old_value, "owner6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner6"):
                opp_val = getattr(value, "owner6", None)
                setattr(value, "owner6", self)

