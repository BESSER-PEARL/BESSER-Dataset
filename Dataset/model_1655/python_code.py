from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class error4_RelatedTo(NamedElement):

    def __init__(self, since: str, RelatedTo: "error4_Thing" = None, relations: "error4_Thing" = None, error4_RelatedTo: "error4_Thing" = None, error4_RelatedTo8: "error4_Component" = None):
        self.since = since
        self.RelatedTo = RelatedTo
        self.relations = relations
        self.error4_RelatedTo = error4_RelatedTo
        self.error4_RelatedTo8 = error4_RelatedTo8
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def error4_RelatedTo(self):
        return self.__error4_RelatedTo

    @error4_RelatedTo.setter
    def error4_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error4_RelatedTo__error4_RelatedTo", None)
        self.__error4_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "error4_Thing6"):
                opp_val = getattr(old_value, "error4_Thing6", None)
                if opp_val == self:
                    setattr(old_value, "error4_Thing6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "error4_Thing6"):
                opp_val = getattr(value, "error4_Thing6", None)
                setattr(value, "error4_Thing6", self)

    @property
    def relations(self):
        return self.__relations

    @relations.setter
    def relations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error4_RelatedTo__relations", None)
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
    def error4_RelatedTo8(self):
        return self.__error4_RelatedTo8

    @error4_RelatedTo8.setter
    def error4_RelatedTo8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error4_RelatedTo__error4_RelatedTo8", None)
        self.__error4_RelatedTo8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "error4_Component9"):
                opp_val = getattr(old_value, "error4_Component9", None)
                if opp_val == self:
                    setattr(old_value, "error4_Component9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "error4_Component9"):
                opp_val = getattr(value, "error4_Component9", None)
                setattr(value, "error4_Component9", self)

    @property
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error4_RelatedTo__RelatedTo", None)
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

class error4_Thing(NamedElement):

    def __init__(self, id: int, error4_Thing3: set["error4_Component"] = None, error4_Thing: "error4_World" = None, fromThing: set["error4_RelatedTo"] = None, Thing: "error4_RelatedTo" = None, error4_Thing6: "error4_RelatedTo" = None):
        self.id = id
        self.error4_Thing3 = error4_Thing3 if error4_Thing3 is not None else set()
        self.error4_Thing = error4_Thing
        self.fromThing = fromThing if fromThing is not None else set()
        self.Thing = Thing
        self.error4_Thing6 = error4_Thing6
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def error4_Thing6(self):
        return self.__error4_Thing6

    @error4_Thing6.setter
    def error4_Thing6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error4_Thing__error4_Thing6", None)
        self.__error4_Thing6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "error4_RelatedTo"):
                opp_val = getattr(old_value, "error4_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "error4_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "error4_RelatedTo"):
                opp_val = getattr(value, "error4_RelatedTo", None)
                setattr(value, "error4_RelatedTo", self)

    @property
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error4_Thing__Thing", None)
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
        old_value = getattr(self, f"_error4_Thing__fromThing", None)
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
    def error4_Thing(self):
        return self.__error4_Thing

    @error4_Thing.setter
    def error4_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error4_Thing__error4_Thing", None)
        self.__error4_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "error4_World"):
                opp_val = getattr(old_value, "error4_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "error4_World"):
                opp_val = getattr(value, "error4_World", None)
                if opp_val is None:
                    setattr(value, "error4_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def error4_Thing3(self):
        return self.__error4_Thing3

    @error4_Thing3.setter
    def error4_Thing3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error4_Thing__error4_Thing3", None)
        self.__error4_Thing3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "error4_Component"):
                    opp_val = getattr(item, "error4_Component", None)
                    
                    if opp_val == self:
                        setattr(item, "error4_Component", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "error4_Component"):
                    opp_val = getattr(item, "error4_Component", None)
                    
                    setattr(item, "error4_Component", self)
                    

class error4_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class error4_Component(NamedElement):

    pass
class error4_World:

    pass