from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class ktest401_Line(NamedElement):

    def __init__(self, quant: int, articleAid: str, ktest401_Line: "ktest401_Thing" = None, ktest401_Line14: "ktest401_Thing" = None, ktest401_Line17: "ktest401_Article" = None):
        self.quant = quant
        self.articleAid = articleAid
        self.ktest401_Line = ktest401_Line
        self.ktest401_Line14 = ktest401_Line14
        self.ktest401_Line17 = ktest401_Line17
        
    @property
    def articleAid(self) -> str:
        return self.__articleAid

    @articleAid.setter
    def articleAid(self, articleAid: str):
        self.__articleAid = articleAid

    @property
    def quant(self) -> int:
        return self.__quant

    @quant.setter
    def quant(self, quant: int):
        self.__quant = quant

    @property
    def ktest401_Line(self):
        return self.__ktest401_Line

    @ktest401_Line.setter
    def ktest401_Line(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest401_Line__ktest401_Line", None)
        self.__ktest401_Line = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest401_Thing5"):
                opp_val = getattr(old_value, "ktest401_Thing5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest401_Thing5"):
                opp_val = getattr(value, "ktest401_Thing5", None)
                if opp_val is None:
                    setattr(value, "ktest401_Thing5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ktest401_Line17(self):
        return self.__ktest401_Line17

    @ktest401_Line17.setter
    def ktest401_Line17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest401_Line__ktest401_Line17", None)
        self.__ktest401_Line17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest401_Article18"):
                opp_val = getattr(old_value, "ktest401_Article18", None)
                if opp_val == self:
                    setattr(old_value, "ktest401_Article18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest401_Article18"):
                opp_val = getattr(value, "ktest401_Article18", None)
                setattr(value, "ktest401_Article18", self)

    @property
    def ktest401_Line14(self):
        return self.__ktest401_Line14

    @ktest401_Line14.setter
    def ktest401_Line14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest401_Line__ktest401_Line14", None)
        self.__ktest401_Line14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest401_Thing15"):
                opp_val = getattr(old_value, "ktest401_Thing15", None)
                if opp_val == self:
                    setattr(old_value, "ktest401_Thing15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest401_Thing15"):
                opp_val = getattr(value, "ktest401_Thing15", None)
                setattr(value, "ktest401_Thing15", self)

class ktest401_EClass0(NamedElement):

    pass
class ktest401_RelatedTo(NamedElement):

    def __init__(self, since: str, RelatedTo: "ktest401_Thing" = None, ktest401_RelatedTo21: "ktest401_EClass1" = None, relations: "ktest401_Thing" = None, ktest401_RelatedTo: "ktest401_Thing" = None, ktest401_RelatedTo12: set["ktest401_EClass1"] = None):
        self.since = since
        self.RelatedTo = RelatedTo
        self.ktest401_RelatedTo21 = ktest401_RelatedTo21
        self.relations = relations
        self.ktest401_RelatedTo = ktest401_RelatedTo
        self.ktest401_RelatedTo12 = ktest401_RelatedTo12 if ktest401_RelatedTo12 is not None else set()
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def ktest401_RelatedTo(self):
        return self.__ktest401_RelatedTo

    @ktest401_RelatedTo.setter
    def ktest401_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest401_RelatedTo__ktest401_RelatedTo", None)
        self.__ktest401_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest401_Thing10"):
                opp_val = getattr(old_value, "ktest401_Thing10", None)
                if opp_val == self:
                    setattr(old_value, "ktest401_Thing10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest401_Thing10"):
                opp_val = getattr(value, "ktest401_Thing10", None)
                setattr(value, "ktest401_Thing10", self)

    @property
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest401_RelatedTo__RelatedTo", None)
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
        old_value = getattr(self, f"_ktest401_RelatedTo__relations", None)
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
    def ktest401_RelatedTo21(self):
        return self.__ktest401_RelatedTo21

    @ktest401_RelatedTo21.setter
    def ktest401_RelatedTo21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest401_RelatedTo__ktest401_RelatedTo21", None)
        self.__ktest401_RelatedTo21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest401_EClass120"):
                opp_val = getattr(old_value, "ktest401_EClass120", None)
                if opp_val == self:
                    setattr(old_value, "ktest401_EClass120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest401_EClass120"):
                opp_val = getattr(value, "ktest401_EClass120", None)
                setattr(value, "ktest401_EClass120", self)

    @property
    def ktest401_RelatedTo12(self):
        return self.__ktest401_RelatedTo12

    @ktest401_RelatedTo12.setter
    def ktest401_RelatedTo12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest401_RelatedTo__ktest401_RelatedTo12", None)
        self.__ktest401_RelatedTo12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ktest401_EClass1"):
                    opp_val = getattr(item, "ktest401_EClass1", None)
                    
                    if opp_val == self:
                        setattr(item, "ktest401_EClass1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ktest401_EClass1"):
                    opp_val = getattr(item, "ktest401_EClass1", None)
                    
                    setattr(item, "ktest401_EClass1", self)
                    

class ktest401_EClass1(NamedElement):

    def __init__(self, foo: str, bar: str, ktest401_EClass120: "ktest401_RelatedTo" = None, ktest401_EClass1: "ktest401_RelatedTo" = None, ktest401_EClass123: "ktest401_EClass0" = None):
        self.foo = foo
        self.bar = bar
        self.ktest401_EClass120 = ktest401_EClass120
        self.ktest401_EClass1 = ktest401_EClass1
        self.ktest401_EClass123 = ktest401_EClass123
        
    @property
    def bar(self) -> str:
        return self.__bar

    @bar.setter
    def bar(self, bar: str):
        self.__bar = bar

    @property
    def foo(self) -> str:
        return self.__foo

    @foo.setter
    def foo(self, foo: str):
        self.__foo = foo

    @property
    def ktest401_EClass120(self):
        return self.__ktest401_EClass120

    @ktest401_EClass120.setter
    def ktest401_EClass120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest401_EClass1__ktest401_EClass120", None)
        self.__ktest401_EClass120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest401_RelatedTo21"):
                opp_val = getattr(old_value, "ktest401_RelatedTo21", None)
                if opp_val == self:
                    setattr(old_value, "ktest401_RelatedTo21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest401_RelatedTo21"):
                opp_val = getattr(value, "ktest401_RelatedTo21", None)
                setattr(value, "ktest401_RelatedTo21", self)

    @property
    def ktest401_EClass1(self):
        return self.__ktest401_EClass1

    @ktest401_EClass1.setter
    def ktest401_EClass1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest401_EClass1__ktest401_EClass1", None)
        self.__ktest401_EClass1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest401_RelatedTo12"):
                opp_val = getattr(old_value, "ktest401_RelatedTo12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest401_RelatedTo12"):
                opp_val = getattr(value, "ktest401_RelatedTo12", None)
                if opp_val is None:
                    setattr(value, "ktest401_RelatedTo12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ktest401_EClass123(self):
        return self.__ktest401_EClass123

    @ktest401_EClass123.setter
    def ktest401_EClass123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest401_EClass1__ktest401_EClass123", None)
        self.__ktest401_EClass123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest401_EClass024"):
                opp_val = getattr(old_value, "ktest401_EClass024", None)
                if opp_val == self:
                    setattr(old_value, "ktest401_EClass024", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest401_EClass024"):
                opp_val = getattr(value, "ktest401_EClass024", None)
                setattr(value, "ktest401_EClass024", self)

class ktest401_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ktest401_World:

    pass
class ktest401_Article(NamedElement):

    def __init__(self, aid: str, ktest401_Article: "ktest401_World" = None, ktest401_Article18: "ktest401_Line" = None):
        self.aid = aid
        self.ktest401_Article = ktest401_Article
        self.ktest401_Article18 = ktest401_Article18
        
    @property
    def aid(self) -> str:
        return self.__aid

    @aid.setter
    def aid(self, aid: str):
        self.__aid = aid

    @property
    def ktest401_Article(self):
        return self.__ktest401_Article

    @ktest401_Article.setter
    def ktest401_Article(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest401_Article__ktest401_Article", None)
        self.__ktest401_Article = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest401_World2"):
                opp_val = getattr(old_value, "ktest401_World2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest401_World2"):
                opp_val = getattr(value, "ktest401_World2", None)
                if opp_val is None:
                    setattr(value, "ktest401_World2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ktest401_Article18(self):
        return self.__ktest401_Article18

    @ktest401_Article18.setter
    def ktest401_Article18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest401_Article__ktest401_Article18", None)
        self.__ktest401_Article18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest401_Line17"):
                opp_val = getattr(old_value, "ktest401_Line17", None)
                if opp_val == self:
                    setattr(old_value, "ktest401_Line17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest401_Line17"):
                opp_val = getattr(value, "ktest401_Line17", None)
                setattr(value, "ktest401_Line17", self)

class ktest401_Thing(NamedElement):

    def __init__(self, id: int, ktest401_Thing: "ktest401_World" = None, ktest401_Thing7: set["ktest401_EClass0"] = None, fromThing: set["ktest401_RelatedTo"] = None, ktest401_Thing5: set["ktest401_Line"] = None, Thing: "ktest401_RelatedTo" = None, ktest401_Thing10: "ktest401_RelatedTo" = None, ktest401_Thing15: "ktest401_Line" = None):
        self.id = id
        self.ktest401_Thing = ktest401_Thing
        self.ktest401_Thing7 = ktest401_Thing7 if ktest401_Thing7 is not None else set()
        self.fromThing = fromThing if fromThing is not None else set()
        self.ktest401_Thing5 = ktest401_Thing5 if ktest401_Thing5 is not None else set()
        self.Thing = Thing
        self.ktest401_Thing10 = ktest401_Thing10
        self.ktest401_Thing15 = ktest401_Thing15
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def ktest401_Thing(self):
        return self.__ktest401_Thing

    @ktest401_Thing.setter
    def ktest401_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest401_Thing__ktest401_Thing", None)
        self.__ktest401_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest401_World"):
                opp_val = getattr(old_value, "ktest401_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest401_World"):
                opp_val = getattr(value, "ktest401_World", None)
                if opp_val is None:
                    setattr(value, "ktest401_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ktest401_Thing10(self):
        return self.__ktest401_Thing10

    @ktest401_Thing10.setter
    def ktest401_Thing10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest401_Thing__ktest401_Thing10", None)
        self.__ktest401_Thing10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest401_RelatedTo"):
                opp_val = getattr(old_value, "ktest401_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "ktest401_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest401_RelatedTo"):
                opp_val = getattr(value, "ktest401_RelatedTo", None)
                setattr(value, "ktest401_RelatedTo", self)

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest401_Thing__fromThing", None)
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
    def ktest401_Thing7(self):
        return self.__ktest401_Thing7

    @ktest401_Thing7.setter
    def ktest401_Thing7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest401_Thing__ktest401_Thing7", None)
        self.__ktest401_Thing7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ktest401_EClass0"):
                    opp_val = getattr(item, "ktest401_EClass0", None)
                    
                    if opp_val == self:
                        setattr(item, "ktest401_EClass0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ktest401_EClass0"):
                    opp_val = getattr(item, "ktest401_EClass0", None)
                    
                    setattr(item, "ktest401_EClass0", self)
                    

    @property
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest401_Thing__Thing", None)
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
    def ktest401_Thing15(self):
        return self.__ktest401_Thing15

    @ktest401_Thing15.setter
    def ktest401_Thing15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest401_Thing__ktest401_Thing15", None)
        self.__ktest401_Thing15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest401_Line14"):
                opp_val = getattr(old_value, "ktest401_Line14", None)
                if opp_val == self:
                    setattr(old_value, "ktest401_Line14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest401_Line14"):
                opp_val = getattr(value, "ktest401_Line14", None)
                setattr(value, "ktest401_Line14", self)

    @property
    def ktest401_Thing5(self):
        return self.__ktest401_Thing5

    @ktest401_Thing5.setter
    def ktest401_Thing5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest401_Thing__ktest401_Thing5", None)
        self.__ktest401_Thing5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ktest401_Line"):
                    opp_val = getattr(item, "ktest401_Line", None)
                    
                    if opp_val == self:
                        setattr(item, "ktest401_Line", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ktest401_Line"):
                    opp_val = getattr(item, "ktest401_Line", None)
                    
                    setattr(item, "ktest401_Line", self)
                    
