from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Employee_Actor:

    pass


class Administrator_Actor:

    pass


class Authentication_UseCase:

    pass





class Logout_external:

    pass


class Login_external:

    pass


class Admin:

    def __init__(self, UserName: str, Password: str, UserType: str, employee11: "Employee" = None):
        self.UserName = UserName
        self.Password = Password
        self.UserType = UserType
        self.employee11 = employee11
        
        pass
    @property
    def UserType(self):
        return self.__UserType
    @UserType.setter
    def UserType(self, UserType: str):
        self.__UserType = UserType

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
    def employee11(self):
        return self.__employee11
    @employee11.setter
    def employee11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__employee11", None)
        self.__employee11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin10"):
                opp_val = getattr(old_value, "admin10", None)
                if opp_val == self:
                    setattr(old_value, "admin10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin10"):
                opp_val = getattr(value, "admin10", None)
                setattr(value, "admin10", self)



class FingerprintReader:

    def __init__(self, X_cord: float, Y__Cord: float, Angle: float, MiniType: FingerprintReader, miniType: int, Emp_Id: int, attendance8: "Attendance" = None):
        self.X_cord = X_cord
        self.Y__Cord = Y__Cord
        self.Angle = Angle
        self.MiniType = MiniType
        self.miniType = miniType
        self.Emp_Id = Emp_Id
        self.attendance8 = attendance8
        
        pass
    @property
    def Emp_Id(self):
        return self.__Emp_Id
    @Emp_Id.setter
    def Emp_Id(self, Emp_Id: int):
        self.__Emp_Id = Emp_Id

    @property
    def Angle(self):
        return self.__Angle
    @Angle.setter
    def Angle(self, Angle: float):
        self.__Angle = Angle

    @property
    def MiniType(self):
        return self.__MiniType
    @MiniType.setter
    def MiniType(self, MiniType: FingerprintReader):
        self.__MiniType = MiniType

    @property
    def Y__Cord(self):
        return self.__Y__Cord
    @Y__Cord.setter
    def Y__Cord(self, Y__Cord: float):
        self.__Y__Cord = Y__Cord

    @property
    def X_cord(self):
        return self.__X_cord
    @X_cord.setter
    def X_cord(self, X_cord: float):
        self.__X_cord = X_cord

    @property
    def miniType(self):
        return self.__miniType
    @miniType.setter
    def miniType(self, miniType: int):
        self.__miniType = miniType

    @property
    def attendance8(self):
        return self.__attendance8
    @attendance8.setter
    def attendance8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FingerprintReader__attendance8", None)
        self.__attendance8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fingerprintReader9"):
                opp_val = getattr(old_value, "fingerprintReader9", None)
                if opp_val == self:
                    setattr(old_value, "fingerprintReader9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fingerprintReader9"):
                opp_val = getattr(value, "fingerprintReader9", None)
                setattr(value, "fingerprintReader9", self)



class Employee_Management_System_Component:

    pass


class Login:

    def __init__(self, UserName: str, Password: str, Password1: str):
        self.UserName = UserName
        self.Password = Password
        self.Password1 = Password1
        
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
    def Password1(self):
        return self.__Password1
    @Password1.setter
    def Password1(self, Password1: str):
        self.__Password1 = Password1



class Attendance:

    def __init__(self, Leaving_Time: str, Attend_date: date, Emp_id: str, AttendTime: str, employee3: "Employee" = None, fingerprintReader9: "FingerprintReader" = None):
        self.Leaving_Time = Leaving_Time
        self.Attend_date = Attend_date
        self.Emp_id = Emp_id
        self.AttendTime = AttendTime
        self.employee3 = employee3
        self.fingerprintReader9 = fingerprintReader9
        
        pass
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

    @property
    def fingerprintReader9(self):
        return self.__fingerprintReader9
    @fingerprintReader9.setter
    def fingerprintReader9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Attendance__fingerprintReader9", None)
        self.__fingerprintReader9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attendance8"):
                opp_val = getattr(old_value, "attendance8", None)
                if opp_val == self:
                    setattr(old_value, "attendance8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attendance8"):
                opp_val = getattr(value, "attendance8", None)
                setattr(value, "attendance8", self)



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
    def Emp_Id(self):
        return self.__Emp_Id
    @Emp_Id.setter
    def Emp_Id(self, Emp_Id: int):
        self.__Emp_Id = Emp_Id

    @property
    def Leave_ApplyDate(self):
        return self.__Leave_ApplyDate
    @Leave_ApplyDate.setter
    def Leave_ApplyDate(self, Leave_ApplyDate: date):
        self.__Leave_ApplyDate = Leave_ApplyDate

    @property
    def leave_id(self):
        return self.__leave_id
    @leave_id.setter
    def leave_id(self, leave_id: int):
        self.__leave_id = leave_id

    @property
    def Leave_Title(self):
        return self.__Leave_Title
    @Leave_Title.setter
    def Leave_Title(self, Leave_Title: str):
        self.__Leave_Title = Leave_Title

    @property
    def Leave_detail(self):
        return self.__Leave_detail
    @Leave_detail.setter
    def Leave_detail(self, Leave_detail: str):
        self.__Leave_detail = Leave_detail

    @property
    def Leave_StartDate(self):
        return self.__Leave_StartDate
    @Leave_StartDate.setter
    def Leave_StartDate(self, Leave_StartDate: date):
        self.__Leave_StartDate = Leave_StartDate

    @property
    def Leave_NoOfDays(self):
        return self.__Leave_NoOfDays
    @Leave_NoOfDays.setter
    def Leave_NoOfDays(self, Leave_NoOfDays: int):
        self.__Leave_NoOfDays = Leave_NoOfDays

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



class Employee:

    def __init__(self, Emp_Id: int, Emp_Name: str, Emp_ContactNo: str, Emp_Email: str, Emp_NIC: str, Emp_Address: str, Emp_DOB: date, Emp_Department: str, Emp_Date_Of_Joint: date, Emp_Position: str, leave0: "Leave" = None, attendance2: "Attendance" = None, admin10: "Admin" = None):
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
        self.leave0 = leave0
        self.attendance2 = attendance2
        self.admin10 = admin10
        
        pass
    @property
    def Emp_Email(self):
        return self.__Emp_Email
    @Emp_Email.setter
    def Emp_Email(self, Emp_Email: str):
        self.__Emp_Email = Emp_Email

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
    def Emp_NIC(self):
        return self.__Emp_NIC
    @Emp_NIC.setter
    def Emp_NIC(self, Emp_NIC: str):
        self.__Emp_NIC = Emp_NIC

    @property
    def Emp_Date_Of_Joint(self):
        return self.__Emp_Date_Of_Joint
    @Emp_Date_Of_Joint.setter
    def Emp_Date_Of_Joint(self, Emp_Date_Of_Joint: date):
        self.__Emp_Date_Of_Joint = Emp_Date_Of_Joint

    @property
    def Emp_Department(self):
        return self.__Emp_Department
    @Emp_Department.setter
    def Emp_Department(self, Emp_Department: str):
        self.__Emp_Department = Emp_Department

    @property
    def Emp_Address(self):
        return self.__Emp_Address
    @Emp_Address.setter
    def Emp_Address(self, Emp_Address: str):
        self.__Emp_Address = Emp_Address

    @property
    def Emp_Position(self):
        return self.__Emp_Position
    @Emp_Position.setter
    def Emp_Position(self, Emp_Position: str):
        self.__Emp_Position = Emp_Position

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
    def admin10(self):
        return self.__admin10
    @admin10.setter
    def admin10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__admin10", None)
        self.__admin10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee11"):
                opp_val = getattr(old_value, "employee11", None)
                if opp_val == self:
                    setattr(old_value, "employee11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee11"):
                opp_val = getattr(value, "employee11", None)
                setattr(value, "employee11", self)

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

