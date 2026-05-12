from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class admin_Actor:

    pass


class parent_Actor:

    pass


class faculty_Actor:

    pass


class student_Actor:

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


class take_attendance_call_external:

    pass


class modify_list_of_students_external:

    pass


class recieve_attendance_sms_external:

    pass


class send_attendance_sms_external:

    pass


class ADMIN:

    def __init__(self, id: str, password: str, fACULTY41: set["FACULTY"] = None, sTUDENT43: set["STUDENT"] = None, pARENT45: set["PARENT"] = None):
        self.id = id
        self.password = password
        self.fACULTY41 = fACULTY41 if fACULTY41 is not None else set()
        self.sTUDENT43 = sTUDENT43 if sTUDENT43 is not None else set()
        self.pARENT45 = pARENT45 if pARENT45 is not None else set()
        
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
    def pARENT45(self):
        return self.__pARENT45
    @pARENT45.setter
    def pARENT45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__pARENT45", None)
        self.__pARENT45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDMIN44"):
                    opp_val = getattr(item, "aDMIN44", None)
                    
                    if opp_val == self:
                        setattr(item, "aDMIN44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDMIN44"):
                    opp_val = getattr(item, "aDMIN44", None)
                    
                    setattr(item, "aDMIN44", self)
                    

    @property
    def sTUDENT43(self):
        return self.__sTUDENT43
    @sTUDENT43.setter
    def sTUDENT43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__sTUDENT43", None)
        self.__sTUDENT43 = value if value is not None else set()
        
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
    def fACULTY41(self):
        return self.__fACULTY41
    @fACULTY41.setter
    def fACULTY41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__fACULTY41", None)
        self.__fACULTY41 = value if value is not None else set()
        
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

    def __init__(self, id: str, password: str, phoneNumber: int, aDMIN44: "ADMIN" = None):
        self.id = id
        self.password = password
        self.phoneNumber = phoneNumber
        self.aDMIN44 = aDMIN44
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

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
    def aDMIN44(self):
        return self.__aDMIN44
    @aDMIN44.setter
    def aDMIN44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PARENT__aDMIN44", None)
        self.__aDMIN44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pARENT45"):
                opp_val = getattr(old_value, "pARENT45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pARENT45"):
                opp_val = getattr(value, "pARENT45", None)
                if opp_val is None:
                    setattr(value, "pARENT45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class STUDENT:

    def __init__(self, id: str, password: str, fACULTY39: set["FACULTY"] = None, aDMIN42: "ADMIN" = None):
        self.id = id
        self.password = password
        self.fACULTY39 = fACULTY39 if fACULTY39 is not None else set()
        self.aDMIN42 = aDMIN42
        
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
    def fACULTY39(self):
        return self.__fACULTY39
    @fACULTY39.setter
    def fACULTY39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__fACULTY39", None)
        self.__fACULTY39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sTUDENT38"):
                    opp_val = getattr(item, "sTUDENT38", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sTUDENT38"):
                    opp_val = getattr(item, "sTUDENT38", None)
                    
                    if opp_val is None:
                        setattr(item, "sTUDENT38", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def aDMIN42(self):
        return self.__aDMIN42
    @aDMIN42.setter
    def aDMIN42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__aDMIN42", None)
        self.__aDMIN42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sTUDENT43"):
                opp_val = getattr(old_value, "sTUDENT43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sTUDENT43"):
                opp_val = getattr(value, "sTUDENT43", None)
                if opp_val is None:
                    setattr(value, "sTUDENT43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class FACULTY:

    def __init__(self, id: str, password: str, sTUDENT38: set["STUDENT"] = None, aDMIN40: "ADMIN" = None):
        self.id = id
        self.password = password
        self.sTUDENT38 = sTUDENT38 if sTUDENT38 is not None else set()
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
    def sTUDENT38(self):
        return self.__sTUDENT38
    @sTUDENT38.setter
    def sTUDENT38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FACULTY__sTUDENT38", None)
        self.__sTUDENT38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fACULTY39"):
                    opp_val = getattr(item, "fACULTY39", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fACULTY39"):
                    opp_val = getattr(item, "fACULTY39", None)
                    
                    if opp_val is None:
                        setattr(item, "fACULTY39", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def aDMIN40(self):
        return self.__aDMIN40
    @aDMIN40.setter
    def aDMIN40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FACULTY__aDMIN40", None)
        self.__aDMIN40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fACULTY41"):
                opp_val = getattr(old_value, "fACULTY41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fACULTY41"):
                opp_val = getattr(value, "fACULTY41", None)
                if opp_val is None:
                    setattr(value, "fACULTY41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class _Component:

    pass
