from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AccessModifier(Enum):
    default = "default"
    private = "private"
    protected = "protected"
    public = "public"


############################################
# Definition of Classes
############################################

class Classifier:

    pass
class classDiagram_Type(Classifier):

    pass
class classDiagram_Class(Classifier):

    def __init__(self, isAbstract: bool, isStatic: bool, accessModifier: str, classDiagram_Class: set["classDiagram_Attribute"] = None, Class: "classDiagram_Class" = None, subtypes: set["classDiagram_Class"] = None, Class8: "classDiagram_Class" = None, supertypes: set["classDiagram_Class"] = None, classDiagram_Class10: set["classDiagram_Function"] = None):
        self.isAbstract = isAbstract
        self.isStatic = isStatic
        self.accessModifier = accessModifier
        self.classDiagram_Class = classDiagram_Class if classDiagram_Class is not None else set()
        self.Class = Class
        self.subtypes = subtypes if subtypes is not None else set()
        self.Class8 = Class8
        self.supertypes = supertypes if supertypes is not None else set()
        self.classDiagram_Class10 = classDiagram_Class10 if classDiagram_Class10 is not None else set()
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def accessModifier(self) -> str:
        return self.__accessModifier

    @accessModifier.setter
    def accessModifier(self, accessModifier: str):
        self.__accessModifier = accessModifier

    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subtypes"):
                opp_val = getattr(old_value, "subtypes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subtypes"):
                opp_val = getattr(value, "subtypes", None)
                if opp_val is None:
                    setattr(value, "subtypes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def subtypes(self):
        return self.__subtypes

    @subtypes.setter
    def subtypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_Class__subtypes", None)
        self.__subtypes = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Class"):
                    opp_val = getattr(item, "Class", None)
                    
                    if opp_val == self:
                        setattr(item, "Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Class"):
                    opp_val = getattr(item, "Class", None)
                    
                    setattr(item, "Class", self)
                    

    @property
    def classDiagram_Class10(self):
        return self.__classDiagram_Class10

    @classDiagram_Class10.setter
    def classDiagram_Class10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_Class__classDiagram_Class10", None)
        self.__classDiagram_Class10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classDiagram_Function"):
                    opp_val = getattr(item, "classDiagram_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "classDiagram_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classDiagram_Function"):
                    opp_val = getattr(item, "classDiagram_Function", None)
                    
                    setattr(item, "classDiagram_Function", self)
                    

    @property
    def classDiagram_Class(self):
        return self.__classDiagram_Class

    @classDiagram_Class.setter
    def classDiagram_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_Class__classDiagram_Class", None)
        self.__classDiagram_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classDiagram_Attribute"):
                    opp_val = getattr(item, "classDiagram_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "classDiagram_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classDiagram_Attribute"):
                    opp_val = getattr(item, "classDiagram_Attribute", None)
                    
                    setattr(item, "classDiagram_Attribute", self)
                    

    @property
    def Class8(self):
        return self.__Class8

    @Class8.setter
    def Class8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_Class__Class8", None)
        self.__Class8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "supertypes"):
                opp_val = getattr(old_value, "supertypes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "supertypes"):
                opp_val = getattr(value, "supertypes", None)
                if opp_val is None:
                    setattr(value, "supertypes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def supertypes(self):
        return self.__supertypes

    @supertypes.setter
    def supertypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_Class__supertypes", None)
        self.__supertypes = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Class8"):
                    opp_val = getattr(item, "Class8", None)
                    
                    if opp_val == self:
                        setattr(item, "Class8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Class8"):
                    opp_val = getattr(item, "Class8", None)
                    
                    setattr(item, "Class8", self)
                    

class ModelingConcept:

    pass
class classDiagram_Classifier(ModelingConcept):

    pass
class classDiagram_Function(ModelingConcept):

    def __init__(self, isAbstract: bool, body: str, accessModifier: str, isStatic: bool, classDiagram_Function: "classDiagram_Class" = None, classDiagram_Function14: "classDiagram_Classifier" = None, classDiagram_Function17: set["classDiagram_Attribute"] = None):
        self.isAbstract = isAbstract
        self.body = body
        self.accessModifier = accessModifier
        self.isStatic = isStatic
        self.classDiagram_Function = classDiagram_Function
        self.classDiagram_Function14 = classDiagram_Function14
        self.classDiagram_Function17 = classDiagram_Function17 if classDiagram_Function17 is not None else set()
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def accessModifier(self) -> str:
        return self.__accessModifier

    @accessModifier.setter
    def accessModifier(self, accessModifier: str):
        self.__accessModifier = accessModifier

    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def classDiagram_Function14(self):
        return self.__classDiagram_Function14

    @classDiagram_Function14.setter
    def classDiagram_Function14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_Function__classDiagram_Function14", None)
        self.__classDiagram_Function14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classDiagram_Classifier15"):
                opp_val = getattr(old_value, "classDiagram_Classifier15", None)
                if opp_val == self:
                    setattr(old_value, "classDiagram_Classifier15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classDiagram_Classifier15"):
                opp_val = getattr(value, "classDiagram_Classifier15", None)
                setattr(value, "classDiagram_Classifier15", self)

    @property
    def classDiagram_Function(self):
        return self.__classDiagram_Function

    @classDiagram_Function.setter
    def classDiagram_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_Function__classDiagram_Function", None)
        self.__classDiagram_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classDiagram_Class10"):
                opp_val = getattr(old_value, "classDiagram_Class10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classDiagram_Class10"):
                opp_val = getattr(value, "classDiagram_Class10", None)
                if opp_val is None:
                    setattr(value, "classDiagram_Class10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classDiagram_Function17(self):
        return self.__classDiagram_Function17

    @classDiagram_Function17.setter
    def classDiagram_Function17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_Function__classDiagram_Function17", None)
        self.__classDiagram_Function17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classDiagram_Attribute18"):
                    opp_val = getattr(item, "classDiagram_Attribute18", None)
                    
                    if opp_val == self:
                        setattr(item, "classDiagram_Attribute18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classDiagram_Attribute18"):
                    opp_val = getattr(item, "classDiagram_Attribute18", None)
                    
                    setattr(item, "classDiagram_Attribute18", self)
                    

class classDiagram_Attribute(ModelingConcept):

    def __init__(self, isStatic: bool, accessModifier: str, classDiagram_Attribute: "classDiagram_Class" = None, classDiagram_Attribute12: "classDiagram_Classifier" = None, classDiagram_Attribute18: "classDiagram_Function" = None):
        self.isStatic = isStatic
        self.accessModifier = accessModifier
        self.classDiagram_Attribute = classDiagram_Attribute
        self.classDiagram_Attribute12 = classDiagram_Attribute12
        self.classDiagram_Attribute18 = classDiagram_Attribute18
        
    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def accessModifier(self) -> str:
        return self.__accessModifier

    @accessModifier.setter
    def accessModifier(self, accessModifier: str):
        self.__accessModifier = accessModifier

    @property
    def classDiagram_Attribute(self):
        return self.__classDiagram_Attribute

    @classDiagram_Attribute.setter
    def classDiagram_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_Attribute__classDiagram_Attribute", None)
        self.__classDiagram_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classDiagram_Class"):
                opp_val = getattr(old_value, "classDiagram_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classDiagram_Class"):
                opp_val = getattr(value, "classDiagram_Class", None)
                if opp_val is None:
                    setattr(value, "classDiagram_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classDiagram_Attribute12(self):
        return self.__classDiagram_Attribute12

    @classDiagram_Attribute12.setter
    def classDiagram_Attribute12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_Attribute__classDiagram_Attribute12", None)
        self.__classDiagram_Attribute12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classDiagram_Classifier"):
                opp_val = getattr(old_value, "classDiagram_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "classDiagram_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classDiagram_Classifier"):
                opp_val = getattr(value, "classDiagram_Classifier", None)
                setattr(value, "classDiagram_Classifier", self)

    @property
    def classDiagram_Attribute18(self):
        return self.__classDiagram_Attribute18

    @classDiagram_Attribute18.setter
    def classDiagram_Attribute18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_Attribute__classDiagram_Attribute18", None)
        self.__classDiagram_Attribute18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classDiagram_Function17"):
                opp_val = getattr(old_value, "classDiagram_Function17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classDiagram_Function17"):
                opp_val = getattr(value, "classDiagram_Function17", None)
                if opp_val is None:
                    setattr(value, "classDiagram_Function17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class classDiagram_ModelingConcept(ABC):

    def __init__(self, name: str, classDiagram_ModelingConcept: "classDiagram_Package" = None):
        self.name = name
        self.classDiagram_ModelingConcept = classDiagram_ModelingConcept
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classDiagram_ModelingConcept(self):
        return self.__classDiagram_ModelingConcept

    @classDiagram_ModelingConcept.setter
    def classDiagram_ModelingConcept(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_ModelingConcept__classDiagram_ModelingConcept", None)
        self.__classDiagram_ModelingConcept = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classDiagram_Package2"):
                opp_val = getattr(old_value, "classDiagram_Package2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classDiagram_Package2"):
                opp_val = getattr(value, "classDiagram_Package2", None)
                if opp_val is None:
                    setattr(value, "classDiagram_Package2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class classDiagram_Package(ModelingConcept):

    pass
class classDiagram_ClassModel:

    pass