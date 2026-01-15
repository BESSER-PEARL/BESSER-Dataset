from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class StructuralFeature:

    pass
class KM3_Reference(StructuralFeature):

    def __init__(self, isContainer: str, KM3_Reference: "KM3_Reference" = None, KM3_Reference17: "KM3_Reference" = None):
        self.isContainer = isContainer
        self.KM3_Reference = KM3_Reference
        self.KM3_Reference17 = KM3_Reference17
        
    @property
    def isContainer(self) -> str:
        return self.__isContainer

    @isContainer.setter
    def isContainer(self, isContainer: str):
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
            if hasattr(old_value, "KM3_Reference17"):
                opp_val = getattr(old_value, "KM3_Reference17", None)
                if opp_val == self:
                    setattr(old_value, "KM3_Reference17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "KM3_Reference17"):
                opp_val = getattr(value, "KM3_Reference17", None)
                setattr(value, "KM3_Reference17", self)

    @property
    def KM3_Reference17(self):
        return self.__KM3_Reference17

    @KM3_Reference17.setter
    def KM3_Reference17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_Reference__KM3_Reference17", None)
        self.__KM3_Reference17 = value
        
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
class TypedElement:

    pass
class KM3_Operation(TypedElement):

    pass
class KM3_StructuralFeature(TypedElement):

    pass
class KM3_Parameter(TypedElement):

    pass
class Classifier:

    pass
class KM3_Enumeration(Classifier):

    pass
class KM3_TemplateParameter(Classifier):

    pass
class KM3_Class(Classifier):

    def __init__(self, isAbstract: str, KM3_Class: set["KM3_TemplateParameter"] = None, KM3_Class5: "KM3_Class" = None, KM3_Class3: set["KM3_Class"] = None, Class: "KM3_StructuralFeature" = None, Class20: "KM3_Operation" = None, owner: set["KM3_StructuralFeature"] = None, owner8: set["KM3_Operation"] = None):
        self.isAbstract = isAbstract
        self.KM3_Class = KM3_Class if KM3_Class is not None else set()
        self.KM3_Class5 = KM3_Class5
        self.KM3_Class3 = KM3_Class3 if KM3_Class3 is not None else set()
        self.Class = Class
        self.Class20 = Class20
        self.owner = owner if owner is not None else set()
        self.owner8 = owner8 if owner8 is not None else set()
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
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
    def KM3_Class(self):
        return self.__KM3_Class

    @KM3_Class.setter
    def KM3_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_Class__KM3_Class", None)
        self.__KM3_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "KM3_TemplateParameter"):
                    opp_val = getattr(item, "KM3_TemplateParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "KM3_TemplateParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "KM3_TemplateParameter"):
                    opp_val = getattr(item, "KM3_TemplateParameter", None)
                    
                    setattr(item, "KM3_TemplateParameter", self)
                    

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
                if hasattr(item, "KM3_Class5"):
                    opp_val = getattr(item, "KM3_Class5", None)
                    
                    if opp_val == self:
                        setattr(item, "KM3_Class5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "KM3_Class5"):
                    opp_val = getattr(item, "KM3_Class5", None)
                    
                    setattr(item, "KM3_Class5", self)
                    

    @property
    def KM3_Class5(self):
        return self.__KM3_Class5

    @KM3_Class5.setter
    def KM3_Class5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_Class__KM3_Class5", None)
        self.__KM3_Class5 = value
        
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

    @property
    def owner8(self):
        return self.__owner8

    @owner8.setter
    def owner8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_Class__owner8", None)
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
                    

    @property
    def Class20(self):
        return self.__Class20

    @Class20.setter
    def Class20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KM3_Class__Class20", None)
        self.__Class20 = value
        
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

class KM3_DataType(Classifier):

    pass
class ModelElement:

    pass
class KM3_EnumLiteral(ModelElement):

    pass
class KM3_TypedElement(ModelElement):

    def __init__(self, isOrdered: str, isUnique: str, lower: str, upper: str, KM3_TypedElement: "KM3_Classifier" = None):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        self.KM3_TypedElement = KM3_TypedElement
        
    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def isOrdered(self) -> str:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

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

class KM3_Package(ModelElement):

    pass
class KM3_Classifier(ModelElement):

    pass
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
