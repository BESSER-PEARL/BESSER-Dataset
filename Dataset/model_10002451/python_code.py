from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Employee_Actor:

    pass


class Administrator_Actor:

    pass


class Salary_Management_UseCase:

    pass


class Authentication_UseCase:

    pass





class Logout_external:

    pass


class Login_external:

    pass


class Employee_Management_System_Component:

    pass


class Login:

    def __init__(self, UserName: str, Password: str):
        self.UserName = UserName
        self.Password = Password
        
        pass
    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password



class Attendance:

    def __init__(self, Emp_id: str, Date: date, startTime: str, endTime: str, Employee_Attendance_13: "Employee" = None):
        self.Emp_id = Emp_id
        self.Date = Date
        self.startTime = startTime
        self.endTime = endTime
        self.Employee_Attendance_13 = Employee_Attendance_13
        
        pass
    @property
    def startTime(self):
        return self.__startTime
    @startTime.setter
    def startTime(self, startTime: str):
        self.__startTime = startTime

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: date):
        self.__Date = Date

    @property
    def endTime(self):
        return self.__endTime
    @endTime.setter
    def endTime(self, endTime: str):
        self.__endTime = endTime

    @property
    def Emp_id(self):
        return self.__Emp_id
    @Emp_id.setter
    def Emp_id(self, Emp_id: str):
        self.__Emp_id = Emp_id

    @property
    def Employee_Attendance_13(self):
        return self.__Employee_Attendance_13
    @Employee_Attendance_13.setter
    def Employee_Attendance_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Attendance__Employee_Attendance_13", None)
        self.__Employee_Attendance_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_Attendance_02"):
                opp_val = getattr(old_value, "Employee_Attendance_02", None)
                if opp_val == self:
                    setattr(old_value, "Employee_Attendance_02", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_Attendance_02"):
                opp_val = getattr(value, "Employee_Attendance_02", None)
                setattr(value, "Employee_Attendance_02", self)



class Leave:

    def __init__(self, leave_id: int, Emp_Id: int, Leave_Title: str, Leave_Type: str, Leave_ApplyDate: date, Leave_StartDate: date, Leave_EndDate: date, Leave_NoOfDays: int, Leave_Status: str, Employee_Leave_11: "Employee" = None):
        self.leave_id = leave_id
        self.Emp_Id = Emp_Id
        self.Leave_Title = Leave_Title
        self.Leave_Type = Leave_Type
        self.Leave_ApplyDate = Leave_ApplyDate
        self.Leave_StartDate = Leave_StartDate
        self.Leave_EndDate = Leave_EndDate
        self.Leave_NoOfDays = Leave_NoOfDays
        self.Leave_Status = Leave_Status
        self.Employee_Leave_11 = Employee_Leave_11
        
        pass
    @property
    def Leave_Type(self):
        return self.__Leave_Type
    @Leave_Type.setter
    def Leave_Type(self, Leave_Type: str):
        self.__Leave_Type = Leave_Type

    @property
    def Emp_Id(self):
        return self.__Emp_Id
    @Emp_Id.setter
    def Emp_Id(self, Emp_Id: int):
        self.__Emp_Id = Emp_Id

    @property
    def Leave_Status(self):
        return self.__Leave_Status
    @Leave_Status.setter
    def Leave_Status(self, Leave_Status: str):
        self.__Leave_Status = Leave_Status

    @property
    def Leave_EndDate(self):
        return self.__Leave_EndDate
    @Leave_EndDate.setter
    def Leave_EndDate(self, Leave_EndDate: date):
        self.__Leave_EndDate = Leave_EndDate

    @property
    def Leave_StartDate(self):
        return self.__Leave_StartDate
    @Leave_StartDate.setter
    def Leave_StartDate(self, Leave_StartDate: date):
        self.__Leave_StartDate = Leave_StartDate

    @property
    def Leave_Title(self):
        return self.__Leave_Title
    @Leave_Title.setter
    def Leave_Title(self, Leave_Title: str):
        self.__Leave_Title = Leave_Title

    @property
    def Leave_ApplyDate(self):
        return self.__Leave_ApplyDate
    @Leave_ApplyDate.setter
    def Leave_ApplyDate(self, Leave_ApplyDate: date):
        self.__Leave_ApplyDate = Leave_ApplyDate

    @property
    def Leave_NoOfDays(self):
        return self.__Leave_NoOfDays
    @Leave_NoOfDays.setter
    def Leave_NoOfDays(self, Leave_NoOfDays: int):
        self.__Leave_NoOfDays = Leave_NoOfDays

    @property
    def leave_id(self):
        return self.__leave_id
    @leave_id.setter
    def leave_id(self, leave_id: int):
        self.__leave_id = leave_id

    @property
    def Employee_Leave_11(self):
        return self.__Employee_Leave_11
    @Employee_Leave_11.setter
    def Employee_Leave_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Leave__Employee_Leave_11", None)
        self.__Employee_Leave_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_Leave_00"):
                opp_val = getattr(old_value, "Employee_Leave_00", None)
                if opp_val == self:
                    setattr(old_value, "Employee_Leave_00", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_Leave_00"):
                opp_val = getattr(value, "Employee_Leave_00", None)
                setattr(value, "Employee_Leave_00", self)



class Authenticate_staff:

    def __init__(self, UserName: str, Password: str, Authendication_Mood: str):
        self.UserName = UserName
        self.Password = Password
        self.Authendication_Mood = Authendication_Mood
        
        pass
    @property
    def Authendication_Mood(self):
        return self.__Authendication_Mood
    @Authendication_Mood.setter
    def Authendication_Mood(self, Authendication_Mood: str):
        self.__Authendication_Mood = Authendication_Mood

    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password



class Salary:

    def __init__(self, Sly_Decrement: float, Sly_Netgross: float, OverTime: str, Emp_Id: int, Sly_Basic: float, Sly_Increment: float, Employee_Salary_15: "Employee" = None):
        self.Sly_Decrement = Sly_Decrement
        self.Sly_Netgross = Sly_Netgross
        self.OverTime = OverTime
        self.Emp_Id = Emp_Id
        self.Sly_Basic = Sly_Basic
        self.Sly_Increment = Sly_Increment
        self.Employee_Salary_15 = Employee_Salary_15
        
        pass
    @property
    def Sly_Increment(self):
        return self.__Sly_Increment
    @Sly_Increment.setter
    def Sly_Increment(self, Sly_Increment: float):
        self.__Sly_Increment = Sly_Increment

    @property
    def Emp_Id(self):
        return self.__Emp_Id
    @Emp_Id.setter
    def Emp_Id(self, Emp_Id: int):
        self.__Emp_Id = Emp_Id

    @property
    def Sly_Basic(self):
        return self.__Sly_Basic
    @Sly_Basic.setter
    def Sly_Basic(self, Sly_Basic: float):
        self.__Sly_Basic = Sly_Basic

    @property
    def Sly_Netgross(self):
        return self.__Sly_Netgross
    @Sly_Netgross.setter
    def Sly_Netgross(self, Sly_Netgross: float):
        self.__Sly_Netgross = Sly_Netgross

    @property
    def OverTime(self):
        return self.__OverTime
    @OverTime.setter
    def OverTime(self, OverTime: str):
        self.__OverTime = OverTime

    @property
    def Sly_Decrement(self):
        return self.__Sly_Decrement
    @Sly_Decrement.setter
    def Sly_Decrement(self, Sly_Decrement: float):
        self.__Sly_Decrement = Sly_Decrement

    @property
    def Employee_Salary_15(self):
        return self.__Employee_Salary_15
    @Employee_Salary_15.setter
    def Employee_Salary_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Salary__Employee_Salary_15", None)
        self.__Employee_Salary_15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_Salary_04"):
                opp_val = getattr(old_value, "Employee_Salary_04", None)
                if opp_val == self:
                    setattr(old_value, "Employee_Salary_04", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_Salary_04"):
                opp_val = getattr(value, "Employee_Salary_04", None)
                setattr(value, "Employee_Salary_04", self)



class Employee:

    def __init__(self, Emp_Id: int, Emp_Name: str, Emp_ContactNo: str, Emp_Email: str, Emp_DOB: date, Emp_Designation: str, Emp_Salary: float, Employee_Leave_00: "Leave" = None, Employee_Attendance_02: "Attendance" = None, Employee_Salary_04: "Salary" = None):
        self.Emp_Id = Emp_Id
        self.Emp_Name = Emp_Name
        self.Emp_ContactNo = Emp_ContactNo
        self.Emp_Email = Emp_Email
        self.Emp_DOB = Emp_DOB
        self.Emp_Designation = Emp_Designation
        self.Emp_Salary = Emp_Salary
        self.Employee_Leave_00 = Employee_Leave_00
        self.Employee_Attendance_02 = Employee_Attendance_02
        self.Employee_Salary_04 = Employee_Salary_04
        
        pass
    @property
    def Emp_Designation(self):
        return self.__Emp_Designation
    @Emp_Designation.setter
    def Emp_Designation(self, Emp_Designation: str):
        self.__Emp_Designation = Emp_Designation

    @property
    def Emp_Salary(self):
        return self.__Emp_Salary
    @Emp_Salary.setter
    def Emp_Salary(self, Emp_Salary: float):
        self.__Emp_Salary = Emp_Salary

    @property
    def Emp_Email(self):
        return self.__Emp_Email
    @Emp_Email.setter
    def Emp_Email(self, Emp_Email: str):
        self.__Emp_Email = Emp_Email

    @property
    def Emp_DOB(self):
        return self.__Emp_DOB
    @Emp_DOB.setter
    def Emp_DOB(self, Emp_DOB: date):
        self.__Emp_DOB = Emp_DOB

    @property
    def Emp_Name(self):
        return self.__Emp_Name
    @Emp_Name.setter
    def Emp_Name(self, Emp_Name: str):
        self.__Emp_Name = Emp_Name

    @property
    def Emp_Id(self):
        return self.__Emp_Id
    @Emp_Id.setter
    def Emp_Id(self, Emp_Id: int):
        self.__Emp_Id = Emp_Id

    @property
    def Emp_ContactNo(self):
        return self.__Emp_ContactNo
    @Emp_ContactNo.setter
    def Emp_ContactNo(self, Emp_ContactNo: str):
        self.__Emp_ContactNo = Emp_ContactNo

    @property
    def Employee_Attendance_02(self):
        return self.__Employee_Attendance_02
    @Employee_Attendance_02.setter
    def Employee_Attendance_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__Employee_Attendance_02", None)
        self.__Employee_Attendance_02 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_Attendance_13"):
                opp_val = getattr(old_value, "Employee_Attendance_13", None)
                if opp_val == self:
                    setattr(old_value, "Employee_Attendance_13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_Attendance_13"):
                opp_val = getattr(value, "Employee_Attendance_13", None)
                setattr(value, "Employee_Attendance_13", self)

    @property
    def Employee_Leave_00(self):
        return self.__Employee_Leave_00
    @Employee_Leave_00.setter
    def Employee_Leave_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__Employee_Leave_00", None)
        self.__Employee_Leave_00 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_Leave_11"):
                opp_val = getattr(old_value, "Employee_Leave_11", None)
                if opp_val == self:
                    setattr(old_value, "Employee_Leave_11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_Leave_11"):
                opp_val = getattr(value, "Employee_Leave_11", None)
                setattr(value, "Employee_Leave_11", self)

    @property
    def Employee_Salary_04(self):
        return self.__Employee_Salary_04
    @Employee_Salary_04.setter
    def Employee_Salary_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__Employee_Salary_04", None)
        self.__Employee_Salary_04 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee_Salary_15"):
                opp_val = getattr(old_value, "Employee_Salary_15", None)
                if opp_val == self:
                    setattr(old_value, "Employee_Salary_15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee_Salary_15"):
                opp_val = getattr(value, "Employee_Salary_15", None)
                setattr(value, "Employee_Salary_15", self)

