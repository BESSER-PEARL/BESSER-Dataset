from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Baz:

    pass
class yyg_Boul(Baz):

    def __init__(self, hi: str):
        self.hi = hi
        
    @property
    def hi(self) -> str:
        return self.__hi

    @hi.setter
    def hi(self, hi: str):
        self.__hi = hi

class yyg_Bouz(Baz):

    def __init__(self, bil: str, yyg_Bouz: set["yyg_Zing"] = None):
        self.bil = bil
        self.yyg_Bouz = yyg_Bouz if yyg_Bouz is not None else set()
        
    @property
    def bil(self) -> str:
        return self.__bil

    @bil.setter
    def bil(self, bil: str):
        self.__bil = bil

    @property
    def yyg_Bouz(self):
        return self.__yyg_Bouz

    @yyg_Bouz.setter
    def yyg_Bouz(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Bouz__yyg_Bouz", None)
        self.__yyg_Bouz = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyg_Zing29"):
                    opp_val = getattr(item, "yyg_Zing29", None)
                    
                    if opp_val == self:
                        setattr(item, "yyg_Zing29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyg_Zing29"):
                    opp_val = getattr(item, "yyg_Zing29", None)
                    
                    setattr(item, "yyg_Zing29", self)
                    

class yyg_Bar:

    def __init__(self, id: str, yyg_Bar: "yyg_NamedElement" = None, yyg_Bar18: "yyg_Output" = None):
        self.id = id
        self.yyg_Bar = yyg_Bar
        self.yyg_Bar18 = yyg_Bar18
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyg_Bar18(self):
        return self.__yyg_Bar18

    @yyg_Bar18.setter
    def yyg_Bar18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Bar__yyg_Bar18", None)
        self.__yyg_Bar18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyg_Output19"):
                opp_val = getattr(old_value, "yyg_Output19", None)
                if opp_val == self:
                    setattr(old_value, "yyg_Output19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyg_Output19"):
                opp_val = getattr(value, "yyg_Output19", None)
                setattr(value, "yyg_Output19", self)

    @property
    def yyg_Bar(self):
        return self.__yyg_Bar

    @yyg_Bar.setter
    def yyg_Bar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Bar__yyg_Bar", None)
        self.__yyg_Bar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyg_NamedElement8"):
                opp_val = getattr(old_value, "yyg_NamedElement8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyg_NamedElement8"):
                opp_val = getattr(value, "yyg_NamedElement8", None)
                if opp_val is None:
                    setattr(value, "yyg_NamedElement8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yyg_Alias:

    def __init__(self, id: str, yyg_Alias: "yyg_NamedElement" = None):
        self.id = id
        self.yyg_Alias = yyg_Alias
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyg_Alias(self):
        return self.__yyg_Alias

    @yyg_Alias.setter
    def yyg_Alias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Alias__yyg_Alias", None)
        self.__yyg_Alias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyg_NamedElement"):
                opp_val = getattr(old_value, "yyg_NamedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyg_NamedElement"):
                opp_val = getattr(value, "yyg_NamedElement", None)
                if opp_val is None:
                    setattr(value, "yyg_NamedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yyg_NamedElement(ABC):

    def __init__(self, name: str, yyg_NamedElement8: set["yyg_Bar"] = None, yyg_NamedElement10: set["yyg_Rel"] = None, yyg_NamedElement: set["yyg_Alias"] = None, yyg_NamedElement13: "yyg_Boz" = None, yyg_NamedElement22: "yyg_Rel" = None):
        self.name = name
        self.yyg_NamedElement8 = yyg_NamedElement8 if yyg_NamedElement8 is not None else set()
        self.yyg_NamedElement10 = yyg_NamedElement10 if yyg_NamedElement10 is not None else set()
        self.yyg_NamedElement = yyg_NamedElement if yyg_NamedElement is not None else set()
        self.yyg_NamedElement13 = yyg_NamedElement13
        self.yyg_NamedElement22 = yyg_NamedElement22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def yyg_NamedElement8(self):
        return self.__yyg_NamedElement8

    @yyg_NamedElement8.setter
    def yyg_NamedElement8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_NamedElement__yyg_NamedElement8", None)
        self.__yyg_NamedElement8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyg_Bar"):
                    opp_val = getattr(item, "yyg_Bar", None)
                    
                    if opp_val == self:
                        setattr(item, "yyg_Bar", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyg_Bar"):
                    opp_val = getattr(item, "yyg_Bar", None)
                    
                    setattr(item, "yyg_Bar", self)
                    

    @property
    def yyg_NamedElement22(self):
        return self.__yyg_NamedElement22

    @yyg_NamedElement22.setter
    def yyg_NamedElement22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_NamedElement__yyg_NamedElement22", None)
        self.__yyg_NamedElement22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyg_Rel21"):
                opp_val = getattr(old_value, "yyg_Rel21", None)
                if opp_val == self:
                    setattr(old_value, "yyg_Rel21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyg_Rel21"):
                opp_val = getattr(value, "yyg_Rel21", None)
                setattr(value, "yyg_Rel21", self)

    @property
    def yyg_NamedElement(self):
        return self.__yyg_NamedElement

    @yyg_NamedElement.setter
    def yyg_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_NamedElement__yyg_NamedElement", None)
        self.__yyg_NamedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyg_Alias"):
                    opp_val = getattr(item, "yyg_Alias", None)
                    
                    if opp_val == self:
                        setattr(item, "yyg_Alias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyg_Alias"):
                    opp_val = getattr(item, "yyg_Alias", None)
                    
                    setattr(item, "yyg_Alias", self)
                    

    @property
    def yyg_NamedElement13(self):
        return self.__yyg_NamedElement13

    @yyg_NamedElement13.setter
    def yyg_NamedElement13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_NamedElement__yyg_NamedElement13", None)
        self.__yyg_NamedElement13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyg_Boz"):
                opp_val = getattr(old_value, "yyg_Boz", None)
                if opp_val == self:
                    setattr(old_value, "yyg_Boz", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyg_Boz"):
                opp_val = getattr(value, "yyg_Boz", None)
                setattr(value, "yyg_Boz", self)

    @property
    def yyg_NamedElement10(self):
        return self.__yyg_NamedElement10

    @yyg_NamedElement10.setter
    def yyg_NamedElement10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_NamedElement__yyg_NamedElement10", None)
        self.__yyg_NamedElement10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyg_Rel"):
                    opp_val = getattr(item, "yyg_Rel", None)
                    
                    if opp_val == self:
                        setattr(item, "yyg_Rel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyg_Rel"):
                    opp_val = getattr(item, "yyg_Rel", None)
                    
                    setattr(item, "yyg_Rel", self)
                    

class yyg_Rel:

    def __init__(self, id: str, yyg_Rel: "yyg_NamedElement" = None, yyg_Rel21: "yyg_NamedElement" = None, yyg_Rel24: "yyg_Boz" = None):
        self.id = id
        self.yyg_Rel = yyg_Rel
        self.yyg_Rel21 = yyg_Rel21
        self.yyg_Rel24 = yyg_Rel24
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyg_Rel24(self):
        return self.__yyg_Rel24

    @yyg_Rel24.setter
    def yyg_Rel24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Rel__yyg_Rel24", None)
        self.__yyg_Rel24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyg_Boz25"):
                opp_val = getattr(old_value, "yyg_Boz25", None)
                if opp_val == self:
                    setattr(old_value, "yyg_Boz25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyg_Boz25"):
                opp_val = getattr(value, "yyg_Boz25", None)
                setattr(value, "yyg_Boz25", self)

    @property
    def yyg_Rel21(self):
        return self.__yyg_Rel21

    @yyg_Rel21.setter
    def yyg_Rel21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Rel__yyg_Rel21", None)
        self.__yyg_Rel21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyg_NamedElement22"):
                opp_val = getattr(old_value, "yyg_NamedElement22", None)
                if opp_val == self:
                    setattr(old_value, "yyg_NamedElement22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyg_NamedElement22"):
                opp_val = getattr(value, "yyg_NamedElement22", None)
                setattr(value, "yyg_NamedElement22", self)

    @property
    def yyg_Rel(self):
        return self.__yyg_Rel

    @yyg_Rel.setter
    def yyg_Rel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Rel__yyg_Rel", None)
        self.__yyg_Rel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyg_NamedElement10"):
                opp_val = getattr(old_value, "yyg_NamedElement10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyg_NamedElement10"):
                opp_val = getattr(value, "yyg_NamedElement10", None)
                if opp_val is None:
                    setattr(value, "yyg_NamedElement10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class yyg_Zing(NamedElement):

    pass
class yyg_Baz(NamedElement):

    def __init__(self, zig: str, yyg_Baz: "yyg_Base" = None, yyg_Baz27: "yyg_Zing" = None):
        self.zig = zig
        self.yyg_Baz = yyg_Baz
        self.yyg_Baz27 = yyg_Baz27
        
    @property
    def zig(self) -> str:
        return self.__zig

    @zig.setter
    def zig(self, zig: str):
        self.__zig = zig

    @property
    def yyg_Baz(self):
        return self.__yyg_Baz

    @yyg_Baz.setter
    def yyg_Baz(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Baz__yyg_Baz", None)
        self.__yyg_Baz = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyg_Base5"):
                opp_val = getattr(old_value, "yyg_Base5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyg_Base5"):
                opp_val = getattr(value, "yyg_Base5", None)
                if opp_val is None:
                    setattr(value, "yyg_Base5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def yyg_Baz27(self):
        return self.__yyg_Baz27

    @yyg_Baz27.setter
    def yyg_Baz27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Baz__yyg_Baz27", None)
        self.__yyg_Baz27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyg_Zing"):
                opp_val = getattr(old_value, "yyg_Zing", None)
                if opp_val == self:
                    setattr(old_value, "yyg_Zing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyg_Zing"):
                opp_val = getattr(value, "yyg_Zing", None)
                setattr(value, "yyg_Zing", self)

class yyg_Base(NamedElement):

    def __init__(self, id: int, fromThing: set["yyg_Boz"] = None, yyg_Base: set["yyg_Foo"] = None, yyg_Base3: set["yyg_Output"] = None, yyg_Base5: set["yyg_Baz"] = None, Base: "yyg_Boz" = None):
        self.id = id
        self.fromThing = fromThing if fromThing is not None else set()
        self.yyg_Base = yyg_Base if yyg_Base is not None else set()
        self.yyg_Base3 = yyg_Base3 if yyg_Base3 is not None else set()
        self.yyg_Base5 = yyg_Base5 if yyg_Base5 is not None else set()
        self.Base = Base
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def yyg_Base5(self):
        return self.__yyg_Base5

    @yyg_Base5.setter
    def yyg_Base5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Base__yyg_Base5", None)
        self.__yyg_Base5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyg_Baz"):
                    opp_val = getattr(item, "yyg_Baz", None)
                    
                    if opp_val == self:
                        setattr(item, "yyg_Baz", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyg_Baz"):
                    opp_val = getattr(item, "yyg_Baz", None)
                    
                    setattr(item, "yyg_Baz", self)
                    

    @property
    def yyg_Base3(self):
        return self.__yyg_Base3

    @yyg_Base3.setter
    def yyg_Base3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Base__yyg_Base3", None)
        self.__yyg_Base3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyg_Output"):
                    opp_val = getattr(item, "yyg_Output", None)
                    
                    if opp_val == self:
                        setattr(item, "yyg_Output", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyg_Output"):
                    opp_val = getattr(item, "yyg_Output", None)
                    
                    setattr(item, "yyg_Output", self)
                    

    @property
    def yyg_Base(self):
        return self.__yyg_Base

    @yyg_Base.setter
    def yyg_Base(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Base__yyg_Base", None)
        self.__yyg_Base = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyg_Foo"):
                    opp_val = getattr(item, "yyg_Foo", None)
                    
                    if opp_val == self:
                        setattr(item, "yyg_Foo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyg_Foo"):
                    opp_val = getattr(item, "yyg_Foo", None)
                    
                    setattr(item, "yyg_Foo", self)
                    

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Base__fromThing", None)
        self.__fromThing = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Boz"):
                    opp_val = getattr(item, "Boz", None)
                    
                    if opp_val == self:
                        setattr(item, "Boz", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Boz"):
                    opp_val = getattr(item, "Boz", None)
                    
                    setattr(item, "Boz", self)
                    

    @property
    def Base(self):
        return self.__Base

    @Base.setter
    def Base(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Base__Base", None)
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

class yyg_Output:

    def __init__(self, id: str, yyg_Output: "yyg_Base" = None, yyg_Output19: "yyg_Bar" = None):
        self.id = id
        self.yyg_Output = yyg_Output
        self.yyg_Output19 = yyg_Output19
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyg_Output(self):
        return self.__yyg_Output

    @yyg_Output.setter
    def yyg_Output(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Output__yyg_Output", None)
        self.__yyg_Output = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyg_Base3"):
                opp_val = getattr(old_value, "yyg_Base3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyg_Base3"):
                opp_val = getattr(value, "yyg_Base3", None)
                if opp_val is None:
                    setattr(value, "yyg_Base3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def yyg_Output19(self):
        return self.__yyg_Output19

    @yyg_Output19.setter
    def yyg_Output19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Output__yyg_Output19", None)
        self.__yyg_Output19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyg_Bar18"):
                opp_val = getattr(old_value, "yyg_Bar18", None)
                if opp_val == self:
                    setattr(old_value, "yyg_Bar18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyg_Bar18"):
                opp_val = getattr(value, "yyg_Bar18", None)
                setattr(value, "yyg_Bar18", self)

class yyg_Foo:

    def __init__(self, id: str, yyg_Foo: "yyg_Base" = None):
        self.id = id
        self.yyg_Foo = yyg_Foo
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyg_Foo(self):
        return self.__yyg_Foo

    @yyg_Foo.setter
    def yyg_Foo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Foo__yyg_Foo", None)
        self.__yyg_Foo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyg_Base"):
                opp_val = getattr(old_value, "yyg_Base", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyg_Base"):
                opp_val = getattr(value, "yyg_Base", None)
                if opp_val is None:
                    setattr(value, "yyg_Base", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yyg_Boz(NamedElement):

    def __init__(self, since: str, Boz: "yyg_Base" = None, relations: "yyg_Base" = None, yyg_Boz: "yyg_NamedElement" = None, yyg_Boz16: "yyg_Boz" = None, yyg_Boz14: set["yyg_Boz"] = None, yyg_Boz25: "yyg_Rel" = None):
        self.since = since
        self.Boz = Boz
        self.relations = relations
        self.yyg_Boz = yyg_Boz
        self.yyg_Boz16 = yyg_Boz16
        self.yyg_Boz14 = yyg_Boz14 if yyg_Boz14 is not None else set()
        self.yyg_Boz25 = yyg_Boz25
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def yyg_Boz(self):
        return self.__yyg_Boz

    @yyg_Boz.setter
    def yyg_Boz(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Boz__yyg_Boz", None)
        self.__yyg_Boz = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyg_NamedElement13"):
                opp_val = getattr(old_value, "yyg_NamedElement13", None)
                if opp_val == self:
                    setattr(old_value, "yyg_NamedElement13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyg_NamedElement13"):
                opp_val = getattr(value, "yyg_NamedElement13", None)
                setattr(value, "yyg_NamedElement13", self)

    @property
    def relations(self):
        return self.__relations

    @relations.setter
    def relations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Boz__relations", None)
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
    def Boz(self):
        return self.__Boz

    @Boz.setter
    def Boz(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Boz__Boz", None)
        self.__Boz = value
        
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
    def yyg_Boz25(self):
        return self.__yyg_Boz25

    @yyg_Boz25.setter
    def yyg_Boz25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Boz__yyg_Boz25", None)
        self.__yyg_Boz25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyg_Rel24"):
                opp_val = getattr(old_value, "yyg_Rel24", None)
                if opp_val == self:
                    setattr(old_value, "yyg_Rel24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyg_Rel24"):
                opp_val = getattr(value, "yyg_Rel24", None)
                setattr(value, "yyg_Rel24", self)

    @property
    def yyg_Boz14(self):
        return self.__yyg_Boz14

    @yyg_Boz14.setter
    def yyg_Boz14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Boz__yyg_Boz14", None)
        self.__yyg_Boz14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyg_Boz16"):
                    opp_val = getattr(item, "yyg_Boz16", None)
                    
                    if opp_val == self:
                        setattr(item, "yyg_Boz16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyg_Boz16"):
                    opp_val = getattr(item, "yyg_Boz16", None)
                    
                    setattr(item, "yyg_Boz16", self)
                    

    @property
    def yyg_Boz16(self):
        return self.__yyg_Boz16

    @yyg_Boz16.setter
    def yyg_Boz16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyg_Boz__yyg_Boz16", None)
        self.__yyg_Boz16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyg_Boz14"):
                opp_val = getattr(old_value, "yyg_Boz14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyg_Boz14"):
                opp_val = getattr(value, "yyg_Boz14", None)
                if opp_val is None:
                    setattr(value, "yyg_Boz14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
