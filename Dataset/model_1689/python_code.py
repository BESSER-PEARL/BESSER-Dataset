from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class helloworld150_Comment:

    def __init__(self, content: str, helloworld150_Comment: "helloworld150_NamedElement" = None):
        self.content = content
        self.helloworld150_Comment = helloworld150_Comment
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def helloworld150_Comment(self):
        return self.__helloworld150_Comment

    @helloworld150_Comment.setter
    def helloworld150_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld150_Comment__helloworld150_Comment", None)
        self.__helloworld150_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld150_NamedElement"):
                opp_val = getattr(old_value, "helloworld150_NamedElement", None)
                if opp_val == self:
                    setattr(old_value, "helloworld150_NamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld150_NamedElement"):
                opp_val = getattr(value, "helloworld150_NamedElement", None)
                setattr(value, "helloworld150_NamedElement", self)

class NamedElement:

    pass
class helloworld150_Profession:

    def __init__(self, name: str, helloworld150_Profession: "helloworld150_World" = None, helloworld150_Profession15: "helloworld150_Person" = None):
        self.name = name
        self.helloworld150_Profession = helloworld150_Profession
        self.helloworld150_Profession15 = helloworld150_Profession15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def helloworld150_Profession15(self):
        return self.__helloworld150_Profession15

    @helloworld150_Profession15.setter
    def helloworld150_Profession15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld150_Profession__helloworld150_Profession15", None)
        self.__helloworld150_Profession15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld150_Person14"):
                opp_val = getattr(old_value, "helloworld150_Person14", None)
                if opp_val == self:
                    setattr(old_value, "helloworld150_Person14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld150_Person14"):
                opp_val = getattr(value, "helloworld150_Person14", None)
                setattr(value, "helloworld150_Person14", self)

    @property
    def helloworld150_Profession(self):
        return self.__helloworld150_Profession

    @helloworld150_Profession.setter
    def helloworld150_Profession(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld150_Profession__helloworld150_Profession", None)
        self.__helloworld150_Profession = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld150_World4"):
                opp_val = getattr(old_value, "helloworld150_World4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld150_World4"):
                opp_val = getattr(value, "helloworld150_World4", None)
                if opp_val is None:
                    setattr(value, "helloworld150_World4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class helloworld150_Person(NamedElement):

    def __init__(self, forName: str, birthDate: str, helloworld150_Person: "helloworld150_World" = None, helloworld150_Person12: "helloworld150_Own" = None, helloworld150_Person14: "helloworld150_Profession" = None):
        self.forName = forName
        self.birthDate = birthDate
        self.helloworld150_Person = helloworld150_Person
        self.helloworld150_Person12 = helloworld150_Person12
        self.helloworld150_Person14 = helloworld150_Person14
        
    @property
    def birthDate(self) -> str:
        return self.__birthDate

    @birthDate.setter
    def birthDate(self, birthDate: str):
        self.__birthDate = birthDate

    @property
    def forName(self) -> str:
        return self.__forName

    @forName.setter
    def forName(self, forName: str):
        self.__forName = forName

    @property
    def helloworld150_Person14(self):
        return self.__helloworld150_Person14

    @helloworld150_Person14.setter
    def helloworld150_Person14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld150_Person__helloworld150_Person14", None)
        self.__helloworld150_Person14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld150_Profession15"):
                opp_val = getattr(old_value, "helloworld150_Profession15", None)
                if opp_val == self:
                    setattr(old_value, "helloworld150_Profession15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld150_Profession15"):
                opp_val = getattr(value, "helloworld150_Profession15", None)
                setattr(value, "helloworld150_Profession15", self)

    @property
    def helloworld150_Person(self):
        return self.__helloworld150_Person

    @helloworld150_Person.setter
    def helloworld150_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld150_Person__helloworld150_Person", None)
        self.__helloworld150_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld150_World2"):
                opp_val = getattr(old_value, "helloworld150_World2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld150_World2"):
                opp_val = getattr(value, "helloworld150_World2", None)
                if opp_val is None:
                    setattr(value, "helloworld150_World2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def helloworld150_Person12(self):
        return self.__helloworld150_Person12

    @helloworld150_Person12.setter
    def helloworld150_Person12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld150_Person__helloworld150_Person12", None)
        self.__helloworld150_Person12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld150_Own11"):
                opp_val = getattr(old_value, "helloworld150_Own11", None)
                if opp_val == self:
                    setattr(old_value, "helloworld150_Own11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld150_Own11"):
                opp_val = getattr(value, "helloworld150_Own11", None)
                setattr(value, "helloworld150_Own11", self)

class helloworld150_NamedElement(ABC):

    def __init__(self, name: str, helloworld150_NamedElement: "helloworld150_Comment" = None):
        self.name = name
        self.helloworld150_NamedElement = helloworld150_NamedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def helloworld150_NamedElement(self):
        return self.__helloworld150_NamedElement

    @helloworld150_NamedElement.setter
    def helloworld150_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld150_NamedElement__helloworld150_NamedElement", None)
        self.__helloworld150_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld150_Comment"):
                opp_val = getattr(old_value, "helloworld150_Comment", None)
                if opp_val == self:
                    setattr(old_value, "helloworld150_Comment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld150_Comment"):
                opp_val = getattr(value, "helloworld150_Comment", None)
                setattr(value, "helloworld150_Comment", self)

class helloworld150_Own(NamedElement):

    def __init__(self, since: str, ownerName: str, Own: "helloworld150_Thing" = None, helloworld150_Own: "helloworld150_Thing" = None, ownership: "helloworld150_Thing" = None, helloworld150_Own11: "helloworld150_Person" = None):
        self.since = since
        self.ownerName = ownerName
        self.Own = Own
        self.helloworld150_Own = helloworld150_Own
        self.ownership = ownership
        self.helloworld150_Own11 = helloworld150_Own11
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def ownerName(self) -> str:
        return self.__ownerName

    @ownerName.setter
    def ownerName(self, ownerName: str):
        self.__ownerName = ownerName

    @property
    def Own(self):
        return self.__Own

    @Own.setter
    def Own(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld150_Own__Own", None)
        self.__Own = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thing"):
                opp_val = getattr(old_value, "thing", None)
                if opp_val == self:
                    setattr(old_value, "thing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thing"):
                opp_val = getattr(value, "thing", None)
                setattr(value, "thing", self)

    @property
    def helloworld150_Own11(self):
        return self.__helloworld150_Own11

    @helloworld150_Own11.setter
    def helloworld150_Own11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld150_Own__helloworld150_Own11", None)
        self.__helloworld150_Own11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld150_Person12"):
                opp_val = getattr(old_value, "helloworld150_Person12", None)
                if opp_val == self:
                    setattr(old_value, "helloworld150_Person12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld150_Person12"):
                opp_val = getattr(value, "helloworld150_Person12", None)
                setattr(value, "helloworld150_Person12", self)

    @property
    def helloworld150_Own(self):
        return self.__helloworld150_Own

    @helloworld150_Own.setter
    def helloworld150_Own(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld150_Own__helloworld150_Own", None)
        self.__helloworld150_Own = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld150_Thing7"):
                opp_val = getattr(old_value, "helloworld150_Thing7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld150_Thing7"):
                opp_val = getattr(value, "helloworld150_Thing7", None)
                if opp_val is None:
                    setattr(value, "helloworld150_Thing7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownership(self):
        return self.__ownership

    @ownership.setter
    def ownership(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld150_Own__ownership", None)
        self.__ownership = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Thing"):
                opp_val = getattr(old_value, "Thing", None)
                if opp_val == self:
                    setattr(old_value, "Thing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Thing"):
                opp_val = getattr(value, "Thing", None)
                setattr(value, "Thing", self)

class helloworld150_Thing(NamedElement):

    def __init__(self, id: int, helloworld150_Thing: "helloworld150_World" = None, thing: "helloworld150_Own" = None, helloworld150_Thing7: set["helloworld150_Own"] = None, Thing: "helloworld150_Own" = None):
        self.id = id
        self.helloworld150_Thing = helloworld150_Thing
        self.thing = thing
        self.helloworld150_Thing7 = helloworld150_Thing7 if helloworld150_Thing7 is not None else set()
        self.Thing = Thing
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def helloworld150_Thing7(self):
        return self.__helloworld150_Thing7

    @helloworld150_Thing7.setter
    def helloworld150_Thing7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld150_Thing__helloworld150_Thing7", None)
        self.__helloworld150_Thing7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "helloworld150_Own"):
                    opp_val = getattr(item, "helloworld150_Own", None)
                    
                    if opp_val == self:
                        setattr(item, "helloworld150_Own", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "helloworld150_Own"):
                    opp_val = getattr(item, "helloworld150_Own", None)
                    
                    setattr(item, "helloworld150_Own", self)
                    

    @property
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld150_Thing__Thing", None)
        self.__Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownership"):
                opp_val = getattr(old_value, "ownership", None)
                if opp_val == self:
                    setattr(old_value, "ownership", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownership"):
                opp_val = getattr(value, "ownership", None)
                setattr(value, "ownership", self)

    @property
    def helloworld150_Thing(self):
        return self.__helloworld150_Thing

    @helloworld150_Thing.setter
    def helloworld150_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld150_Thing__helloworld150_Thing", None)
        self.__helloworld150_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld150_World"):
                opp_val = getattr(old_value, "helloworld150_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld150_World"):
                opp_val = getattr(value, "helloworld150_World", None)
                if opp_val is None:
                    setattr(value, "helloworld150_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thing(self):
        return self.__thing

    @thing.setter
    def thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld150_Thing__thing", None)
        self.__thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Own"):
                opp_val = getattr(old_value, "Own", None)
                if opp_val == self:
                    setattr(old_value, "Own", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Own"):
                opp_val = getattr(value, "Own", None)
                setattr(value, "Own", self)

class helloworld150_World:

    pass