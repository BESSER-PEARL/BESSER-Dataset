from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class syswb103_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class syswb103_PatternCatalog:

    def __init__(self, id: str, syswb103_PatternCatalog: "syswb103_Workbench" = None, syswb103_PatternCatalog45: set["syswb103_Function"] = None):
        self.id = id
        self.syswb103_PatternCatalog = syswb103_PatternCatalog
        self.syswb103_PatternCatalog45 = syswb103_PatternCatalog45 if syswb103_PatternCatalog45 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def syswb103_PatternCatalog45(self):
        return self.__syswb103_PatternCatalog45

    @syswb103_PatternCatalog45.setter
    def syswb103_PatternCatalog45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb103_PatternCatalog__syswb103_PatternCatalog45", None)
        self.__syswb103_PatternCatalog45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswb103_Function46"):
                    opp_val = getattr(item, "syswb103_Function46", None)
                    
                    if opp_val == self:
                        setattr(item, "syswb103_Function46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswb103_Function46"):
                    opp_val = getattr(item, "syswb103_Function46", None)
                    
                    setattr(item, "syswb103_Function46", self)
                    

    @property
    def syswb103_PatternCatalog(self):
        return self.__syswb103_PatternCatalog

    @syswb103_PatternCatalog.setter
    def syswb103_PatternCatalog(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb103_PatternCatalog__syswb103_PatternCatalog", None)
        self.__syswb103_PatternCatalog = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb103_Workbench8"):
                opp_val = getattr(old_value, "syswb103_Workbench8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb103_Workbench8"):
                opp_val = getattr(value, "syswb103_Workbench8", None)
                if opp_val is None:
                    setattr(value, "syswb103_Workbench8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class syswb103_RelatedTo(NamedElement):

    def __init__(self, since: str, RelatedTo: "syswb103_Thing" = None, relations: "syswb103_Thing" = None, syswb103_RelatedTo: "syswb103_Thing" = None):
        self.since = since
        self.RelatedTo = RelatedTo
        self.relations = relations
        self.syswb103_RelatedTo = syswb103_RelatedTo
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb103_RelatedTo__RelatedTo", None)
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
        old_value = getattr(self, f"_syswb103_RelatedTo__relations", None)
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
    def syswb103_RelatedTo(self):
        return self.__syswb103_RelatedTo

    @syswb103_RelatedTo.setter
    def syswb103_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb103_RelatedTo__syswb103_RelatedTo", None)
        self.__syswb103_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb103_Thing12"):
                opp_val = getattr(old_value, "syswb103_Thing12", None)
                if opp_val == self:
                    setattr(old_value, "syswb103_Thing12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb103_Thing12"):
                opp_val = getattr(value, "syswb103_Thing12", None)
                setattr(value, "syswb103_Thing12", self)

class syswb103_Thing(NamedElement):

    def __init__(self, id: int, syswb103_Thing: "syswb103_Workbench" = None, fromThing: set["syswb103_RelatedTo"] = None, Thing: "syswb103_RelatedTo" = None, syswb103_Thing12: "syswb103_RelatedTo" = None, syswb103_Thing15: "syswb103_Thoughts" = None):
        self.id = id
        self.syswb103_Thing = syswb103_Thing
        self.fromThing = fromThing if fromThing is not None else set()
        self.Thing = Thing
        self.syswb103_Thing12 = syswb103_Thing12
        self.syswb103_Thing15 = syswb103_Thing15
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def syswb103_Thing15(self):
        return self.__syswb103_Thing15

    @syswb103_Thing15.setter
    def syswb103_Thing15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb103_Thing__syswb103_Thing15", None)
        self.__syswb103_Thing15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb103_Thoughts14"):
                opp_val = getattr(old_value, "syswb103_Thoughts14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb103_Thoughts14"):
                opp_val = getattr(value, "syswb103_Thoughts14", None)
                if opp_val is None:
                    setattr(value, "syswb103_Thoughts14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswb103_Thing12(self):
        return self.__syswb103_Thing12

    @syswb103_Thing12.setter
    def syswb103_Thing12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb103_Thing__syswb103_Thing12", None)
        self.__syswb103_Thing12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb103_RelatedTo"):
                opp_val = getattr(old_value, "syswb103_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "syswb103_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb103_RelatedTo"):
                opp_val = getattr(value, "syswb103_RelatedTo", None)
                setattr(value, "syswb103_RelatedTo", self)

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb103_Thing__fromThing", None)
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
    def syswb103_Thing(self):
        return self.__syswb103_Thing

    @syswb103_Thing.setter
    def syswb103_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb103_Thing__syswb103_Thing", None)
        self.__syswb103_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb103_Workbench"):
                opp_val = getattr(old_value, "syswb103_Workbench", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb103_Workbench"):
                opp_val = getattr(value, "syswb103_Workbench", None)
                if opp_val is None:
                    setattr(value, "syswb103_Workbench", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb103_Thing__Thing", None)
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

class syswb103_Thoughts(NamedElement):

    pass
class syswb103_Component(NamedElement):

    pass
class syswb103_System(NamedElement):

    pass
class syswb103_Function(NamedElement):

    pass
class syswb103_FunctionProperty(NamedElement):

    def __init__(self, description: str, syswb103_FunctionProperty: "syswb103_Workbench" = None, syswb103_FunctionProperty18: "syswb103_FunctionProperty" = None, syswb103_FunctionProperty16: "syswb103_FunctionProperty" = None, syswb103_FunctionProperty31: "syswb103_Function" = None):
        self.description = description
        self.syswb103_FunctionProperty = syswb103_FunctionProperty
        self.syswb103_FunctionProperty18 = syswb103_FunctionProperty18
        self.syswb103_FunctionProperty16 = syswb103_FunctionProperty16
        self.syswb103_FunctionProperty31 = syswb103_FunctionProperty31
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def syswb103_FunctionProperty31(self):
        return self.__syswb103_FunctionProperty31

    @syswb103_FunctionProperty31.setter
    def syswb103_FunctionProperty31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb103_FunctionProperty__syswb103_FunctionProperty31", None)
        self.__syswb103_FunctionProperty31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb103_Function30"):
                opp_val = getattr(old_value, "syswb103_Function30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb103_Function30"):
                opp_val = getattr(value, "syswb103_Function30", None)
                if opp_val is None:
                    setattr(value, "syswb103_Function30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswb103_FunctionProperty(self):
        return self.__syswb103_FunctionProperty

    @syswb103_FunctionProperty.setter
    def syswb103_FunctionProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb103_FunctionProperty__syswb103_FunctionProperty", None)
        self.__syswb103_FunctionProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb103_Workbench6"):
                opp_val = getattr(old_value, "syswb103_Workbench6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb103_Workbench6"):
                opp_val = getattr(value, "syswb103_Workbench6", None)
                if opp_val is None:
                    setattr(value, "syswb103_Workbench6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswb103_FunctionProperty16(self):
        return self.__syswb103_FunctionProperty16

    @syswb103_FunctionProperty16.setter
    def syswb103_FunctionProperty16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb103_FunctionProperty__syswb103_FunctionProperty16", None)
        self.__syswb103_FunctionProperty16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb103_FunctionProperty18"):
                opp_val = getattr(old_value, "syswb103_FunctionProperty18", None)
                if opp_val == self:
                    setattr(old_value, "syswb103_FunctionProperty18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb103_FunctionProperty18"):
                opp_val = getattr(value, "syswb103_FunctionProperty18", None)
                setattr(value, "syswb103_FunctionProperty18", self)

    @property
    def syswb103_FunctionProperty18(self):
        return self.__syswb103_FunctionProperty18

    @syswb103_FunctionProperty18.setter
    def syswb103_FunctionProperty18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb103_FunctionProperty__syswb103_FunctionProperty18", None)
        self.__syswb103_FunctionProperty18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb103_FunctionProperty16"):
                opp_val = getattr(old_value, "syswb103_FunctionProperty16", None)
                if opp_val == self:
                    setattr(old_value, "syswb103_FunctionProperty16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb103_FunctionProperty16"):
                opp_val = getattr(value, "syswb103_FunctionProperty16", None)
                setattr(value, "syswb103_FunctionProperty16", self)

class syswb103_Workbench(NamedElement):

    def __init__(self, aprop: str, syswb103_Workbench: set["syswb103_Thing"] = None, syswb103_Workbench2: set["syswb103_Thoughts"] = None, syswb103_Workbench4: "syswb103_System" = None, syswb103_Workbench6: set["syswb103_FunctionProperty"] = None, syswb103_Workbench8: set["syswb103_PatternCatalog"] = None):
        self.aprop = aprop
        self.syswb103_Workbench = syswb103_Workbench if syswb103_Workbench is not None else set()
        self.syswb103_Workbench2 = syswb103_Workbench2 if syswb103_Workbench2 is not None else set()
        self.syswb103_Workbench4 = syswb103_Workbench4
        self.syswb103_Workbench6 = syswb103_Workbench6 if syswb103_Workbench6 is not None else set()
        self.syswb103_Workbench8 = syswb103_Workbench8 if syswb103_Workbench8 is not None else set()
        
    @property
    def aprop(self) -> str:
        return self.__aprop

    @aprop.setter
    def aprop(self, aprop: str):
        self.__aprop = aprop

    @property
    def syswb103_Workbench(self):
        return self.__syswb103_Workbench

    @syswb103_Workbench.setter
    def syswb103_Workbench(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb103_Workbench__syswb103_Workbench", None)
        self.__syswb103_Workbench = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswb103_Thing"):
                    opp_val = getattr(item, "syswb103_Thing", None)
                    
                    if opp_val == self:
                        setattr(item, "syswb103_Thing", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswb103_Thing"):
                    opp_val = getattr(item, "syswb103_Thing", None)
                    
                    setattr(item, "syswb103_Thing", self)
                    

    @property
    def syswb103_Workbench6(self):
        return self.__syswb103_Workbench6

    @syswb103_Workbench6.setter
    def syswb103_Workbench6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb103_Workbench__syswb103_Workbench6", None)
        self.__syswb103_Workbench6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswb103_FunctionProperty"):
                    opp_val = getattr(item, "syswb103_FunctionProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "syswb103_FunctionProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswb103_FunctionProperty"):
                    opp_val = getattr(item, "syswb103_FunctionProperty", None)
                    
                    setattr(item, "syswb103_FunctionProperty", self)
                    

    @property
    def syswb103_Workbench4(self):
        return self.__syswb103_Workbench4

    @syswb103_Workbench4.setter
    def syswb103_Workbench4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb103_Workbench__syswb103_Workbench4", None)
        self.__syswb103_Workbench4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb103_System"):
                opp_val = getattr(old_value, "syswb103_System", None)
                if opp_val == self:
                    setattr(old_value, "syswb103_System", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb103_System"):
                opp_val = getattr(value, "syswb103_System", None)
                setattr(value, "syswb103_System", self)

    @property
    def syswb103_Workbench2(self):
        return self.__syswb103_Workbench2

    @syswb103_Workbench2.setter
    def syswb103_Workbench2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb103_Workbench__syswb103_Workbench2", None)
        self.__syswb103_Workbench2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswb103_Thoughts"):
                    opp_val = getattr(item, "syswb103_Thoughts", None)
                    
                    if opp_val == self:
                        setattr(item, "syswb103_Thoughts", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswb103_Thoughts"):
                    opp_val = getattr(item, "syswb103_Thoughts", None)
                    
                    setattr(item, "syswb103_Thoughts", self)
                    

    @property
    def syswb103_Workbench8(self):
        return self.__syswb103_Workbench8

    @syswb103_Workbench8.setter
    def syswb103_Workbench8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb103_Workbench__syswb103_Workbench8", None)
        self.__syswb103_Workbench8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswb103_PatternCatalog"):
                    opp_val = getattr(item, "syswb103_PatternCatalog", None)
                    
                    if opp_val == self:
                        setattr(item, "syswb103_PatternCatalog", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswb103_PatternCatalog"):
                    opp_val = getattr(item, "syswb103_PatternCatalog", None)
                    
                    setattr(item, "syswb103_PatternCatalog", self)
                    
