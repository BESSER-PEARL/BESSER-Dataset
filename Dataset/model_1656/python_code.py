from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class simpleparts_NamedElement(ABC):

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
class simpleparts_Piece(NamedElement):

    pass
class simpleparts_Item(NamedElement):

    pass
class simpleparts_Part(NamedElement):

    pass
class simpleparts_RelatedTo(NamedElement):

    def __init__(self, since: str, RelatedTo: "simpleparts_Thing" = None, relations: "simpleparts_Thing" = None, simpleparts_RelatedTo: "simpleparts_Thing" = None):
        self.since = since
        self.RelatedTo = RelatedTo
        self.relations = relations
        self.simpleparts_RelatedTo = simpleparts_RelatedTo
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def simpleparts_RelatedTo(self):
        return self.__simpleparts_RelatedTo

    @simpleparts_RelatedTo.setter
    def simpleparts_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleparts_RelatedTo__simpleparts_RelatedTo", None)
        self.__simpleparts_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleparts_Thing12"):
                opp_val = getattr(old_value, "simpleparts_Thing12", None)
                if opp_val == self:
                    setattr(old_value, "simpleparts_Thing12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleparts_Thing12"):
                opp_val = getattr(value, "simpleparts_Thing12", None)
                setattr(value, "simpleparts_Thing12", self)

    @property
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleparts_RelatedTo__RelatedTo", None)
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
        old_value = getattr(self, f"_simpleparts_RelatedTo__relations", None)
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

class simpleparts_Element(NamedElement):

    pass
class simpleparts_Thing(NamedElement):

    def __init__(self, id: int, simpleparts_Thing: "simpleparts_World" = None, simpleparts_Thing5: set["simpleparts_Element"] = None, simpleparts_Thing7: set["simpleparts_Item"] = None, simpleparts_Thing9: set["simpleparts_Piece"] = None, fromThing: set["simpleparts_RelatedTo"] = None, simpleparts_Thing3: set["simpleparts_Part"] = None, Thing: "simpleparts_RelatedTo" = None, simpleparts_Thing12: "simpleparts_RelatedTo" = None):
        self.id = id
        self.simpleparts_Thing = simpleparts_Thing
        self.simpleparts_Thing5 = simpleparts_Thing5 if simpleparts_Thing5 is not None else set()
        self.simpleparts_Thing7 = simpleparts_Thing7 if simpleparts_Thing7 is not None else set()
        self.simpleparts_Thing9 = simpleparts_Thing9 if simpleparts_Thing9 is not None else set()
        self.fromThing = fromThing if fromThing is not None else set()
        self.simpleparts_Thing3 = simpleparts_Thing3 if simpleparts_Thing3 is not None else set()
        self.Thing = Thing
        self.simpleparts_Thing12 = simpleparts_Thing12
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def simpleparts_Thing3(self):
        return self.__simpleparts_Thing3

    @simpleparts_Thing3.setter
    def simpleparts_Thing3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleparts_Thing__simpleparts_Thing3", None)
        self.__simpleparts_Thing3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleparts_Part"):
                    opp_val = getattr(item, "simpleparts_Part", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleparts_Part", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleparts_Part"):
                    opp_val = getattr(item, "simpleparts_Part", None)
                    
                    setattr(item, "simpleparts_Part", self)
                    

    @property
    def simpleparts_Thing7(self):
        return self.__simpleparts_Thing7

    @simpleparts_Thing7.setter
    def simpleparts_Thing7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleparts_Thing__simpleparts_Thing7", None)
        self.__simpleparts_Thing7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleparts_Item"):
                    opp_val = getattr(item, "simpleparts_Item", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleparts_Item", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleparts_Item"):
                    opp_val = getattr(item, "simpleparts_Item", None)
                    
                    setattr(item, "simpleparts_Item", self)
                    

    @property
    def simpleparts_Thing12(self):
        return self.__simpleparts_Thing12

    @simpleparts_Thing12.setter
    def simpleparts_Thing12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleparts_Thing__simpleparts_Thing12", None)
        self.__simpleparts_Thing12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleparts_RelatedTo"):
                opp_val = getattr(old_value, "simpleparts_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "simpleparts_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleparts_RelatedTo"):
                opp_val = getattr(value, "simpleparts_RelatedTo", None)
                setattr(value, "simpleparts_RelatedTo", self)

    @property
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleparts_Thing__Thing", None)
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
    def simpleparts_Thing9(self):
        return self.__simpleparts_Thing9

    @simpleparts_Thing9.setter
    def simpleparts_Thing9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleparts_Thing__simpleparts_Thing9", None)
        self.__simpleparts_Thing9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleparts_Piece"):
                    opp_val = getattr(item, "simpleparts_Piece", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleparts_Piece", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleparts_Piece"):
                    opp_val = getattr(item, "simpleparts_Piece", None)
                    
                    setattr(item, "simpleparts_Piece", self)
                    

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleparts_Thing__fromThing", None)
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
    def simpleparts_Thing(self):
        return self.__simpleparts_Thing

    @simpleparts_Thing.setter
    def simpleparts_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleparts_Thing__simpleparts_Thing", None)
        self.__simpleparts_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleparts_World"):
                opp_val = getattr(old_value, "simpleparts_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleparts_World"):
                opp_val = getattr(value, "simpleparts_World", None)
                if opp_val is None:
                    setattr(value, "simpleparts_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleparts_Thing5(self):
        return self.__simpleparts_Thing5

    @simpleparts_Thing5.setter
    def simpleparts_Thing5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleparts_Thing__simpleparts_Thing5", None)
        self.__simpleparts_Thing5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleparts_Element"):
                    opp_val = getattr(item, "simpleparts_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleparts_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleparts_Element"):
                    opp_val = getattr(item, "simpleparts_Element", None)
                    
                    setattr(item, "simpleparts_Element", self)
                    

class simpleparts_World:

    pass