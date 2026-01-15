from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TypedElement:

    pass
class KM3_Operation(TypedElement):

    pass
class KM3_Parameter(TypedElement):

    pass
class StructuralFeature:

    pass
class KM3_Reference(StructuralFeature):

    def __init__(self, isContainer: bool, KM3_Reference: "KM3_Reference" = None, KM3_Reference16: "KM3_Reference" = None):
        self.isContainer = isContainer
        self.KM3_Reference = KM3_Reference
        self.KM3_Reference16 = KM3_Reference16
        
    @property
    def isContainer(self) -> bool:
        return self.__isContainer

    @isContainer.setter
    def isContainer(self, isContainer: bool):
        self.__isContainer = isContainer

    @property
    def KM3_Reference(self):
        return self.__KM3_Reference

    @KM3_Reference.setter
    def KM3_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_Reference__KM3_Reference", None)
        self.__KM3_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "KM3_Reference16"):
                opp_val = getattr(old_value, "KM3_Reference16", None)
                if opp_val == self:
                    setattr(old_value, "KM3_Reference16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "KM3_Reference16"):
                opp_val = getattr(value, "KM3_Reference16", None)
                setattr(value, "KM3_Reference16", self)

    @property
    def KM3_Reference16(self):
        return self.__KM3_Reference16

    @KM3_Reference16.setter
    def KM3_Reference16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_Reference__KM3_Reference16", None)
        self.__KM3_Reference16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "KM3_Reference"):
                opp_val = getattr(old_value, "KM3_Reference", None)
                if opp_val == self:
                    setattr(old_value, "KM3_Reference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "KM3_Reference"):
                opp_val = getattr(value, "KM3_Reference", None)
                setattr(value, "KM3_Reference", self)

class KM3_Attribute(StructuralFeature):

    pass
class KM3_LocatedElement(ABC):

    def __init__(self, commentsAfter: str, location: str, commentsBefore: str):
        self.commentsAfter = commentsAfter
        self.location = location
        self.commentsBefore = commentsBefore
        
    @property
    def commentsAfter(self) -> str:
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def commentsBefore(self) -> str:
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore

class KM3_StructuralFeature(TypedElement):

    pass
class Classifier:

    pass
class KM3_Enumeration(Classifier):

    pass
class KM3_Class(Classifier):

    def __init__(self, isAbstract: bool, KM3_Class: "KM3_Class" = None, KM3_Class3: set["KM3_Class"] = None, owner: set["KM3_StructuralFeature"] = None, Class19: "KM3_Operation" = None, owner7: set["KM3_Operation"] = None, Class: "KM3_StructuralFeature" = None):
        self.isAbstract = isAbstract
        self.KM3_Class = KM3_Class
        self.KM3_Class3 = KM3_Class3 if KM3_Class3 is not None else set()
        self.owner = owner if owner is not None else set()
        self.Class19 = Class19
        self.owner7 = owner7 if owner7 is not None else set()
        self.Class = Class
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structuralFeatures"):
                opp_val = getattr(old_value, "structuralFeatures", None)
                if opp_val == self:
                    setattr(old_value, "structuralFeatures", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structuralFeatures"):
                opp_val = getattr(value, "structuralFeatures", None)
                setattr(value, "structuralFeatures", self)

    @property
    def Class19(self):
        return self.__Class19

    @Class19.setter
    def Class19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_Class__Class19", None)
        self.__Class19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operations"):
                opp_val = getattr(old_value, "operations", None)
                if opp_val == self:
                    setattr(old_value, "operations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operations"):
                opp_val = getattr(value, "operations", None)
                setattr(value, "operations", self)

    @property
    def KM3_Class3(self):
        return self.__KM3_Class3

    @KM3_Class3.setter
    def KM3_Class3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_Class__KM3_Class3", None)
        self.__KM3_Class3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "KM3_Class"):
                    opp_val = getattr(item, "KM3_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "KM3_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "KM3_Class"):
                    opp_val = getattr(item, "KM3_Class", None)
                    
                    setattr(item, "KM3_Class", self)
                    

    @property
    def owner7(self):
        return self.__owner7

    @owner7.setter
    def owner7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_Class__owner7", None)
        self.__owner7 = value if value is not None else set()
        
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
                    

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_Class__owner", None)
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
    def KM3_Class(self):
        return self.__KM3_Class

    @KM3_Class.setter
    def KM3_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_Class__KM3_Class", None)
        self.__KM3_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "KM3_Class3"):
                opp_val = getattr(old_value, "KM3_Class3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "KM3_Class3"):
                opp_val = getattr(value, "KM3_Class3", None)
                if opp_val is None:
                    setattr(value, "KM3_Class3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class KM3_DataType(Classifier):

    pass
class ModelElement:

    pass
class KM3_EnumLiteral(ModelElement):

    pass
class KM3_TypedElement(ModelElement):

    def __init__(self, lower: int, upper: int, isOrdered: bool, isUnique: bool, KM3_TypedElement: "KM3_Classifier" = None):
        self.lower = lower
        self.upper = upper
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.KM3_TypedElement = KM3_TypedElement
        
    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def isUnique(self) -> bool:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def KM3_TypedElement(self):
        return self.__KM3_TypedElement

    @KM3_TypedElement.setter
    def KM3_TypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_TypedElement__KM3_TypedElement", None)
        self.__KM3_TypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "KM3_Classifier"):
                opp_val = getattr(old_value, "KM3_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "KM3_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "KM3_Classifier"):
                opp_val = getattr(value, "KM3_Classifier", None)
                setattr(value, "KM3_Classifier", self)

class KM3_Classifier(ModelElement):

    pass
class KM3_Package(ModelElement):

    pass
class LocatedElement:

    pass
class KM3_Metamodel(LocatedElement):

    pass
class KM3_ModelElement(LocatedElement):

    def __init__(self, name: str, KM3_ModelElement: "KM3_Package" = None, KM3_ModelElement26: "KM3_Package" = None):
        self.name = name
        self.KM3_ModelElement = KM3_ModelElement
        self.KM3_ModelElement26 = KM3_ModelElement26
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def KM3_ModelElement(self):
        return self.__KM3_ModelElement

    @KM3_ModelElement.setter
    def KM3_ModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_ModelElement__KM3_ModelElement", None)
        self.__KM3_ModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "KM3_Package"):
                opp_val = getattr(old_value, "KM3_Package", None)
                if opp_val == self:
                    setattr(old_value, "KM3_Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "KM3_Package"):
                opp_val = getattr(value, "KM3_Package", None)
                setattr(value, "KM3_Package", self)

    @property
    def KM3_ModelElement26(self):
        return self.__KM3_ModelElement26

    @KM3_ModelElement26.setter
    def KM3_ModelElement26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_ModelElement__KM3_ModelElement26", None)
        self.__KM3_ModelElement26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "KM3_Package25"):
                opp_val = getattr(old_value, "KM3_Package25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "KM3_Package25"):
                opp_val = getattr(value, "KM3_Package25", None)
                if opp_val is None:
                    setattr(value, "KM3_Package25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
