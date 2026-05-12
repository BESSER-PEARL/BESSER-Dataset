from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Work_days:

    def __init__(self, _No__of_working_days_: int, Days_Attended: int, daysAttended5: set["DaysAttended"] = None, salary6: set["Salary"] = None):
        self._No__of_working_days_ = _No__of_working_days_
        self.Days_Attended = Days_Attended
        self.daysAttended5 = daysAttended5 if daysAttended5 is not None else set()
        self.salary6 = salary6 if salary6 is not None else set()
        
        pass
    @property
    def Days_Attended(self):
        return self.__Days_Attended
    @Days_Attended.setter
    def Days_Attended(self, Days_Attended: int):
        self.__Days_Attended = Days_Attended

    @property
    def _No__of_working_days_(self):
        return self.___No__of_working_days_
    @_No__of_working_days_.setter
    def _No__of_working_days_(self, _No__of_working_days_: int):
        self.___No__of_working_days_ = _No__of_working_days_

    @property
    def daysAttended5(self):
        return self.__daysAttended5
    @daysAttended5.setter
    def daysAttended5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Work_days__daysAttended5", None)
        self.__daysAttended5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "work_days4"):
                    opp_val = getattr(item, "work_days4", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "work_days4"):
                    opp_val = getattr(item, "work_days4", None)
                    
                    if opp_val is None:
                        setattr(item, "work_days4", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def salary6(self):
        return self.__salary6
    @salary6.setter
    def salary6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Work_days__salary6", None)
        self.__salary6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "work_days7"):
                    opp_val = getattr(item, "work_days7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "work_days7"):
                    opp_val = getattr(item, "work_days7", None)
                    
                    if opp_val is None:
                        setattr(item, "work_days7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Salary:

    def __init__(self, Emp_Id: str, Days_attended: int, Net_Salary: str, Bonus__: str, work_days7: set["Work_days"] = None, employee9: "Employee" = None, employee11: set["Employee"] = None, daysAttended13: "DaysAttended" = None):
        self.Emp_Id = Emp_Id
        self.Days_attended = Days_attended
        self.Net_Salary = Net_Salary
        self.Bonus__ = Bonus__
        self.work_days7 = work_days7 if work_days7 is not None else set()
        self.employee9 = employee9
        self.employee11 = employee11 if employee11 is not None else set()
        self.daysAttended13 = daysAttended13
        
        pass
    @property
    def Net_Salary(self):
        return self.__Net_Salary
    @Net_Salary.setter
    def Net_Salary(self, Net_Salary: str):
        self.__Net_Salary = Net_Salary

    @property
    def Emp_Id(self):
        return self.__Emp_Id
    @Emp_Id.setter
    def Emp_Id(self, Emp_Id: str):
        self.__Emp_Id = Emp_Id

    @property
    def Days_attended(self):
        return self.__Days_attended
    @Days_attended.setter
    def Days_attended(self, Days_attended: int):
        self.__Days_attended = Days_attended

    @property
    def Bonus__(self):
        return self.__Bonus__
    @Bonus__.setter
    def Bonus__(self, Bonus__: str):
        self.__Bonus__ = Bonus__

    @property
    def employee9(self):
        return self.__employee9
    @employee9.setter
    def employee9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Salary__employee9", None)
        self.__employee9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "salary8"):
                opp_val = getattr(old_value, "salary8", None)
                if opp_val == self:
                    setattr(old_value, "salary8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "salary8"):
                opp_val = getattr(value, "salary8", None)
                setattr(value, "salary8", self)

    @property
    def employee11(self):
        return self.__employee11
    @employee11.setter
    def employee11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Salary__employee11", None)
        self.__employee11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "salary10"):
                    opp_val = getattr(item, "salary10", None)
                    
                    if opp_val == self:
                        setattr(item, "salary10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "salary10"):
                    opp_val = getattr(item, "salary10", None)
                    
                    setattr(item, "salary10", self)
                    

    @property
    def work_days7(self):
        return self.__work_days7
    @work_days7.setter
    def work_days7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Salary__work_days7", None)
        self.__work_days7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "salary6"):
                    opp_val = getattr(item, "salary6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "salary6"):
                    opp_val = getattr(item, "salary6", None)
                    
                    if opp_val is None:
                        setattr(item, "salary6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def daysAttended13(self):
        return self.__daysAttended13
    @daysAttended13.setter
    def daysAttended13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Salary__daysAttended13", None)
        self.__daysAttended13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "salary12"):
                opp_val = getattr(old_value, "salary12", None)
                if opp_val == self:
                    setattr(old_value, "salary12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "salary12"):
                opp_val = getattr(value, "salary12", None)
                setattr(value, "salary12", self)



class DaysAttended:

    def __init__(self, Emp_Id: str, Emp_BasicSalary: str, Additional_hours__: str, employee3: "Employee" = None, work_days4: set["Work_days"] = None, salary12: "Salary" = None):
        self.Emp_Id = Emp_Id
        self.Emp_BasicSalary = Emp_BasicSalary
        self.Additional_hours__ = Additional_hours__
        self.employee3 = employee3
        self.work_days4 = work_days4 if work_days4 is not None else set()
        self.salary12 = salary12
        
        pass
    @property
    def Emp_Id(self):
        return self.__Emp_Id
    @Emp_Id.setter
    def Emp_Id(self, Emp_Id: str):
        self.__Emp_Id = Emp_Id

    @property
    def Emp_BasicSalary(self):
        return self.__Emp_BasicSalary
    @Emp_BasicSalary.setter
    def Emp_BasicSalary(self, Emp_BasicSalary: str):
        self.__Emp_BasicSalary = Emp_BasicSalary

    @property
    def Additional_hours__(self):
        return self.__Additional_hours__
    @Additional_hours__.setter
    def Additional_hours__(self, Additional_hours__: str):
        self.__Additional_hours__ = Additional_hours__

    @property
    def work_days4(self):
        return self.__work_days4
    @work_days4.setter
    def work_days4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DaysAttended__work_days4", None)
        self.__work_days4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "daysAttended5"):
                    opp_val = getattr(item, "daysAttended5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "daysAttended5"):
                    opp_val = getattr(item, "daysAttended5", None)
                    
                    if opp_val is None:
                        setattr(item, "daysAttended5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def employee3(self):
        return self.__employee3
    @employee3.setter
    def employee3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DaysAttended__employee3", None)
        self.__employee3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "daysAttended2"):
                opp_val = getattr(old_value, "daysAttended2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "daysAttended2"):
                opp_val = getattr(value, "daysAttended2", None)
                if opp_val is None:
                    setattr(value, "daysAttended2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def salary12(self):
        return self.__salary12
    @salary12.setter
    def salary12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DaysAttended__salary12", None)
        self.__salary12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "daysAttended13"):
                opp_val = getattr(old_value, "daysAttended13", None)
                if opp_val == self:
                    setattr(old_value, "daysAttended13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "daysAttended13"):
                opp_val = getattr(value, "daysAttended13", None)
                setattr(value, "daysAttended13", self)



class Employee:

    def __init__(self, Emp_Id: str, Emp_Name: str, Emp_FName: str, login1: "Login" = None, daysAttended2: set["DaysAttended"] = None, salary8: "Salary" = None, salary10: "Salary" = None):
        self.Emp_Id = Emp_Id
        self.Emp_Name = Emp_Name
        self.Emp_FName = Emp_FName
        self.login1 = login1
        self.daysAttended2 = daysAttended2 if daysAttended2 is not None else set()
        self.salary8 = salary8
        self.salary10 = salary10
        
        pass
    @property
    def Emp_Name(self):
        return self.__Emp_Name
    @Emp_Name.setter
    def Emp_Name(self, Emp_Name: str):
        self.__Emp_Name = Emp_Name

    @property
    def Emp_FName(self):
        return self.__Emp_FName
    @Emp_FName.setter
    def Emp_FName(self, Emp_FName: str):
        self.__Emp_FName = Emp_FName

    @property
    def Emp_Id(self):
        return self.__Emp_Id
    @Emp_Id.setter
    def Emp_Id(self, Emp_Id: str):
        self.__Emp_Id = Emp_Id

    @property
    def salary10(self):
        return self.__salary10
    @salary10.setter
    def salary10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__salary10", None)
        self.__salary10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee11"):
                opp_val = getattr(old_value, "employee11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee11"):
                opp_val = getattr(value, "employee11", None)
                if opp_val is None:
                    setattr(value, "employee11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def daysAttended2(self):
        return self.__daysAttended2
    @daysAttended2.setter
    def daysAttended2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__daysAttended2", None)
        self.__daysAttended2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee3"):
                    opp_val = getattr(item, "employee3", None)
                    
                    if opp_val == self:
                        setattr(item, "employee3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee3"):
                    opp_val = getattr(item, "employee3", None)
                    
                    setattr(item, "employee3", self)
                    

    @property
    def salary8(self):
        return self.__salary8
    @salary8.setter
    def salary8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__salary8", None)
        self.__salary8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee9"):
                opp_val = getattr(old_value, "employee9", None)
                if opp_val == self:
                    setattr(old_value, "employee9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee9"):
                opp_val = getattr(value, "employee9", None)
                setattr(value, "employee9", self)

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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee0"):
                opp_val = getattr(value, "employee0", None)
                if opp_val is None:
                    setattr(value, "employee0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Login:

    def __init__(self, User_Name: str, Password: str, employee0: set["Employee"] = None):
        self.User_Name = User_Name
        self.Password = Password
        self.employee0 = employee0 if employee0 is not None else set()
        
        pass
    @property
    def User_Name(self):
        return self.__User_Name
    @User_Name.setter
    def User_Name(self, User_Name: str):
        self.__User_Name = User_Name

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
        self.__employee0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "login1"):
                    opp_val = getattr(item, "login1", None)
                    
                    if opp_val == self:
                        setattr(item, "login1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "login1"):
                    opp_val = getattr(item, "login1", None)
                    
                    setattr(item, "login1", self)
                    

