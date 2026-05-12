from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class User:

    def __init__(self, Name: str, phn_no: int, id: int, mail_id: str, address: str, password: int, guest10: "Guest" = None):
        self.Name = Name
        self.phn_no = phn_no
        self.id = id
        self.mail_id = mail_id
        self.address = address
        self.password = password
        self.guest10 = guest10
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: int):
        self.__password = password

    @property
    def mail_id(self):
        return self.__mail_id
    @mail_id.setter
    def mail_id(self, mail_id: str):
        self.__mail_id = mail_id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def phn_no(self):
        return self.__phn_no
    @phn_no.setter
    def phn_no(self, phn_no: int):
        self.__phn_no = phn_no

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def guest10(self):
        return self.__guest10
    @guest10.setter
    def guest10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__guest10", None)
        self.__guest10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user11"):
                opp_val = getattr(old_value, "user11", None)
                if opp_val == self:
                    setattr(old_value, "user11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user11"):
                opp_val = getattr(value, "user11", None)
                setattr(value, "user11", self)



class Payment:

    def __init__(self, amount: int, card_no: int, cvv: int, card_type: str, password: int, guest7: "Guest" = None, manager13: "Manager" = None):
        self.amount = amount
        self.card_no = card_no
        self.cvv = cvv
        self.card_type = card_type
        self.password = password
        self.guest7 = guest7
        self.manager13 = manager13
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: int):
        self.__password = password

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount

    @property
    def card_type(self):
        return self.__card_type
    @card_type.setter
    def card_type(self, card_type: str):
        self.__card_type = card_type

    @property
    def card_no(self):
        return self.__card_no
    @card_no.setter
    def card_no(self, card_no: int):
        self.__card_no = card_no

    @property
    def cvv(self):
        return self.__cvv
    @cvv.setter
    def cvv(self, cvv: int):
        self.__cvv = cvv

    @property
    def guest7(self):
        return self.__guest7
    @guest7.setter
    def guest7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__guest7", None)
        self.__guest7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment6"):
                opp_val = getattr(old_value, "payment6", None)
                if opp_val == self:
                    setattr(old_value, "payment6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment6"):
                opp_val = getattr(value, "payment6", None)
                setattr(value, "payment6", self)

    @property
    def manager13(self):
        return self.__manager13
    @manager13.setter
    def manager13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__manager13", None)
        self.__manager13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment12"):
                opp_val = getattr(old_value, "payment12", None)
                if opp_val == self:
                    setattr(old_value, "payment12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment12"):
                opp_val = getattr(value, "payment12", None)
                setattr(value, "payment12", self)



class City:

    def __init__(self, city: str, id: int, hotels0: "Hotels" = None):
        self.city = city
        self.id = id
        self.hotels0 = hotels0
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def hotels0(self):
        return self.__hotels0
    @hotels0.setter
    def hotels0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_City__hotels0", None)
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



class Guest:

    def __init__(self, Nmae: str, id: int, Phone_no_: int, address: str, rooms5: "Rooms" = None, payment6: "Payment" = None, hotels9: "Hotels" = None, user11: "User" = None, manager15: "Manager" = None):
        self.Nmae = Nmae
        self.id = id
        self.Phone_no_ = Phone_no_
        self.address = address
        self.rooms5 = rooms5
        self.payment6 = payment6
        self.hotels9 = hotels9
        self.user11 = user11
        self.manager15 = manager15
        
        pass
    @property
    def Phone_no_(self):
        return self.__Phone_no_
    @Phone_no_.setter
    def Phone_no_(self, Phone_no_: int):
        self.__Phone_no_ = Phone_no_

    @property
    def Nmae(self):
        return self.__Nmae
    @Nmae.setter
    def Nmae(self, Nmae: str):
        self.__Nmae = Nmae

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def hotels9(self):
        return self.__hotels9
    @hotels9.setter
    def hotels9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Guest__hotels9", None)
        self.__hotels9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "guest8"):
                opp_val = getattr(old_value, "guest8", None)
                if opp_val == self:
                    setattr(old_value, "guest8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "guest8"):
                opp_val = getattr(value, "guest8", None)
                setattr(value, "guest8", self)

    @property
    def manager15(self):
        return self.__manager15
    @manager15.setter
    def manager15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Guest__manager15", None)
        self.__manager15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "guest14"):
                opp_val = getattr(old_value, "guest14", None)
                if opp_val == self:
                    setattr(old_value, "guest14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "guest14"):
                opp_val = getattr(value, "guest14", None)
                setattr(value, "guest14", self)

    @property
    def user11(self):
        return self.__user11
    @user11.setter
    def user11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Guest__user11", None)
        self.__user11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "guest10"):
                opp_val = getattr(old_value, "guest10", None)
                if opp_val == self:
                    setattr(old_value, "guest10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "guest10"):
                opp_val = getattr(value, "guest10", None)
                setattr(value, "guest10", self)

    @property
    def payment6(self):
        return self.__payment6
    @payment6.setter
    def payment6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Guest__payment6", None)
        self.__payment6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "guest7"):
                opp_val = getattr(old_value, "guest7", None)
                if opp_val == self:
                    setattr(old_value, "guest7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "guest7"):
                opp_val = getattr(value, "guest7", None)
                setattr(value, "guest7", self)

    @property
    def rooms5(self):
        return self.__rooms5
    @rooms5.setter
    def rooms5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Guest__rooms5", None)
        self.__rooms5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "guest4"):
                opp_val = getattr(old_value, "guest4", None)
                if opp_val == self:
                    setattr(old_value, "guest4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "guest4"):
                opp_val = getattr(value, "guest4", None)
                setattr(value, "guest4", self)



class Rooms:

    def __init__(self, id: int, name: str, room_description: str, price: int, hotels3: "Hotels" = None, guest4: "Guest" = None):
        self.id = id
        self.name = name
        self.room_description = room_description
        self.price = price
        self.hotels3 = hotels3
        self.guest4 = guest4
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def room_description(self):
        return self.__room_description
    @room_description.setter
    def room_description(self, room_description: str):
        self.__room_description = room_description

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def guest4(self):
        return self.__guest4
    @guest4.setter
    def guest4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rooms__guest4", None)
        self.__guest4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rooms5"):
                opp_val = getattr(old_value, "rooms5", None)
                if opp_val == self:
                    setattr(old_value, "rooms5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rooms5"):
                opp_val = getattr(value, "rooms5", None)
                setattr(value, "rooms5", self)

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



class Hotels:

    def __init__(self, id: int, name: int, location: int, city1: "City" = None, rooms2: "Rooms" = None, guest8: "Guest" = None):
        self.id = id
        self.name = name
        self.location = location
        self.city1 = city1
        self.rooms2 = rooms2
        self.guest8 = guest8
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: int):
        self.__name = name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: int):
        self.__location = location

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

    @property
    def guest8(self):
        return self.__guest8
    @guest8.setter
    def guest8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hotels__guest8", None)
        self.__guest8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hotels9"):
                opp_val = getattr(old_value, "hotels9", None)
                if opp_val == self:
                    setattr(old_value, "hotels9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hotels9"):
                opp_val = getattr(value, "hotels9", None)
                setattr(value, "hotels9", self)



class Manager:

    def __init__(self, Name: str, ID: int, Phn_no_: Manager, Address: str, payment12: "Payment" = None, guest14: "Guest" = None):
        self.Name = Name
        self.ID = ID
        self.Phn_no_ = Phn_no_
        self.Address = Address
        self.payment12 = payment12
        self.guest14 = guest14
        
        pass
    @property
    def Phn_no_(self):
        return self.__Phn_no_
    @Phn_no_.setter
    def Phn_no_(self, Phn_no_: Manager):
        self.__Phn_no_ = Phn_no_

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def payment12(self):
        return self.__payment12
    @payment12.setter
    def payment12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager__payment12", None)
        self.__payment12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manager13"):
                opp_val = getattr(old_value, "manager13", None)
                if opp_val == self:
                    setattr(old_value, "manager13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manager13"):
                opp_val = getattr(value, "manager13", None)
                setattr(value, "manager13", self)

    @property
    def guest14(self):
        return self.__guest14
    @guest14.setter
    def guest14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager__guest14", None)
        self.__guest14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manager15"):
                opp_val = getattr(old_value, "manager15", None)
                if opp_val == self:
                    setattr(old_value, "manager15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manager15"):
                opp_val = getattr(value, "manager15", None)
                setattr(value, "manager15", self)

