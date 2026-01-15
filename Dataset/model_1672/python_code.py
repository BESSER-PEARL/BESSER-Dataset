from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class systemworkbench102_Named:

    def __init__(self, ident: str):
        self.ident = ident
        
    @property
    def ident(self) -> str:
        return self.__ident

    @ident.setter
    def ident(self, ident: str):
        self.__ident = ident

class systemworkbench102_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class systemworkbench102_RelatedTo(NamedElement):

    def __init__(self, since: str, RelatedTo: "systemworkbench102_Thing" = None, relations: "systemworkbench102_Thing" = None, systemworkbench102_RelatedTo: "systemworkbench102_Thing" = None):
        self.since = since
        self.RelatedTo = RelatedTo
        self.relations = relations
        self.systemworkbench102_RelatedTo = systemworkbench102_RelatedTo
        
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
        old_value = getattr(self, f"_systemworkbench102_RelatedTo__relations", None)
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
        old_value = getattr(self, f"_systemworkbench102_RelatedTo__RelatedTo", None)
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
    def systemworkbench102_RelatedTo(self):
        return self.__systemworkbench102_RelatedTo

    @systemworkbench102_RelatedTo.setter
    def systemworkbench102_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench102_RelatedTo__systemworkbench102_RelatedTo", None)
        self.__systemworkbench102_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench102_Thing12"):
                opp_val = getattr(old_value, "systemworkbench102_Thing12", None)
                if opp_val == self:
                    setattr(old_value, "systemworkbench102_Thing12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench102_Thing12"):
                opp_val = getattr(value, "systemworkbench102_Thing12", None)
                setattr(value, "systemworkbench102_Thing12", self)

class systemworkbench102_Thoughts(NamedElement):

    pass
class systemworkbench102_PatternCatalog:

    def __init__(self, id: int, systemworkbench102_PatternCatalog: "systemworkbench102_Workbench" = None, systemworkbench102_PatternCatalog45: set["systemworkbench102_Function"] = None):
        self.id = id
        self.systemworkbench102_PatternCatalog = systemworkbench102_PatternCatalog
        self.systemworkbench102_PatternCatalog45 = systemworkbench102_PatternCatalog45 if systemworkbench102_PatternCatalog45 is not None else set()
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def systemworkbench102_PatternCatalog(self):
        return self.__systemworkbench102_PatternCatalog

    @systemworkbench102_PatternCatalog.setter
    def systemworkbench102_PatternCatalog(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench102_PatternCatalog__systemworkbench102_PatternCatalog", None)
        self.__systemworkbench102_PatternCatalog = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench102_Workbench8"):
                opp_val = getattr(old_value, "systemworkbench102_Workbench8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench102_Workbench8"):
                opp_val = getattr(value, "systemworkbench102_Workbench8", None)
                if opp_val is None:
                    setattr(value, "systemworkbench102_Workbench8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def systemworkbench102_PatternCatalog45(self):
        return self.__systemworkbench102_PatternCatalog45

    @systemworkbench102_PatternCatalog45.setter
    def systemworkbench102_PatternCatalog45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench102_PatternCatalog__systemworkbench102_PatternCatalog45", None)
        self.__systemworkbench102_PatternCatalog45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "systemworkbench102_Function46"):
                    opp_val = getattr(item, "systemworkbench102_Function46", None)
                    
                    if opp_val == self:
                        setattr(item, "systemworkbench102_Function46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "systemworkbench102_Function46"):
                    opp_val = getattr(item, "systemworkbench102_Function46", None)
                    
                    setattr(item, "systemworkbench102_Function46", self)
                    

class systemworkbench102_Thing(NamedElement):

    def __init__(self, id: int, systemworkbench102_Thing: "systemworkbench102_Workbench" = None, fromThing: set["systemworkbench102_RelatedTo"] = None, Thing: "systemworkbench102_RelatedTo" = None, systemworkbench102_Thing15: "systemworkbench102_Thoughts" = None, systemworkbench102_Thing12: "systemworkbench102_RelatedTo" = None):
        self.id = id
        self.systemworkbench102_Thing = systemworkbench102_Thing
        self.fromThing = fromThing if fromThing is not None else set()
        self.Thing = Thing
        self.systemworkbench102_Thing15 = systemworkbench102_Thing15
        self.systemworkbench102_Thing12 = systemworkbench102_Thing12
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def systemworkbench102_Thing(self):
        return self.__systemworkbench102_Thing

    @systemworkbench102_Thing.setter
    def systemworkbench102_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench102_Thing__systemworkbench102_Thing", None)
        self.__systemworkbench102_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench102_Workbench"):
                opp_val = getattr(old_value, "systemworkbench102_Workbench", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench102_Workbench"):
                opp_val = getattr(value, "systemworkbench102_Workbench", None)
                if opp_val is None:
                    setattr(value, "systemworkbench102_Workbench", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def systemworkbench102_Thing12(self):
        return self.__systemworkbench102_Thing12

    @systemworkbench102_Thing12.setter
    def systemworkbench102_Thing12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench102_Thing__systemworkbench102_Thing12", None)
        self.__systemworkbench102_Thing12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench102_RelatedTo"):
                opp_val = getattr(old_value, "systemworkbench102_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "systemworkbench102_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench102_RelatedTo"):
                opp_val = getattr(value, "systemworkbench102_RelatedTo", None)
                setattr(value, "systemworkbench102_RelatedTo", self)

    @property
    def systemworkbench102_Thing15(self):
        return self.__systemworkbench102_Thing15

    @systemworkbench102_Thing15.setter
    def systemworkbench102_Thing15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench102_Thing__systemworkbench102_Thing15", None)
        self.__systemworkbench102_Thing15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench102_Thoughts14"):
                opp_val = getattr(old_value, "systemworkbench102_Thoughts14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench102_Thoughts14"):
                opp_val = getattr(value, "systemworkbench102_Thoughts14", None)
                if opp_val is None:
                    setattr(value, "systemworkbench102_Thoughts14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench102_Thing__fromThing", None)
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
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench102_Thing__Thing", None)
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

class Named:

    pass
class systemworkbench102_Function(Named):

    pass
class systemworkbench102_System(Named):

    pass
class systemworkbench102_Component(Named):

    pass
class systemworkbench102_FunctionProperty(Named):

    def __init__(self, description: str, systemworkbench102_FunctionProperty: "systemworkbench102_Workbench" = None, systemworkbench102_FunctionProperty18: "systemworkbench102_FunctionProperty" = None, systemworkbench102_FunctionProperty16: "systemworkbench102_FunctionProperty" = None, systemworkbench102_FunctionProperty31: "systemworkbench102_Function" = None):
        self.description = description
        self.systemworkbench102_FunctionProperty = systemworkbench102_FunctionProperty
        self.systemworkbench102_FunctionProperty18 = systemworkbench102_FunctionProperty18
        self.systemworkbench102_FunctionProperty16 = systemworkbench102_FunctionProperty16
        self.systemworkbench102_FunctionProperty31 = systemworkbench102_FunctionProperty31
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def systemworkbench102_FunctionProperty18(self):
        return self.__systemworkbench102_FunctionProperty18

    @systemworkbench102_FunctionProperty18.setter
    def systemworkbench102_FunctionProperty18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench102_FunctionProperty__systemworkbench102_FunctionProperty18", None)
        self.__systemworkbench102_FunctionProperty18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench102_FunctionProperty16"):
                opp_val = getattr(old_value, "systemworkbench102_FunctionProperty16", None)
                if opp_val == self:
                    setattr(old_value, "systemworkbench102_FunctionProperty16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench102_FunctionProperty16"):
                opp_val = getattr(value, "systemworkbench102_FunctionProperty16", None)
                setattr(value, "systemworkbench102_FunctionProperty16", self)

    @property
    def systemworkbench102_FunctionProperty(self):
        return self.__systemworkbench102_FunctionProperty

    @systemworkbench102_FunctionProperty.setter
    def systemworkbench102_FunctionProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench102_FunctionProperty__systemworkbench102_FunctionProperty", None)
        self.__systemworkbench102_FunctionProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench102_Workbench6"):
                opp_val = getattr(old_value, "systemworkbench102_Workbench6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench102_Workbench6"):
                opp_val = getattr(value, "systemworkbench102_Workbench6", None)
                if opp_val is None:
                    setattr(value, "systemworkbench102_Workbench6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def systemworkbench102_FunctionProperty31(self):
        return self.__systemworkbench102_FunctionProperty31

    @systemworkbench102_FunctionProperty31.setter
    def systemworkbench102_FunctionProperty31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench102_FunctionProperty__systemworkbench102_FunctionProperty31", None)
        self.__systemworkbench102_FunctionProperty31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench102_Function30"):
                opp_val = getattr(old_value, "systemworkbench102_Function30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench102_Function30"):
                opp_val = getattr(value, "systemworkbench102_Function30", None)
                if opp_val is None:
                    setattr(value, "systemworkbench102_Function30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def systemworkbench102_FunctionProperty16(self):
        return self.__systemworkbench102_FunctionProperty16

    @systemworkbench102_FunctionProperty16.setter
    def systemworkbench102_FunctionProperty16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench102_FunctionProperty__systemworkbench102_FunctionProperty16", None)
        self.__systemworkbench102_FunctionProperty16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench102_FunctionProperty18"):
                opp_val = getattr(old_value, "systemworkbench102_FunctionProperty18", None)
                if opp_val == self:
                    setattr(old_value, "systemworkbench102_FunctionProperty18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench102_FunctionProperty18"):
                opp_val = getattr(value, "systemworkbench102_FunctionProperty18", None)
                setattr(value, "systemworkbench102_FunctionProperty18", self)

class systemworkbench102_Workbench(Named):

    def __init__(self, aprop: str, systemworkbench102_Workbench: set["systemworkbench102_Thing"] = None, systemworkbench102_Workbench4: "systemworkbench102_System" = None, systemworkbench102_Workbench6: set["systemworkbench102_FunctionProperty"] = None, systemworkbench102_Workbench8: set["systemworkbench102_PatternCatalog"] = None, systemworkbench102_Workbench2: set["systemworkbench102_Thoughts"] = None):
        self.aprop = aprop
        self.systemworkbench102_Workbench = systemworkbench102_Workbench if systemworkbench102_Workbench is not None else set()
        self.systemworkbench102_Workbench4 = systemworkbench102_Workbench4
        self.systemworkbench102_Workbench6 = systemworkbench102_Workbench6 if systemworkbench102_Workbench6 is not None else set()
        self.systemworkbench102_Workbench8 = systemworkbench102_Workbench8 if systemworkbench102_Workbench8 is not None else set()
        self.systemworkbench102_Workbench2 = systemworkbench102_Workbench2 if systemworkbench102_Workbench2 is not None else set()
        
    @property
    def aprop(self) -> str:
        return self.__aprop

    @aprop.setter
    def aprop(self, aprop: str):
        self.__aprop = aprop

    @property
    def systemworkbench102_Workbench2(self):
        return self.__systemworkbench102_Workbench2

    @systemworkbench102_Workbench2.setter
    def systemworkbench102_Workbench2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench102_Workbench__systemworkbench102_Workbench2", None)
        self.__systemworkbench102_Workbench2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "systemworkbench102_Thoughts"):
                    opp_val = getattr(item, "systemworkbench102_Thoughts", None)
                    
                    if opp_val == self:
                        setattr(item, "systemworkbench102_Thoughts", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "systemworkbench102_Thoughts"):
                    opp_val = getattr(item, "systemworkbench102_Thoughts", None)
                    
                    setattr(item, "systemworkbench102_Thoughts", self)
                    

    @property
    def systemworkbench102_Workbench8(self):
        return self.__systemworkbench102_Workbench8

    @systemworkbench102_Workbench8.setter
    def systemworkbench102_Workbench8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench102_Workbench__systemworkbench102_Workbench8", None)
        self.__systemworkbench102_Workbench8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "systemworkbench102_PatternCatalog"):
                    opp_val = getattr(item, "systemworkbench102_PatternCatalog", None)
                    
                    if opp_val == self:
                        setattr(item, "systemworkbench102_PatternCatalog", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "systemworkbench102_PatternCatalog"):
                    opp_val = getattr(item, "systemworkbench102_PatternCatalog", None)
                    
                    setattr(item, "systemworkbench102_PatternCatalog", self)
                    

    @property
    def systemworkbench102_Workbench4(self):
        return self.__systemworkbench102_Workbench4

    @systemworkbench102_Workbench4.setter
    def systemworkbench102_Workbench4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench102_Workbench__systemworkbench102_Workbench4", None)
        self.__systemworkbench102_Workbench4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench102_System"):
                opp_val = getattr(old_value, "systemworkbench102_System", None)
                if opp_val == self:
                    setattr(old_value, "systemworkbench102_System", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench102_System"):
                opp_val = getattr(value, "systemworkbench102_System", None)
                setattr(value, "systemworkbench102_System", self)

    @property
    def systemworkbench102_Workbench(self):
        return self.__systemworkbench102_Workbench

    @systemworkbench102_Workbench.setter
    def systemworkbench102_Workbench(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench102_Workbench__systemworkbench102_Workbench", None)
        self.__systemworkbench102_Workbench = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "systemworkbench102_Thing"):
                    opp_val = getattr(item, "systemworkbench102_Thing", None)
                    
                    if opp_val == self:
                        setattr(item, "systemworkbench102_Thing", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "systemworkbench102_Thing"):
                    opp_val = getattr(item, "systemworkbench102_Thing", None)
                    
                    setattr(item, "systemworkbench102_Thing", self)
                    

    @property
    def systemworkbench102_Workbench6(self):
        return self.__systemworkbench102_Workbench6

    @systemworkbench102_Workbench6.setter
    def systemworkbench102_Workbench6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench102_Workbench__systemworkbench102_Workbench6", None)
        self.__systemworkbench102_Workbench6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "systemworkbench102_FunctionProperty"):
                    opp_val = getattr(item, "systemworkbench102_FunctionProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "systemworkbench102_FunctionProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "systemworkbench102_FunctionProperty"):
                    opp_val = getattr(item, "systemworkbench102_FunctionProperty", None)
                    
                    setattr(item, "systemworkbench102_FunctionProperty", self)
                    
