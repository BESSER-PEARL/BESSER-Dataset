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


class Tuning_Staff:

    def __init__(self, UserName: str, Address: str, Authendication_Mood: str, staff23: "Staff" = None):
        self.UserName = UserName
        self.Address = Address
        self.Authendication_Mood = Authendication_Mood
        self.staff23 = staff23
        
        pass
    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Authendication_Mood(self):
        return self.__Authendication_Mood
    @Authendication_Mood.setter
    def Authendication_Mood(self, Authendication_Mood: str):
        self.__Authendication_Mood = Authendication_Mood

    @property
    def staff23(self):
        return self.__staff23
    @staff23.setter
    def staff23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tuning_Staff__staff23", None)
        self.__staff23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tuning_Staff22"):
                opp_val = getattr(old_value, "tuning_Staff22", None)
                if opp_val == self:
                    setattr(old_value, "tuning_Staff22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tuning_Staff22"):
                opp_val = getattr(value, "tuning_Staff22", None)
                setattr(value, "tuning_Staff22", self)



class Driving_Staff:

    def __init__(self, PilotName: str, Password: str, Authendication_Mood: str, Pilot_ContactNo: str, staff21: "Staff" = None):
        self.PilotName = PilotName
        self.Password = Password
        self.Authendication_Mood = Authendication_Mood
        self.Pilot_ContactNo = Pilot_ContactNo
        self.staff21 = staff21
        
        pass
    @property
    def Pilot_ContactNo(self):
        return self.__Pilot_ContactNo
    @Pilot_ContactNo.setter
    def Pilot_ContactNo(self, Pilot_ContactNo: str):
        self.__Pilot_ContactNo = Pilot_ContactNo

    @property
    def Authendication_Mood(self):
        return self.__Authendication_Mood
    @Authendication_Mood.setter
    def Authendication_Mood(self, Authendication_Mood: str):
        self.__Authendication_Mood = Authendication_Mood

    @property
    def PilotName(self):
        return self.__PilotName
    @PilotName.setter
    def PilotName(self, PilotName: str):
        self.__PilotName = PilotName

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def staff21(self):
        return self.__staff21
    @staff21.setter
    def staff21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Driving_Staff__staff21", None)
        self.__staff21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driving_Staff20"):
                opp_val = getattr(old_value, "driving_Staff20", None)
                if opp_val == self:
                    setattr(old_value, "driving_Staff20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driving_Staff20"):
                opp_val = getattr(value, "driving_Staff20", None)
                setattr(value, "driving_Staff20", self)



class Administrator:

    def __init__(self, Admin_Id: int, Admin_Name: str, Admin_ContactNo: str, Admin_Email: str, Admin_NIC: str, Emp_DOB: date, Emp_Department: str, Emp_Date_Of_Joint: date, Emp_Position: str, manager12: "Manager" = None, login15: "Login" = None, login16: "Login" = None):
        self.Admin_Id = Admin_Id
        self.Admin_Name = Admin_Name
        self.Admin_ContactNo = Admin_ContactNo
        self.Admin_Email = Admin_Email
        self.Admin_NIC = Admin_NIC
        self.Emp_DOB = Emp_DOB
        self.Emp_Department = Emp_Department
        self.Emp_Date_Of_Joint = Emp_Date_Of_Joint
        self.Emp_Position = Emp_Position
        self.manager12 = manager12
        self.login15 = login15
        self.login16 = login16
        
        pass
    @property
    def Admin_ContactNo(self):
        return self.__Admin_ContactNo
    @Admin_ContactNo.setter
    def Admin_ContactNo(self, Admin_ContactNo: str):
        self.__Admin_ContactNo = Admin_ContactNo

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
    def Emp_Department(self):
        return self.__Emp_Department
    @Emp_Department.setter
    def Emp_Department(self, Emp_Department: str):
        self.__Emp_Department = Emp_Department

    @property
    def Emp_Date_Of_Joint(self):
        return self.__Emp_Date_Of_Joint
    @Emp_Date_Of_Joint.setter
    def Emp_Date_Of_Joint(self, Emp_Date_Of_Joint: date):
        self.__Emp_Date_Of_Joint = Emp_Date_Of_Joint

    @property
    def Admin_Email(self):
        return self.__Admin_Email
    @Admin_Email.setter
    def Admin_Email(self, Admin_Email: str):
        self.__Admin_Email = Admin_Email

    @property
    def Admin_Id(self):
        return self.__Admin_Id
    @Admin_Id.setter
    def Admin_Id(self, Admin_Id: int):
        self.__Admin_Id = Admin_Id

    @property
    def Admin_Name(self):
        return self.__Admin_Name
    @Admin_Name.setter
    def Admin_Name(self, Admin_Name: str):
        self.__Admin_Name = Admin_Name

    @property
    def Admin_NIC(self):
        return self.__Admin_NIC
    @Admin_NIC.setter
    def Admin_NIC(self, Admin_NIC: str):
        self.__Admin_NIC = Admin_NIC

    @property
    def manager12(self):
        return self.__manager12
    @manager12.setter
    def manager12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__manager12", None)
        self.__manager12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrator13"):
                opp_val = getattr(old_value, "administrator13", None)
                if opp_val == self:
                    setattr(old_value, "administrator13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrator13"):
                opp_val = getattr(value, "administrator13", None)
                setattr(value, "administrator13", self)

    @property
    def login15(self):
        return self.__login15
    @login15.setter
    def login15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__login15", None)
        self.__login15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrator14"):
                opp_val = getattr(old_value, "administrator14", None)
                if opp_val == self:
                    setattr(old_value, "administrator14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrator14"):
                opp_val = getattr(value, "administrator14", None)
                setattr(value, "administrator14", self)

    @property
    def login16(self):
        return self.__login16
    @login16.setter
    def login16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__login16", None)
        self.__login16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrator17"):
                opp_val = getattr(old_value, "administrator17", None)
                if opp_val == self:
                    setattr(old_value, "administrator17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrator17"):
                opp_val = getattr(value, "administrator17", None)
                setattr(value, "administrator17", self)



class Employee_Management_System_Component:

    pass


class Login:

    def __init__(self, UserName: str, Password: str, administrator14: "Administrator" = None, administrator17: "Administrator" = None, manager18: "Manager" = None):
        self.UserName = UserName
        self.Password = Password
        self.administrator14 = administrator14
        self.administrator17 = administrator17
        self.manager18 = manager18
        
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
    def manager18(self):
        return self.__manager18
    @manager18.setter
    def manager18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__manager18", None)
        self.__manager18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login19"):
                opp_val = getattr(old_value, "login19", None)
                if opp_val == self:
                    setattr(old_value, "login19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login19"):
                opp_val = getattr(value, "login19", None)
                setattr(value, "login19", self)

    @property
    def administrator14(self):
        return self.__administrator14
    @administrator14.setter
    def administrator14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__administrator14", None)
        self.__administrator14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login15"):
                opp_val = getattr(old_value, "login15", None)
                if opp_val == self:
                    setattr(old_value, "login15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login15"):
                opp_val = getattr(value, "login15", None)
                setattr(value, "login15", self)

    @property
    def administrator17(self):
        return self.__administrator17
    @administrator17.setter
    def administrator17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__administrator17", None)
        self.__administrator17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login16"):
                opp_val = getattr(old_value, "login16", None)
                if opp_val == self:
                    setattr(old_value, "login16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login16"):
                opp_val = getattr(value, "login16", None)
                setattr(value, "login16", self)



class Attendance:

    def __init__(self, Emp_id: str, AttendTime: str, Leaving_Time: str, Attend_date: date, employee3: "Manager" = None):
        self.Emp_id = Emp_id
        self.AttendTime = AttendTime
        self.Leaving_Time = Leaving_Time
        self.Attend_date = Attend_date
        self.employee3 = employee3
        
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



class Leave_Status:

    def __init__(self, leave_id: int, Emp_Id: int, Leave_Title: str, Leave_detail: str, Leave_ApplyDate: date, Leave_StartDate: date, Leave_EndDate: date, Leave_NoOfDays: int, Leave_Status: str, staff11: "Staff" = None, employee1: "Manager" = None):
        self.leave_id = leave_id
        self.Emp_Id = Emp_Id
        self.Leave_Title = Leave_Title
        self.Leave_detail = Leave_detail
        self.Leave_ApplyDate = Leave_ApplyDate
        self.Leave_StartDate = Leave_StartDate
        self.Leave_EndDate = Leave_EndDate
        self.Leave_NoOfDays = Leave_NoOfDays
        self.Leave_Status = Leave_Status
        self.staff11 = staff11
        self.employee1 = employee1
        
        pass
    @property
    def Leave_detail(self):
        return self.__Leave_detail
    @Leave_detail.setter
    def Leave_detail(self, Leave_detail: str):
        self.__Leave_detail = Leave_detail

    @property
    def Leave_Title(self):
        return self.__Leave_Title
    @Leave_Title.setter
    def Leave_Title(self, Leave_Title: str):
        self.__Leave_Title = Leave_Title

    @property
    def Emp_Id(self):
        return self.__Emp_Id
    @Emp_Id.setter
    def Emp_Id(self, Emp_Id: int):
        self.__Emp_Id = Emp_Id

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
    def Leave_NoOfDays(self):
        return self.__Leave_NoOfDays
    @Leave_NoOfDays.setter
    def Leave_NoOfDays(self, Leave_NoOfDays: int):
        self.__Leave_NoOfDays = Leave_NoOfDays

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
    def employee1(self):
        return self.__employee1
    @employee1.setter
    def employee1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Leave_Status__employee1", None)
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

    @property
    def staff11(self):
        return self.__staff11
    @staff11.setter
    def staff11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Leave_Status__staff11", None)
        self.__staff11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leave_Status10"):
                opp_val = getattr(old_value, "leave_Status10", None)
                if opp_val == self:
                    setattr(old_value, "leave_Status10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leave_Status10"):
                opp_val = getattr(value, "leave_Status10", None)
                setattr(value, "leave_Status10", self)



class Staff:

    def __init__(self, UserName: str, Password: str, Authendication_Mood: str, leave_Status10: "Leave_Status" = None, driving_Staff20: "Driving_Staff" = None, tuning_Staff22: "Tuning_Staff" = None):
        self.UserName = UserName
        self.Password = Password
        self.Authendication_Mood = Authendication_Mood
        self.leave_Status10 = leave_Status10
        self.driving_Staff20 = driving_Staff20
        self.tuning_Staff22 = tuning_Staff22
        
        pass
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

    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

    @property
    def leave_Status10(self):
        return self.__leave_Status10
    @leave_Status10.setter
    def leave_Status10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__leave_Status10", None)
        self.__leave_Status10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff11"):
                opp_val = getattr(old_value, "staff11", None)
                if opp_val == self:
                    setattr(old_value, "staff11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff11"):
                opp_val = getattr(value, "staff11", None)
                setattr(value, "staff11", self)

    @property
    def driving_Staff20(self):
        return self.__driving_Staff20
    @driving_Staff20.setter
    def driving_Staff20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__driving_Staff20", None)
        self.__driving_Staff20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff21"):
                opp_val = getattr(old_value, "staff21", None)
                if opp_val == self:
                    setattr(old_value, "staff21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff21"):
                opp_val = getattr(value, "staff21", None)
                setattr(value, "staff21", self)

    @property
    def tuning_Staff22(self):
        return self.__tuning_Staff22
    @tuning_Staff22.setter
    def tuning_Staff22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__tuning_Staff22", None)
        self.__tuning_Staff22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff23"):
                opp_val = getattr(old_value, "staff23", None)
                if opp_val == self:
                    setattr(old_value, "staff23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff23"):
                opp_val = getattr(value, "staff23", None)
                setattr(value, "staff23", self)



class Salary:

    def __init__(self, Emp_Id: int, Sly_Basic: float, Sly_Increment: float, Sly_Decrement: float, Sly_Netgross: float, OverTime: str, employee5: "Manager" = None):
        self.Emp_Id = Emp_Id
        self.Sly_Basic = Sly_Basic
        self.Sly_Increment = Sly_Increment
        self.Sly_Decrement = Sly_Decrement
        self.Sly_Netgross = Sly_Netgross
        self.OverTime = OverTime
        self.employee5 = employee5
        
        pass
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
    def Sly_Increment(self):
        return self.__Sly_Increment
    @Sly_Increment.setter
    def Sly_Increment(self, Sly_Increment: float):
        self.__Sly_Increment = Sly_Increment

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
    def Sly_Netgross(self):
        return self.__Sly_Netgross
    @Sly_Netgross.setter
    def Sly_Netgross(self, Sly_Netgross: float):
        self.__Sly_Netgross = Sly_Netgross

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



class Manager:

    def __init__(self, Mng_Id: int, Mng_Name: str, Mng_ContactNo: str, Mng_Email: str, Emp_NIC: str, Emp_Address: str, Emp_DOB: date, Emp_Department: str, Emp_Date_Of_Joint: date, Emp_Position: str, Mng_Salary: float, salary4: "Salary" = None, administrator13: "Administrator" = None, login19: "Login" = None, leave0: "Leave_Status" = None, attendance2: "Attendance" = None):
        self.Mng_Id = Mng_Id
        self.Mng_Name = Mng_Name
        self.Mng_ContactNo = Mng_ContactNo
        self.Mng_Email = Mng_Email
        self.Emp_NIC = Emp_NIC
        self.Emp_Address = Emp_Address
        self.Emp_DOB = Emp_DOB
        self.Emp_Department = Emp_Department
        self.Emp_Date_Of_Joint = Emp_Date_Of_Joint
        self.Emp_Position = Emp_Position
        self.Mng_Salary = Mng_Salary
        self.salary4 = salary4
        self.administrator13 = administrator13
        self.login19 = login19
        self.leave0 = leave0
        self.attendance2 = attendance2
        
        pass
    @property
    def Mng_Salary(self):
        return self.__Mng_Salary
    @Mng_Salary.setter
    def Mng_Salary(self, Mng_Salary: float):
        self.__Mng_Salary = Mng_Salary

    @property
    def Emp_Date_Of_Joint(self):
        return self.__Emp_Date_Of_Joint
    @Emp_Date_Of_Joint.setter
    def Emp_Date_Of_Joint(self, Emp_Date_Of_Joint: date):
        self.__Emp_Date_Of_Joint = Emp_Date_Of_Joint

    @property
    def Emp_DOB(self):
        return self.__Emp_DOB
    @Emp_DOB.setter
    def Emp_DOB(self, Emp_DOB: date):
        self.__Emp_DOB = Emp_DOB

    @property
    def Mng_Email(self):
        return self.__Mng_Email
    @Mng_Email.setter
    def Mng_Email(self, Mng_Email: str):
        self.__Mng_Email = Mng_Email

    @property
    def Emp_Department(self):
        return self.__Emp_Department
    @Emp_Department.setter
    def Emp_Department(self, Emp_Department: str):
        self.__Emp_Department = Emp_Department

    @property
    def Mng_Id(self):
        return self.__Mng_Id
    @Mng_Id.setter
    def Mng_Id(self, Mng_Id: int):
        self.__Mng_Id = Mng_Id

    @property
    def Emp_Address(self):
        return self.__Emp_Address
    @Emp_Address.setter
    def Emp_Address(self, Emp_Address: str):
        self.__Emp_Address = Emp_Address

    @property
    def Mng_ContactNo(self):
        return self.__Mng_ContactNo
    @Mng_ContactNo.setter
    def Mng_ContactNo(self, Mng_ContactNo: str):
        self.__Mng_ContactNo = Mng_ContactNo

    @property
    def Mng_Name(self):
        return self.__Mng_Name
    @Mng_Name.setter
    def Mng_Name(self, Mng_Name: str):
        self.__Mng_Name = Mng_Name

    @property
    def Emp_Position(self):
        return self.__Emp_Position
    @Emp_Position.setter
    def Emp_Position(self, Emp_Position: str):
        self.__Emp_Position = Emp_Position

    @property
    def Emp_NIC(self):
        return self.__Emp_NIC
    @Emp_NIC.setter
    def Emp_NIC(self, Emp_NIC: str):
        self.__Emp_NIC = Emp_NIC

    @property
    def administrator13(self):
        return self.__administrator13
    @administrator13.setter
    def administrator13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager__administrator13", None)
        self.__administrator13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manager12"):
                opp_val = getattr(old_value, "manager12", None)
                if opp_val == self:
                    setattr(old_value, "manager12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manager12"):
                opp_val = getattr(value, "manager12", None)
                setattr(value, "manager12", self)

    @property
    def leave0(self):
        return self.__leave0
    @leave0.setter
    def leave0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager__leave0", None)
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
    def login19(self):
        return self.__login19
    @login19.setter
    def login19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager__login19", None)
        self.__login19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manager18"):
                opp_val = getattr(old_value, "manager18", None)
                if opp_val == self:
                    setattr(old_value, "manager18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manager18"):
                opp_val = getattr(value, "manager18", None)
                setattr(value, "manager18", self)

    @property
    def salary4(self):
        return self.__salary4
    @salary4.setter
    def salary4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager__salary4", None)
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
    def attendance2(self):
        return self.__attendance2
    @attendance2.setter
    def attendance2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager__attendance2", None)
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

