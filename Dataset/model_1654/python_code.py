from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class helloworldsaved_Alias:

    def __init__(self, id: str, helloworldsaved_Alias: "helloworldsaved_NamedElement" = None):
        self.id = id
        self.helloworldsaved_Alias = helloworldsaved_Alias
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def helloworldsaved_Alias(self):
        return self.__helloworldsaved_Alias

    @helloworldsaved_Alias.setter
    def helloworldsaved_Alias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworldsaved_Alias__helloworldsaved_Alias", None)
        self.__helloworldsaved_Alias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworldsaved_NamedElement"):
                opp_val = getattr(old_value, "helloworldsaved_NamedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworldsaved_NamedElement"):
                opp_val = getattr(value, "helloworldsaved_NamedElement", None)
                if opp_val is None:
                    setattr(value, "helloworldsaved_NamedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class helloworldsaved_RelatedTo(NamedElement):

    def __init__(self, since: str, RelatedTo: "helloworldsaved_Thing" = None, relations: "helloworldsaved_Thing" = None, helloworldsaved_RelatedTo: "helloworldsaved_Thing" = None):
        self.since = since
        self.RelatedTo = RelatedTo
        self.relations = relations
        self.helloworldsaved_RelatedTo = helloworldsaved_RelatedTo
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def helloworldsaved_RelatedTo(self):
        return self.__helloworldsaved_RelatedTo

    @helloworldsaved_RelatedTo.setter
    def helloworldsaved_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworldsaved_RelatedTo__helloworldsaved_RelatedTo", None)
        self.__helloworldsaved_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworldsaved_Thing5"):
                opp_val = getattr(old_value, "helloworldsaved_Thing5", None)
                if opp_val == self:
                    setattr(old_value, "helloworldsaved_Thing5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworldsaved_Thing5"):
                opp_val = getattr(value, "helloworldsaved_Thing5", None)
                setattr(value, "helloworldsaved_Thing5", self)

    @property
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworldsaved_RelatedTo__RelatedTo", None)
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
        old_value = getattr(self, f"_helloworldsaved_RelatedTo__relations", None)
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

class helloworldsaved_Thing(NamedElement):

    def __init__(self, id: int, helloworldsaved_Thing: "helloworldsaved_World" = None, fromThing: set["helloworldsaved_RelatedTo"] = None, Thing: "helloworldsaved_RelatedTo" = None, helloworldsaved_Thing5: "helloworldsaved_RelatedTo" = None):
        self.id = id
        self.helloworldsaved_Thing = helloworldsaved_Thing
        self.fromThing = fromThing if fromThing is not None else set()
        self.Thing = Thing
        self.helloworldsaved_Thing5 = helloworldsaved_Thing5
        
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
        old_value = getattr(self, f"_helloworldsaved_Thing__Thing", None)
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
    def helloworldsaved_Thing(self):
        return self.__helloworldsaved_Thing

    @helloworldsaved_Thing.setter
    def helloworldsaved_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworldsaved_Thing__helloworldsaved_Thing", None)
        self.__helloworldsaved_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworldsaved_World"):
                opp_val = getattr(old_value, "helloworldsaved_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworldsaved_World"):
                opp_val = getattr(value, "helloworldsaved_World", None)
                if opp_val is None:
                    setattr(value, "helloworldsaved_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def helloworldsaved_Thing5(self):
        return self.__helloworldsaved_Thing5

    @helloworldsaved_Thing5.setter
    def helloworldsaved_Thing5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworldsaved_Thing__helloworldsaved_Thing5", None)
        self.__helloworldsaved_Thing5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworldsaved_RelatedTo"):
                opp_val = getattr(old_value, "helloworldsaved_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "helloworldsaved_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworldsaved_RelatedTo"):
                opp_val = getattr(value, "helloworldsaved_RelatedTo", None)
                setattr(value, "helloworldsaved_RelatedTo", self)

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworldsaved_Thing__fromThing", None)
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
                    

class helloworldsaved_World:

    pass
class helloworldsaved_NamedElement(ABC):

    def __init__(self, name: str, helloworldsaved_NamedElement: set["helloworldsaved_Alias"] = None):
        self.name = name
        self.helloworldsaved_NamedElement = helloworldsaved_NamedElement if helloworldsaved_NamedElement is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def helloworldsaved_NamedElement(self):
        return self.__helloworldsaved_NamedElement

    @helloworldsaved_NamedElement.setter
    def helloworldsaved_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworldsaved_NamedElement__helloworldsaved_NamedElement", None)
        self.__helloworldsaved_NamedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "helloworldsaved_Alias"):
                    opp_val = getattr(item, "helloworldsaved_Alias", None)
                    
                    if opp_val == self:
                        setattr(item, "helloworldsaved_Alias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "helloworldsaved_Alias"):
                    opp_val = getattr(item, "helloworldsaved_Alias", None)
                    
                    setattr(item, "helloworldsaved_Alias", self)
                    
