from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class admin_Actor:

    pass


class Supervisor_Actor:

    pass


class Employee_Actor:

    pass





class modify_list_of_students_external:

    pass


class send_attendance_sms_external:

    pass


class logout_external:

    pass


class login_external:

    pass


class view_cumiliative_attendance_external:

    pass


class answer_attendance_call_external:

    pass


class post_attendance_external:

    pass


class generate_attendance_report_external:

    pass


class take_attendance_call_external:

    pass


class ADMIN:

    def __init__(self, id: str, password: str, fACULTY31: set["FACULTY"] = None, sTUDENT33: set["STUDENT"] = None, pARENT35: set["PARENT"] = None):
        self.id = id
        self.password = password
        self.fACULTY31 = fACULTY31 if fACULTY31 is not None else set()
        self.sTUDENT33 = sTUDENT33 if sTUDENT33 is not None else set()
        self.pARENT35 = pARENT35 if pARENT35 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def fACULTY31(self):
        return self.__fACULTY31
    @fACULTY31.setter
    def fACULTY31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__fACULTY31", None)
        self.__fACULTY31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDMIN30"):
                    opp_val = getattr(item, "aDMIN30", None)
                    
                    if opp_val == self:
                        setattr(item, "aDMIN30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDMIN30"):
                    opp_val = getattr(item, "aDMIN30", None)
                    
                    setattr(item, "aDMIN30", self)
                    

    @property
    def sTUDENT33(self):
        return self.__sTUDENT33
    @sTUDENT33.setter
    def sTUDENT33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__sTUDENT33", None)
        self.__sTUDENT33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDMIN32"):
                    opp_val = getattr(item, "aDMIN32", None)
                    
                    if opp_val == self:
                        setattr(item, "aDMIN32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDMIN32"):
                    opp_val = getattr(item, "aDMIN32", None)
                    
                    setattr(item, "aDMIN32", self)
                    

    @property
    def pARENT35(self):
        return self.__pARENT35
    @pARENT35.setter
    def pARENT35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__pARENT35", None)
        self.__pARENT35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDMIN34"):
                    opp_val = getattr(item, "aDMIN34", None)
                    
                    if opp_val == self:
                        setattr(item, "aDMIN34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDMIN34"):
                    opp_val = getattr(item, "aDMIN34", None)
                    
                    setattr(item, "aDMIN34", self)
                    



class PARENT:

    def __init__(self, id: str, password: str, phoneNumber: int, aDMIN34: "ADMIN" = None):
        self.id = id
        self.password = password
        self.phoneNumber = phoneNumber
        self.aDMIN34 = aDMIN34
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: int):
        self.__phoneNumber = phoneNumber

    @property
    def aDMIN34(self):
        return self.__aDMIN34
    @aDMIN34.setter
    def aDMIN34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PARENT__aDMIN34", None)
        self.__aDMIN34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pARENT35"):
                opp_val = getattr(old_value, "pARENT35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pARENT35"):
                opp_val = getattr(value, "pARENT35", None)
                if opp_val is None:
                    setattr(value, "pARENT35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class STUDENT:

    def __init__(self, id: str, password: str, fACULTY29: set["FACULTY"] = None, aDMIN32: "ADMIN" = None):
        self.id = id
        self.password = password
        self.fACULTY29 = fACULTY29 if fACULTY29 is not None else set()
        self.aDMIN32 = aDMIN32
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def aDMIN32(self):
        return self.__aDMIN32
    @aDMIN32.setter
    def aDMIN32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__aDMIN32", None)
        self.__aDMIN32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sTUDENT33"):
                opp_val = getattr(old_value, "sTUDENT33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sTUDENT33"):
                opp_val = getattr(value, "sTUDENT33", None)
                if opp_val is None:
                    setattr(value, "sTUDENT33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fACULTY29(self):
        return self.__fACULTY29
    @fACULTY29.setter
    def fACULTY29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__fACULTY29", None)
        self.__fACULTY29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sTUDENT28"):
                    opp_val = getattr(item, "sTUDENT28", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sTUDENT28"):
                    opp_val = getattr(item, "sTUDENT28", None)
                    
                    if opp_val is None:
                        setattr(item, "sTUDENT28", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class FACULTY:

    def __init__(self, id: str, password: str, sTUDENT28: set["STUDENT"] = None, aDMIN30: "ADMIN" = None):
        self.id = id
        self.password = password
        self.sTUDENT28 = sTUDENT28 if sTUDENT28 is not None else set()
        self.aDMIN30 = aDMIN30
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def aDMIN30(self):
        return self.__aDMIN30
    @aDMIN30.setter
    def aDMIN30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FACULTY__aDMIN30", None)
        self.__aDMIN30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fACULTY31"):
                opp_val = getattr(old_value, "fACULTY31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fACULTY31"):
                opp_val = getattr(value, "fACULTY31", None)
                if opp_val is None:
                    setattr(value, "fACULTY31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sTUDENT28(self):
        return self.__sTUDENT28
    @sTUDENT28.setter
    def sTUDENT28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FACULTY__sTUDENT28", None)
        self.__sTUDENT28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fACULTY29"):
                    opp_val = getattr(item, "fACULTY29", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fACULTY29"):
                    opp_val = getattr(item, "fACULTY29", None)
                    
                    if opp_val is None:
                        setattr(item, "fACULTY29", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class _Component:

    pass
