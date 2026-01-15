from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ContactType(Enum):
    PHONE = "PHONE"
    EMAIL = "EMAIL"


############################################
# Definition of Classes
############################################

class test_Address:

    def __init__(self, street: str, city: str, test_Address: "test_Person" = None):
        self.street = street
        self.city = city
        self.test_Address = test_Address
        
    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def test_Address(self):
        return self.__test_Address

    @test_Address.setter
    def test_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Address__test_Address", None)
        self.__test_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_Person"):
                opp_val = getattr(old_value, "test_Person", None)
                if opp_val == self:
                    setattr(old_value, "test_Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_Person"):
                opp_val = getattr(value, "test_Person", None)
                setattr(value, "test_Person", self)

class test_Contact:

    def __init__(self, value: str, type: str, test_Contact: "test_Person" = None):
        self.value = value
        self.type = type
        self.test_Contact = test_Contact
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def test_Contact(self):
        return self.__test_Contact

    @test_Contact.setter
    def test_Contact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Contact__test_Contact", None)
        self.__test_Contact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_Person2"):
                opp_val = getattr(old_value, "test_Person2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_Person2"):
                opp_val = getattr(value, "test_Person2", None)
                if opp_val is None:
                    setattr(value, "test_Person2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test_Person:

    def __init__(self, firstname: str, lastname: str, test_Person2: set["test_Contact"] = None, test_Person: "test_Address" = None):
        self.firstname = firstname
        self.lastname = lastname
        self.test_Person2 = test_Person2 if test_Person2 is not None else set()
        self.test_Person = test_Person
        
    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def test_Person(self):
        return self.__test_Person

    @test_Person.setter
    def test_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Person__test_Person", None)
        self.__test_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_Address"):
                opp_val = getattr(old_value, "test_Address", None)
                if opp_val == self:
                    setattr(old_value, "test_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_Address"):
                opp_val = getattr(value, "test_Address", None)
                setattr(value, "test_Address", self)

    @property
    def test_Person2(self):
        return self.__test_Person2

    @test_Person2.setter
    def test_Person2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Person__test_Person2", None)
        self.__test_Person2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_Contact"):
                    opp_val = getattr(item, "test_Contact", None)
                    
                    if opp_val == self:
                        setattr(item, "test_Contact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_Contact"):
                    opp_val = getattr(item, "test_Contact", None)
                    
                    setattr(item, "test_Contact", self)
                    
