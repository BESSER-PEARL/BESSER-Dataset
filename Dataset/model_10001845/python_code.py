from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class exam:

    pass


class subject:

    def __init__(self, id: int, name: str, admin5: "admin" = None, class17: "claas1" = None):
        self.id = id
        self.name = name
        self.admin5 = admin5
        self.class17 = class17
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def admin5(self):
        return self.__admin5
    @admin5.setter
    def admin5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_subject__admin5", None)
        self.__admin5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subject4"):
                opp_val = getattr(old_value, "subject4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subject4"):
                opp_val = getattr(value, "subject4", None)
                if opp_val is None:
                    setattr(value, "subject4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def class17(self):
        return self.__class17
    @class17.setter
    def class17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_subject__class17", None)
        self.__class17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subject6"):
                opp_val = getattr(old_value, "subject6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subject6"):
                opp_val = getattr(value, "subject6", None)
                if opp_val is None:
                    setattr(value, "subject6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class claas1:

    def __init__(self, id: int, name: str, subject6: set["subject"] = None, student8: set["student"] = None, teachers1: "teachers" = None):
        self.id = id
        self.name = name
        self.subject6 = subject6 if subject6 is not None else set()
        self.student8 = student8 if student8 is not None else set()
        self.teachers1 = teachers1
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def subject6(self):
        return self.__subject6
    @subject6.setter
    def subject6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_claas1__subject6", None)
        self.__subject6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "class17"):
                    opp_val = getattr(item, "class17", None)
                    
                    if opp_val == self:
                        setattr(item, "class17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "class17"):
                    opp_val = getattr(item, "class17", None)
                    
                    setattr(item, "class17", self)
                    

    @property
    def student8(self):
        return self.__student8
    @student8.setter
    def student8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_claas1__student8", None)
        self.__student8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "class19"):
                    opp_val = getattr(item, "class19", None)
                    
                    if opp_val == self:
                        setattr(item, "class19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "class19"):
                    opp_val = getattr(item, "class19", None)
                    
                    setattr(item, "class19", self)
                    

    @property
    def teachers1(self):
        return self.__teachers1
    @teachers1.setter
    def teachers1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_claas1__teachers1", None)
        self.__teachers1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class10"):
                opp_val = getattr(old_value, "class10", None)
                if opp_val == self:
                    setattr(old_value, "class10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class10"):
                opp_val = getattr(value, "class10", None)
                setattr(value, "class10", self)



class student:

    pass


class teachers:

    pass


class admin:

    pass


class user:

    def __init__(self, user_name: str, pas: str, sex: str):
        self.user_name = user_name
        self.pas = pas
        self.sex = sex
        
        pass
    @property
    def user_name(self):
        return self.__user_name
    @user_name.setter
    def user_name(self, user_name: str):
        self.__user_name = user_name

    @property
    def pas(self):
        return self.__pas
    @pas.setter
    def pas(self, pas: str):
        self.__pas = pas

    @property
    def sex(self):
        return self.__sex
    @sex.setter
    def sex(self, sex: str):
        self.__sex = sex

