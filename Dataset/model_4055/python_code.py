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

class classDiagram_ElementType:

    def __init__(self, isCollection: bool, classDiagram_ElementType: "classDiagram_Attribute" = None, classDiagram_ElementType25: "classDiagram_Method" = None, classDiagram_ElementType30: "classDiagram_Classifier" = None):
        self.isCollection = isCollection
        self.classDiagram_ElementType = classDiagram_ElementType
        self.classDiagram_ElementType25 = classDiagram_ElementType25
        self.classDiagram_ElementType30 = classDiagram_ElementType30
        
    @property
    def isCollection(self) -> bool:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: bool):
        self.__isCollection = isCollection

    @property
    def classDiagram_ElementType25(self):
        return self.__classDiagram_ElementType25

    @classDiagram_ElementType25.setter
    def classDiagram_ElementType25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_ElementType__classDiagram_ElementType25", None)
        self.__classDiagram_ElementType25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classDiagram_Method24"):
                opp_val = getattr(old_value, "classDiagram_Method24", None)
                if opp_val == self:
                    setattr(old_value, "classDiagram_Method24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classDiagram_Method24"):
                opp_val = getattr(value, "classDiagram_Method24", None)
                setattr(value, "classDiagram_Method24", self)

    @property
    def classDiagram_ElementType(self):
        return self.__classDiagram_ElementType

    @classDiagram_ElementType.setter
    def classDiagram_ElementType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_ElementType__classDiagram_ElementType", None)
        self.__classDiagram_ElementType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classDiagram_Attribute22"):
                opp_val = getattr(old_value, "classDiagram_Attribute22", None)
                if opp_val == self:
                    setattr(old_value, "classDiagram_Attribute22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classDiagram_Attribute22"):
                opp_val = getattr(value, "classDiagram_Attribute22", None)
                setattr(value, "classDiagram_Attribute22", self)

    @property
    def classDiagram_ElementType30(self):
        return self.__classDiagram_ElementType30

    @classDiagram_ElementType30.setter
    def classDiagram_ElementType30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_ElementType__classDiagram_ElementType30", None)
        self.__classDiagram_ElementType30 = value
        
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

class Classifier:

    pass
class classDiagram_Class(Classifier):

    def __init__(self, isStatic: bool, accessModifier: str, isAbstract: bool, classDiagram_Class: "classDiagram_Package" = None, classDiagram_Class20: set["classDiagram_Method"] = None, classDiagram_Class13: set["classDiagram_Attribute"] = None, Class: "classDiagram_Class" = None, subtypes: set["classDiagram_Class"] = None, Class18: "classDiagram_Class" = None, supertypes: set["classDiagram_Class"] = None):
        self.isStatic = isStatic
        self.accessModifier = accessModifier
        self.isAbstract = isAbstract
        self.classDiagram_Class = classDiagram_Class
        self.classDiagram_Class20 = classDiagram_Class20 if classDiagram_Class20 is not None else set()
        self.classDiagram_Class13 = classDiagram_Class13 if classDiagram_Class13 is not None else set()
        self.Class = Class
        self.subtypes = subtypes if subtypes is not None else set()
        self.Class18 = Class18
        self.supertypes = supertypes if supertypes is not None else set()
        
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
    def classDiagram_Class13(self):
        return self.__classDiagram_Class13

    @classDiagram_Class13.setter
    def classDiagram_Class13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_Class__classDiagram_Class13", None)
        self.__classDiagram_Class13 = value if value is not None else set()
        
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
                if hasattr(item, "Class18"):
                    opp_val = getattr(item, "Class18", None)
                    
                    if opp_val == self:
                        setattr(item, "Class18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Class18"):
                    opp_val = getattr(item, "Class18", None)
                    
                    setattr(item, "Class18", self)
                    

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
    def Class18(self):
        return self.__Class18

    @Class18.setter
    def Class18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_Class__Class18", None)
        self.__Class18 = value
        
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
    def classDiagram_Class(self):
        return self.__classDiagram_Class

    @classDiagram_Class.setter
    def classDiagram_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_Class__classDiagram_Class", None)
        self.__classDiagram_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classDiagram_Package11"):
                opp_val = getattr(old_value, "classDiagram_Package11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classDiagram_Package11"):
                opp_val = getattr(value, "classDiagram_Package11", None)
                if opp_val is None:
                    setattr(value, "classDiagram_Package11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classDiagram_Class20(self):
        return self.__classDiagram_Class20

    @classDiagram_Class20.setter
    def classDiagram_Class20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_Class__classDiagram_Class20", None)
        self.__classDiagram_Class20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classDiagram_Method"):
                    opp_val = getattr(item, "classDiagram_Method", None)
                    
                    if opp_val == self:
                        setattr(item, "classDiagram_Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classDiagram_Method"):
                    opp_val = getattr(item, "classDiagram_Method", None)
                    
                    setattr(item, "classDiagram_Method", self)
                    

class ModelingConcept:

    pass
class classDiagram_Attribute(ModelingConcept):

    def __init__(self, isStatic: bool, accessModifier: str, classDiagram_Attribute22: "classDiagram_ElementType" = None, classDiagram_Attribute28: "classDiagram_Method" = None, classDiagram_Attribute: "classDiagram_Class" = None):
        self.isStatic = isStatic
        self.accessModifier = accessModifier
        self.classDiagram_Attribute22 = classDiagram_Attribute22
        self.classDiagram_Attribute28 = classDiagram_Attribute28
        self.classDiagram_Attribute = classDiagram_Attribute
        
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
    def classDiagram_Attribute22(self):
        return self.__classDiagram_Attribute22

    @classDiagram_Attribute22.setter
    def classDiagram_Attribute22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_Attribute__classDiagram_Attribute22", None)
        self.__classDiagram_Attribute22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classDiagram_ElementType"):
                opp_val = getattr(old_value, "classDiagram_ElementType", None)
                if opp_val == self:
                    setattr(old_value, "classDiagram_ElementType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classDiagram_ElementType"):
                opp_val = getattr(value, "classDiagram_ElementType", None)
                setattr(value, "classDiagram_ElementType", self)

    @property
    def classDiagram_Attribute28(self):
        return self.__classDiagram_Attribute28

    @classDiagram_Attribute28.setter
    def classDiagram_Attribute28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_Attribute__classDiagram_Attribute28", None)
        self.__classDiagram_Attribute28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classDiagram_Method27"):
                opp_val = getattr(old_value, "classDiagram_Method27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classDiagram_Method27"):
                opp_val = getattr(value, "classDiagram_Method27", None)
                if opp_val is None:
                    setattr(value, "classDiagram_Method27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "classDiagram_Class13"):
                opp_val = getattr(old_value, "classDiagram_Class13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classDiagram_Class13"):
                opp_val = getattr(value, "classDiagram_Class13", None)
                if opp_val is None:
                    setattr(value, "classDiagram_Class13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class classDiagram_Classifier(ModelingConcept):

    pass
class classDiagram_Method(ModelingConcept):

    def __init__(self, accessModifier: str, isStatic: bool, isAbstract: bool, body: str, classDiagram_Method: "classDiagram_Class" = None, classDiagram_Method24: "classDiagram_ElementType" = None, classDiagram_Method27: set["classDiagram_Attribute"] = None):
        self.accessModifier = accessModifier
        self.isStatic = isStatic
        self.isAbstract = isAbstract
        self.body = body
        self.classDiagram_Method = classDiagram_Method
        self.classDiagram_Method24 = classDiagram_Method24
        self.classDiagram_Method27 = classDiagram_Method27 if classDiagram_Method27 is not None else set()
        
    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

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
    def classDiagram_Method(self):
        return self.__classDiagram_Method

    @classDiagram_Method.setter
    def classDiagram_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_Method__classDiagram_Method", None)
        self.__classDiagram_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classDiagram_Class20"):
                opp_val = getattr(old_value, "classDiagram_Class20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classDiagram_Class20"):
                opp_val = getattr(value, "classDiagram_Class20", None)
                if opp_val is None:
                    setattr(value, "classDiagram_Class20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classDiagram_Method24(self):
        return self.__classDiagram_Method24

    @classDiagram_Method24.setter
    def classDiagram_Method24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_Method__classDiagram_Method24", None)
        self.__classDiagram_Method24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classDiagram_ElementType25"):
                opp_val = getattr(old_value, "classDiagram_ElementType25", None)
                if opp_val == self:
                    setattr(old_value, "classDiagram_ElementType25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classDiagram_ElementType25"):
                opp_val = getattr(value, "classDiagram_ElementType25", None)
                setattr(value, "classDiagram_ElementType25", self)

    @property
    def classDiagram_Method27(self):
        return self.__classDiagram_Method27

    @classDiagram_Method27.setter
    def classDiagram_Method27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_Method__classDiagram_Method27", None)
        self.__classDiagram_Method27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classDiagram_Attribute28"):
                    opp_val = getattr(item, "classDiagram_Attribute28", None)
                    
                    if opp_val == self:
                        setattr(item, "classDiagram_Attribute28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classDiagram_Attribute28"):
                    opp_val = getattr(item, "classDiagram_Attribute28", None)
                    
                    setattr(item, "classDiagram_Attribute28", self)
                    

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
            if hasattr(old_value, "classDiagram_Package4"):
                opp_val = getattr(old_value, "classDiagram_Package4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classDiagram_Package4"):
                opp_val = getattr(value, "classDiagram_Package4", None)
                if opp_val is None:
                    setattr(value, "classDiagram_Package4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class classDiagram_Type(Classifier):

    pass
class classDiagram_Package(ModelingConcept):

    pass
class classDiagram_ClassModel:

    pass