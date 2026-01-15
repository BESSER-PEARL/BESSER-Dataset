from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ETypedElement:

    pass
class EDataType:

    pass
class RefinementsEcore_EEnum(EDataType):

    pass
class RefinementsEcore_EParameter(ETypedElement):

    pass
class RefinementsEcore_EOperation(ETypedElement):

    pass
class EClassifier:

    pass
class RefinementsEcore_EClass(EClassifier):

    def __init__(self, abstract: bool, interface: bool, RefinementsEcore_EClass9: set["RefinementsEcore_EReference"] = None, RefinementsEcore_EClass11: set["RefinementsEcore_EAttribute"] = None, RefinementsEcore_EClass14: "RefinementsEcore_EAttribute" = None, eContainingClass17: set["RefinementsEcore_EStructuralFeature"] = None, RefinementsEcore_EClass: "RefinementsEcore_EClass" = None, RefinementsEcore_EClass5: set["RefinementsEcore_EClass"] = None, eContainingClass: set["RefinementsEcore_EOperation"] = None, EClass: "RefinementsEcore_EOperation" = None, EClass47: "RefinementsEcore_EStructuralFeature" = None, RefinementsEcore_EClass39: "RefinementsEcore_EReference" = None):
        self.abstract = abstract
        self.interface = interface
        self.RefinementsEcore_EClass9 = RefinementsEcore_EClass9 if RefinementsEcore_EClass9 is not None else set()
        self.RefinementsEcore_EClass11 = RefinementsEcore_EClass11 if RefinementsEcore_EClass11 is not None else set()
        self.RefinementsEcore_EClass14 = RefinementsEcore_EClass14
        self.eContainingClass17 = eContainingClass17 if eContainingClass17 is not None else set()
        self.RefinementsEcore_EClass = RefinementsEcore_EClass
        self.RefinementsEcore_EClass5 = RefinementsEcore_EClass5 if RefinementsEcore_EClass5 is not None else set()
        self.eContainingClass = eContainingClass if eContainingClass is not None else set()
        self.EClass = EClass
        self.EClass47 = EClass47
        self.RefinementsEcore_EClass39 = RefinementsEcore_EClass39
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def interface(self) -> bool:
        return self.__interface

    @interface.setter
    def interface(self, interface: bool):
        self.__interface = interface

    @property
    def RefinementsEcore_EClass14(self):
        return self.__RefinementsEcore_EClass14

    @RefinementsEcore_EClass14.setter
    def RefinementsEcore_EClass14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EClass__RefinementsEcore_EClass14", None)
        self.__RefinementsEcore_EClass14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefinementsEcore_EAttribute15"):
                opp_val = getattr(old_value, "RefinementsEcore_EAttribute15", None)
                if opp_val == self:
                    setattr(old_value, "RefinementsEcore_EAttribute15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefinementsEcore_EAttribute15"):
                opp_val = getattr(value, "RefinementsEcore_EAttribute15", None)
                setattr(value, "RefinementsEcore_EAttribute15", self)

    @property
    def RefinementsEcore_EClass(self):
        return self.__RefinementsEcore_EClass

    @RefinementsEcore_EClass.setter
    def RefinementsEcore_EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EClass__RefinementsEcore_EClass", None)
        self.__RefinementsEcore_EClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefinementsEcore_EClass5"):
                opp_val = getattr(old_value, "RefinementsEcore_EClass5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefinementsEcore_EClass5"):
                opp_val = getattr(value, "RefinementsEcore_EClass5", None)
                if opp_val is None:
                    setattr(value, "RefinementsEcore_EClass5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefinementsEcore_EClass39(self):
        return self.__RefinementsEcore_EClass39

    @RefinementsEcore_EClass39.setter
    def RefinementsEcore_EClass39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EClass__RefinementsEcore_EClass39", None)
        self.__RefinementsEcore_EClass39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefinementsEcore_EReference38"):
                opp_val = getattr(old_value, "RefinementsEcore_EReference38", None)
                if opp_val == self:
                    setattr(old_value, "RefinementsEcore_EReference38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefinementsEcore_EReference38"):
                opp_val = getattr(value, "RefinementsEcore_EReference38", None)
                setattr(value, "RefinementsEcore_EReference38", self)

    @property
    def eContainingClass(self):
        return self.__eContainingClass

    @eContainingClass.setter
    def eContainingClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EClass__eContainingClass", None)
        self.__eContainingClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EOperation"):
                    opp_val = getattr(item, "EOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "EOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EOperation"):
                    opp_val = getattr(item, "EOperation", None)
                    
                    setattr(item, "EOperation", self)
                    

    @property
    def EClass(self):
        return self.__EClass

    @EClass.setter
    def EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EClass__EClass", None)
        self.__EClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eOperations"):
                opp_val = getattr(old_value, "eOperations", None)
                if opp_val == self:
                    setattr(old_value, "eOperations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eOperations"):
                opp_val = getattr(value, "eOperations", None)
                setattr(value, "eOperations", self)

    @property
    def RefinementsEcore_EClass9(self):
        return self.__RefinementsEcore_EClass9

    @RefinementsEcore_EClass9.setter
    def RefinementsEcore_EClass9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EClass__RefinementsEcore_EClass9", None)
        self.__RefinementsEcore_EClass9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefinementsEcore_EReference"):
                    opp_val = getattr(item, "RefinementsEcore_EReference", None)
                    
                    if opp_val == self:
                        setattr(item, "RefinementsEcore_EReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefinementsEcore_EReference"):
                    opp_val = getattr(item, "RefinementsEcore_EReference", None)
                    
                    setattr(item, "RefinementsEcore_EReference", self)
                    

    @property
    def RefinementsEcore_EClass5(self):
        return self.__RefinementsEcore_EClass5

    @RefinementsEcore_EClass5.setter
    def RefinementsEcore_EClass5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EClass__RefinementsEcore_EClass5", None)
        self.__RefinementsEcore_EClass5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefinementsEcore_EClass"):
                    opp_val = getattr(item, "RefinementsEcore_EClass", None)
                    
                    if opp_val == self:
                        setattr(item, "RefinementsEcore_EClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefinementsEcore_EClass"):
                    opp_val = getattr(item, "RefinementsEcore_EClass", None)
                    
                    setattr(item, "RefinementsEcore_EClass", self)
                    

    @property
    def RefinementsEcore_EClass11(self):
        return self.__RefinementsEcore_EClass11

    @RefinementsEcore_EClass11.setter
    def RefinementsEcore_EClass11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EClass__RefinementsEcore_EClass11", None)
        self.__RefinementsEcore_EClass11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefinementsEcore_EAttribute12"):
                    opp_val = getattr(item, "RefinementsEcore_EAttribute12", None)
                    
                    if opp_val == self:
                        setattr(item, "RefinementsEcore_EAttribute12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefinementsEcore_EAttribute12"):
                    opp_val = getattr(item, "RefinementsEcore_EAttribute12", None)
                    
                    setattr(item, "RefinementsEcore_EAttribute12", self)
                    

    @property
    def eContainingClass17(self):
        return self.__eContainingClass17

    @eContainingClass17.setter
    def eContainingClass17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EClass__eContainingClass17", None)
        self.__eContainingClass17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EStructuralFeature"):
                    opp_val = getattr(item, "EStructuralFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "EStructuralFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EStructuralFeature"):
                    opp_val = getattr(item, "EStructuralFeature", None)
                    
                    setattr(item, "EStructuralFeature", self)
                    

    @property
    def EClass47(self):
        return self.__EClass47

    @EClass47.setter
    def EClass47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EClass__EClass47", None)
        self.__EClass47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eStructuralFeatures"):
                opp_val = getattr(old_value, "eStructuralFeatures", None)
                if opp_val == self:
                    setattr(old_value, "eStructuralFeatures", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eStructuralFeatures"):
                opp_val = getattr(value, "eStructuralFeatures", None)
                setattr(value, "eStructuralFeatures", self)

class RefinementsEcore_EModelElement(ABC):

    pass
class EModelElement:

    pass
class RefinementsEcore_ENamedElement(EModelElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class RefinementsEcore_EAnnotation(EModelElement):

    def __init__(self, source: str, eAnnotations: "RefinementsEcore_EModelElement" = None, EAnnotation: "RefinementsEcore_EModelElement" = None):
        self.source = source
        self.eAnnotations = eAnnotations
        self.EAnnotation = EAnnotation
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def eAnnotations(self):
        return self.__eAnnotations

    @eAnnotations.setter
    def eAnnotations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EAnnotation__eAnnotations", None)
        self.__eAnnotations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EModelElement"):
                opp_val = getattr(old_value, "EModelElement", None)
                if opp_val == self:
                    setattr(old_value, "EModelElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EModelElement"):
                opp_val = getattr(value, "EModelElement", None)
                setattr(value, "EModelElement", self)

    @property
    def EAnnotation(self):
        return self.__EAnnotation

    @EAnnotation.setter
    def EAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EAnnotation__EAnnotation", None)
        self.__EAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eModelElement"):
                opp_val = getattr(old_value, "eModelElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eModelElement"):
                opp_val = getattr(value, "eModelElement", None)
                if opp_val is None:
                    setattr(value, "eModelElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RefinementsEcore_EDataType(EClassifier):

    def __init__(self, serializable: bool, RefinementsEcore_EDataType: "RefinementsEcore_EAttribute" = None):
        self.serializable = serializable
        self.RefinementsEcore_EDataType = RefinementsEcore_EDataType
        
    @property
    def serializable(self) -> bool:
        return self.__serializable

    @serializable.setter
    def serializable(self, serializable: bool):
        self.__serializable = serializable

    @property
    def RefinementsEcore_EDataType(self):
        return self.__RefinementsEcore_EDataType

    @RefinementsEcore_EDataType.setter
    def RefinementsEcore_EDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EDataType__RefinementsEcore_EDataType", None)
        self.__RefinementsEcore_EDataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefinementsEcore_EAttribute"):
                opp_val = getattr(old_value, "RefinementsEcore_EAttribute", None)
                if opp_val == self:
                    setattr(old_value, "RefinementsEcore_EAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefinementsEcore_EAttribute"):
                opp_val = getattr(value, "RefinementsEcore_EAttribute", None)
                setattr(value, "RefinementsEcore_EAttribute", self)

class ENamedElement:

    pass
class RefinementsEcore_EPackage(ENamedElement):

    def __init__(self, nsURI: str, nsPrefix: str, ePackage: set["RefinementsEcore_EClassifier"] = None, EPackage28: "RefinementsEcore_EPackage" = None, EPackage: "RefinementsEcore_EClassifier" = None, eSuperPackage: set["RefinementsEcore_EPackage"] = None, EPackage31: "RefinementsEcore_EPackage" = None, eSubpackages: "RefinementsEcore_EPackage" = None):
        self.nsURI = nsURI
        self.nsPrefix = nsPrefix
        self.ePackage = ePackage if ePackage is not None else set()
        self.EPackage28 = EPackage28
        self.EPackage = EPackage
        self.eSuperPackage = eSuperPackage if eSuperPackage is not None else set()
        self.EPackage31 = EPackage31
        self.eSubpackages = eSubpackages
        
    @property
    def nsPrefix(self) -> str:
        return self.__nsPrefix

    @nsPrefix.setter
    def nsPrefix(self, nsPrefix: str):
        self.__nsPrefix = nsPrefix

    @property
    def nsURI(self) -> str:
        return self.__nsURI

    @nsURI.setter
    def nsURI(self, nsURI: str):
        self.__nsURI = nsURI

    @property
    def eSuperPackage(self):
        return self.__eSuperPackage

    @eSuperPackage.setter
    def eSuperPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EPackage__eSuperPackage", None)
        self.__eSuperPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EPackage28"):
                    opp_val = getattr(item, "EPackage28", None)
                    
                    if opp_val == self:
                        setattr(item, "EPackage28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EPackage28"):
                    opp_val = getattr(item, "EPackage28", None)
                    
                    setattr(item, "EPackage28", self)
                    

    @property
    def ePackage(self):
        return self.__ePackage

    @ePackage.setter
    def ePackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EPackage__ePackage", None)
        self.__ePackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EClassifier"):
                    opp_val = getattr(item, "EClassifier", None)
                    
                    if opp_val == self:
                        setattr(item, "EClassifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EClassifier"):
                    opp_val = getattr(item, "EClassifier", None)
                    
                    setattr(item, "EClassifier", self)
                    

    @property
    def EPackage28(self):
        return self.__EPackage28

    @EPackage28.setter
    def EPackage28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EPackage__EPackage28", None)
        self.__EPackage28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eSuperPackage"):
                opp_val = getattr(old_value, "eSuperPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eSuperPackage"):
                opp_val = getattr(value, "eSuperPackage", None)
                if opp_val is None:
                    setattr(value, "eSuperPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EPackage31(self):
        return self.__EPackage31

    @EPackage31.setter
    def EPackage31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EPackage__EPackage31", None)
        self.__EPackage31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eSubpackages"):
                opp_val = getattr(old_value, "eSubpackages", None)
                if opp_val == self:
                    setattr(old_value, "eSubpackages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eSubpackages"):
                opp_val = getattr(value, "eSubpackages", None)
                setattr(value, "eSubpackages", self)

    @property
    def EPackage(self):
        return self.__EPackage

    @EPackage.setter
    def EPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EPackage__EPackage", None)
        self.__EPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eClassifiers"):
                opp_val = getattr(old_value, "eClassifiers", None)
                if opp_val == self:
                    setattr(old_value, "eClassifiers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eClassifiers"):
                opp_val = getattr(value, "eClassifiers", None)
                setattr(value, "eClassifiers", self)

    @property
    def eSubpackages(self):
        return self.__eSubpackages

    @eSubpackages.setter
    def eSubpackages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EPackage__eSubpackages", None)
        self.__eSubpackages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EPackage31"):
                opp_val = getattr(old_value, "EPackage31", None)
                if opp_val == self:
                    setattr(old_value, "EPackage31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EPackage31"):
                opp_val = getattr(value, "EPackage31", None)
                setattr(value, "EPackage31", self)

class RefinementsEcore_ETypedElement(ENamedElement):

    def __init__(self, ordered: bool, unique: bool, lowerBound: int, upperBound: int, many: bool, required: bool, RefinementsEcore_ETypedElement: "RefinementsEcore_EClassifier" = None):
        self.ordered = ordered
        self.unique = unique
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.many = many
        self.required = required
        self.RefinementsEcore_ETypedElement = RefinementsEcore_ETypedElement
        
    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def ordered(self) -> bool:
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered

    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def RefinementsEcore_ETypedElement(self):
        return self.__RefinementsEcore_ETypedElement

    @RefinementsEcore_ETypedElement.setter
    def RefinementsEcore_ETypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_ETypedElement__RefinementsEcore_ETypedElement", None)
        self.__RefinementsEcore_ETypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefinementsEcore_EClassifier49"):
                opp_val = getattr(old_value, "RefinementsEcore_EClassifier49", None)
                if opp_val == self:
                    setattr(old_value, "RefinementsEcore_EClassifier49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefinementsEcore_EClassifier49"):
                opp_val = getattr(value, "RefinementsEcore_EClassifier49", None)
                setattr(value, "RefinementsEcore_EClassifier49", self)

class RefinementsEcore_EEnumLiteral(ENamedElement):

    def __init__(self, value: int, literal: str, EEnumLiteral: "RefinementsEcore_EEnum" = None, eLiterals: "RefinementsEcore_EEnum" = None):
        self.value = value
        self.literal = literal
        self.EEnumLiteral = EEnumLiteral
        self.eLiterals = eLiterals
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

    @property
    def eLiterals(self):
        return self.__eLiterals

    @eLiterals.setter
    def eLiterals(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EEnumLiteral__eLiterals", None)
        self.__eLiterals = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EEnum"):
                opp_val = getattr(old_value, "EEnum", None)
                if opp_val == self:
                    setattr(old_value, "EEnum", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EEnum"):
                opp_val = getattr(value, "EEnum", None)
                setattr(value, "EEnum", self)

    @property
    def EEnumLiteral(self):
        return self.__EEnumLiteral

    @EEnumLiteral.setter
    def EEnumLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EEnumLiteral__EEnumLiteral", None)
        self.__EEnumLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eEnum"):
                opp_val = getattr(old_value, "eEnum", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eEnum"):
                opp_val = getattr(value, "eEnum", None)
                if opp_val is None:
                    setattr(value, "eEnum", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RefinementsEcore_EClassifier(ENamedElement):

    def __init__(self, instanceClassName: str, instanceClass: str, instanceTypeName: str, RefinementsEcore_EClassifier: "RefinementsEcore_EOperation" = None, EClassifier: "RefinementsEcore_EPackage" = None, eClassifiers: "RefinementsEcore_EPackage" = None, RefinementsEcore_EClassifier49: "RefinementsEcore_ETypedElement" = None):
        self.instanceClassName = instanceClassName
        self.instanceClass = instanceClass
        self.instanceTypeName = instanceTypeName
        self.RefinementsEcore_EClassifier = RefinementsEcore_EClassifier
        self.EClassifier = EClassifier
        self.eClassifiers = eClassifiers
        self.RefinementsEcore_EClassifier49 = RefinementsEcore_EClassifier49
        
    @property
    def instanceClass(self) -> str:
        return self.__instanceClass

    @instanceClass.setter
    def instanceClass(self, instanceClass: str):
        self.__instanceClass = instanceClass

    @property
    def instanceClassName(self) -> str:
        return self.__instanceClassName

    @instanceClassName.setter
    def instanceClassName(self, instanceClassName: str):
        self.__instanceClassName = instanceClassName

    @property
    def instanceTypeName(self) -> str:
        return self.__instanceTypeName

    @instanceTypeName.setter
    def instanceTypeName(self, instanceTypeName: str):
        self.__instanceTypeName = instanceTypeName

    @property
    def eClassifiers(self):
        return self.__eClassifiers

    @eClassifiers.setter
    def eClassifiers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EClassifier__eClassifiers", None)
        self.__eClassifiers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EPackage"):
                opp_val = getattr(old_value, "EPackage", None)
                if opp_val == self:
                    setattr(old_value, "EPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EPackage"):
                opp_val = getattr(value, "EPackage", None)
                setattr(value, "EPackage", self)

    @property
    def RefinementsEcore_EClassifier(self):
        return self.__RefinementsEcore_EClassifier

    @RefinementsEcore_EClassifier.setter
    def RefinementsEcore_EClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EClassifier__RefinementsEcore_EClassifier", None)
        self.__RefinementsEcore_EClassifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefinementsEcore_EOperation"):
                opp_val = getattr(old_value, "RefinementsEcore_EOperation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefinementsEcore_EOperation"):
                opp_val = getattr(value, "RefinementsEcore_EOperation", None)
                if opp_val is None:
                    setattr(value, "RefinementsEcore_EOperation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EClassifier(self):
        return self.__EClassifier

    @EClassifier.setter
    def EClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EClassifier__EClassifier", None)
        self.__EClassifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ePackage"):
                opp_val = getattr(old_value, "ePackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ePackage"):
                opp_val = getattr(value, "ePackage", None)
                if opp_val is None:
                    setattr(value, "ePackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefinementsEcore_EClassifier49(self):
        return self.__RefinementsEcore_EClassifier49

    @RefinementsEcore_EClassifier49.setter
    def RefinementsEcore_EClassifier49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EClassifier__RefinementsEcore_EClassifier49", None)
        self.__RefinementsEcore_EClassifier49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefinementsEcore_ETypedElement"):
                opp_val = getattr(old_value, "RefinementsEcore_ETypedElement", None)
                if opp_val == self:
                    setattr(old_value, "RefinementsEcore_ETypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefinementsEcore_ETypedElement"):
                opp_val = getattr(value, "RefinementsEcore_ETypedElement", None)
                setattr(value, "RefinementsEcore_ETypedElement", self)

class RefinementsEcore_EStructuralFeature(ETypedElement):

    def __init__(self, transient: bool, defaultValueLiteral: str, unsettable: bool, derived: bool, changeable: bool, volatile: bool, EStructuralFeature: "RefinementsEcore_EClass" = None, eStructuralFeatures: "RefinementsEcore_EClass" = None):
        self.transient = transient
        self.defaultValueLiteral = defaultValueLiteral
        self.unsettable = unsettable
        self.derived = derived
        self.changeable = changeable
        self.volatile = volatile
        self.EStructuralFeature = EStructuralFeature
        self.eStructuralFeatures = eStructuralFeatures
        
    @property
    def volatile(self) -> bool:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: bool):
        self.__volatile = volatile

    @property
    def unsettable(self) -> bool:
        return self.__unsettable

    @unsettable.setter
    def unsettable(self, unsettable: bool):
        self.__unsettable = unsettable

    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def changeable(self) -> bool:
        return self.__changeable

    @changeable.setter
    def changeable(self, changeable: bool):
        self.__changeable = changeable

    @property
    def defaultValueLiteral(self) -> str:
        return self.__defaultValueLiteral

    @defaultValueLiteral.setter
    def defaultValueLiteral(self, defaultValueLiteral: str):
        self.__defaultValueLiteral = defaultValueLiteral

    @property
    def EStructuralFeature(self):
        return self.__EStructuralFeature

    @EStructuralFeature.setter
    def EStructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EStructuralFeature__EStructuralFeature", None)
        self.__EStructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eContainingClass17"):
                opp_val = getattr(old_value, "eContainingClass17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eContainingClass17"):
                opp_val = getattr(value, "eContainingClass17", None)
                if opp_val is None:
                    setattr(value, "eContainingClass17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eStructuralFeatures(self):
        return self.__eStructuralFeatures

    @eStructuralFeatures.setter
    def eStructuralFeatures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EStructuralFeature__eStructuralFeatures", None)
        self.__eStructuralFeatures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EClass47"):
                opp_val = getattr(old_value, "EClass47", None)
                if opp_val == self:
                    setattr(old_value, "EClass47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EClass47"):
                opp_val = getattr(value, "EClass47", None)
                setattr(value, "EClass47", self)

class EStructuralFeature:

    pass
class RefinementsEcore_EReference(EStructuralFeature):

    def __init__(self, containment: bool, container: bool, resolveProxies: bool, RefinementsEcore_EReference: "RefinementsEcore_EClass" = None, RefinementsEcore_EReference36: "RefinementsEcore_EReference" = None, RefinementsEcore_EReference34: "RefinementsEcore_EReference" = None, RefinementsEcore_EReference38: "RefinementsEcore_EClass" = None, RefinementsEcore_EReference41: set["RefinementsEcore_EAttribute"] = None, RefinementsEcore_EReference45: "RefinementsEcore_EReference" = None, RefinementsEcore_EReference43: "RefinementsEcore_EReference" = None):
        self.containment = containment
        self.container = container
        self.resolveProxies = resolveProxies
        self.RefinementsEcore_EReference = RefinementsEcore_EReference
        self.RefinementsEcore_EReference36 = RefinementsEcore_EReference36
        self.RefinementsEcore_EReference34 = RefinementsEcore_EReference34
        self.RefinementsEcore_EReference38 = RefinementsEcore_EReference38
        self.RefinementsEcore_EReference41 = RefinementsEcore_EReference41 if RefinementsEcore_EReference41 is not None else set()
        self.RefinementsEcore_EReference45 = RefinementsEcore_EReference45
        self.RefinementsEcore_EReference43 = RefinementsEcore_EReference43
        
    @property
    def containment(self) -> bool:
        return self.__containment

    @containment.setter
    def containment(self, containment: bool):
        self.__containment = containment

    @property
    def container(self) -> bool:
        return self.__container

    @container.setter
    def container(self, container: bool):
        self.__container = container

    @property
    def resolveProxies(self) -> bool:
        return self.__resolveProxies

    @resolveProxies.setter
    def resolveProxies(self, resolveProxies: bool):
        self.__resolveProxies = resolveProxies

    @property
    def RefinementsEcore_EReference(self):
        return self.__RefinementsEcore_EReference

    @RefinementsEcore_EReference.setter
    def RefinementsEcore_EReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EReference__RefinementsEcore_EReference", None)
        self.__RefinementsEcore_EReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefinementsEcore_EClass9"):
                opp_val = getattr(old_value, "RefinementsEcore_EClass9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefinementsEcore_EClass9"):
                opp_val = getattr(value, "RefinementsEcore_EClass9", None)
                if opp_val is None:
                    setattr(value, "RefinementsEcore_EClass9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefinementsEcore_EReference43(self):
        return self.__RefinementsEcore_EReference43

    @RefinementsEcore_EReference43.setter
    def RefinementsEcore_EReference43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EReference__RefinementsEcore_EReference43", None)
        self.__RefinementsEcore_EReference43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefinementsEcore_EReference45"):
                opp_val = getattr(old_value, "RefinementsEcore_EReference45", None)
                if opp_val == self:
                    setattr(old_value, "RefinementsEcore_EReference45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefinementsEcore_EReference45"):
                opp_val = getattr(value, "RefinementsEcore_EReference45", None)
                setattr(value, "RefinementsEcore_EReference45", self)

    @property
    def RefinementsEcore_EReference38(self):
        return self.__RefinementsEcore_EReference38

    @RefinementsEcore_EReference38.setter
    def RefinementsEcore_EReference38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EReference__RefinementsEcore_EReference38", None)
        self.__RefinementsEcore_EReference38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefinementsEcore_EClass39"):
                opp_val = getattr(old_value, "RefinementsEcore_EClass39", None)
                if opp_val == self:
                    setattr(old_value, "RefinementsEcore_EClass39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefinementsEcore_EClass39"):
                opp_val = getattr(value, "RefinementsEcore_EClass39", None)
                setattr(value, "RefinementsEcore_EClass39", self)

    @property
    def RefinementsEcore_EReference45(self):
        return self.__RefinementsEcore_EReference45

    @RefinementsEcore_EReference45.setter
    def RefinementsEcore_EReference45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EReference__RefinementsEcore_EReference45", None)
        self.__RefinementsEcore_EReference45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefinementsEcore_EReference43"):
                opp_val = getattr(old_value, "RefinementsEcore_EReference43", None)
                if opp_val == self:
                    setattr(old_value, "RefinementsEcore_EReference43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefinementsEcore_EReference43"):
                opp_val = getattr(value, "RefinementsEcore_EReference43", None)
                setattr(value, "RefinementsEcore_EReference43", self)

    @property
    def RefinementsEcore_EReference41(self):
        return self.__RefinementsEcore_EReference41

    @RefinementsEcore_EReference41.setter
    def RefinementsEcore_EReference41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EReference__RefinementsEcore_EReference41", None)
        self.__RefinementsEcore_EReference41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefinementsEcore_EAttribute42"):
                    opp_val = getattr(item, "RefinementsEcore_EAttribute42", None)
                    
                    if opp_val == self:
                        setattr(item, "RefinementsEcore_EAttribute42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefinementsEcore_EAttribute42"):
                    opp_val = getattr(item, "RefinementsEcore_EAttribute42", None)
                    
                    setattr(item, "RefinementsEcore_EAttribute42", self)
                    

    @property
    def RefinementsEcore_EReference34(self):
        return self.__RefinementsEcore_EReference34

    @RefinementsEcore_EReference34.setter
    def RefinementsEcore_EReference34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EReference__RefinementsEcore_EReference34", None)
        self.__RefinementsEcore_EReference34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefinementsEcore_EReference36"):
                opp_val = getattr(old_value, "RefinementsEcore_EReference36", None)
                if opp_val == self:
                    setattr(old_value, "RefinementsEcore_EReference36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefinementsEcore_EReference36"):
                opp_val = getattr(value, "RefinementsEcore_EReference36", None)
                setattr(value, "RefinementsEcore_EReference36", self)

    @property
    def RefinementsEcore_EReference36(self):
        return self.__RefinementsEcore_EReference36

    @RefinementsEcore_EReference36.setter
    def RefinementsEcore_EReference36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EReference__RefinementsEcore_EReference36", None)
        self.__RefinementsEcore_EReference36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefinementsEcore_EReference34"):
                opp_val = getattr(old_value, "RefinementsEcore_EReference34", None)
                if opp_val == self:
                    setattr(old_value, "RefinementsEcore_EReference34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefinementsEcore_EReference34"):
                opp_val = getattr(value, "RefinementsEcore_EReference34", None)
                setattr(value, "RefinementsEcore_EReference34", self)

class RefinementsEcore_EAttribute(EStructuralFeature):

    def __init__(self, iD: int, RefinementsEcore_EAttribute12: "RefinementsEcore_EClass" = None, RefinementsEcore_EAttribute15: "RefinementsEcore_EClass" = None, RefinementsEcore_EAttribute: "RefinementsEcore_EDataType" = None, RefinementsEcore_EAttribute3: "RefinementsEcore_EAttribute" = None, RefinementsEcore_EAttribute1: "RefinementsEcore_EAttribute" = None, RefinementsEcore_EAttribute42: "RefinementsEcore_EReference" = None):
        self.iD = iD
        self.RefinementsEcore_EAttribute12 = RefinementsEcore_EAttribute12
        self.RefinementsEcore_EAttribute15 = RefinementsEcore_EAttribute15
        self.RefinementsEcore_EAttribute = RefinementsEcore_EAttribute
        self.RefinementsEcore_EAttribute3 = RefinementsEcore_EAttribute3
        self.RefinementsEcore_EAttribute1 = RefinementsEcore_EAttribute1
        self.RefinementsEcore_EAttribute42 = RefinementsEcore_EAttribute42
        
    @property
    def iD(self) -> int:
        return self.__iD

    @iD.setter
    def iD(self, iD: int):
        self.__iD = iD

    @property
    def RefinementsEcore_EAttribute1(self):
        return self.__RefinementsEcore_EAttribute1

    @RefinementsEcore_EAttribute1.setter
    def RefinementsEcore_EAttribute1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EAttribute__RefinementsEcore_EAttribute1", None)
        self.__RefinementsEcore_EAttribute1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefinementsEcore_EAttribute3"):
                opp_val = getattr(old_value, "RefinementsEcore_EAttribute3", None)
                if opp_val == self:
                    setattr(old_value, "RefinementsEcore_EAttribute3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefinementsEcore_EAttribute3"):
                opp_val = getattr(value, "RefinementsEcore_EAttribute3", None)
                setattr(value, "RefinementsEcore_EAttribute3", self)

    @property
    def RefinementsEcore_EAttribute(self):
        return self.__RefinementsEcore_EAttribute

    @RefinementsEcore_EAttribute.setter
    def RefinementsEcore_EAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EAttribute__RefinementsEcore_EAttribute", None)
        self.__RefinementsEcore_EAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefinementsEcore_EDataType"):
                opp_val = getattr(old_value, "RefinementsEcore_EDataType", None)
                if opp_val == self:
                    setattr(old_value, "RefinementsEcore_EDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefinementsEcore_EDataType"):
                opp_val = getattr(value, "RefinementsEcore_EDataType", None)
                setattr(value, "RefinementsEcore_EDataType", self)

    @property
    def RefinementsEcore_EAttribute42(self):
        return self.__RefinementsEcore_EAttribute42

    @RefinementsEcore_EAttribute42.setter
    def RefinementsEcore_EAttribute42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EAttribute__RefinementsEcore_EAttribute42", None)
        self.__RefinementsEcore_EAttribute42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefinementsEcore_EReference41"):
                opp_val = getattr(old_value, "RefinementsEcore_EReference41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefinementsEcore_EReference41"):
                opp_val = getattr(value, "RefinementsEcore_EReference41", None)
                if opp_val is None:
                    setattr(value, "RefinementsEcore_EReference41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefinementsEcore_EAttribute3(self):
        return self.__RefinementsEcore_EAttribute3

    @RefinementsEcore_EAttribute3.setter
    def RefinementsEcore_EAttribute3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EAttribute__RefinementsEcore_EAttribute3", None)
        self.__RefinementsEcore_EAttribute3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefinementsEcore_EAttribute1"):
                opp_val = getattr(old_value, "RefinementsEcore_EAttribute1", None)
                if opp_val == self:
                    setattr(old_value, "RefinementsEcore_EAttribute1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefinementsEcore_EAttribute1"):
                opp_val = getattr(value, "RefinementsEcore_EAttribute1", None)
                setattr(value, "RefinementsEcore_EAttribute1", self)

    @property
    def RefinementsEcore_EAttribute12(self):
        return self.__RefinementsEcore_EAttribute12

    @RefinementsEcore_EAttribute12.setter
    def RefinementsEcore_EAttribute12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EAttribute__RefinementsEcore_EAttribute12", None)
        self.__RefinementsEcore_EAttribute12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefinementsEcore_EClass11"):
                opp_val = getattr(old_value, "RefinementsEcore_EClass11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefinementsEcore_EClass11"):
                opp_val = getattr(value, "RefinementsEcore_EClass11", None)
                if opp_val is None:
                    setattr(value, "RefinementsEcore_EClass11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RefinementsEcore_EAttribute15(self):
        return self.__RefinementsEcore_EAttribute15

    @RefinementsEcore_EAttribute15.setter
    def RefinementsEcore_EAttribute15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RefinementsEcore_EAttribute__RefinementsEcore_EAttribute15", None)
        self.__RefinementsEcore_EAttribute15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RefinementsEcore_EClass14"):
                opp_val = getattr(old_value, "RefinementsEcore_EClass14", None)
                if opp_val == self:
                    setattr(old_value, "RefinementsEcore_EClass14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RefinementsEcore_EClass14"):
                opp_val = getattr(value, "RefinementsEcore_EClass14", None)
                setattr(value, "RefinementsEcore_EClass14", self)
