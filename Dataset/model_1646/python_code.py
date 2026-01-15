from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class helloworld123_Alias:

    def __init__(self, id: str, helloworld123_Alias: "helloworld123_NamedElement" = None):
        self.id = id
        self.helloworld123_Alias = helloworld123_Alias
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def helloworld123_Alias(self):
        return self.__helloworld123_Alias

    @helloworld123_Alias.setter
    def helloworld123_Alias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld123_Alias__helloworld123_Alias", None)
        self.__helloworld123_Alias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld123_NamedElement"):
                opp_val = getattr(old_value, "helloworld123_NamedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld123_NamedElement"):
                opp_val = getattr(value, "helloworld123_NamedElement", None)
                if opp_val is None:
                    setattr(value, "helloworld123_NamedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class helloworld123_NamedElement(ABC):

    def __init__(self, name: str, helloworld123_NamedElement: set["helloworld123_Alias"] = None):
        self.name = name
        self.helloworld123_NamedElement = helloworld123_NamedElement if helloworld123_NamedElement is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def helloworld123_NamedElement(self):
        return self.__helloworld123_NamedElement

    @helloworld123_NamedElement.setter
    def helloworld123_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld123_NamedElement__helloworld123_NamedElement", None)
        self.__helloworld123_NamedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "helloworld123_Alias"):
                    opp_val = getattr(item, "helloworld123_Alias", None)
                    
                    if opp_val == self:
                        setattr(item, "helloworld123_Alias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "helloworld123_Alias"):
                    opp_val = getattr(item, "helloworld123_Alias", None)
                    
                    setattr(item, "helloworld123_Alias", self)
                    

class helloworld123_World:

    pass
class NamedElement:

    pass
class helloworld123_RelatedTo(NamedElement):

    def __init__(self, since: str, 2: "helloworld123_Thing" = None, 5: "helloworld123_Thing" = None, helloworld123_RelatedTo: "helloworld123_Thing" = None):
        self.since = since
        self.2 = 2
        self.5 = 5
        self.helloworld123_RelatedTo = helloworld123_RelatedTo
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def helloworld123_RelatedTo(self):
        return self.__helloworld123_RelatedTo

    @helloworld123_RelatedTo.setter
    def helloworld123_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld123_RelatedTo__helloworld123_RelatedTo", None)
        self.__helloworld123_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld123_Thing8"):
                opp_val = getattr(old_value, "helloworld123_Thing8", None)
                if opp_val == self:
                    setattr(old_value, "helloworld123_Thing8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld123_Thing8"):
                opp_val = getattr(value, "helloworld123_Thing8", None)
                setattr(value, "helloworld123_Thing8", self)

    @property
    def 5(self):
        return self.__5

    @5.setter
    def 5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld123_RelatedTo__5", None)
        self.__5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "6"):
                opp_val = getattr(old_value, "6", None)
                if opp_val == self:
                    setattr(old_value, "6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "6"):
                opp_val = getattr(value, "6", None)
                setattr(value, "6", self)

    @property
    def 2(self):
        return self.__2

    @2.setter
    def 2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld123_RelatedTo__2", None)
        self.__2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                if opp_val is None:
                    setattr(value, "", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class helloworld123_Thing(NamedElement):

    def __init__(self, id: int, helloworld123_Thing: "helloworld123_World" = None, : set["helloworld123_RelatedTo"] = None, 6: "helloworld123_RelatedTo" = None, helloworld123_Thing8: "helloworld123_RelatedTo" = None):
        self.id = id
        self.helloworld123_Thing = helloworld123_Thing
        self. =  if  is not None else set()
        self.6 = 6
        self.helloworld123_Thing8 = helloworld123_Thing8
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def helloworld123_Thing8(self):
        return self.__helloworld123_Thing8

    @helloworld123_Thing8.setter
    def helloworld123_Thing8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld123_Thing__helloworld123_Thing8", None)
        self.__helloworld123_Thing8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld123_RelatedTo"):
                opp_val = getattr(old_value, "helloworld123_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "helloworld123_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld123_RelatedTo"):
                opp_val = getattr(value, "helloworld123_RelatedTo", None)
                setattr(value, "helloworld123_RelatedTo", self)

    @property
    def 6(self):
        return self.__6

    @6.setter
    def 6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld123_Thing__6", None)
        self.__6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "5"):
                opp_val = getattr(old_value, "5", None)
                if opp_val == self:
                    setattr(old_value, "5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "5"):
                opp_val = getattr(value, "5", None)
                setattr(value, "5", self)

    @property
    def helloworld123_Thing(self):
        return self.__helloworld123_Thing

    @helloworld123_Thing.setter
    def helloworld123_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld123_Thing__helloworld123_Thing", None)
        self.__helloworld123_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld123_World"):
                opp_val = getattr(old_value, "helloworld123_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld123_World"):
                opp_val = getattr(value, "helloworld123_World", None)
                if opp_val is None:
                    setattr(value, "helloworld123_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld123_Thing__", None)
        self.__ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "2"):
                    opp_val = getattr(item, "2", None)
                    
                    if opp_val == self:
                        setattr(item, "2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "2"):
                    opp_val = getattr(item, "2", None)
                    
                    setattr(item, "2", self)
                    
