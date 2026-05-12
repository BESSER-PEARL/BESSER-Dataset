from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class admin_Actor:

    pass


class parent_Actor:

    pass


class Teacher_Actor:

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


class answer_attendance_call_external:

    pass


class post_attendance_external:

    pass


class generate_class_wise_attendance_report_external:

    pass


class take_attendance_call_external:

    pass


class ADMIN:

    def __init__(self, id: str, password: str, fACULTY39: set["FACULTY"] = None, sTUDENT41: set["STUDENT"] = None, pARENT43: set["PARENT"] = None):
        self.id = id
        self.password = password
        self.fACULTY39 = fACULTY39 if fACULTY39 is not None else set()
        self.sTUDENT41 = sTUDENT41 if sTUDENT41 is not None else set()
        self.pARENT43 = pARENT43 if pARENT43 is not None else set()
        
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
    def pARENT43(self):
        return self.__pARENT43
    @pARENT43.setter
    def pARENT43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__pARENT43", None)
        self.__pARENT43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDMIN42"):
                    opp_val = getattr(item, "aDMIN42", None)
                    
                    if opp_val == self:
                        setattr(item, "aDMIN42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDMIN42"):
                    opp_val = getattr(item, "aDMIN42", None)
                    
                    setattr(item, "aDMIN42", self)
                    

    @property
    def fACULTY39(self):
        return self.__fACULTY39
    @fACULTY39.setter
    def fACULTY39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__fACULTY39", None)
        self.__fACULTY39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDMIN38"):
                    opp_val = getattr(item, "aDMIN38", None)
                    
                    if opp_val == self:
                        setattr(item, "aDMIN38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDMIN38"):
                    opp_val = getattr(item, "aDMIN38", None)
                    
                    setattr(item, "aDMIN38", self)
                    

    @property
    def sTUDENT41(self):
        return self.__sTUDENT41
    @sTUDENT41.setter
    def sTUDENT41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__sTUDENT41", None)
        self.__sTUDENT41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDMIN40"):
                    opp_val = getattr(item, "aDMIN40", None)
                    
                    if opp_val == self:
                        setattr(item, "aDMIN40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDMIN40"):
                    opp_val = getattr(item, "aDMIN40", None)
                    
                    setattr(item, "aDMIN40", self)
                    



class PARENT:

    def __init__(self, id: str, password: str, phoneNumber: int, aDMIN42: "ADMIN" = None):
        self.id = id
        self.password = password
        self.phoneNumber = phoneNumber
        self.aDMIN42 = aDMIN42
        
        pass
    @property
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: int):
        self.__phoneNumber = phoneNumber

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
    def aDMIN42(self):
        return self.__aDMIN42
    @aDMIN42.setter
    def aDMIN42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PARENT__aDMIN42", None)
        self.__aDMIN42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pARENT43"):
                opp_val = getattr(old_value, "pARENT43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pARENT43"):
                opp_val = getattr(value, "pARENT43", None)
                if opp_val is None:
                    setattr(value, "pARENT43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class STUDENT:

    def __init__(self, id: str, password: str, fACULTY37: set["FACULTY"] = None, aDMIN40: "ADMIN" = None):
        self.id = id
        self.password = password
        self.fACULTY37 = fACULTY37 if fACULTY37 is not None else set()
        self.aDMIN40 = aDMIN40
        
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
    def aDMIN40(self):
        return self.__aDMIN40
    @aDMIN40.setter
    def aDMIN40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__aDMIN40", None)
        self.__aDMIN40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sTUDENT41"):
                opp_val = getattr(old_value, "sTUDENT41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sTUDENT41"):
                opp_val = getattr(value, "sTUDENT41", None)
                if opp_val is None:
                    setattr(value, "sTUDENT41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fACULTY37(self):
        return self.__fACULTY37
    @fACULTY37.setter
    def fACULTY37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__fACULTY37", None)
        self.__fACULTY37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sTUDENT36"):
                    opp_val = getattr(item, "sTUDENT36", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sTUDENT36"):
                    opp_val = getattr(item, "sTUDENT36", None)
                    
                    if opp_val is None:
                        setattr(item, "sTUDENT36", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class FACULTY:

    def __init__(self, id: str, password: str, sTUDENT36: set["STUDENT"] = None, aDMIN38: "ADMIN" = None):
        self.id = id
        self.password = password
        self.sTUDENT36 = sTUDENT36 if sTUDENT36 is not None else set()
        self.aDMIN38 = aDMIN38
        
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
    def sTUDENT36(self):
        return self.__sTUDENT36
    @sTUDENT36.setter
    def sTUDENT36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FACULTY__sTUDENT36", None)
        self.__sTUDENT36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fACULTY37"):
                    opp_val = getattr(item, "fACULTY37", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fACULTY37"):
                    opp_val = getattr(item, "fACULTY37", None)
                    
                    if opp_val is None:
                        setattr(item, "fACULTY37", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def aDMIN38(self):
        return self.__aDMIN38
    @aDMIN38.setter
    def aDMIN38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FACULTY__aDMIN38", None)
        self.__aDMIN38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fACULTY39"):
                opp_val = getattr(old_value, "fACULTY39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fACULTY39"):
                opp_val = getattr(value, "fACULTY39", None)
                if opp_val is None:
                    setattr(value, "fACULTY39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class _Component:

    pass
