from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class techStaff_DeveloperTest:

    pass


class techStaff_DatabaseAdminTest:

    pass


class techStaff_Developer:

    pass


class techStaff_DatabaseAdmin:

    pass


class Staff_Employee(ABC):

    def __init__(self, name: str, nationalInsurance: str, salary: float):
        self.name = name
        self.nationalInsurance = nationalInsurance
        self.salary = salary
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nationalInsurance(self):
        return self.__nationalInsurance
    @nationalInsurance.setter
    def nationalInsurance(self, nationalInsurance: str):
        self.__nationalInsurance = nationalInsurance

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary: float):
        self.__salary = salary



class Management_ManagerTest:

    pass


class Management_DirectorTest:

    pass


class Management_Manager:

    def __init__(self, deptName: str, managertest4: "Management_ManagerTest" = None):
        self.deptName = deptName
        self.managertest4 = managertest4
        
        pass
    @property
    def deptName(self):
        return self.__deptName
    @deptName.setter
    def deptName(self, deptName: str):
        self.__deptName = deptName

    @property
    def managertest4(self):
        return self.__managertest4
    @managertest4.setter
    def managertest4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Management_Manager__managertest4", None)
        self.__managertest4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manager5"):
                opp_val = getattr(old_value, "manager5", None)
                if opp_val == self:
                    setattr(old_value, "manager5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manager5"):
                opp_val = getattr(value, "manager5", None)
                setattr(value, "manager5", self)



class Management_Director:

    def __init__(self, budget: float, directortest6: "Management_DirectorTest" = None):
        self.budget = budget
        self.directortest6 = directortest6
        
        pass
    @property
    def budget(self):
        return self.__budget
    @budget.setter
    def budget(self, budget: float):
        self.__budget = budget

    @property
    def directortest6(self):
        return self.__directortest6
    @directortest6.setter
    def directortest6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Management_Director__directortest6", None)
        self.__directortest6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "director7"):
                opp_val = getattr(old_value, "director7", None)
                if opp_val == self:
                    setattr(old_value, "director7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "director7"):
                opp_val = getattr(value, "director7", None)
                setattr(value, "director7", self)

