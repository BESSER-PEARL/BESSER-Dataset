from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class company_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class company_Department(NamedElement):

    def __init__(self, numberOfEmployees: int, ageSumOfEmployees: int, company_Department: "company_Company" = None, company_Department2: set["company_Person"] = None):
        self.numberOfEmployees = numberOfEmployees
        self.ageSumOfEmployees = ageSumOfEmployees
        self.company_Department = company_Department
        self.company_Department2 = company_Department2 if company_Department2 is not None else set()
        
    @property
    def ageSumOfEmployees(self) -> int:
        return self.__ageSumOfEmployees

    @ageSumOfEmployees.setter
    def ageSumOfEmployees(self, ageSumOfEmployees: int):
        self.__ageSumOfEmployees = ageSumOfEmployees

    @property
    def numberOfEmployees(self) -> int:
        return self.__numberOfEmployees

    @numberOfEmployees.setter
    def numberOfEmployees(self, numberOfEmployees: int):
        self.__numberOfEmployees = numberOfEmployees

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
                if hasattr(item, "company_Person"):
                    opp_val = getattr(item, "company_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "company_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company_Person"):
                    opp_val = getattr(item, "company_Person", None)
                    
                    setattr(item, "company_Person", self)
                    

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

class company_Person(NamedElement):

    def __init__(self, firstName: str, fullName: str, age: int, company_Person: "company_Department" = None, company_Person5: "company_Person" = None, company_Person3: "company_Person" = None):
        self.firstName = firstName
        self.fullName = fullName
        self.age = age
        self.company_Person = company_Person
        self.company_Person5 = company_Person5
        self.company_Person3 = company_Person3
        
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def company_Person(self):
        return self.__company_Person

    @company_Person.setter
    def company_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Person__company_Person", None)
        self.__company_Person = value
        
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

    @property
    def company_Person3(self):
        return self.__company_Person3

    @company_Person3.setter
    def company_Person3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Person__company_Person3", None)
        self.__company_Person3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Person5"):
                opp_val = getattr(old_value, "company_Person5", None)
                if opp_val == self:
                    setattr(old_value, "company_Person5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Person5"):
                opp_val = getattr(value, "company_Person5", None)
                setattr(value, "company_Person5", self)

    @property
    def company_Person5(self):
        return self.__company_Person5

    @company_Person5.setter
    def company_Person5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Person__company_Person5", None)
        self.__company_Person5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Person3"):
                opp_val = getattr(old_value, "company_Person3", None)
                if opp_val == self:
                    setattr(old_value, "company_Person3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Person3"):
                opp_val = getattr(value, "company_Person3", None)
                setattr(value, "company_Person3", self)

class company_Company(NamedElement):

    pass