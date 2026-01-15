from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class addressbook_Entry(ABC):

    def __init__(self, id: int, Entry: "addressbook_Category" = None, entries: "addressbook_Category" = None):
        self.id = id
        self.Entry = Entry
        self.entries = entries
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def entries(self):
        return self.__entries

    @entries.setter
    def entries(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Entry__entries", None)
        self.__entries = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Category4"):
                opp_val = getattr(old_value, "Category4", None)
                if opp_val == self:
                    setattr(old_value, "Category4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Category4"):
                opp_val = getattr(value, "Category4", None)
                setattr(value, "Category4", self)

    @property
    def Entry(self):
        return self.__Entry

    @Entry.setter
    def Entry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Entry__Entry", None)
        self.__Entry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category"):
                opp_val = getattr(old_value, "category", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category"):
                opp_val = getattr(value, "category", None)
                if opp_val is None:
                    setattr(value, "category", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Entry:

    pass
class addressbook_Contact(Entry):

    def __init__(self, firstName: str, lastName: str, email: str, employees: set["addressbook_Organization"] = None, Contact: "addressbook_Organization" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.employees = employees if employees is not None else set()
        self.Contact = Contact
        
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def Contact(self):
        return self.__Contact

    @Contact.setter
    def Contact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Contact__Contact", None)
        self.__Contact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employers"):
                opp_val = getattr(old_value, "employers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employers"):
                opp_val = getattr(value, "employers", None)
                if opp_val is None:
                    setattr(value, "employers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Contact__employees", None)
        self.__employees = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Organization"):
                    opp_val = getattr(item, "Organization", None)
                    
                    if opp_val == self:
                        setattr(item, "Organization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Organization"):
                    opp_val = getattr(item, "Organization", None)
                    
                    setattr(item, "Organization", self)
                    

class NamedElement:

    pass
class addressbook_Category(NamedElement):

    pass
class addressbook_Organization(NamedElement, Entry):

    def __init__(self, homepage: str, Organization: "addressbook_Contact" = None, employers: set["addressbook_Contact"] = None):
        self.homepage = homepage
        self.Organization = Organization
        self.employers = employers if employers is not None else set()
        
    @property
    def homepage(self) -> str:
        return self.__homepage

    @homepage.setter
    def homepage(self, homepage: str):
        self.__homepage = homepage

    @property
    def employers(self):
        return self.__employers

    @employers.setter
    def employers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Organization__employers", None)
        self.__employers = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Contact"):
                    opp_val = getattr(item, "Contact", None)
                    
                    if opp_val == self:
                        setattr(item, "Contact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Contact"):
                    opp_val = getattr(item, "Contact", None)
                    
                    setattr(item, "Contact", self)
                    

    @property
    def Organization(self):
        return self.__Organization

    @Organization.setter
    def Organization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Organization__Organization", None)
        self.__Organization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employees"):
                opp_val = getattr(old_value, "employees", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employees"):
                opp_val = getattr(value, "employees", None)
                if opp_val is None:
                    setattr(value, "employees", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class addressbook_AddressBook(NamedElement):

    pass
class addressbook_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
