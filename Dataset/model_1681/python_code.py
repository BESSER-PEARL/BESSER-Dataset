from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class syswb106_Function:

    pass
class syswb106_Component:

    pass
class syswb106_RelatedTo:

    def __init__(self, since: str, RelatedTo: "syswb106_Thing" = None, relations: "syswb106_Thing" = None, syswb106_RelatedTo: "syswb106_Thing" = None):
        self.since = since
        self.RelatedTo = RelatedTo
        self.relations = relations
        self.syswb106_RelatedTo = syswb106_RelatedTo
        
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
        old_value = getattr(self, f"_syswb106_RelatedTo__relations", None)
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
        old_value = getattr(self, f"_syswb106_RelatedTo__RelatedTo", None)
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
    def syswb106_RelatedTo(self):
        return self.__syswb106_RelatedTo

    @syswb106_RelatedTo.setter
    def syswb106_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb106_RelatedTo__syswb106_RelatedTo", None)
        self.__syswb106_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb106_Thing12"):
                opp_val = getattr(old_value, "syswb106_Thing12", None)
                if opp_val == self:
                    setattr(old_value, "syswb106_Thing12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb106_Thing12"):
                opp_val = getattr(value, "syswb106_Thing12", None)
                setattr(value, "syswb106_Thing12", self)

class syswb106_PatternCatalog:

    def __init__(self, id: str, syswb106_PatternCatalog: "syswb106_Workbench" = None, syswb106_PatternCatalog45: set["syswb106_Function"] = None):
        self.id = id
        self.syswb106_PatternCatalog = syswb106_PatternCatalog
        self.syswb106_PatternCatalog45 = syswb106_PatternCatalog45 if syswb106_PatternCatalog45 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def syswb106_PatternCatalog45(self):
        return self.__syswb106_PatternCatalog45

    @syswb106_PatternCatalog45.setter
    def syswb106_PatternCatalog45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb106_PatternCatalog__syswb106_PatternCatalog45", None)
        self.__syswb106_PatternCatalog45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswb106_Function46"):
                    opp_val = getattr(item, "syswb106_Function46", None)
                    
                    if opp_val == self:
                        setattr(item, "syswb106_Function46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswb106_Function46"):
                    opp_val = getattr(item, "syswb106_Function46", None)
                    
                    setattr(item, "syswb106_Function46", self)
                    

    @property
    def syswb106_PatternCatalog(self):
        return self.__syswb106_PatternCatalog

    @syswb106_PatternCatalog.setter
    def syswb106_PatternCatalog(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb106_PatternCatalog__syswb106_PatternCatalog", None)
        self.__syswb106_PatternCatalog = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb106_Workbench8"):
                opp_val = getattr(old_value, "syswb106_Workbench8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb106_Workbench8"):
                opp_val = getattr(value, "syswb106_Workbench8", None)
                if opp_val is None:
                    setattr(value, "syswb106_Workbench8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class syswb106_Thoughts:

    pass
class syswb106_Thing:

    def __init__(self, id: int, syswb106_Thing: "syswb106_Workbench" = None, syswb106_Thing15: "syswb106_Thoughts" = None, fromThing: set["syswb106_RelatedTo"] = None, Thing: "syswb106_RelatedTo" = None, syswb106_Thing12: "syswb106_RelatedTo" = None):
        self.id = id
        self.syswb106_Thing = syswb106_Thing
        self.syswb106_Thing15 = syswb106_Thing15
        self.fromThing = fromThing if fromThing is not None else set()
        self.Thing = Thing
        self.syswb106_Thing12 = syswb106_Thing12
        
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
        old_value = getattr(self, f"_syswb106_Thing__fromThing", None)
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
    def syswb106_Thing15(self):
        return self.__syswb106_Thing15

    @syswb106_Thing15.setter
    def syswb106_Thing15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb106_Thing__syswb106_Thing15", None)
        self.__syswb106_Thing15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb106_Thoughts14"):
                opp_val = getattr(old_value, "syswb106_Thoughts14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb106_Thoughts14"):
                opp_val = getattr(value, "syswb106_Thoughts14", None)
                if opp_val is None:
                    setattr(value, "syswb106_Thoughts14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb106_Thing__Thing", None)
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
    def syswb106_Thing12(self):
        return self.__syswb106_Thing12

    @syswb106_Thing12.setter
    def syswb106_Thing12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb106_Thing__syswb106_Thing12", None)
        self.__syswb106_Thing12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb106_RelatedTo"):
                opp_val = getattr(old_value, "syswb106_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "syswb106_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb106_RelatedTo"):
                opp_val = getattr(value, "syswb106_RelatedTo", None)
                setattr(value, "syswb106_RelatedTo", self)

    @property
    def syswb106_Thing(self):
        return self.__syswb106_Thing

    @syswb106_Thing.setter
    def syswb106_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb106_Thing__syswb106_Thing", None)
        self.__syswb106_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb106_Workbench"):
                opp_val = getattr(old_value, "syswb106_Workbench", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb106_Workbench"):
                opp_val = getattr(value, "syswb106_Workbench", None)
                if opp_val is None:
                    setattr(value, "syswb106_Workbench", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class syswb106_Workbench:

    def __init__(self, aprop: str, syswb106_Workbench4: "syswb106_System" = None, syswb106_Workbench: set["syswb106_Thing"] = None, syswb106_Workbench2: set["syswb106_Thoughts"] = None, syswb106_Workbench6: set["syswb106_FunctionProperty"] = None, syswb106_Workbench8: set["syswb106_PatternCatalog"] = None):
        self.aprop = aprop
        self.syswb106_Workbench4 = syswb106_Workbench4
        self.syswb106_Workbench = syswb106_Workbench if syswb106_Workbench is not None else set()
        self.syswb106_Workbench2 = syswb106_Workbench2 if syswb106_Workbench2 is not None else set()
        self.syswb106_Workbench6 = syswb106_Workbench6 if syswb106_Workbench6 is not None else set()
        self.syswb106_Workbench8 = syswb106_Workbench8 if syswb106_Workbench8 is not None else set()
        
    @property
    def aprop(self) -> str:
        return self.__aprop

    @aprop.setter
    def aprop(self, aprop: str):
        self.__aprop = aprop

    @property
    def syswb106_Workbench6(self):
        return self.__syswb106_Workbench6

    @syswb106_Workbench6.setter
    def syswb106_Workbench6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb106_Workbench__syswb106_Workbench6", None)
        self.__syswb106_Workbench6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswb106_FunctionProperty"):
                    opp_val = getattr(item, "syswb106_FunctionProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "syswb106_FunctionProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswb106_FunctionProperty"):
                    opp_val = getattr(item, "syswb106_FunctionProperty", None)
                    
                    setattr(item, "syswb106_FunctionProperty", self)
                    

    @property
    def syswb106_Workbench2(self):
        return self.__syswb106_Workbench2

    @syswb106_Workbench2.setter
    def syswb106_Workbench2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb106_Workbench__syswb106_Workbench2", None)
        self.__syswb106_Workbench2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswb106_Thoughts"):
                    opp_val = getattr(item, "syswb106_Thoughts", None)
                    
                    if opp_val == self:
                        setattr(item, "syswb106_Thoughts", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswb106_Thoughts"):
                    opp_val = getattr(item, "syswb106_Thoughts", None)
                    
                    setattr(item, "syswb106_Thoughts", self)
                    

    @property
    def syswb106_Workbench(self):
        return self.__syswb106_Workbench

    @syswb106_Workbench.setter
    def syswb106_Workbench(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb106_Workbench__syswb106_Workbench", None)
        self.__syswb106_Workbench = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswb106_Thing"):
                    opp_val = getattr(item, "syswb106_Thing", None)
                    
                    if opp_val == self:
                        setattr(item, "syswb106_Thing", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswb106_Thing"):
                    opp_val = getattr(item, "syswb106_Thing", None)
                    
                    setattr(item, "syswb106_Thing", self)
                    

    @property
    def syswb106_Workbench4(self):
        return self.__syswb106_Workbench4

    @syswb106_Workbench4.setter
    def syswb106_Workbench4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb106_Workbench__syswb106_Workbench4", None)
        self.__syswb106_Workbench4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb106_System"):
                opp_val = getattr(old_value, "syswb106_System", None)
                if opp_val == self:
                    setattr(old_value, "syswb106_System", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb106_System"):
                opp_val = getattr(value, "syswb106_System", None)
                setattr(value, "syswb106_System", self)

    @property
    def syswb106_Workbench8(self):
        return self.__syswb106_Workbench8

    @syswb106_Workbench8.setter
    def syswb106_Workbench8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb106_Workbench__syswb106_Workbench8", None)
        self.__syswb106_Workbench8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswb106_PatternCatalog"):
                    opp_val = getattr(item, "syswb106_PatternCatalog", None)
                    
                    if opp_val == self:
                        setattr(item, "syswb106_PatternCatalog", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswb106_PatternCatalog"):
                    opp_val = getattr(item, "syswb106_PatternCatalog", None)
                    
                    setattr(item, "syswb106_PatternCatalog", self)
                    

class syswb106_FunctionProperty:

    def __init__(self, description: str, syswb106_FunctionProperty: "syswb106_Workbench" = None, syswb106_FunctionProperty18: "syswb106_FunctionProperty" = None, syswb106_FunctionProperty16: "syswb106_FunctionProperty" = None, syswb106_FunctionProperty31: "syswb106_Function" = None):
        self.description = description
        self.syswb106_FunctionProperty = syswb106_FunctionProperty
        self.syswb106_FunctionProperty18 = syswb106_FunctionProperty18
        self.syswb106_FunctionProperty16 = syswb106_FunctionProperty16
        self.syswb106_FunctionProperty31 = syswb106_FunctionProperty31
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def syswb106_FunctionProperty31(self):
        return self.__syswb106_FunctionProperty31

    @syswb106_FunctionProperty31.setter
    def syswb106_FunctionProperty31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb106_FunctionProperty__syswb106_FunctionProperty31", None)
        self.__syswb106_FunctionProperty31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb106_Function30"):
                opp_val = getattr(old_value, "syswb106_Function30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb106_Function30"):
                opp_val = getattr(value, "syswb106_Function30", None)
                if opp_val is None:
                    setattr(value, "syswb106_Function30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswb106_FunctionProperty(self):
        return self.__syswb106_FunctionProperty

    @syswb106_FunctionProperty.setter
    def syswb106_FunctionProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb106_FunctionProperty__syswb106_FunctionProperty", None)
        self.__syswb106_FunctionProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb106_Workbench6"):
                opp_val = getattr(old_value, "syswb106_Workbench6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb106_Workbench6"):
                opp_val = getattr(value, "syswb106_Workbench6", None)
                if opp_val is None:
                    setattr(value, "syswb106_Workbench6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswb106_FunctionProperty16(self):
        return self.__syswb106_FunctionProperty16

    @syswb106_FunctionProperty16.setter
    def syswb106_FunctionProperty16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb106_FunctionProperty__syswb106_FunctionProperty16", None)
        self.__syswb106_FunctionProperty16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb106_FunctionProperty18"):
                opp_val = getattr(old_value, "syswb106_FunctionProperty18", None)
                if opp_val == self:
                    setattr(old_value, "syswb106_FunctionProperty18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb106_FunctionProperty18"):
                opp_val = getattr(value, "syswb106_FunctionProperty18", None)
                setattr(value, "syswb106_FunctionProperty18", self)

    @property
    def syswb106_FunctionProperty18(self):
        return self.__syswb106_FunctionProperty18

    @syswb106_FunctionProperty18.setter
    def syswb106_FunctionProperty18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswb106_FunctionProperty__syswb106_FunctionProperty18", None)
        self.__syswb106_FunctionProperty18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswb106_FunctionProperty16"):
                opp_val = getattr(old_value, "syswb106_FunctionProperty16", None)
                if opp_val == self:
                    setattr(old_value, "syswb106_FunctionProperty16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswb106_FunctionProperty16"):
                opp_val = getattr(value, "syswb106_FunctionProperty16", None)
                setattr(value, "syswb106_FunctionProperty16", self)

class syswb106_System:

    pass