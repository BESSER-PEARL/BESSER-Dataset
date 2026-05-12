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





class recieve_attendance_sms_external:

    pass


class send_attendance_sms_external:

    pass


class logout_external:

    pass


class modify_list_of_students_external:

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


class STUDENT:

    def __init__(self, id: str, password: str, fACULTY41: set["FACULTY"] = None):
        self.id = id
        self.password = password
        self.fACULTY41 = fACULTY41 if fACULTY41 is not None else set()
        
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
                    



class FACULTY:

    def __init__(self, id: str, password: str, sTUDENT40: set["STUDENT"] = None):
        self.id = id
        self.password = password
        self.sTUDENT40 = sTUDENT40 if sTUDENT40 is not None else set()
        
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
