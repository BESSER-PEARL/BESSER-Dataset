from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class yyf_Bar:

    def __init__(self, id: str, yyf_Bar: "yyf_NamedElement" = None, yyf_Bar14: "yyf_Output" = None):
        self.id = id
        self.yyf_Bar = yyf_Bar
        self.yyf_Bar14 = yyf_Bar14
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyf_Bar14(self):
        return self.__yyf_Bar14

    @yyf_Bar14.setter
    def yyf_Bar14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyf_Bar__yyf_Bar14", None)
        self.__yyf_Bar14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyf_Output15"):
                opp_val = getattr(old_value, "yyf_Output15", None)
                if opp_val == self:
                    setattr(old_value, "yyf_Output15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyf_Output15"):
                opp_val = getattr(value, "yyf_Output15", None)
                setattr(value, "yyf_Output15", self)

    @property
    def yyf_Bar(self):
        return self.__yyf_Bar

    @yyf_Bar.setter
    def yyf_Bar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyf_Bar__yyf_Bar", None)
        self.__yyf_Bar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyf_NamedElement6"):
                opp_val = getattr(old_value, "yyf_NamedElement6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyf_NamedElement6"):
                opp_val = getattr(value, "yyf_NamedElement6", None)
                if opp_val is None:
                    setattr(value, "yyf_NamedElement6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yyf_Alias:

    def __init__(self, id: str, yyf_Alias: "yyf_NamedElement" = None):
        self.id = id
        self.yyf_Alias = yyf_Alias
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyf_Alias(self):
        return self.__yyf_Alias

    @yyf_Alias.setter
    def yyf_Alias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyf_Alias__yyf_Alias", None)
        self.__yyf_Alias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyf_NamedElement"):
                opp_val = getattr(old_value, "yyf_NamedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyf_NamedElement"):
                opp_val = getattr(value, "yyf_NamedElement", None)
                if opp_val is None:
                    setattr(value, "yyf_NamedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class yyf_Base(NamedElement):

    def __init__(self, id: int, fromThing: set["yyf_Relation"] = None, yyf_Base: set["yyf_Foo"] = None, yyf_Base3: set["yyf_Output"] = None, Base: "yyf_Relation" = None, yyf_Base9: "yyf_Relation" = None):
        self.id = id
        self.fromThing = fromThing if fromThing is not None else set()
        self.yyf_Base = yyf_Base if yyf_Base is not None else set()
        self.yyf_Base3 = yyf_Base3 if yyf_Base3 is not None else set()
        self.Base = Base
        self.yyf_Base9 = yyf_Base9
        
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
        old_value = getattr(self, f"_yyf_Base__fromThing", None)
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
                    

    @property
    def yyf_Base3(self):
        return self.__yyf_Base3

    @yyf_Base3.setter
    def yyf_Base3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyf_Base__yyf_Base3", None)
        self.__yyf_Base3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyf_Output"):
                    opp_val = getattr(item, "yyf_Output", None)
                    
                    if opp_val == self:
                        setattr(item, "yyf_Output", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyf_Output"):
                    opp_val = getattr(item, "yyf_Output", None)
                    
                    setattr(item, "yyf_Output", self)
                    

    @property
    def yyf_Base9(self):
        return self.__yyf_Base9

    @yyf_Base9.setter
    def yyf_Base9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyf_Base__yyf_Base9", None)
        self.__yyf_Base9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyf_Relation"):
                opp_val = getattr(old_value, "yyf_Relation", None)
                if opp_val == self:
                    setattr(old_value, "yyf_Relation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyf_Relation"):
                opp_val = getattr(value, "yyf_Relation", None)
                setattr(value, "yyf_Relation", self)

    @property
    def yyf_Base(self):
        return self.__yyf_Base

    @yyf_Base.setter
    def yyf_Base(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyf_Base__yyf_Base", None)
        self.__yyf_Base = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyf_Foo"):
                    opp_val = getattr(item, "yyf_Foo", None)
                    
                    if opp_val == self:
                        setattr(item, "yyf_Foo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyf_Foo"):
                    opp_val = getattr(item, "yyf_Foo", None)
                    
                    setattr(item, "yyf_Foo", self)
                    

    @property
    def Base(self):
        return self.__Base

    @Base.setter
    def Base(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyf_Base__Base", None)
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

class yyf_NamedElement(ABC):

    def __init__(self, name: str, yyf_NamedElement: set["yyf_Alias"] = None, yyf_NamedElement6: set["yyf_Bar"] = None):
        self.name = name
        self.yyf_NamedElement = yyf_NamedElement if yyf_NamedElement is not None else set()
        self.yyf_NamedElement6 = yyf_NamedElement6 if yyf_NamedElement6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def yyf_NamedElement(self):
        return self.__yyf_NamedElement

    @yyf_NamedElement.setter
    def yyf_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyf_NamedElement__yyf_NamedElement", None)
        self.__yyf_NamedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyf_Alias"):
                    opp_val = getattr(item, "yyf_Alias", None)
                    
                    if opp_val == self:
                        setattr(item, "yyf_Alias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyf_Alias"):
                    opp_val = getattr(item, "yyf_Alias", None)
                    
                    setattr(item, "yyf_Alias", self)
                    

    @property
    def yyf_NamedElement6(self):
        return self.__yyf_NamedElement6

    @yyf_NamedElement6.setter
    def yyf_NamedElement6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyf_NamedElement__yyf_NamedElement6", None)
        self.__yyf_NamedElement6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyf_Bar"):
                    opp_val = getattr(item, "yyf_Bar", None)
                    
                    if opp_val == self:
                        setattr(item, "yyf_Bar", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyf_Bar"):
                    opp_val = getattr(item, "yyf_Bar", None)
                    
                    setattr(item, "yyf_Bar", self)
                    

class yyf_Output:

    def __init__(self, id: str, yyf_Output: "yyf_Base" = None, yyf_Output15: "yyf_Bar" = None):
        self.id = id
        self.yyf_Output = yyf_Output
        self.yyf_Output15 = yyf_Output15
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyf_Output(self):
        return self.__yyf_Output

    @yyf_Output.setter
    def yyf_Output(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyf_Output__yyf_Output", None)
        self.__yyf_Output = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyf_Base3"):
                opp_val = getattr(old_value, "yyf_Base3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyf_Base3"):
                opp_val = getattr(value, "yyf_Base3", None)
                if opp_val is None:
                    setattr(value, "yyf_Base3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def yyf_Output15(self):
        return self.__yyf_Output15

    @yyf_Output15.setter
    def yyf_Output15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyf_Output__yyf_Output15", None)
        self.__yyf_Output15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyf_Bar14"):
                opp_val = getattr(old_value, "yyf_Bar14", None)
                if opp_val == self:
                    setattr(old_value, "yyf_Bar14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyf_Bar14"):
                opp_val = getattr(value, "yyf_Bar14", None)
                setattr(value, "yyf_Bar14", self)

class yyf_Foo:

    def __init__(self, id: str, yyf_Foo: "yyf_Base" = None):
        self.id = id
        self.yyf_Foo = yyf_Foo
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyf_Foo(self):
        return self.__yyf_Foo

    @yyf_Foo.setter
    def yyf_Foo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyf_Foo__yyf_Foo", None)
        self.__yyf_Foo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyf_Base"):
                opp_val = getattr(old_value, "yyf_Base", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyf_Base"):
                opp_val = getattr(value, "yyf_Base", None)
                if opp_val is None:
                    setattr(value, "yyf_Base", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yyf_Relation(NamedElement):

    def __init__(self, since: str, Relation: "yyf_Base" = None, relations: "yyf_Base" = None, yyf_Relation: "yyf_Base" = None, yyf_Relation12: "yyf_Relation" = None, yyf_Relation10: set["yyf_Relation"] = None):
        self.since = since
        self.Relation = Relation
        self.relations = relations
        self.yyf_Relation = yyf_Relation
        self.yyf_Relation12 = yyf_Relation12
        self.yyf_Relation10 = yyf_Relation10 if yyf_Relation10 is not None else set()
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def yyf_Relation12(self):
        return self.__yyf_Relation12

    @yyf_Relation12.setter
    def yyf_Relation12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyf_Relation__yyf_Relation12", None)
        self.__yyf_Relation12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyf_Relation10"):
                opp_val = getattr(old_value, "yyf_Relation10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyf_Relation10"):
                opp_val = getattr(value, "yyf_Relation10", None)
                if opp_val is None:
                    setattr(value, "yyf_Relation10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relations(self):
        return self.__relations

    @relations.setter
    def relations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyf_Relation__relations", None)
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
    def Relation(self):
        return self.__Relation

    @Relation.setter
    def Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyf_Relation__Relation", None)
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
    def yyf_Relation(self):
        return self.__yyf_Relation

    @yyf_Relation.setter
    def yyf_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyf_Relation__yyf_Relation", None)
        self.__yyf_Relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyf_Base9"):
                opp_val = getattr(old_value, "yyf_Base9", None)
                if opp_val == self:
                    setattr(old_value, "yyf_Base9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyf_Base9"):
                opp_val = getattr(value, "yyf_Base9", None)
                setattr(value, "yyf_Base9", self)

    @property
    def yyf_Relation10(self):
        return self.__yyf_Relation10

    @yyf_Relation10.setter
    def yyf_Relation10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyf_Relation__yyf_Relation10", None)
        self.__yyf_Relation10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyf_Relation12"):
                    opp_val = getattr(item, "yyf_Relation12", None)
                    
                    if opp_val == self:
                        setattr(item, "yyf_Relation12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyf_Relation12"):
                    opp_val = getattr(item, "yyf_Relation12", None)
                    
                    setattr(item, "yyf_Relation12", self)
                    
