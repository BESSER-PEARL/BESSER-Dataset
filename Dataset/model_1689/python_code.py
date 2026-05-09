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
        
        pass
    @property
    def hi(self):
        return self.__hi

    @hi.setter
    def hi(self, hi: str):
        self.__hi = hi


class yyk_Bouz(Baz):

    def __init__(self, bil: str, yyk_Bouz: set["yyk_Zing"] = None):
        self.bil = bil
        self.yyk_Bouz = yyk_Bouz if yyk_Bouz is not None else set()
        
        pass
    @property
    def bil(self):
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
                if hasattr(item, "yyk_Zing29"):
                    opp_val = getattr(item, "yyk_Zing29", None)
                    
                    if opp_val == self:
                        setattr(item, "yyk_Zing29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyk_Zing29"):
                    opp_val = getattr(item, "yyk_Zing29", None)
                    
                    setattr(item, "yyk_Zing29", self)
                    

class yyk_NamedElement(ABC):

    def __init__(self, name: str, yyk_NamedElement: set["yyk_Alias"] = None, yyk_NamedElement8: set["yyk_Bar"] = None, yyk_NamedElement10: set["yyk_Rel"] = None, yyk_NamedElement13: "yyk_Relation" = None, yyk_NamedElement22: "yyk_Rel" = None):
        self.name = name
        self.yyk_NamedElement = yyk_NamedElement if yyk_NamedElement is not None else set()
        self.yyk_NamedElement8 = yyk_NamedElement8 if yyk_NamedElement8 is not None else set()
        self.yyk_NamedElement10 = yyk_NamedElement10 if yyk_NamedElement10 is not None else set()
        self.yyk_NamedElement13 = yyk_NamedElement13
        self.yyk_NamedElement22 = yyk_NamedElement22
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
    def yyk_NamedElement8(self):
        return self.__yyk_NamedElement8

    @yyk_NamedElement8.setter
    def yyk_NamedElement8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_NamedElement__yyk_NamedElement8", None)
        self.__yyk_NamedElement8 = value if value is not None else set()
        
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
    def yyk_NamedElement13(self):
        return self.__yyk_NamedElement13

    @yyk_NamedElement13.setter
    def yyk_NamedElement13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_NamedElement__yyk_NamedElement13", None)
        self.__yyk_NamedElement13 = value
        
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
    def yyk_NamedElement10(self):
        return self.__yyk_NamedElement10

    @yyk_NamedElement10.setter
    def yyk_NamedElement10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_NamedElement__yyk_NamedElement10", None)
        self.__yyk_NamedElement10 = value if value is not None else set()
        
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
                    

    @property
    def yyk_NamedElement22(self):
        return self.__yyk_NamedElement22

    @yyk_NamedElement22.setter
    def yyk_NamedElement22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_NamedElement__yyk_NamedElement22", None)
        self.__yyk_NamedElement22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyk_Rel21"):
                opp_val = getattr(old_value, "yyk_Rel21", None)
                if opp_val == self:
                    setattr(old_value, "yyk_Rel21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_Rel21"):
                opp_val = getattr(value, "yyk_Rel21", None)
                setattr(value, "yyk_Rel21", self)

class yyk_Output:

    def __init__(self, id: str, yyk_Output: "yyk_Base" = None, yyk_Output19: "yyk_Bar" = None):
        self.id = id
        self.yyk_Output = yyk_Output
        self.yyk_Output19 = yyk_Output19
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


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
            if hasattr(old_value, "yyk_Base3"):
                opp_val = getattr(old_value, "yyk_Base3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_Base3"):
                opp_val = getattr(value, "yyk_Base3", None)
                if opp_val is None:
                    setattr(value, "yyk_Base3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def yyk_Output19(self):
        return self.__yyk_Output19

    @yyk_Output19.setter
    def yyk_Output19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Output__yyk_Output19", None)
        self.__yyk_Output19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyk_Bar18"):
                opp_val = getattr(old_value, "yyk_Bar18", None)
                if opp_val == self:
                    setattr(old_value, "yyk_Bar18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_Bar18"):
                opp_val = getattr(value, "yyk_Bar18", None)
                setattr(value, "yyk_Bar18", self)

class yyk_Foo:

    def __init__(self, id: str, yyk_Foo: "yyk_Base" = None):
        self.id = id
        self.yyk_Foo = yyk_Foo
        
        pass
    @property
    def id(self):
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

class NamedElement:

    pass
class yyk_Relation(NamedElement):

    def __init__(self, since: str, relations: "yyk_Base" = None, yyk_Relation: "yyk_NamedElement" = None, yyk_Relation16: "yyk_Relation" = None, yyk_Relation14: set["yyk_Relation"] = None, Relation: "yyk_Base" = None, yyk_Relation25: "yyk_Rel" = None):
        self.since = since
        self.relations = relations
        self.yyk_Relation = yyk_Relation
        self.yyk_Relation16 = yyk_Relation16
        self.yyk_Relation14 = yyk_Relation14 if yyk_Relation14 is not None else set()
        self.Relation = Relation
        self.yyk_Relation25 = yyk_Relation25
        
        pass
    @property
    def since(self):
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
            if hasattr(old_value, "yyk_NamedElement13"):
                opp_val = getattr(old_value, "yyk_NamedElement13", None)
                if opp_val == self:
                    setattr(old_value, "yyk_NamedElement13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_NamedElement13"):
                opp_val = getattr(value, "yyk_NamedElement13", None)
                setattr(value, "yyk_NamedElement13", self)

    @property
    def relations(self):
        return self.__relations

    @relations.setter
    def relations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Relation__relations", None)
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
        old_value = getattr(self, f"_yyk_Relation__Relation", None)
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
    def yyk_Relation14(self):
        return self.__yyk_Relation14

    @yyk_Relation14.setter
    def yyk_Relation14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Relation__yyk_Relation14", None)
        self.__yyk_Relation14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yyk_Relation16"):
                    opp_val = getattr(item, "yyk_Relation16", None)
                    
                    if opp_val == self:
                        setattr(item, "yyk_Relation16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yyk_Relation16"):
                    opp_val = getattr(item, "yyk_Relation16", None)
                    
                    setattr(item, "yyk_Relation16", self)
                    

    @property
    def yyk_Relation25(self):
        return self.__yyk_Relation25

    @yyk_Relation25.setter
    def yyk_Relation25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Relation__yyk_Relation25", None)
        self.__yyk_Relation25 = value
        
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
    def yyk_Relation16(self):
        return self.__yyk_Relation16

    @yyk_Relation16.setter
    def yyk_Relation16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Relation__yyk_Relation16", None)
        self.__yyk_Relation16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyk_Relation14"):
                opp_val = getattr(old_value, "yyk_Relation14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_Relation14"):
                opp_val = getattr(value, "yyk_Relation14", None)
                if opp_val is None:
                    setattr(value, "yyk_Relation14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yyk_Baz(NamedElement):

    def __init__(self, zig: str, yyk_Baz: "yyk_Base" = None, yyk_Baz27: "yyk_Zing" = None):
        self.zig = zig
        self.yyk_Baz = yyk_Baz
        self.yyk_Baz27 = yyk_Baz27
        
        pass
    @property
    def zig(self):
        return self.__zig

    @zig.setter
    def zig(self, zig: str):
        self.__zig = zig


    @property
    def yyk_Baz27(self):
        return self.__yyk_Baz27

    @yyk_Baz27.setter
    def yyk_Baz27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Baz__yyk_Baz27", None)
        self.__yyk_Baz27 = value
        
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
            if hasattr(old_value, "yyk_Base5"):
                opp_val = getattr(old_value, "yyk_Base5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_Base5"):
                opp_val = getattr(value, "yyk_Base5", None)
                if opp_val is None:
                    setattr(value, "yyk_Base5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yyk_Zing(NamedElement):

    pass
class yyk_Base(NamedElement):

    def __init__(self, id: int, Base: "yyk_Relation" = None, fromThing: set["yyk_Relation"] = None, yyk_Base: set["yyk_Foo"] = None, yyk_Base3: set["yyk_Output"] = None, yyk_Base5: set["yyk_Baz"] = None):
        self.id = id
        self.Base = Base
        self.fromThing = fromThing if fromThing is not None else set()
        self.yyk_Base = yyk_Base if yyk_Base is not None else set()
        self.yyk_Base3 = yyk_Base3 if yyk_Base3 is not None else set()
        self.yyk_Base5 = yyk_Base5 if yyk_Base5 is not None else set()
        
        pass
    @property
    def id(self):
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
        old_value = getattr(self, f"_yyk_Base__fromThing", None)
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
    def Base(self):
        return self.__Base

    @Base.setter
    def Base(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Base__Base", None)
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
    def yyk_Base3(self):
        return self.__yyk_Base3

    @yyk_Base3.setter
    def yyk_Base3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Base__yyk_Base3", None)
        self.__yyk_Base3 = value if value is not None else set()
        
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
    def yyk_Base5(self):
        return self.__yyk_Base5

    @yyk_Base5.setter
    def yyk_Base5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Base__yyk_Base5", None)
        self.__yyk_Base5 = value if value is not None else set()
        
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
                    

class yyk_Rel:

    def __init__(self, id: str, yyk_Rel: "yyk_NamedElement" = None, yyk_Rel24: "yyk_Relation" = None, yyk_Rel21: "yyk_NamedElement" = None):
        self.id = id
        self.yyk_Rel = yyk_Rel
        self.yyk_Rel24 = yyk_Rel24
        self.yyk_Rel21 = yyk_Rel21
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def yyk_Rel21(self):
        return self.__yyk_Rel21

    @yyk_Rel21.setter
    def yyk_Rel21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Rel__yyk_Rel21", None)
        self.__yyk_Rel21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyk_NamedElement22"):
                opp_val = getattr(old_value, "yyk_NamedElement22", None)
                if opp_val == self:
                    setattr(old_value, "yyk_NamedElement22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_NamedElement22"):
                opp_val = getattr(value, "yyk_NamedElement22", None)
                setattr(value, "yyk_NamedElement22", self)

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
            if hasattr(old_value, "yyk_NamedElement10"):
                opp_val = getattr(old_value, "yyk_NamedElement10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_NamedElement10"):
                opp_val = getattr(value, "yyk_NamedElement10", None)
                if opp_val is None:
                    setattr(value, "yyk_NamedElement10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "yyk_Relation25"):
                opp_val = getattr(old_value, "yyk_Relation25", None)
                if opp_val == self:
                    setattr(old_value, "yyk_Relation25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_Relation25"):
                opp_val = getattr(value, "yyk_Relation25", None)
                setattr(value, "yyk_Relation25", self)

class yyk_Bar:

    def __init__(self, id: str, yyk_Bar: "yyk_NamedElement" = None, yyk_Bar18: "yyk_Output" = None):
        self.id = id
        self.yyk_Bar = yyk_Bar
        self.yyk_Bar18 = yyk_Bar18
        
        pass
    @property
    def id(self):
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
            if hasattr(old_value, "yyk_NamedElement8"):
                opp_val = getattr(old_value, "yyk_NamedElement8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_NamedElement8"):
                opp_val = getattr(value, "yyk_NamedElement8", None)
                if opp_val is None:
                    setattr(value, "yyk_NamedElement8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def yyk_Bar18(self):
        return self.__yyk_Bar18

    @yyk_Bar18.setter
    def yyk_Bar18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yyk_Bar__yyk_Bar18", None)
        self.__yyk_Bar18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yyk_Output19"):
                opp_val = getattr(old_value, "yyk_Output19", None)
                if opp_val == self:
                    setattr(old_value, "yyk_Output19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yyk_Output19"):
                opp_val = getattr(value, "yyk_Output19", None)
                setattr(value, "yyk_Output19", self)

class yyk_Alias:

    def __init__(self, id: str, yyk_Alias: "yyk_NamedElement" = None):
        self.id = id
        self.yyk_Alias = yyk_Alias
        
        pass
    @property
    def id(self):
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
