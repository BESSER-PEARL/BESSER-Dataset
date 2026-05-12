from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class admin_technician_Actor:

    pass


class parent_Actor:

    pass


class Teachers_Actor:

    pass


class student_Actor:

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


class view_subject_wise_attendance_external:

    pass


class answer_attendance_call_external:

    pass


class post_attendance_external:

    pass


class generate_class_wise_attendance_report_external:

    pass


class call_students_for_attendance_external:

    pass


class ADMIN:

    def __init__(self, id: str, password: str, sTUDENT39: set["STUDENT"] = None, pARENT41: set["PARENT"] = None, fACULTY37: set["FACULTY"] = None):
        self.id = id
        self.password = password
        self.sTUDENT39 = sTUDENT39 if sTUDENT39 is not None else set()
        self.pARENT41 = pARENT41 if pARENT41 is not None else set()
        self.fACULTY37 = fACULTY37 if fACULTY37 is not None else set()
        
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
    def fACULTY37(self):
        return self.__fACULTY37
    @fACULTY37.setter
    def fACULTY37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__fACULTY37", None)
        self.__fACULTY37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDMIN36"):
                    opp_val = getattr(item, "aDMIN36", None)
                    
                    if opp_val == self:
                        setattr(item, "aDMIN36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDMIN36"):
                    opp_val = getattr(item, "aDMIN36", None)
                    
                    setattr(item, "aDMIN36", self)
                    

    @property
    def sTUDENT39(self):
        return self.__sTUDENT39
    @sTUDENT39.setter
    def sTUDENT39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__sTUDENT39", None)
        self.__sTUDENT39 = value if value is not None else set()
        
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
    def pARENT41(self):
        return self.__pARENT41
    @pARENT41.setter
    def pARENT41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__pARENT41", None)
        self.__pARENT41 = value if value is not None else set()
        
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

    def __init__(self, id: str, password: str, phoneNumber: int, aDMIN40: "ADMIN" = None):
        self.id = id
        self.password = password
        self.phoneNumber = phoneNumber
        self.aDMIN40 = aDMIN40
        
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
    def aDMIN40(self):
        return self.__aDMIN40
    @aDMIN40.setter
    def aDMIN40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PARENT__aDMIN40", None)
        self.__aDMIN40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pARENT41"):
                opp_val = getattr(old_value, "pARENT41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pARENT41"):
                opp_val = getattr(value, "pARENT41", None)
                if opp_val is None:
                    setattr(value, "pARENT41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class STUDENT:

    def __init__(self, id: str, password: str, aDMIN38: "ADMIN" = None, fACULTY35: set["FACULTY"] = None):
        self.id = id
        self.password = password
        self.aDMIN38 = aDMIN38
        self.fACULTY35 = fACULTY35 if fACULTY35 is not None else set()
        
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
    def fACULTY35(self):
        return self.__fACULTY35
    @fACULTY35.setter
    def fACULTY35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__fACULTY35", None)
        self.__fACULTY35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sTUDENT34"):
                    opp_val = getattr(item, "sTUDENT34", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sTUDENT34"):
                    opp_val = getattr(item, "sTUDENT34", None)
                    
                    if opp_val is None:
                        setattr(item, "sTUDENT34", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def aDMIN38(self):
        return self.__aDMIN38
    @aDMIN38.setter
    def aDMIN38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__aDMIN38", None)
        self.__aDMIN38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sTUDENT39"):
                opp_val = getattr(old_value, "sTUDENT39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sTUDENT39"):
                opp_val = getattr(value, "sTUDENT39", None)
                if opp_val is None:
                    setattr(value, "sTUDENT39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class FACULTY:

    def __init__(self, id: str, password: str, sTUDENT34: set["STUDENT"] = None, aDMIN36: "ADMIN" = None):
        self.id = id
        self.password = password
        self.sTUDENT34 = sTUDENT34 if sTUDENT34 is not None else set()
        self.aDMIN36 = aDMIN36
        
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
    def sTUDENT34(self):
        return self.__sTUDENT34
    @sTUDENT34.setter
    def sTUDENT34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FACULTY__sTUDENT34", None)
        self.__sTUDENT34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fACULTY35"):
                    opp_val = getattr(item, "fACULTY35", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fACULTY35"):
                    opp_val = getattr(item, "fACULTY35", None)
                    
                    if opp_val is None:
                        setattr(item, "fACULTY35", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def aDMIN36(self):
        return self.__aDMIN36
    @aDMIN36.setter
    def aDMIN36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FACULTY__aDMIN36", None)
        self.__aDMIN36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fACULTY37"):
                opp_val = getattr(old_value, "fACULTY37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fACULTY37"):
                opp_val = getattr(value, "fACULTY37", None)
                if opp_val is None:
                    setattr(value, "fACULTY37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Student_Attendance_at_INU_Component:

    pass
