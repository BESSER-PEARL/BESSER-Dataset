from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class visualworld_NamedElement(ABC):

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
class visualworld_Thing(NamedElement):

    def __init__(self, id: int, fromThing: set["visualworld_RelatedTo"] = None, visualworld_Thing: "visualworld_World" = None, visualworld_Thing4: "visualworld_RelatedTo" = None, Thing: "visualworld_RelatedTo" = None):
        self.id = id
        self.fromThing = fromThing if fromThing is not None else set()
        self.visualworld_Thing = visualworld_Thing
        self.visualworld_Thing4 = visualworld_Thing4
        self.Thing = Thing
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_visualworld_Thing__fromThing", None)
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
        old_value = getattr(self, f"_visualworld_Thing__Thing", None)
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
    def visualworld_Thing(self):
        return self.__visualworld_Thing

    @visualworld_Thing.setter
    def visualworld_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_visualworld_Thing__visualworld_Thing", None)
        self.__visualworld_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "visualworld_World"):
                opp_val = getattr(old_value, "visualworld_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "visualworld_World"):
                opp_val = getattr(value, "visualworld_World", None)
                if opp_val is None:
                    setattr(value, "visualworld_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def visualworld_Thing4(self):
        return self.__visualworld_Thing4

    @visualworld_Thing4.setter
    def visualworld_Thing4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_visualworld_Thing__visualworld_Thing4", None)
        self.__visualworld_Thing4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "visualworld_RelatedTo"):
                opp_val = getattr(old_value, "visualworld_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "visualworld_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "visualworld_RelatedTo"):
                opp_val = getattr(value, "visualworld_RelatedTo", None)
                setattr(value, "visualworld_RelatedTo", self)

class visualworld_RelatedTo(NamedElement):

    def __init__(self, since: str, RelatedTo: "visualworld_Thing" = None, visualworld_RelatedTo: "visualworld_Thing" = None, relations: "visualworld_Thing" = None):
        self.since = since
        self.RelatedTo = RelatedTo
        self.visualworld_RelatedTo = visualworld_RelatedTo
        self.relations = relations
        
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
        old_value = getattr(self, f"_visualworld_RelatedTo__relations", None)
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
    def visualworld_RelatedTo(self):
        return self.__visualworld_RelatedTo

    @visualworld_RelatedTo.setter
    def visualworld_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_visualworld_RelatedTo__visualworld_RelatedTo", None)
        self.__visualworld_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "visualworld_Thing4"):
                opp_val = getattr(old_value, "visualworld_Thing4", None)
                if opp_val == self:
                    setattr(old_value, "visualworld_Thing4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "visualworld_Thing4"):
                opp_val = getattr(value, "visualworld_Thing4", None)
                setattr(value, "visualworld_Thing4", self)

    @property
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_visualworld_RelatedTo__RelatedTo", None)
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

class visualworld_World:

    pass