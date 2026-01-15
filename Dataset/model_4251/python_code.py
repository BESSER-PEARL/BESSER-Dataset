from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class employeeDsl_Employee:

    def __init__(self, ID: int, name: str, salary: int, employeeDsl_Employee: "employeeDsl_EmployeeContainer" = None):
        self.ID = ID
        self.name = name
        self.salary = salary
        self.employeeDsl_Employee = employeeDsl_Employee
        
    @property
    def salary(self) -> int:
        return self.__salary

    @salary.setter
    def salary(self, salary: int):
        self.__salary = salary

    @property
    def ID(self) -> int:
        return self.__ID

    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def employeeDsl_Employee(self):
        return self.__employeeDsl_Employee

    @employeeDsl_Employee.setter
    def employeeDsl_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employeeDsl_Employee__employeeDsl_Employee", None)
        self.__employeeDsl_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employeeDsl_EmployeeContainer"):
                opp_val = getattr(old_value, "employeeDsl_EmployeeContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employeeDsl_EmployeeContainer"):
                opp_val = getattr(value, "employeeDsl_EmployeeContainer", None)
                if opp_val is None:
                    setattr(value, "employeeDsl_EmployeeContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class employeeDsl_EmployeeContainer:

    pass