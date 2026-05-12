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


class take_attendance_call_external:

    pass


class ADMIN:

    def __init__(self, id: str, password: str, fACULTY33: set["FACULTY"] = None, sTUDENT35: set["STUDENT"] = None):
        self.id = id
        self.password = password
        self.fACULTY33 = fACULTY33 if fACULTY33 is not None else set()
        self.sTUDENT35 = sTUDENT35 if sTUDENT35 is not None else set()
        
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
    def sTUDENT35(self):
        return self.__sTUDENT35
    @sTUDENT35.setter
    def sTUDENT35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__sTUDENT35", None)
        self.__sTUDENT35 = value if value is not None else set()
        
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
                    

    @property
    def fACULTY33(self):
        return self.__fACULTY33
    @fACULTY33.setter
    def fACULTY33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__fACULTY33", None)
        self.__fACULTY33 = value if value is not None else set()
        
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
                    



class STUDENT:

    def __init__(self, id: str, fACULTY31: set["FACULTY"] = None, aDMIN34: "ADMIN" = None):
        self.id = id
        self.fACULTY31 = fACULTY31 if fACULTY31 is not None else set()
        self.aDMIN34 = aDMIN34
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def aDMIN34(self):
        return self.__aDMIN34
    @aDMIN34.setter
    def aDMIN34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__aDMIN34", None)
        self.__aDMIN34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sTUDENT35"):
                opp_val = getattr(old_value, "sTUDENT35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sTUDENT35"):
                opp_val = getattr(value, "sTUDENT35", None)
                if opp_val is None:
                    setattr(value, "sTUDENT35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fACULTY31(self):
        return self.__fACULTY31
    @fACULTY31.setter
    def fACULTY31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__fACULTY31", None)
        self.__fACULTY31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sTUDENT30"):
                    opp_val = getattr(item, "sTUDENT30", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sTUDENT30"):
                    opp_val = getattr(item, "sTUDENT30", None)
                    
                    if opp_val is None:
                        setattr(item, "sTUDENT30", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class FACULTY:

    def __init__(self, id: str, password: str, sTUDENT30: set["STUDENT"] = None, aDMIN32: "ADMIN" = None):
        self.id = id
        self.password = password
        self.sTUDENT30 = sTUDENT30 if sTUDENT30 is not None else set()
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
    def sTUDENT30(self):
        return self.__sTUDENT30
    @sTUDENT30.setter
    def sTUDENT30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FACULTY__sTUDENT30", None)
        self.__sTUDENT30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fACULTY31"):
                    opp_val = getattr(item, "fACULTY31", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fACULTY31"):
                    opp_val = getattr(item, "fACULTY31", None)
                    
                    if opp_val is None:
                        setattr(item, "fACULTY31", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def aDMIN32(self):
        return self.__aDMIN32
    @aDMIN32.setter
    def aDMIN32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FACULTY__aDMIN32", None)
        self.__aDMIN32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fACULTY33"):
                opp_val = getattr(old_value, "fACULTY33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fACULTY33"):
                opp_val = getattr(value, "fACULTY33", None)
                if opp_val is None:
                    setattr(value, "fACULTY33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class _Component:

    pass
