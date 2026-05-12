from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Logout_UseCase:

    pass


class View_Questions_And_Post_Answers_UseCase:

    pass


class Post_Questions_UseCase:

    pass


class View_The_Uploaded_Materials_UseCase:

    pass


class Manage_Student___Faculty_List_UseCase:

    pass


class View___Modify_the_Uploaded_Materials_UseCase:

    pass


class Upload_Materials_UseCase:

    pass


class Login_UseCase:

    pass


class SignUp_UseCase:

    pass


class Admin_Actor:

    pass


class Faculty__Actor:

    pass


class Student_Actor:

    pass





class Admin:

    def __init__(self, name: str, mail_ID: str, faculty33: set["Faculty"] = None, student31: set["Student"] = None):
        self.name = name
        self.mail_ID = mail_ID
        self.faculty33 = faculty33 if faculty33 is not None else set()
        self.student31 = student31 if student31 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mail_ID(self):
        return self.__mail_ID
    @mail_ID.setter
    def mail_ID(self, mail_ID: str):
        self.__mail_ID = mail_ID

    @property
    def faculty33(self):
        return self.__faculty33
    @faculty33.setter
    def faculty33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__faculty33", None)
        self.__faculty33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "admin32"):
                    opp_val = getattr(item, "admin32", None)
                    
                    if opp_val == self:
                        setattr(item, "admin32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "admin32"):
                    opp_val = getattr(item, "admin32", None)
                    
                    setattr(item, "admin32", self)
                    

    @property
    def student31(self):
        return self.__student31
    @student31.setter
    def student31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__student31", None)
        self.__student31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "admin30"):
                    opp_val = getattr(item, "admin30", None)
                    
                    if opp_val == self:
                        setattr(item, "admin30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "admin30"):
                    opp_val = getattr(item, "admin30", None)
                    
                    setattr(item, "admin30", self)
                    



class Faculty:

    def __init__(self, name: str, mail_ID: str, emp_ID: str, admin32: "Admin" = None, student29: set["Student"] = None):
        self.name = name
        self.mail_ID = mail_ID
        self.emp_ID = emp_ID
        self.admin32 = admin32
        self.student29 = student29 if student29 is not None else set()
        
        pass
    @property
    def emp_ID(self):
        return self.__emp_ID
    @emp_ID.setter
    def emp_ID(self, emp_ID: str):
        self.__emp_ID = emp_ID

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mail_ID(self):
        return self.__mail_ID
    @mail_ID.setter
    def mail_ID(self, mail_ID: str):
        self.__mail_ID = mail_ID

    @property
    def student29(self):
        return self.__student29
    @student29.setter
    def student29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Faculty__student29", None)
        self.__student29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "faculty28"):
                    opp_val = getattr(item, "faculty28", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "faculty28"):
                    opp_val = getattr(item, "faculty28", None)
                    
                    if opp_val is None:
                        setattr(item, "faculty28", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def admin32(self):
        return self.__admin32
    @admin32.setter
    def admin32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Faculty__admin32", None)
        self.__admin32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "faculty33"):
                opp_val = getattr(old_value, "faculty33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "faculty33"):
                opp_val = getattr(value, "faculty33", None)
                if opp_val is None:
                    setattr(value, "faculty33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Student:

    def __init__(self, name: str, mail_ID: str, reg_Num: str, faculty28: set["Faculty"] = None, admin30: "Admin" = None):
        self.name = name
        self.mail_ID = mail_ID
        self.reg_Num = reg_Num
        self.faculty28 = faculty28 if faculty28 is not None else set()
        self.admin30 = admin30
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mail_ID(self):
        return self.__mail_ID
    @mail_ID.setter
    def mail_ID(self, mail_ID: str):
        self.__mail_ID = mail_ID

    @property
    def reg_Num(self):
        return self.__reg_Num
    @reg_Num.setter
    def reg_Num(self, reg_Num: str):
        self.__reg_Num = reg_Num

    @property
    def admin30(self):
        return self.__admin30
    @admin30.setter
    def admin30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__admin30", None)
        self.__admin30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student31"):
                opp_val = getattr(old_value, "student31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student31"):
                opp_val = getattr(value, "student31", None)
                if opp_val is None:
                    setattr(value, "student31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def faculty28(self):
        return self.__faculty28
    @faculty28.setter
    def faculty28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__faculty28", None)
        self.__faculty28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "student29"):
                    opp_val = getattr(item, "student29", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "student29"):
                    opp_val = getattr(item, "student29", None)
                    
                    if opp_val is None:
                        setattr(item, "student29", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

