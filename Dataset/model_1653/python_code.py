from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class yyaa_Alias:

    def __init__(self, id: str, yyaa_Alias: "yyaa_NamedElement" = None):
        self.id = id
        self.yyaa_Alias = yyaa_Alias
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyaa_Alias(self):
        return self.__yyaa_Alias

    @yyaa_Alias.setter
    def yyaa_Alias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyaa_Alias__yyaa_Alias", None)
        self.__yyaa_Alias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyaa_NamedElement"):
                opp_val = getattr(old_value, "yyaa_NamedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyaa_NamedElement"):
                opp_val = getattr(value, "yyaa_NamedElement", None)
                if opp_val is None:
                    setattr(value, "yyaa_NamedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yyaa_NamedElement(ABC):

    def __init__(self, name: str, yyaa_NamedElement: set["yyaa_Alias"] = None):
        self.name = name
        self.yyaa_NamedElement = yyaa_NamedElement if yyaa_NamedElement is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def yyaa_NamedElement(self):
        return self.__yyaa_NamedElement

    @yyaa_NamedElement.setter
    def yyaa_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyaa_NamedElement__yyaa_NamedElement", None)
        self.__yyaa_NamedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyaa_Alias"):
                    opp_val = getattr(item, "yyaa_Alias", None)
                    
                    if opp_val == self:
                        setattr(item, "yyaa_Alias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyaa_Alias"):
                    opp_val = getattr(item, "yyaa_Alias", None)
                    
                    setattr(item, "yyaa_Alias", self)
                    

class NamedElement:

    pass
class yyaa_RelatedTo(NamedElement):

    def __init__(self, since: str, 2: "yyaa_Thing" = None, 5: "yyaa_Thing" = None, yyaa_RelatedTo: "yyaa_Thing" = None):
        self.since = since
        self.2 = 2
        self.5 = 5
        self.yyaa_RelatedTo = yyaa_RelatedTo
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def 5(self):
        return self.__5

    @5.setter
    def 5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyaa_RelatedTo__5", None)
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
    def yyaa_RelatedTo(self):
        return self.__yyaa_RelatedTo

    @yyaa_RelatedTo.setter
    def yyaa_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyaa_RelatedTo__yyaa_RelatedTo", None)
        self.__yyaa_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyaa_Thing8"):
                opp_val = getattr(old_value, "yyaa_Thing8", None)
                if opp_val == self:
                    setattr(old_value, "yyaa_Thing8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyaa_Thing8"):
                opp_val = getattr(value, "yyaa_Thing8", None)
                setattr(value, "yyaa_Thing8", self)

    @property
    def 2(self):
        return self.__2

    @2.setter
    def 2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyaa_RelatedTo__2", None)
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

class yyaa_Thing(NamedElement):

    def __init__(self, id: int, yyaa_Thing: "yyaa_World" = None, : set["yyaa_RelatedTo"] = None, 6: "yyaa_RelatedTo" = None, yyaa_Thing8: "yyaa_RelatedTo" = None):
        self.id = id
        self.yyaa_Thing = yyaa_Thing
        self. =  if  is not None else set()
        self.6 = 6
        self.yyaa_Thing8 = yyaa_Thing8
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def 6(self):
        return self.__6

    @6.setter
    def 6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyaa_Thing__6", None)
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
    def yyaa_Thing8(self):
        return self.__yyaa_Thing8

    @yyaa_Thing8.setter
    def yyaa_Thing8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyaa_Thing__yyaa_Thing8", None)
        self.__yyaa_Thing8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyaa_RelatedTo"):
                opp_val = getattr(old_value, "yyaa_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "yyaa_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyaa_RelatedTo"):
                opp_val = getattr(value, "yyaa_RelatedTo", None)
                setattr(value, "yyaa_RelatedTo", self)

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyaa_Thing__", None)
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
                    

    @property
    def yyaa_Thing(self):
        return self.__yyaa_Thing

    @yyaa_Thing.setter
    def yyaa_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyaa_Thing__yyaa_Thing", None)
        self.__yyaa_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyaa_World"):
                opp_val = getattr(old_value, "yyaa_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyaa_World"):
                opp_val = getattr(value, "yyaa_World", None)
                if opp_val is None:
                    setattr(value, "yyaa_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yyaa_World:

    pass