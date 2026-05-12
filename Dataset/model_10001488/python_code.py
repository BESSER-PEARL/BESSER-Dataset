from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class UseCase3_UseCase:

    pass





class Insurance:

    def __init__(self, email: str, password: str, user10: "user" = None):
        self.email = email
        self.password = password
        self.user10 = user10
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def user10(self):
        return self.__user10
    @user10.setter
    def user10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Insurance__user10", None)
        self.__user10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "insurance11"):
                opp_val = getattr(old_value, "insurance11", None)
                if opp_val == self:
                    setattr(old_value, "insurance11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "insurance11"):
                opp_val = getattr(value, "insurance11", None)
                setattr(value, "insurance11", self)



class Admin:

    def __init__(self, uname: str, password: str, Admin_Doctor_04: set["Doctor"] = None, Admin_Patient_06: set["Patient"] = None, Admin_user_08: "user" = None):
        self.uname = uname
        self.password = password
        self.Admin_Doctor_04 = Admin_Doctor_04 if Admin_Doctor_04 is not None else set()
        self.Admin_Patient_06 = Admin_Patient_06 if Admin_Patient_06 is not None else set()
        self.Admin_user_08 = Admin_user_08
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def uname(self):
        return self.__uname
    @uname.setter
    def uname(self, uname: str):
        self.__uname = uname

    @property
    def Admin_user_08(self):
        return self.__Admin_user_08
    @Admin_user_08.setter
    def Admin_user_08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__Admin_user_08", None)
        self.__Admin_user_08 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "send_mail9"):
                opp_val = getattr(old_value, "send_mail9", None)
                if opp_val == self:
                    setattr(old_value, "send_mail9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "send_mail9"):
                opp_val = getattr(value, "send_mail9", None)
                setattr(value, "send_mail9", self)

    @property
    def Admin_Patient_06(self):
        return self.__Admin_Patient_06
    @Admin_Patient_06.setter
    def Admin_Patient_06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__Admin_Patient_06", None)
        self.__Admin_Patient_06 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "accepts7"):
                    opp_val = getattr(item, "accepts7", None)
                    
                    if opp_val == self:
                        setattr(item, "accepts7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "accepts7"):
                    opp_val = getattr(item, "accepts7", None)
                    
                    setattr(item, "accepts7", self)
                    

    @property
    def Admin_Doctor_04(self):
        return self.__Admin_Doctor_04
    @Admin_Doctor_04.setter
    def Admin_Doctor_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__Admin_Doctor_04", None)
        self.__Admin_Doctor_04 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "accepts5"):
                    opp_val = getattr(item, "accepts5", None)
                    
                    if opp_val == self:
                        setattr(item, "accepts5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "accepts5"):
                    opp_val = getattr(item, "accepts5", None)
                    
                    setattr(item, "accepts5", self)
                    



class Patient:

    def __init__(self, email: str, password: str, checks3: "Doctor" = None, accepts7: "Admin" = None):
        self.email = email
        self.password = password
        self.checks3 = checks3
        self.accepts7 = accepts7
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def accepts7(self):
        return self.__accepts7
    @accepts7.setter
    def accepts7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__accepts7", None)
        self.__accepts7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Admin_Patient_06"):
                opp_val = getattr(old_value, "Admin_Patient_06", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Admin_Patient_06"):
                opp_val = getattr(value, "Admin_Patient_06", None)
                if opp_val is None:
                    setattr(value, "Admin_Patient_06", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def checks3(self):
        return self.__checks3
    @checks3.setter
    def checks3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__checks3", None)
        self.__checks3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "request_to2"):
                opp_val = getattr(old_value, "request_to2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "request_to2"):
                opp_val = getattr(value, "request_to2", None)
                if opp_val is None:
                    setattr(value, "request_to2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Doctor:

    def __init__(self, email: str, password: str, register1: "user" = None, request_to2: set["Patient"] = None, accepts5: "Admin" = None):
        self.email = email
        self.password = password
        self.register1 = register1
        self.request_to2 = request_to2 if request_to2 is not None else set()
        self.accepts5 = accepts5
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def request_to2(self):
        return self.__request_to2
    @request_to2.setter
    def request_to2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__request_to2", None)
        self.__request_to2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "checks3"):
                    opp_val = getattr(item, "checks3", None)
                    
                    if opp_val == self:
                        setattr(item, "checks3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "checks3"):
                    opp_val = getattr(item, "checks3", None)
                    
                    setattr(item, "checks3", self)
                    

    @property
    def accepts5(self):
        return self.__accepts5
    @accepts5.setter
    def accepts5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__accepts5", None)
        self.__accepts5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Admin_Doctor_04"):
                opp_val = getattr(old_value, "Admin_Doctor_04", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Admin_Doctor_04"):
                opp_val = getattr(value, "Admin_Doctor_04", None)
                if opp_val is None:
                    setattr(value, "Admin_Doctor_04", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def register1(self):
        return self.__register1
    @register1.setter
    def register1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__register1", None)
        self.__register1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user_Doctor_00"):
                opp_val = getattr(old_value, "user_Doctor_00", None)
                if opp_val == self:
                    setattr(old_value, "user_Doctor_00", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user_Doctor_00"):
                opp_val = getattr(value, "user_Doctor_00", None)
                setattr(value, "user_Doctor_00", self)



class user:

    def __init__(self, name: str, phone_number: int, address: str, email: str, password: str, user_Doctor_00: "Doctor" = None, send_mail9: "Admin" = None, insurance11: "Insurance" = None):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.password = password
        self.user_Doctor_00 = user_Doctor_00
        self.send_mail9 = send_mail9
        self.insurance11 = insurance11
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def phone_number(self):
        return self.__phone_number
    @phone_number.setter
    def phone_number(self, phone_number: int):
        self.__phone_number = phone_number

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def user_Doctor_00(self):
        return self.__user_Doctor_00
    @user_Doctor_00.setter
    def user_Doctor_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_user__user_Doctor_00", None)
        self.__user_Doctor_00 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "register1"):
                opp_val = getattr(old_value, "register1", None)
                if opp_val == self:
                    setattr(old_value, "register1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "register1"):
                opp_val = getattr(value, "register1", None)
                setattr(value, "register1", self)

    @property
    def insurance11(self):
        return self.__insurance11
    @insurance11.setter
    def insurance11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_user__insurance11", None)
        self.__insurance11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user10"):
                opp_val = getattr(old_value, "user10", None)
                if opp_val == self:
                    setattr(old_value, "user10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user10"):
                opp_val = getattr(value, "user10", None)
                setattr(value, "user10", self)

    @property
    def send_mail9(self):
        return self.__send_mail9
    @send_mail9.setter
    def send_mail9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_user__send_mail9", None)
        self.__send_mail9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Admin_user_08"):
                opp_val = getattr(old_value, "Admin_user_08", None)
                if opp_val == self:
                    setattr(old_value, "Admin_user_08", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Admin_user_08"):
                opp_val = getattr(value, "Admin_user_08", None)
                setattr(value, "Admin_user_08", self)

