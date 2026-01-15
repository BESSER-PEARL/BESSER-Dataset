from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class yya_Alias:

    def __init__(self, id: str, yya_Alias: "yya_NamedElement" = None):
        self.id = id
        self.yya_Alias = yya_Alias
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yya_Alias(self):
        return self.__yya_Alias

    @yya_Alias.setter
    def yya_Alias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yya_Alias__yya_Alias", None)
        self.__yya_Alias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yya_NamedElement"):
                opp_val = getattr(old_value, "yya_NamedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yya_NamedElement"):
                opp_val = getattr(value, "yya_NamedElement", None)
                if opp_val is None:
                    setattr(value, "yya_NamedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yya_NamedElement(ABC):

    def __init__(self, name: str, yya_NamedElement: set["yya_Alias"] = None):
        self.name = name
        self.yya_NamedElement = yya_NamedElement if yya_NamedElement is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def yya_NamedElement(self):
        return self.__yya_NamedElement

    @yya_NamedElement.setter
    def yya_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yya_NamedElement__yya_NamedElement", None)
        self.__yya_NamedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yya_Alias"):
                    opp_val = getattr(item, "yya_Alias", None)
                    
                    if opp_val == self:
                        setattr(item, "yya_Alias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yya_Alias"):
                    opp_val = getattr(item, "yya_Alias", None)
                    
                    setattr(item, "yya_Alias", self)
                    

class NamedElement:

    pass
class yya_RelatedTo(NamedElement):

    def __init__(self, since: str, yya_RelatedTo: "yya_Thing" = None, RelatedTo: "yya_Thing" = None, relations: "yya_Thing" = None):
        self.since = since
        self.yya_RelatedTo = yya_RelatedTo
        self.RelatedTo = RelatedTo
        self.relations = relations
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def yya_RelatedTo(self):
        return self.__yya_RelatedTo

    @yya_RelatedTo.setter
    def yya_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yya_RelatedTo__yya_RelatedTo", None)
        self.__yya_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yya_Thing"):
                opp_val = getattr(old_value, "yya_Thing", None)
                if opp_val == self:
                    setattr(old_value, "yya_Thing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yya_Thing"):
                opp_val = getattr(value, "yya_Thing", None)
                setattr(value, "yya_Thing", self)

    @property
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yya_RelatedTo__RelatedTo", None)
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

    @property
    def relations(self):
        return self.__relations

    @relations.setter
    def relations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yya_RelatedTo__relations", None)
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

class yya_Thing(NamedElement):

    def __init__(self, id: int, yya_Thing: "yya_RelatedTo" = None, fromThing: set["yya_RelatedTo"] = None, Thing: "yya_RelatedTo" = None):
        self.id = id
        self.yya_Thing = yya_Thing
        self.fromThing = fromThing if fromThing is not None else set()
        self.Thing = Thing
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def yya_Thing(self):
        return self.__yya_Thing

    @yya_Thing.setter
    def yya_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yya_Thing__yya_Thing", None)
        self.__yya_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yya_RelatedTo"):
                opp_val = getattr(old_value, "yya_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "yya_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yya_RelatedTo"):
                opp_val = getattr(value, "yya_RelatedTo", None)
                setattr(value, "yya_RelatedTo", self)

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yya_Thing__fromThing", None)
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
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yya_Thing__Thing", None)
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
