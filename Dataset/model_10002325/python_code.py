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


class logout_external:

    pass


class login_external:

    pass


class view_cumiliative_attendance_external:

    pass


class view_subject_wise_attendance_external:

    pass


class post_attendance_external:

    pass


class generate_class_wise_attendance_report_external:

    pass


class take_attendance_call_external:

    pass


class ADMIN:

    def __init__(self, id: str, password: str, fACULTY29: set["FACULTY"] = None, sTUDENT31: set["STUDENT"] = None, pARENT33: set["PARENT"] = None):
        self.id = id
        self.password = password
        self.fACULTY29 = fACULTY29 if fACULTY29 is not None else set()
        self.sTUDENT31 = sTUDENT31 if sTUDENT31 is not None else set()
        self.pARENT33 = pARENT33 if pARENT33 is not None else set()
        
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
    def sTUDENT31(self):
        return self.__sTUDENT31
    @sTUDENT31.setter
    def sTUDENT31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__sTUDENT31", None)
        self.__sTUDENT31 = value if value is not None else set()
        
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
    def fACULTY29(self):
        return self.__fACULTY29
    @fACULTY29.setter
    def fACULTY29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__fACULTY29", None)
        self.__fACULTY29 = value if value is not None else set()
        
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
    def pARENT33(self):
        return self.__pARENT33
    @pARENT33.setter
    def pARENT33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__pARENT33", None)
        self.__pARENT33 = value if value is not None else set()
        
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
                    



class PARENT:

    def __init__(self, id: str, password: str, phoneNumber: int, aDMIN32: "ADMIN" = None):
        self.id = id
        self.password = password
        self.phoneNumber = phoneNumber
        self.aDMIN32 = aDMIN32
        
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
    def aDMIN32(self):
        return self.__aDMIN32
    @aDMIN32.setter
    def aDMIN32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PARENT__aDMIN32", None)
        self.__aDMIN32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pARENT33"):
                opp_val = getattr(old_value, "pARENT33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pARENT33"):
                opp_val = getattr(value, "pARENT33", None)
                if opp_val is None:
                    setattr(value, "pARENT33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class STUDENT:

    def __init__(self, id: str, password: str, fACULTY27: set["FACULTY"] = None, aDMIN30: "ADMIN" = None):
        self.id = id
        self.password = password
        self.fACULTY27 = fACULTY27 if fACULTY27 is not None else set()
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
        old_value = getattr(self, f"_STUDENT__aDMIN30", None)
        self.__aDMIN30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sTUDENT31"):
                opp_val = getattr(old_value, "sTUDENT31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sTUDENT31"):
                opp_val = getattr(value, "sTUDENT31", None)
                if opp_val is None:
                    setattr(value, "sTUDENT31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fACULTY27(self):
        return self.__fACULTY27
    @fACULTY27.setter
    def fACULTY27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__fACULTY27", None)
        self.__fACULTY27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sTUDENT26"):
                    opp_val = getattr(item, "sTUDENT26", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sTUDENT26"):
                    opp_val = getattr(item, "sTUDENT26", None)
                    
                    if opp_val is None:
                        setattr(item, "sTUDENT26", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class FACULTY:

    def __init__(self, id: str, password: str, sTUDENT26: set["STUDENT"] = None, aDMIN28: "ADMIN" = None):
        self.id = id
        self.password = password
        self.sTUDENT26 = sTUDENT26 if sTUDENT26 is not None else set()
        self.aDMIN28 = aDMIN28
        
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
    def sTUDENT26(self):
        return self.__sTUDENT26
    @sTUDENT26.setter
    def sTUDENT26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FACULTY__sTUDENT26", None)
        self.__sTUDENT26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fACULTY27"):
                    opp_val = getattr(item, "fACULTY27", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fACULTY27"):
                    opp_val = getattr(item, "fACULTY27", None)
                    
                    if opp_val is None:
                        setattr(item, "fACULTY27", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def aDMIN28(self):
        return self.__aDMIN28
    @aDMIN28.setter
    def aDMIN28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FACULTY__aDMIN28", None)
        self.__aDMIN28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fACULTY29"):
                opp_val = getattr(old_value, "fACULTY29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fACULTY29"):
                opp_val = getattr(value, "fACULTY29", None)
                if opp_val is None:
                    setattr(value, "fACULTY29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class _Component:

    pass
