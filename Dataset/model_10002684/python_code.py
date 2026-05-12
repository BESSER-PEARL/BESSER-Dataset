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


class HOD:

    def __init__(self, id: str, password: str, FACULTY_ADMIN_143: set["COUNSELLOR"] = None, sTUDENT45: set["STUDENT"] = None):
        self.id = id
        self.password = password
        self.FACULTY_ADMIN_143 = FACULTY_ADMIN_143 if FACULTY_ADMIN_143 is not None else set()
        self.sTUDENT45 = sTUDENT45 if sTUDENT45 is not None else set()
        
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
        old_value = getattr(self, f"_HOD__sTUDENT45", None)
        self.__sTUDENT45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hod44"):
                    opp_val = getattr(item, "hod44", None)
                    
                    if opp_val == self:
                        setattr(item, "hod44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hod44"):
                    opp_val = getattr(item, "hod44", None)
                    
                    setattr(item, "hod44", self)
                    

    @property
    def FACULTY_ADMIN_143(self):
        return self.__FACULTY_ADMIN_143
    @FACULTY_ADMIN_143.setter
    def FACULTY_ADMIN_143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HOD__FACULTY_ADMIN_143", None)
        self.__FACULTY_ADMIN_143 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hod42"):
                    opp_val = getattr(item, "hod42", None)
                    
                    if opp_val == self:
                        setattr(item, "hod42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hod42"):
                    opp_val = getattr(item, "hod42", None)
                    
                    setattr(item, "hod42", self)
                    



class STUDENT:

    def __init__(self, id: str, password: str, counsellor41: set["COUNSELLOR"] = None, hod44: "HOD" = None):
        self.id = id
        self.password = password
        self.counsellor41 = counsellor41 if counsellor41 is not None else set()
        self.hod44 = hod44
        
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
    def counsellor41(self):
        return self.__counsellor41
    @counsellor41.setter
    def counsellor41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__counsellor41", None)
        self.__counsellor41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "student40"):
                    opp_val = getattr(item, "student40", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "student40"):
                    opp_val = getattr(item, "student40", None)
                    
                    if opp_val is None:
                        setattr(item, "student40", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def hod44(self):
        return self.__hod44
    @hod44.setter
    def hod44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__hod44", None)
        self.__hod44 = value
        
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



class COUNSELLOR:

    def __init__(self, id: str, password: str, student40: set["STUDENT"] = None, hod42: "HOD" = None):
        self.id = id
        self.password = password
        self.student40 = student40 if student40 is not None else set()
        self.hod42 = hod42
        
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
    def student40(self):
        return self.__student40
    @student40.setter
    def student40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_COUNSELLOR__student40", None)
        self.__student40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "counsellor41"):
                    opp_val = getattr(item, "counsellor41", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "counsellor41"):
                    opp_val = getattr(item, "counsellor41", None)
                    
                    if opp_val is None:
                        setattr(item, "counsellor41", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def hod42(self):
        return self.__hod42
    @hod42.setter
    def hod42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_COUNSELLOR__hod42", None)
        self.__hod42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FACULTY_ADMIN_143"):
                opp_val = getattr(old_value, "FACULTY_ADMIN_143", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FACULTY_ADMIN_143"):
                opp_val = getattr(value, "FACULTY_ADMIN_143", None)
                if opp_val is None:
                    setattr(value, "FACULTY_ADMIN_143", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class _Component:

    pass
