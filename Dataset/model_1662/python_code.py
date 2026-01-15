from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Thing:

    pass
class nested102_EClass7(Thing):

    pass
class EClass8:

    pass
class EClass7:

    pass
class nested102_EClass6(EClass7, EClass8):

    pass
class EClass6:

    pass
class nested102_NamedElement(ABC):

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
class nested102_EClass1(NamedElement):

    pass
class nested102_EClass5(NamedElement, EClass6):

    pass
class nested102_RelatedTo(NamedElement):

    def __init__(self, since: str, RelatedTo: "nested102_Thing" = None, relations: "nested102_Thing" = None, nested102_RelatedTo: "nested102_Thing" = None):
        self.since = since
        self.RelatedTo = RelatedTo
        self.relations = relations
        self.nested102_RelatedTo = nested102_RelatedTo
        
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
        old_value = getattr(self, f"_nested102_RelatedTo__relations", None)
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
    def nested102_RelatedTo(self):
        return self.__nested102_RelatedTo

    @nested102_RelatedTo.setter
    def nested102_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nested102_RelatedTo__nested102_RelatedTo", None)
        self.__nested102_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nested102_Thing6"):
                opp_val = getattr(old_value, "nested102_Thing6", None)
                if opp_val == self:
                    setattr(old_value, "nested102_Thing6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nested102_Thing6"):
                opp_val = getattr(value, "nested102_Thing6", None)
                setattr(value, "nested102_Thing6", self)

    @property
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nested102_RelatedTo__RelatedTo", None)
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

class nested102_EClass3(NamedElement):

    pass
class nested102_EClass4(NamedElement):

    pass
class nested102_EClass2(NamedElement):

    pass
class nested102_EClass8(NamedElement):

    pass
class nested102_EClass0(NamedElement):

    pass
class nested102_Thing(NamedElement):

    def __init__(self, id: int, nested102_Thing: "nested102_World" = None, fromThing: set["nested102_RelatedTo"] = None, nested102_Thing3: set["nested102_EClass0"] = None, Thing: "nested102_RelatedTo" = None, nested102_Thing6: "nested102_RelatedTo" = None):
        self.id = id
        self.nested102_Thing = nested102_Thing
        self.fromThing = fromThing if fromThing is not None else set()
        self.nested102_Thing3 = nested102_Thing3 if nested102_Thing3 is not None else set()
        self.Thing = Thing
        self.nested102_Thing6 = nested102_Thing6
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def nested102_Thing3(self):
        return self.__nested102_Thing3

    @nested102_Thing3.setter
    def nested102_Thing3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nested102_Thing__nested102_Thing3", None)
        self.__nested102_Thing3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nested102_EClass0"):
                    opp_val = getattr(item, "nested102_EClass0", None)
                    
                    if opp_val == self:
                        setattr(item, "nested102_EClass0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nested102_EClass0"):
                    opp_val = getattr(item, "nested102_EClass0", None)
                    
                    setattr(item, "nested102_EClass0", self)
                    

    @property
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nested102_Thing__Thing", None)
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
    def nested102_Thing6(self):
        return self.__nested102_Thing6

    @nested102_Thing6.setter
    def nested102_Thing6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nested102_Thing__nested102_Thing6", None)
        self.__nested102_Thing6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nested102_RelatedTo"):
                opp_val = getattr(old_value, "nested102_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "nested102_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nested102_RelatedTo"):
                opp_val = getattr(value, "nested102_RelatedTo", None)
                setattr(value, "nested102_RelatedTo", self)

    @property
    def nested102_Thing(self):
        return self.__nested102_Thing

    @nested102_Thing.setter
    def nested102_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nested102_Thing__nested102_Thing", None)
        self.__nested102_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nested102_World"):
                opp_val = getattr(old_value, "nested102_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nested102_World"):
                opp_val = getattr(value, "nested102_World", None)
                if opp_val is None:
                    setattr(value, "nested102_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nested102_Thing__fromThing", None)
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
                    

class nested102_World:

    pass