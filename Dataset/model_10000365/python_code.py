from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Print_UseCase:

    pass


class Edit__Archive_UseCase:

    pass


class Reporting_UseCase:

    pass


class Managing_Users_UseCase:

    pass


class Administrator_Actor:

    pass


class Notes___Comments_UseCase:

    pass


class Log_Out_UseCase:

    pass


class Log_In_UseCase:

    pass


class Employee_Actor:

    pass





class Employee_DB:

    def __init__(self, Name__1st_and_last_: Employee_Actor, Username: Log_In_UseCase, Password: str, Employee_ID: int, Address: str, Telephone: int, E_Mail: str, Date_of_Birth: int, SSN: int, Title: Employee_Title__Non_Admin, Supervisor: Administrator_Actor, Salary: int, employee_Title__Non_Admin22: "Employee_Title__Non_Admin" = None, administration24: "Administration" = None):
        self.Name__1st_and_last_ = Name__1st_and_last_
        self.Username = Username
        self.Password = Password
        self.Employee_ID = Employee_ID
        self.Address = Address
        self.Telephone = Telephone
        self.E_Mail = E_Mail
        self.Date_of_Birth = Date_of_Birth
        self.SSN = SSN
        self.Title = Title
        self.Supervisor = Supervisor
        self.Salary = Salary
        self.employee_Title__Non_Admin22 = employee_Title__Non_Admin22
        self.administration24 = administration24
        
        pass
    @property
    def Employee_ID(self):
        return self.__Employee_ID
    @Employee_ID.setter
    def Employee_ID(self, Employee_ID: int):
        self.__Employee_ID = Employee_ID

    @property
    def Supervisor(self):
        return self.__Supervisor
    @Supervisor.setter
    def Supervisor(self, Supervisor: Administrator_Actor):
        self.__Supervisor = Supervisor

    @property
    def Username(self):
        return self.__Username
    @Username.setter
    def Username(self, Username: Log_In_UseCase):
        self.__Username = Username

    @property
    def Name__1st_and_last_(self):
        return self.__Name__1st_and_last_
    @Name__1st_and_last_.setter
    def Name__1st_and_last_(self, Name__1st_and_last_: Employee_Actor):
        self.__Name__1st_and_last_ = Name__1st_and_last_

    @property
    def E_Mail(self):
        return self.__E_Mail
    @E_Mail.setter
    def E_Mail(self, E_Mail: str):
        self.__E_Mail = E_Mail

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Salary(self):
        return self.__Salary
    @Salary.setter
    def Salary(self, Salary: int):
        self.__Salary = Salary

    @property
    def Telephone(self):
        return self.__Telephone
    @Telephone.setter
    def Telephone(self, Telephone: int):
        self.__Telephone = Telephone

    @property
    def SSN(self):
        return self.__SSN
    @SSN.setter
    def SSN(self, SSN: int):
        self.__SSN = SSN

    @property
    def Title(self):
        return self.__Title
    @Title.setter
    def Title(self, Title: Employee_Title__Non_Admin):
        self.__Title = Title

    @property
    def Date_of_Birth(self):
        return self.__Date_of_Birth
    @Date_of_Birth.setter
    def Date_of_Birth(self, Date_of_Birth: int):
        self.__Date_of_Birth = Date_of_Birth

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def administration24(self):
        return self.__administration24
    @administration24.setter
    def administration24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee_DB__administration24", None)
        self.__administration24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_DB25"):
                opp_val = getattr(old_value, "employee_DB25", None)
                if opp_val == self:
                    setattr(old_value, "employee_DB25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_DB25"):
                opp_val = getattr(value, "employee_DB25", None)
                setattr(value, "employee_DB25", self)

    @property
    def employee_Title__Non_Admin22(self):
        return self.__employee_Title__Non_Admin22
    @employee_Title__Non_Admin22.setter
    def employee_Title__Non_Admin22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee_DB__employee_Title__Non_Admin22", None)
        self.__employee_Title__Non_Admin22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_DB23"):
                opp_val = getattr(old_value, "employee_DB23", None)
                if opp_val == self:
                    setattr(old_value, "employee_DB23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_DB23"):
                opp_val = getattr(value, "employee_DB23", None)
                setattr(value, "employee_DB23", self)



class Employee_Title__Non_Admin:

    def __init__(self, Teacher: Employee_Actor, Cook: Employee_Actor, Assistant_Teacher: Employee_Actor, Maintenance: Employee_Actor, Community_Service: str, Work_Study: str, employee_DB23: "Employee_DB" = None):
        self.Teacher = Teacher
        self.Cook = Cook
        self.Assistant_Teacher = Assistant_Teacher
        self.Maintenance = Maintenance
        self.Community_Service = Community_Service
        self.Work_Study = Work_Study
        self.employee_DB23 = employee_DB23
        
        pass
    @property
    def Cook(self):
        return self.__Cook
    @Cook.setter
    def Cook(self, Cook: Employee_Actor):
        self.__Cook = Cook

    @property
    def Maintenance(self):
        return self.__Maintenance
    @Maintenance.setter
    def Maintenance(self, Maintenance: Employee_Actor):
        self.__Maintenance = Maintenance

    @property
    def Community_Service(self):
        return self.__Community_Service
    @Community_Service.setter
    def Community_Service(self, Community_Service: str):
        self.__Community_Service = Community_Service

    @property
    def Work_Study(self):
        return self.__Work_Study
    @Work_Study.setter
    def Work_Study(self, Work_Study: str):
        self.__Work_Study = Work_Study

    @property
    def Assistant_Teacher(self):
        return self.__Assistant_Teacher
    @Assistant_Teacher.setter
    def Assistant_Teacher(self, Assistant_Teacher: Employee_Actor):
        self.__Assistant_Teacher = Assistant_Teacher

    @property
    def Teacher(self):
        return self.__Teacher
    @Teacher.setter
    def Teacher(self, Teacher: Employee_Actor):
        self.__Teacher = Teacher

    @property
    def employee_DB23(self):
        return self.__employee_DB23
    @employee_DB23.setter
    def employee_DB23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee_Title__Non_Admin__employee_DB23", None)
        self.__employee_DB23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Title__Non_Admin22"):
                opp_val = getattr(old_value, "employee_Title__Non_Admin22", None)
                if opp_val == self:
                    setattr(old_value, "employee_Title__Non_Admin22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Title__Non_Admin22"):
                opp_val = getattr(value, "employee_Title__Non_Admin22", None)
                setattr(value, "employee_Title__Non_Admin22", self)



class Administration:

    def __init__(self, Executive_Director___COO: Administrator_Actor, Asst__Executive_Director: Administrator_Actor, CFO: Administrator_Actor, Office_Manager: Employee_Actor, employee_DB25: "Employee_DB" = None):
        self.Executive_Director___COO = Executive_Director___COO
        self.Asst__Executive_Director = Asst__Executive_Director
        self.CFO = CFO
        self.Office_Manager = Office_Manager
        self.employee_DB25 = employee_DB25
        
        pass
    @property
    def CFO(self):
        return self.__CFO
    @CFO.setter
    def CFO(self, CFO: Administrator_Actor):
        self.__CFO = CFO

    @property
    def Office_Manager(self):
        return self.__Office_Manager
    @Office_Manager.setter
    def Office_Manager(self, Office_Manager: Employee_Actor):
        self.__Office_Manager = Office_Manager

    @property
    def Executive_Director___COO(self):
        return self.__Executive_Director___COO
    @Executive_Director___COO.setter
    def Executive_Director___COO(self, Executive_Director___COO: Administrator_Actor):
        self.__Executive_Director___COO = Executive_Director___COO

    @property
    def Asst__Executive_Director(self):
        return self.__Asst__Executive_Director
    @Asst__Executive_Director.setter
    def Asst__Executive_Director(self, Asst__Executive_Director: Administrator_Actor):
        self.__Asst__Executive_Director = Asst__Executive_Director

    @property
    def employee_DB25(self):
        return self.__employee_DB25
    @employee_DB25.setter
    def employee_DB25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administration__employee_DB25", None)
        self.__employee_DB25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administration24"):
                opp_val = getattr(old_value, "administration24", None)
                if opp_val == self:
                    setattr(old_value, "administration24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administration24"):
                opp_val = getattr(value, "administration24", None)
                setattr(value, "administration24", self)

