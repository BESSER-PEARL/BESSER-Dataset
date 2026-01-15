from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ktest400_NamedElement(ABC):

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
class ktest400_RelatedTo(NamedElement):

    def __init__(self, since: str, relations: "ktest400_Thing" = None, ktest400_RelatedTo: "ktest400_Thing" = None, RelatedTo: "ktest400_Thing" = None):
        self.since = since
        self.relations = relations
        self.ktest400_RelatedTo = ktest400_RelatedTo
        self.RelatedTo = RelatedTo
        
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
        old_value = getattr(self, f"_ktest400_RelatedTo__relations", None)
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
    def ktest400_RelatedTo(self):
        return self.__ktest400_RelatedTo

    @ktest400_RelatedTo.setter
    def ktest400_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest400_RelatedTo__ktest400_RelatedTo", None)
        self.__ktest400_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest400_Thing8"):
                opp_val = getattr(old_value, "ktest400_Thing8", None)
                if opp_val == self:
                    setattr(old_value, "ktest400_Thing8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest400_Thing8"):
                opp_val = getattr(value, "ktest400_Thing8", None)
                setattr(value, "ktest400_Thing8", self)

    @property
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest400_RelatedTo__RelatedTo", None)
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

class ktest400_Line(NamedElement):

    def __init__(self, quant: int, articleAid: str, ktest400_Line: "ktest400_Thing" = None, ktest400_Line10: "ktest400_Thing" = None, ktest400_Line13: "ktest400_Article" = None):
        self.quant = quant
        self.articleAid = articleAid
        self.ktest400_Line = ktest400_Line
        self.ktest400_Line10 = ktest400_Line10
        self.ktest400_Line13 = ktest400_Line13
        
    @property
    def quant(self) -> int:
        return self.__quant

    @quant.setter
    def quant(self, quant: int):
        self.__quant = quant

    @property
    def articleAid(self) -> str:
        return self.__articleAid

    @articleAid.setter
    def articleAid(self, articleAid: str):
        self.__articleAid = articleAid

    @property
    def ktest400_Line(self):
        return self.__ktest400_Line

    @ktest400_Line.setter
    def ktest400_Line(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest400_Line__ktest400_Line", None)
        self.__ktest400_Line = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest400_Thing5"):
                opp_val = getattr(old_value, "ktest400_Thing5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest400_Thing5"):
                opp_val = getattr(value, "ktest400_Thing5", None)
                if opp_val is None:
                    setattr(value, "ktest400_Thing5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ktest400_Line13(self):
        return self.__ktest400_Line13

    @ktest400_Line13.setter
    def ktest400_Line13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest400_Line__ktest400_Line13", None)
        self.__ktest400_Line13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest400_Article14"):
                opp_val = getattr(old_value, "ktest400_Article14", None)
                if opp_val == self:
                    setattr(old_value, "ktest400_Article14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest400_Article14"):
                opp_val = getattr(value, "ktest400_Article14", None)
                setattr(value, "ktest400_Article14", self)

    @property
    def ktest400_Line10(self):
        return self.__ktest400_Line10

    @ktest400_Line10.setter
    def ktest400_Line10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest400_Line__ktest400_Line10", None)
        self.__ktest400_Line10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest400_Thing11"):
                opp_val = getattr(old_value, "ktest400_Thing11", None)
                if opp_val == self:
                    setattr(old_value, "ktest400_Thing11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest400_Thing11"):
                opp_val = getattr(value, "ktest400_Thing11", None)
                setattr(value, "ktest400_Thing11", self)

class ktest400_Article(NamedElement):

    def __init__(self, aid: str, ktest400_Article: "ktest400_World" = None, ktest400_Article14: "ktest400_Line" = None):
        self.aid = aid
        self.ktest400_Article = ktest400_Article
        self.ktest400_Article14 = ktest400_Article14
        
    @property
    def aid(self) -> str:
        return self.__aid

    @aid.setter
    def aid(self, aid: str):
        self.__aid = aid

    @property
    def ktest400_Article14(self):
        return self.__ktest400_Article14

    @ktest400_Article14.setter
    def ktest400_Article14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest400_Article__ktest400_Article14", None)
        self.__ktest400_Article14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest400_Line13"):
                opp_val = getattr(old_value, "ktest400_Line13", None)
                if opp_val == self:
                    setattr(old_value, "ktest400_Line13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest400_Line13"):
                opp_val = getattr(value, "ktest400_Line13", None)
                setattr(value, "ktest400_Line13", self)

    @property
    def ktest400_Article(self):
        return self.__ktest400_Article

    @ktest400_Article.setter
    def ktest400_Article(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest400_Article__ktest400_Article", None)
        self.__ktest400_Article = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest400_World2"):
                opp_val = getattr(old_value, "ktest400_World2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest400_World2"):
                opp_val = getattr(value, "ktest400_World2", None)
                if opp_val is None:
                    setattr(value, "ktest400_World2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ktest400_Thing(NamedElement):

    def __init__(self, id: int, ktest400_Thing: "ktest400_World" = None, Thing: "ktest400_RelatedTo" = None, ktest400_Thing8: "ktest400_RelatedTo" = None, fromThing: set["ktest400_RelatedTo"] = None, ktest400_Thing5: set["ktest400_Line"] = None, ktest400_Thing11: "ktest400_Line" = None):
        self.id = id
        self.ktest400_Thing = ktest400_Thing
        self.Thing = Thing
        self.ktest400_Thing8 = ktest400_Thing8
        self.fromThing = fromThing if fromThing is not None else set()
        self.ktest400_Thing5 = ktest400_Thing5 if ktest400_Thing5 is not None else set()
        self.ktest400_Thing11 = ktest400_Thing11
        
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
        old_value = getattr(self, f"_ktest400_Thing__Thing", None)
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
    def ktest400_Thing(self):
        return self.__ktest400_Thing

    @ktest400_Thing.setter
    def ktest400_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest400_Thing__ktest400_Thing", None)
        self.__ktest400_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest400_World"):
                opp_val = getattr(old_value, "ktest400_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest400_World"):
                opp_val = getattr(value, "ktest400_World", None)
                if opp_val is None:
                    setattr(value, "ktest400_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ktest400_Thing8(self):
        return self.__ktest400_Thing8

    @ktest400_Thing8.setter
    def ktest400_Thing8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest400_Thing__ktest400_Thing8", None)
        self.__ktest400_Thing8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest400_RelatedTo"):
                opp_val = getattr(old_value, "ktest400_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "ktest400_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest400_RelatedTo"):
                opp_val = getattr(value, "ktest400_RelatedTo", None)
                setattr(value, "ktest400_RelatedTo", self)

    @property
    def ktest400_Thing11(self):
        return self.__ktest400_Thing11

    @ktest400_Thing11.setter
    def ktest400_Thing11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest400_Thing__ktest400_Thing11", None)
        self.__ktest400_Thing11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest400_Line10"):
                opp_val = getattr(old_value, "ktest400_Line10", None)
                if opp_val == self:
                    setattr(old_value, "ktest400_Line10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest400_Line10"):
                opp_val = getattr(value, "ktest400_Line10", None)
                setattr(value, "ktest400_Line10", self)

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest400_Thing__fromThing", None)
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
    def ktest400_Thing5(self):
        return self.__ktest400_Thing5

    @ktest400_Thing5.setter
    def ktest400_Thing5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest400_Thing__ktest400_Thing5", None)
        self.__ktest400_Thing5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ktest400_Line"):
                    opp_val = getattr(item, "ktest400_Line", None)
                    
                    if opp_val == self:
                        setattr(item, "ktest400_Line", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ktest400_Line"):
                    opp_val = getattr(item, "ktest400_Line", None)
                    
                    setattr(item, "ktest400_Line", self)
                    

class ktest400_World:

    pass