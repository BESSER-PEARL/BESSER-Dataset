from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class employee_NamedEntity:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Department:

    pass
class employee_PoorDepartment(Department):

    pass
class employee_RichDepartment(Department):

    pass
class NamedEntity:

    pass
class employee_Department(NamedEntity):

    pass
class employee_Company(NamedEntity):

    pass
class employee_Employee(NamedEntity):

    def __init__(self, wage: int, employee_Employee: "employee_Department" = None):
        self.wage = wage
        self.employee_Employee = employee_Employee
        
    @property
    def wage(self) -> int:
        return self.__wage

    @wage.setter
    def wage(self, wage: int):
        self.__wage = wage

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
            if hasattr(old_value, "employee_Department2"):
                opp_val = getattr(old_value, "employee_Department2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Department2"):
                opp_val = getattr(value, "employee_Department2", None)
                if opp_val is None:
                    setattr(value, "employee_Department2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
