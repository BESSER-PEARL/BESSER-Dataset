from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RelationshipType(Enum):
    Boss = "Boss"
    Employee = "Employee"
    Subdivision = "Subdivision"
    CoWorker = "CoWorker"
class NoteType(Enum):
    MEETING = "MEETING"
    CALL = "CALL"
    EMAIL = "EMAIL"


############################################
# Definition of Classes
############################################

class addressbook_AddressBook:

    pass
class Contact:

    pass
class addressbook_Company(Contact):

    def __init__(self, Industry: str):
        self.Industry = Industry
        
    @property
    def Industry(self) -> str:
        return self.__Industry

    @Industry.setter
    def Industry(self, Industry: str):
        self.__Industry = Industry

class addressbook_Person(Contact):

    def __init__(self, Title: str):
        self.Title = Title
        
    @property
    def Title(self) -> str:
        return self.__Title

    @Title.setter
    def Title(self, Title: str):
        self.__Title = Title

class addressbook_Note:

    def __init__(self, Author: str, Time: date, Type: str, Comment: str, addressbook_Note: "addressbook_Contact" = None):
        self.Author = Author
        self.Time = Time
        self.Type = Type
        self.Comment = Comment
        self.addressbook_Note = addressbook_Note
        
    @property
    def Comment(self) -> str:
        return self.__Comment

    @Comment.setter
    def Comment(self, Comment: str):
        self.__Comment = Comment

    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Author(self) -> str:
        return self.__Author

    @Author.setter
    def Author(self, Author: str):
        self.__Author = Author

    @property
    def Time(self) -> date:
        return self.__Time

    @Time.setter
    def Time(self, Time: date):
        self.__Time = Time

    @property
    def addressbook_Note(self):
        return self.__addressbook_Note

    @addressbook_Note.setter
    def addressbook_Note(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Note__addressbook_Note", None)
        self.__addressbook_Note = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "addressbook_Contact8"):
                opp_val = getattr(old_value, "addressbook_Contact8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "addressbook_Contact8"):
                opp_val = getattr(value, "addressbook_Contact8", None)
                if opp_val is None:
                    setattr(value, "addressbook_Contact8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class addressbook_Relationship:

    def __init__(self, Type: str, isRelated: "addressbook_Contact" = None, relates: "addressbook_Contact" = None, Relationship: "addressbook_Contact" = None, Relationship6: "addressbook_Contact" = None):
        self.Type = Type
        self.isRelated = isRelated
        self.relates = relates
        self.Relationship = Relationship
        self.Relationship6 = Relationship6
        
    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Relationship6(self):
        return self.__Relationship6

    @Relationship6.setter
    def Relationship6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Relationship__Relationship6", None)
        self.__Relationship6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def isRelated(self):
        return self.__isRelated

    @isRelated.setter
    def isRelated(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Relationship__isRelated", None)
        self.__isRelated = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Contact"):
                opp_val = getattr(old_value, "Contact", None)
                if opp_val == self:
                    setattr(old_value, "Contact", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Contact"):
                opp_val = getattr(value, "Contact", None)
                setattr(value, "Contact", self)

    @property
    def relates(self):
        return self.__relates

    @relates.setter
    def relates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Relationship__relates", None)
        self.__relates = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Contact13"):
                opp_val = getattr(old_value, "Contact13", None)
                if opp_val == self:
                    setattr(old_value, "Contact13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Contact13"):
                opp_val = getattr(value, "Contact13", None)
                setattr(value, "Contact13", self)

    @property
    def Relationship(self):
        return self.__Relationship

    @Relationship.setter
    def Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Relationship__Relationship", None)
        self.__Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class addressbook_Address:

    def __init__(self, City: str, Street: str, HouseNr: str, addressbook_Address: "addressbook_Contact" = None):
        self.City = City
        self.Street = Street
        self.HouseNr = HouseNr
        self.addressbook_Address = addressbook_Address
        
    @property
    def HouseNr(self) -> str:
        return self.__HouseNr

    @HouseNr.setter
    def HouseNr(self, HouseNr: str):
        self.__HouseNr = HouseNr

    @property
    def City(self) -> str:
        return self.__City

    @City.setter
    def City(self, City: str):
        self.__City = City

    @property
    def Street(self) -> str:
        return self.__Street

    @Street.setter
    def Street(self, Street: str):
        self.__Street = Street

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
            if hasattr(old_value, "addressbook_Contact"):
                opp_val = getattr(old_value, "addressbook_Contact", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "addressbook_Contact"):
                opp_val = getattr(value, "addressbook_Contact", None)
                if opp_val is None:
                    setattr(value, "addressbook_Contact", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class addressbook_Contact(ABC):

    def __init__(self, Name: str, Phone: str, Website: str, EMail: str, addressbook_Contact10: "addressbook_AddressBook" = None, Contact: "addressbook_Relationship" = None, Contact13: "addressbook_Relationship" = None, addressbook_Contact: set["addressbook_Address"] = None, addressbook_Contact3: "addressbook_Contact" = None, addressbook_Contact1: set["addressbook_Contact"] = None, source: set["addressbook_Relationship"] = None, target: set["addressbook_Relationship"] = None, addressbook_Contact8: set["addressbook_Note"] = None):
        self.Name = Name
        self.Phone = Phone
        self.Website = Website
        self.EMail = EMail
        self.addressbook_Contact10 = addressbook_Contact10
        self.Contact = Contact
        self.Contact13 = Contact13
        self.addressbook_Contact = addressbook_Contact if addressbook_Contact is not None else set()
        self.addressbook_Contact3 = addressbook_Contact3
        self.addressbook_Contact1 = addressbook_Contact1 if addressbook_Contact1 is not None else set()
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.addressbook_Contact8 = addressbook_Contact8 if addressbook_Contact8 is not None else set()
        
    @property
    def Phone(self) -> str:
        return self.__Phone

    @Phone.setter
    def Phone(self, Phone: str):
        self.__Phone = Phone

    @property
    def Website(self) -> str:
        return self.__Website

    @Website.setter
    def Website(self, Website: str):
        self.__Website = Website

    @property
    def EMail(self) -> str:
        return self.__EMail

    @EMail.setter
    def EMail(self, EMail: str):
        self.__EMail = EMail

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

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
            if hasattr(old_value, "isRelated"):
                opp_val = getattr(old_value, "isRelated", None)
                if opp_val == self:
                    setattr(old_value, "isRelated", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isRelated"):
                opp_val = getattr(value, "isRelated", None)
                setattr(value, "isRelated", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Contact__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relationship6"):
                    opp_val = getattr(item, "Relationship6", None)
                    
                    if opp_val == self:
                        setattr(item, "Relationship6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relationship6"):
                    opp_val = getattr(item, "Relationship6", None)
                    
                    setattr(item, "Relationship6", self)
                    

    @property
    def addressbook_Contact8(self):
        return self.__addressbook_Contact8

    @addressbook_Contact8.setter
    def addressbook_Contact8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Contact__addressbook_Contact8", None)
        self.__addressbook_Contact8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "addressbook_Note"):
                    opp_val = getattr(item, "addressbook_Note", None)
                    
                    if opp_val == self:
                        setattr(item, "addressbook_Note", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "addressbook_Note"):
                    opp_val = getattr(item, "addressbook_Note", None)
                    
                    setattr(item, "addressbook_Note", self)
                    

    @property
    def addressbook_Contact1(self):
        return self.__addressbook_Contact1

    @addressbook_Contact1.setter
    def addressbook_Contact1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Contact__addressbook_Contact1", None)
        self.__addressbook_Contact1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "addressbook_Contact3"):
                    opp_val = getattr(item, "addressbook_Contact3", None)
                    
                    if opp_val == self:
                        setattr(item, "addressbook_Contact3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "addressbook_Contact3"):
                    opp_val = getattr(item, "addressbook_Contact3", None)
                    
                    setattr(item, "addressbook_Contact3", self)
                    

    @property
    def addressbook_Contact(self):
        return self.__addressbook_Contact

    @addressbook_Contact.setter
    def addressbook_Contact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Contact__addressbook_Contact", None)
        self.__addressbook_Contact = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "addressbook_Address"):
                    opp_val = getattr(item, "addressbook_Address", None)
                    
                    if opp_val == self:
                        setattr(item, "addressbook_Address", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "addressbook_Address"):
                    opp_val = getattr(item, "addressbook_Address", None)
                    
                    setattr(item, "addressbook_Address", self)
                    

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Contact__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relationship"):
                    opp_val = getattr(item, "Relationship", None)
                    
                    if opp_val == self:
                        setattr(item, "Relationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relationship"):
                    opp_val = getattr(item, "Relationship", None)
                    
                    setattr(item, "Relationship", self)
                    

    @property
    def addressbook_Contact10(self):
        return self.__addressbook_Contact10

    @addressbook_Contact10.setter
    def addressbook_Contact10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Contact__addressbook_Contact10", None)
        self.__addressbook_Contact10 = value
        
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
    def addressbook_Contact3(self):
        return self.__addressbook_Contact3

    @addressbook_Contact3.setter
    def addressbook_Contact3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Contact__addressbook_Contact3", None)
        self.__addressbook_Contact3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "addressbook_Contact1"):
                opp_val = getattr(old_value, "addressbook_Contact1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "addressbook_Contact1"):
                opp_val = getattr(value, "addressbook_Contact1", None)
                if opp_val is None:
                    setattr(value, "addressbook_Contact1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Contact13(self):
        return self.__Contact13

    @Contact13.setter
    def Contact13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_addressbook_Contact__Contact13", None)
        self.__Contact13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relates"):
                opp_val = getattr(old_value, "relates", None)
                if opp_val == self:
                    setattr(old_value, "relates", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relates"):
                opp_val = getattr(value, "relates", None)
                setattr(value, "relates", self)
