from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Admin:

    def __init__(self, Name: str, Email: str, employee8: set["Employee"] = None):
        self.Name = Name
        self.Email = Email
        self.employee8 = employee8 if employee8 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

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
                if hasattr(item, "admin9"):
                    opp_val = getattr(item, "admin9", None)
                    
                    if opp_val == self:
                        setattr(item, "admin9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "admin9"):
                    opp_val = getattr(item, "admin9", None)
                    
                    setattr(item, "admin9", self)
                    



class Leave:

    def __init__(self, Leave_Detail: str, Leave_NoOfDays: int, attribute: str, employee7: "Employee" = None):
        self.Leave_Detail = Leave_Detail
        self.Leave_NoOfDays = Leave_NoOfDays
        self.attribute = attribute
        self.employee7 = employee7
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def Leave_Detail(self):
        return self.__Leave_Detail
    @Leave_Detail.setter
    def Leave_Detail(self, Leave_Detail: str):
        self.__Leave_Detail = Leave_Detail

    @property
    def Leave_NoOfDays(self):
        return self.__Leave_NoOfDays
    @Leave_NoOfDays.setter
    def Leave_NoOfDays(self, Leave_NoOfDays: int):
        self.__Leave_NoOfDays = Leave_NoOfDays

    @property
    def employee7(self):
        return self.__employee7
    @employee7.setter
    def employee7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Leave__employee7", None)
        self.__employee7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leave6"):
                opp_val = getattr(old_value, "leave6", None)
                if opp_val == self:
                    setattr(old_value, "leave6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leave6"):
                opp_val = getattr(value, "leave6", None)
                setattr(value, "leave6", self)



class Days_Attended:

    def __init__(self, EmployeeId: str, EmployeeBasicSalary: int, OverTime: int, Total_no__of_workingdays: int, Days_attended: int, employee5: "Employee" = None, salary11: "Salary" = None):
        self.EmployeeId = EmployeeId
        self.EmployeeBasicSalary = EmployeeBasicSalary
        self.OverTime = OverTime
        self.Total_no__of_workingdays = Total_no__of_workingdays
        self.Days_attended = Days_attended
        self.employee5 = employee5
        self.salary11 = salary11
        
        pass
    @property
    def Days_attended(self):
        return self.__Days_attended
    @Days_attended.setter
    def Days_attended(self, Days_attended: int):
        self.__Days_attended = Days_attended

    @property
    def EmployeeId(self):
        return self.__EmployeeId
    @EmployeeId.setter
    def EmployeeId(self, EmployeeId: str):
        self.__EmployeeId = EmployeeId

    @property
    def EmployeeBasicSalary(self):
        return self.__EmployeeBasicSalary
    @EmployeeBasicSalary.setter
    def EmployeeBasicSalary(self, EmployeeBasicSalary: int):
        self.__EmployeeBasicSalary = EmployeeBasicSalary

    @property
    def Total_no__of_workingdays(self):
        return self.__Total_no__of_workingdays
    @Total_no__of_workingdays.setter
    def Total_no__of_workingdays(self, Total_no__of_workingdays: int):
        self.__Total_no__of_workingdays = Total_no__of_workingdays

    @property
    def OverTime(self):
        return self.__OverTime
    @OverTime.setter
    def OverTime(self, OverTime: int):
        self.__OverTime = OverTime

    @property
    def salary11(self):
        return self.__salary11
    @salary11.setter
    def salary11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Days_Attended__salary11", None)
        self.__salary11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "days_Attended10"):
                opp_val = getattr(old_value, "days_Attended10", None)
                if opp_val == self:
                    setattr(old_value, "days_Attended10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "days_Attended10"):
                opp_val = getattr(value, "days_Attended10", None)
                setattr(value, "days_Attended10", self)

    @property
    def employee5(self):
        return self.__employee5
    @employee5.setter
    def employee5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Days_Attended__employee5", None)
        self.__employee5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "days_Attended4"):
                opp_val = getattr(old_value, "days_Attended4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "days_Attended4"):
                opp_val = getattr(value, "days_Attended4", None)
                if opp_val is None:
                    setattr(value, "days_Attended4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Salary:

    def __init__(self, EmployeeID: str, DaysAttended: int, Bonus: int, NetSalary: int, employee3: "Employee" = None, days_Attended10: "Days_Attended" = None):
        self.EmployeeID = EmployeeID
        self.DaysAttended = DaysAttended
        self.Bonus = Bonus
        self.NetSalary = NetSalary
        self.employee3 = employee3
        self.days_Attended10 = days_Attended10
        
        pass
    @property
    def NetSalary(self):
        return self.__NetSalary
    @NetSalary.setter
    def NetSalary(self, NetSalary: int):
        self.__NetSalary = NetSalary

    @property
    def EmployeeID(self):
        return self.__EmployeeID
    @EmployeeID.setter
    def EmployeeID(self, EmployeeID: str):
        self.__EmployeeID = EmployeeID

    @property
    def Bonus(self):
        return self.__Bonus
    @Bonus.setter
    def Bonus(self, Bonus: int):
        self.__Bonus = Bonus

    @property
    def DaysAttended(self):
        return self.__DaysAttended
    @DaysAttended.setter
    def DaysAttended(self, DaysAttended: int):
        self.__DaysAttended = DaysAttended

    @property
    def employee3(self):
        return self.__employee3
    @employee3.setter
    def employee3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Salary__employee3", None)
        self.__employee3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "salary2"):
                opp_val = getattr(old_value, "salary2", None)
                if opp_val == self:
                    setattr(old_value, "salary2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "salary2"):
                opp_val = getattr(value, "salary2", None)
                setattr(value, "salary2", self)

    @property
    def days_Attended10(self):
        return self.__days_Attended10
    @days_Attended10.setter
    def days_Attended10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Salary__days_Attended10", None)
        self.__days_Attended10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "salary11"):
                opp_val = getattr(old_value, "salary11", None)
                if opp_val == self:
                    setattr(old_value, "salary11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "salary11"):
                opp_val = getattr(value, "salary11", None)
                setattr(value, "salary11", self)



class Employee:

    def __init__(self, EmployeeId: str, EmplyeeName: str, EmployeePhoneNumber: int, EmployeeEmail: str, login1: "Login" = None, salary2: "Salary" = None, days_Attended4: set["Days_Attended"] = None, leave6: "Leave" = None, admin9: "Admin" = None):
        self.EmployeeId = EmployeeId
        self.EmplyeeName = EmplyeeName
        self.EmployeePhoneNumber = EmployeePhoneNumber
        self.EmployeeEmail = EmployeeEmail
        self.login1 = login1
        self.salary2 = salary2
        self.days_Attended4 = days_Attended4 if days_Attended4 is not None else set()
        self.leave6 = leave6
        self.admin9 = admin9
        
        pass
    @property
    def EmployeePhoneNumber(self):
        return self.__EmployeePhoneNumber
    @EmployeePhoneNumber.setter
    def EmployeePhoneNumber(self, EmployeePhoneNumber: int):
        self.__EmployeePhoneNumber = EmployeePhoneNumber

    @property
    def EmplyeeName(self):
        return self.__EmplyeeName
    @EmplyeeName.setter
    def EmplyeeName(self, EmplyeeName: str):
        self.__EmplyeeName = EmplyeeName

    @property
    def EmployeeEmail(self):
        return self.__EmployeeEmail
    @EmployeeEmail.setter
    def EmployeeEmail(self, EmployeeEmail: str):
        self.__EmployeeEmail = EmployeeEmail

    @property
    def EmployeeId(self):
        return self.__EmployeeId
    @EmployeeId.setter
    def EmployeeId(self, EmployeeId: str):
        self.__EmployeeId = EmployeeId

    @property
    def salary2(self):
        return self.__salary2
    @salary2.setter
    def salary2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__salary2", None)
        self.__salary2 = value
        
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

    @property
    def leave6(self):
        return self.__leave6
    @leave6.setter
    def leave6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__leave6", None)
        self.__leave6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee7"):
                opp_val = getattr(old_value, "employee7", None)
                if opp_val == self:
                    setattr(old_value, "employee7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee7"):
                opp_val = getattr(value, "employee7", None)
                setattr(value, "employee7", self)

    @property
    def admin9(self):
        return self.__admin9
    @admin9.setter
    def admin9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__admin9", None)
        self.__admin9 = value
        
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
    def days_Attended4(self):
        return self.__days_Attended4
    @days_Attended4.setter
    def days_Attended4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__days_Attended4", None)
        self.__days_Attended4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee5"):
                    opp_val = getattr(item, "employee5", None)
                    
                    if opp_val == self:
                        setattr(item, "employee5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee5"):
                    opp_val = getattr(item, "employee5", None)
                    
                    setattr(item, "employee5", self)
                    

    @property
    def login1(self):
        return self.__login1
    @login1.setter
    def login1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__login1", None)
        self.__login1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee0"):
                opp_val = getattr(old_value, "employee0", None)
                if opp_val == self:
                    setattr(old_value, "employee0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee0"):
                opp_val = getattr(value, "employee0", None)
                setattr(value, "employee0", self)



class Login:

    def __init__(self, Username: str, Password: str, employee0: "Employee" = None):
        self.Username = Username
        self.Password = Password
        self.employee0 = employee0
        
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
    def employee0(self):
        return self.__employee0
    @employee0.setter
    def employee0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__employee0", None)
        self.__employee0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login1"):
                opp_val = getattr(old_value, "login1", None)
                if opp_val == self:
                    setattr(old_value, "login1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login1"):
                opp_val = getattr(value, "login1", None)
                setattr(value, "login1", self)

