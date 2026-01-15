from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class yyb_Alias:

    def __init__(self, id: str, yyb_Alias: "yyb_RelatedTo" = None):
        self.id = id
        self.yyb_Alias = yyb_Alias
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyb_Alias(self):
        return self.__yyb_Alias

    @yyb_Alias.setter
    def yyb_Alias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyb_Alias__yyb_Alias", None)
        self.__yyb_Alias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyb_RelatedTo"):
                opp_val = getattr(old_value, "yyb_RelatedTo", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyb_RelatedTo"):
                opp_val = getattr(value, "yyb_RelatedTo", None)
                if opp_val is None:
                    setattr(value, "yyb_RelatedTo", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yyb_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class yyb_RelatedTo(NamedElement):

    def __init__(self, since: str, RelatedTo: "yyb_Thing" = None, relations: "yyb_Thing" = None, yyb_RelatedTo: set["yyb_Alias"] = None):
        self.since = since
        self.RelatedTo = RelatedTo
        self.relations = relations
        self.yyb_RelatedTo = yyb_RelatedTo if yyb_RelatedTo is not None else set()
        
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
        old_value = getattr(self, f"_yyb_RelatedTo__relations", None)
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
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyb_RelatedTo__RelatedTo", None)
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
    def yyb_RelatedTo(self):
        return self.__yyb_RelatedTo

    @yyb_RelatedTo.setter
    def yyb_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyb_RelatedTo__yyb_RelatedTo", None)
        self.__yyb_RelatedTo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyb_Alias"):
                    opp_val = getattr(item, "yyb_Alias", None)
                    
                    if opp_val == self:
                        setattr(item, "yyb_Alias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyb_Alias"):
                    opp_val = getattr(item, "yyb_Alias", None)
                    
                    setattr(item, "yyb_Alias", self)
                    

class yyb_Thing(NamedElement):

    def __init__(self, id: int, fromThing: set["yyb_RelatedTo"] = None, Thing: "yyb_RelatedTo" = None):
        self.id = id
        self.fromThing = fromThing if fromThing is not None else set()
        self.Thing = Thing
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyb_Thing__Thing", None)
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
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyb_Thing__fromThing", None)
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
                    
