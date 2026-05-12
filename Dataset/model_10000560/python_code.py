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

    def __init__(self, Attend_date: date, Emp_id: str, AttendTime: str, Leaving_Time: str, employee3: "Employee" = None):
        self.Attend_date = Attend_date
        self.Emp_id = Emp_id
        self.AttendTime = AttendTime
        self.Leaving_Time = Leaving_Time
        self.employee3 = employee3
        
        pass
    @property
    def Emp_id(self):
        return self.__Emp_id
    @Emp_id.setter
    def Emp_id(self, Emp_id: str):
        self.__Emp_id = Emp_id

    @property
    def Attend_date(self):
        return self.__Attend_date
    @Attend_date.setter
    def Attend_date(self, Attend_date: date):
        self.__Attend_date = Attend_date

    @property
    def Leaving_Time(self):
        return self.__Leaving_Time
    @Leaving_Time.setter
    def Leaving_Time(self, Leaving_Time: str):
        self.__Leaving_Time = Leaving_Time

    @property
    def AttendTime(self):
        return self.__AttendTime
    @AttendTime.setter
    def AttendTime(self, AttendTime: str):
        self.__AttendTime = AttendTime

    @property
    def employee3(self):
        return self.__employee3
    @employee3.setter
    def employee3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Attendance__employee3", None)
        self.__employee3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attendance2"):
                opp_val = getattr(old_value, "attendance2", None)
                if opp_val == self:
                    setattr(old_value, "attendance2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attendance2"):
                opp_val = getattr(value, "attendance2", None)
                setattr(value, "attendance2", self)



class Leave:

    def __init__(self, leave_id: int, Emp_Id: int, Leave_Title: str, Leave_detail: str, Leave_ApplyDate: date, Leave_StartDate: date, Leave_EndDate: date, Leave_NoOfDays: int, Leave_Status: str, employee1: "Employee" = None):
        self.leave_id = leave_id
        self.Emp_Id = Emp_Id
        self.Leave_Title = Leave_Title
        self.Leave_detail = Leave_detail
        self.Leave_ApplyDate = Leave_ApplyDate
        self.Leave_StartDate = Leave_StartDate
        self.Leave_EndDate = Leave_EndDate
        self.Leave_NoOfDays = Leave_NoOfDays
        self.Leave_Status = Leave_Status
        self.employee1 = employee1
        
        pass
    @property
    def Leave_Title(self):
        return self.__Leave_Title
    @Leave_Title.setter
    def Leave_Title(self, Leave_Title: str):
        self.__Leave_Title = Leave_Title

    @property
    def Leave_Status(self):
        return self.__Leave_Status
    @Leave_Status.setter
    def Leave_Status(self, Leave_Status: str):
        self.__Leave_Status = Leave_Status

    @property
    def leave_id(self):
        return self.__leave_id
    @leave_id.setter
    def leave_id(self, leave_id: int):
        self.__leave_id = leave_id

    @property
    def Leave_StartDate(self):
        return self.__Leave_StartDate
    @Leave_StartDate.setter
    def Leave_StartDate(self, Leave_StartDate: date):
        self.__Leave_StartDate = Leave_StartDate

    @property
    def Leave_ApplyDate(self):
        return self.__Leave_ApplyDate
    @Leave_ApplyDate.setter
    def Leave_ApplyDate(self, Leave_ApplyDate: date):
        self.__Leave_ApplyDate = Leave_ApplyDate

    @property
    def Emp_Id(self):
        return self.__Emp_Id
    @Emp_Id.setter
    def Emp_Id(self, Emp_Id: int):
        self.__Emp_Id = Emp_Id

    @property
    def Leave_EndDate(self):
        return self.__Leave_EndDate
    @Leave_EndDate.setter
    def Leave_EndDate(self, Leave_EndDate: date):
        self.__Leave_EndDate = Leave_EndDate

    @property
    def Leave_NoOfDays(self):
        return self.__Leave_NoOfDays
    @Leave_NoOfDays.setter
    def Leave_NoOfDays(self, Leave_NoOfDays: int):
        self.__Leave_NoOfDays = Leave_NoOfDays

    @property
    def Leave_detail(self):
        return self.__Leave_detail
    @Leave_detail.setter
    def Leave_detail(self, Leave_detail: str):
        self.__Leave_detail = Leave_detail

    @property
    def employee1(self):
        return self.__employee1
    @employee1.setter
    def employee1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Leave__employee1", None)
        self.__employee1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leave0"):
                opp_val = getattr(old_value, "leave0", None)
                if opp_val == self:
                    setattr(old_value, "leave0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leave0"):
                opp_val = getattr(value, "leave0", None)
                setattr(value, "leave0", self)



class Authenticate_staff:

    def __init__(self, UserName: str, Password: str, Authendication_Mood: str):
        self.UserName = UserName
        self.Password = Password
        self.Authendication_Mood = Authendication_Mood
        
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

    @property
    def Authendication_Mood(self):
        return self.__Authendication_Mood
    @Authendication_Mood.setter
    def Authendication_Mood(self, Authendication_Mood: str):
        self.__Authendication_Mood = Authendication_Mood



class Salary:

    def __init__(self, Emp_Id: int, Sly_Basic: float, Sly_Increment: float, Sly_Decrement: float, Sly_Netgross: float, OverTime: str, employee5: "Employee" = None):
        self.Emp_Id = Emp_Id
        self.Sly_Basic = Sly_Basic
        self.Sly_Increment = Sly_Increment
        self.Sly_Decrement = Sly_Decrement
        self.Sly_Netgross = Sly_Netgross
        self.OverTime = OverTime
        self.employee5 = employee5
        
        pass
    @property
    def Sly_Decrement(self):
        return self.__Sly_Decrement
    @Sly_Decrement.setter
    def Sly_Decrement(self, Sly_Decrement: float):
        self.__Sly_Decrement = Sly_Decrement

    @property
    def Sly_Basic(self):
        return self.__Sly_Basic
    @Sly_Basic.setter
    def Sly_Basic(self, Sly_Basic: float):
        self.__Sly_Basic = Sly_Basic

    @property
    def OverTime(self):
        return self.__OverTime
    @OverTime.setter
    def OverTime(self, OverTime: str):
        self.__OverTime = OverTime

    @property
    def Sly_Netgross(self):
        return self.__Sly_Netgross
    @Sly_Netgross.setter
    def Sly_Netgross(self, Sly_Netgross: float):
        self.__Sly_Netgross = Sly_Netgross

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
    def employee5(self):
        return self.__employee5
    @employee5.setter
    def employee5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Salary__employee5", None)
        self.__employee5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "salary4"):
                opp_val = getattr(old_value, "salary4", None)
                if opp_val == self:
                    setattr(old_value, "salary4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "salary4"):
                opp_val = getattr(value, "salary4", None)
                setattr(value, "salary4", self)



class Employee:

    def __init__(self, Emp_Id: int, Emp_Name: str, Emp_ContactNo: str, Emp_Email: str, Emp_NIC: str, Emp_Address: str, Emp_DOB: date, Emp_Department: str, Emp_Date_Of_Joint: date, Emp_Position: str, Emp_Salary: float, leave0: "Leave" = None, attendance2: "Attendance" = None, salary4: "Salary" = None):
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
        self.leave0 = leave0
        self.attendance2 = attendance2
        self.salary4 = salary4
        
        pass
    @property
    def Emp_Address(self):
        return self.__Emp_Address
    @Emp_Address.setter
    def Emp_Address(self, Emp_Address: str):
        self.__Emp_Address = Emp_Address

    @property
    def Emp_Date_Of_Joint(self):
        return self.__Emp_Date_Of_Joint
    @Emp_Date_Of_Joint.setter
    def Emp_Date_Of_Joint(self, Emp_Date_Of_Joint: date):
        self.__Emp_Date_Of_Joint = Emp_Date_Of_Joint

    @property
    def Emp_NIC(self):
        return self.__Emp_NIC
    @Emp_NIC.setter
    def Emp_NIC(self, Emp_NIC: str):
        self.__Emp_NIC = Emp_NIC

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
    def Emp_ContactNo(self):
        return self.__Emp_ContactNo
    @Emp_ContactNo.setter
    def Emp_ContactNo(self, Emp_ContactNo: str):
        self.__Emp_ContactNo = Emp_ContactNo

    @property
    def Emp_Department(self):
        return self.__Emp_Department
    @Emp_Department.setter
    def Emp_Department(self, Emp_Department: str):
        self.__Emp_Department = Emp_Department

    @property
    def Emp_Id(self):
        return self.__Emp_Id
    @Emp_Id.setter
    def Emp_Id(self, Emp_Id: int):
        self.__Emp_Id = Emp_Id

    @property
    def Emp_Position(self):
        return self.__Emp_Position
    @Emp_Position.setter
    def Emp_Position(self, Emp_Position: str):
        self.__Emp_Position = Emp_Position

    @property
    def Emp_Name(self):
        return self.__Emp_Name
    @Emp_Name.setter
    def Emp_Name(self, Emp_Name: str):
        self.__Emp_Name = Emp_Name

    @property
    def salary4(self):
        return self.__salary4
    @salary4.setter
    def salary4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__salary4", None)
        self.__salary4 = value
        
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
    def leave0(self):
        return self.__leave0
    @leave0.setter
    def leave0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__leave0", None)
        self.__leave0 = value
        
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
    def attendance2(self):
        return self.__attendance2
    @attendance2.setter
    def attendance2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__attendance2", None)
        self.__attendance2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee3"):
                opp_val = getattr(old_value, "employee3", None)
                if opp_val == self:
                    setattr(old_value, "employee3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee3"):
                opp_val = getattr(value, "employee3", None)
                setattr(value, "employee3", self)

