from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class location:

    def __init__(self, Latitude: int, Longitude: int, attendance16: "Attendance" = None, attendance7: "Attendance" = None):
        self.Latitude = Latitude
        self.Longitude = Longitude
        self.attendance16 = attendance16
        self.attendance7 = attendance7
        
        pass
    @property
    def Longitude(self):
        return self.__Longitude
    @Longitude.setter
    def Longitude(self, Longitude: int):
        self.__Longitude = Longitude

    @property
    def Latitude(self):
        return self.__Latitude
    @Latitude.setter
    def Latitude(self, Latitude: int):
        self.__Latitude = Latitude

    @property
    def attendance16(self):
        return self.__attendance16
    @attendance16.setter
    def attendance16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_location__attendance16", None)
        self.__attendance16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "location17"):
                opp_val = getattr(old_value, "location17", None)
                if opp_val == self:
                    setattr(old_value, "location17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "location17"):
                opp_val = getattr(value, "location17", None)
                setattr(value, "location17", self)

    @property
    def attendance7(self):
        return self.__attendance7
    @attendance7.setter
    def attendance7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_location__attendance7", None)
        self.__attendance7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "location6"):
                opp_val = getattr(old_value, "location6", None)
                if opp_val == self:
                    setattr(old_value, "location6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "location6"):
                opp_val = getattr(value, "location6", None)
                setattr(value, "location6", self)



class login:

    def __init__(self, login_id: int, loginUsername: str, loginpassword: str, loginStatus: str, employee19: "Employee" = None, Admin21: "Admin" = None):
        self.login_id = login_id
        self.loginUsername = loginUsername
        self.loginpassword = loginpassword
        self.loginStatus = loginStatus
        self.employee19 = employee19
        self.Admin21 = Admin21
        
        pass
    @property
    def loginStatus(self):
        return self.__loginStatus
    @loginStatus.setter
    def loginStatus(self, loginStatus: str):
        self.__loginStatus = loginStatus

    @property
    def login_id(self):
        return self.__login_id
    @login_id.setter
    def login_id(self, login_id: int):
        self.__login_id = login_id

    @property
    def loginpassword(self):
        return self.__loginpassword
    @loginpassword.setter
    def loginpassword(self, loginpassword: str):
        self.__loginpassword = loginpassword

    @property
    def loginUsername(self):
        return self.__loginUsername
    @loginUsername.setter
    def loginUsername(self, loginUsername: str):
        self.__loginUsername = loginUsername

    @property
    def employee19(self):
        return self.__employee19
    @employee19.setter
    def employee19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_login__employee19", None)
        self.__employee19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login218"):
                opp_val = getattr(old_value, "login218", None)
                if opp_val == self:
                    setattr(old_value, "login218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login218"):
                opp_val = getattr(value, "login218", None)
                setattr(value, "login218", self)

    @property
    def Admin21(self):
        return self.__Admin21
    @Admin21.setter
    def Admin21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_login__Admin21", None)
        self.__Admin21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login20"):
                opp_val = getattr(old_value, "login20", None)
                if opp_val == self:
                    setattr(old_value, "login20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login20"):
                opp_val = getattr(value, "login20", None)
                setattr(value, "login20", self)



class Attendance:

    def __init__(self, atten_id: int, atten_emp_id: int, atten_type: str, atten_time: int, atten_date: str, Admin13: "Admin" = None, employee15: "Employee" = None, location17: "location" = None, employee5: "Employee" = None, location6: "location" = None):
        self.atten_id = atten_id
        self.atten_emp_id = atten_emp_id
        self.atten_type = atten_type
        self.atten_time = atten_time
        self.atten_date = atten_date
        self.Admin13 = Admin13
        self.employee15 = employee15
        self.location17 = location17
        self.employee5 = employee5
        self.location6 = location6
        
        pass
    @property
    def atten_type(self):
        return self.__atten_type
    @atten_type.setter
    def atten_type(self, atten_type: str):
        self.__atten_type = atten_type

    @property
    def atten_date(self):
        return self.__atten_date
    @atten_date.setter
    def atten_date(self, atten_date: str):
        self.__atten_date = atten_date

    @property
    def atten_emp_id(self):
        return self.__atten_emp_id
    @atten_emp_id.setter
    def atten_emp_id(self, atten_emp_id: int):
        self.__atten_emp_id = atten_emp_id

    @property
    def atten_time(self):
        return self.__atten_time
    @atten_time.setter
    def atten_time(self, atten_time: int):
        self.__atten_time = atten_time

    @property
    def atten_id(self):
        return self.__atten_id
    @atten_id.setter
    def atten_id(self, atten_id: int):
        self.__atten_id = atten_id

    @property
    def location6(self):
        return self.__location6
    @location6.setter
    def location6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Attendance__location6", None)
        self.__location6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attendance7"):
                opp_val = getattr(old_value, "attendance7", None)
                if opp_val == self:
                    setattr(old_value, "attendance7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attendance7"):
                opp_val = getattr(value, "attendance7", None)
                setattr(value, "attendance7", self)

    @property
    def employee15(self):
        return self.__employee15
    @employee15.setter
    def employee15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Attendance__employee15", None)
        self.__employee15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attendance14"):
                opp_val = getattr(old_value, "attendance14", None)
                if opp_val == self:
                    setattr(old_value, "attendance14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attendance14"):
                opp_val = getattr(value, "attendance14", None)
                setattr(value, "attendance14", self)

    @property
    def employee5(self):
        return self.__employee5
    @employee5.setter
    def employee5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Attendance__employee5", None)
        self.__employee5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attendance4"):
                opp_val = getattr(old_value, "attendance4", None)
                if opp_val == self:
                    setattr(old_value, "attendance4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attendance4"):
                opp_val = getattr(value, "attendance4", None)
                setattr(value, "attendance4", self)

    @property
    def Admin13(self):
        return self.__Admin13
    @Admin13.setter
    def Admin13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Attendance__Admin13", None)
        self.__Admin13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attendance12"):
                opp_val = getattr(old_value, "attendance12", None)
                if opp_val == self:
                    setattr(old_value, "attendance12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attendance12"):
                opp_val = getattr(value, "attendance12", None)
                setattr(value, "attendance12", self)

    @property
    def location17(self):
        return self.__location17
    @location17.setter
    def location17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Attendance__location17", None)
        self.__location17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attendance16"):
                opp_val = getattr(old_value, "attendance16", None)
                if opp_val == self:
                    setattr(old_value, "attendance16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attendance16"):
                opp_val = getattr(value, "attendance16", None)
                setattr(value, "attendance16", self)



class Full_day:

    def __init__(self, start_date: int, end_date: int):
        self.start_date = start_date
        self.end_date = end_date
        
        pass
    @property
    def end_date(self):
        return self.__end_date
    @end_date.setter
    def end_date(self, end_date: int):
        self.__end_date = end_date

    @property
    def start_date(self):
        return self.__start_date
    @start_date.setter
    def start_date(self, start_date: int):
        self.__start_date = start_date



class Haff_day:

    def __init__(self, start_date: int):
        self.start_date = start_date
        
        pass
    @property
    def start_date(self):
        return self.__start_date
    @start_date.setter
    def start_date(self, start_date: int):
        self.__start_date = start_date



class Leave:

    def __init__(self, l_id: int, l_description: str, l_type: str, l_emp_id: int, Admin3: "Admin" = None, employee10: set["Employee"] = None):
        self.l_id = l_id
        self.l_description = l_description
        self.l_type = l_type
        self.l_emp_id = l_emp_id
        self.Admin3 = Admin3
        self.employee10 = employee10 if employee10 is not None else set()
        
        pass
    @property
    def l_id(self):
        return self.__l_id
    @l_id.setter
    def l_id(self, l_id: int):
        self.__l_id = l_id

    @property
    def l_type(self):
        return self.__l_type
    @l_type.setter
    def l_type(self, l_type: str):
        self.__l_type = l_type

    @property
    def l_emp_id(self):
        return self.__l_emp_id
    @l_emp_id.setter
    def l_emp_id(self, l_emp_id: int):
        self.__l_emp_id = l_emp_id

    @property
    def l_description(self):
        return self.__l_description
    @l_description.setter
    def l_description(self, l_description: str):
        self.__l_description = l_description

    @property
    def Admin3(self):
        return self.__Admin3
    @Admin3.setter
    def Admin3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Leave__Admin3", None)
        self.__Admin3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leave2"):
                opp_val = getattr(old_value, "leave2", None)
                if opp_val == self:
                    setattr(old_value, "leave2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leave2"):
                opp_val = getattr(value, "leave2", None)
                setattr(value, "leave2", self)

    @property
    def employee10(self):
        return self.__employee10
    @employee10.setter
    def employee10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Leave__employee10", None)
        self.__employee10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "leave11"):
                    opp_val = getattr(item, "leave11", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "leave11"):
                    opp_val = getattr(item, "leave11", None)
                    
                    if opp_val is None:
                        setattr(item, "leave11", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Employee:

    def __init__(self, e_id: int, name: str, phone_no: int, email_id: str, paasword: str, address: str, office_address: str, attendance14: "Attendance" = None, Admin0: "Admin" = None, login218: "login" = None, attendance4: "Attendance" = None, Admin9: "Admin" = None, leave11: set["Leave"] = None):
        self.e_id = e_id
        self.name = name
        self.phone_no = phone_no
        self.email_id = email_id
        self.paasword = paasword
        self.address = address
        self.office_address = office_address
        self.attendance14 = attendance14
        self.Admin0 = Admin0
        self.login218 = login218
        self.attendance4 = attendance4
        self.Admin9 = Admin9
        self.leave11 = leave11 if leave11 is not None else set()
        
        pass
    @property
    def office_address(self):
        return self.__office_address
    @office_address.setter
    def office_address(self, office_address: str):
        self.__office_address = office_address

    @property
    def paasword(self):
        return self.__paasword
    @paasword.setter
    def paasword(self, paasword: str):
        self.__paasword = paasword

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def e_id(self):
        return self.__e_id
    @e_id.setter
    def e_id(self, e_id: int):
        self.__e_id = e_id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def email_id(self):
        return self.__email_id
    @email_id.setter
    def email_id(self, email_id: str):
        self.__email_id = email_id

    @property
    def phone_no(self):
        return self.__phone_no
    @phone_no.setter
    def phone_no(self, phone_no: int):
        self.__phone_no = phone_no

    @property
    def Admin9(self):
        return self.__Admin9
    @Admin9.setter
    def Admin9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__Admin9", None)
        self.__Admin9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee8"):
                opp_val = getattr(old_value, "employee8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee8"):
                opp_val = getattr(value, "employee8", None)
                if opp_val is None:
                    setattr(value, "employee8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def attendance4(self):
        return self.__attendance4
    @attendance4.setter
    def attendance4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__attendance4", None)
        self.__attendance4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee5"):
                opp_val = getattr(old_value, "employee5", None)
                if opp_val == self:
                    setattr(old_value, "employee5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee5"):
                opp_val = getattr(value, "employee5", None)
                setattr(value, "employee5", self)

    @property
    def login218(self):
        return self.__login218
    @login218.setter
    def login218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__login218", None)
        self.__login218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee19"):
                opp_val = getattr(old_value, "employee19", None)
                if opp_val == self:
                    setattr(old_value, "employee19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee19"):
                opp_val = getattr(value, "employee19", None)
                setattr(value, "employee19", self)

    @property
    def Admin0(self):
        return self.__Admin0
    @Admin0.setter
    def Admin0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__Admin0", None)
        self.__Admin0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee1"):
                opp_val = getattr(old_value, "employee1", None)
                if opp_val == self:
                    setattr(old_value, "employee1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee1"):
                opp_val = getattr(value, "employee1", None)
                setattr(value, "employee1", self)

    @property
    def attendance14(self):
        return self.__attendance14
    @attendance14.setter
    def attendance14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__attendance14", None)
        self.__attendance14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee15"):
                opp_val = getattr(old_value, "employee15", None)
                if opp_val == self:
                    setattr(old_value, "employee15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee15"):
                opp_val = getattr(value, "employee15", None)
                setattr(value, "employee15", self)

    @property
    def leave11(self):
        return self.__leave11
    @leave11.setter
    def leave11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__leave11", None)
        self.__leave11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee10"):
                    opp_val = getattr(item, "employee10", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee10"):
                    opp_val = getattr(item, "employee10", None)
                    
                    if opp_val is None:
                        setattr(item, "employee10", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Admin:

    def __init__(self, username: str, password: str, attendance12: "Attendance" = None, employee1: "Employee" = None, leave2: "Leave" = None, login20: "login" = None, employee8: set["Employee"] = None):
        self.username = username
        self.password = password
        self.attendance12 = attendance12
        self.employee1 = employee1
        self.leave2 = leave2
        self.login20 = login20
        self.employee8 = employee8 if employee8 is not None else set()
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def login20(self):
        return self.__login20
    @login20.setter
    def login20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__login20", None)
        self.__login20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Admin21"):
                opp_val = getattr(old_value, "Admin21", None)
                if opp_val == self:
                    setattr(old_value, "Admin21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Admin21"):
                opp_val = getattr(value, "Admin21", None)
                setattr(value, "Admin21", self)

    @property
    def attendance12(self):
        return self.__attendance12
    @attendance12.setter
    def attendance12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__attendance12", None)
        self.__attendance12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Admin13"):
                opp_val = getattr(old_value, "Admin13", None)
                if opp_val == self:
                    setattr(old_value, "Admin13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Admin13"):
                opp_val = getattr(value, "Admin13", None)
                setattr(value, "Admin13", self)

    @property
    def leave2(self):
        return self.__leave2
    @leave2.setter
    def leave2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__leave2", None)
        self.__leave2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Admin3"):
                opp_val = getattr(old_value, "Admin3", None)
                if opp_val == self:
                    setattr(old_value, "Admin3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Admin3"):
                opp_val = getattr(value, "Admin3", None)
                setattr(value, "Admin3", self)

    @property
    def employee1(self):
        return self.__employee1
    @employee1.setter
    def employee1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__employee1", None)
        self.__employee1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Admin0"):
                opp_val = getattr(old_value, "Admin0", None)
                if opp_val == self:
                    setattr(old_value, "Admin0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Admin0"):
                opp_val = getattr(value, "Admin0", None)
                setattr(value, "Admin0", self)

    @property
    def employee8(self):
        return self.__employee8
    @employee8.setter
    def employee8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__employee8", None)
        self.__employee8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Admin9"):
                    opp_val = getattr(item, "Admin9", None)
                    
                    if opp_val == self:
                        setattr(item, "Admin9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Admin9"):
                    opp_val = getattr(item, "Admin9", None)
                    
                    setattr(item, "Admin9", self)
                    

