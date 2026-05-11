from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Parameter:

    pass
class Reference:

    pass
class TypedElement:

    pass
class km3_Parameter(TypedElement):

    pass
class km3_Operation(TypedElement):

    pass
class km3_StructuralFeature(TypedElement):

    pass
class Operation:

    pass
class Metamodel:

    pass
class StructuralFeature:

    pass
class km3_Attribute(StructuralFeature):

    pass
class km3_Reference(StructuralFeature):

    def __init__(self, isContainer: str, km3_Reference: "Reference" = None, StructuralFeature: "km3_Class" = None, StructuralFeature13: "km3_StructuralFeature" = None, StructuralFeature15: "km3_StructuralFeature" = None):
        self.isContainer = isContainer
        self.km3_Reference = km3_Reference
        
        pass
    @property
    def isContainer(self):
        return self.__isContainer

    @isContainer.setter
    def isContainer(self, isContainer: str):
        self.__isContainer = isContainer


    @property
    def km3_Reference(self):
        return self.__km3_Reference

    @km3_Reference.setter
    def km3_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_km3_Reference__km3_Reference", None)
        self.__km3_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Reference"):
                opp_val = getattr(old_value, "Reference", None)
                if opp_val == self:
                    setattr(old_value, "Reference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Reference"):
                opp_val = getattr(value, "Reference", None)
                setattr(value, "Reference", self)

class Class:

    pass
class TemplateParameter:

    pass
class Enumeration:

    pass
class EnumLiteral:

    pass
class Classifier:

    pass
class km3_Class(Classifier):

    def __init__(self, isAbstract: str, owner8: set["Operation"] = None, owner: set["StructuralFeature"] = None, km3_Class: set["TemplateParameter"] = None, km3_Class5: set["Class"] = None, Classifier: "km3_TypedElement" = None):
        self.isAbstract = isAbstract
        self.owner8 = owner8 if owner8 is not None else set()
        self.owner = owner if owner is not None else set()
        self.km3_Class = km3_Class if km3_Class is not None else set()
        self.km3_Class5 = km3_Class5 if km3_Class5 is not None else set()
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def km3_Class(self):
        return self.__km3_Class

    @km3_Class.setter
    def km3_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_km3_Class__km3_Class", None)
        self.__km3_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TemplateParameter"):
                    opp_val = getattr(item, "TemplateParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "TemplateParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TemplateParameter"):
                    opp_val = getattr(item, "TemplateParameter", None)
                    
                    setattr(item, "TemplateParameter", self)
                    

    @property
    def km3_Class5(self):
        return self.__km3_Class5

    @km3_Class5.setter
    def km3_Class5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_km3_Class__km3_Class5", None)
        self.__km3_Class5 = value if value is not None else set()
        
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
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_km3_Class__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StructuralFeature"):
                    opp_val = getattr(item, "StructuralFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "StructuralFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StructuralFeature"):
                    opp_val = getattr(item, "StructuralFeature", None)
                    
                    setattr(item, "StructuralFeature", self)
                    

    @property
    def owner8(self):
        return self.__owner8

    @owner8.setter
    def owner8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_km3_Class__owner8", None)
        self.__owner8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    setattr(item, "Operation", self)
                    

class km3_TemplateParameter(Classifier):

    pass
class km3_Enumeration(Classifier):

    pass
class km3_DataType(Classifier):

    pass
class ModelElement:

    pass
class km3_Package(ModelElement):

    pass
class km3_TypedElement(ModelElement):

    def __init__(self, lower: str, upper: str, isOrdered: str, isUnique: str, km3_TypedElement: "Classifier" = None, ModelElement: "km3_Package" = None):
        self.lower = lower
        self.upper = upper
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.km3_TypedElement = km3_TypedElement
        
        pass
    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique


    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper


    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower


    @property
    def isOrdered(self):
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered


    @property
    def km3_TypedElement(self):
        return self.__km3_TypedElement

    @km3_TypedElement.setter
    def km3_TypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_km3_TypedElement__km3_TypedElement", None)
        self.__km3_TypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier"):
                opp_val = getattr(old_value, "Classifier", None)
                if opp_val == self:
                    setattr(old_value, "Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier"):
                opp_val = getattr(value, "Classifier", None)
                setattr(value, "Classifier", self)

class km3_EnumLiteral(ModelElement):

    pass
class km3_Classifier(ModelElement):

    pass
class Package:

    pass
class LocatedElement:

    pass
class km3_Metamodel(LocatedElement):

    pass
class km3_ModelElement(LocatedElement):

    def __init__(self, name: str, contents: "Package" = None):
        self.name = name
        self.contents = contents
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def contents(self):
        return self.__contents

    @contents.setter
    def contents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_km3_ModelElement__contents", None)
        self.__contents = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package"):
                opp_val = getattr(old_value, "Package", None)
                if opp_val == self:
                    setattr(old_value, "Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package"):
                opp_val = getattr(value, "Package", None)
                setattr(value, "Package", self)

class km3_LocatedElement(ABC):

    def __init__(self, location: str):
        self.location = location
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

