from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Feature:

    pass
class simple_OO_concept_Feature(ABC):

    def __init__(self, isPublic: bool, isProtected: bool, isPrivate: bool):
        self.isPublic = isPublic
        self.isProtected = isProtected
        self.isPrivate = isPrivate
        
    @property
    def isPublic(self) -> bool:
        return self.__isPublic

    @isPublic.setter
    def isPublic(self, isPublic: bool):
        self.__isPublic = isPublic

    @property
    def isProtected(self) -> bool:
        return self.__isProtected

    @isProtected.setter
    def isProtected(self, isProtected: bool):
        self.__isProtected = isProtected

    @property
    def isPrivate(self) -> bool:
        return self.__isPrivate

    @isPrivate.setter
    def isPrivate(self, isPrivate: bool):
        self.__isPrivate = isPrivate

class Class:

    pass
class simple_OO_concept_Behavior(Class):

    pass
class simple_OO_concept_Parameter:

    pass
class simple_OO_concept_NamedElement(ABC):

    def __init__(self, name: str, simple_OO_concept_NamedElement: "simple_OO_concept_Dependency" = None, simple_OO_concept_NamedElement7: "simple_OO_concept_Dependency" = None):
        self.name = name
        self.simple_OO_concept_NamedElement = simple_OO_concept_NamedElement
        self.simple_OO_concept_NamedElement7 = simple_OO_concept_NamedElement7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simple_OO_concept_NamedElement7(self):
        return self.__simple_OO_concept_NamedElement7

    @simple_OO_concept_NamedElement7.setter
    def simple_OO_concept_NamedElement7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple_OO_concept_NamedElement__simple_OO_concept_NamedElement7", None)
        self.__simple_OO_concept_NamedElement7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simple_OO_concept_Dependency6"):
                opp_val = getattr(old_value, "simple_OO_concept_Dependency6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simple_OO_concept_Dependency6"):
                opp_val = getattr(value, "simple_OO_concept_Dependency6", None)
                if opp_val is None:
                    setattr(value, "simple_OO_concept_Dependency6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simple_OO_concept_NamedElement(self):
        return self.__simple_OO_concept_NamedElement

    @simple_OO_concept_NamedElement.setter
    def simple_OO_concept_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple_OO_concept_NamedElement__simple_OO_concept_NamedElement", None)
        self.__simple_OO_concept_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simple_OO_concept_Dependency4"):
                opp_val = getattr(old_value, "simple_OO_concept_Dependency4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simple_OO_concept_Dependency4"):
                opp_val = getattr(value, "simple_OO_concept_Dependency4", None)
                if opp_val is None:
                    setattr(value, "simple_OO_concept_Dependency4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simple_OO_concept_Dependency:

    pass
class NamedElement:

    pass
class simple_OO_concept_Attribute(Feature, NamedElement):

    pass
class simple_OO_concept_Operation(Feature, NamedElement):

    pass
class simple_OO_concept_Class(NamedElement):

    def __init__(self, isAbstract: bool, simple_OO_concept_Class: "simple_OO_concept_Package" = None, simple_OO_concept_Class24: "simple_OO_concept_Parameter" = None, simple_OO_concept_Class9: set["simple_OO_concept_Attribute"] = None, simple_OO_concept_Class11: set["simple_OO_concept_Operation"] = None, simple_OO_concept_Class14: "simple_OO_concept_Class" = None, simple_OO_concept_Class12: set["simple_OO_concept_Class"] = None, simple_OO_concept_Class17: "simple_OO_concept_Attribute" = None):
        self.isAbstract = isAbstract
        self.simple_OO_concept_Class = simple_OO_concept_Class
        self.simple_OO_concept_Class24 = simple_OO_concept_Class24
        self.simple_OO_concept_Class9 = simple_OO_concept_Class9 if simple_OO_concept_Class9 is not None else set()
        self.simple_OO_concept_Class11 = simple_OO_concept_Class11 if simple_OO_concept_Class11 is not None else set()
        self.simple_OO_concept_Class14 = simple_OO_concept_Class14
        self.simple_OO_concept_Class12 = simple_OO_concept_Class12 if simple_OO_concept_Class12 is not None else set()
        self.simple_OO_concept_Class17 = simple_OO_concept_Class17
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def simple_OO_concept_Class24(self):
        return self.__simple_OO_concept_Class24

    @simple_OO_concept_Class24.setter
    def simple_OO_concept_Class24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple_OO_concept_Class__simple_OO_concept_Class24", None)
        self.__simple_OO_concept_Class24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simple_OO_concept_Parameter23"):
                opp_val = getattr(old_value, "simple_OO_concept_Parameter23", None)
                if opp_val == self:
                    setattr(old_value, "simple_OO_concept_Parameter23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simple_OO_concept_Parameter23"):
                opp_val = getattr(value, "simple_OO_concept_Parameter23", None)
                setattr(value, "simple_OO_concept_Parameter23", self)

    @property
    def simple_OO_concept_Class17(self):
        return self.__simple_OO_concept_Class17

    @simple_OO_concept_Class17.setter
    def simple_OO_concept_Class17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple_OO_concept_Class__simple_OO_concept_Class17", None)
        self.__simple_OO_concept_Class17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simple_OO_concept_Attribute16"):
                opp_val = getattr(old_value, "simple_OO_concept_Attribute16", None)
                if opp_val == self:
                    setattr(old_value, "simple_OO_concept_Attribute16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simple_OO_concept_Attribute16"):
                opp_val = getattr(value, "simple_OO_concept_Attribute16", None)
                setattr(value, "simple_OO_concept_Attribute16", self)

    @property
    def simple_OO_concept_Class(self):
        return self.__simple_OO_concept_Class

    @simple_OO_concept_Class.setter
    def simple_OO_concept_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple_OO_concept_Class__simple_OO_concept_Class", None)
        self.__simple_OO_concept_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simple_OO_concept_Package"):
                opp_val = getattr(old_value, "simple_OO_concept_Package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simple_OO_concept_Package"):
                opp_val = getattr(value, "simple_OO_concept_Package", None)
                if opp_val is None:
                    setattr(value, "simple_OO_concept_Package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simple_OO_concept_Class12(self):
        return self.__simple_OO_concept_Class12

    @simple_OO_concept_Class12.setter
    def simple_OO_concept_Class12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple_OO_concept_Class__simple_OO_concept_Class12", None)
        self.__simple_OO_concept_Class12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simple_OO_concept_Class14"):
                    opp_val = getattr(item, "simple_OO_concept_Class14", None)
                    
                    if opp_val == self:
                        setattr(item, "simple_OO_concept_Class14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simple_OO_concept_Class14"):
                    opp_val = getattr(item, "simple_OO_concept_Class14", None)
                    
                    setattr(item, "simple_OO_concept_Class14", self)
                    

    @property
    def simple_OO_concept_Class9(self):
        return self.__simple_OO_concept_Class9

    @simple_OO_concept_Class9.setter
    def simple_OO_concept_Class9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple_OO_concept_Class__simple_OO_concept_Class9", None)
        self.__simple_OO_concept_Class9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simple_OO_concept_Attribute"):
                    opp_val = getattr(item, "simple_OO_concept_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "simple_OO_concept_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simple_OO_concept_Attribute"):
                    opp_val = getattr(item, "simple_OO_concept_Attribute", None)
                    
                    setattr(item, "simple_OO_concept_Attribute", self)
                    

    @property
    def simple_OO_concept_Class11(self):
        return self.__simple_OO_concept_Class11

    @simple_OO_concept_Class11.setter
    def simple_OO_concept_Class11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple_OO_concept_Class__simple_OO_concept_Class11", None)
        self.__simple_OO_concept_Class11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simple_OO_concept_Operation"):
                    opp_val = getattr(item, "simple_OO_concept_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "simple_OO_concept_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simple_OO_concept_Operation"):
                    opp_val = getattr(item, "simple_OO_concept_Operation", None)
                    
                    setattr(item, "simple_OO_concept_Operation", self)
                    

    @property
    def simple_OO_concept_Class14(self):
        return self.__simple_OO_concept_Class14

    @simple_OO_concept_Class14.setter
    def simple_OO_concept_Class14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple_OO_concept_Class__simple_OO_concept_Class14", None)
        self.__simple_OO_concept_Class14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simple_OO_concept_Class12"):
                opp_val = getattr(old_value, "simple_OO_concept_Class12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simple_OO_concept_Class12"):
                opp_val = getattr(value, "simple_OO_concept_Class12", None)
                if opp_val is None:
                    setattr(value, "simple_OO_concept_Class12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simple_OO_concept_Package(NamedElement):

    pass