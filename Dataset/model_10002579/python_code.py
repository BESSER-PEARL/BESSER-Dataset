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





class Employee_Management_System_Component:

    pass


class Login:

    def __init__(self, Password: str, UserName: str):
        self.Password = Password
        self.UserName = UserName
        
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



class Attendance:

    def __init__(self, Attend_date: date, Emp_id: str, AttendTime: str, Leaving_Time: str, staff3: "staff_member" = None):
        self.Attend_date = Attend_date
        self.Emp_id = Emp_id
        self.AttendTime = AttendTime
        self.Leaving_Time = Leaving_Time
        self.staff3 = staff3
        
        pass
    @property
    def AttendTime(self):
        return self.__AttendTime
    @AttendTime.setter
    def AttendTime(self, AttendTime: str):
        self.__AttendTime = AttendTime

    @property
    def Emp_id(self):
        return self.__Emp_id
    @Emp_id.setter
    def Emp_id(self, Emp_id: str):
        self.__Emp_id = Emp_id

    @property
    def Leaving_Time(self):
        return self.__Leaving_Time
    @Leaving_Time.setter
    def Leaving_Time(self, Leaving_Time: str):
        self.__Leaving_Time = Leaving_Time

    @property
    def Attend_date(self):
        return self.__Attend_date
    @Attend_date.setter
    def Attend_date(self, Attend_date: date):
        self.__Attend_date = Attend_date

    @property
    def staff3(self):
        return self.__staff3
    @staff3.setter
    def staff3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Attendance__staff3", None)
        self.__staff3 = value
        
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



class Mission:

    def __init__(self, mission_id: int, staff_Id: int, mission_Title: str, mission_detail: str, mission_StartDate: date, mission_EndDate: date, mission_NoOfDays: int, mission_Status: str, staff1: "staff_member" = None):
        self.mission_id = mission_id
        self.staff_Id = staff_Id
        self.mission_Title = mission_Title
        self.mission_detail = mission_detail
        self.mission_StartDate = mission_StartDate
        self.mission_EndDate = mission_EndDate
        self.mission_NoOfDays = mission_NoOfDays
        self.mission_Status = mission_Status
        self.staff1 = staff1
        
        pass
    @property
    def mission_NoOfDays(self):
        return self.__mission_NoOfDays
    @mission_NoOfDays.setter
    def mission_NoOfDays(self, mission_NoOfDays: int):
        self.__mission_NoOfDays = mission_NoOfDays

    @property
    def mission_detail(self):
        return self.__mission_detail
    @mission_detail.setter
    def mission_detail(self, mission_detail: str):
        self.__mission_detail = mission_detail

    @property
    def mission_id(self):
        return self.__mission_id
    @mission_id.setter
    def mission_id(self, mission_id: int):
        self.__mission_id = mission_id

    @property
    def mission_EndDate(self):
        return self.__mission_EndDate
    @mission_EndDate.setter
    def mission_EndDate(self, mission_EndDate: date):
        self.__mission_EndDate = mission_EndDate

    @property
    def mission_Status(self):
        return self.__mission_Status
    @mission_Status.setter
    def mission_Status(self, mission_Status: str):
        self.__mission_Status = mission_Status

    @property
    def mission_Title(self):
        return self.__mission_Title
    @mission_Title.setter
    def mission_Title(self, mission_Title: str):
        self.__mission_Title = mission_Title

    @property
    def staff_Id(self):
        return self.__staff_Id
    @staff_Id.setter
    def staff_Id(self, staff_Id: int):
        self.__staff_Id = staff_Id

    @property
    def mission_StartDate(self):
        return self.__mission_StartDate
    @mission_StartDate.setter
    def mission_StartDate(self, mission_StartDate: date):
        self.__mission_StartDate = mission_StartDate

    @property
    def staff1(self):
        return self.__staff1
    @staff1.setter
    def staff1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mission__staff1", None)
        self.__staff1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff0"):
                opp_val = getattr(old_value, "staff0", None)
                if opp_val == self:
                    setattr(old_value, "staff0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff0"):
                opp_val = getattr(value, "staff0", None)
                setattr(value, "staff0", self)



class Authenticate_staff:

    def __init__(self, Password: str, Authendication_Mood: str, UserName: str):
        self.Password = Password
        self.Authendication_Mood = Authendication_Mood
        self.UserName = UserName
        
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

    def __init__(self, Emp_Id: int, Sly_Basic: float, Sly_Increment: float, Sly_Decrement: float, Sly_Netgross: float, OverTime: str, staff5: "staff_member" = None):
        self.Emp_Id = Emp_Id
        self.Sly_Basic = Sly_Basic
        self.Sly_Increment = Sly_Increment
        self.Sly_Decrement = Sly_Decrement
        self.Sly_Netgross = Sly_Netgross
        self.OverTime = OverTime
        self.staff5 = staff5
        
        pass
    @property
    def Sly_Decrement(self):
        return self.__Sly_Decrement
    @Sly_Decrement.setter
    def Sly_Decrement(self, Sly_Decrement: float):
        self.__Sly_Decrement = Sly_Decrement

    @property
    def Sly_Increment(self):
        return self.__Sly_Increment
    @Sly_Increment.setter
    def Sly_Increment(self, Sly_Increment: float):
        self.__Sly_Increment = Sly_Increment

    @property
    def Sly_Netgross(self):
        return self.__Sly_Netgross
    @Sly_Netgross.setter
    def Sly_Netgross(self, Sly_Netgross: float):
        self.__Sly_Netgross = Sly_Netgross

    @property
    def Emp_Id(self):
        return self.__Emp_Id
    @Emp_Id.setter
    def Emp_Id(self, Emp_Id: int):
        self.__Emp_Id = Emp_Id

    @property
    def OverTime(self):
        return self.__OverTime
    @OverTime.setter
    def OverTime(self, OverTime: str):
        self.__OverTime = OverTime

    @property
    def Sly_Basic(self):
        return self.__Sly_Basic
    @Sly_Basic.setter
    def Sly_Basic(self, Sly_Basic: float):
        self.__Sly_Basic = Sly_Basic

    @property
    def staff5(self):
        return self.__staff5
    @staff5.setter
    def staff5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Salary__staff5", None)
        self.__staff5 = value
        
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



class staff_member:

    def __init__(self, staff_Salary: float, staff_Id: int, staff_Name: str, staff_ContactNo: str, staff_Email: str, staff_NIC: str, staff_Address: str, staff_DOB: date, staff_Department: str, staff_Date_Of_Joint: date, staff_Position: str, staff0: "Mission" = None, attendance2: "Attendance" = None, salary4: "Salary" = None):
        self.staff_Salary = staff_Salary
        self.staff_Id = staff_Id
        self.staff_Name = staff_Name
        self.staff_ContactNo = staff_ContactNo
        self.staff_Email = staff_Email
        self.staff_NIC = staff_NIC
        self.staff_Address = staff_Address
        self.staff_DOB = staff_DOB
        self.staff_Department = staff_Department
        self.staff_Date_Of_Joint = staff_Date_Of_Joint
        self.staff_Position = staff_Position
        self.staff0 = staff0
        self.attendance2 = attendance2
        self.salary4 = salary4
        
        pass
    @property
    def staff_ContactNo(self):
        return self.__staff_ContactNo
    @staff_ContactNo.setter
    def staff_ContactNo(self, staff_ContactNo: str):
        self.__staff_ContactNo = staff_ContactNo

    @property
    def staff_Department(self):
        return self.__staff_Department
    @staff_Department.setter
    def staff_Department(self, staff_Department: str):
        self.__staff_Department = staff_Department

    @property
    def staff_Position(self):
        return self.__staff_Position
    @staff_Position.setter
    def staff_Position(self, staff_Position: str):
        self.__staff_Position = staff_Position

    @property
    def staff_DOB(self):
        return self.__staff_DOB
    @staff_DOB.setter
    def staff_DOB(self, staff_DOB: date):
        self.__staff_DOB = staff_DOB

    @property
    def staff_NIC(self):
        return self.__staff_NIC
    @staff_NIC.setter
    def staff_NIC(self, staff_NIC: str):
        self.__staff_NIC = staff_NIC

    @property
    def staff_Id(self):
        return self.__staff_Id
    @staff_Id.setter
    def staff_Id(self, staff_Id: int):
        self.__staff_Id = staff_Id

    @property
    def staff_Salary(self):
        return self.__staff_Salary
    @staff_Salary.setter
    def staff_Salary(self, staff_Salary: float):
        self.__staff_Salary = staff_Salary

    @property
    def staff_Email(self):
        return self.__staff_Email
    @staff_Email.setter
    def staff_Email(self, staff_Email: str):
        self.__staff_Email = staff_Email

    @property
    def staff_Name(self):
        return self.__staff_Name
    @staff_Name.setter
    def staff_Name(self, staff_Name: str):
        self.__staff_Name = staff_Name

    @property
    def staff_Address(self):
        return self.__staff_Address
    @staff_Address.setter
    def staff_Address(self, staff_Address: str):
        self.__staff_Address = staff_Address

    @property
    def staff_Date_Of_Joint(self):
        return self.__staff_Date_Of_Joint
    @staff_Date_Of_Joint.setter
    def staff_Date_Of_Joint(self, staff_Date_Of_Joint: date):
        self.__staff_Date_Of_Joint = staff_Date_Of_Joint

    @property
    def attendance2(self):
        return self.__attendance2
    @attendance2.setter
    def attendance2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_staff_member__attendance2", None)
        self.__attendance2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff3"):
                opp_val = getattr(old_value, "staff3", None)
                if opp_val == self:
                    setattr(old_value, "staff3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff3"):
                opp_val = getattr(value, "staff3", None)
                setattr(value, "staff3", self)

    @property
    def salary4(self):
        return self.__salary4
    @salary4.setter
    def salary4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_staff_member__salary4", None)
        self.__salary4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff5"):
                opp_val = getattr(old_value, "staff5", None)
                if opp_val == self:
                    setattr(old_value, "staff5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff5"):
                opp_val = getattr(value, "staff5", None)
                setattr(value, "staff5", self)

    @property
    def staff0(self):
        return self.__staff0
    @staff0.setter
    def staff0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_staff_member__staff0", None)
        self.__staff0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff1"):
                opp_val = getattr(old_value, "staff1", None)
                if opp_val == self:
                    setattr(old_value, "staff1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff1"):
                opp_val = getattr(value, "staff1", None)
                setattr(value, "staff1", self)



class Logout_external:

    pass


class Login_external:

    pass
