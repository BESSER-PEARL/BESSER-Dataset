from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class helloworld123_Alias:

    def __init__(self, id: str, helloworld123_Alias: "helloworld123_NamedElement" = None):
        self.id = id
        self.helloworld123_Alias = helloworld123_Alias
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def helloworld123_Alias(self):
        return self.__helloworld123_Alias

    @helloworld123_Alias.setter
    def helloworld123_Alias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld123_Alias__helloworld123_Alias", None)
        self.__helloworld123_Alias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld123_NamedElement"):
                opp_val = getattr(old_value, "helloworld123_NamedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld123_NamedElement"):
                opp_val = getattr(value, "helloworld123_NamedElement", None)
                if opp_val is None:
                    setattr(value, "helloworld123_NamedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class helloworld123_World:

    pass
class helloworld123_NamedElement(ABC):

    def __init__(self, name: str, helloworld123_NamedElement: set["helloworld123_Alias"] = None):
        self.name = name
        self.helloworld123_NamedElement = helloworld123_NamedElement if helloworld123_NamedElement is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def helloworld123_NamedElement(self):
        return self.__helloworld123_NamedElement

    @helloworld123_NamedElement.setter
    def helloworld123_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld123_NamedElement__helloworld123_NamedElement", None)
        self.__helloworld123_NamedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "helloworld123_Alias"):
                    opp_val = getattr(item, "helloworld123_Alias", None)
                    
                    if opp_val == self:
                        setattr(item, "helloworld123_Alias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "helloworld123_Alias"):
                    opp_val = getattr(item, "helloworld123_Alias", None)
                    
                    setattr(item, "helloworld123_Alias", self)
                    

class NamedElement:

    pass
class helloworld123_Thing(NamedElement):

    def __init__(self, id: int, helloworld123_Thing5: "helloworld123_RelatedTo" = None, fromThing: set["helloworld123_RelatedTo"] = None, helloworld123_Thing: "helloworld123_World" = None, Thing: "helloworld123_RelatedTo" = None):
        self.id = id
        self.helloworld123_Thing5 = helloworld123_Thing5
        self.fromThing = fromThing if fromThing is not None else set()
        self.helloworld123_Thing = helloworld123_Thing
        self.Thing = Thing
        
        pass
    @property
    def id(self):
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
        old_value = getattr(self, f"_helloworld123_Thing__Thing", None)
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
        old_value = getattr(self, f"_helloworld123_Thing__fromThing", None)
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
    def helloworld123_Thing(self):
        return self.__helloworld123_Thing

    @helloworld123_Thing.setter
    def helloworld123_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld123_Thing__helloworld123_Thing", None)
        self.__helloworld123_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld123_World"):
                opp_val = getattr(old_value, "helloworld123_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld123_World"):
                opp_val = getattr(value, "helloworld123_World", None)
                if opp_val is None:
                    setattr(value, "helloworld123_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def helloworld123_Thing5(self):
        return self.__helloworld123_Thing5

    @helloworld123_Thing5.setter
    def helloworld123_Thing5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld123_Thing__helloworld123_Thing5", None)
        self.__helloworld123_Thing5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld123_RelatedTo"):
                opp_val = getattr(old_value, "helloworld123_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "helloworld123_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld123_RelatedTo"):
                opp_val = getattr(value, "helloworld123_RelatedTo", None)
                setattr(value, "helloworld123_RelatedTo", self)

class helloworld123_RelatedTo(NamedElement):

    def __init__(self, since: str, helloworld123_RelatedTo: "helloworld123_Thing" = None, RelatedTo: "helloworld123_Thing" = None, relations: "helloworld123_Thing" = None):
        self.since = since
        self.helloworld123_RelatedTo = helloworld123_RelatedTo
        self.RelatedTo = RelatedTo
        self.relations = relations
        
        pass
    @property
    def since(self):
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since


    @property
    def helloworld123_RelatedTo(self):
        return self.__helloworld123_RelatedTo

    @helloworld123_RelatedTo.setter
    def helloworld123_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld123_RelatedTo__helloworld123_RelatedTo", None)
        self.__helloworld123_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld123_Thing5"):
                opp_val = getattr(old_value, "helloworld123_Thing5", None)
                if opp_val == self:
                    setattr(old_value, "helloworld123_Thing5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld123_Thing5"):
                opp_val = getattr(value, "helloworld123_Thing5", None)
                setattr(value, "helloworld123_Thing5", self)

    @property
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld123_RelatedTo__RelatedTo", None)
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
        old_value = getattr(self, f"_helloworld123_RelatedTo__relations", None)
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
