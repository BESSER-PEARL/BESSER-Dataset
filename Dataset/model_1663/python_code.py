from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class nested103_EClass12(ABC):

    pass
class Thing:

    pass
class nested103_EClass7(Thing):

    pass
class nested103_EClass11(ABC):

    pass
class EClass9:

    pass
class nested103_EClass13:

    pass
class EClass12:

    pass
class EClass11:

    pass
class nested103_EClass9(EClass11, EClass12):

    def __init__(self, name: str, nested103_EClass9: set["nested103_EClass13"] = None):
        self.name = name
        self.nested103_EClass9 = nested103_EClass9 if nested103_EClass9 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nested103_EClass9(self):
        return self.__nested103_EClass9

    @nested103_EClass9.setter
    def nested103_EClass9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nested103_EClass9__nested103_EClass9", None)
        self.__nested103_EClass9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nested103_EClass13"):
                    opp_val = getattr(item, "nested103_EClass13", None)
                    
                    if opp_val == self:
                        setattr(item, "nested103_EClass13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nested103_EClass13"):
                    opp_val = getattr(item, "nested103_EClass13", None)
                    
                    setattr(item, "nested103_EClass13", self)
                    

class EClass8:

    pass
class EClass7:

    pass
class nested103_EClass6(EClass7, EClass8):

    pass
class EClass6:

    pass
class nested103_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class nested103_World:

    pass
class NamedElement:

    pass
class nested103_EClass8(NamedElement):

    pass
class nested103_EClass5(NamedElement, EClass6):

    pass
class nested103_EClass1(NamedElement):

    pass
class nested103_EClass4(NamedElement):

    pass
class nested103_EClass2(NamedElement):

    pass
class nested103_RelatedTo(NamedElement):

    def __init__(self, since: str, RelatedTo: "nested103_Thing" = None, relations: "nested103_Thing" = None, nested103_RelatedTo: "nested103_Thing" = None):
        self.since = since
        self.RelatedTo = RelatedTo
        self.relations = relations
        self.nested103_RelatedTo = nested103_RelatedTo
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def nested103_RelatedTo(self):
        return self.__nested103_RelatedTo

    @nested103_RelatedTo.setter
    def nested103_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nested103_RelatedTo__nested103_RelatedTo", None)
        self.__nested103_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nested103_Thing8"):
                opp_val = getattr(old_value, "nested103_Thing8", None)
                if opp_val == self:
                    setattr(old_value, "nested103_Thing8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nested103_Thing8"):
                opp_val = getattr(value, "nested103_Thing8", None)
                setattr(value, "nested103_Thing8", self)

    @property
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nested103_RelatedTo__RelatedTo", None)
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
        old_value = getattr(self, f"_nested103_RelatedTo__relations", None)
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

class nested103_EClass3(NamedElement):

    pass
class nested103_EClass0(NamedElement):

    pass
class nested103_EClass10(EClass9):

    pass
class nested103_Thing(NamedElement):

    def __init__(self, id: int, nested103_Thing: "nested103_World" = None, fromThing: set["nested103_RelatedTo"] = None, Thing: "nested103_RelatedTo" = None, nested103_Thing8: "nested103_RelatedTo" = None, nested103_Thing5: set["nested103_EClass0"] = None):
        self.id = id
        self.nested103_Thing = nested103_Thing
        self.fromThing = fromThing if fromThing is not None else set()
        self.Thing = Thing
        self.nested103_Thing8 = nested103_Thing8
        self.nested103_Thing5 = nested103_Thing5 if nested103_Thing5 is not None else set()
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def nested103_Thing(self):
        return self.__nested103_Thing

    @nested103_Thing.setter
    def nested103_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nested103_Thing__nested103_Thing", None)
        self.__nested103_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nested103_World"):
                opp_val = getattr(old_value, "nested103_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nested103_World"):
                opp_val = getattr(value, "nested103_World", None)
                if opp_val is None:
                    setattr(value, "nested103_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nested103_Thing5(self):
        return self.__nested103_Thing5

    @nested103_Thing5.setter
    def nested103_Thing5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nested103_Thing__nested103_Thing5", None)
        self.__nested103_Thing5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nested103_EClass0"):
                    opp_val = getattr(item, "nested103_EClass0", None)
                    
                    if opp_val == self:
                        setattr(item, "nested103_EClass0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nested103_EClass0"):
                    opp_val = getattr(item, "nested103_EClass0", None)
                    
                    setattr(item, "nested103_EClass0", self)
                    

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nested103_Thing__fromThing", None)
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
        old_value = getattr(self, f"_nested103_Thing__Thing", None)
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
    def nested103_Thing8(self):
        return self.__nested103_Thing8

    @nested103_Thing8.setter
    def nested103_Thing8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nested103_Thing__nested103_Thing8", None)
        self.__nested103_Thing8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nested103_RelatedTo"):
                opp_val = getattr(old_value, "nested103_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "nested103_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nested103_RelatedTo"):
                opp_val = getattr(value, "nested103_RelatedTo", None)
                setattr(value, "nested103_RelatedTo", self)
