from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class systemworkbench101_NamedElement:

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
class systemworkbench101_RelatedTo(NamedElement):

    def __init__(self, since: str, systemworkbench101_RelatedTo39: "systemworkbench101_Thing" = None, systemworkbench101_RelatedTo: "systemworkbench101_Thing" = None, systemworkbench101_RelatedTo43: "systemworkbench101_Thing" = None):
        self.since = since
        self.systemworkbench101_RelatedTo39 = systemworkbench101_RelatedTo39
        self.systemworkbench101_RelatedTo = systemworkbench101_RelatedTo
        self.systemworkbench101_RelatedTo43 = systemworkbench101_RelatedTo43
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def systemworkbench101_RelatedTo43(self):
        return self.__systemworkbench101_RelatedTo43

    @systemworkbench101_RelatedTo43.setter
    def systemworkbench101_RelatedTo43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench101_RelatedTo__systemworkbench101_RelatedTo43", None)
        self.__systemworkbench101_RelatedTo43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench101_Thing42"):
                opp_val = getattr(old_value, "systemworkbench101_Thing42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench101_Thing42"):
                opp_val = getattr(value, "systemworkbench101_Thing42", None)
                if opp_val is None:
                    setattr(value, "systemworkbench101_Thing42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def systemworkbench101_RelatedTo39(self):
        return self.__systemworkbench101_RelatedTo39

    @systemworkbench101_RelatedTo39.setter
    def systemworkbench101_RelatedTo39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench101_RelatedTo__systemworkbench101_RelatedTo39", None)
        self.__systemworkbench101_RelatedTo39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench101_Thing40"):
                opp_val = getattr(old_value, "systemworkbench101_Thing40", None)
                if opp_val == self:
                    setattr(old_value, "systemworkbench101_Thing40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench101_Thing40"):
                opp_val = getattr(value, "systemworkbench101_Thing40", None)
                setattr(value, "systemworkbench101_Thing40", self)

    @property
    def systemworkbench101_RelatedTo(self):
        return self.__systemworkbench101_RelatedTo

    @systemworkbench101_RelatedTo.setter
    def systemworkbench101_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench101_RelatedTo__systemworkbench101_RelatedTo", None)
        self.__systemworkbench101_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench101_Thing37"):
                opp_val = getattr(old_value, "systemworkbench101_Thing37", None)
                if opp_val == self:
                    setattr(old_value, "systemworkbench101_Thing37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench101_Thing37"):
                opp_val = getattr(value, "systemworkbench101_Thing37", None)
                setattr(value, "systemworkbench101_Thing37", self)

class systemworkbench101_Named(ABC):

    def __init__(self, ident: str):
        self.ident = ident
        
    @property
    def ident(self) -> str:
        return self.__ident

    @ident.setter
    def ident(self, ident: str):
        self.__ident = ident

class systemworkbench101_Thoughts(NamedElement):

    pass
class systemworkbench101_Thing(NamedElement):

    def __init__(self, id: int, systemworkbench101_Thing: "systemworkbench101_Workbench" = None, systemworkbench101_Thing40: "systemworkbench101_RelatedTo" = None, systemworkbench101_Thing37: "systemworkbench101_RelatedTo" = None, systemworkbench101_Thing42: set["systemworkbench101_RelatedTo"] = None, systemworkbench101_Thing46: "systemworkbench101_Thoughts" = None):
        self.id = id
        self.systemworkbench101_Thing = systemworkbench101_Thing
        self.systemworkbench101_Thing40 = systemworkbench101_Thing40
        self.systemworkbench101_Thing37 = systemworkbench101_Thing37
        self.systemworkbench101_Thing42 = systemworkbench101_Thing42 if systemworkbench101_Thing42 is not None else set()
        self.systemworkbench101_Thing46 = systemworkbench101_Thing46
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def systemworkbench101_Thing46(self):
        return self.__systemworkbench101_Thing46

    @systemworkbench101_Thing46.setter
    def systemworkbench101_Thing46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench101_Thing__systemworkbench101_Thing46", None)
        self.__systemworkbench101_Thing46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench101_Thoughts45"):
                opp_val = getattr(old_value, "systemworkbench101_Thoughts45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench101_Thoughts45"):
                opp_val = getattr(value, "systemworkbench101_Thoughts45", None)
                if opp_val is None:
                    setattr(value, "systemworkbench101_Thoughts45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def systemworkbench101_Thing40(self):
        return self.__systemworkbench101_Thing40

    @systemworkbench101_Thing40.setter
    def systemworkbench101_Thing40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench101_Thing__systemworkbench101_Thing40", None)
        self.__systemworkbench101_Thing40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench101_RelatedTo39"):
                opp_val = getattr(old_value, "systemworkbench101_RelatedTo39", None)
                if opp_val == self:
                    setattr(old_value, "systemworkbench101_RelatedTo39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench101_RelatedTo39"):
                opp_val = getattr(value, "systemworkbench101_RelatedTo39", None)
                setattr(value, "systemworkbench101_RelatedTo39", self)

    @property
    def systemworkbench101_Thing(self):
        return self.__systemworkbench101_Thing

    @systemworkbench101_Thing.setter
    def systemworkbench101_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench101_Thing__systemworkbench101_Thing", None)
        self.__systemworkbench101_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench101_Workbench10"):
                opp_val = getattr(old_value, "systemworkbench101_Workbench10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench101_Workbench10"):
                opp_val = getattr(value, "systemworkbench101_Workbench10", None)
                if opp_val is None:
                    setattr(value, "systemworkbench101_Workbench10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def systemworkbench101_Thing37(self):
        return self.__systemworkbench101_Thing37

    @systemworkbench101_Thing37.setter
    def systemworkbench101_Thing37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench101_Thing__systemworkbench101_Thing37", None)
        self.__systemworkbench101_Thing37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench101_RelatedTo"):
                opp_val = getattr(old_value, "systemworkbench101_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "systemworkbench101_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench101_RelatedTo"):
                opp_val = getattr(value, "systemworkbench101_RelatedTo", None)
                setattr(value, "systemworkbench101_RelatedTo", self)

    @property
    def systemworkbench101_Thing42(self):
        return self.__systemworkbench101_Thing42

    @systemworkbench101_Thing42.setter
    def systemworkbench101_Thing42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench101_Thing__systemworkbench101_Thing42", None)
        self.__systemworkbench101_Thing42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "systemworkbench101_RelatedTo43"):
                    opp_val = getattr(item, "systemworkbench101_RelatedTo43", None)
                    
                    if opp_val == self:
                        setattr(item, "systemworkbench101_RelatedTo43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "systemworkbench101_RelatedTo43"):
                    opp_val = getattr(item, "systemworkbench101_RelatedTo43", None)
                    
                    setattr(item, "systemworkbench101_RelatedTo43", self)
                    

class systemworkbench101_PatternCatalog:

    def __init__(self, id: int, systemworkbench101_PatternCatalog: "systemworkbench101_Workbench" = None, systemworkbench101_PatternCatalog34: set["systemworkbench101_Function"] = None):
        self.id = id
        self.systemworkbench101_PatternCatalog = systemworkbench101_PatternCatalog
        self.systemworkbench101_PatternCatalog34 = systemworkbench101_PatternCatalog34 if systemworkbench101_PatternCatalog34 is not None else set()
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def systemworkbench101_PatternCatalog(self):
        return self.__systemworkbench101_PatternCatalog

    @systemworkbench101_PatternCatalog.setter
    def systemworkbench101_PatternCatalog(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench101_PatternCatalog__systemworkbench101_PatternCatalog", None)
        self.__systemworkbench101_PatternCatalog = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench101_Workbench8"):
                opp_val = getattr(old_value, "systemworkbench101_Workbench8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench101_Workbench8"):
                opp_val = getattr(value, "systemworkbench101_Workbench8", None)
                if opp_val is None:
                    setattr(value, "systemworkbench101_Workbench8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def systemworkbench101_PatternCatalog34(self):
        return self.__systemworkbench101_PatternCatalog34

    @systemworkbench101_PatternCatalog34.setter
    def systemworkbench101_PatternCatalog34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench101_PatternCatalog__systemworkbench101_PatternCatalog34", None)
        self.__systemworkbench101_PatternCatalog34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "systemworkbench101_Function35"):
                    opp_val = getattr(item, "systemworkbench101_Function35", None)
                    
                    if opp_val == self:
                        setattr(item, "systemworkbench101_Function35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "systemworkbench101_Function35"):
                    opp_val = getattr(item, "systemworkbench101_Function35", None)
                    
                    setattr(item, "systemworkbench101_Function35", self)
                    

class Named:

    pass
class systemworkbench101_System(Named):

    pass
class systemworkbench101_FunctionProperty(Named):

    def __init__(self, description: str, systemworkbench101_FunctionProperty: "systemworkbench101_Workbench" = None, systemworkbench101_FunctionProperty15: "systemworkbench101_FunctionProperty" = None, systemworkbench101_FunctionProperty13: "systemworkbench101_FunctionProperty" = None, systemworkbench101_FunctionProperty21: "systemworkbench101_Function" = None):
        self.description = description
        self.systemworkbench101_FunctionProperty = systemworkbench101_FunctionProperty
        self.systemworkbench101_FunctionProperty15 = systemworkbench101_FunctionProperty15
        self.systemworkbench101_FunctionProperty13 = systemworkbench101_FunctionProperty13
        self.systemworkbench101_FunctionProperty21 = systemworkbench101_FunctionProperty21
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def systemworkbench101_FunctionProperty(self):
        return self.__systemworkbench101_FunctionProperty

    @systemworkbench101_FunctionProperty.setter
    def systemworkbench101_FunctionProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench101_FunctionProperty__systemworkbench101_FunctionProperty", None)
        self.__systemworkbench101_FunctionProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench101_Workbench6"):
                opp_val = getattr(old_value, "systemworkbench101_Workbench6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench101_Workbench6"):
                opp_val = getattr(value, "systemworkbench101_Workbench6", None)
                if opp_val is None:
                    setattr(value, "systemworkbench101_Workbench6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def systemworkbench101_FunctionProperty13(self):
        return self.__systemworkbench101_FunctionProperty13

    @systemworkbench101_FunctionProperty13.setter
    def systemworkbench101_FunctionProperty13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench101_FunctionProperty__systemworkbench101_FunctionProperty13", None)
        self.__systemworkbench101_FunctionProperty13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench101_FunctionProperty15"):
                opp_val = getattr(old_value, "systemworkbench101_FunctionProperty15", None)
                if opp_val == self:
                    setattr(old_value, "systemworkbench101_FunctionProperty15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench101_FunctionProperty15"):
                opp_val = getattr(value, "systemworkbench101_FunctionProperty15", None)
                setattr(value, "systemworkbench101_FunctionProperty15", self)

    @property
    def systemworkbench101_FunctionProperty15(self):
        return self.__systemworkbench101_FunctionProperty15

    @systemworkbench101_FunctionProperty15.setter
    def systemworkbench101_FunctionProperty15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench101_FunctionProperty__systemworkbench101_FunctionProperty15", None)
        self.__systemworkbench101_FunctionProperty15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench101_FunctionProperty13"):
                opp_val = getattr(old_value, "systemworkbench101_FunctionProperty13", None)
                if opp_val == self:
                    setattr(old_value, "systemworkbench101_FunctionProperty13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench101_FunctionProperty13"):
                opp_val = getattr(value, "systemworkbench101_FunctionProperty13", None)
                setattr(value, "systemworkbench101_FunctionProperty13", self)

    @property
    def systemworkbench101_FunctionProperty21(self):
        return self.__systemworkbench101_FunctionProperty21

    @systemworkbench101_FunctionProperty21.setter
    def systemworkbench101_FunctionProperty21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench101_FunctionProperty__systemworkbench101_FunctionProperty21", None)
        self.__systemworkbench101_FunctionProperty21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench101_Function20"):
                opp_val = getattr(old_value, "systemworkbench101_Function20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench101_Function20"):
                opp_val = getattr(value, "systemworkbench101_Function20", None)
                if opp_val is None:
                    setattr(value, "systemworkbench101_Function20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class systemworkbench101_Workbench(Named):

    def __init__(self, foobar: str, systemworkbench101_Workbench: "systemworkbench101_System" = None, systemworkbench101_Workbench6: set["systemworkbench101_FunctionProperty"] = None, systemworkbench101_Workbench8: set["systemworkbench101_PatternCatalog"] = None, systemworkbench101_Workbench10: set["systemworkbench101_Thing"] = None, systemworkbench101_Workbench12: set["systemworkbench101_Thoughts"] = None):
        self.foobar = foobar
        self.systemworkbench101_Workbench = systemworkbench101_Workbench
        self.systemworkbench101_Workbench6 = systemworkbench101_Workbench6 if systemworkbench101_Workbench6 is not None else set()
        self.systemworkbench101_Workbench8 = systemworkbench101_Workbench8 if systemworkbench101_Workbench8 is not None else set()
        self.systemworkbench101_Workbench10 = systemworkbench101_Workbench10 if systemworkbench101_Workbench10 is not None else set()
        self.systemworkbench101_Workbench12 = systemworkbench101_Workbench12 if systemworkbench101_Workbench12 is not None else set()
        
    @property
    def foobar(self) -> str:
        return self.__foobar

    @foobar.setter
    def foobar(self, foobar: str):
        self.__foobar = foobar

    @property
    def systemworkbench101_Workbench12(self):
        return self.__systemworkbench101_Workbench12

    @systemworkbench101_Workbench12.setter
    def systemworkbench101_Workbench12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench101_Workbench__systemworkbench101_Workbench12", None)
        self.__systemworkbench101_Workbench12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "systemworkbench101_Thoughts"):
                    opp_val = getattr(item, "systemworkbench101_Thoughts", None)
                    
                    if opp_val == self:
                        setattr(item, "systemworkbench101_Thoughts", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "systemworkbench101_Thoughts"):
                    opp_val = getattr(item, "systemworkbench101_Thoughts", None)
                    
                    setattr(item, "systemworkbench101_Thoughts", self)
                    

    @property
    def systemworkbench101_Workbench10(self):
        return self.__systemworkbench101_Workbench10

    @systemworkbench101_Workbench10.setter
    def systemworkbench101_Workbench10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench101_Workbench__systemworkbench101_Workbench10", None)
        self.__systemworkbench101_Workbench10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "systemworkbench101_Thing"):
                    opp_val = getattr(item, "systemworkbench101_Thing", None)
                    
                    if opp_val == self:
                        setattr(item, "systemworkbench101_Thing", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "systemworkbench101_Thing"):
                    opp_val = getattr(item, "systemworkbench101_Thing", None)
                    
                    setattr(item, "systemworkbench101_Thing", self)
                    

    @property
    def systemworkbench101_Workbench8(self):
        return self.__systemworkbench101_Workbench8

    @systemworkbench101_Workbench8.setter
    def systemworkbench101_Workbench8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench101_Workbench__systemworkbench101_Workbench8", None)
        self.__systemworkbench101_Workbench8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "systemworkbench101_PatternCatalog"):
                    opp_val = getattr(item, "systemworkbench101_PatternCatalog", None)
                    
                    if opp_val == self:
                        setattr(item, "systemworkbench101_PatternCatalog", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "systemworkbench101_PatternCatalog"):
                    opp_val = getattr(item, "systemworkbench101_PatternCatalog", None)
                    
                    setattr(item, "systemworkbench101_PatternCatalog", self)
                    

    @property
    def systemworkbench101_Workbench(self):
        return self.__systemworkbench101_Workbench

    @systemworkbench101_Workbench.setter
    def systemworkbench101_Workbench(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench101_Workbench__systemworkbench101_Workbench", None)
        self.__systemworkbench101_Workbench = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemworkbench101_System4"):
                opp_val = getattr(old_value, "systemworkbench101_System4", None)
                if opp_val == self:
                    setattr(old_value, "systemworkbench101_System4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemworkbench101_System4"):
                opp_val = getattr(value, "systemworkbench101_System4", None)
                setattr(value, "systemworkbench101_System4", self)

    @property
    def systemworkbench101_Workbench6(self):
        return self.__systemworkbench101_Workbench6

    @systemworkbench101_Workbench6.setter
    def systemworkbench101_Workbench6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemworkbench101_Workbench__systemworkbench101_Workbench6", None)
        self.__systemworkbench101_Workbench6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "systemworkbench101_FunctionProperty"):
                    opp_val = getattr(item, "systemworkbench101_FunctionProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "systemworkbench101_FunctionProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "systemworkbench101_FunctionProperty"):
                    opp_val = getattr(item, "systemworkbench101_FunctionProperty", None)
                    
                    setattr(item, "systemworkbench101_FunctionProperty", self)
                    

class systemworkbench101_Component(Named):

    pass
class systemworkbench101_Function(Named):

    pass