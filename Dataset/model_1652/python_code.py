from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class errya_Alias:

    def __init__(self, id: str, errya_Alias: "errya_NamedElement" = None):
        self.id = id
        self.errya_Alias = errya_Alias
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def errya_Alias(self):
        return self.__errya_Alias

    @errya_Alias.setter
    def errya_Alias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errya_Alias__errya_Alias", None)
        self.__errya_Alias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errya_NamedElement"):
                opp_val = getattr(old_value, "errya_NamedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errya_NamedElement"):
                opp_val = getattr(value, "errya_NamedElement", None)
                if opp_val is None:
                    setattr(value, "errya_NamedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class errya_NamedElement(ABC):

    def __init__(self, name: str, errya_NamedElement: set["errya_Alias"] = None):
        self.name = name
        self.errya_NamedElement = errya_NamedElement if errya_NamedElement is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def errya_NamedElement(self):
        return self.__errya_NamedElement

    @errya_NamedElement.setter
    def errya_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errya_NamedElement__errya_NamedElement", None)
        self.__errya_NamedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "errya_Alias"):
                    opp_val = getattr(item, "errya_Alias", None)
                    
                    if opp_val == self:
                        setattr(item, "errya_Alias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "errya_Alias"):
                    opp_val = getattr(item, "errya_Alias", None)
                    
                    setattr(item, "errya_Alias", self)
                    

class errya_World:

    pass
class NamedElement:

    pass
class errya_RelatedTo(NamedElement):

    def __init__(self, since: str, RelatedTo: "errya_Thing" = None, relations: "errya_Thing" = None, errya_RelatedTo: "errya_Thing" = None):
        self.since = since
        self.RelatedTo = RelatedTo
        self.relations = relations
        self.errya_RelatedTo = errya_RelatedTo
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errya_RelatedTo__RelatedTo", None)
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
        old_value = getattr(self, f"_errya_RelatedTo__relations", None)
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
    def errya_RelatedTo(self):
        return self.__errya_RelatedTo

    @errya_RelatedTo.setter
    def errya_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errya_RelatedTo__errya_RelatedTo", None)
        self.__errya_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errya_Thing5"):
                opp_val = getattr(old_value, "errya_Thing5", None)
                if opp_val == self:
                    setattr(old_value, "errya_Thing5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errya_Thing5"):
                opp_val = getattr(value, "errya_Thing5", None)
                setattr(value, "errya_Thing5", self)

class errya_Thing(NamedElement):

    def __init__(self, id: int, errya_Thing: "errya_World" = None, fromThing: set["errya_RelatedTo"] = None, Thing: "errya_RelatedTo" = None, errya_Thing5: "errya_RelatedTo" = None):
        self.id = id
        self.errya_Thing = errya_Thing
        self.fromThing = fromThing if fromThing is not None else set()
        self.Thing = Thing
        self.errya_Thing5 = errya_Thing5
        
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
        old_value = getattr(self, f"_errya_Thing__Thing", None)
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
    def errya_Thing(self):
        return self.__errya_Thing

    @errya_Thing.setter
    def errya_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errya_Thing__errya_Thing", None)
        self.__errya_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errya_World"):
                opp_val = getattr(old_value, "errya_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errya_World"):
                opp_val = getattr(value, "errya_World", None)
                if opp_val is None:
                    setattr(value, "errya_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errya_Thing__fromThing", None)
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
    def errya_Thing5(self):
        return self.__errya_Thing5

    @errya_Thing5.setter
    def errya_Thing5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errya_Thing__errya_Thing5", None)
        self.__errya_Thing5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errya_RelatedTo"):
                opp_val = getattr(old_value, "errya_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "errya_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errya_RelatedTo"):
                opp_val = getattr(value, "errya_RelatedTo", None)
                setattr(value, "errya_RelatedTo", self)
