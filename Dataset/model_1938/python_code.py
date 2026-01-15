from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class AddressType(Enum):
    PRIVATE = "PRIVATE"
    BUSINESS = "BUSINESS"
    DELIVERY = "DELIVERY"


############################################
# Definition of Classes
############################################

class addressbook_FederalState:

    def __init__(self, name: str, FederalState: "addressbook_Country" = None, federalStates: "addressbook_Country" = None, addressbook_FederalState: "addressbook_Address" = None):
        self.name = name
        self.FederalState = FederalState
        self.federalStates = federalStates
        self.addressbook_FederalState = addressbook_FederalState
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def addressbook_FederalState(self):
        return self.__addressbook_FederalState

    @addressbook_FederalState.setter
    def addressbook_FederalState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_FederalState__addressbook_FederalState", None)
        self.__addressbook_FederalState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "addressbook_Address7"):
                opp_val = getattr(old_value, "addressbook_Address7", None)
                if opp_val == self:
                    setattr(old_value, "addressbook_Address7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "addressbook_Address7"):
                opp_val = getattr(value, "addressbook_Address7", None)
                setattr(value, "addressbook_Address7", self)

    @property
    def FederalState(self):
        return self.__FederalState

    @FederalState.setter
    def FederalState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_FederalState__FederalState", None)
        self.__FederalState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "country"):
                opp_val = getattr(old_value, "country", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "country"):
                opp_val = getattr(value, "country", None)
                if opp_val is None:
                    setattr(value, "country", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def federalStates(self):
        return self.__federalStates

    @federalStates.setter
    def federalStates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_FederalState__federalStates", None)
        self.__federalStates = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Country"):
                opp_val = getattr(old_value, "Country", None)
                if opp_val == self:
                    setattr(old_value, "Country", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Country"):
                opp_val = getattr(value, "Country", None)
                setattr(value, "Country", self)

class addressbook_Person:

    def __init__(self, firstname: str, lastname: str, person: set["addressbook_Address"] = None, persons: "addressbook_AddressBook" = None, Person: "addressbook_AddressBook" = None, Person9: "addressbook_Address" = None):
        self.firstname = firstname
        self.lastname = lastname
        self.person = person if person is not None else set()
        self.persons = persons
        self.Person = Person
        self.Person9 = Person9
        
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
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "addressBook"):
                opp_val = getattr(old_value, "addressBook", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "addressBook"):
                opp_val = getattr(value, "addressBook", None)
                if opp_val is None:
                    setattr(value, "addressBook", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def person(self):
        return self.__person

    @person.setter
    def person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Person__person", None)
        self.__person = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Address"):
                    opp_val = getattr(item, "Address", None)
                    
                    if opp_val == self:
                        setattr(item, "Address", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Address"):
                    opp_val = getattr(item, "Address", None)
                    
                    setattr(item, "Address", self)
                    

    @property
    def persons(self):
        return self.__persons

    @persons.setter
    def persons(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Person__persons", None)
        self.__persons = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AddressBook"):
                opp_val = getattr(old_value, "AddressBook", None)
                if opp_val == self:
                    setattr(old_value, "AddressBook", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AddressBook"):
                opp_val = getattr(value, "AddressBook", None)
                setattr(value, "AddressBook", self)

    @property
    def Person9(self):
        return self.__Person9

    @Person9.setter
    def Person9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Person__Person9", None)
        self.__Person9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "addresses"):
                opp_val = getattr(old_value, "addresses", None)
                if opp_val == self:
                    setattr(old_value, "addresses", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "addresses"):
                opp_val = getattr(value, "addresses", None)
                setattr(value, "addresses", self)

class addressbook_AddressBook:

    pass
class addressbook_Address:

    def __init__(self, street: str, zip: str, city: str, type: str, Address: "addressbook_Person" = None, addresses: "addressbook_Person" = None, addressbook_Address: "addressbook_Country" = None, addressbook_Address7: "addressbook_FederalState" = None):
        self.street = street
        self.zip = zip
        self.city = city
        self.type = type
        self.Address = Address
        self.addresses = addresses
        self.addressbook_Address = addressbook_Address
        self.addressbook_Address7 = addressbook_Address7
        
    @property
    def zip(self) -> str:
        return self.__zip

    @zip.setter
    def zip(self, zip: str):
        self.__zip = zip

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def addressbook_Address7(self):
        return self.__addressbook_Address7

    @addressbook_Address7.setter
    def addressbook_Address7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Address__addressbook_Address7", None)
        self.__addressbook_Address7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "addressbook_FederalState"):
                opp_val = getattr(old_value, "addressbook_FederalState", None)
                if opp_val == self:
                    setattr(old_value, "addressbook_FederalState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "addressbook_FederalState"):
                opp_val = getattr(value, "addressbook_FederalState", None)
                setattr(value, "addressbook_FederalState", self)

    @property
    def addressbook_Address(self):
        return self.__addressbook_Address

    @addressbook_Address.setter
    def addressbook_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Address__addressbook_Address", None)
        self.__addressbook_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "addressbook_Country5"):
                opp_val = getattr(old_value, "addressbook_Country5", None)
                if opp_val == self:
                    setattr(old_value, "addressbook_Country5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "addressbook_Country5"):
                opp_val = getattr(value, "addressbook_Country5", None)
                setattr(value, "addressbook_Country5", self)

    @property
    def Address(self):
        return self.__Address

    @Address.setter
    def Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Address__Address", None)
        self.__Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "person"):
                opp_val = getattr(old_value, "person", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "person"):
                opp_val = getattr(value, "person", None)
                if opp_val is None:
                    setattr(value, "person", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def addresses(self):
        return self.__addresses

    @addresses.setter
    def addresses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Address__addresses", None)
        self.__addresses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person9"):
                opp_val = getattr(old_value, "Person9", None)
                if opp_val == self:
                    setattr(old_value, "Person9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person9"):
                opp_val = getattr(value, "Person9", None)
                setattr(value, "Person9", self)

class addressbook_Country:

    def __init__(self, name: str, addressbook_Country: "addressbook_AddressBook" = None, country: set["addressbook_FederalState"] = None, addressbook_Country12: "addressbook_AddressBook" = None, Country: "addressbook_FederalState" = None, addressbook_Country5: "addressbook_Address" = None):
        self.name = name
        self.addressbook_Country = addressbook_Country
        self.country = country if country is not None else set()
        self.addressbook_Country12 = addressbook_Country12
        self.Country = Country
        self.addressbook_Country5 = addressbook_Country5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Country(self):
        return self.__Country

    @Country.setter
    def Country(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Country__Country", None)
        self.__Country = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "federalStates"):
                opp_val = getattr(old_value, "federalStates", None)
                if opp_val == self:
                    setattr(old_value, "federalStates", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "federalStates"):
                opp_val = getattr(value, "federalStates", None)
                setattr(value, "federalStates", self)

    @property
    def addressbook_Country12(self):
        return self.__addressbook_Country12

    @addressbook_Country12.setter
    def addressbook_Country12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Country__addressbook_Country12", None)
        self.__addressbook_Country12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "addressbook_AddressBook13"):
                opp_val = getattr(old_value, "addressbook_AddressBook13", None)
                if opp_val == self:
                    setattr(old_value, "addressbook_AddressBook13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "addressbook_AddressBook13"):
                opp_val = getattr(value, "addressbook_AddressBook13", None)
                setattr(value, "addressbook_AddressBook13", self)

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Country__country", None)
        self.__country = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FederalState"):
                    opp_val = getattr(item, "FederalState", None)
                    
                    if opp_val == self:
                        setattr(item, "FederalState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FederalState"):
                    opp_val = getattr(item, "FederalState", None)
                    
                    setattr(item, "FederalState", self)
                    

    @property
    def addressbook_Country(self):
        return self.__addressbook_Country

    @addressbook_Country.setter
    def addressbook_Country(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Country__addressbook_Country", None)
        self.__addressbook_Country = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "addressbook_AddressBook"):
                opp_val = getattr(old_value, "addressbook_AddressBook", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "addressbook_AddressBook"):
                opp_val = getattr(value, "addressbook_AddressBook", None)
                if opp_val is None:
                    setattr(value, "addressbook_AddressBook", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def addressbook_Country5(self):
        return self.__addressbook_Country5

    @addressbook_Country5.setter
    def addressbook_Country5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Country__addressbook_Country5", None)
        self.__addressbook_Country5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "addressbook_Address"):
                opp_val = getattr(old_value, "addressbook_Address", None)
                if opp_val == self:
                    setattr(old_value, "addressbook_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "addressbook_Address"):
                opp_val = getattr(value, "addressbook_Address", None)
                setattr(value, "addressbook_Address", self)
