from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Sexus(Enum):
    male = "male"
    female = "female"
    undefined = "undefined"


############################################
# Definition of Classes
############################################

class gedcoml_Address(ABC):

    def __init__(self, entry: str, exodus: str, gedcoml_Address: "gedcoml_Person" = None):
        self.entry = entry
        self.exodus = exodus
        self.gedcoml_Address = gedcoml_Address
        
    @property
    def exodus(self) -> str:
        return self.__exodus

    @exodus.setter
    def exodus(self, exodus: str):
        self.__exodus = exodus

    @property
    def entry(self) -> str:
        return self.__entry

    @entry.setter
    def entry(self, entry: str):
        self.__entry = entry

    @property
    def gedcoml_Address(self):
        return self.__gedcoml_Address

    @gedcoml_Address.setter
    def gedcoml_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_Address__gedcoml_Address", None)
        self.__gedcoml_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gedcoml_Person35"):
                opp_val = getattr(old_value, "gedcoml_Person35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gedcoml_Person35"):
                opp_val = getattr(value, "gedcoml_Person35", None)
                if opp_val is None:
                    setattr(value, "gedcoml_Person35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Address:

    pass
class gedcoml_PostAddress(Address):

    def __init__(self, street: str, postcode: str, city: str):
        self.street = street
        self.postcode = postcode
        self.city = city
        
    @property
    def postcode(self) -> str:
        return self.__postcode

    @postcode.setter
    def postcode(self, postcode: str):
        self.__postcode = postcode

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

class gedcoml_FamilyBook:

    pass
class gedcoml_Source(ABC):

    pass
class gedcoml_Note:

    def __init__(self, content: str, gedcoml_Note: "gedcoml_BekanntePerson" = None):
        self.content = content
        self.gedcoml_Note = gedcoml_Note
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def gedcoml_Note(self):
        return self.__gedcoml_Note

    @gedcoml_Note.setter
    def gedcoml_Note(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_Note__gedcoml_Note", None)
        self.__gedcoml_Note = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gedcoml_BekanntePerson18"):
                opp_val = getattr(old_value, "gedcoml_BekanntePerson18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gedcoml_BekanntePerson18"):
                opp_val = getattr(value, "gedcoml_BekanntePerson18", None)
                if opp_val is None:
                    setattr(value, "gedcoml_BekanntePerson18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class gedcoml_Married:

    def __init__(self, weddingDay: str, separationDay: str, gedcoml_Married: "gedcoml_BekanntePerson" = None, gedcoml_Married27: "gedcoml_Person" = None):
        self.weddingDay = weddingDay
        self.separationDay = separationDay
        self.gedcoml_Married = gedcoml_Married
        self.gedcoml_Married27 = gedcoml_Married27
        
    @property
    def weddingDay(self) -> str:
        return self.__weddingDay

    @weddingDay.setter
    def weddingDay(self, weddingDay: str):
        self.__weddingDay = weddingDay

    @property
    def separationDay(self) -> str:
        return self.__separationDay

    @separationDay.setter
    def separationDay(self, separationDay: str):
        self.__separationDay = separationDay

    @property
    def gedcoml_Married(self):
        return self.__gedcoml_Married

    @gedcoml_Married.setter
    def gedcoml_Married(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_Married__gedcoml_Married", None)
        self.__gedcoml_Married = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gedcoml_BekanntePerson16"):
                opp_val = getattr(old_value, "gedcoml_BekanntePerson16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gedcoml_BekanntePerson16"):
                opp_val = getattr(value, "gedcoml_BekanntePerson16", None)
                if opp_val is None:
                    setattr(value, "gedcoml_BekanntePerson16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gedcoml_Married27(self):
        return self.__gedcoml_Married27

    @gedcoml_Married27.setter
    def gedcoml_Married27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_Married__gedcoml_Married27", None)
        self.__gedcoml_Married27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gedcoml_Person28"):
                opp_val = getattr(old_value, "gedcoml_Person28", None)
                if opp_val == self:
                    setattr(old_value, "gedcoml_Person28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gedcoml_Person28"):
                opp_val = getattr(value, "gedcoml_Person28", None)
                setattr(value, "gedcoml_Person28", self)

class Source:

    pass
class gedcoml_PersonRef(Source):

    pass
class gedcoml_Others(Source):

    def __init__(self, description: str):
        self.description = description
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class Person:

    pass
class gedcoml_UnbekanntePerson(Person):

    pass
class gedcoml_BekanntePerson(Person):

    def __init__(self, firstName: str, lastName: str, middleName: str, birthDay: str, deathDay: str, birthName: str, gedcoml_BekanntePerson: set["gedcoml_Person"] = None, gedcoml_BekanntePerson31: "gedcoml_Author" = None, gedcoml_BekanntePerson33: "gedcoml_PersonRef" = None, gedcoml_BekanntePerson10: "gedcoml_Person" = None, gedcoml_BekanntePerson13: "gedcoml_Person" = None, gedcoml_BekanntePerson16: set["gedcoml_Married"] = None, gedcoml_BekanntePerson18: set["gedcoml_Note"] = None, gedcoml_BekanntePerson20: set["gedcoml_Source"] = None):
        self.firstName = firstName
        self.lastName = lastName
        self.middleName = middleName
        self.birthDay = birthDay
        self.deathDay = deathDay
        self.birthName = birthName
        self.gedcoml_BekanntePerson = gedcoml_BekanntePerson if gedcoml_BekanntePerson is not None else set()
        self.gedcoml_BekanntePerson31 = gedcoml_BekanntePerson31
        self.gedcoml_BekanntePerson33 = gedcoml_BekanntePerson33
        self.gedcoml_BekanntePerson10 = gedcoml_BekanntePerson10
        self.gedcoml_BekanntePerson13 = gedcoml_BekanntePerson13
        self.gedcoml_BekanntePerson16 = gedcoml_BekanntePerson16 if gedcoml_BekanntePerson16 is not None else set()
        self.gedcoml_BekanntePerson18 = gedcoml_BekanntePerson18 if gedcoml_BekanntePerson18 is not None else set()
        self.gedcoml_BekanntePerson20 = gedcoml_BekanntePerson20 if gedcoml_BekanntePerson20 is not None else set()
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def birthName(self) -> str:
        return self.__birthName

    @birthName.setter
    def birthName(self, birthName: str):
        self.__birthName = birthName

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def birthDay(self) -> str:
        return self.__birthDay

    @birthDay.setter
    def birthDay(self, birthDay: str):
        self.__birthDay = birthDay

    @property
    def deathDay(self) -> str:
        return self.__deathDay

    @deathDay.setter
    def deathDay(self, deathDay: str):
        self.__deathDay = deathDay

    @property
    def middleName(self) -> str:
        return self.__middleName

    @middleName.setter
    def middleName(self, middleName: str):
        self.__middleName = middleName

    @property
    def gedcoml_BekanntePerson13(self):
        return self.__gedcoml_BekanntePerson13

    @gedcoml_BekanntePerson13.setter
    def gedcoml_BekanntePerson13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_BekanntePerson__gedcoml_BekanntePerson13", None)
        self.__gedcoml_BekanntePerson13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gedcoml_Person14"):
                opp_val = getattr(old_value, "gedcoml_Person14", None)
                if opp_val == self:
                    setattr(old_value, "gedcoml_Person14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gedcoml_Person14"):
                opp_val = getattr(value, "gedcoml_Person14", None)
                setattr(value, "gedcoml_Person14", self)

    @property
    def gedcoml_BekanntePerson(self):
        return self.__gedcoml_BekanntePerson

    @gedcoml_BekanntePerson.setter
    def gedcoml_BekanntePerson(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_BekanntePerson__gedcoml_BekanntePerson", None)
        self.__gedcoml_BekanntePerson = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gedcoml_Person8"):
                    opp_val = getattr(item, "gedcoml_Person8", None)
                    
                    if opp_val == self:
                        setattr(item, "gedcoml_Person8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gedcoml_Person8"):
                    opp_val = getattr(item, "gedcoml_Person8", None)
                    
                    setattr(item, "gedcoml_Person8", self)
                    

    @property
    def gedcoml_BekanntePerson33(self):
        return self.__gedcoml_BekanntePerson33

    @gedcoml_BekanntePerson33.setter
    def gedcoml_BekanntePerson33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_BekanntePerson__gedcoml_BekanntePerson33", None)
        self.__gedcoml_BekanntePerson33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gedcoml_PersonRef"):
                opp_val = getattr(old_value, "gedcoml_PersonRef", None)
                if opp_val == self:
                    setattr(old_value, "gedcoml_PersonRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gedcoml_PersonRef"):
                opp_val = getattr(value, "gedcoml_PersonRef", None)
                setattr(value, "gedcoml_PersonRef", self)

    @property
    def gedcoml_BekanntePerson20(self):
        return self.__gedcoml_BekanntePerson20

    @gedcoml_BekanntePerson20.setter
    def gedcoml_BekanntePerson20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_BekanntePerson__gedcoml_BekanntePerson20", None)
        self.__gedcoml_BekanntePerson20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gedcoml_Source"):
                    opp_val = getattr(item, "gedcoml_Source", None)
                    
                    if opp_val == self:
                        setattr(item, "gedcoml_Source", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gedcoml_Source"):
                    opp_val = getattr(item, "gedcoml_Source", None)
                    
                    setattr(item, "gedcoml_Source", self)
                    

    @property
    def gedcoml_BekanntePerson31(self):
        return self.__gedcoml_BekanntePerson31

    @gedcoml_BekanntePerson31.setter
    def gedcoml_BekanntePerson31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_BekanntePerson__gedcoml_BekanntePerson31", None)
        self.__gedcoml_BekanntePerson31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gedcoml_Author30"):
                opp_val = getattr(old_value, "gedcoml_Author30", None)
                if opp_val == self:
                    setattr(old_value, "gedcoml_Author30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gedcoml_Author30"):
                opp_val = getattr(value, "gedcoml_Author30", None)
                setattr(value, "gedcoml_Author30", self)

    @property
    def gedcoml_BekanntePerson16(self):
        return self.__gedcoml_BekanntePerson16

    @gedcoml_BekanntePerson16.setter
    def gedcoml_BekanntePerson16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_BekanntePerson__gedcoml_BekanntePerson16", None)
        self.__gedcoml_BekanntePerson16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gedcoml_Married"):
                    opp_val = getattr(item, "gedcoml_Married", None)
                    
                    if opp_val == self:
                        setattr(item, "gedcoml_Married", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gedcoml_Married"):
                    opp_val = getattr(item, "gedcoml_Married", None)
                    
                    setattr(item, "gedcoml_Married", self)
                    

    @property
    def gedcoml_BekanntePerson10(self):
        return self.__gedcoml_BekanntePerson10

    @gedcoml_BekanntePerson10.setter
    def gedcoml_BekanntePerson10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_BekanntePerson__gedcoml_BekanntePerson10", None)
        self.__gedcoml_BekanntePerson10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gedcoml_Person11"):
                opp_val = getattr(old_value, "gedcoml_Person11", None)
                if opp_val == self:
                    setattr(old_value, "gedcoml_Person11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gedcoml_Person11"):
                opp_val = getattr(value, "gedcoml_Person11", None)
                setattr(value, "gedcoml_Person11", self)

    @property
    def gedcoml_BekanntePerson18(self):
        return self.__gedcoml_BekanntePerson18

    @gedcoml_BekanntePerson18.setter
    def gedcoml_BekanntePerson18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_BekanntePerson__gedcoml_BekanntePerson18", None)
        self.__gedcoml_BekanntePerson18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gedcoml_Note"):
                    opp_val = getattr(item, "gedcoml_Note", None)
                    
                    if opp_val == self:
                        setattr(item, "gedcoml_Note", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gedcoml_Note"):
                    opp_val = getattr(item, "gedcoml_Note", None)
                    
                    setattr(item, "gedcoml_Note", self)
                    

class gedcoml_Person(ABC):

    def __init__(self, id: str, sex: str, gedcoml_Person8: "gedcoml_BekanntePerson" = None, gedcoml_Person: "gedcoml_Family" = None, gedcoml_Person11: "gedcoml_BekanntePerson" = None, gedcoml_Person14: "gedcoml_BekanntePerson" = None, gedcoml_Person28: "gedcoml_Married" = None, gedcoml_Person35: set["gedcoml_Address"] = None):
        self.id = id
        self.sex = sex
        self.gedcoml_Person8 = gedcoml_Person8
        self.gedcoml_Person = gedcoml_Person
        self.gedcoml_Person11 = gedcoml_Person11
        self.gedcoml_Person14 = gedcoml_Person14
        self.gedcoml_Person28 = gedcoml_Person28
        self.gedcoml_Person35 = gedcoml_Person35 if gedcoml_Person35 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def sex(self) -> str:
        return self.__sex

    @sex.setter
    def sex(self, sex: str):
        self.__sex = sex

    @property
    def gedcoml_Person14(self):
        return self.__gedcoml_Person14

    @gedcoml_Person14.setter
    def gedcoml_Person14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_Person__gedcoml_Person14", None)
        self.__gedcoml_Person14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gedcoml_BekanntePerson13"):
                opp_val = getattr(old_value, "gedcoml_BekanntePerson13", None)
                if opp_val == self:
                    setattr(old_value, "gedcoml_BekanntePerson13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gedcoml_BekanntePerson13"):
                opp_val = getattr(value, "gedcoml_BekanntePerson13", None)
                setattr(value, "gedcoml_BekanntePerson13", self)

    @property
    def gedcoml_Person8(self):
        return self.__gedcoml_Person8

    @gedcoml_Person8.setter
    def gedcoml_Person8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_Person__gedcoml_Person8", None)
        self.__gedcoml_Person8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gedcoml_BekanntePerson"):
                opp_val = getattr(old_value, "gedcoml_BekanntePerson", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gedcoml_BekanntePerson"):
                opp_val = getattr(value, "gedcoml_BekanntePerson", None)
                if opp_val is None:
                    setattr(value, "gedcoml_BekanntePerson", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gedcoml_Person28(self):
        return self.__gedcoml_Person28

    @gedcoml_Person28.setter
    def gedcoml_Person28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_Person__gedcoml_Person28", None)
        self.__gedcoml_Person28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gedcoml_Married27"):
                opp_val = getattr(old_value, "gedcoml_Married27", None)
                if opp_val == self:
                    setattr(old_value, "gedcoml_Married27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gedcoml_Married27"):
                opp_val = getattr(value, "gedcoml_Married27", None)
                setattr(value, "gedcoml_Married27", self)

    @property
    def gedcoml_Person11(self):
        return self.__gedcoml_Person11

    @gedcoml_Person11.setter
    def gedcoml_Person11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_Person__gedcoml_Person11", None)
        self.__gedcoml_Person11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gedcoml_BekanntePerson10"):
                opp_val = getattr(old_value, "gedcoml_BekanntePerson10", None)
                if opp_val == self:
                    setattr(old_value, "gedcoml_BekanntePerson10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gedcoml_BekanntePerson10"):
                opp_val = getattr(value, "gedcoml_BekanntePerson10", None)
                setattr(value, "gedcoml_BekanntePerson10", self)

    @property
    def gedcoml_Person(self):
        return self.__gedcoml_Person

    @gedcoml_Person.setter
    def gedcoml_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_Person__gedcoml_Person", None)
        self.__gedcoml_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gedcoml_Family"):
                opp_val = getattr(old_value, "gedcoml_Family", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gedcoml_Family"):
                opp_val = getattr(value, "gedcoml_Family", None)
                if opp_val is None:
                    setattr(value, "gedcoml_Family", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gedcoml_Person35(self):
        return self.__gedcoml_Person35

    @gedcoml_Person35.setter
    def gedcoml_Person35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_Person__gedcoml_Person35", None)
        self.__gedcoml_Person35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gedcoml_Address"):
                    opp_val = getattr(item, "gedcoml_Address", None)
                    
                    if opp_val == self:
                        setattr(item, "gedcoml_Address", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gedcoml_Address"):
                    opp_val = getattr(item, "gedcoml_Address", None)
                    
                    setattr(item, "gedcoml_Address", self)
                    

class gedcoml_Family:

    def __init__(self, name: str, gedcoml_Family: set["gedcoml_Person"] = None, gedcoml_Family5: set["gedcoml_FamilyImport"] = None, gedcoml_Family25: "gedcoml_FamilyImport" = None):
        self.name = name
        self.gedcoml_Family = gedcoml_Family if gedcoml_Family is not None else set()
        self.gedcoml_Family5 = gedcoml_Family5 if gedcoml_Family5 is not None else set()
        self.gedcoml_Family25 = gedcoml_Family25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gedcoml_Family5(self):
        return self.__gedcoml_Family5

    @gedcoml_Family5.setter
    def gedcoml_Family5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_Family__gedcoml_Family5", None)
        self.__gedcoml_Family5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gedcoml_FamilyImport6"):
                    opp_val = getattr(item, "gedcoml_FamilyImport6", None)
                    
                    if opp_val == self:
                        setattr(item, "gedcoml_FamilyImport6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gedcoml_FamilyImport6"):
                    opp_val = getattr(item, "gedcoml_FamilyImport6", None)
                    
                    setattr(item, "gedcoml_FamilyImport6", self)
                    

    @property
    def gedcoml_Family(self):
        return self.__gedcoml_Family

    @gedcoml_Family.setter
    def gedcoml_Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_Family__gedcoml_Family", None)
        self.__gedcoml_Family = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gedcoml_Person"):
                    opp_val = getattr(item, "gedcoml_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "gedcoml_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gedcoml_Person"):
                    opp_val = getattr(item, "gedcoml_Person", None)
                    
                    setattr(item, "gedcoml_Person", self)
                    

    @property
    def gedcoml_Family25(self):
        return self.__gedcoml_Family25

    @gedcoml_Family25.setter
    def gedcoml_Family25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_Family__gedcoml_Family25", None)
        self.__gedcoml_Family25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gedcoml_FamilyImport24"):
                opp_val = getattr(old_value, "gedcoml_FamilyImport24", None)
                if opp_val == self:
                    setattr(old_value, "gedcoml_FamilyImport24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gedcoml_FamilyImport24"):
                opp_val = getattr(value, "gedcoml_FamilyImport24", None)
                setattr(value, "gedcoml_FamilyImport24", self)

class gedcoml_Author:

    def __init__(self, firstName: str, lastName: str, gedcoml_Author: "gedcoml_Projectdescription" = None, gedcoml_Author30: "gedcoml_BekanntePerson" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.gedcoml_Author = gedcoml_Author
        self.gedcoml_Author30 = gedcoml_Author30
        
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
    def gedcoml_Author30(self):
        return self.__gedcoml_Author30

    @gedcoml_Author30.setter
    def gedcoml_Author30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_Author__gedcoml_Author30", None)
        self.__gedcoml_Author30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gedcoml_BekanntePerson31"):
                opp_val = getattr(old_value, "gedcoml_BekanntePerson31", None)
                if opp_val == self:
                    setattr(old_value, "gedcoml_BekanntePerson31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gedcoml_BekanntePerson31"):
                opp_val = getattr(value, "gedcoml_BekanntePerson31", None)
                setattr(value, "gedcoml_BekanntePerson31", self)

    @property
    def gedcoml_Author(self):
        return self.__gedcoml_Author

    @gedcoml_Author.setter
    def gedcoml_Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_Author__gedcoml_Author", None)
        self.__gedcoml_Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gedcoml_Projectdescription2"):
                opp_val = getattr(old_value, "gedcoml_Projectdescription2", None)
                if opp_val == self:
                    setattr(old_value, "gedcoml_Projectdescription2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gedcoml_Projectdescription2"):
                opp_val = getattr(value, "gedcoml_Projectdescription2", None)
                setattr(value, "gedcoml_Projectdescription2", self)

class gedcoml_FamilyImport:

    pass
class gedcoml_Projectdescription:

    def __init__(self, groupId: str, artifactId: str, version: str, publishingDate: str, gedcoml_Projectdescription: set["gedcoml_FamilyImport"] = None, gedcoml_Projectdescription2: "gedcoml_Author" = None, gedcoml_Projectdescription22: "gedcoml_FamilyBook" = None):
        self.groupId = groupId
        self.artifactId = artifactId
        self.version = version
        self.publishingDate = publishingDate
        self.gedcoml_Projectdescription = gedcoml_Projectdescription if gedcoml_Projectdescription is not None else set()
        self.gedcoml_Projectdescription2 = gedcoml_Projectdescription2
        self.gedcoml_Projectdescription22 = gedcoml_Projectdescription22
        
    @property
    def groupId(self) -> str:
        return self.__groupId

    @groupId.setter
    def groupId(self, groupId: str):
        self.__groupId = groupId

    @property
    def publishingDate(self) -> str:
        return self.__publishingDate

    @publishingDate.setter
    def publishingDate(self, publishingDate: str):
        self.__publishingDate = publishingDate

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def artifactId(self) -> str:
        return self.__artifactId

    @artifactId.setter
    def artifactId(self, artifactId: str):
        self.__artifactId = artifactId

    @property
    def gedcoml_Projectdescription2(self):
        return self.__gedcoml_Projectdescription2

    @gedcoml_Projectdescription2.setter
    def gedcoml_Projectdescription2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_Projectdescription__gedcoml_Projectdescription2", None)
        self.__gedcoml_Projectdescription2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gedcoml_Author"):
                opp_val = getattr(old_value, "gedcoml_Author", None)
                if opp_val == self:
                    setattr(old_value, "gedcoml_Author", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gedcoml_Author"):
                opp_val = getattr(value, "gedcoml_Author", None)
                setattr(value, "gedcoml_Author", self)

    @property
    def gedcoml_Projectdescription22(self):
        return self.__gedcoml_Projectdescription22

    @gedcoml_Projectdescription22.setter
    def gedcoml_Projectdescription22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_Projectdescription__gedcoml_Projectdescription22", None)
        self.__gedcoml_Projectdescription22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gedcoml_FamilyBook"):
                opp_val = getattr(old_value, "gedcoml_FamilyBook", None)
                if opp_val == self:
                    setattr(old_value, "gedcoml_FamilyBook", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gedcoml_FamilyBook"):
                opp_val = getattr(value, "gedcoml_FamilyBook", None)
                setattr(value, "gedcoml_FamilyBook", self)

    @property
    def gedcoml_Projectdescription(self):
        return self.__gedcoml_Projectdescription

    @gedcoml_Projectdescription.setter
    def gedcoml_Projectdescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gedcoml_Projectdescription__gedcoml_Projectdescription", None)
        self.__gedcoml_Projectdescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gedcoml_FamilyImport"):
                    opp_val = getattr(item, "gedcoml_FamilyImport", None)
                    
                    if opp_val == self:
                        setattr(item, "gedcoml_FamilyImport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gedcoml_FamilyImport"):
                    opp_val = getattr(item, "gedcoml_FamilyImport", None)
                    
                    setattr(item, "gedcoml_FamilyImport", self)
                    
