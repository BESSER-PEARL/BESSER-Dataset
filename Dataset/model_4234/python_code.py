from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class employee_Department:

    def __init__(self, name: str, employee_Department: set["employee_Employee"] = None):
        self.name = name
        self.employee_Department = employee_Department if employee_Department is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def employee_Department(self):
        return self.__employee_Department

    @employee_Department.setter
    def employee_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Department__employee_Department", None)
        self.__employee_Department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee_Employee"):
                    opp_val = getattr(item, "employee_Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "employee_Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee_Employee"):
                    opp_val = getattr(item, "employee_Employee", None)
                    
                    setattr(item, "employee_Employee", self)
                    

class employee_Employee:

    def __init__(self, name: str, salary: str, age: str, hireDate: str, employee_Employee: "employee_Department" = None):
        self.name = name
        self.salary = salary
        self.age = age
        self.hireDate = hireDate
        self.employee_Employee = employee_Employee
        
    @property
    def hireDate(self) -> str:
        return self.__hireDate

    @hireDate.setter
    def hireDate(self, hireDate: str):
        self.__hireDate = hireDate

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def salary(self) -> str:
        return self.__salary

    @salary.setter
    def salary(self, salary: str):
        self.__salary = salary

    @property
    def age(self) -> str:
        return self.__age

    @age.setter
    def age(self, age: str):
        self.__age = age

    @property
    def employee_Employee(self):
        return self.__employee_Employee

    @employee_Employee.setter
    def employee_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee", None)
        self.__employee_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Department"):
                opp_val = getattr(old_value, "employee_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Department"):
                opp_val = getattr(value, "employee_Department", None)
                if opp_val is None:
                    setattr(value, "employee_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
