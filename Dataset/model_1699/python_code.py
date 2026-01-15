from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Baz:

    pass
class yyh_Boul(Baz):

    def __init__(self, hi: str):
        self.hi = hi
        
    @property
    def hi(self) -> str:
        return self.__hi

    @hi.setter
    def hi(self, hi: str):
        self.__hi = hi

class yyh_Bouz(Baz):

    def __init__(self, bil: str, yyh_Bouz: set["yyh_Zing"] = None):
        self.bil = bil
        self.yyh_Bouz = yyh_Bouz if yyh_Bouz is not None else set()
        
    @property
    def bil(self) -> str:
        return self.__bil

    @bil.setter
    def bil(self, bil: str):
        self.__bil = bil

    @property
    def yyh_Bouz(self):
        return self.__yyh_Bouz

    @yyh_Bouz.setter
    def yyh_Bouz(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Bouz__yyh_Bouz", None)
        self.__yyh_Bouz = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyh_Zing29"):
                    opp_val = getattr(item, "yyh_Zing29", None)
                    
                    if opp_val == self:
                        setattr(item, "yyh_Zing29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyh_Zing29"):
                    opp_val = getattr(item, "yyh_Zing29", None)
                    
                    setattr(item, "yyh_Zing29", self)
                    

class yyh_Rel:

    def __init__(self, id: str, yyh_Rel: "yyh_NamedElement" = None, yyh_Rel24: "yyh_Boz" = None, yyh_Rel21: "yyh_NamedElement" = None):
        self.id = id
        self.yyh_Rel = yyh_Rel
        self.yyh_Rel24 = yyh_Rel24
        self.yyh_Rel21 = yyh_Rel21
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyh_Rel24(self):
        return self.__yyh_Rel24

    @yyh_Rel24.setter
    def yyh_Rel24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Rel__yyh_Rel24", None)
        self.__yyh_Rel24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyh_Boz25"):
                opp_val = getattr(old_value, "yyh_Boz25", None)
                if opp_val == self:
                    setattr(old_value, "yyh_Boz25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyh_Boz25"):
                opp_val = getattr(value, "yyh_Boz25", None)
                setattr(value, "yyh_Boz25", self)

    @property
    def yyh_Rel(self):
        return self.__yyh_Rel

    @yyh_Rel.setter
    def yyh_Rel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Rel__yyh_Rel", None)
        self.__yyh_Rel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyh_NamedElement10"):
                opp_val = getattr(old_value, "yyh_NamedElement10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyh_NamedElement10"):
                opp_val = getattr(value, "yyh_NamedElement10", None)
                if opp_val is None:
                    setattr(value, "yyh_NamedElement10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def yyh_Rel21(self):
        return self.__yyh_Rel21

    @yyh_Rel21.setter
    def yyh_Rel21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Rel__yyh_Rel21", None)
        self.__yyh_Rel21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyh_NamedElement22"):
                opp_val = getattr(old_value, "yyh_NamedElement22", None)
                if opp_val == self:
                    setattr(old_value, "yyh_NamedElement22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyh_NamedElement22"):
                opp_val = getattr(value, "yyh_NamedElement22", None)
                setattr(value, "yyh_NamedElement22", self)

class yyh_Output:

    def __init__(self, id: str, yyh_Output: "yyh_Base" = None, yyh_Output19: "yyh_Bar" = None):
        self.id = id
        self.yyh_Output = yyh_Output
        self.yyh_Output19 = yyh_Output19
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyh_Output(self):
        return self.__yyh_Output

    @yyh_Output.setter
    def yyh_Output(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Output__yyh_Output", None)
        self.__yyh_Output = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyh_Base3"):
                opp_val = getattr(old_value, "yyh_Base3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyh_Base3"):
                opp_val = getattr(value, "yyh_Base3", None)
                if opp_val is None:
                    setattr(value, "yyh_Base3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def yyh_Output19(self):
        return self.__yyh_Output19

    @yyh_Output19.setter
    def yyh_Output19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Output__yyh_Output19", None)
        self.__yyh_Output19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyh_Bar18"):
                opp_val = getattr(old_value, "yyh_Bar18", None)
                if opp_val == self:
                    setattr(old_value, "yyh_Bar18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyh_Bar18"):
                opp_val = getattr(value, "yyh_Bar18", None)
                setattr(value, "yyh_Bar18", self)

class yyh_Foo:

    def __init__(self, id: str, yyh_Foo: "yyh_Base" = None):
        self.id = id
        self.yyh_Foo = yyh_Foo
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyh_Foo(self):
        return self.__yyh_Foo

    @yyh_Foo.setter
    def yyh_Foo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Foo__yyh_Foo", None)
        self.__yyh_Foo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyh_Base"):
                opp_val = getattr(old_value, "yyh_Base", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyh_Base"):
                opp_val = getattr(value, "yyh_Base", None)
                if opp_val is None:
                    setattr(value, "yyh_Base", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yyh_Bar:

    def __init__(self, id: str, yyh_Bar: "yyh_NamedElement" = None, yyh_Bar18: "yyh_Output" = None):
        self.id = id
        self.yyh_Bar = yyh_Bar
        self.yyh_Bar18 = yyh_Bar18
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyh_Bar18(self):
        return self.__yyh_Bar18

    @yyh_Bar18.setter
    def yyh_Bar18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Bar__yyh_Bar18", None)
        self.__yyh_Bar18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyh_Output19"):
                opp_val = getattr(old_value, "yyh_Output19", None)
                if opp_val == self:
                    setattr(old_value, "yyh_Output19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyh_Output19"):
                opp_val = getattr(value, "yyh_Output19", None)
                setattr(value, "yyh_Output19", self)

    @property
    def yyh_Bar(self):
        return self.__yyh_Bar

    @yyh_Bar.setter
    def yyh_Bar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Bar__yyh_Bar", None)
        self.__yyh_Bar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyh_NamedElement8"):
                opp_val = getattr(old_value, "yyh_NamedElement8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyh_NamedElement8"):
                opp_val = getattr(value, "yyh_NamedElement8", None)
                if opp_val is None:
                    setattr(value, "yyh_NamedElement8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yyh_Alias:

    def __init__(self, id: str, yyh_Alias: "yyh_NamedElement" = None):
        self.id = id
        self.yyh_Alias = yyh_Alias
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def yyh_Alias(self):
        return self.__yyh_Alias

    @yyh_Alias.setter
    def yyh_Alias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Alias__yyh_Alias", None)
        self.__yyh_Alias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyh_NamedElement"):
                opp_val = getattr(old_value, "yyh_NamedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyh_NamedElement"):
                opp_val = getattr(value, "yyh_NamedElement", None)
                if opp_val is None:
                    setattr(value, "yyh_NamedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yyh_NamedElement(ABC):

    def __init__(self, name: str, yyh_NamedElement: set["yyh_Alias"] = None, yyh_NamedElement8: set["yyh_Bar"] = None, yyh_NamedElement10: set["yyh_Rel"] = None, yyh_NamedElement13: "yyh_Boz" = None, yyh_NamedElement22: "yyh_Rel" = None):
        self.name = name
        self.yyh_NamedElement = yyh_NamedElement if yyh_NamedElement is not None else set()
        self.yyh_NamedElement8 = yyh_NamedElement8 if yyh_NamedElement8 is not None else set()
        self.yyh_NamedElement10 = yyh_NamedElement10 if yyh_NamedElement10 is not None else set()
        self.yyh_NamedElement13 = yyh_NamedElement13
        self.yyh_NamedElement22 = yyh_NamedElement22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def yyh_NamedElement13(self):
        return self.__yyh_NamedElement13

    @yyh_NamedElement13.setter
    def yyh_NamedElement13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_NamedElement__yyh_NamedElement13", None)
        self.__yyh_NamedElement13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyh_Boz"):
                opp_val = getattr(old_value, "yyh_Boz", None)
                if opp_val == self:
                    setattr(old_value, "yyh_Boz", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyh_Boz"):
                opp_val = getattr(value, "yyh_Boz", None)
                setattr(value, "yyh_Boz", self)

    @property
    def yyh_NamedElement10(self):
        return self.__yyh_NamedElement10

    @yyh_NamedElement10.setter
    def yyh_NamedElement10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_NamedElement__yyh_NamedElement10", None)
        self.__yyh_NamedElement10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyh_Rel"):
                    opp_val = getattr(item, "yyh_Rel", None)
                    
                    if opp_val == self:
                        setattr(item, "yyh_Rel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyh_Rel"):
                    opp_val = getattr(item, "yyh_Rel", None)
                    
                    setattr(item, "yyh_Rel", self)
                    

    @property
    def yyh_NamedElement22(self):
        return self.__yyh_NamedElement22

    @yyh_NamedElement22.setter
    def yyh_NamedElement22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_NamedElement__yyh_NamedElement22", None)
        self.__yyh_NamedElement22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyh_Rel21"):
                opp_val = getattr(old_value, "yyh_Rel21", None)
                if opp_val == self:
                    setattr(old_value, "yyh_Rel21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyh_Rel21"):
                opp_val = getattr(value, "yyh_Rel21", None)
                setattr(value, "yyh_Rel21", self)

    @property
    def yyh_NamedElement(self):
        return self.__yyh_NamedElement

    @yyh_NamedElement.setter
    def yyh_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_NamedElement__yyh_NamedElement", None)
        self.__yyh_NamedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyh_Alias"):
                    opp_val = getattr(item, "yyh_Alias", None)
                    
                    if opp_val == self:
                        setattr(item, "yyh_Alias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyh_Alias"):
                    opp_val = getattr(item, "yyh_Alias", None)
                    
                    setattr(item, "yyh_Alias", self)
                    

    @property
    def yyh_NamedElement8(self):
        return self.__yyh_NamedElement8

    @yyh_NamedElement8.setter
    def yyh_NamedElement8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_NamedElement__yyh_NamedElement8", None)
        self.__yyh_NamedElement8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyh_Bar"):
                    opp_val = getattr(item, "yyh_Bar", None)
                    
                    if opp_val == self:
                        setattr(item, "yyh_Bar", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyh_Bar"):
                    opp_val = getattr(item, "yyh_Bar", None)
                    
                    setattr(item, "yyh_Bar", self)
                    

class NamedElement:

    pass
class yyh_Zing(NamedElement):

    pass
class yyh_Boz(NamedElement):

    def __init__(self, since: str, Boz: "yyh_Base" = None, yyh_Boz16: "yyh_Boz" = None, yyh_Boz14: set["yyh_Boz"] = None, relations: "yyh_Base" = None, yyh_Boz: "yyh_NamedElement" = None, yyh_Boz25: "yyh_Rel" = None):
        self.since = since
        self.Boz = Boz
        self.yyh_Boz16 = yyh_Boz16
        self.yyh_Boz14 = yyh_Boz14 if yyh_Boz14 is not None else set()
        self.relations = relations
        self.yyh_Boz = yyh_Boz
        self.yyh_Boz25 = yyh_Boz25
        
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
        old_value = getattr(self, f"_yyh_Boz__relations", None)
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
    def yyh_Boz16(self):
        return self.__yyh_Boz16

    @yyh_Boz16.setter
    def yyh_Boz16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Boz__yyh_Boz16", None)
        self.__yyh_Boz16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyh_Boz14"):
                opp_val = getattr(old_value, "yyh_Boz14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyh_Boz14"):
                opp_val = getattr(value, "yyh_Boz14", None)
                if opp_val is None:
                    setattr(value, "yyh_Boz14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Boz(self):
        return self.__Boz

    @Boz.setter
    def Boz(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Boz__Boz", None)
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
    def yyh_Boz14(self):
        return self.__yyh_Boz14

    @yyh_Boz14.setter
    def yyh_Boz14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Boz__yyh_Boz14", None)
        self.__yyh_Boz14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyh_Boz16"):
                    opp_val = getattr(item, "yyh_Boz16", None)
                    
                    if opp_val == self:
                        setattr(item, "yyh_Boz16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyh_Boz16"):
                    opp_val = getattr(item, "yyh_Boz16", None)
                    
                    setattr(item, "yyh_Boz16", self)
                    

    @property
    def yyh_Boz(self):
        return self.__yyh_Boz

    @yyh_Boz.setter
    def yyh_Boz(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Boz__yyh_Boz", None)
        self.__yyh_Boz = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyh_NamedElement13"):
                opp_val = getattr(old_value, "yyh_NamedElement13", None)
                if opp_val == self:
                    setattr(old_value, "yyh_NamedElement13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyh_NamedElement13"):
                opp_val = getattr(value, "yyh_NamedElement13", None)
                setattr(value, "yyh_NamedElement13", self)

    @property
    def yyh_Boz25(self):
        return self.__yyh_Boz25

    @yyh_Boz25.setter
    def yyh_Boz25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Boz__yyh_Boz25", None)
        self.__yyh_Boz25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyh_Rel24"):
                opp_val = getattr(old_value, "yyh_Rel24", None)
                if opp_val == self:
                    setattr(old_value, "yyh_Rel24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyh_Rel24"):
                opp_val = getattr(value, "yyh_Rel24", None)
                setattr(value, "yyh_Rel24", self)

class yyh_Baz(NamedElement):

    def __init__(self, zig: str, yyh_Baz: "yyh_Base" = None, yyh_Baz27: "yyh_Zing" = None):
        self.zig = zig
        self.yyh_Baz = yyh_Baz
        self.yyh_Baz27 = yyh_Baz27
        
    @property
    def zig(self) -> str:
        return self.__zig

    @zig.setter
    def zig(self, zig: str):
        self.__zig = zig

    @property
    def yyh_Baz27(self):
        return self.__yyh_Baz27

    @yyh_Baz27.setter
    def yyh_Baz27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Baz__yyh_Baz27", None)
        self.__yyh_Baz27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyh_Zing"):
                opp_val = getattr(old_value, "yyh_Zing", None)
                if opp_val == self:
                    setattr(old_value, "yyh_Zing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyh_Zing"):
                opp_val = getattr(value, "yyh_Zing", None)
                setattr(value, "yyh_Zing", self)

    @property
    def yyh_Baz(self):
        return self.__yyh_Baz

    @yyh_Baz.setter
    def yyh_Baz(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Baz__yyh_Baz", None)
        self.__yyh_Baz = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyh_Base5"):
                opp_val = getattr(old_value, "yyh_Base5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyh_Base5"):
                opp_val = getattr(value, "yyh_Base5", None)
                if opp_val is None:
                    setattr(value, "yyh_Base5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yyh_Base(NamedElement):

    def __init__(self, id: int, fromThing: set["yyh_Boz"] = None, yyh_Base: set["yyh_Foo"] = None, yyh_Base3: set["yyh_Output"] = None, yyh_Base5: set["yyh_Baz"] = None, Base: "yyh_Boz" = None):
        self.id = id
        self.fromThing = fromThing if fromThing is not None else set()
        self.yyh_Base = yyh_Base if yyh_Base is not None else set()
        self.yyh_Base3 = yyh_Base3 if yyh_Base3 is not None else set()
        self.yyh_Base5 = yyh_Base5 if yyh_Base5 is not None else set()
        self.Base = Base
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def yyh_Base(self):
        return self.__yyh_Base

    @yyh_Base.setter
    def yyh_Base(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Base__yyh_Base", None)
        self.__yyh_Base = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyh_Foo"):
                    opp_val = getattr(item, "yyh_Foo", None)
                    
                    if opp_val == self:
                        setattr(item, "yyh_Foo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyh_Foo"):
                    opp_val = getattr(item, "yyh_Foo", None)
                    
                    setattr(item, "yyh_Foo", self)
                    

    @property
    def yyh_Base5(self):
        return self.__yyh_Base5

    @yyh_Base5.setter
    def yyh_Base5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Base__yyh_Base5", None)
        self.__yyh_Base5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyh_Baz"):
                    opp_val = getattr(item, "yyh_Baz", None)
                    
                    if opp_val == self:
                        setattr(item, "yyh_Baz", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyh_Baz"):
                    opp_val = getattr(item, "yyh_Baz", None)
                    
                    setattr(item, "yyh_Baz", self)
                    

    @property
    def Base(self):
        return self.__Base

    @Base.setter
    def Base(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Base__Base", None)
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
    def yyh_Base3(self):
        return self.__yyh_Base3

    @yyh_Base3.setter
    def yyh_Base3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Base__yyh_Base3", None)
        self.__yyh_Base3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyh_Output"):
                    opp_val = getattr(item, "yyh_Output", None)
                    
                    if opp_val == self:
                        setattr(item, "yyh_Output", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyh_Output"):
                    opp_val = getattr(item, "yyh_Output", None)
                    
                    setattr(item, "yyh_Output", self)
                    

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyh_Base__fromThing", None)
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
                    
