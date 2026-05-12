from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Class4:

    pass


class Class3:

    pass


class Class2:

    pass


class c1:

    pass


class c:

    pass


class Class:

    pass


class Teacher:

    def __init__(self, Name: str, room0: "Room" = None):
        self.Name = Name
        self.room0 = room0
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def room0(self):
        return self.__room0
    @room0.setter
    def room0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Teacher__room0", None)
        self.__room0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teacher1"):
                opp_val = getattr(old_value, "teacher1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teacher1"):
                opp_val = getattr(value, "teacher1", None)
                if opp_val is None:
                    setattr(value, "teacher1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Room:

    def __init__(self, Name: str, teacher1: set["Teacher"] = None, class42: "Class4" = None):
        self.Name = Name
        self.teacher1 = teacher1 if teacher1 is not None else set()
        self.class42 = class42
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def class42(self):
        return self.__class42
    @class42.setter
    def class42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__class42", None)
        self.__class42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room3"):
                opp_val = getattr(old_value, "room3", None)
                if opp_val == self:
                    setattr(old_value, "room3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room3"):
                opp_val = getattr(value, "room3", None)
                setattr(value, "room3", self)

    @property
    def teacher1(self):
        return self.__teacher1
    @teacher1.setter
    def teacher1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__teacher1", None)
        self.__teacher1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room0"):
                    opp_val = getattr(item, "room0", None)
                    
                    if opp_val == self:
                        setattr(item, "room0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room0"):
                    opp_val = getattr(item, "room0", None)
                    
                    setattr(item, "room0", self)
                    

