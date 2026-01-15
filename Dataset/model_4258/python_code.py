from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Person:

    pass
class attroverridesecondarytable_NonEmployee(Person):

    pass
class attroverridesecondarytable_Employee(Person):

    def __init__(self, employeeNumber: str, attroverridesecondarytable_Employee: "attroverridesecondarytable_Address" = None):
        self.employeeNumber = employeeNumber
        self.attroverridesecondarytable_Employee = attroverridesecondarytable_Employee
        
    @property
    def employeeNumber(self) -> str:
        return self.__employeeNumber

    @employeeNumber.setter
    def employeeNumber(self, employeeNumber: str):
        self.__employeeNumber = employeeNumber

    @property
    def attroverridesecondarytable_Employee(self):
        return self.__attroverridesecondarytable_Employee

    @attroverridesecondarytable_Employee.setter
    def attroverridesecondarytable_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attroverridesecondarytable_Employee__attroverridesecondarytable_Employee", None)
        self.__attroverridesecondarytable_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attroverridesecondarytable_Address2"):
                opp_val = getattr(old_value, "attroverridesecondarytable_Address2", None)
                if opp_val == self:
                    setattr(old_value, "attroverridesecondarytable_Address2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attroverridesecondarytable_Address2"):
                opp_val = getattr(value, "attroverridesecondarytable_Address2", None)
                setattr(value, "attroverridesecondarytable_Address2", self)

class attroverridesecondarytable_Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class attroverridesecondarytable_Country:

    def __init__(self, name: str, attroverridesecondarytable_Country: "attroverridesecondarytable_Address" = None):
        self.name = name
        self.attroverridesecondarytable_Country = attroverridesecondarytable_Country
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def attroverridesecondarytable_Country(self):
        return self.__attroverridesecondarytable_Country

    @attroverridesecondarytable_Country.setter
    def attroverridesecondarytable_Country(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attroverridesecondarytable_Country__attroverridesecondarytable_Country", None)
        self.__attroverridesecondarytable_Country = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attroverridesecondarytable_Address"):
                opp_val = getattr(old_value, "attroverridesecondarytable_Address", None)
                if opp_val == self:
                    setattr(old_value, "attroverridesecondarytable_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attroverridesecondarytable_Address"):
                opp_val = getattr(value, "attroverridesecondarytable_Address", None)
                setattr(value, "attroverridesecondarytable_Address", self)

class attroverridesecondarytable_Address:

    def __init__(self, name: str, street: str, city: str, attroverridesecondarytable_Address: "attroverridesecondarytable_Country" = None, attroverridesecondarytable_Address2: "attroverridesecondarytable_Employee" = None, attroverridesecondarytable_Address4: "attroverridesecondarytable_NonEmployee" = None):
        self.name = name
        self.street = street
        self.city = city
        self.attroverridesecondarytable_Address = attroverridesecondarytable_Address
        self.attroverridesecondarytable_Address2 = attroverridesecondarytable_Address2
        self.attroverridesecondarytable_Address4 = attroverridesecondarytable_Address4
        
    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def attroverridesecondarytable_Address(self):
        return self.__attroverridesecondarytable_Address

    @attroverridesecondarytable_Address.setter
    def attroverridesecondarytable_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attroverridesecondarytable_Address__attroverridesecondarytable_Address", None)
        self.__attroverridesecondarytable_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attroverridesecondarytable_Country"):
                opp_val = getattr(old_value, "attroverridesecondarytable_Country", None)
                if opp_val == self:
                    setattr(old_value, "attroverridesecondarytable_Country", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attroverridesecondarytable_Country"):
                opp_val = getattr(value, "attroverridesecondarytable_Country", None)
                setattr(value, "attroverridesecondarytable_Country", self)

    @property
    def attroverridesecondarytable_Address4(self):
        return self.__attroverridesecondarytable_Address4

    @attroverridesecondarytable_Address4.setter
    def attroverridesecondarytable_Address4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attroverridesecondarytable_Address__attroverridesecondarytable_Address4", None)
        self.__attroverridesecondarytable_Address4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attroverridesecondarytable_NonEmployee"):
                opp_val = getattr(old_value, "attroverridesecondarytable_NonEmployee", None)
                if opp_val == self:
                    setattr(old_value, "attroverridesecondarytable_NonEmployee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attroverridesecondarytable_NonEmployee"):
                opp_val = getattr(value, "attroverridesecondarytable_NonEmployee", None)
                setattr(value, "attroverridesecondarytable_NonEmployee", self)

    @property
    def attroverridesecondarytable_Address2(self):
        return self.__attroverridesecondarytable_Address2

    @attroverridesecondarytable_Address2.setter
    def attroverridesecondarytable_Address2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attroverridesecondarytable_Address__attroverridesecondarytable_Address2", None)
        self.__attroverridesecondarytable_Address2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attroverridesecondarytable_Employee"):
                opp_val = getattr(old_value, "attroverridesecondarytable_Employee", None)
                if opp_val == self:
                    setattr(old_value, "attroverridesecondarytable_Employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attroverridesecondarytable_Employee"):
                opp_val = getattr(value, "attroverridesecondarytable_Employee", None)
                setattr(value, "attroverridesecondarytable_Employee", self)
