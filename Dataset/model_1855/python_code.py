from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class addressbook_BookVersion:

    def __init__(self, id: int, addressbook_BookVersion: "addressbook_Repository" = None, addressbook_BookVersion8: "addressbook_AddressBook" = None):
        self.id = id
        self.addressbook_BookVersion = addressbook_BookVersion
        self.addressbook_BookVersion8 = addressbook_BookVersion8
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def addressbook_BookVersion(self):
        return self.__addressbook_BookVersion

    @addressbook_BookVersion.setter
    def addressbook_BookVersion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_BookVersion__addressbook_BookVersion", None)
        self.__addressbook_BookVersion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "addressbook_Repository6"):
                opp_val = getattr(old_value, "addressbook_Repository6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "addressbook_Repository6"):
                opp_val = getattr(value, "addressbook_Repository6", None)
                if opp_val is None:
                    setattr(value, "addressbook_Repository6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def addressbook_BookVersion8(self):
        return self.__addressbook_BookVersion8

    @addressbook_BookVersion8.setter
    def addressbook_BookVersion8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_BookVersion__addressbook_BookVersion8", None)
        self.__addressbook_BookVersion8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "addressbook_AddressBook9"):
                opp_val = getattr(old_value, "addressbook_AddressBook9", None)
                if opp_val == self:
                    setattr(old_value, "addressbook_AddressBook9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "addressbook_AddressBook9"):
                opp_val = getattr(value, "addressbook_AddressBook9", None)
                setattr(value, "addressbook_AddressBook9", self)

class addressbook_Repository:

    def __init__(self, addressbook_Repository: "addressbook_AddressBook" = None, addressbook_Repository6: set["addressbook_BookVersion"] = None):
        self.addressbook_Repository = addressbook_Repository
        self.addressbook_Repository6 = addressbook_Repository6 if addressbook_Repository6 is not None else set()
        
    @property
    def addressbook_Repository(self):
        return self.__addressbook_Repository

    @addressbook_Repository.setter
    def addressbook_Repository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Repository__addressbook_Repository", None)
        self.__addressbook_Repository = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "addressbook_AddressBook4"):
                opp_val = getattr(old_value, "addressbook_AddressBook4", None)
                if opp_val == self:
                    setattr(old_value, "addressbook_AddressBook4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "addressbook_AddressBook4"):
                opp_val = getattr(value, "addressbook_AddressBook4", None)
                setattr(value, "addressbook_AddressBook4", self)

    @property
    def addressbook_Repository6(self):
        return self.__addressbook_Repository6

    @addressbook_Repository6.setter
    def addressbook_Repository6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Repository__addressbook_Repository6", None)
        self.__addressbook_Repository6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "addressbook_BookVersion"):
                    opp_val = getattr(item, "addressbook_BookVersion", None)
                    
                    if opp_val == self:
                        setattr(item, "addressbook_BookVersion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "addressbook_BookVersion"):
                    opp_val = getattr(item, "addressbook_BookVersion", None)
                    
                    setattr(item, "addressbook_BookVersion", self)
                    

    def checkout(self, id: int) -> str:
        # TODO: Implement checkout method
        pass

    def checkin(self):
        # TODO: Implement checkin method
        pass

class addressbook_AddressBook:

    pass
class addressbook_People:

    def __init__(self, name: str, addressbook_People: set["addressbook_Contact"] = None, addressbook_People2: "addressbook_AddressBook" = None):
        self.name = name
        self.addressbook_People = addressbook_People if addressbook_People is not None else set()
        self.addressbook_People2 = addressbook_People2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def addressbook_People2(self):
        return self.__addressbook_People2

    @addressbook_People2.setter
    def addressbook_People2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_People__addressbook_People2", None)
        self.__addressbook_People2 = value
        
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
    def addressbook_People(self):
        return self.__addressbook_People

    @addressbook_People.setter
    def addressbook_People(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_People__addressbook_People", None)
        self.__addressbook_People = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "addressbook_Contact"):
                    opp_val = getattr(item, "addressbook_Contact", None)
                    
                    if opp_val == self:
                        setattr(item, "addressbook_Contact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "addressbook_Contact"):
                    opp_val = getattr(item, "addressbook_Contact", None)
                    
                    setattr(item, "addressbook_Contact", self)
                    

class Contact:

    pass
class addressbook_Office(Contact):

    def __init__(self, company: str):
        self.company = company
        
    @property
    def company(self) -> str:
        return self.__company

    @company.setter
    def company(self, company: str):
        self.__company = company

class addressbook_Electronic(Contact):

    def __init__(self, email: str, website: str):
        self.email = email
        self.website = website
        
    @property
    def website(self) -> str:
        return self.__website

    @website.setter
    def website(self, website: str):
        self.__website = website

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

class addressbook_Contact(ABC):

    pass