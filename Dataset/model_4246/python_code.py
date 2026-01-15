from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ce_Employee:

    def __init__(self, name: str, address: str, department: str, ce_Employee: "ce_Company" = None):
        self.name = name
        self.address = address
        self.department = department
        self.ce_Employee = ce_Employee
        
    @property
    def department(self) -> str:
        return self.__department

    @department.setter
    def department(self, department: str):
        self.__department = department

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def ce_Employee(self):
        return self.__ce_Employee

    @ce_Employee.setter
    def ce_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ce_Employee__ce_Employee", None)
        self.__ce_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ce_Company"):
                opp_val = getattr(old_value, "ce_Company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ce_Company"):
                opp_val = getattr(value, "ce_Company", None)
                if opp_val is None:
                    setattr(value, "ce_Company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ce_Company:

    def __init__(self, name: str, ce_Company: set["ce_Employee"] = None):
        self.name = name
        self.ce_Company = ce_Company if ce_Company is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ce_Company(self):
        return self.__ce_Company

    @ce_Company.setter
    def ce_Company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ce_Company__ce_Company", None)
        self.__ce_Company = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ce_Employee"):
                    opp_val = getattr(item, "ce_Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "ce_Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ce_Employee"):
                    opp_val = getattr(item, "ce_Employee", None)
                    
                    setattr(item, "ce_Employee", self)
                    
