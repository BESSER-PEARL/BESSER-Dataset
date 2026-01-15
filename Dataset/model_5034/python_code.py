from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class party_CommonObject(ABC):

    pass
class Party:

    pass
class party_Person(Party):

    def __init__(self, title: str):
        self.title = title
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

class Address:

    pass
class party_USAddress(Address):

    def __init__(self, recipient: str, street1: str, street2: str, city: str, state: str, zip: str):
        self.recipient = recipient
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.state = state
        self.zip = zip
        
    @property
    def recipient(self) -> str:
        return self.__recipient

    @recipient.setter
    def recipient(self, recipient: str):
        self.__recipient = recipient

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def street2(self) -> str:
        return self.__street2

    @street2.setter
    def street2(self, street2: str):
        self.__street2 = street2

    @property
    def street1(self) -> str:
        return self.__street1

    @street1.setter
    def street1(self, street1: str):
        self.__street1 = street1

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def zip(self) -> str:
        return self.__zip

    @zip.setter
    def zip(self, zip: str):
        self.__zip = zip

class URL:

    pass
class party_EMail(URL):

    pass
class party_Web(URL):

    pass
class ContactInfo:

    pass
class party_URL(ContactInfo):

    def __init__(self, address: str):
        self.address = address
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

class party_Address(ContactInfo):

    def __init__(self, country: str):
        self.country = country
        
    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

class party_Custom(ContactInfo):

    def __init__(self, location: str):
        self.location = location
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

class party_Phone(ContactInfo):

    def __init__(self, countryCode: str, areaCode: int, number: str):
        self.countryCode = countryCode
        self.areaCode = areaCode
        self.number = number
        
    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def areaCode(self) -> int:
        return self.__areaCode

    @areaCode.setter
    def areaCode(self, areaCode: int):
        self.__areaCode = areaCode

    @property
    def countryCode(self) -> str:
        return self.__countryCode

    @countryCode.setter
    def countryCode(self, countryCode: str):
        self.__countryCode = countryCode

class DateEffectiveObject:

    pass
class party_Role(DateEffectiveObject):

    def __init__(self, name: str, party_Role: set["party_Party"] = None, roles: "party_CommonObject" = None, Role: "party_CommonObject" = None):
        self.name = name
        self.party_Role = party_Role if party_Role is not None else set()
        self.roles = roles
        self.Role = Role
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def roles(self):
        return self.__roles

    @roles.setter
    def roles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_Role__roles", None)
        self.__roles = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CommonObject"):
                opp_val = getattr(old_value, "CommonObject", None)
                if opp_val == self:
                    setattr(old_value, "CommonObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CommonObject"):
                opp_val = getattr(value, "CommonObject", None)
                setattr(value, "CommonObject", self)

    @property
    def party_Role(self):
        return self.__party_Role

    @party_Role.setter
    def party_Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_Role__party_Role", None)
        self.__party_Role = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "party_Party12"):
                    opp_val = getattr(item, "party_Party12", None)
                    
                    if opp_val == self:
                        setattr(item, "party_Party12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "party_Party12"):
                    opp_val = getattr(item, "party_Party12", None)
                    
                    setattr(item, "party_Party12", self)
                    

    @property
    def Role(self):
        return self.__Role

    @Role.setter
    def Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_Role__Role", None)
        self.__Role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner15"):
                opp_val = getattr(old_value, "owner15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner15"):
                opp_val = getattr(value, "owner15", None)
                if opp_val is None:
                    setattr(value, "owner15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class party_MatrixRelationship(DateEffectiveObject):

    def __init__(self, name: str, party_MatrixRelationship: "party_Organization" = None, party_MatrixRelationship17: "party_Party" = None):
        self.name = name
        self.party_MatrixRelationship = party_MatrixRelationship
        self.party_MatrixRelationship17 = party_MatrixRelationship17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def party_MatrixRelationship17(self):
        return self.__party_MatrixRelationship17

    @party_MatrixRelationship17.setter
    def party_MatrixRelationship17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_MatrixRelationship__party_MatrixRelationship17", None)
        self.__party_MatrixRelationship17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "party_Party18"):
                opp_val = getattr(old_value, "party_Party18", None)
                if opp_val == self:
                    setattr(old_value, "party_Party18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "party_Party18"):
                opp_val = getattr(value, "party_Party18", None)
                setattr(value, "party_Party18", self)

    @property
    def party_MatrixRelationship(self):
        return self.__party_MatrixRelationship

    @party_MatrixRelationship.setter
    def party_MatrixRelationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_MatrixRelationship__party_MatrixRelationship", None)
        self.__party_MatrixRelationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "party_Organization10"):
                opp_val = getattr(old_value, "party_Organization10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "party_Organization10"):
                opp_val = getattr(value, "party_Organization10", None)
                if opp_val is None:
                    setattr(value, "party_Organization10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class party_Tag:

    def __init__(self, name: str, value: str, comment: str, party_Tag: "party_Tagged" = None):
        self.name = name
        self.value = value
        self.comment = comment
        self.party_Tag = party_Tag
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def party_Tag(self):
        return self.__party_Tag

    @party_Tag.setter
    def party_Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_Tag__party_Tag", None)
        self.__party_Tag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "party_Tagged"):
                opp_val = getattr(old_value, "party_Tagged", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "party_Tagged"):
                opp_val = getattr(value, "party_Tagged", None)
                if opp_val is None:
                    setattr(value, "party_Tagged", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class party_Tagged(ABC):

    def __init__(self, comment: str, party_Tagged: set["party_Tag"] = None):
        self.comment = comment
        self.party_Tagged = party_Tagged if party_Tagged is not None else set()
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def party_Tagged(self):
        return self.__party_Tagged

    @party_Tagged.setter
    def party_Tagged(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_Tagged__party_Tagged", None)
        self.__party_Tagged = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "party_Tag"):
                    opp_val = getattr(item, "party_Tag", None)
                    
                    if opp_val == self:
                        setattr(item, "party_Tag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "party_Tag"):
                    opp_val = getattr(item, "party_Tag", None)
                    
                    setattr(item, "party_Tag", self)
                    

class party_Organization(Party):

    def __init__(self, organizationType: str, Organization: "party_Party" = None, parent: set["party_Party"] = None, party_Organization: set["party_Party"] = None, party_Organization10: set["party_MatrixRelationship"] = None):
        self.organizationType = organizationType
        self.Organization = Organization
        self.parent = parent if parent is not None else set()
        self.party_Organization = party_Organization if party_Organization is not None else set()
        self.party_Organization10 = party_Organization10 if party_Organization10 is not None else set()
        
    @property
    def organizationType(self) -> str:
        return self.__organizationType

    @organizationType.setter
    def organizationType(self, organizationType: str):
        self.__organizationType = organizationType

    @property
    def Organization(self):
        return self.__Organization

    @Organization.setter
    def Organization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_Organization__Organization", None)
        self.__Organization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if opp_val == self:
                    setattr(old_value, "children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                setattr(value, "children", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_Organization__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Party6"):
                    opp_val = getattr(item, "Party6", None)
                    
                    if opp_val == self:
                        setattr(item, "Party6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Party6"):
                    opp_val = getattr(item, "Party6", None)
                    
                    setattr(item, "Party6", self)
                    

    @property
    def party_Organization10(self):
        return self.__party_Organization10

    @party_Organization10.setter
    def party_Organization10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_Organization__party_Organization10", None)
        self.__party_Organization10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "party_MatrixRelationship"):
                    opp_val = getattr(item, "party_MatrixRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "party_MatrixRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "party_MatrixRelationship"):
                    opp_val = getattr(item, "party_MatrixRelationship", None)
                    
                    setattr(item, "party_MatrixRelationship", self)
                    

    @property
    def party_Organization(self):
        return self.__party_Organization

    @party_Organization.setter
    def party_Organization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_Organization__party_Organization", None)
        self.__party_Organization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "party_Party8"):
                    opp_val = getattr(item, "party_Party8", None)
                    
                    if opp_val == self:
                        setattr(item, "party_Party8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "party_Party8"):
                    opp_val = getattr(item, "party_Party8", None)
                    
                    setattr(item, "party_Party8", self)
                    

class party_Identity:

    def __init__(self, type: str, value: str, comment: str, party_Identity: "party_Party" = None):
        self.type = type
        self.value = value
        self.comment = comment
        self.party_Identity = party_Identity
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def party_Identity(self):
        return self.__party_Identity

    @party_Identity.setter
    def party_Identity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_Identity__party_Identity", None)
        self.__party_Identity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "party_Party"):
                opp_val = getattr(old_value, "party_Party", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "party_Party"):
                opp_val = getattr(value, "party_Party", None)
                if opp_val is None:
                    setattr(value, "party_Party", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class party_ContactInfo(DateEffectiveObject):

    def __init__(self, category: str, ContactInfo: "party_Party" = None, contactInfo: "party_Party" = None):
        self.category = category
        self.ContactInfo = ContactInfo
        self.contactInfo = contactInfo
        
    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def contactInfo(self):
        return self.__contactInfo

    @contactInfo.setter
    def contactInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_ContactInfo__contactInfo", None)
        self.__contactInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Party"):
                opp_val = getattr(old_value, "Party", None)
                if opp_val == self:
                    setattr(old_value, "Party", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Party"):
                opp_val = getattr(value, "Party", None)
                setattr(value, "Party", self)

    @property
    def ContactInfo(self):
        return self.__ContactInfo

    @ContactInfo.setter
    def ContactInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_ContactInfo__ContactInfo", None)
        self.__ContactInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Tagged:

    pass
class party_DateEffectiveObject(Tagged):

    def __init__(self, start: date, end: date):
        self.start = start
        self.end = end
        
    @property
    def end(self) -> date:
        return self.__end

    @end.setter
    def end(self, end: date):
        self.__end = end

    @property
    def start(self) -> date:
        return self.__start

    @start.setter
    def start(self, start: date):
        self.__start = start

    def isEffectiveNow(self) -> bool:
        # TODO: Implement isEffectiveNow method
        pass

    def isEffective(self, date: date) -> bool:
        # TODO: Implement isEffective method
        pass

class party_Party(Tagged):

    def __init__(self, name: str, uid: str, owner: set["party_ContactInfo"] = None, party_Party: set["party_Identity"] = None, children: "party_Organization" = None, Party: "party_ContactInfo" = None, Party6: "party_Organization" = None, party_Party8: "party_Organization" = None, party_Party12: "party_Role" = None, party_Party18: "party_MatrixRelationship" = None):
        self.name = name
        self.uid = uid
        self.owner = owner if owner is not None else set()
        self.party_Party = party_Party if party_Party is not None else set()
        self.children = children
        self.Party = Party
        self.Party6 = Party6
        self.party_Party8 = party_Party8
        self.party_Party12 = party_Party12
        self.party_Party18 = party_Party18
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Party6(self):
        return self.__Party6

    @Party6.setter
    def Party6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_Party__Party6", None)
        self.__Party6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def party_Party18(self):
        return self.__party_Party18

    @party_Party18.setter
    def party_Party18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_Party__party_Party18", None)
        self.__party_Party18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "party_MatrixRelationship17"):
                opp_val = getattr(old_value, "party_MatrixRelationship17", None)
                if opp_val == self:
                    setattr(old_value, "party_MatrixRelationship17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "party_MatrixRelationship17"):
                opp_val = getattr(value, "party_MatrixRelationship17", None)
                setattr(value, "party_MatrixRelationship17", self)

    @property
    def Party(self):
        return self.__Party

    @Party.setter
    def Party(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_Party__Party", None)
        self.__Party = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contactInfo"):
                opp_val = getattr(old_value, "contactInfo", None)
                if opp_val == self:
                    setattr(old_value, "contactInfo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contactInfo"):
                opp_val = getattr(value, "contactInfo", None)
                setattr(value, "contactInfo", self)

    @property
    def party_Party12(self):
        return self.__party_Party12

    @party_Party12.setter
    def party_Party12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_Party__party_Party12", None)
        self.__party_Party12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "party_Role"):
                opp_val = getattr(old_value, "party_Role", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "party_Role"):
                opp_val = getattr(value, "party_Role", None)
                if opp_val is None:
                    setattr(value, "party_Role", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def party_Party8(self):
        return self.__party_Party8

    @party_Party8.setter
    def party_Party8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_Party__party_Party8", None)
        self.__party_Party8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "party_Organization"):
                opp_val = getattr(old_value, "party_Organization", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "party_Organization"):
                opp_val = getattr(value, "party_Organization", None)
                if opp_val is None:
                    setattr(value, "party_Organization", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_Party__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organization"):
                opp_val = getattr(old_value, "Organization", None)
                if opp_val == self:
                    setattr(old_value, "Organization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organization"):
                opp_val = getattr(value, "Organization", None)
                setattr(value, "Organization", self)

    @property
    def party_Party(self):
        return self.__party_Party

    @party_Party.setter
    def party_Party(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_Party__party_Party", None)
        self.__party_Party = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "party_Identity"):
                    opp_val = getattr(item, "party_Identity", None)
                    
                    if opp_val == self:
                        setattr(item, "party_Identity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "party_Identity"):
                    opp_val = getattr(item, "party_Identity", None)
                    
                    setattr(item, "party_Identity", self)
                    

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_party_Party__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContactInfo"):
                    opp_val = getattr(item, "ContactInfo", None)
                    
                    if opp_val == self:
                        setattr(item, "ContactInfo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContactInfo"):
                    opp_val = getattr(item, "ContactInfo", None)
                    
                    setattr(item, "ContactInfo", self)
                    

    def getPath(self) -> str:
        # TODO: Implement getPath method
        pass

    def setExternalParent(self, externalParent: str):
        # TODO: Implement setExternalParent method
        pass
