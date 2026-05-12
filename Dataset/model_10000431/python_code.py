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





class view_subject_wise_attendance_external:

    pass


class answer_attendance_call_external:

    pass


class post_attendance_external:

    pass


class generate_class_wise_attendance_report_external:

    pass


class ADMIN:

    def __init__(self, id: str, password: str, fACULTY43: set["FACULTY"] = None, sTUDENT45: set["STUDENT"] = None, pARENT47: set["PARENT"] = None):
        self.id = id
        self.password = password
        self.fACULTY43 = fACULTY43 if fACULTY43 is not None else set()
        self.sTUDENT45 = sTUDENT45 if sTUDENT45 is not None else set()
        self.pARENT47 = pARENT47 if pARENT47 is not None else set()
        
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
    def sTUDENT45(self):
        return self.__sTUDENT45
    @sTUDENT45.setter
    def sTUDENT45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__sTUDENT45", None)
        self.__sTUDENT45 = value if value is not None else set()
        
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
    def pARENT47(self):
        return self.__pARENT47
    @pARENT47.setter
    def pARENT47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__pARENT47", None)
        self.__pARENT47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDMIN46"):
                    opp_val = getattr(item, "aDMIN46", None)
                    
                    if opp_val == self:
                        setattr(item, "aDMIN46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDMIN46"):
                    opp_val = getattr(item, "aDMIN46", None)
                    
                    setattr(item, "aDMIN46", self)
                    

    @property
    def fACULTY43(self):
        return self.__fACULTY43
    @fACULTY43.setter
    def fACULTY43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__fACULTY43", None)
        self.__fACULTY43 = value if value is not None else set()
        
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
                    



class PARENT:

    def __init__(self, id: str, password: str, phoneNumber: int, aDMIN46: "ADMIN" = None):
        self.id = id
        self.password = password
        self.phoneNumber = phoneNumber
        self.aDMIN46 = aDMIN46
        
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
    def aDMIN46(self):
        return self.__aDMIN46
    @aDMIN46.setter
    def aDMIN46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PARENT__aDMIN46", None)
        self.__aDMIN46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pARENT47"):
                opp_val = getattr(old_value, "pARENT47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pARENT47"):
                opp_val = getattr(value, "pARENT47", None)
                if opp_val is None:
                    setattr(value, "pARENT47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class STUDENT:

    def __init__(self, id: str, password: str, fACULTY41: set["FACULTY"] = None, aDMIN44: "ADMIN" = None):
        self.id = id
        self.password = password
        self.fACULTY41 = fACULTY41 if fACULTY41 is not None else set()
        self.aDMIN44 = aDMIN44
        
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
    def fACULTY41(self):
        return self.__fACULTY41
    @fACULTY41.setter
    def fACULTY41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__fACULTY41", None)
        self.__fACULTY41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sTUDENT40"):
                    opp_val = getattr(item, "sTUDENT40", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sTUDENT40"):
                    opp_val = getattr(item, "sTUDENT40", None)
                    
                    if opp_val is None:
                        setattr(item, "sTUDENT40", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def aDMIN44(self):
        return self.__aDMIN44
    @aDMIN44.setter
    def aDMIN44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__aDMIN44", None)
        self.__aDMIN44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sTUDENT45"):
                opp_val = getattr(old_value, "sTUDENT45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sTUDENT45"):
                opp_val = getattr(value, "sTUDENT45", None)
                if opp_val is None:
                    setattr(value, "sTUDENT45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class FACULTY:

    def __init__(self, id: str, password: str, sTUDENT40: set["STUDENT"] = None, aDMIN42: "ADMIN" = None):
        self.id = id
        self.password = password
        self.sTUDENT40 = sTUDENT40 if sTUDENT40 is not None else set()
        self.aDMIN42 = aDMIN42
        
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
    def aDMIN42(self):
        return self.__aDMIN42
    @aDMIN42.setter
    def aDMIN42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FACULTY__aDMIN42", None)
        self.__aDMIN42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fACULTY43"):
                opp_val = getattr(old_value, "fACULTY43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fACULTY43"):
                opp_val = getattr(value, "fACULTY43", None)
                if opp_val is None:
                    setattr(value, "fACULTY43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sTUDENT40(self):
        return self.__sTUDENT40
    @sTUDENT40.setter
    def sTUDENT40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FACULTY__sTUDENT40", None)
        self.__sTUDENT40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fACULTY41"):
                    opp_val = getattr(item, "fACULTY41", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fACULTY41"):
                    opp_val = getattr(item, "fACULTY41", None)
                    
                    if opp_val is None:
                        setattr(item, "fACULTY41", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class _Component:

    pass


class take_attendance_call_external:

    pass


class modify_list_of_students_external:

    pass


class recieve_attendance_sms_external:

    pass


class send_attendance_sms_external:

    pass


class logout_external:

    pass


class login_external:

    pass


class view_cumiliative_attendance_external:

    pass
