from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class admin_Actor:

    pass


class faculty_Actor:

    pass


class student_Actor:

    pass





class modify_list_of_students_external:

    pass


class view_cumiliative_attendance_external:

    pass


class send_attendance_sms_external:

    pass


class logout_external:

    pass


class login_external:

    pass


class answer_attendance_call_external:

    pass


class post_attendance_external:

    pass


class generate_class_wise_attendance_report_external:

    pass


class take_attendance_call_external:

    pass


class ADMIN:

    def __init__(self, id: str, password: str, sTUDENT27: set["STUDENT"] = None, pARENT29: set["PARENT"] = None, fACULTY25: set["FACULTY"] = None):
        self.id = id
        self.password = password
        self.sTUDENT27 = sTUDENT27 if sTUDENT27 is not None else set()
        self.pARENT29 = pARENT29 if pARENT29 is not None else set()
        self.fACULTY25 = fACULTY25 if fACULTY25 is not None else set()
        
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
    def pARENT29(self):
        return self.__pARENT29
    @pARENT29.setter
    def pARENT29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__pARENT29", None)
        self.__pARENT29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDMIN28"):
                    opp_val = getattr(item, "aDMIN28", None)
                    
                    if opp_val == self:
                        setattr(item, "aDMIN28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDMIN28"):
                    opp_val = getattr(item, "aDMIN28", None)
                    
                    setattr(item, "aDMIN28", self)
                    

    @property
    def fACULTY25(self):
        return self.__fACULTY25
    @fACULTY25.setter
    def fACULTY25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__fACULTY25", None)
        self.__fACULTY25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDMIN24"):
                    opp_val = getattr(item, "aDMIN24", None)
                    
                    if opp_val == self:
                        setattr(item, "aDMIN24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDMIN24"):
                    opp_val = getattr(item, "aDMIN24", None)
                    
                    setattr(item, "aDMIN24", self)
                    

    @property
    def sTUDENT27(self):
        return self.__sTUDENT27
    @sTUDENT27.setter
    def sTUDENT27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__sTUDENT27", None)
        self.__sTUDENT27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDMIN26"):
                    opp_val = getattr(item, "aDMIN26", None)
                    
                    if opp_val == self:
                        setattr(item, "aDMIN26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDMIN26"):
                    opp_val = getattr(item, "aDMIN26", None)
                    
                    setattr(item, "aDMIN26", self)
                    



class PARENT:

    def __init__(self, id: str, password: str, phoneNumber: int, aDMIN28: "ADMIN" = None):
        self.id = id
        self.password = password
        self.phoneNumber = phoneNumber
        self.aDMIN28 = aDMIN28
        
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
    def aDMIN28(self):
        return self.__aDMIN28
    @aDMIN28.setter
    def aDMIN28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PARENT__aDMIN28", None)
        self.__aDMIN28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pARENT29"):
                opp_val = getattr(old_value, "pARENT29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pARENT29"):
                opp_val = getattr(value, "pARENT29", None)
                if opp_val is None:
                    setattr(value, "pARENT29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class STUDENT:

    def __init__(self, id: str, password: str, aDMIN26: "ADMIN" = None, fACULTY23: set["FACULTY"] = None):
        self.id = id
        self.password = password
        self.aDMIN26 = aDMIN26
        self.fACULTY23 = fACULTY23 if fACULTY23 is not None else set()
        
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
    def fACULTY23(self):
        return self.__fACULTY23
    @fACULTY23.setter
    def fACULTY23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__fACULTY23", None)
        self.__fACULTY23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sTUDENT22"):
                    opp_val = getattr(item, "sTUDENT22", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sTUDENT22"):
                    opp_val = getattr(item, "sTUDENT22", None)
                    
                    if opp_val is None:
                        setattr(item, "sTUDENT22", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def aDMIN26(self):
        return self.__aDMIN26
    @aDMIN26.setter
    def aDMIN26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__aDMIN26", None)
        self.__aDMIN26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sTUDENT27"):
                opp_val = getattr(old_value, "sTUDENT27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sTUDENT27"):
                opp_val = getattr(value, "sTUDENT27", None)
                if opp_val is None:
                    setattr(value, "sTUDENT27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class FACULTY:

    def __init__(self, id: str, password: str, sTUDENT22: set["STUDENT"] = None, aDMIN24: "ADMIN" = None):
        self.id = id
        self.password = password
        self.sTUDENT22 = sTUDENT22 if sTUDENT22 is not None else set()
        self.aDMIN24 = aDMIN24
        
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
    def aDMIN24(self):
        return self.__aDMIN24
    @aDMIN24.setter
    def aDMIN24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FACULTY__aDMIN24", None)
        self.__aDMIN24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fACULTY25"):
                opp_val = getattr(old_value, "fACULTY25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fACULTY25"):
                opp_val = getattr(value, "fACULTY25", None)
                if opp_val is None:
                    setattr(value, "fACULTY25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sTUDENT22(self):
        return self.__sTUDENT22
    @sTUDENT22.setter
    def sTUDENT22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FACULTY__sTUDENT22", None)
        self.__sTUDENT22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fACULTY23"):
                    opp_val = getattr(item, "fACULTY23", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fACULTY23"):
                    opp_val = getattr(item, "fACULTY23", None)
                    
                    if opp_val is None:
                        setattr(item, "fACULTY23", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class _Component:

    pass
