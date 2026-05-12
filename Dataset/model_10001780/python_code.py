from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Timinglist:

    def __init__(self, flightname: str, time: str, source: str, destination: str, has9: "System" = None):
        self.flightname = flightname
        self.time = time
        self.source = source
        self.destination = destination
        self.has9 = has9
        
        pass
    @property
    def destination(self):
        return self.__destination
    @destination.setter
    def destination(self, destination: str):
        self.__destination = destination

    @property
    def source(self):
        return self.__source
    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def flightname(self):
        return self.__flightname
    @flightname.setter
    def flightname(self, flightname: str):
        self.__flightname = flightname

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def has9(self):
        return self.__has9
    @has9.setter
    def has9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Timinglist__has9", None)
        self.__has9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system8"):
                opp_val = getattr(old_value, "system8", None)
                if opp_val == self:
                    setattr(old_value, "system8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system8"):
                opp_val = getattr(value, "system8", None)
                setattr(value, "system8", self)



class Flightlist:

    def __init__(self, name: str, id: str, system7: "System" = None):
        self.name = name
        self.id = id
        self.system7 = system7
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def system7(self):
        return self.__system7
    @system7.setter
    def system7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flightlist__system7", None)
        self.__system7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "has6"):
                opp_val = getattr(old_value, "has6", None)
                if opp_val == self:
                    setattr(old_value, "has6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "has6"):
                opp_val = getattr(value, "has6", None)
                setattr(value, "has6", self)



class Admin:

    def __init__(self, adminname: str, password: str, mobile: int, type: str, gender: str, system4: "System" = None):
        self.adminname = adminname
        self.password = password
        self.mobile = mobile
        self.type = type
        self.gender = gender
        self.system4 = system4
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def mobile(self):
        return self.__mobile
    @mobile.setter
    def mobile(self, mobile: int):
        self.__mobile = mobile

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def adminname(self):
        return self.__adminname
    @adminname.setter
    def adminname(self, adminname: str):
        self.__adminname = adminname

    @property
    def system4(self):
        return self.__system4
    @system4.setter
    def system4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__system4", None)
        self.__system4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "maintains5"):
                opp_val = getattr(old_value, "maintains5", None)
                if opp_val == self:
                    setattr(old_value, "maintains5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "maintains5"):
                opp_val = getattr(value, "maintains5", None)
                setattr(value, "maintains5", self)



class System:

    def __init__(self, name: str, id: str, session: str, maintains5: "Admin" = None, has6: "Flightlist" = None, system8: "Timinglist" = None, visits3: "User" = None):
        self.name = name
        self.id = id
        self.session = session
        self.maintains5 = maintains5
        self.has6 = has6
        self.system8 = system8
        self.visits3 = visits3
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def session(self):
        return self.__session
    @session.setter
    def session(self, session: str):
        self.__session = session

    @property
    def has6(self):
        return self.__has6
    @has6.setter
    def has6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__has6", None)
        self.__has6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system7"):
                opp_val = getattr(old_value, "system7", None)
                if opp_val == self:
                    setattr(old_value, "system7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system7"):
                opp_val = getattr(value, "system7", None)
                setattr(value, "system7", self)

    @property
    def maintains5(self):
        return self.__maintains5
    @maintains5.setter
    def maintains5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__maintains5", None)
        self.__maintains5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system4"):
                opp_val = getattr(old_value, "system4", None)
                if opp_val == self:
                    setattr(old_value, "system4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system4"):
                opp_val = getattr(value, "system4", None)
                setattr(value, "system4", self)

    @property
    def system8(self):
        return self.__system8
    @system8.setter
    def system8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__system8", None)
        self.__system8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "has9"):
                opp_val = getattr(old_value, "has9", None)
                if opp_val == self:
                    setattr(old_value, "has9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "has9"):
                opp_val = getattr(value, "has9", None)
                setattr(value, "has9", self)

    @property
    def visits3(self):
        return self.__visits3
    @visits3.setter
    def visits3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System__visits3", None)
        self.__visits3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system2"):
                opp_val = getattr(old_value, "system2", None)
                if opp_val == self:
                    setattr(old_value, "system2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system2"):
                opp_val = getattr(value, "system2", None)
                setattr(value, "system2", self)



class Ticket:

    def __init__(self, ticketid: str, flightname: str, passengername: str, price: int, source: str, destination: str, system1: set["User"] = None):
        self.ticketid = ticketid
        self.flightname = flightname
        self.passengername = passengername
        self.price = price
        self.source = source
        self.destination = destination
        self.system1 = system1 if system1 is not None else set()
        
        pass
    @property
    def passengername(self):
        return self.__passengername
    @passengername.setter
    def passengername(self, passengername: str):
        self.__passengername = passengername

    @property
    def flightname(self):
        return self.__flightname
    @flightname.setter
    def flightname(self, flightname: str):
        self.__flightname = flightname

    @property
    def source(self):
        return self.__source
    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def ticketid(self):
        return self.__ticketid
    @ticketid.setter
    def ticketid(self, ticketid: str):
        self.__ticketid = ticketid

    @property
    def destination(self):
        return self.__destination
    @destination.setter
    def destination(self, destination: str):
        self.__destination = destination

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def system1(self):
        return self.__system1
    @system1.setter
    def system1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ticket__system1", None)
        self.__system1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "books0"):
                    opp_val = getattr(item, "books0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "books0"):
                    opp_val = getattr(item, "books0", None)
                    
                    if opp_val is None:
                        setattr(item, "books0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class User:

    def __init__(self, username: str, password: str, gender: str, address: str, phoneno: int, books0: set["Ticket"] = None, system2: "System" = None):
        self.username = username
        self.password = password
        self.gender = gender
        self.address = address
        self.phoneno = phoneno
        self.books0 = books0 if books0 is not None else set()
        self.system2 = system2
        
        pass
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def phoneno(self):
        return self.__phoneno
    @phoneno.setter
    def phoneno(self, phoneno: int):
        self.__phoneno = phoneno

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def books0(self):
        return self.__books0
    @books0.setter
    def books0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__books0", None)
        self.__books0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "system1"):
                    opp_val = getattr(item, "system1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "system1"):
                    opp_val = getattr(item, "system1", None)
                    
                    if opp_val is None:
                        setattr(item, "system1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def system2(self):
        return self.__system2
    @system2.setter
    def system2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__system2", None)
        self.__system2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "visits3"):
                opp_val = getattr(old_value, "visits3", None)
                if opp_val == self:
                    setattr(old_value, "visits3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "visits3"):
                opp_val = getattr(value, "visits3", None)
                setattr(value, "visits3", self)

