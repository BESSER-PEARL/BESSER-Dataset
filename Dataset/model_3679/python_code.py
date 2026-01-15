from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class company_TestClass:

    def __init__(self, stringAttribute1: str, stringAttribute2: str, intAttribute1: int, intAttribute2: int):
        self.stringAttribute1 = stringAttribute1
        self.stringAttribute2 = stringAttribute2
        self.intAttribute1 = intAttribute1
        self.intAttribute2 = intAttribute2
        
    @property
    def stringAttribute2(self) -> str:
        return self.__stringAttribute2

    @stringAttribute2.setter
    def stringAttribute2(self, stringAttribute2: str):
        self.__stringAttribute2 = stringAttribute2

    @property
    def intAttribute1(self) -> int:
        return self.__intAttribute1

    @intAttribute1.setter
    def intAttribute1(self, intAttribute1: int):
        self.__intAttribute1 = intAttribute1

    @property
    def stringAttribute1(self) -> str:
        return self.__stringAttribute1

    @stringAttribute1.setter
    def stringAttribute1(self, stringAttribute1: str):
        self.__stringAttribute1 = stringAttribute1

    @property
    def intAttribute2(self) -> int:
        return self.__intAttribute2

    @intAttribute2.setter
    def intAttribute2(self, intAttribute2: int):
        self.__intAttribute2 = intAttribute2

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
                if hasattr(item, "company_Department2"):
                    opp_val = getattr(item, "company_Department2", None)
                    
                    if opp_val == self:
                        setattr(item, "company_Department2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company_Department2"):
                    opp_val = getattr(item, "company_Department2", None)
                    
                    setattr(item, "company_Department2", self)
                    

class company_Employee:

    def __init__(self, firstName: str, lastName: str, age: int, company_Employee: "company_Department" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.company_Employee = company_Employee
        
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

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
            if hasattr(old_value, "company_Department"):
                opp_val = getattr(old_value, "company_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Department"):
                opp_val = getattr(value, "company_Department", None)
                if opp_val is None:
                    setattr(value, "company_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class company_Department:

    def __init__(self, number: int, company_Department: set["company_Employee"] = None, company_Department2: "company_Company" = None):
        self.number = number
        self.company_Department = company_Department if company_Department is not None else set()
        self.company_Department2 = company_Department2
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def company_Department(self):
        return self.__company_Department

    @company_Department.setter
    def company_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Department__company_Department", None)
        self.__company_Department = value if value is not None else set()
        
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
    def company_Department2(self):
        return self.__company_Department2

    @company_Department2.setter
    def company_Department2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Department__company_Department2", None)
        self.__company_Department2 = value
        
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
