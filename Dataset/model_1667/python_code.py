from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class hello121_NamedElement(ABC):

    def __init__(self, name: str, hello121_NamedElement: set["hello121_Alias"] = None):
        self.name = name
        self.hello121_NamedElement = hello121_NamedElement if hello121_NamedElement is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hello121_NamedElement(self):
        return self.__hello121_NamedElement

    @hello121_NamedElement.setter
    def hello121_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello121_NamedElement__hello121_NamedElement", None)
        self.__hello121_NamedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hello121_Alias"):
                    opp_val = getattr(item, "hello121_Alias", None)
                    
                    if opp_val == self:
                        setattr(item, "hello121_Alias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hello121_Alias"):
                    opp_val = getattr(item, "hello121_Alias", None)
                    
                    setattr(item, "hello121_Alias", self)
                    

class hello121_Third:

    def __init__(self, id: str, hello121_Third: "hello121_Thing" = None, hello121_Third15: "hello121_Classoc" = None):
        self.id = id
        self.hello121_Third = hello121_Third
        self.hello121_Third15 = hello121_Third15
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def hello121_Third15(self):
        return self.__hello121_Third15

    @hello121_Third15.setter
    def hello121_Third15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello121_Third__hello121_Third15", None)
        self.__hello121_Third15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello121_Classoc14"):
                opp_val = getattr(old_value, "hello121_Classoc14", None)
                if opp_val == self:
                    setattr(old_value, "hello121_Classoc14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello121_Classoc14"):
                opp_val = getattr(value, "hello121_Classoc14", None)
                setattr(value, "hello121_Classoc14", self)

    @property
    def hello121_Third(self):
        return self.__hello121_Third

    @hello121_Third.setter
    def hello121_Third(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello121_Third__hello121_Third", None)
        self.__hello121_Third = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello121_Thing5"):
                opp_val = getattr(old_value, "hello121_Thing5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello121_Thing5"):
                opp_val = getattr(value, "hello121_Thing5", None)
                if opp_val is None:
                    setattr(value, "hello121_Thing5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hello121_Alias:

    def __init__(self, id: str, hello121_Alias: "hello121_NamedElement" = None):
        self.id = id
        self.hello121_Alias = hello121_Alias
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def hello121_Alias(self):
        return self.__hello121_Alias

    @hello121_Alias.setter
    def hello121_Alias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello121_Alias__hello121_Alias", None)
        self.__hello121_Alias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello121_NamedElement"):
                opp_val = getattr(old_value, "hello121_NamedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello121_NamedElement"):
                opp_val = getattr(value, "hello121_NamedElement", None)
                if opp_val is None:
                    setattr(value, "hello121_NamedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hello121_Classoc:

    def __init__(self, id: str, hello121_Classoc: "hello121_Base" = None, hello121_Classoc8: "hello121_Thing" = None, hello121_Classoc14: "hello121_Third" = None, hello121_Classoc17: "hello121_Base" = None):
        self.id = id
        self.hello121_Classoc = hello121_Classoc
        self.hello121_Classoc8 = hello121_Classoc8
        self.hello121_Classoc14 = hello121_Classoc14
        self.hello121_Classoc17 = hello121_Classoc17
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def hello121_Classoc17(self):
        return self.__hello121_Classoc17

    @hello121_Classoc17.setter
    def hello121_Classoc17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello121_Classoc__hello121_Classoc17", None)
        self.__hello121_Classoc17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello121_Base18"):
                opp_val = getattr(old_value, "hello121_Base18", None)
                if opp_val == self:
                    setattr(old_value, "hello121_Base18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello121_Base18"):
                opp_val = getattr(value, "hello121_Base18", None)
                setattr(value, "hello121_Base18", self)

    @property
    def hello121_Classoc(self):
        return self.__hello121_Classoc

    @hello121_Classoc.setter
    def hello121_Classoc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello121_Classoc__hello121_Classoc", None)
        self.__hello121_Classoc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello121_Base2"):
                opp_val = getattr(old_value, "hello121_Base2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello121_Base2"):
                opp_val = getattr(value, "hello121_Base2", None)
                if opp_val is None:
                    setattr(value, "hello121_Base2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hello121_Classoc14(self):
        return self.__hello121_Classoc14

    @hello121_Classoc14.setter
    def hello121_Classoc14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello121_Classoc__hello121_Classoc14", None)
        self.__hello121_Classoc14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello121_Third15"):
                opp_val = getattr(old_value, "hello121_Third15", None)
                if opp_val == self:
                    setattr(old_value, "hello121_Third15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello121_Third15"):
                opp_val = getattr(value, "hello121_Third15", None)
                setattr(value, "hello121_Third15", self)

    @property
    def hello121_Classoc8(self):
        return self.__hello121_Classoc8

    @hello121_Classoc8.setter
    def hello121_Classoc8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello121_Classoc__hello121_Classoc8", None)
        self.__hello121_Classoc8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello121_Thing7"):
                opp_val = getattr(old_value, "hello121_Thing7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello121_Thing7"):
                opp_val = getattr(value, "hello121_Thing7", None)
                if opp_val is None:
                    setattr(value, "hello121_Thing7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hello121_Base:

    pass
class NamedElement:

    pass
class hello121_RelatedTo(NamedElement):

    def __init__(self, since: str, RelatedTo: "hello121_Thing" = None, relations: "hello121_Thing" = None, hello121_RelatedTo: "hello121_Thing" = None):
        self.since = since
        self.RelatedTo = RelatedTo
        self.relations = relations
        self.hello121_RelatedTo = hello121_RelatedTo
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def relations(self):
        return self.__relations

    @relations.setter
    def relations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello121_RelatedTo__relations", None)
        self.__relations = value
        
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

    @property
    def hello121_RelatedTo(self):
        return self.__hello121_RelatedTo

    @hello121_RelatedTo.setter
    def hello121_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello121_RelatedTo__hello121_RelatedTo", None)
        self.__hello121_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello121_Thing12"):
                opp_val = getattr(old_value, "hello121_Thing12", None)
                if opp_val == self:
                    setattr(old_value, "hello121_Thing12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello121_Thing12"):
                opp_val = getattr(value, "hello121_Thing12", None)
                setattr(value, "hello121_Thing12", self)

    @property
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello121_RelatedTo__RelatedTo", None)
        self.__RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fromThing"):
                opp_val = getattr(old_value, "fromThing", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fromThing"):
                opp_val = getattr(value, "fromThing", None)
                if opp_val is None:
                    setattr(value, "fromThing", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hello121_Thing(NamedElement):

    def __init__(self, id: int, hello121_Thing: "hello121_Base" = None, fromThing: set["hello121_RelatedTo"] = None, hello121_Thing5: set["hello121_Third"] = None, hello121_Thing7: set["hello121_Classoc"] = None, Thing: "hello121_RelatedTo" = None, hello121_Thing12: "hello121_RelatedTo" = None):
        self.id = id
        self.hello121_Thing = hello121_Thing
        self.fromThing = fromThing if fromThing is not None else set()
        self.hello121_Thing5 = hello121_Thing5 if hello121_Thing5 is not None else set()
        self.hello121_Thing7 = hello121_Thing7 if hello121_Thing7 is not None else set()
        self.Thing = Thing
        self.hello121_Thing12 = hello121_Thing12
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def hello121_Thing7(self):
        return self.__hello121_Thing7

    @hello121_Thing7.setter
    def hello121_Thing7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello121_Thing__hello121_Thing7", None)
        self.__hello121_Thing7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hello121_Classoc8"):
                    opp_val = getattr(item, "hello121_Classoc8", None)
                    
                    if opp_val == self:
                        setattr(item, "hello121_Classoc8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hello121_Classoc8"):
                    opp_val = getattr(item, "hello121_Classoc8", None)
                    
                    setattr(item, "hello121_Classoc8", self)
                    

    @property
    def hello121_Thing5(self):
        return self.__hello121_Thing5

    @hello121_Thing5.setter
    def hello121_Thing5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello121_Thing__hello121_Thing5", None)
        self.__hello121_Thing5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hello121_Third"):
                    opp_val = getattr(item, "hello121_Third", None)
                    
                    if opp_val == self:
                        setattr(item, "hello121_Third", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hello121_Third"):
                    opp_val = getattr(item, "hello121_Third", None)
                    
                    setattr(item, "hello121_Third", self)
                    

    @property
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello121_Thing__Thing", None)
        self.__Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relations"):
                opp_val = getattr(old_value, "relations", None)
                if opp_val == self:
                    setattr(old_value, "relations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relations"):
                opp_val = getattr(value, "relations", None)
                setattr(value, "relations", self)

    @property
    def hello121_Thing12(self):
        return self.__hello121_Thing12

    @hello121_Thing12.setter
    def hello121_Thing12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello121_Thing__hello121_Thing12", None)
        self.__hello121_Thing12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello121_RelatedTo"):
                opp_val = getattr(old_value, "hello121_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "hello121_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello121_RelatedTo"):
                opp_val = getattr(value, "hello121_RelatedTo", None)
                setattr(value, "hello121_RelatedTo", self)

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello121_Thing__fromThing", None)
        self.__fromThing = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RelatedTo"):
                    opp_val = getattr(item, "RelatedTo", None)
                    
                    if opp_val == self:
                        setattr(item, "RelatedTo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RelatedTo"):
                    opp_val = getattr(item, "RelatedTo", None)
                    
                    setattr(item, "RelatedTo", self)
                    

    @property
    def hello121_Thing(self):
        return self.__hello121_Thing

    @hello121_Thing.setter
    def hello121_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello121_Thing__hello121_Thing", None)
        self.__hello121_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello121_Base"):
                opp_val = getattr(old_value, "hello121_Base", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello121_Base"):
                opp_val = getattr(value, "hello121_Base", None)
                if opp_val is None:
                    setattr(value, "hello121_Base", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
