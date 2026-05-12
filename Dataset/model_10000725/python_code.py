from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Database:

    def __init__(self, Category: str, Attendance: str, Attendance_Database_19: "Attendance" = None):
        self.Category = Category
        self.Attendance = Attendance
        self.Attendance_Database_19 = Attendance_Database_19
        
        pass
    @property
    def Attendance(self):
        return self.__Attendance
    @Attendance.setter
    def Attendance(self, Attendance: str):
        self.__Attendance = Attendance

    @property
    def Category(self):
        return self.__Category
    @Category.setter
    def Category(self, Category: str):
        self.__Category = Category

    @property
    def Attendance_Database_19(self):
        return self.__Attendance_Database_19
    @Attendance_Database_19.setter
    def Attendance_Database_19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Database__Attendance_Database_19", None)
        self.__Attendance_Database_19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attendance_Database_08"):
                opp_val = getattr(old_value, "Attendance_Database_08", None)
                if opp_val == self:
                    setattr(old_value, "Attendance_Database_08", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attendance_Database_08"):
                opp_val = getattr(value, "Attendance_Database_08", None)
                setattr(value, "Attendance_Database_08", self)



class Attendance:

    def __init__(self, ID: str, Date: str, user1: "Student" = None, Faculty_Attendance_17: "Faculty" = None, Attendance_Database_08: "Database" = None):
        self.ID = ID
        self.Date = Date
        self.user1 = user1
        self.Faculty_Attendance_17 = Faculty_Attendance_17
        self.Attendance_Database_08 = Attendance_Database_08
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def user1(self):
        return self.__user1
    @user1.setter
    def user1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Attendance__user1", None)
        self.__user1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login0"):
                opp_val = getattr(old_value, "login0", None)
                if opp_val == self:
                    setattr(old_value, "login0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login0"):
                opp_val = getattr(value, "login0", None)
                setattr(value, "login0", self)

    @property
    def Attendance_Database_08(self):
        return self.__Attendance_Database_08
    @Attendance_Database_08.setter
    def Attendance_Database_08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Attendance__Attendance_Database_08", None)
        self.__Attendance_Database_08 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attendance_Database_19"):
                opp_val = getattr(old_value, "Attendance_Database_19", None)
                if opp_val == self:
                    setattr(old_value, "Attendance_Database_19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attendance_Database_19"):
                opp_val = getattr(value, "Attendance_Database_19", None)
                setattr(value, "Attendance_Database_19", self)

    @property
    def Faculty_Attendance_17(self):
        return self.__Faculty_Attendance_17
    @Faculty_Attendance_17.setter
    def Faculty_Attendance_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Attendance__Faculty_Attendance_17", None)
        self.__Faculty_Attendance_17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Faculty_Attendance_06"):
                opp_val = getattr(old_value, "Faculty_Attendance_06", None)
                if opp_val == self:
                    setattr(old_value, "Faculty_Attendance_06", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Faculty_Attendance_06"):
                opp_val = getattr(value, "Faculty_Attendance_06", None)
                setattr(value, "Faculty_Attendance_06", self)



class Monitor:

    def __init__(self, Date: date, Location: str, Time: int, user3: "Student" = None):
        self.Date = Date
        self.Location = Location
        self.Time = Time
        self.user3 = user3
        
        pass
    @property
    def Time(self):
        return self.__Time
    @Time.setter
    def Time(self, Time: int):
        self.__Time = Time

    @property
    def Location(self):
        return self.__Location
    @Location.setter
    def Location(self, Location: str):
        self.__Location = Location

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: date):
        self.__Date = Date

    @property
    def user3(self):
        return self.__user3
    @user3.setter
    def user3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Monitor__user3", None)
        self.__user3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "message2"):
                opp_val = getattr(old_value, "message2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "message2"):
                opp_val = getattr(value, "message2", None)
                if opp_val is None:
                    setattr(value, "message2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Login:

    def __init__(self, Username: str, Password: str, login: Faculty, Faculty_Login_15: "Faculty" = None, Student_Login_111: "Student" = None):
        self.Username = Username
        self.Password = Password
        self.login = login
        self.Faculty_Login_15 = Faculty_Login_15
        self.Student_Login_111 = Student_Login_111
        
        pass
    @property
    def Username(self):
        return self.__Username
    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login: Faculty):
        self.__login = login

    @property
    def Faculty_Login_15(self):
        return self.__Faculty_Login_15
    @Faculty_Login_15.setter
    def Faculty_Login_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__Faculty_Login_15", None)
        self.__Faculty_Login_15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Faculty_Login_04"):
                opp_val = getattr(old_value, "Faculty_Login_04", None)
                if opp_val == self:
                    setattr(old_value, "Faculty_Login_04", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Faculty_Login_04"):
                opp_val = getattr(value, "Faculty_Login_04", None)
                setattr(value, "Faculty_Login_04", self)

    @property
    def Student_Login_111(self):
        return self.__Student_Login_111
    @Student_Login_111.setter
    def Student_Login_111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__Student_Login_111", None)
        self.__Student_Login_111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Student_Login_010"):
                opp_val = getattr(old_value, "Student_Login_010", None)
                if opp_val == self:
                    setattr(old_value, "Student_Login_010", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Student_Login_010"):
                opp_val = getattr(value, "Student_Login_010", None)
                setattr(value, "Student_Login_010", self)



class Faculty:

    def __init__(self, ID: str, Username: str, Password: str, Faculty_Login_04: "Login" = None, Faculty_Attendance_06: "Attendance" = None):
        self.ID = ID
        self.Username = Username
        self.Password = Password
        self.Faculty_Login_04 = Faculty_Login_04
        self.Faculty_Attendance_06 = Faculty_Attendance_06
        
        pass
    @property
    def Username(self):
        return self.__Username
    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Faculty_Login_04(self):
        return self.__Faculty_Login_04
    @Faculty_Login_04.setter
    def Faculty_Login_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Faculty__Faculty_Login_04", None)
        self.__Faculty_Login_04 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Faculty_Login_15"):
                opp_val = getattr(old_value, "Faculty_Login_15", None)
                if opp_val == self:
                    setattr(old_value, "Faculty_Login_15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Faculty_Login_15"):
                opp_val = getattr(value, "Faculty_Login_15", None)
                setattr(value, "Faculty_Login_15", self)

    @property
    def Faculty_Attendance_06(self):
        return self.__Faculty_Attendance_06
    @Faculty_Attendance_06.setter
    def Faculty_Attendance_06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Faculty__Faculty_Attendance_06", None)
        self.__Faculty_Attendance_06 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Faculty_Attendance_17"):
                opp_val = getattr(old_value, "Faculty_Attendance_17", None)
                if opp_val == self:
                    setattr(old_value, "Faculty_Attendance_17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Faculty_Attendance_17"):
                opp_val = getattr(value, "Faculty_Attendance_17", None)
                setattr(value, "Faculty_Attendance_17", self)



class Student:

    def __init__(self, Username: str, ID: str, Password: str, First_Name: str, Last_Name: str, login0: "Attendance" = None, message2: set["Monitor"] = None, Student_Login_010: "Login" = None):
        self.Username = Username
        self.ID = ID
        self.Password = Password
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.login0 = login0
        self.message2 = message2 if message2 is not None else set()
        self.Student_Login_010 = Student_Login_010
        
        pass
    @property
    def Username(self):
        return self.__Username
    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username

    @property
    def First_Name(self):
        return self.__First_Name
    @First_Name.setter
    def First_Name(self, First_Name: str):
        self.__First_Name = First_Name

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def Last_Name(self):
        return self.__Last_Name
    @Last_Name.setter
    def Last_Name(self, Last_Name: str):
        self.__Last_Name = Last_Name

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def message2(self):
        return self.__message2
    @message2.setter
    def message2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__message2", None)
        self.__message2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user3"):
                    opp_val = getattr(item, "user3", None)
                    
                    if opp_val == self:
                        setattr(item, "user3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user3"):
                    opp_val = getattr(item, "user3", None)
                    
                    setattr(item, "user3", self)
                    

    @property
    def Student_Login_010(self):
        return self.__Student_Login_010
    @Student_Login_010.setter
    def Student_Login_010(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__Student_Login_010", None)
        self.__Student_Login_010 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Student_Login_111"):
                opp_val = getattr(old_value, "Student_Login_111", None)
                if opp_val == self:
                    setattr(old_value, "Student_Login_111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Student_Login_111"):
                opp_val = getattr(value, "Student_Login_111", None)
                setattr(value, "Student_Login_111", self)

    @property
    def login0(self):
        return self.__login0
    @login0.setter
    def login0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__login0", None)
        self.__login0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user1"):
                opp_val = getattr(old_value, "user1", None)
                if opp_val == self:
                    setattr(old_value, "user1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user1"):
                opp_val = getattr(value, "user1", None)
                setattr(value, "user1", self)

