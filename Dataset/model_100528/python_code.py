from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class useCase_Uses:

    def __init__(self, name: str, multiplicity: str, useCase_Uses: "useCase_Actor" = None):
        self.name = name
        self.multiplicity = multiplicity
        self.useCase_Uses = useCase_Uses
        
        pass
    @property
    def multiplicity(self):
        return self.__multiplicity

    @multiplicity.setter
    def multiplicity(self, multiplicity: str):
        self.__multiplicity = multiplicity


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def useCase_Uses(self):
        return self.__useCase_Uses

    @useCase_Uses.setter
    def useCase_Uses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCase_Uses__useCase_Uses", None)
        self.__useCase_Uses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCase_Actor14"):
                opp_val = getattr(old_value, "useCase_Actor14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCase_Actor14"):
                opp_val = getattr(value, "useCase_Actor14", None)
                if opp_val is None:
                    setattr(value, "useCase_Actor14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class useCase_Inheritance:

    def __init__(self, name: str, useCase_Inheritance: "useCase_Actor" = None):
        self.name = name
        self.useCase_Inheritance = useCase_Inheritance
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def useCase_Inheritance(self):
        return self.__useCase_Inheritance

    @useCase_Inheritance.setter
    def useCase_Inheritance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCase_Inheritance__useCase_Inheritance", None)
        self.__useCase_Inheritance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCase_Actor12"):
                opp_val = getattr(old_value, "useCase_Actor12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCase_Actor12"):
                opp_val = getattr(value, "useCase_Actor12", None)
                if opp_val is None:
                    setattr(value, "useCase_Actor12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class useCase_ExtensionPoint:

    def __init__(self, name: str, useCase_ExtensionPoint: "useCase_Case" = None):
        self.name = name
        self.useCase_ExtensionPoint = useCase_ExtensionPoint
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def useCase_ExtensionPoint(self):
        return self.__useCase_ExtensionPoint

    @useCase_ExtensionPoint.setter
    def useCase_ExtensionPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCase_ExtensionPoint__useCase_ExtensionPoint", None)
        self.__useCase_ExtensionPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCase_Case6"):
                opp_val = getattr(old_value, "useCase_Case6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCase_Case6"):
                opp_val = getattr(value, "useCase_Case6", None)
                if opp_val is None:
                    setattr(value, "useCase_Case6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class useCase_Case:

    def __init__(self, name: str, useCase_Case8: set["useCase_Includes"] = None, useCase_Case10: set["useCase_Extends"] = None, useCase_Case: "useCase_Subsystem" = None, useCase_Case6: set["useCase_ExtensionPoint"] = None):
        self.name = name
        self.useCase_Case8 = useCase_Case8 if useCase_Case8 is not None else set()
        self.useCase_Case10 = useCase_Case10 if useCase_Case10 is not None else set()
        self.useCase_Case = useCase_Case
        self.useCase_Case6 = useCase_Case6 if useCase_Case6 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def useCase_Case6(self):
        return self.__useCase_Case6

    @useCase_Case6.setter
    def useCase_Case6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCase_Case__useCase_Case6", None)
        self.__useCase_Case6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "useCase_ExtensionPoint"):
                    opp_val = getattr(item, "useCase_ExtensionPoint", None)
                    
                    if opp_val == self:
                        setattr(item, "useCase_ExtensionPoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "useCase_ExtensionPoint"):
                    opp_val = getattr(item, "useCase_ExtensionPoint", None)
                    
                    setattr(item, "useCase_ExtensionPoint", self)
                    

    @property
    def useCase_Case(self):
        return self.__useCase_Case

    @useCase_Case.setter
    def useCase_Case(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCase_Case__useCase_Case", None)
        self.__useCase_Case = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCase_Subsystem4"):
                opp_val = getattr(old_value, "useCase_Subsystem4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCase_Subsystem4"):
                opp_val = getattr(value, "useCase_Subsystem4", None)
                if opp_val is None:
                    setattr(value, "useCase_Subsystem4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def useCase_Case10(self):
        return self.__useCase_Case10

    @useCase_Case10.setter
    def useCase_Case10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCase_Case__useCase_Case10", None)
        self.__useCase_Case10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "useCase_Extends"):
                    opp_val = getattr(item, "useCase_Extends", None)
                    
                    if opp_val == self:
                        setattr(item, "useCase_Extends", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "useCase_Extends"):
                    opp_val = getattr(item, "useCase_Extends", None)
                    
                    setattr(item, "useCase_Extends", self)
                    

    @property
    def useCase_Case8(self):
        return self.__useCase_Case8

    @useCase_Case8.setter
    def useCase_Case8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCase_Case__useCase_Case8", None)
        self.__useCase_Case8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "useCase_Includes"):
                    opp_val = getattr(item, "useCase_Includes", None)
                    
                    if opp_val == self:
                        setattr(item, "useCase_Includes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "useCase_Includes"):
                    opp_val = getattr(item, "useCase_Includes", None)
                    
                    setattr(item, "useCase_Includes", self)
                    

class useCase_Actor:

    def __init__(self, name: str, useCase_Actor: "useCase_UseCase" = None, useCase_Actor12: set["useCase_Inheritance"] = None, useCase_Actor14: set["useCase_Uses"] = None):
        self.name = name
        self.useCase_Actor = useCase_Actor
        self.useCase_Actor12 = useCase_Actor12 if useCase_Actor12 is not None else set()
        self.useCase_Actor14 = useCase_Actor14 if useCase_Actor14 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def useCase_Actor14(self):
        return self.__useCase_Actor14

    @useCase_Actor14.setter
    def useCase_Actor14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCase_Actor__useCase_Actor14", None)
        self.__useCase_Actor14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "useCase_Uses"):
                    opp_val = getattr(item, "useCase_Uses", None)
                    
                    if opp_val == self:
                        setattr(item, "useCase_Uses", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "useCase_Uses"):
                    opp_val = getattr(item, "useCase_Uses", None)
                    
                    setattr(item, "useCase_Uses", self)
                    

    @property
    def useCase_Actor12(self):
        return self.__useCase_Actor12

    @useCase_Actor12.setter
    def useCase_Actor12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCase_Actor__useCase_Actor12", None)
        self.__useCase_Actor12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "useCase_Inheritance"):
                    opp_val = getattr(item, "useCase_Inheritance", None)
                    
                    if opp_val == self:
                        setattr(item, "useCase_Inheritance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "useCase_Inheritance"):
                    opp_val = getattr(item, "useCase_Inheritance", None)
                    
                    setattr(item, "useCase_Inheritance", self)
                    

    @property
    def useCase_Actor(self):
        return self.__useCase_Actor

    @useCase_Actor.setter
    def useCase_Actor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCase_Actor__useCase_Actor", None)
        self.__useCase_Actor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCase_UseCase2"):
                opp_val = getattr(old_value, "useCase_UseCase2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCase_UseCase2"):
                opp_val = getattr(value, "useCase_UseCase2", None)
                if opp_val is None:
                    setattr(value, "useCase_UseCase2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class useCase_Subsystem:

    def __init__(self, name: str, useCase_Subsystem: "useCase_UseCase" = None, useCase_Subsystem4: set["useCase_Case"] = None):
        self.name = name
        self.useCase_Subsystem = useCase_Subsystem
        self.useCase_Subsystem4 = useCase_Subsystem4 if useCase_Subsystem4 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def useCase_Subsystem4(self):
        return self.__useCase_Subsystem4

    @useCase_Subsystem4.setter
    def useCase_Subsystem4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCase_Subsystem__useCase_Subsystem4", None)
        self.__useCase_Subsystem4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "useCase_Case"):
                    opp_val = getattr(item, "useCase_Case", None)
                    
                    if opp_val == self:
                        setattr(item, "useCase_Case", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "useCase_Case"):
                    opp_val = getattr(item, "useCase_Case", None)
                    
                    setattr(item, "useCase_Case", self)
                    

    @property
    def useCase_Subsystem(self):
        return self.__useCase_Subsystem

    @useCase_Subsystem.setter
    def useCase_Subsystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCase_Subsystem__useCase_Subsystem", None)
        self.__useCase_Subsystem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCase_UseCase"):
                opp_val = getattr(old_value, "useCase_UseCase", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCase_UseCase"):
                opp_val = getattr(value, "useCase_UseCase", None)
                if opp_val is None:
                    setattr(value, "useCase_UseCase", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class useCase_UseCase:

    pass
class useCase_Extends:

    def __init__(self, name: str, rules: str, useCase_Extends: "useCase_Case" = None):
        self.name = name
        self.rules = rules
        self.useCase_Extends = useCase_Extends
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def rules(self):
        return self.__rules

    @rules.setter
    def rules(self, rules: str):
        self.__rules = rules


    @property
    def useCase_Extends(self):
        return self.__useCase_Extends

    @useCase_Extends.setter
    def useCase_Extends(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCase_Extends__useCase_Extends", None)
        self.__useCase_Extends = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCase_Case10"):
                opp_val = getattr(old_value, "useCase_Case10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCase_Case10"):
                opp_val = getattr(value, "useCase_Case10", None)
                if opp_val is None:
                    setattr(value, "useCase_Case10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class useCase_Includes:

    def __init__(self, name: str, rules: str, useCase_Includes: "useCase_Case" = None):
        self.name = name
        self.rules = rules
        self.useCase_Includes = useCase_Includes
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def rules(self):
        return self.__rules

    @rules.setter
    def rules(self, rules: str):
        self.__rules = rules


    @property
    def useCase_Includes(self):
        return self.__useCase_Includes

    @useCase_Includes.setter
    def useCase_Includes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_useCase_Includes__useCase_Includes", None)
        self.__useCase_Includes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCase_Case8"):
                opp_val = getattr(old_value, "useCase_Case8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCase_Case8"):
                opp_val = getattr(value, "useCase_Case8", None)
                if opp_val is None:
                    setattr(value, "useCase_Case8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
