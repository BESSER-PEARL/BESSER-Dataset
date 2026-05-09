from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class yyaa_Alias:

    def __init__(self, id: str, yyaa_Alias: "yyaa_NamedElement" = None):
        self.id = id
        self.yyaa_Alias = yyaa_Alias
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def yyaa_Alias(self):
        return self.__yyaa_Alias

    @yyaa_Alias.setter
    def yyaa_Alias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyaa_Alias__yyaa_Alias", None)
        self.__yyaa_Alias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyaa_NamedElement"):
                opp_val = getattr(old_value, "yyaa_NamedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyaa_NamedElement"):
                opp_val = getattr(value, "yyaa_NamedElement", None)
                if opp_val is None:
                    setattr(value, "yyaa_NamedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yyaa_NamedElement(ABC):

    def __init__(self, name: str, yyaa_NamedElement: set["yyaa_Alias"] = None):
        self.name = name
        self.yyaa_NamedElement = yyaa_NamedElement if yyaa_NamedElement is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def yyaa_NamedElement(self):
        return self.__yyaa_NamedElement

    @yyaa_NamedElement.setter
    def yyaa_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyaa_NamedElement__yyaa_NamedElement", None)
        self.__yyaa_NamedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyaa_Alias"):
                    opp_val = getattr(item, "yyaa_Alias", None)
                    
                    if opp_val == self:
                        setattr(item, "yyaa_Alias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyaa_Alias"):
                    opp_val = getattr(item, "yyaa_Alias", None)
                    
                    setattr(item, "yyaa_Alias", self)
                    

class NamedElement:

    pass
class yyaa_RelatedTo(NamedElement):

    def __init__(self, since: str, RelatedTo: "yyaa_Thing" = None, relations: "yyaa_Thing" = None, yyaa_RelatedTo: "yyaa_Thing" = None):
        self.since = since
        self.RelatedTo = RelatedTo
        self.relations = relations
        self.yyaa_RelatedTo = yyaa_RelatedTo
        
        pass
    @property
    def since(self):
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since


    @property
    def yyaa_RelatedTo(self):
        return self.__yyaa_RelatedTo

    @yyaa_RelatedTo.setter
    def yyaa_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyaa_RelatedTo__yyaa_RelatedTo", None)
        self.__yyaa_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyaa_Thing5"):
                opp_val = getattr(old_value, "yyaa_Thing5", None)
                if opp_val == self:
                    setattr(old_value, "yyaa_Thing5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyaa_Thing5"):
                opp_val = getattr(value, "yyaa_Thing5", None)
                setattr(value, "yyaa_Thing5", self)

    @property
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyaa_RelatedTo__RelatedTo", None)
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
        old_value = getattr(self, f"_yyaa_RelatedTo__relations", None)
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

class yyaa_Thing(NamedElement):

    def __init__(self, id: int, yyaa_Thing: "yyaa_World" = None, fromThing: set["yyaa_RelatedTo"] = None, Thing: "yyaa_RelatedTo" = None, yyaa_Thing5: "yyaa_RelatedTo" = None):
        self.id = id
        self.yyaa_Thing = yyaa_Thing
        self.fromThing = fromThing if fromThing is not None else set()
        self.Thing = Thing
        self.yyaa_Thing5 = yyaa_Thing5
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def yyaa_Thing5(self):
        return self.__yyaa_Thing5

    @yyaa_Thing5.setter
    def yyaa_Thing5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyaa_Thing__yyaa_Thing5", None)
        self.__yyaa_Thing5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyaa_RelatedTo"):
                opp_val = getattr(old_value, "yyaa_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "yyaa_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyaa_RelatedTo"):
                opp_val = getattr(value, "yyaa_RelatedTo", None)
                setattr(value, "yyaa_RelatedTo", self)

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyaa_Thing__fromThing", None)
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
    def yyaa_Thing(self):
        return self.__yyaa_Thing

    @yyaa_Thing.setter
    def yyaa_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyaa_Thing__yyaa_Thing", None)
        self.__yyaa_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyaa_World"):
                opp_val = getattr(old_value, "yyaa_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyaa_World"):
                opp_val = getattr(value, "yyaa_World", None)
                if opp_val is None:
                    setattr(value, "yyaa_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyaa_Thing__Thing", None)
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

class yyaa_World:

    pass