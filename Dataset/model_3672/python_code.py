from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class company_Company:

    pass
class company_Employee:

    def __init__(self, name: str, company_Employee: "company_Company" = None, company_Employee5: "company_Department" = None):
        self.name = name
        self.company_Employee = company_Employee
        self.company_Employee5 = company_Employee5
        
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
            if hasattr(old_value, "company_Company2"):
                opp_val = getattr(old_value, "company_Company2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Company2"):
                opp_val = getattr(value, "company_Company2", None)
                if opp_val is None:
                    setattr(value, "company_Company2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def company_Employee5(self):
        return self.__company_Employee5

    @company_Employee5.setter
    def company_Employee5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__company_Employee5", None)
        self.__company_Employee5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Department4"):
                opp_val = getattr(old_value, "company_Department4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Department4"):
                opp_val = getattr(value, "company_Department4", None)
                if opp_val is None:
                    setattr(value, "company_Department4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class company_Department:

    def __init__(self, name: str, budget: int, company_Department: "company_Company" = None, company_Department4: set["company_Employee"] = None):
        self.name = name
        self.budget = budget
        self.company_Department = company_Department
        self.company_Department4 = company_Department4 if company_Department4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def budget(self) -> int:
        return self.__budget

    @budget.setter
    def budget(self, budget: int):
        self.__budget = budget

    @property
    def company_Department4(self):
        return self.__company_Department4

    @company_Department4.setter
    def company_Department4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Department__company_Department4", None)
        self.__company_Department4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company_Employee5"):
                    opp_val = getattr(item, "company_Employee5", None)
                    
                    if opp_val == self:
                        setattr(item, "company_Employee5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company_Employee5"):
                    opp_val = getattr(item, "company_Employee5", None)
                    
                    setattr(item, "company_Employee5", self)
                    

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
