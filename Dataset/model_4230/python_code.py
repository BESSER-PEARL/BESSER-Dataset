from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class NamedEntity:

    pass
class employee_Department(NamedEntity):

    def __init__(self, isRich: bool, employee_Department: "employee_Company" = None, employee_Department2: set["employee_Employee"] = None):
        self.isRich = isRich
        self.employee_Department = employee_Department
        self.employee_Department2 = employee_Department2 if employee_Department2 is not None else set()
        
    @property
    def isRich(self) -> bool:
        return self.__isRich

    @isRich.setter
    def isRich(self, isRich: bool):
        self.__isRich = isRich

    @property
    def employee_Department(self):
        return self.__employee_Department

    @employee_Department.setter
    def employee_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Department__employee_Department", None)
        self.__employee_Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Company"):
                opp_val = getattr(old_value, "employee_Company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Company"):
                opp_val = getattr(value, "employee_Company", None)
                if opp_val is None:
                    setattr(value, "employee_Company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def employee_Department2(self):
        return self.__employee_Department2

    @employee_Department2.setter
    def employee_Department2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Department__employee_Department2", None)
        self.__employee_Department2 = value if value is not None else set()
        
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

class employee_Company(NamedEntity):

    pass
class employee_NamedEntity:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
