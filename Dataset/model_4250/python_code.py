from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Employees_Employee:

    def __init__(self, name: str, salary: int, ID: int, Employees_Employee: "Employees_EmployeeContainer" = None):
        self.name = name
        self.salary = salary
        self.ID = ID
        self.Employees_Employee = Employees_Employee
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ID(self) -> int:
        return self.__ID

    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def salary(self) -> int:
        return self.__salary

    @salary.setter
    def salary(self, salary: int):
        self.__salary = salary

    @property
    def Employees_Employee(self):
        return self.__Employees_Employee

    @Employees_Employee.setter
    def Employees_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employees_Employee__Employees_Employee", None)
        self.__Employees_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employees_EmployeeContainer"):
                opp_val = getattr(old_value, "Employees_EmployeeContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employees_EmployeeContainer"):
                opp_val = getattr(value, "Employees_EmployeeContainer", None)
                if opp_val is None:
                    setattr(value, "Employees_EmployeeContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Employees_EmployeeContainer:

    pass