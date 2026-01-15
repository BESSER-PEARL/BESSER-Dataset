from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class bz321765_EmployeePK:

    def __init__(self, id: str, firstName: str, lastName: str, bz321765_EmployeePK: "bz321765_Employee" = None):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.bz321765_EmployeePK = bz321765_EmployeePK
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def bz321765_EmployeePK(self):
        return self.__bz321765_EmployeePK

    @bz321765_EmployeePK.setter
    def bz321765_EmployeePK(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz321765_EmployeePK__bz321765_EmployeePK", None)
        self.__bz321765_EmployeePK = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bz321765_Employee"):
                opp_val = getattr(old_value, "bz321765_Employee", None)
                if opp_val == self:
                    setattr(old_value, "bz321765_Employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bz321765_Employee"):
                opp_val = getattr(value, "bz321765_Employee", None)
                setattr(value, "bz321765_Employee", self)

class bz321765_Employee:

    def __init__(self, title: str, salary: str, bz321765_Employee: "bz321765_EmployeePK" = None):
        self.title = title
        self.salary = salary
        self.bz321765_Employee = bz321765_Employee
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def salary(self) -> str:
        return self.__salary

    @salary.setter
    def salary(self, salary: str):
        self.__salary = salary

    @property
    def bz321765_Employee(self):
        return self.__bz321765_Employee

    @bz321765_Employee.setter
    def bz321765_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz321765_Employee__bz321765_Employee", None)
        self.__bz321765_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bz321765_EmployeePK"):
                opp_val = getattr(old_value, "bz321765_EmployeePK", None)
                if opp_val == self:
                    setattr(old_value, "bz321765_EmployeePK", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bz321765_EmployeePK"):
                opp_val = getattr(value, "bz321765_EmployeePK", None)
                setattr(value, "bz321765_EmployeePK", self)
