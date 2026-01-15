from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Baz:

    pass
class yyk_Boul(Baz):

    def __init__(self, hi: str):
        self.hi = hi
        
    @property
    def hi(self) -> str:
        return self.__hi

    @hi.setter
    def hi(self, hi: str):
        self.__hi = hi

class yyk_Bouz(Baz):

    def __init__(self, bil: str, yyk_Bouz: set["yyk_Zing"] = None):
        self.bil = bil
        self.yyk_Bouz = yyk_Bouz if yyk_Bouz is not None else set()
        
    @property
    def bil(self) -> str:
        return self.__bil

    @bil.setter
    def bil(self, bil: str):
        self.__bil = bil

    @property
    def yyk_Bouz(self):
        return self.__yyk_Bouz

    @yyk_Bouz.setter
    def yyk_Bouz(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Bouz__yyk_Bouz", None)
        self.__yyk_Bouz = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyk_Zing32"):
                    opp_val = getattr(item, "yyk_Zing32", None)
                    
                    if opp_val == self:
                        setattr(item, "yyk_Zing32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyk_Zing32"):
                    opp_val = getattr(item, "yyk_Zing32", None)
                    
                    setattr(item, "yyk_Zing32", self)
                    

class yyk_Bar:

    def __init__(self, id: str, yyk_Bar: "yyk_NamedElement" = None, yyk_Bar21: "yyk_Output" = None):
        self.id = id
        self.yyk_Bar = yyk_Bar
        self.yyk_Bar21 = yyk_Bar21
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyk_Bar(self):
        return self.__yyk_Bar

    @yyk_Bar.setter
    def yyk_Bar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Bar__yyk_Bar", None)
        self.__yyk_Bar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyk_NamedElement9"):
                opp_val = getattr(old_value, "yyk_NamedElement9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_NamedElement9"):
                opp_val = getattr(value, "yyk_NamedElement9", None)
                if opp_val is None:
                    setattr(value, "yyk_NamedElement9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def yyk_Bar21(self):
        return self.__yyk_Bar21

    @yyk_Bar21.setter
    def yyk_Bar21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Bar__yyk_Bar21", None)
        self.__yyk_Bar21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyk_Output22"):
                opp_val = getattr(old_value, "yyk_Output22", None)
                if opp_val == self:
                    setattr(old_value, "yyk_Output22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_Output22"):
                opp_val = getattr(value, "yyk_Output22", None)
                setattr(value, "yyk_Output22", self)

class yyk_Alias:

    def __init__(self, id: str, yyk_Alias: "yyk_NamedElement" = None):
        self.id = id
        self.yyk_Alias = yyk_Alias
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyk_Alias(self):
        return self.__yyk_Alias

    @yyk_Alias.setter
    def yyk_Alias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Alias__yyk_Alias", None)
        self.__yyk_Alias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyk_NamedElement"):
                opp_val = getattr(old_value, "yyk_NamedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_NamedElement"):
                opp_val = getattr(value, "yyk_NamedElement", None)
                if opp_val is None:
                    setattr(value, "yyk_NamedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yyk_Rel:

    def __init__(self, id: str, yyk_Rel: "yyk_NamedElement" = None, yyk_Rel24: "yyk_NamedElement" = None, yyk_Rel27: "yyk_Relation" = None):
        self.id = id
        self.yyk_Rel = yyk_Rel
        self.yyk_Rel24 = yyk_Rel24
        self.yyk_Rel27 = yyk_Rel27
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyk_Rel24(self):
        return self.__yyk_Rel24

    @yyk_Rel24.setter
    def yyk_Rel24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Rel__yyk_Rel24", None)
        self.__yyk_Rel24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyk_NamedElement25"):
                opp_val = getattr(old_value, "yyk_NamedElement25", None)
                if opp_val == self:
                    setattr(old_value, "yyk_NamedElement25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_NamedElement25"):
                opp_val = getattr(value, "yyk_NamedElement25", None)
                setattr(value, "yyk_NamedElement25", self)

    @property
    def yyk_Rel(self):
        return self.__yyk_Rel

    @yyk_Rel.setter
    def yyk_Rel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Rel__yyk_Rel", None)
        self.__yyk_Rel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyk_NamedElement11"):
                opp_val = getattr(old_value, "yyk_NamedElement11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_NamedElement11"):
                opp_val = getattr(value, "yyk_NamedElement11", None)
                if opp_val is None:
                    setattr(value, "yyk_NamedElement11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def yyk_Rel27(self):
        return self.__yyk_Rel27

    @yyk_Rel27.setter
    def yyk_Rel27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Rel__yyk_Rel27", None)
        self.__yyk_Rel27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyk_Relation28"):
                opp_val = getattr(old_value, "yyk_Relation28", None)
                if opp_val == self:
                    setattr(old_value, "yyk_Relation28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_Relation28"):
                opp_val = getattr(value, "yyk_Relation28", None)
                setattr(value, "yyk_Relation28", self)

class NamedElement:

    pass
class yyk_Zing(NamedElement):

    pass
class yyk_Base(NamedElement):

    def __init__(self, id: int, : set["yyk_Relation"] = None, yyk_Base: set["yyk_Foo"] = None, yyk_Base4: set["yyk_Output"] = None, yyk_Base6: set["yyk_Baz"] = None, 14: "yyk_Relation" = None):
        self.id = id
        self. =  if  is not None else set()
        self.yyk_Base = yyk_Base if yyk_Base is not None else set()
        self.yyk_Base4 = yyk_Base4 if yyk_Base4 is not None else set()
        self.yyk_Base6 = yyk_Base6 if yyk_Base6 is not None else set()
        self.14 = 14
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Base__", None)
        self.__ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "1"):
                    opp_val = getattr(item, "1", None)
                    
                    if opp_val == self:
                        setattr(item, "1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "1"):
                    opp_val = getattr(item, "1", None)
                    
                    setattr(item, "1", self)
                    

    @property
    def yyk_Base(self):
        return self.__yyk_Base

    @yyk_Base.setter
    def yyk_Base(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Base__yyk_Base", None)
        self.__yyk_Base = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyk_Foo"):
                    opp_val = getattr(item, "yyk_Foo", None)
                    
                    if opp_val == self:
                        setattr(item, "yyk_Foo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyk_Foo"):
                    opp_val = getattr(item, "yyk_Foo", None)
                    
                    setattr(item, "yyk_Foo", self)
                    

    @property
    def yyk_Base4(self):
        return self.__yyk_Base4

    @yyk_Base4.setter
    def yyk_Base4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Base__yyk_Base4", None)
        self.__yyk_Base4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyk_Output"):
                    opp_val = getattr(item, "yyk_Output", None)
                    
                    if opp_val == self:
                        setattr(item, "yyk_Output", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyk_Output"):
                    opp_val = getattr(item, "yyk_Output", None)
                    
                    setattr(item, "yyk_Output", self)
                    

    @property
    def yyk_Base6(self):
        return self.__yyk_Base6

    @yyk_Base6.setter
    def yyk_Base6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Base__yyk_Base6", None)
        self.__yyk_Base6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyk_Baz"):
                    opp_val = getattr(item, "yyk_Baz", None)
                    
                    if opp_val == self:
                        setattr(item, "yyk_Baz", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyk_Baz"):
                    opp_val = getattr(item, "yyk_Baz", None)
                    
                    setattr(item, "yyk_Baz", self)
                    

    @property
    def 14(self):
        return self.__14

    @14.setter
    def 14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Base__14", None)
        self.__14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "13"):
                opp_val = getattr(old_value, "13", None)
                if opp_val == self:
                    setattr(old_value, "13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "13"):
                opp_val = getattr(value, "13", None)
                setattr(value, "13", self)

class yyk_NamedElement(ABC):

    def __init__(self, name: str, yyk_NamedElement9: set["yyk_Bar"] = None, yyk_NamedElement11: set["yyk_Rel"] = None, yyk_NamedElement16: "yyk_Relation" = None, yyk_NamedElement: set["yyk_Alias"] = None, yyk_NamedElement25: "yyk_Rel" = None):
        self.name = name
        self.yyk_NamedElement9 = yyk_NamedElement9 if yyk_NamedElement9 is not None else set()
        self.yyk_NamedElement11 = yyk_NamedElement11 if yyk_NamedElement11 is not None else set()
        self.yyk_NamedElement16 = yyk_NamedElement16
        self.yyk_NamedElement = yyk_NamedElement if yyk_NamedElement is not None else set()
        self.yyk_NamedElement25 = yyk_NamedElement25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def yyk_NamedElement25(self):
        return self.__yyk_NamedElement25

    @yyk_NamedElement25.setter
    def yyk_NamedElement25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_NamedElement__yyk_NamedElement25", None)
        self.__yyk_NamedElement25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyk_Rel24"):
                opp_val = getattr(old_value, "yyk_Rel24", None)
                if opp_val == self:
                    setattr(old_value, "yyk_Rel24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_Rel24"):
                opp_val = getattr(value, "yyk_Rel24", None)
                setattr(value, "yyk_Rel24", self)

    @property
    def yyk_NamedElement9(self):
        return self.__yyk_NamedElement9

    @yyk_NamedElement9.setter
    def yyk_NamedElement9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_NamedElement__yyk_NamedElement9", None)
        self.__yyk_NamedElement9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyk_Bar"):
                    opp_val = getattr(item, "yyk_Bar", None)
                    
                    if opp_val == self:
                        setattr(item, "yyk_Bar", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyk_Bar"):
                    opp_val = getattr(item, "yyk_Bar", None)
                    
                    setattr(item, "yyk_Bar", self)
                    

    @property
    def yyk_NamedElement16(self):
        return self.__yyk_NamedElement16

    @yyk_NamedElement16.setter
    def yyk_NamedElement16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_NamedElement__yyk_NamedElement16", None)
        self.__yyk_NamedElement16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyk_Relation"):
                opp_val = getattr(old_value, "yyk_Relation", None)
                if opp_val == self:
                    setattr(old_value, "yyk_Relation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_Relation"):
                opp_val = getattr(value, "yyk_Relation", None)
                setattr(value, "yyk_Relation", self)

    @property
    def yyk_NamedElement(self):
        return self.__yyk_NamedElement

    @yyk_NamedElement.setter
    def yyk_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_NamedElement__yyk_NamedElement", None)
        self.__yyk_NamedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyk_Alias"):
                    opp_val = getattr(item, "yyk_Alias", None)
                    
                    if opp_val == self:
                        setattr(item, "yyk_Alias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyk_Alias"):
                    opp_val = getattr(item, "yyk_Alias", None)
                    
                    setattr(item, "yyk_Alias", self)
                    

    @property
    def yyk_NamedElement11(self):
        return self.__yyk_NamedElement11

    @yyk_NamedElement11.setter
    def yyk_NamedElement11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_NamedElement__yyk_NamedElement11", None)
        self.__yyk_NamedElement11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyk_Rel"):
                    opp_val = getattr(item, "yyk_Rel", None)
                    
                    if opp_val == self:
                        setattr(item, "yyk_Rel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyk_Rel"):
                    opp_val = getattr(item, "yyk_Rel", None)
                    
                    setattr(item, "yyk_Rel", self)
                    

class yyk_Baz(NamedElement):

    def __init__(self, zig: str, yyk_Baz: "yyk_Base" = None, yyk_Baz30: "yyk_Zing" = None):
        self.zig = zig
        self.yyk_Baz = yyk_Baz
        self.yyk_Baz30 = yyk_Baz30
        
    @property
    def zig(self) -> str:
        return self.__zig

    @zig.setter
    def zig(self, zig: str):
        self.__zig = zig

    @property
    def yyk_Baz30(self):
        return self.__yyk_Baz30

    @yyk_Baz30.setter
    def yyk_Baz30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Baz__yyk_Baz30", None)
        self.__yyk_Baz30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyk_Zing"):
                opp_val = getattr(old_value, "yyk_Zing", None)
                if opp_val == self:
                    setattr(old_value, "yyk_Zing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_Zing"):
                opp_val = getattr(value, "yyk_Zing", None)
                setattr(value, "yyk_Zing", self)

    @property
    def yyk_Baz(self):
        return self.__yyk_Baz

    @yyk_Baz.setter
    def yyk_Baz(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Baz__yyk_Baz", None)
        self.__yyk_Baz = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyk_Base6"):
                opp_val = getattr(old_value, "yyk_Base6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_Base6"):
                opp_val = getattr(value, "yyk_Base6", None)
                if opp_val is None:
                    setattr(value, "yyk_Base6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yyk_Output:

    def __init__(self, id: str, yyk_Output: "yyk_Base" = None, yyk_Output22: "yyk_Bar" = None):
        self.id = id
        self.yyk_Output = yyk_Output
        self.yyk_Output22 = yyk_Output22
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyk_Output22(self):
        return self.__yyk_Output22

    @yyk_Output22.setter
    def yyk_Output22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Output__yyk_Output22", None)
        self.__yyk_Output22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyk_Bar21"):
                opp_val = getattr(old_value, "yyk_Bar21", None)
                if opp_val == self:
                    setattr(old_value, "yyk_Bar21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_Bar21"):
                opp_val = getattr(value, "yyk_Bar21", None)
                setattr(value, "yyk_Bar21", self)

    @property
    def yyk_Output(self):
        return self.__yyk_Output

    @yyk_Output.setter
    def yyk_Output(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Output__yyk_Output", None)
        self.__yyk_Output = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyk_Base4"):
                opp_val = getattr(old_value, "yyk_Base4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_Base4"):
                opp_val = getattr(value, "yyk_Base4", None)
                if opp_val is None:
                    setattr(value, "yyk_Base4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yyk_Foo:

    def __init__(self, id: str, yyk_Foo: "yyk_Base" = None):
        self.id = id
        self.yyk_Foo = yyk_Foo
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyk_Foo(self):
        return self.__yyk_Foo

    @yyk_Foo.setter
    def yyk_Foo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Foo__yyk_Foo", None)
        self.__yyk_Foo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyk_Base"):
                opp_val = getattr(old_value, "yyk_Base", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_Base"):
                opp_val = getattr(value, "yyk_Base", None)
                if opp_val is None:
                    setattr(value, "yyk_Base", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yyk_Relation(NamedElement):

    def __init__(self, since: str, 1: "yyk_Base" = None, 13: "yyk_Base" = None, yyk_Relation: "yyk_NamedElement" = None, yyk_Relation19: "yyk_Relation" = None, yyk_Relation17: set["yyk_Relation"] = None, yyk_Relation28: "yyk_Rel" = None):
        self.since = since
        self.1 = 1
        self.13 = 13
        self.yyk_Relation = yyk_Relation
        self.yyk_Relation19 = yyk_Relation19
        self.yyk_Relation17 = yyk_Relation17 if yyk_Relation17 is not None else set()
        self.yyk_Relation28 = yyk_Relation28
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def yyk_Relation(self):
        return self.__yyk_Relation

    @yyk_Relation.setter
    def yyk_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Relation__yyk_Relation", None)
        self.__yyk_Relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyk_NamedElement16"):
                opp_val = getattr(old_value, "yyk_NamedElement16", None)
                if opp_val == self:
                    setattr(old_value, "yyk_NamedElement16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_NamedElement16"):
                opp_val = getattr(value, "yyk_NamedElement16", None)
                setattr(value, "yyk_NamedElement16", self)

    @property
    def yyk_Relation28(self):
        return self.__yyk_Relation28

    @yyk_Relation28.setter
    def yyk_Relation28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Relation__yyk_Relation28", None)
        self.__yyk_Relation28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyk_Rel27"):
                opp_val = getattr(old_value, "yyk_Rel27", None)
                if opp_val == self:
                    setattr(old_value, "yyk_Rel27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_Rel27"):
                opp_val = getattr(value, "yyk_Rel27", None)
                setattr(value, "yyk_Rel27", self)

    @property
    def 13(self):
        return self.__13

    @13.setter
    def 13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Relation__13", None)
        self.__13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "14"):
                opp_val = getattr(old_value, "14", None)
                if opp_val == self:
                    setattr(old_value, "14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "14"):
                opp_val = getattr(value, "14", None)
                setattr(value, "14", self)

    @property
    def yyk_Relation17(self):
        return self.__yyk_Relation17

    @yyk_Relation17.setter
    def yyk_Relation17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Relation__yyk_Relation17", None)
        self.__yyk_Relation17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyk_Relation19"):
                    opp_val = getattr(item, "yyk_Relation19", None)
                    
                    if opp_val == self:
                        setattr(item, "yyk_Relation19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyk_Relation19"):
                    opp_val = getattr(item, "yyk_Relation19", None)
                    
                    setattr(item, "yyk_Relation19", self)
                    

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Relation__1", None)
        self.__1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                if opp_val is None:
                    setattr(value, "", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def yyk_Relation19(self):
        return self.__yyk_Relation19

    @yyk_Relation19.setter
    def yyk_Relation19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Relation__yyk_Relation19", None)
        self.__yyk_Relation19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyk_Relation17"):
                opp_val = getattr(old_value, "yyk_Relation17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_Relation17"):
                opp_val = getattr(value, "yyk_Relation17", None)
                if opp_val is None:
                    setattr(value, "yyk_Relation17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
