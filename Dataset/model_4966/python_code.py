from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Classifier:

    pass
class KM3_Enumeration(Classifier):

    pass
class KM3_DataType(Classifier):

    pass
class ModelElement:

    pass
class KM3_EnumLiteral(ModelElement):

    pass
class KM3_Classifier(ModelElement):

    pass
class KM3_Package(ModelElement):

    pass
class StructuralFeature:

    pass
class KM3_Reference(StructuralFeature):

    def __init__(self, isContainer: bool, KM3_Reference: "KM3_Reference" = None, KM3_Reference6: "KM3_Reference" = None):
        self.isContainer = isContainer
        self.KM3_Reference = KM3_Reference
        self.KM3_Reference6 = KM3_Reference6
        
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
            if hasattr(old_value, "KM3_Reference6"):
                opp_val = getattr(old_value, "KM3_Reference6", None)
                if opp_val == self:
                    setattr(old_value, "KM3_Reference6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "KM3_Reference6"):
                opp_val = getattr(value, "KM3_Reference6", None)
                setattr(value, "KM3_Reference6", self)

    @property
    def KM3_Reference6(self):
        return self.__KM3_Reference6

    @KM3_Reference6.setter
    def KM3_Reference6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_Reference__KM3_Reference6", None)
        self.__KM3_Reference6 = value
        
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
class KM3_StructuralFeature(ModelElement):

    def __init__(self, lower: int, upper: int, isOrdered: bool, isUnique: bool, StructuralFeature: "KM3_Class" = None, structuralFeatures: "KM3_Class" = None, KM3_StructuralFeature: "KM3_Classifier" = None):
        self.lower = lower
        self.upper = upper
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.StructuralFeature = StructuralFeature
        self.structuralFeatures = structuralFeatures
        self.KM3_StructuralFeature = KM3_StructuralFeature
        
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
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def StructuralFeature(self):
        return self.__StructuralFeature

    @StructuralFeature.setter
    def StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_StructuralFeature__StructuralFeature", None)
        self.__StructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def KM3_StructuralFeature(self):
        return self.__KM3_StructuralFeature

    @KM3_StructuralFeature.setter
    def KM3_StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_StructuralFeature__KM3_StructuralFeature", None)
        self.__KM3_StructuralFeature = value
        
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

    @property
    def structuralFeatures(self):
        return self.__structuralFeatures

    @structuralFeatures.setter
    def structuralFeatures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_StructuralFeature__structuralFeatures", None)
        self.__structuralFeatures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class"):
                opp_val = getattr(old_value, "Class", None)
                if opp_val == self:
                    setattr(old_value, "Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class"):
                opp_val = getattr(value, "Class", None)
                setattr(value, "Class", self)

class KM3_Class(Classifier):

    def __init__(self, isAbstract: bool, KM3_Class: "KM3_Class" = None, KM3_Class1: set["KM3_Class"] = None, owner: set["KM3_StructuralFeature"] = None, Class: "KM3_StructuralFeature" = None):
        self.isAbstract = isAbstract
        self.KM3_Class = KM3_Class
        self.KM3_Class1 = KM3_Class1 if KM3_Class1 is not None else set()
        self.owner = owner if owner is not None else set()
        self.Class = Class
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def KM3_Class1(self):
        return self.__KM3_Class1

    @KM3_Class1.setter
    def KM3_Class1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_Class__KM3_Class1", None)
        self.__KM3_Class1 = value if value is not None else set()
        
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
    def KM3_Class(self):
        return self.__KM3_Class

    @KM3_Class.setter
    def KM3_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_Class__KM3_Class", None)
        self.__KM3_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "KM3_Class1"):
                opp_val = getattr(old_value, "KM3_Class1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "KM3_Class1"):
                opp_val = getattr(value, "KM3_Class1", None)
                if opp_val is None:
                    setattr(value, "KM3_Class1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class LocatedElement:

    pass
class KM3_Metamodel(LocatedElement):

    pass
class KM3_ModelElement(LocatedElement):

    def __init__(self, name: str, KM3_ModelElement: "KM3_Package" = None):
        self.name = name
        self.KM3_ModelElement = KM3_ModelElement
        
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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "KM3_Package"):
                opp_val = getattr(value, "KM3_Package", None)
                if opp_val is None:
                    setattr(value, "KM3_Package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class KM3_LocatedElement(ABC):

    def __init__(self, location: str):
        self.location = location
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location
