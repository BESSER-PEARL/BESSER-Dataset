from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class company_Employee:

    def __init__(self, name: str, address: str, salary: float, company_Employee: "company_Department" = None, company_Employee8: "company_Department" = None, company_Employee11: "company_Employee" = None, company_Employee9: "company_Employee" = None):
        self.name = name
        self.address = address
        self.salary = salary
        self.company_Employee = company_Employee
        self.company_Employee8 = company_Employee8
        self.company_Employee11 = company_Employee11
        self.company_Employee9 = company_Employee9
        
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
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, salary: float):
        self.__salary = salary

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
                if opp_val == self:
                    setattr(old_value, "company_Department2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Department2"):
                opp_val = getattr(value, "company_Department2", None)
                setattr(value, "company_Department2", self)

    @property
    def company_Employee11(self):
        return self.__company_Employee11

    @company_Employee11.setter
    def company_Employee11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__company_Employee11", None)
        self.__company_Employee11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Employee9"):
                opp_val = getattr(old_value, "company_Employee9", None)
                if opp_val == self:
                    setattr(old_value, "company_Employee9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Employee9"):
                opp_val = getattr(value, "company_Employee9", None)
                setattr(value, "company_Employee9", self)

    @property
    def company_Employee8(self):
        return self.__company_Employee8

    @company_Employee8.setter
    def company_Employee8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__company_Employee8", None)
        self.__company_Employee8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Department7"):
                opp_val = getattr(old_value, "company_Department7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Department7"):
                opp_val = getattr(value, "company_Department7", None)
                if opp_val is None:
                    setattr(value, "company_Department7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def company_Employee9(self):
        return self.__company_Employee9

    @company_Employee9.setter
    def company_Employee9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__company_Employee9", None)
        self.__company_Employee9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Employee11"):
                opp_val = getattr(old_value, "company_Employee11", None)
                if opp_val == self:
                    setattr(old_value, "company_Employee11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Employee11"):
                opp_val = getattr(value, "company_Employee11", None)
                setattr(value, "company_Employee11", self)

class company_Department:

    def __init__(self, name: str, company_Department: "company_Company" = None, company_Department2: "company_Employee" = None, company_Department5: "company_Department" = None, company_Department3: set["company_Department"] = None, company_Department7: set["company_Employee"] = None):
        self.name = name
        self.company_Department = company_Department
        self.company_Department2 = company_Department2
        self.company_Department5 = company_Department5
        self.company_Department3 = company_Department3 if company_Department3 is not None else set()
        self.company_Department7 = company_Department7 if company_Department7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def company_Department2(self):
        return self.__company_Department2

    @company_Department2.setter
    def company_Department2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Department__company_Department2", None)
        self.__company_Department2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Employee"):
                opp_val = getattr(old_value, "company_Employee", None)
                if opp_val == self:
                    setattr(old_value, "company_Employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Employee"):
                opp_val = getattr(value, "company_Employee", None)
                setattr(value, "company_Employee", self)

    @property
    def company_Department5(self):
        return self.__company_Department5

    @company_Department5.setter
    def company_Department5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Department__company_Department5", None)
        self.__company_Department5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Department3"):
                opp_val = getattr(old_value, "company_Department3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Department3"):
                opp_val = getattr(value, "company_Department3", None)
                if opp_val is None:
                    setattr(value, "company_Department3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def company_Department7(self):
        return self.__company_Department7

    @company_Department7.setter
    def company_Department7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Department__company_Department7", None)
        self.__company_Department7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company_Employee8"):
                    opp_val = getattr(item, "company_Employee8", None)
                    
                    if opp_val == self:
                        setattr(item, "company_Employee8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company_Employee8"):
                    opp_val = getattr(item, "company_Employee8", None)
                    
                    setattr(item, "company_Employee8", self)
                    

    @property
    def company_Department3(self):
        return self.__company_Department3

    @company_Department3.setter
    def company_Department3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Department__company_Department3", None)
        self.__company_Department3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company_Department5"):
                    opp_val = getattr(item, "company_Department5", None)
                    
                    if opp_val == self:
                        setattr(item, "company_Department5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company_Department5"):
                    opp_val = getattr(item, "company_Department5", None)
                    
                    setattr(item, "company_Department5", self)
                    

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
                    
