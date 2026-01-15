from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class CompanyModel_Product:

    def __init__(self, name: str, productID: int, CompanyModel_Product: "CompanyModel_Department" = None):
        self.name = name
        self.productID = productID
        self.CompanyModel_Product = CompanyModel_Product
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def productID(self) -> int:
        return self.__productID

    @productID.setter
    def productID(self, productID: int):
        self.__productID = productID

    @property
    def CompanyModel_Product(self):
        return self.__CompanyModel_Product

    @CompanyModel_Product.setter
    def CompanyModel_Product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompanyModel_Product__CompanyModel_Product", None)
        self.__CompanyModel_Product = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompanyModel_Department4"):
                opp_val = getattr(old_value, "CompanyModel_Department4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompanyModel_Department4"):
                opp_val = getattr(value, "CompanyModel_Department4", None)
                if opp_val is None:
                    setattr(value, "CompanyModel_Department4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CompanyModel_Employee:

    def __init__(self, isManager: bool, name: str, CompanyModel_Employee: "CompanyModel_Department" = None):
        self.isManager = isManager
        self.name = name
        self.CompanyModel_Employee = CompanyModel_Employee
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isManager(self) -> bool:
        return self.__isManager

    @isManager.setter
    def isManager(self, isManager: bool):
        self.__isManager = isManager

    @property
    def CompanyModel_Employee(self):
        return self.__CompanyModel_Employee

    @CompanyModel_Employee.setter
    def CompanyModel_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompanyModel_Employee__CompanyModel_Employee", None)
        self.__CompanyModel_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompanyModel_Department2"):
                opp_val = getattr(old_value, "CompanyModel_Department2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompanyModel_Department2"):
                opp_val = getattr(value, "CompanyModel_Department2", None)
                if opp_val is None:
                    setattr(value, "CompanyModel_Department2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CompanyModel_Department:

    def __init__(self, number: int, CompanyModel_Department: "CompanyModel_Company" = None, CompanyModel_Department2: set["CompanyModel_Employee"] = None, CompanyModel_Department4: set["CompanyModel_Product"] = None):
        self.number = number
        self.CompanyModel_Department = CompanyModel_Department
        self.CompanyModel_Department2 = CompanyModel_Department2 if CompanyModel_Department2 is not None else set()
        self.CompanyModel_Department4 = CompanyModel_Department4 if CompanyModel_Department4 is not None else set()
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def CompanyModel_Department2(self):
        return self.__CompanyModel_Department2

    @CompanyModel_Department2.setter
    def CompanyModel_Department2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompanyModel_Department__CompanyModel_Department2", None)
        self.__CompanyModel_Department2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompanyModel_Employee"):
                    opp_val = getattr(item, "CompanyModel_Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "CompanyModel_Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompanyModel_Employee"):
                    opp_val = getattr(item, "CompanyModel_Employee", None)
                    
                    setattr(item, "CompanyModel_Employee", self)
                    

    @property
    def CompanyModel_Department4(self):
        return self.__CompanyModel_Department4

    @CompanyModel_Department4.setter
    def CompanyModel_Department4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompanyModel_Department__CompanyModel_Department4", None)
        self.__CompanyModel_Department4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompanyModel_Product"):
                    opp_val = getattr(item, "CompanyModel_Product", None)
                    
                    if opp_val == self:
                        setattr(item, "CompanyModel_Product", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompanyModel_Product"):
                    opp_val = getattr(item, "CompanyModel_Product", None)
                    
                    setattr(item, "CompanyModel_Product", self)
                    

    @property
    def CompanyModel_Department(self):
        return self.__CompanyModel_Department

    @CompanyModel_Department.setter
    def CompanyModel_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompanyModel_Department__CompanyModel_Department", None)
        self.__CompanyModel_Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompanyModel_Company"):
                opp_val = getattr(old_value, "CompanyModel_Company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompanyModel_Company"):
                opp_val = getattr(value, "CompanyModel_Company", None)
                if opp_val is None:
                    setattr(value, "CompanyModel_Company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CompanyModel_Company:

    def __init__(self, name: str, CompanyModel_Company: set["CompanyModel_Department"] = None):
        self.name = name
        self.CompanyModel_Company = CompanyModel_Company if CompanyModel_Company is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def CompanyModel_Company(self):
        return self.__CompanyModel_Company

    @CompanyModel_Company.setter
    def CompanyModel_Company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompanyModel_Company__CompanyModel_Company", None)
        self.__CompanyModel_Company = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompanyModel_Department"):
                    opp_val = getattr(item, "CompanyModel_Department", None)
                    
                    if opp_val == self:
                        setattr(item, "CompanyModel_Department", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompanyModel_Department"):
                    opp_val = getattr(item, "CompanyModel_Department", None)
                    
                    setattr(item, "CompanyModel_Department", self)
                    
