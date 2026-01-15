from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class yye_Alias:

    def __init__(self, id: str, yye_Alias: "yye_NamedElement" = None):
        self.id = id
        self.yye_Alias = yye_Alias
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yye_Alias(self):
        return self.__yye_Alias

    @yye_Alias.setter
    def yye_Alias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yye_Alias__yye_Alias", None)
        self.__yye_Alias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yye_NamedElement"):
                opp_val = getattr(old_value, "yye_NamedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yye_NamedElement"):
                opp_val = getattr(value, "yye_NamedElement", None)
                if opp_val is None:
                    setattr(value, "yye_NamedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yye_Foo:

    def __init__(self, id: str, yye_Foo: "yye_Base" = None):
        self.id = id
        self.yye_Foo = yye_Foo
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yye_Foo(self):
        return self.__yye_Foo

    @yye_Foo.setter
    def yye_Foo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yye_Foo__yye_Foo", None)
        self.__yye_Foo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yye_Base"):
                opp_val = getattr(old_value, "yye_Base", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yye_Base"):
                opp_val = getattr(value, "yye_Base", None)
                if opp_val is None:
                    setattr(value, "yye_Base", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yye_NamedElement(ABC):

    def __init__(self, name: str, yye_NamedElement: set["yye_Alias"] = None):
        self.name = name
        self.yye_NamedElement = yye_NamedElement if yye_NamedElement is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def yye_NamedElement(self):
        return self.__yye_NamedElement

    @yye_NamedElement.setter
    def yye_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yye_NamedElement__yye_NamedElement", None)
        self.__yye_NamedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yye_Alias"):
                    opp_val = getattr(item, "yye_Alias", None)
                    
                    if opp_val == self:
                        setattr(item, "yye_Alias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yye_Alias"):
                    opp_val = getattr(item, "yye_Alias", None)
                    
                    setattr(item, "yye_Alias", self)
                    

class NamedElement:

    pass
class yye_Base(NamedElement):

    def __init__(self, id: int, fromThing: set["yye_Relation"] = None, yye_Base: set["yye_Foo"] = None, Base: "yye_Relation" = None, yye_Base5: "yye_Relation" = None):
        self.id = id
        self.fromThing = fromThing if fromThing is not None else set()
        self.yye_Base = yye_Base if yye_Base is not None else set()
        self.Base = Base
        self.yye_Base5 = yye_Base5
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Base(self):
        return self.__Base

    @Base.setter
    def Base(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yye_Base__Base", None)
        self.__Base = value
        
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
    def yye_Base(self):
        return self.__yye_Base

    @yye_Base.setter
    def yye_Base(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yye_Base__yye_Base", None)
        self.__yye_Base = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yye_Foo"):
                    opp_val = getattr(item, "yye_Foo", None)
                    
                    if opp_val == self:
                        setattr(item, "yye_Foo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yye_Foo"):
                    opp_val = getattr(item, "yye_Foo", None)
                    
                    setattr(item, "yye_Foo", self)
                    

    @property
    def yye_Base5(self):
        return self.__yye_Base5

    @yye_Base5.setter
    def yye_Base5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yye_Base__yye_Base5", None)
        self.__yye_Base5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yye_Relation"):
                opp_val = getattr(old_value, "yye_Relation", None)
                if opp_val == self:
                    setattr(old_value, "yye_Relation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yye_Relation"):
                opp_val = getattr(value, "yye_Relation", None)
                setattr(value, "yye_Relation", self)

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yye_Base__fromThing", None)
        self.__fromThing = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relation"):
                    opp_val = getattr(item, "Relation", None)
                    
                    if opp_val == self:
                        setattr(item, "Relation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relation"):
                    opp_val = getattr(item, "Relation", None)
                    
                    setattr(item, "Relation", self)
                    

class yye_Relation(NamedElement):

    def __init__(self, since: str, Relation: "yye_Base" = None, yye_Relation8: "yye_Relation" = None, yye_Relation6: set["yye_Relation"] = None, relations: "yye_Base" = None, yye_Relation: "yye_Base" = None):
        self.since = since
        self.Relation = Relation
        self.yye_Relation8 = yye_Relation8
        self.yye_Relation6 = yye_Relation6 if yye_Relation6 is not None else set()
        self.relations = relations
        self.yye_Relation = yye_Relation
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def yye_Relation(self):
        return self.__yye_Relation

    @yye_Relation.setter
    def yye_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yye_Relation__yye_Relation", None)
        self.__yye_Relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yye_Base5"):
                opp_val = getattr(old_value, "yye_Base5", None)
                if opp_val == self:
                    setattr(old_value, "yye_Base5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yye_Base5"):
                opp_val = getattr(value, "yye_Base5", None)
                setattr(value, "yye_Base5", self)

    @property
    def Relation(self):
        return self.__Relation

    @Relation.setter
    def Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yye_Relation__Relation", None)
        self.__Relation = value
        
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
        old_value = getattr(self, f"_yye_Relation__relations", None)
        self.__relations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Base"):
                opp_val = getattr(old_value, "Base", None)
                if opp_val == self:
                    setattr(old_value, "Base", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Base"):
                opp_val = getattr(value, "Base", None)
                setattr(value, "Base", self)

    @property
    def yye_Relation6(self):
        return self.__yye_Relation6

    @yye_Relation6.setter
    def yye_Relation6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yye_Relation__yye_Relation6", None)
        self.__yye_Relation6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yye_Relation8"):
                    opp_val = getattr(item, "yye_Relation8", None)
                    
                    if opp_val == self:
                        setattr(item, "yye_Relation8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yye_Relation8"):
                    opp_val = getattr(item, "yye_Relation8", None)
                    
                    setattr(item, "yye_Relation8", self)
                    

    @property
    def yye_Relation8(self):
        return self.__yye_Relation8

    @yye_Relation8.setter
    def yye_Relation8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yye_Relation__yye_Relation8", None)
        self.__yye_Relation8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yye_Relation6"):
                opp_val = getattr(old_value, "yye_Relation6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yye_Relation6"):
                opp_val = getattr(value, "yye_Relation6", None)
                if opp_val is None:
                    setattr(value, "yye_Relation6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
