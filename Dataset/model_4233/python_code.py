from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class cde_Employee:

    def __init__(self, name: str, address: str, cde_Employee: "cde_Department" = None):
        self.name = name
        self.address = address
        self.cde_Employee = cde_Employee
        
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
    def cde_Employee(self):
        return self.__cde_Employee

    @cde_Employee.setter
    def cde_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cde_Employee__cde_Employee", None)
        self.__cde_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cde_Department2"):
                opp_val = getattr(old_value, "cde_Department2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cde_Department2"):
                opp_val = getattr(value, "cde_Department2", None)
                if opp_val is None:
                    setattr(value, "cde_Department2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cde_Department:

    def __init__(self, name: str, cde_Department: "cde_Company" = None, cde_Department2: set["cde_Employee"] = None):
        self.name = name
        self.cde_Department = cde_Department
        self.cde_Department2 = cde_Department2 if cde_Department2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cde_Department(self):
        return self.__cde_Department

    @cde_Department.setter
    def cde_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cde_Department__cde_Department", None)
        self.__cde_Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cde_Company"):
                opp_val = getattr(old_value, "cde_Company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cde_Company"):
                opp_val = getattr(value, "cde_Company", None)
                if opp_val is None:
                    setattr(value, "cde_Company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cde_Department2(self):
        return self.__cde_Department2

    @cde_Department2.setter
    def cde_Department2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cde_Department__cde_Department2", None)
        self.__cde_Department2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cde_Employee"):
                    opp_val = getattr(item, "cde_Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "cde_Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cde_Employee"):
                    opp_val = getattr(item, "cde_Employee", None)
                    
                    setattr(item, "cde_Employee", self)
                    

class cde_Company:

    def __init__(self, name: str, cde_Company: set["cde_Department"] = None):
        self.name = name
        self.cde_Company = cde_Company if cde_Company is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cde_Company(self):
        return self.__cde_Company

    @cde_Company.setter
    def cde_Company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cde_Company__cde_Company", None)
        self.__cde_Company = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cde_Department"):
                    opp_val = getattr(item, "cde_Department", None)
                    
                    if opp_val == self:
                        setattr(item, "cde_Department", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cde_Department"):
                    opp_val = getattr(item, "cde_Department", None)
                    
                    setattr(item, "cde_Department", self)
                    
