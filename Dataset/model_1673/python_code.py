from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class syswb101_Named(ABC):

    def __init__(self, ident: str):
        self.ident = ident
        
    @property
    def ident(self) -> str:
        return self.__ident

    @ident.setter
    def ident(self, ident: str):
        self.__ident = ident

class syswb101_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Named:

    pass
class syswb101_Component(Named):

    pass
class syswb101_Function(Named):

    pass
class syswb101_Workbench(Named):

    def __init__(self, aprop: str, syswb101_Workbench2: set["syswb101_Thoughts"] = None, syswb101_Workbench4: "syswb101_System" = None, syswb101_Workbench6: set["syswb101_FunctionProperty"] = None, syswb101_Workbench8: set["syswb101_PatternCatalog"] = None, syswb101_Workbench: set["syswb101_Thing"] = None):
        self.aprop = aprop
        self.syswb101_Workbench2 = syswb101_Workbench2 if syswb101_Workbench2 is not None else set()
        self.syswb101_Workbench4 = syswb101_Workbench4
        self.syswb101_Workbench6 = syswb101_Workbench6 if syswb101_Workbench6 is not None else set()
        self.syswb101_Workbench8 = syswb101_Workbench8 if syswb101_Workbench8 is not None else set()
        self.syswb101_Workbench = syswb101_Workbench if syswb101_Workbench is not None else set()
        
    @property
    def aprop(self) -> str:
        return self.__aprop

    @aprop.setter
    def aprop(self, aprop: str):
        self.__aprop = aprop

    @property
    def syswb101_Workbench6(self):
        return self.__syswb101_Workbench6

    @syswb101_Workbench6.setter
    def syswb101_Workbench6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb101_Workbench__syswb101_Workbench6", None)
        self.__syswb101_Workbench6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswb101_FunctionProperty"):
                    opp_val = getattr(item, "syswb101_FunctionProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "syswb101_FunctionProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswb101_FunctionProperty"):
                    opp_val = getattr(item, "syswb101_FunctionProperty", None)
                    
                    setattr(item, "syswb101_FunctionProperty", self)
                    

    @property
    def syswb101_Workbench(self):
        return self.__syswb101_Workbench

    @syswb101_Workbench.setter
    def syswb101_Workbench(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb101_Workbench__syswb101_Workbench", None)
        self.__syswb101_Workbench = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswb101_Thing"):
                    opp_val = getattr(item, "syswb101_Thing", None)
                    
                    if opp_val == self:
                        setattr(item, "syswb101_Thing", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswb101_Thing"):
                    opp_val = getattr(item, "syswb101_Thing", None)
                    
                    setattr(item, "syswb101_Thing", self)
                    

    @property
    def syswb101_Workbench4(self):
        return self.__syswb101_Workbench4

    @syswb101_Workbench4.setter
    def syswb101_Workbench4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb101_Workbench__syswb101_Workbench4", None)
        self.__syswb101_Workbench4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb101_System"):
                opp_val = getattr(old_value, "syswb101_System", None)
                if opp_val == self:
                    setattr(old_value, "syswb101_System", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb101_System"):
                opp_val = getattr(value, "syswb101_System", None)
                setattr(value, "syswb101_System", self)

    @property
    def syswb101_Workbench2(self):
        return self.__syswb101_Workbench2

    @syswb101_Workbench2.setter
    def syswb101_Workbench2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb101_Workbench__syswb101_Workbench2", None)
        self.__syswb101_Workbench2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswb101_Thoughts"):
                    opp_val = getattr(item, "syswb101_Thoughts", None)
                    
                    if opp_val == self:
                        setattr(item, "syswb101_Thoughts", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswb101_Thoughts"):
                    opp_val = getattr(item, "syswb101_Thoughts", None)
                    
                    setattr(item, "syswb101_Thoughts", self)
                    

    @property
    def syswb101_Workbench8(self):
        return self.__syswb101_Workbench8

    @syswb101_Workbench8.setter
    def syswb101_Workbench8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb101_Workbench__syswb101_Workbench8", None)
        self.__syswb101_Workbench8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswb101_PatternCatalog"):
                    opp_val = getattr(item, "syswb101_PatternCatalog", None)
                    
                    if opp_val == self:
                        setattr(item, "syswb101_PatternCatalog", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswb101_PatternCatalog"):
                    opp_val = getattr(item, "syswb101_PatternCatalog", None)
                    
                    setattr(item, "syswb101_PatternCatalog", self)
                    

class NamedElement:

    pass
class syswb101_Thing(NamedElement):

    def __init__(self, id: int, syswb101_Thing: "syswb101_Workbench" = None, Thing: "syswb101_RelatedTo" = None, syswb101_Thing12: "syswb101_RelatedTo" = None, syswb101_Thing15: "syswb101_Thoughts" = None, fromThing: set["syswb101_RelatedTo"] = None):
        self.id = id
        self.syswb101_Thing = syswb101_Thing
        self.Thing = Thing
        self.syswb101_Thing12 = syswb101_Thing12
        self.syswb101_Thing15 = syswb101_Thing15
        self.fromThing = fromThing if fromThing is not None else set()
        
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
        old_value = getattr(self, f"_syswb101_Thing__fromThing", None)
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
    def syswb101_Thing12(self):
        return self.__syswb101_Thing12

    @syswb101_Thing12.setter
    def syswb101_Thing12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb101_Thing__syswb101_Thing12", None)
        self.__syswb101_Thing12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb101_RelatedTo"):
                opp_val = getattr(old_value, "syswb101_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "syswb101_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb101_RelatedTo"):
                opp_val = getattr(value, "syswb101_RelatedTo", None)
                setattr(value, "syswb101_RelatedTo", self)

    @property
    def syswb101_Thing(self):
        return self.__syswb101_Thing

    @syswb101_Thing.setter
    def syswb101_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb101_Thing__syswb101_Thing", None)
        self.__syswb101_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb101_Workbench"):
                opp_val = getattr(old_value, "syswb101_Workbench", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb101_Workbench"):
                opp_val = getattr(value, "syswb101_Workbench", None)
                if opp_val is None:
                    setattr(value, "syswb101_Workbench", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswb101_Thing15(self):
        return self.__syswb101_Thing15

    @syswb101_Thing15.setter
    def syswb101_Thing15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb101_Thing__syswb101_Thing15", None)
        self.__syswb101_Thing15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb101_Thoughts14"):
                opp_val = getattr(old_value, "syswb101_Thoughts14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb101_Thoughts14"):
                opp_val = getattr(value, "syswb101_Thoughts14", None)
                if opp_val is None:
                    setattr(value, "syswb101_Thoughts14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb101_Thing__Thing", None)
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

class syswb101_RelatedTo(NamedElement):

    def __init__(self, since: str, relations: "syswb101_Thing" = None, syswb101_RelatedTo: "syswb101_Thing" = None, RelatedTo: "syswb101_Thing" = None):
        self.since = since
        self.relations = relations
        self.syswb101_RelatedTo = syswb101_RelatedTo
        self.RelatedTo = RelatedTo
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def syswb101_RelatedTo(self):
        return self.__syswb101_RelatedTo

    @syswb101_RelatedTo.setter
    def syswb101_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb101_RelatedTo__syswb101_RelatedTo", None)
        self.__syswb101_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb101_Thing12"):
                opp_val = getattr(old_value, "syswb101_Thing12", None)
                if opp_val == self:
                    setattr(old_value, "syswb101_Thing12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb101_Thing12"):
                opp_val = getattr(value, "syswb101_Thing12", None)
                setattr(value, "syswb101_Thing12", self)

    @property
    def relations(self):
        return self.__relations

    @relations.setter
    def relations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb101_RelatedTo__relations", None)
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
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb101_RelatedTo__RelatedTo", None)
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

class syswb101_PatternCatalog:

    def __init__(self, id: str, syswb101_PatternCatalog: "syswb101_Workbench" = None, syswb101_PatternCatalog45: set["syswb101_Function"] = None):
        self.id = id
        self.syswb101_PatternCatalog = syswb101_PatternCatalog
        self.syswb101_PatternCatalog45 = syswb101_PatternCatalog45 if syswb101_PatternCatalog45 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def syswb101_PatternCatalog(self):
        return self.__syswb101_PatternCatalog

    @syswb101_PatternCatalog.setter
    def syswb101_PatternCatalog(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb101_PatternCatalog__syswb101_PatternCatalog", None)
        self.__syswb101_PatternCatalog = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb101_Workbench8"):
                opp_val = getattr(old_value, "syswb101_Workbench8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb101_Workbench8"):
                opp_val = getattr(value, "syswb101_Workbench8", None)
                if opp_val is None:
                    setattr(value, "syswb101_Workbench8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswb101_PatternCatalog45(self):
        return self.__syswb101_PatternCatalog45

    @syswb101_PatternCatalog45.setter
    def syswb101_PatternCatalog45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb101_PatternCatalog__syswb101_PatternCatalog45", None)
        self.__syswb101_PatternCatalog45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswb101_Function46"):
                    opp_val = getattr(item, "syswb101_Function46", None)
                    
                    if opp_val == self:
                        setattr(item, "syswb101_Function46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswb101_Function46"):
                    opp_val = getattr(item, "syswb101_Function46", None)
                    
                    setattr(item, "syswb101_Function46", self)
                    

class syswb101_FunctionProperty(Named):

    def __init__(self, description: str, syswb101_FunctionProperty: "syswb101_Workbench" = None, syswb101_FunctionProperty18: "syswb101_FunctionProperty" = None, syswb101_FunctionProperty16: "syswb101_FunctionProperty" = None, syswb101_FunctionProperty31: "syswb101_Function" = None):
        self.description = description
        self.syswb101_FunctionProperty = syswb101_FunctionProperty
        self.syswb101_FunctionProperty18 = syswb101_FunctionProperty18
        self.syswb101_FunctionProperty16 = syswb101_FunctionProperty16
        self.syswb101_FunctionProperty31 = syswb101_FunctionProperty31
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def syswb101_FunctionProperty18(self):
        return self.__syswb101_FunctionProperty18

    @syswb101_FunctionProperty18.setter
    def syswb101_FunctionProperty18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb101_FunctionProperty__syswb101_FunctionProperty18", None)
        self.__syswb101_FunctionProperty18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb101_FunctionProperty16"):
                opp_val = getattr(old_value, "syswb101_FunctionProperty16", None)
                if opp_val == self:
                    setattr(old_value, "syswb101_FunctionProperty16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb101_FunctionProperty16"):
                opp_val = getattr(value, "syswb101_FunctionProperty16", None)
                setattr(value, "syswb101_FunctionProperty16", self)

    @property
    def syswb101_FunctionProperty31(self):
        return self.__syswb101_FunctionProperty31

    @syswb101_FunctionProperty31.setter
    def syswb101_FunctionProperty31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb101_FunctionProperty__syswb101_FunctionProperty31", None)
        self.__syswb101_FunctionProperty31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb101_Function30"):
                opp_val = getattr(old_value, "syswb101_Function30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb101_Function30"):
                opp_val = getattr(value, "syswb101_Function30", None)
                if opp_val is None:
                    setattr(value, "syswb101_Function30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswb101_FunctionProperty(self):
        return self.__syswb101_FunctionProperty

    @syswb101_FunctionProperty.setter
    def syswb101_FunctionProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb101_FunctionProperty__syswb101_FunctionProperty", None)
        self.__syswb101_FunctionProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb101_Workbench6"):
                opp_val = getattr(old_value, "syswb101_Workbench6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb101_Workbench6"):
                opp_val = getattr(value, "syswb101_Workbench6", None)
                if opp_val is None:
                    setattr(value, "syswb101_Workbench6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswb101_FunctionProperty16(self):
        return self.__syswb101_FunctionProperty16

    @syswb101_FunctionProperty16.setter
    def syswb101_FunctionProperty16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb101_FunctionProperty__syswb101_FunctionProperty16", None)
        self.__syswb101_FunctionProperty16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb101_FunctionProperty18"):
                opp_val = getattr(old_value, "syswb101_FunctionProperty18", None)
                if opp_val == self:
                    setattr(old_value, "syswb101_FunctionProperty18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb101_FunctionProperty18"):
                opp_val = getattr(value, "syswb101_FunctionProperty18", None)
                setattr(value, "syswb101_FunctionProperty18", self)

class syswb101_System(Named):

    pass
class syswb101_Thoughts(NamedElement):

    pass