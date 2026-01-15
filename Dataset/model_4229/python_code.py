from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class CompanyLanguage_Company:

    def __init__(self, name: str, CompanyLanguage_Company: set["CompanyLanguage_Employee"] = None, CompanyLanguage_Company6: set["CompanyLanguage_CEO"] = None, CompanyLanguage_Company9: set["CompanyLanguage_Admin"] = None):
        self.name = name
        self.CompanyLanguage_Company = CompanyLanguage_Company if CompanyLanguage_Company is not None else set()
        self.CompanyLanguage_Company6 = CompanyLanguage_Company6 if CompanyLanguage_Company6 is not None else set()
        self.CompanyLanguage_Company9 = CompanyLanguage_Company9 if CompanyLanguage_Company9 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def CompanyLanguage_Company6(self):
        return self.__CompanyLanguage_Company6

    @CompanyLanguage_Company6.setter
    def CompanyLanguage_Company6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompanyLanguage_Company__CompanyLanguage_Company6", None)
        self.__CompanyLanguage_Company6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompanyLanguage_CEO7"):
                    opp_val = getattr(item, "CompanyLanguage_CEO7", None)
                    
                    if opp_val == self:
                        setattr(item, "CompanyLanguage_CEO7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompanyLanguage_CEO7"):
                    opp_val = getattr(item, "CompanyLanguage_CEO7", None)
                    
                    setattr(item, "CompanyLanguage_CEO7", self)
                    

    @property
    def CompanyLanguage_Company(self):
        return self.__CompanyLanguage_Company

    @CompanyLanguage_Company.setter
    def CompanyLanguage_Company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompanyLanguage_Company__CompanyLanguage_Company", None)
        self.__CompanyLanguage_Company = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompanyLanguage_Employee4"):
                    opp_val = getattr(item, "CompanyLanguage_Employee4", None)
                    
                    if opp_val == self:
                        setattr(item, "CompanyLanguage_Employee4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompanyLanguage_Employee4"):
                    opp_val = getattr(item, "CompanyLanguage_Employee4", None)
                    
                    setattr(item, "CompanyLanguage_Employee4", self)
                    

    @property
    def CompanyLanguage_Company9(self):
        return self.__CompanyLanguage_Company9

    @CompanyLanguage_Company9.setter
    def CompanyLanguage_Company9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompanyLanguage_Company__CompanyLanguage_Company9", None)
        self.__CompanyLanguage_Company9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompanyLanguage_Admin10"):
                    opp_val = getattr(item, "CompanyLanguage_Admin10", None)
                    
                    if opp_val == self:
                        setattr(item, "CompanyLanguage_Admin10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompanyLanguage_Admin10"):
                    opp_val = getattr(item, "CompanyLanguage_Admin10", None)
                    
                    setattr(item, "CompanyLanguage_Admin10", self)
                    

class CompanyLanguage_Employee:

    def __init__(self, name: str, CompanyLanguage_Employee: "CompanyLanguage_CEO" = None, CompanyLanguage_Employee4: "CompanyLanguage_Company" = None):
        self.name = name
        self.CompanyLanguage_Employee = CompanyLanguage_Employee
        self.CompanyLanguage_Employee4 = CompanyLanguage_Employee4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def CompanyLanguage_Employee(self):
        return self.__CompanyLanguage_Employee

    @CompanyLanguage_Employee.setter
    def CompanyLanguage_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompanyLanguage_Employee__CompanyLanguage_Employee", None)
        self.__CompanyLanguage_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompanyLanguage_CEO2"):
                opp_val = getattr(old_value, "CompanyLanguage_CEO2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompanyLanguage_CEO2"):
                opp_val = getattr(value, "CompanyLanguage_CEO2", None)
                if opp_val is None:
                    setattr(value, "CompanyLanguage_CEO2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompanyLanguage_Employee4(self):
        return self.__CompanyLanguage_Employee4

    @CompanyLanguage_Employee4.setter
    def CompanyLanguage_Employee4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompanyLanguage_Employee__CompanyLanguage_Employee4", None)
        self.__CompanyLanguage_Employee4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompanyLanguage_Company"):
                opp_val = getattr(old_value, "CompanyLanguage_Company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompanyLanguage_Company"):
                opp_val = getattr(value, "CompanyLanguage_Company", None)
                if opp_val is None:
                    setattr(value, "CompanyLanguage_Company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CompanyLanguage_CEO:

    def __init__(self, name: str, CompanyLanguage_CEO: "CompanyLanguage_Admin" = None, CompanyLanguage_CEO2: set["CompanyLanguage_Employee"] = None, CompanyLanguage_CEO7: "CompanyLanguage_Company" = None):
        self.name = name
        self.CompanyLanguage_CEO = CompanyLanguage_CEO
        self.CompanyLanguage_CEO2 = CompanyLanguage_CEO2 if CompanyLanguage_CEO2 is not None else set()
        self.CompanyLanguage_CEO7 = CompanyLanguage_CEO7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def CompanyLanguage_CEO(self):
        return self.__CompanyLanguage_CEO

    @CompanyLanguage_CEO.setter
    def CompanyLanguage_CEO(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompanyLanguage_CEO__CompanyLanguage_CEO", None)
        self.__CompanyLanguage_CEO = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompanyLanguage_Admin"):
                opp_val = getattr(old_value, "CompanyLanguage_Admin", None)
                if opp_val == self:
                    setattr(old_value, "CompanyLanguage_Admin", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompanyLanguage_Admin"):
                opp_val = getattr(value, "CompanyLanguage_Admin", None)
                setattr(value, "CompanyLanguage_Admin", self)

    @property
    def CompanyLanguage_CEO7(self):
        return self.__CompanyLanguage_CEO7

    @CompanyLanguage_CEO7.setter
    def CompanyLanguage_CEO7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompanyLanguage_CEO__CompanyLanguage_CEO7", None)
        self.__CompanyLanguage_CEO7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompanyLanguage_Company6"):
                opp_val = getattr(old_value, "CompanyLanguage_Company6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompanyLanguage_Company6"):
                opp_val = getattr(value, "CompanyLanguage_Company6", None)
                if opp_val is None:
                    setattr(value, "CompanyLanguage_Company6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompanyLanguage_CEO2(self):
        return self.__CompanyLanguage_CEO2

    @CompanyLanguage_CEO2.setter
    def CompanyLanguage_CEO2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompanyLanguage_CEO__CompanyLanguage_CEO2", None)
        self.__CompanyLanguage_CEO2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompanyLanguage_Employee"):
                    opp_val = getattr(item, "CompanyLanguage_Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "CompanyLanguage_Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompanyLanguage_Employee"):
                    opp_val = getattr(item, "CompanyLanguage_Employee", None)
                    
                    setattr(item, "CompanyLanguage_Employee", self)
                    

class CompanyLanguage_Admin:

    def __init__(self, name: str, CompanyLanguage_Admin: "CompanyLanguage_CEO" = None, CompanyLanguage_Admin10: "CompanyLanguage_Company" = None):
        self.name = name
        self.CompanyLanguage_Admin = CompanyLanguage_Admin
        self.CompanyLanguage_Admin10 = CompanyLanguage_Admin10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def CompanyLanguage_Admin10(self):
        return self.__CompanyLanguage_Admin10

    @CompanyLanguage_Admin10.setter
    def CompanyLanguage_Admin10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompanyLanguage_Admin__CompanyLanguage_Admin10", None)
        self.__CompanyLanguage_Admin10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompanyLanguage_Company9"):
                opp_val = getattr(old_value, "CompanyLanguage_Company9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompanyLanguage_Company9"):
                opp_val = getattr(value, "CompanyLanguage_Company9", None)
                if opp_val is None:
                    setattr(value, "CompanyLanguage_Company9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompanyLanguage_Admin(self):
        return self.__CompanyLanguage_Admin

    @CompanyLanguage_Admin.setter
    def CompanyLanguage_Admin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompanyLanguage_Admin__CompanyLanguage_Admin", None)
        self.__CompanyLanguage_Admin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompanyLanguage_CEO"):
                opp_val = getattr(old_value, "CompanyLanguage_CEO", None)
                if opp_val == self:
                    setattr(old_value, "CompanyLanguage_CEO", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompanyLanguage_CEO"):
                opp_val = getattr(value, "CompanyLanguage_CEO", None)
                setattr(value, "CompanyLanguage_CEO", self)
