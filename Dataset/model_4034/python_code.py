from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class simpleClass_Class(NamedElement):

    def __init__(self, persistent: bool, simpleClass_Class9: set["simpleClass_Attribute"] = None, simpleClass_Class12: "simpleClass_Class" = None, simpleClass_Class10: set["simpleClass_Class"] = None, simpleClass_Class15: "simpleClass_Association" = None, simpleClass_Class18: "simpleClass_Association" = None, simpleClass_Class: "simpleClass_Package" = None):
        self.persistent = persistent
        self.simpleClass_Class9 = simpleClass_Class9 if simpleClass_Class9 is not None else set()
        self.simpleClass_Class12 = simpleClass_Class12
        self.simpleClass_Class10 = simpleClass_Class10 if simpleClass_Class10 is not None else set()
        self.simpleClass_Class15 = simpleClass_Class15
        self.simpleClass_Class18 = simpleClass_Class18
        self.simpleClass_Class = simpleClass_Class
        
    @property
    def persistent(self) -> bool:
        return self.__persistent

    @persistent.setter
    def persistent(self, persistent: bool):
        self.__persistent = persistent

    @property
    def simpleClass_Class10(self):
        return self.__simpleClass_Class10

    @simpleClass_Class10.setter
    def simpleClass_Class10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Class__simpleClass_Class10", None)
        self.__simpleClass_Class10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleClass_Class12"):
                    opp_val = getattr(item, "simpleClass_Class12", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleClass_Class12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleClass_Class12"):
                    opp_val = getattr(item, "simpleClass_Class12", None)
                    
                    setattr(item, "simpleClass_Class12", self)
                    

    @property
    def simpleClass_Class9(self):
        return self.__simpleClass_Class9

    @simpleClass_Class9.setter
    def simpleClass_Class9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Class__simpleClass_Class9", None)
        self.__simpleClass_Class9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleClass_Attribute"):
                    opp_val = getattr(item, "simpleClass_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleClass_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleClass_Attribute"):
                    opp_val = getattr(item, "simpleClass_Attribute", None)
                    
                    setattr(item, "simpleClass_Attribute", self)
                    

    @property
    def simpleClass_Class(self):
        return self.__simpleClass_Class

    @simpleClass_Class.setter
    def simpleClass_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Class__simpleClass_Class", None)
        self.__simpleClass_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleClass_Package5"):
                opp_val = getattr(old_value, "simpleClass_Package5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleClass_Package5"):
                opp_val = getattr(value, "simpleClass_Package5", None)
                if opp_val is None:
                    setattr(value, "simpleClass_Package5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleClass_Class18(self):
        return self.__simpleClass_Class18

    @simpleClass_Class18.setter
    def simpleClass_Class18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Class__simpleClass_Class18", None)
        self.__simpleClass_Class18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleClass_Association17"):
                opp_val = getattr(old_value, "simpleClass_Association17", None)
                if opp_val == self:
                    setattr(old_value, "simpleClass_Association17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleClass_Association17"):
                opp_val = getattr(value, "simpleClass_Association17", None)
                setattr(value, "simpleClass_Association17", self)

    @property
    def simpleClass_Class15(self):
        return self.__simpleClass_Class15

    @simpleClass_Class15.setter
    def simpleClass_Class15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Class__simpleClass_Class15", None)
        self.__simpleClass_Class15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleClass_Association14"):
                opp_val = getattr(old_value, "simpleClass_Association14", None)
                if opp_val == self:
                    setattr(old_value, "simpleClass_Association14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleClass_Association14"):
                opp_val = getattr(value, "simpleClass_Association14", None)
                setattr(value, "simpleClass_Association14", self)

    @property
    def simpleClass_Class12(self):
        return self.__simpleClass_Class12

    @simpleClass_Class12.setter
    def simpleClass_Class12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Class__simpleClass_Class12", None)
        self.__simpleClass_Class12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleClass_Class10"):
                opp_val = getattr(old_value, "simpleClass_Class10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleClass_Class10"):
                opp_val = getattr(value, "simpleClass_Class10", None)
                if opp_val is None:
                    setattr(value, "simpleClass_Class10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simpleClass_Package(NamedElement):

    pass
class simpleClass_ClassModel:

    pass
class simpleClass_Attribute(NamedElement):

    pass
class simpleClass_Association(NamedElement):

    pass
class simpleClass_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
