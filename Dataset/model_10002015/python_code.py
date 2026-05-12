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





class Login_external:

    pass


class Logout_external:

    pass


class _10_7_1992:

    pass


class _10000:

    pass


class Employee:

    def __init__(self, Emp_Id: str, Emp_Name: str, Emp_ContactNo: str, Emp_Email: str, Emp_NIC: str, Emp_Address: str, Emp_DOB: _10_7_1992, Emp_Department: str, Emp_Date_Of_Joint: str, Emp_Position: str, Emp_Salary: str):
        self.Emp_Id = Emp_Id
        self.Emp_Name = Emp_Name
        self.Emp_ContactNo = Emp_ContactNo
        self.Emp_Email = Emp_Email
        self.Emp_NIC = Emp_NIC
        self.Emp_Address = Emp_Address
        self.Emp_DOB = Emp_DOB
        self.Emp_Department = Emp_Department
        self.Emp_Date_Of_Joint = Emp_Date_Of_Joint
        self.Emp_Position = Emp_Position
        self.Emp_Salary = Emp_Salary
        
        pass
    @property
    def Emp_Address(self):
        return self.__Emp_Address
    @Emp_Address.setter
    def Emp_Address(self, Emp_Address: str):
        self.__Emp_Address = Emp_Address

    @property
    def Emp_Salary(self):
        return self.__Emp_Salary
    @Emp_Salary.setter
    def Emp_Salary(self, Emp_Salary: str):
        self.__Emp_Salary = Emp_Salary

    @property
    def Emp_Id(self):
        return self.__Emp_Id
    @Emp_Id.setter
    def Emp_Id(self, Emp_Id: str):
        self.__Emp_Id = Emp_Id

    @property
    def Emp_DOB(self):
        return self.__Emp_DOB
    @Emp_DOB.setter
    def Emp_DOB(self, Emp_DOB: _10_7_1992):
        self.__Emp_DOB = Emp_DOB

    @property
    def Emp_Email(self):
        return self.__Emp_Email
    @Emp_Email.setter
    def Emp_Email(self, Emp_Email: str):
        self.__Emp_Email = Emp_Email

    @property
    def Emp_Position(self):
        return self.__Emp_Position
    @Emp_Position.setter
    def Emp_Position(self, Emp_Position: str):
        self.__Emp_Position = Emp_Position

    @property
    def Emp_ContactNo(self):
        return self.__Emp_ContactNo
    @Emp_ContactNo.setter
    def Emp_ContactNo(self, Emp_ContactNo: str):
        self.__Emp_ContactNo = Emp_ContactNo

    @property
    def Emp_Name(self):
        return self.__Emp_Name
    @Emp_Name.setter
    def Emp_Name(self, Emp_Name: str):
        self.__Emp_Name = Emp_Name

    @property
    def Emp_Department(self):
        return self.__Emp_Department
    @Emp_Department.setter
    def Emp_Department(self, Emp_Department: str):
        self.__Emp_Department = Emp_Department

    @property
    def Emp_Date_Of_Joint(self):
        return self.__Emp_Date_Of_Joint
    @Emp_Date_Of_Joint.setter
    def Emp_Date_Of_Joint(self, Emp_Date_Of_Joint: str):
        self.__Emp_Date_Of_Joint = Emp_Date_Of_Joint

    @property
    def Emp_NIC(self):
        return self.__Emp_NIC
    @Emp_NIC.setter
    def Emp_NIC(self, Emp_NIC: str):
        self.__Emp_NIC = Emp_NIC



class Employee_Management_System_Component:

    pass


class T:

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

    def __init__(self, Attend_date: str, Emp_id: str, AttendTime: str, Leaving_Time: str, Employee_Attendance_13: "User" = None):
        self.Attend_date = Attend_date
        self.Emp_id = Emp_id
        self.AttendTime = AttendTime
        self.Leaving_Time = Leaving_Time
        self.Employee_Attendance_13 = Employee_Attendance_13
        
        pass
    @property
    def AttendTime(self):
        return self.__AttendTime
    @AttendTime.setter
    def AttendTime(self, AttendTime: str):
        self.__AttendTime = AttendTime

    @property
    def Attend_date(self):
        return self.__Attend_date
    @Attend_date.setter
    def Attend_date(self, Attend_date: str):
        self.__Attend_date = Attend_date

    @property
    def Leaving_Time(self):
        return self.__Leaving_Time
    @Leaving_Time.setter
    def Leaving_Time(self, Leaving_Time: str):
        self.__Leaving_Time = Leaving_Time

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



class L__Leave:

    def __init__(self, leave_id: str, Emp_Id: str, Leave_Title: str, Leave_detail: str, Leave_ApplyDate: str, Leave_StartDate: str, Leave_EndDate: str, Leave_NoOfDays: str, Leave_Status: str, Employee_Leave_11: "User" = None):
        self.leave_id = leave_id
        self.Emp_Id = Emp_Id
        self.Leave_Title = Leave_Title
        self.Leave_detail = Leave_detail
        self.Leave_ApplyDate = Leave_ApplyDate
        self.Leave_StartDate = Leave_StartDate
        self.Leave_EndDate = Leave_EndDate
        self.Leave_NoOfDays = Leave_NoOfDays
        self.Leave_Status = Leave_Status
        self.Employee_Leave_11 = Employee_Leave_11
        
        pass
    @property
    def Leave_StartDate(self):
        return self.__Leave_StartDate
    @Leave_StartDate.setter
    def Leave_StartDate(self, Leave_StartDate: str):
        self.__Leave_StartDate = Leave_StartDate

    @property
    def Leave_detail(self):
        return self.__Leave_detail
    @Leave_detail.setter
    def Leave_detail(self, Leave_detail: str):
        self.__Leave_detail = Leave_detail

    @property
    def Leave_Status(self):
        return self.__Leave_Status
    @Leave_Status.setter
    def Leave_Status(self, Leave_Status: str):
        self.__Leave_Status = Leave_Status

    @property
    def Leave_ApplyDate(self):
        return self.__Leave_ApplyDate
    @Leave_ApplyDate.setter
    def Leave_ApplyDate(self, Leave_ApplyDate: str):
        self.__Leave_ApplyDate = Leave_ApplyDate

    @property
    def Leave_EndDate(self):
        return self.__Leave_EndDate
    @Leave_EndDate.setter
    def Leave_EndDate(self, Leave_EndDate: str):
        self.__Leave_EndDate = Leave_EndDate

    @property
    def Emp_Id(self):
        return self.__Emp_Id
    @Emp_Id.setter
    def Emp_Id(self, Emp_Id: str):
        self.__Emp_Id = Emp_Id

    @property
    def Leave_NoOfDays(self):
        return self.__Leave_NoOfDays
    @Leave_NoOfDays.setter
    def Leave_NoOfDays(self, Leave_NoOfDays: str):
        self.__Leave_NoOfDays = Leave_NoOfDays

    @property
    def Leave_Title(self):
        return self.__Leave_Title
    @Leave_Title.setter
    def Leave_Title(self, Leave_Title: str):
        self.__Leave_Title = Leave_Title

    @property
    def leave_id(self):
        return self.__leave_id
    @leave_id.setter
    def leave_id(self, leave_id: str):
        self.__leave_id = leave_id

    @property
    def Employee_Leave_11(self):
        return self.__Employee_Leave_11
    @Employee_Leave_11.setter
    def Employee_Leave_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_L__Leave__Employee_Leave_11", None)
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



class Admin:

    def __init__(self, UserName: str, Password: str, attribute: str):
        self.UserName = UserName
        self.Password = Password
        self.attribute = attribute
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



class Salary:

    def __init__(self, Emp_Id: str, Sly_Basic: str, Sly_Increment: _10000, Sly_Decrement: str, Sly_Netgross: str, OverTime: str, Employee_Salary_15: "User" = None):
        self.Emp_Id = Emp_Id
        self.Sly_Basic = Sly_Basic
        self.Sly_Increment = Sly_Increment
        self.Sly_Decrement = Sly_Decrement
        self.Sly_Netgross = Sly_Netgross
        self.OverTime = OverTime
        self.Employee_Salary_15 = Employee_Salary_15
        
        pass
    @property
    def Sly_Decrement(self):
        return self.__Sly_Decrement
    @Sly_Decrement.setter
    def Sly_Decrement(self, Sly_Decrement: str):
        self.__Sly_Decrement = Sly_Decrement

    @property
    def OverTime(self):
        return self.__OverTime
    @OverTime.setter
    def OverTime(self, OverTime: str):
        self.__OverTime = OverTime

    @property
    def Emp_Id(self):
        return self.__Emp_Id
    @Emp_Id.setter
    def Emp_Id(self, Emp_Id: str):
        self.__Emp_Id = Emp_Id

    @property
    def Sly_Basic(self):
        return self.__Sly_Basic
    @Sly_Basic.setter
    def Sly_Basic(self, Sly_Basic: str):
        self.__Sly_Basic = Sly_Basic

    @property
    def Sly_Increment(self):
        return self.__Sly_Increment
    @Sly_Increment.setter
    def Sly_Increment(self, Sly_Increment: _10000):
        self.__Sly_Increment = Sly_Increment

    @property
    def Sly_Netgross(self):
        return self.__Sly_Netgross
    @Sly_Netgross.setter
    def Sly_Netgross(self, Sly_Netgross: str):
        self.__Sly_Netgross = Sly_Netgross

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



class User:

    def __init__(self, User_Id: str, User_Name: str, User_contact: str, User_Email: str, User_Address: str, User_DOB: str, Employee_Leave_00: "L__Leave" = None, Employee_Attendance_02: "Attendance" = None, Employee_Salary_04: "Salary" = None):
        self.User_Id = User_Id
        self.User_Name = User_Name
        self.User_contact = User_contact
        self.User_Email = User_Email
        self.User_Address = User_Address
        self.User_DOB = User_DOB
        self.Employee_Leave_00 = Employee_Leave_00
        self.Employee_Attendance_02 = Employee_Attendance_02
        self.Employee_Salary_04 = Employee_Salary_04
        
        pass
    @property
    def User_Id(self):
        return self.__User_Id
    @User_Id.setter
    def User_Id(self, User_Id: str):
        self.__User_Id = User_Id

    @property
    def User_DOB(self):
        return self.__User_DOB
    @User_DOB.setter
    def User_DOB(self, User_DOB: str):
        self.__User_DOB = User_DOB

    @property
    def User_Email(self):
        return self.__User_Email
    @User_Email.setter
    def User_Email(self, User_Email: str):
        self.__User_Email = User_Email

    @property
    def User_Name(self):
        return self.__User_Name
    @User_Name.setter
    def User_Name(self, User_Name: str):
        self.__User_Name = User_Name

    @property
    def User_contact(self):
        return self.__User_contact
    @User_contact.setter
    def User_contact(self, User_contact: str):
        self.__User_contact = User_contact

    @property
    def User_Address(self):
        return self.__User_Address
    @User_Address.setter
    def User_Address(self, User_Address: str):
        self.__User_Address = User_Address

    @property
    def Employee_Salary_04(self):
        return self.__Employee_Salary_04
    @Employee_Salary_04.setter
    def Employee_Salary_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__Employee_Salary_04", None)
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

    @property
    def Employee_Leave_00(self):
        return self.__Employee_Leave_00
    @Employee_Leave_00.setter
    def Employee_Leave_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__Employee_Leave_00", None)
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
    def Employee_Attendance_02(self):
        return self.__Employee_Attendance_02
    @Employee_Attendance_02.setter
    def Employee_Attendance_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__Employee_Attendance_02", None)
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

