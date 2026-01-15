from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class simpleworld_NamedElement(ABC):

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
class simpleworld_RelatedTo(NamedElement):

    def __init__(self, since: str, relations: "simpleworld_Thing" = None, simpleworld_RelatedTo: "simpleworld_Thing" = None, RelatedTo: "simpleworld_Thing" = None):
        self.since = since
        self.relations = relations
        self.simpleworld_RelatedTo = simpleworld_RelatedTo
        self.RelatedTo = RelatedTo
        
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
        old_value = getattr(self, f"_simpleworld_RelatedTo__RelatedTo", None)
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
        old_value = getattr(self, f"_simpleworld_RelatedTo__relations", None)
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
    def simpleworld_RelatedTo(self):
        return self.__simpleworld_RelatedTo

    @simpleworld_RelatedTo.setter
    def simpleworld_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld_RelatedTo__simpleworld_RelatedTo", None)
        self.__simpleworld_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleworld_Thing4"):
                opp_val = getattr(old_value, "simpleworld_Thing4", None)
                if opp_val == self:
                    setattr(old_value, "simpleworld_Thing4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleworld_Thing4"):
                opp_val = getattr(value, "simpleworld_Thing4", None)
                setattr(value, "simpleworld_Thing4", self)

class simpleworld_Thing(NamedElement):

    def __init__(self, id: int, simpleworld_Thing: "simpleworld_World" = None, Thing: "simpleworld_RelatedTo" = None, simpleworld_Thing4: "simpleworld_RelatedTo" = None, fromThing: set["simpleworld_RelatedTo"] = None):
        self.id = id
        self.simpleworld_Thing = simpleworld_Thing
        self.Thing = Thing
        self.simpleworld_Thing4 = simpleworld_Thing4
        self.fromThing = fromThing if fromThing is not None else set()
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def simpleworld_Thing(self):
        return self.__simpleworld_Thing

    @simpleworld_Thing.setter
    def simpleworld_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld_Thing__simpleworld_Thing", None)
        self.__simpleworld_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleworld_World"):
                opp_val = getattr(old_value, "simpleworld_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleworld_World"):
                opp_val = getattr(value, "simpleworld_World", None)
                if opp_val is None:
                    setattr(value, "simpleworld_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleworld_Thing4(self):
        return self.__simpleworld_Thing4

    @simpleworld_Thing4.setter
    def simpleworld_Thing4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld_Thing__simpleworld_Thing4", None)
        self.__simpleworld_Thing4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleworld_RelatedTo"):
                opp_val = getattr(old_value, "simpleworld_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "simpleworld_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleworld_RelatedTo"):
                opp_val = getattr(value, "simpleworld_RelatedTo", None)
                setattr(value, "simpleworld_RelatedTo", self)

    @property
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleworld_Thing__Thing", None)
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
        old_value = getattr(self, f"_simpleworld_Thing__fromThing", None)
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
                    

class simpleworld_World:

    pass