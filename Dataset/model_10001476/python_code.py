from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Admin:

    def __init__(self, username: str, password: str, event10: "Event" = None):
        self.username = username
        self.password = password
        self.event10 = event10
        
        pass
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def event10(self):
        return self.__event10
    @event10.setter
    def event10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__event10", None)
        self.__event10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin11"):
                opp_val = getattr(old_value, "admin11", None)
                if opp_val == self:
                    setattr(old_value, "admin11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin11"):
                opp_val = getattr(value, "admin11", None)
                setattr(value, "admin11", self)



class Commercial_Events:

    pass


class Birthday_Parties:

    pass


class Weddings:

    pass


class Refreshment:

    pass


class Event:

    def __init__(self, eventid: int, eventname: str, date: int, eventhead: Eventhead, amount: int, eventype: str, client3: "Client" = None, volunteer5: "Volunteer" = None, eventhead26: "Eventhead" = None, refreshment8: "Refreshment" = None, admin11: "Admin" = None):
        self.eventid = eventid
        self.eventname = eventname
        self.date = date
        self.eventhead = eventhead
        self.amount = amount
        self.eventype = eventype
        self.client3 = client3
        self.volunteer5 = volunteer5
        self.eventhead26 = eventhead26
        self.refreshment8 = refreshment8
        self.admin11 = admin11
        
        pass
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount

    @property
    def eventhead(self):
        return self.__eventhead
    @eventhead.setter
    def eventhead(self, eventhead: Eventhead):
        self.__eventhead = eventhead

    @property
    def eventid(self):
        return self.__eventid
    @eventid.setter
    def eventid(self, eventid: int):
        self.__eventid = eventid

    @property
    def eventype(self):
        return self.__eventype
    @eventype.setter
    def eventype(self, eventype: str):
        self.__eventype = eventype

    @property
    def eventname(self):
        return self.__eventname
    @eventname.setter
    def eventname(self, eventname: str):
        self.__eventname = eventname

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: int):
        self.__date = date

    @property
    def admin11(self):
        return self.__admin11
    @admin11.setter
    def admin11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Event__admin11", None)
        self.__admin11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "event10"):
                opp_val = getattr(old_value, "event10", None)
                if opp_val == self:
                    setattr(old_value, "event10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "event10"):
                opp_val = getattr(value, "event10", None)
                setattr(value, "event10", self)

    @property
    def volunteer5(self):
        return self.__volunteer5
    @volunteer5.setter
    def volunteer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Event__volunteer5", None)
        self.__volunteer5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "event4"):
                opp_val = getattr(old_value, "event4", None)
                if opp_val == self:
                    setattr(old_value, "event4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "event4"):
                opp_val = getattr(value, "event4", None)
                setattr(value, "event4", self)

    @property
    def eventhead26(self):
        return self.__eventhead26
    @eventhead26.setter
    def eventhead26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Event__eventhead26", None)
        self.__eventhead26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "event7"):
                opp_val = getattr(old_value, "event7", None)
                if opp_val == self:
                    setattr(old_value, "event7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "event7"):
                opp_val = getattr(value, "event7", None)
                setattr(value, "event7", self)

    @property
    def client3(self):
        return self.__client3
    @client3.setter
    def client3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Event__client3", None)
        self.__client3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "event2"):
                opp_val = getattr(old_value, "event2", None)
                if opp_val == self:
                    setattr(old_value, "event2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "event2"):
                opp_val = getattr(value, "event2", None)
                setattr(value, "event2", self)

    @property
    def refreshment8(self):
        return self.__refreshment8
    @refreshment8.setter
    def refreshment8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Event__refreshment8", None)
        self.__refreshment8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "event9"):
                opp_val = getattr(old_value, "event9", None)
                if opp_val == self:
                    setattr(old_value, "event9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "event9"):
                opp_val = getattr(value, "event9", None)
                setattr(value, "event9", self)



class Payment:

    def __init__(self, amout: int, paytype: str, status: str, client1: "Client" = None):
        self.amout = amout
        self.paytype = paytype
        self.status = status
        self.client1 = client1
        
        pass
    @property
    def amout(self):
        return self.__amout
    @amout.setter
    def amout(self, amout: int):
        self.__amout = amout

    @property
    def paytype(self):
        return self.__paytype
    @paytype.setter
    def paytype(self, paytype: str):
        self.__paytype = paytype

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def client1(self):
        return self.__client1
    @client1.setter
    def client1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__client1", None)
        self.__client1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment20"):
                opp_val = getattr(old_value, "payment20", None)
                if opp_val == self:
                    setattr(old_value, "payment20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment20"):
                opp_val = getattr(value, "payment20", None)
                setattr(value, "payment20", self)



class Volunteer:

    def __init__(self, id: int, event4: "Event" = None):
        self.id = id
        self.event4 = event4
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def event4(self):
        return self.__event4
    @event4.setter
    def event4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Volunteer__event4", None)
        self.__event4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "volunteer5"):
                opp_val = getattr(old_value, "volunteer5", None)
                if opp_val == self:
                    setattr(old_value, "volunteer5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "volunteer5"):
                opp_val = getattr(value, "volunteer5", None)
                setattr(value, "volunteer5", self)



class Eventhead:

    def __init__(self, id: int, event7: "Event" = None):
        self.id = id
        self.event7 = event7
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def event7(self):
        return self.__event7
    @event7.setter
    def event7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Eventhead__event7", None)
        self.__event7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eventhead26"):
                opp_val = getattr(old_value, "eventhead26", None)
                if opp_val == self:
                    setattr(old_value, "eventhead26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eventhead26"):
                opp_val = getattr(value, "eventhead26", None)
                setattr(value, "eventhead26", self)



class Client:

    def __init__(self, id: int, payment20: "Payment" = None, event2: "Event" = None):
        self.id = id
        self.payment20 = payment20
        self.event2 = event2
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def payment20(self):
        return self.__payment20
    @payment20.setter
    def payment20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Client__payment20", None)
        self.__payment20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "client1"):
                opp_val = getattr(old_value, "client1", None)
                if opp_val == self:
                    setattr(old_value, "client1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "client1"):
                opp_val = getattr(value, "client1", None)
                setattr(value, "client1", self)

    @property
    def event2(self):
        return self.__event2
    @event2.setter
    def event2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Client__event2", None)
        self.__event2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "client3"):
                opp_val = getattr(old_value, "client3", None)
                if opp_val == self:
                    setattr(old_value, "client3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "client3"):
                opp_val = getattr(value, "client3", None)
                setattr(value, "client3", self)



class User:

    def __init__(self, username: str, fname: str, lname: str, password: str):
        self.username = username
        self.fname = fname
        self.lname = lname
        self.password = password
        
        pass
    @property
    def lname(self):
        return self.__lname
    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def fname(self):
        return self.__fname
    @fname.setter
    def fname(self, fname: str):
        self.__fname = fname

