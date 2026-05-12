from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Payment:

    def __init__(self, Ticketnumber: Ticket, username: Ticket, price: Ticket, date: Ticket, Method: str, ticket7: "Ticket" = None):
        self.Ticketnumber = Ticketnumber
        self.username = username
        self.price = price
        self.date = date
        self.Method = Method
        self.ticket7 = ticket7
        
        pass
    @property
    def Ticketnumber(self):
        return self.__Ticketnumber
    @Ticketnumber.setter
    def Ticketnumber(self, Ticketnumber: Ticket):
        self.__Ticketnumber = Ticketnumber

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: Ticket):
        self.__date = date

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: Ticket):
        self.__username = username

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: Ticket):
        self.__price = price

    @property
    def Method(self):
        return self.__Method
    @Method.setter
    def Method(self, Method: str):
        self.__Method = Method

    @property
    def ticket7(self):
        return self.__ticket7
    @ticket7.setter
    def ticket7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__ticket7", None)
        self.__ticket7 = value
        
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



class Airport:

    def __init__(self, name: str, code: int, location: str, flight5: set["Flight"] = None):
        self.name = name
        self.code = code
        self.location = location
        self.flight5 = flight5 if flight5 is not None else set()
        
        pass
    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self, code: int):
        self.__code = code

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def flight5(self):
        return self.__flight5
    @flight5.setter
    def flight5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Airport__flight5", None)
        self.__flight5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "airport4"):
                    opp_val = getattr(item, "airport4", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "airport4"):
                    opp_val = getattr(item, "airport4", None)
                    
                    if opp_val is None:
                        setattr(item, "airport4", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Ticket:

    def __init__(self, Ticketnumber: int, price: int, date: int, Flightnumber: Flight, class1: str, destination: Flight, arrival: Flight, username: User, age: User, user3: "User" = None, payment6: "Payment" = None, flight9: "Flight" = None):
        self.Ticketnumber = Ticketnumber
        self.price = price
        self.date = date
        self.Flightnumber = Flightnumber
        self.class1 = class1
        self.destination = destination
        self.arrival = arrival
        self.username = username
        self.age = age
        self.user3 = user3
        self.payment6 = payment6
        self.flight9 = flight9
        
        pass
    @property
    def destination(self):
        return self.__destination
    @destination.setter
    def destination(self, destination: Flight):
        self.__destination = destination

    @property
    def arrival(self):
        return self.__arrival
    @arrival.setter
    def arrival(self, arrival: Flight):
        self.__arrival = arrival

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: int):
        self.__date = date

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age: User):
        self.__age = age

    @property
    def Ticketnumber(self):
        return self.__Ticketnumber
    @Ticketnumber.setter
    def Ticketnumber(self, Ticketnumber: int):
        self.__Ticketnumber = Ticketnumber

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: User):
        self.__username = username

    @property
    def Flightnumber(self):
        return self.__Flightnumber
    @Flightnumber.setter
    def Flightnumber(self, Flightnumber: Flight):
        self.__Flightnumber = Flightnumber

    @property
    def class1(self):
        return self.__class1
    @class1.setter
    def class1(self, class1: str):
        self.__class1 = class1

    @property
    def user3(self):
        return self.__user3
    @user3.setter
    def user3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ticket__user3", None)
        self.__user3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ticket2"):
                opp_val = getattr(old_value, "ticket2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ticket2"):
                opp_val = getattr(value, "ticket2", None)
                if opp_val is None:
                    setattr(value, "ticket2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def flight9(self):
        return self.__flight9
    @flight9.setter
    def flight9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ticket__flight9", None)
        self.__flight9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ticket8"):
                opp_val = getattr(old_value, "ticket8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ticket8"):
                opp_val = getattr(value, "ticket8", None)
                if opp_val is None:
                    setattr(value, "ticket8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def payment6(self):
        return self.__payment6
    @payment6.setter
    def payment6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ticket__payment6", None)
        self.__payment6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ticket7"):
                opp_val = getattr(old_value, "ticket7", None)
                if opp_val == self:
                    setattr(old_value, "ticket7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ticket7"):
                opp_val = getattr(value, "ticket7", None)
                setattr(value, "ticket7", self)



class Flight:

    def __init__(self, Flightnumber: int, price: int, time: int, destination: str, arrival: str, date: int, Flightname: str, user1: "User" = None, airport4: set["Airport"] = None, ticket8: set["Ticket"] = None):
        self.Flightnumber = Flightnumber
        self.price = price
        self.time = time
        self.destination = destination
        self.arrival = arrival
        self.date = date
        self.Flightname = Flightname
        self.user1 = user1
        self.airport4 = airport4 if airport4 is not None else set()
        self.ticket8 = ticket8 if ticket8 is not None else set()
        
        pass
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: int):
        self.__date = date

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def arrival(self):
        return self.__arrival
    @arrival.setter
    def arrival(self, arrival: str):
        self.__arrival = arrival

    @property
    def Flightnumber(self):
        return self.__Flightnumber
    @Flightnumber.setter
    def Flightnumber(self, Flightnumber: int):
        self.__Flightnumber = Flightnumber

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def Flightname(self):
        return self.__Flightname
    @Flightname.setter
    def Flightname(self, Flightname: str):
        self.__Flightname = Flightname

    @property
    def destination(self):
        return self.__destination
    @destination.setter
    def destination(self, destination: str):
        self.__destination = destination

    @property
    def ticket8(self):
        return self.__ticket8
    @ticket8.setter
    def ticket8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flight__ticket8", None)
        self.__ticket8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flight9"):
                    opp_val = getattr(item, "flight9", None)
                    
                    if opp_val == self:
                        setattr(item, "flight9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flight9"):
                    opp_val = getattr(item, "flight9", None)
                    
                    setattr(item, "flight9", self)
                    

    @property
    def user1(self):
        return self.__user1
    @user1.setter
    def user1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flight__user1", None)
        self.__user1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flight0"):
                opp_val = getattr(old_value, "flight0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flight0"):
                opp_val = getattr(value, "flight0", None)
                if opp_val is None:
                    setattr(value, "flight0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def airport4(self):
        return self.__airport4
    @airport4.setter
    def airport4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flight__airport4", None)
        self.__airport4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flight5"):
                    opp_val = getattr(item, "flight5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flight5"):
                    opp_val = getattr(item, "flight5", None)
                    
                    if opp_val is None:
                        setattr(item, "flight5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class User:

    def __init__(self, name: str, email: str, phone: int, gender: str, username: str, password: str, age: int, flight0: set["Flight"] = None, ticket2: set["Ticket"] = None):
        self.name = name
        self.email = email
        self.phone = phone
        self.gender = gender
        self.username = username
        self.password = password
        self.age = age
        self.flight0 = flight0 if flight0 is not None else set()
        self.ticket2 = ticket2 if ticket2 is not None else set()
        
        pass
    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: int):
        self.__phone = phone

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def flight0(self):
        return self.__flight0
    @flight0.setter
    def flight0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__flight0", None)
        self.__flight0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user1"):
                    opp_val = getattr(item, "user1", None)
                    
                    if opp_val == self:
                        setattr(item, "user1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user1"):
                    opp_val = getattr(item, "user1", None)
                    
                    setattr(item, "user1", self)
                    

    @property
    def ticket2(self):
        return self.__ticket2
    @ticket2.setter
    def ticket2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__ticket2", None)
        self.__ticket2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user3"):
                    opp_val = getattr(item, "user3", None)
                    
                    if opp_val == self:
                        setattr(item, "user3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user3"):
                    opp_val = getattr(item, "user3", None)
                    
                    setattr(item, "user3", self)
                    

