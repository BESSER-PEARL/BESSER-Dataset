from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class company_Department:

    def __init__(self, number: int, company_Department: "company_Company" = None, company_Department2: set["company_Employee"] = None):
        self.number = number
        self.company_Department = company_Department
        self.company_Department2 = company_Department2 if company_Department2 is not None else set()
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def company_Department2(self):
        return self.__company_Department2

    @company_Department2.setter
    def company_Department2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Department__company_Department2", None)
        self.__company_Department2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company_Employee"):
                    opp_val = getattr(item, "company_Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "company_Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company_Employee"):
                    opp_val = getattr(item, "company_Employee", None)
                    
                    setattr(item, "company_Employee", self)
                    

    @property
    def company_Department(self):
        return self.__company_Department

    @company_Department.setter
    def company_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Department__company_Department", None)
        self.__company_Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Company"):
                opp_val = getattr(old_value, "company_Company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Company"):
                opp_val = getattr(value, "company_Company", None)
                if opp_val is None:
                    setattr(value, "company_Company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class company_Company:

    def __init__(self, name: str, company_Company: set["company_Department"] = None):
        self.name = name
        self.company_Company = company_Company if company_Company is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def company_Company(self):
        return self.__company_Company

    @company_Company.setter
    def company_Company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Company__company_Company", None)
        self.__company_Company = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company_Department"):
                    opp_val = getattr(item, "company_Department", None)
                    
                    if opp_val == self:
                        setattr(item, "company_Department", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company_Department"):
                    opp_val = getattr(item, "company_Department", None)
                    
                    setattr(item, "company_Department", self)
                    

class company_Employee:

    def __init__(self, name: str, company_Employee: "company_Department" = None):
        self.name = name
        self.company_Employee = company_Employee
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def company_Employee(self):
        return self.__company_Employee

    @company_Employee.setter
    def company_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__company_Employee", None)
        self.__company_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Department2"):
                opp_val = getattr(old_value, "company_Department2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Department2"):
                opp_val = getattr(value, "company_Department2", None)
                if opp_val is None:
                    setattr(value, "company_Department2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
