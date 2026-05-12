from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Registration:

    pass


class EventType:

    def __init__(self, Type: str, EventTypeId: int, events2: set["Event"] = None):
        self.Type = Type
        self.EventTypeId = EventTypeId
        self.events2 = events2 if events2 is not None else set()
        
        pass
    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def EventTypeId(self):
        return self.__EventTypeId
    @EventTypeId.setter
    def EventTypeId(self, EventTypeId: int):
        self.__EventTypeId = EventTypeId

    @property
    def events2(self):
        return self.__events2
    @events2.setter
    def events2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventType__events2", None)
        self.__events2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "event_type3"):
                    opp_val = getattr(item, "event_type3", None)
                    
                    if opp_val == self:
                        setattr(item, "event_type3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "event_type3"):
                    opp_val = getattr(item, "event_type3", None)
                    
                    setattr(item, "event_type3", self)
                    



class User:

    def __init__(self, UserId: int, Email: str, Login: str, Password: str, PhoneNumber: str, DateOfBirth: str, registrations0: set["Registration"] = None, events6: "Event" = None):
        self.UserId = UserId
        self.Email = Email
        self.Login = Login
        self.Password = Password
        self.PhoneNumber = PhoneNumber
        self.DateOfBirth = DateOfBirth
        self.registrations0 = registrations0 if registrations0 is not None else set()
        self.events6 = events6
        
        pass
    @property
    def Login(self):
        return self.__Login
    @Login.setter
    def Login(self, Login: str):
        self.__Login = Login

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def UserId(self):
        return self.__UserId
    @UserId.setter
    def UserId(self, UserId: int):
        self.__UserId = UserId

    @property
    def DateOfBirth(self):
        return self.__DateOfBirth
    @DateOfBirth.setter
    def DateOfBirth(self, DateOfBirth: str):
        self.__DateOfBirth = DateOfBirth

    @property
    def PhoneNumber(self):
        return self.__PhoneNumber
    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber: str):
        self.__PhoneNumber = PhoneNumber

    @property
    def events6(self):
        return self.__events6
    @events6.setter
    def events6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__events6", None)
        self.__events6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user7"):
                opp_val = getattr(old_value, "user7", None)
                if opp_val == self:
                    setattr(old_value, "user7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user7"):
                opp_val = getattr(value, "user7", None)
                setattr(value, "user7", self)

    @property
    def registrations0(self):
        return self.__registrations0
    @registrations0.setter
    def registrations0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__registrations0", None)
        self.__registrations0 = value if value is not None else set()
        
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
                    



class Event:

    def __init__(self, EventId: int, Address: str, CurrentNumberOfPlayers: int, MaxNumberOfPlayers: int, DateTime: str, Description: str, attribute: str, event_type3: "EventType" = None, registrations4: set["Registration"] = None, user7: "User" = None):
        self.EventId = EventId
        self.Address = Address
        self.CurrentNumberOfPlayers = CurrentNumberOfPlayers
        self.MaxNumberOfPlayers = MaxNumberOfPlayers
        self.DateTime = DateTime
        self.Description = Description
        self.attribute = attribute
        self.event_type3 = event_type3
        self.registrations4 = registrations4 if registrations4 is not None else set()
        self.user7 = user7
        
        pass
    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def CurrentNumberOfPlayers(self):
        return self.__CurrentNumberOfPlayers
    @CurrentNumberOfPlayers.setter
    def CurrentNumberOfPlayers(self, CurrentNumberOfPlayers: int):
        self.__CurrentNumberOfPlayers = CurrentNumberOfPlayers

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def MaxNumberOfPlayers(self):
        return self.__MaxNumberOfPlayers
    @MaxNumberOfPlayers.setter
    def MaxNumberOfPlayers(self, MaxNumberOfPlayers: int):
        self.__MaxNumberOfPlayers = MaxNumberOfPlayers

    @property
    def EventId(self):
        return self.__EventId
    @EventId.setter
    def EventId(self, EventId: int):
        self.__EventId = EventId

    @property
    def DateTime(self):
        return self.__DateTime
    @DateTime.setter
    def DateTime(self, DateTime: str):
        self.__DateTime = DateTime

    @property
    def event_type3(self):
        return self.__event_type3
    @event_type3.setter
    def event_type3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Event__event_type3", None)
        self.__event_type3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "events2"):
                opp_val = getattr(old_value, "events2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "events2"):
                opp_val = getattr(value, "events2", None)
                if opp_val is None:
                    setattr(value, "events2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def user7(self):
        return self.__user7
    @user7.setter
    def user7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Event__user7", None)
        self.__user7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "events6"):
                opp_val = getattr(old_value, "events6", None)
                if opp_val == self:
                    setattr(old_value, "events6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "events6"):
                opp_val = getattr(value, "events6", None)
                setattr(value, "events6", self)

    @property
    def registrations4(self):
        return self.__registrations4
    @registrations4.setter
    def registrations4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Event__registrations4", None)
        self.__registrations4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "event5"):
                    opp_val = getattr(item, "event5", None)
                    
                    if opp_val == self:
                        setattr(item, "event5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "event5"):
                    opp_val = getattr(item, "event5", None)
                    
                    setattr(item, "event5", self)
                    

