from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ETypedElement:

    pass
class ecore_EParameter(ETypedElement):

    pass
class EObject:

    pass
class EDataType:

    pass
class ecore_EEnum(EDataType):

    def __init__(self, eEnum: set["ecore_EEnumLiteral"] = None, EEnum: "ecore_EEnumLiteral" = None):
        self.eEnum = eEnum if eEnum is not None else set()
        self.EEnum = EEnum
        
    @property
    def EEnum(self):
        return self.__EEnum

    @EEnum.setter
    def EEnum(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EEnum__EEnum", None)
        self.__EEnum = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eLiterals"):
                opp_val = getattr(old_value, "eLiterals", None)
                if opp_val == self:
                    setattr(old_value, "eLiterals", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eLiterals"):
                opp_val = getattr(value, "eLiterals", None)
                setattr(value, "eLiterals", self)

    @property
    def eEnum(self):
        return self.__eEnum

    @eEnum.setter
    def eEnum(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EEnum__eEnum", None)
        self.__eEnum = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EEnumLiteral"):
                    opp_val = getattr(item, "EEnumLiteral", None)
                    
                    if opp_val == self:
                        setattr(item, "EEnumLiteral", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EEnumLiteral"):
                    opp_val = getattr(item, "EEnumLiteral", None)
                    
                    setattr(item, "EEnumLiteral", self)
                    

    def getEEnumLiteralByLiteral(self, literal: str) -> str:
        # TODO: Implement getEEnumLiteralByLiteral method
        pass

    def getEEnumLiteral(self, value: int) -> str:
        # TODO: Implement getEEnumLiteral method
        pass

    def getEEnumLiteral(self, name: str) -> str:
        # TODO: Implement getEEnumLiteral method
        pass

class ENamedElement:

    pass
class ecore_ETypeParameter(ENamedElement):

    pass
class ecore_EPackage(ENamedElement):

    def __init__(self, nsPrefix: str, nsURI: str, EPackage: "ecore_EClassifier" = None, EPackage47: "ecore_EFactory" = None, ePackage: set["ecore_EClassifier"] = None, EPackage81: "ecore_EPackage" = None, eSuperPackage: set["ecore_EPackage"] = None, ePackage83: "ecore_EFactory" = None, EPackage86: "ecore_EPackage" = None, eSubpackages: "ecore_EPackage" = None):
        self.nsPrefix = nsPrefix
        self.nsURI = nsURI
        self.EPackage = EPackage
        self.EPackage47 = EPackage47
        self.ePackage = ePackage if ePackage is not None else set()
        self.EPackage81 = EPackage81
        self.eSuperPackage = eSuperPackage if eSuperPackage is not None else set()
        self.ePackage83 = ePackage83
        self.EPackage86 = EPackage86
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
    def ePackage83(self):
        return self.__ePackage83

    @ePackage83.setter
    def ePackage83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__ePackage83", None)
        self.__ePackage83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFactory"):
                opp_val = getattr(old_value, "EFactory", None)
                if opp_val == self:
                    setattr(old_value, "EFactory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFactory"):
                opp_val = getattr(value, "EFactory", None)
                setattr(value, "EFactory", self)

    @property
    def EPackage86(self):
        return self.__EPackage86

    @EPackage86.setter
    def EPackage86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__EPackage86", None)
        self.__EPackage86 = value
        
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
    def EPackage47(self):
        return self.__EPackage47

    @EPackage47.setter
    def EPackage47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__EPackage47", None)
        self.__EPackage47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eFactoryInstance"):
                opp_val = getattr(old_value, "eFactoryInstance", None)
                if opp_val == self:
                    setattr(old_value, "eFactoryInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eFactoryInstance"):
                opp_val = getattr(value, "eFactoryInstance", None)
                setattr(value, "eFactoryInstance", self)

    @property
    def eSubpackages(self):
        return self.__eSubpackages

    @eSubpackages.setter
    def eSubpackages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__eSubpackages", None)
        self.__eSubpackages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EPackage86"):
                opp_val = getattr(old_value, "EPackage86", None)
                if opp_val == self:
                    setattr(old_value, "EPackage86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EPackage86"):
                opp_val = getattr(value, "EPackage86", None)
                setattr(value, "EPackage86", self)

    @property
    def eSuperPackage(self):
        return self.__eSuperPackage

    @eSuperPackage.setter
    def eSuperPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__eSuperPackage", None)
        self.__eSuperPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EPackage81"):
                    opp_val = getattr(item, "EPackage81", None)
                    
                    if opp_val == self:
                        setattr(item, "EPackage81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EPackage81"):
                    opp_val = getattr(item, "EPackage81", None)
                    
                    setattr(item, "EPackage81", self)
                    

    @property
    def ePackage(self):
        return self.__ePackage

    @ePackage.setter
    def ePackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__ePackage", None)
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
    def EPackage(self):
        return self.__EPackage

    @EPackage.setter
    def EPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__EPackage", None)
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
    def EPackage81(self):
        return self.__EPackage81

    @EPackage81.setter
    def EPackage81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__EPackage81", None)
        self.__EPackage81 = value
        
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

    def getEClassifier(self, name: str) -> EClassifier:
        # TODO: Implement getEClassifier method
        pass

class ecore_ETypedElement(ENamedElement):

    def __init__(self, many: bool, ordered: bool, required: bool, lowerBound: int, unique: bool, upperBound: int, ecore_ETypedElement: "ecore_EGenericType" = None, ecore_ETypedElement103: "ecore_EClassifier" = None):
        self.many = many
        self.ordered = ordered
        self.required = required
        self.lowerBound = lowerBound
        self.unique = unique
        self.upperBound = upperBound
        self.ecore_ETypedElement = ecore_ETypedElement
        self.ecore_ETypedElement103 = ecore_ETypedElement103
        
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
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

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
    def ecore_ETypedElement(self):
        return self.__ecore_ETypedElement

    @ecore_ETypedElement.setter
    def ecore_ETypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_ETypedElement__ecore_ETypedElement", None)
        self.__ecore_ETypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EGenericType101"):
                opp_val = getattr(old_value, "ecore_EGenericType101", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EGenericType101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EGenericType101"):
                opp_val = getattr(value, "ecore_EGenericType101", None)
                setattr(value, "ecore_EGenericType101", self)

    @property
    def ecore_ETypedElement103(self):
        return self.__ecore_ETypedElement103

    @ecore_ETypedElement103.setter
    def ecore_ETypedElement103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_ETypedElement__ecore_ETypedElement103", None)
        self.__ecore_ETypedElement103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClassifier104"):
                opp_val = getattr(old_value, "ecore_EClassifier104", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EClassifier104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClassifier104"):
                opp_val = getattr(value, "ecore_EClassifier104", None)
                setattr(value, "ecore_EClassifier104", self)

class ecore_EEnumLiteral(ENamedElement):

    def __init__(self, instance: str, literal: str, value: int, EEnumLiteral: "ecore_EEnum" = None, eLiterals: "ecore_EEnum" = None):
        self.instance = instance
        self.literal = literal
        self.value = value
        self.EEnumLiteral = EEnumLiteral
        self.eLiterals = eLiterals
        
    @property
    def instance(self) -> str:
        return self.__instance

    @instance.setter
    def instance(self, instance: str):
        self.__instance = instance

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
        old_value = getattr(self, f"_ecore_EEnumLiteral__eLiterals", None)
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
        old_value = getattr(self, f"_ecore_EEnumLiteral__EEnumLiteral", None)
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

class ecore_EClassifier(ENamedElement):

    def __init__(self, instanceClassName: str, instanceTypeName: str, defaultValue: str, instanceClass: str, ecore_EClassifier: set["ecore_ETypeParameter"] = None, eClassifiers: "ecore_EPackage" = None, ecore_EClassifier59: "ecore_EGenericType" = None, ecore_EClassifier62: "ecore_EGenericType" = None, ecore_EClassifier76: "ecore_EOperation" = None, EClassifier: "ecore_EPackage" = None, ecore_EClassifier104: "ecore_ETypedElement" = None):
        self.instanceClassName = instanceClassName
        self.instanceTypeName = instanceTypeName
        self.defaultValue = defaultValue
        self.instanceClass = instanceClass
        self.ecore_EClassifier = ecore_EClassifier if ecore_EClassifier is not None else set()
        self.eClassifiers = eClassifiers
        self.ecore_EClassifier59 = ecore_EClassifier59
        self.ecore_EClassifier62 = ecore_EClassifier62
        self.ecore_EClassifier76 = ecore_EClassifier76
        self.EClassifier = EClassifier
        self.ecore_EClassifier104 = ecore_EClassifier104
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

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
    def instanceClass(self) -> str:
        return self.__instanceClass

    @instanceClass.setter
    def instanceClass(self, instanceClass: str):
        self.__instanceClass = instanceClass

    @property
    def ecore_EClassifier76(self):
        return self.__ecore_EClassifier76

    @ecore_EClassifier76.setter
    def ecore_EClassifier76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier76", None)
        self.__ecore_EClassifier76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EOperation75"):
                opp_val = getattr(old_value, "ecore_EOperation75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EOperation75"):
                opp_val = getattr(value, "ecore_EOperation75", None)
                if opp_val is None:
                    setattr(value, "ecore_EOperation75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EClassifier(self):
        return self.__ecore_EClassifier

    @ecore_EClassifier.setter
    def ecore_EClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier", None)
        self.__ecore_EClassifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_ETypeParameter"):
                    opp_val = getattr(item, "ecore_ETypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_ETypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_ETypeParameter"):
                    opp_val = getattr(item, "ecore_ETypeParameter", None)
                    
                    setattr(item, "ecore_ETypeParameter", self)
                    

    @property
    def ecore_EClassifier62(self):
        return self.__ecore_EClassifier62

    @ecore_EClassifier62.setter
    def ecore_EClassifier62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier62", None)
        self.__ecore_EClassifier62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EGenericType61"):
                opp_val = getattr(old_value, "ecore_EGenericType61", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EGenericType61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EGenericType61"):
                opp_val = getattr(value, "ecore_EGenericType61", None)
                setattr(value, "ecore_EGenericType61", self)

    @property
    def ecore_EClassifier59(self):
        return self.__ecore_EClassifier59

    @ecore_EClassifier59.setter
    def ecore_EClassifier59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier59", None)
        self.__ecore_EClassifier59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EGenericType58"):
                opp_val = getattr(old_value, "ecore_EGenericType58", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EGenericType58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EGenericType58"):
                opp_val = getattr(value, "ecore_EGenericType58", None)
                setattr(value, "ecore_EGenericType58", self)

    @property
    def EClassifier(self):
        return self.__EClassifier

    @EClassifier.setter
    def EClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__EClassifier", None)
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
    def ecore_EClassifier104(self):
        return self.__ecore_EClassifier104

    @ecore_EClassifier104.setter
    def ecore_EClassifier104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier104", None)
        self.__ecore_EClassifier104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_ETypedElement103"):
                opp_val = getattr(old_value, "ecore_ETypedElement103", None)
                if opp_val == self:
                    setattr(old_value, "ecore_ETypedElement103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_ETypedElement103"):
                opp_val = getattr(value, "ecore_ETypedElement103", None)
                setattr(value, "ecore_ETypedElement103", self)

    @property
    def eClassifiers(self):
        return self.__eClassifiers

    @eClassifiers.setter
    def eClassifiers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__eClassifiers", None)
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

    def isInstance(self, object: str) -> bool:
        # TODO: Implement isInstance method
        pass

    def getClassifierID(self) -> int:
        # TODO: Implement getClassifierID method
        pass

class ecore_EGenericType(EObject):

    pass
class ecore_EStructuralFeature(ETypedElement):

    def __init__(self, changeable: bool, defaultValue: str, defaultValueLiteral: str, derived: bool, transient: bool, unsettable: bool, volatile: bool, EStructuralFeature: "ecore_EClass" = None, ecore_EStructuralFeature: "ecore_EClass" = None, eStructuralFeatures: "ecore_EClass" = None):
        self.changeable = changeable
        self.defaultValue = defaultValue
        self.defaultValueLiteral = defaultValueLiteral
        self.derived = derived
        self.transient = transient
        self.unsettable = unsettable
        self.volatile = volatile
        self.EStructuralFeature = EStructuralFeature
        self.ecore_EStructuralFeature = ecore_EStructuralFeature
        self.eStructuralFeatures = eStructuralFeatures
        
    @property
    def unsettable(self) -> bool:
        return self.__unsettable

    @unsettable.setter
    def unsettable(self, unsettable: bool):
        self.__unsettable = unsettable

    @property
    def defaultValueLiteral(self) -> str:
        return self.__defaultValueLiteral

    @defaultValueLiteral.setter
    def defaultValueLiteral(self, defaultValueLiteral: str):
        self.__defaultValueLiteral = defaultValueLiteral

    @property
    def changeable(self) -> bool:
        return self.__changeable

    @changeable.setter
    def changeable(self, changeable: bool):
        self.__changeable = changeable

    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def volatile(self) -> bool:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: bool):
        self.__volatile = volatile

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def ecore_EStructuralFeature(self):
        return self.__ecore_EStructuralFeature

    @ecore_EStructuralFeature.setter
    def ecore_EStructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EStructuralFeature__ecore_EStructuralFeature", None)
        self.__ecore_EStructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass26"):
                opp_val = getattr(old_value, "ecore_EClass26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass26"):
                opp_val = getattr(value, "ecore_EClass26", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eStructuralFeatures(self):
        return self.__eStructuralFeatures

    @eStructuralFeatures.setter
    def eStructuralFeatures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EStructuralFeature__eStructuralFeatures", None)
        self.__eStructuralFeatures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EClass99"):
                opp_val = getattr(old_value, "EClass99", None)
                if opp_val == self:
                    setattr(old_value, "EClass99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EClass99"):
                opp_val = getattr(value, "EClass99", None)
                setattr(value, "EClass99", self)

    @property
    def EStructuralFeature(self):
        return self.__EStructuralFeature

    @EStructuralFeature.setter
    def EStructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EStructuralFeature__EStructuralFeature", None)
        self.__EStructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eContainingClass10"):
                opp_val = getattr(old_value, "eContainingClass10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eContainingClass10"):
                opp_val = getattr(value, "eContainingClass10", None)
                if opp_val is None:
                    setattr(value, "eContainingClass10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getContainerClass(self):
        # TODO: Implement getContainerClass method
        pass

    def getFeatureID(self) -> int:
        # TODO: Implement getFeatureID method
        pass

class ecore_EOperation(ETypedElement):

    pass
class EClassifier:

    pass
class ecore_EClass(EClassifier):

    def __init__(self, abstract: bool, interface: bool, ecore_EClass13: set["ecore_EAttribute"] = None, ecore_EClass16: set["ecore_EReference"] = None, eContainingClass: set["ecore_EOperation"] = None, eContainingClass10: set["ecore_EStructuralFeature"] = None, ecore_EClass: set["ecore_EGenericType"] = None, ecore_EClass29: "ecore_EClass" = None, ecore_EClass27: set["ecore_EClass"] = None, ecore_EClass18: set["ecore_EGenericType"] = None, ecore_EClass21: set["ecore_EOperation"] = None, ecore_EClass23: set["ecore_EReference"] = None, ecore_EClass26: set["ecore_EStructuralFeature"] = None, ecore_EClass31: set["ecore_EAttribute"] = None, ecore_EClass34: "ecore_EAttribute" = None, ecore_EClass37: set["ecore_EReference"] = None, ecore_EClass41: "ecore_EClass" = None, ecore_EClass39: set["ecore_EClass"] = None, EClass: "ecore_EOperation" = None, ecore_EClass97: "ecore_EReference" = None, EClass99: "ecore_EStructuralFeature" = None):
        self.abstract = abstract
        self.interface = interface
        self.ecore_EClass13 = ecore_EClass13 if ecore_EClass13 is not None else set()
        self.ecore_EClass16 = ecore_EClass16 if ecore_EClass16 is not None else set()
        self.eContainingClass = eContainingClass if eContainingClass is not None else set()
        self.eContainingClass10 = eContainingClass10 if eContainingClass10 is not None else set()
        self.ecore_EClass = ecore_EClass if ecore_EClass is not None else set()
        self.ecore_EClass29 = ecore_EClass29
        self.ecore_EClass27 = ecore_EClass27 if ecore_EClass27 is not None else set()
        self.ecore_EClass18 = ecore_EClass18 if ecore_EClass18 is not None else set()
        self.ecore_EClass21 = ecore_EClass21 if ecore_EClass21 is not None else set()
        self.ecore_EClass23 = ecore_EClass23 if ecore_EClass23 is not None else set()
        self.ecore_EClass26 = ecore_EClass26 if ecore_EClass26 is not None else set()
        self.ecore_EClass31 = ecore_EClass31 if ecore_EClass31 is not None else set()
        self.ecore_EClass34 = ecore_EClass34
        self.ecore_EClass37 = ecore_EClass37 if ecore_EClass37 is not None else set()
        self.ecore_EClass41 = ecore_EClass41
        self.ecore_EClass39 = ecore_EClass39 if ecore_EClass39 is not None else set()
        self.EClass = EClass
        self.ecore_EClass97 = ecore_EClass97
        self.EClass99 = EClass99
        
    @property
    def interface(self) -> bool:
        return self.__interface

    @interface.setter
    def interface(self, interface: bool):
        self.__interface = interface

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def EClass(self):
        return self.__EClass

    @EClass.setter
    def EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__EClass", None)
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
    def eContainingClass(self):
        return self.__eContainingClass

    @eContainingClass.setter
    def eContainingClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__eContainingClass", None)
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
    def ecore_EClass31(self):
        return self.__ecore_EClass31

    @ecore_EClass31.setter
    def ecore_EClass31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass31", None)
        self.__ecore_EClass31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EAttribute32"):
                    opp_val = getattr(item, "ecore_EAttribute32", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EAttribute32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EAttribute32"):
                    opp_val = getattr(item, "ecore_EAttribute32", None)
                    
                    setattr(item, "ecore_EAttribute32", self)
                    

    @property
    def ecore_EClass18(self):
        return self.__ecore_EClass18

    @ecore_EClass18.setter
    def ecore_EClass18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass18", None)
        self.__ecore_EClass18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EGenericType19"):
                    opp_val = getattr(item, "ecore_EGenericType19", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EGenericType19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EGenericType19"):
                    opp_val = getattr(item, "ecore_EGenericType19", None)
                    
                    setattr(item, "ecore_EGenericType19", self)
                    

    @property
    def ecore_EClass41(self):
        return self.__ecore_EClass41

    @ecore_EClass41.setter
    def ecore_EClass41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass41", None)
        self.__ecore_EClass41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass39"):
                opp_val = getattr(old_value, "ecore_EClass39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass39"):
                opp_val = getattr(value, "ecore_EClass39", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EClass13(self):
        return self.__ecore_EClass13

    @ecore_EClass13.setter
    def ecore_EClass13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass13", None)
        self.__ecore_EClass13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EAttribute14"):
                    opp_val = getattr(item, "ecore_EAttribute14", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EAttribute14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EAttribute14"):
                    opp_val = getattr(item, "ecore_EAttribute14", None)
                    
                    setattr(item, "ecore_EAttribute14", self)
                    

    @property
    def ecore_EClass97(self):
        return self.__ecore_EClass97

    @ecore_EClass97.setter
    def ecore_EClass97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass97", None)
        self.__ecore_EClass97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EReference96"):
                opp_val = getattr(old_value, "ecore_EReference96", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EReference96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EReference96"):
                opp_val = getattr(value, "ecore_EReference96", None)
                setattr(value, "ecore_EReference96", self)

    @property
    def ecore_EClass29(self):
        return self.__ecore_EClass29

    @ecore_EClass29.setter
    def ecore_EClass29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass29", None)
        self.__ecore_EClass29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass27"):
                opp_val = getattr(old_value, "ecore_EClass27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass27"):
                opp_val = getattr(value, "ecore_EClass27", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EClass34(self):
        return self.__ecore_EClass34

    @ecore_EClass34.setter
    def ecore_EClass34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass34", None)
        self.__ecore_EClass34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EAttribute35"):
                opp_val = getattr(old_value, "ecore_EAttribute35", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EAttribute35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EAttribute35"):
                opp_val = getattr(value, "ecore_EAttribute35", None)
                setattr(value, "ecore_EAttribute35", self)

    @property
    def EClass99(self):
        return self.__EClass99

    @EClass99.setter
    def EClass99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__EClass99", None)
        self.__EClass99 = value
        
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

    @property
    def ecore_EClass(self):
        return self.__ecore_EClass

    @ecore_EClass.setter
    def ecore_EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass", None)
        self.__ecore_EClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EGenericType"):
                    opp_val = getattr(item, "ecore_EGenericType", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EGenericType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EGenericType"):
                    opp_val = getattr(item, "ecore_EGenericType", None)
                    
                    setattr(item, "ecore_EGenericType", self)
                    

    @property
    def ecore_EClass26(self):
        return self.__ecore_EClass26

    @ecore_EClass26.setter
    def ecore_EClass26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass26", None)
        self.__ecore_EClass26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EStructuralFeature"):
                    opp_val = getattr(item, "ecore_EStructuralFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EStructuralFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EStructuralFeature"):
                    opp_val = getattr(item, "ecore_EStructuralFeature", None)
                    
                    setattr(item, "ecore_EStructuralFeature", self)
                    

    @property
    def ecore_EClass39(self):
        return self.__ecore_EClass39

    @ecore_EClass39.setter
    def ecore_EClass39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass39", None)
        self.__ecore_EClass39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EClass41"):
                    opp_val = getattr(item, "ecore_EClass41", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EClass41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EClass41"):
                    opp_val = getattr(item, "ecore_EClass41", None)
                    
                    setattr(item, "ecore_EClass41", self)
                    

    @property
    def ecore_EClass23(self):
        return self.__ecore_EClass23

    @ecore_EClass23.setter
    def ecore_EClass23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass23", None)
        self.__ecore_EClass23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EReference24"):
                    opp_val = getattr(item, "ecore_EReference24", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EReference24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EReference24"):
                    opp_val = getattr(item, "ecore_EReference24", None)
                    
                    setattr(item, "ecore_EReference24", self)
                    

    @property
    def ecore_EClass21(self):
        return self.__ecore_EClass21

    @ecore_EClass21.setter
    def ecore_EClass21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass21", None)
        self.__ecore_EClass21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EOperation"):
                    opp_val = getattr(item, "ecore_EOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EOperation"):
                    opp_val = getattr(item, "ecore_EOperation", None)
                    
                    setattr(item, "ecore_EOperation", self)
                    

    @property
    def ecore_EClass37(self):
        return self.__ecore_EClass37

    @ecore_EClass37.setter
    def ecore_EClass37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass37", None)
        self.__ecore_EClass37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EReference38"):
                    opp_val = getattr(item, "ecore_EReference38", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EReference38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EReference38"):
                    opp_val = getattr(item, "ecore_EReference38", None)
                    
                    setattr(item, "ecore_EReference38", self)
                    

    @property
    def eContainingClass10(self):
        return self.__eContainingClass10

    @eContainingClass10.setter
    def eContainingClass10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__eContainingClass10", None)
        self.__eContainingClass10 = value if value is not None else set()
        
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
    def ecore_EClass27(self):
        return self.__ecore_EClass27

    @ecore_EClass27.setter
    def ecore_EClass27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass27", None)
        self.__ecore_EClass27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EClass29"):
                    opp_val = getattr(item, "ecore_EClass29", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EClass29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EClass29"):
                    opp_val = getattr(item, "ecore_EClass29", None)
                    
                    setattr(item, "ecore_EClass29", self)
                    

    @property
    def ecore_EClass16(self):
        return self.__ecore_EClass16

    @ecore_EClass16.setter
    def ecore_EClass16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass16", None)
        self.__ecore_EClass16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EReference"):
                    opp_val = getattr(item, "ecore_EReference", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EReference"):
                    opp_val = getattr(item, "ecore_EReference", None)
                    
                    setattr(item, "ecore_EReference", self)
                    

    def getFeatureCount(self) -> int:
        # TODO: Implement getFeatureCount method
        pass

    def getEStructuralFeature(self, featureID: int) -> EStructuralFeature:
        # TODO: Implement getEStructuralFeature method
        pass

    def isSuperTypeOf(self, someClass: str) -> bool:
        # TODO: Implement isSuperTypeOf method
        pass

    def getEStructuralFeature(self, featureName: str) -> EStructuralFeature:
        # TODO: Implement getEStructuralFeature method
        pass

    def getFeatureID(self, feature: EStructuralFeature) -> int:
        # TODO: Implement getFeatureID method
        pass

class ecore_EDataType(EClassifier):

    def __init__(self, serializable: bool, ecore_EDataType: "ecore_EAttribute" = None):
        self.serializable = serializable
        self.ecore_EDataType = ecore_EDataType
        
    @property
    def serializable(self) -> bool:
        return self.__serializable

    @serializable.setter
    def serializable(self, serializable: bool):
        self.__serializable = serializable

    @property
    def ecore_EDataType(self):
        return self.__ecore_EDataType

    @ecore_EDataType.setter
    def ecore_EDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EDataType__ecore_EDataType", None)
        self.__ecore_EDataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EAttribute"):
                opp_val = getattr(old_value, "ecore_EAttribute", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EAttribute"):
                opp_val = getattr(value, "ecore_EAttribute", None)
                setattr(value, "ecore_EAttribute", self)

class EStructuralFeature:

    pass
class ecore_EReference(EStructuralFeature):

    def __init__(self, containment: bool, container: bool, resolveProxies: bool, ecore_EReference: "ecore_EClass" = None, ecore_EReference24: "ecore_EClass" = None, ecore_EReference38: "ecore_EClass" = None, ecore_EReference90: set["ecore_EAttribute"] = None, ecore_EReference94: "ecore_EReference" = None, ecore_EReference92: "ecore_EReference" = None, ecore_EReference96: "ecore_EClass" = None):
        self.containment = containment
        self.container = container
        self.resolveProxies = resolveProxies
        self.ecore_EReference = ecore_EReference
        self.ecore_EReference24 = ecore_EReference24
        self.ecore_EReference38 = ecore_EReference38
        self.ecore_EReference90 = ecore_EReference90 if ecore_EReference90 is not None else set()
        self.ecore_EReference94 = ecore_EReference94
        self.ecore_EReference92 = ecore_EReference92
        self.ecore_EReference96 = ecore_EReference96
        
    @property
    def resolveProxies(self) -> bool:
        return self.__resolveProxies

    @resolveProxies.setter
    def resolveProxies(self, resolveProxies: bool):
        self.__resolveProxies = resolveProxies

    @property
    def container(self) -> bool:
        return self.__container

    @container.setter
    def container(self, container: bool):
        self.__container = container

    @property
    def containment(self) -> bool:
        return self.__containment

    @containment.setter
    def containment(self, containment: bool):
        self.__containment = containment

    @property
    def ecore_EReference24(self):
        return self.__ecore_EReference24

    @ecore_EReference24.setter
    def ecore_EReference24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference24", None)
        self.__ecore_EReference24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass23"):
                opp_val = getattr(old_value, "ecore_EClass23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass23"):
                opp_val = getattr(value, "ecore_EClass23", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EReference92(self):
        return self.__ecore_EReference92

    @ecore_EReference92.setter
    def ecore_EReference92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference92", None)
        self.__ecore_EReference92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EReference94"):
                opp_val = getattr(old_value, "ecore_EReference94", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EReference94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EReference94"):
                opp_val = getattr(value, "ecore_EReference94", None)
                setattr(value, "ecore_EReference94", self)

    @property
    def ecore_EReference96(self):
        return self.__ecore_EReference96

    @ecore_EReference96.setter
    def ecore_EReference96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference96", None)
        self.__ecore_EReference96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass97"):
                opp_val = getattr(old_value, "ecore_EClass97", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EClass97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass97"):
                opp_val = getattr(value, "ecore_EClass97", None)
                setattr(value, "ecore_EClass97", self)

    @property
    def ecore_EReference(self):
        return self.__ecore_EReference

    @ecore_EReference.setter
    def ecore_EReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference", None)
        self.__ecore_EReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass16"):
                opp_val = getattr(old_value, "ecore_EClass16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass16"):
                opp_val = getattr(value, "ecore_EClass16", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EReference38(self):
        return self.__ecore_EReference38

    @ecore_EReference38.setter
    def ecore_EReference38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference38", None)
        self.__ecore_EReference38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass37"):
                opp_val = getattr(old_value, "ecore_EClass37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass37"):
                opp_val = getattr(value, "ecore_EClass37", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EReference90(self):
        return self.__ecore_EReference90

    @ecore_EReference90.setter
    def ecore_EReference90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference90", None)
        self.__ecore_EReference90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EAttribute91"):
                    opp_val = getattr(item, "ecore_EAttribute91", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EAttribute91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EAttribute91"):
                    opp_val = getattr(item, "ecore_EAttribute91", None)
                    
                    setattr(item, "ecore_EAttribute91", self)
                    

    @property
    def ecore_EReference94(self):
        return self.__ecore_EReference94

    @ecore_EReference94.setter
    def ecore_EReference94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference94", None)
        self.__ecore_EReference94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EReference92"):
                opp_val = getattr(old_value, "ecore_EReference92", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EReference92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EReference92"):
                opp_val = getattr(value, "ecore_EReference92", None)
                setattr(value, "ecore_EReference92", self)

class ecore_EAttribute(EStructuralFeature):

    def __init__(self, iD: bool, ecore_EAttribute: "ecore_EDataType" = None, ecore_EAttribute14: "ecore_EClass" = None, ecore_EAttribute32: "ecore_EClass" = None, ecore_EAttribute35: "ecore_EClass" = None, ecore_EAttribute91: "ecore_EReference" = None):
        self.iD = iD
        self.ecore_EAttribute = ecore_EAttribute
        self.ecore_EAttribute14 = ecore_EAttribute14
        self.ecore_EAttribute32 = ecore_EAttribute32
        self.ecore_EAttribute35 = ecore_EAttribute35
        self.ecore_EAttribute91 = ecore_EAttribute91
        
    @property
    def iD(self) -> bool:
        return self.__iD

    @iD.setter
    def iD(self, iD: bool):
        self.__iD = iD

    @property
    def ecore_EAttribute32(self):
        return self.__ecore_EAttribute32

    @ecore_EAttribute32.setter
    def ecore_EAttribute32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAttribute__ecore_EAttribute32", None)
        self.__ecore_EAttribute32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass31"):
                opp_val = getattr(old_value, "ecore_EClass31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass31"):
                opp_val = getattr(value, "ecore_EClass31", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EAttribute14(self):
        return self.__ecore_EAttribute14

    @ecore_EAttribute14.setter
    def ecore_EAttribute14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAttribute__ecore_EAttribute14", None)
        self.__ecore_EAttribute14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass13"):
                opp_val = getattr(old_value, "ecore_EClass13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass13"):
                opp_val = getattr(value, "ecore_EClass13", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EAttribute(self):
        return self.__ecore_EAttribute

    @ecore_EAttribute.setter
    def ecore_EAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAttribute__ecore_EAttribute", None)
        self.__ecore_EAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EDataType"):
                opp_val = getattr(old_value, "ecore_EDataType", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EDataType"):
                opp_val = getattr(value, "ecore_EDataType", None)
                setattr(value, "ecore_EDataType", self)

    @property
    def ecore_EAttribute91(self):
        return self.__ecore_EAttribute91

    @ecore_EAttribute91.setter
    def ecore_EAttribute91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAttribute__ecore_EAttribute91", None)
        self.__ecore_EAttribute91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EReference90"):
                opp_val = getattr(old_value, "ecore_EReference90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EReference90"):
                opp_val = getattr(value, "ecore_EReference90", None)
                if opp_val is None:
                    setattr(value, "ecore_EReference90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EAttribute35(self):
        return self.__ecore_EAttribute35

    @ecore_EAttribute35.setter
    def ecore_EAttribute35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAttribute__ecore_EAttribute35", None)
        self.__ecore_EAttribute35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass34"):
                opp_val = getattr(old_value, "ecore_EClass34", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EClass34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass34"):
                opp_val = getattr(value, "ecore_EClass34", None)
                setattr(value, "ecore_EClass34", self)

class ecore_EObject:

    def __init__(self, ecore_EObject: "ecore_EAnnotation" = None, ecore_EObject5: "ecore_EAnnotation" = None):
        self.ecore_EObject = ecore_EObject
        self.ecore_EObject5 = ecore_EObject5
        
    @property
    def ecore_EObject(self):
        return self.__ecore_EObject

    @ecore_EObject.setter
    def ecore_EObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EObject__ecore_EObject", None)
        self.__ecore_EObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EAnnotation2"):
                opp_val = getattr(old_value, "ecore_EAnnotation2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EAnnotation2"):
                opp_val = getattr(value, "ecore_EAnnotation2", None)
                if opp_val is None:
                    setattr(value, "ecore_EAnnotation2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EObject5(self):
        return self.__ecore_EObject5

    @ecore_EObject5.setter
    def ecore_EObject5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EObject__ecore_EObject5", None)
        self.__ecore_EObject5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EAnnotation4"):
                opp_val = getattr(old_value, "ecore_EAnnotation4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EAnnotation4"):
                opp_val = getattr(value, "ecore_EAnnotation4", None)
                if opp_val is None:
                    setattr(value, "ecore_EAnnotation4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def eGet(self, feature: EStructuralFeature) -> str:
        # TODO: Implement eGet method
        pass

    def eCrossReferences(self):
        # TODO: Implement eCrossReferences method
        pass

    def eIsSet(self, feature: EStructuralFeature) -> bool:
        # TODO: Implement eIsSet method
        pass

    def eClass(self) -> str:
        # TODO: Implement eClass method
        pass

    def eContainer(self) -> EObject:
        # TODO: Implement eContainer method
        pass

    def eResource(self) -> str:
        # TODO: Implement eResource method
        pass

    def eContents(self):
        # TODO: Implement eContents method
        pass

    def eAllContents(self):
        # TODO: Implement eAllContents method
        pass

    def eContainingFeature(self) -> EStructuralFeature:
        # TODO: Implement eContainingFeature method
        pass

    def eGet(self, resolve: bool, feature: EStructuralFeature) -> str:
        # TODO: Implement eGet method
        pass

    def eSet(self, feature: EStructuralFeature, newValue: str):
        # TODO: Implement eSet method
        pass

    def eUnset(self, feature: EStructuralFeature):
        # TODO: Implement eUnset method
        pass

    def eContainmentFeature(self) -> str:
        # TODO: Implement eContainmentFeature method
        pass

    def eIsProxy(self) -> bool:
        # TODO: Implement eIsProxy method
        pass

class ecore_EStringToStringMapEntry:

    def __init__(self, key: str, value: str, ecore_EStringToStringMapEntry: "ecore_EAnnotation" = None):
        self.key = key
        self.value = value
        self.ecore_EStringToStringMapEntry = ecore_EStringToStringMapEntry
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def ecore_EStringToStringMapEntry(self):
        return self.__ecore_EStringToStringMapEntry

    @ecore_EStringToStringMapEntry.setter
    def ecore_EStringToStringMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EStringToStringMapEntry__ecore_EStringToStringMapEntry", None)
        self.__ecore_EStringToStringMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EAnnotation"):
                opp_val = getattr(old_value, "ecore_EAnnotation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EAnnotation"):
                opp_val = getattr(value, "ecore_EAnnotation", None)
                if opp_val is None:
                    setattr(value, "ecore_EAnnotation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EModelElement:

    pass
class ecore_EFactory(EModelElement):

    def __init__(self, eFactoryInstance: "ecore_EPackage" = None, EFactory: "ecore_EPackage" = None):
        self.eFactoryInstance = eFactoryInstance
        self.EFactory = EFactory
        
    @property
    def EFactory(self):
        return self.__EFactory

    @EFactory.setter
    def EFactory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EFactory__EFactory", None)
        self.__EFactory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ePackage83"):
                opp_val = getattr(old_value, "ePackage83", None)
                if opp_val == self:
                    setattr(old_value, "ePackage83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ePackage83"):
                opp_val = getattr(value, "ePackage83", None)
                setattr(value, "ePackage83", self)

    @property
    def eFactoryInstance(self):
        return self.__eFactoryInstance

    @eFactoryInstance.setter
    def eFactoryInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EFactory__eFactoryInstance", None)
        self.__eFactoryInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EPackage47"):
                opp_val = getattr(old_value, "EPackage47", None)
                if opp_val == self:
                    setattr(old_value, "EPackage47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EPackage47"):
                opp_val = getattr(value, "EPackage47", None)
                setattr(value, "EPackage47", self)

    def convertToString(self, eDataType: EDataType, instanceValue: str) -> str:
        # TODO: Implement convertToString method
        pass

    def createFromString(self, eDataType: EDataType, literalValue: str) -> str:
        # TODO: Implement createFromString method
        pass

    def create(self, eClass: str) -> str:
        # TODO: Implement create method
        pass

class ecore_ENamedElement(EModelElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ecore_EAnnotation(EModelElement):

    def __init__(self, source: str, eAnnotations: "ecore_EModelElement" = None, ecore_EAnnotation: set["ecore_EStringToStringMapEntry"] = None, ecore_EAnnotation2: set["ecore_EObject"] = None, ecore_EAnnotation4: set["ecore_EObject"] = None, EAnnotation: "ecore_EModelElement" = None):
        self.source = source
        self.eAnnotations = eAnnotations
        self.ecore_EAnnotation = ecore_EAnnotation if ecore_EAnnotation is not None else set()
        self.ecore_EAnnotation2 = ecore_EAnnotation2 if ecore_EAnnotation2 is not None else set()
        self.ecore_EAnnotation4 = ecore_EAnnotation4 if ecore_EAnnotation4 is not None else set()
        self.EAnnotation = EAnnotation
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def ecore_EAnnotation2(self):
        return self.__ecore_EAnnotation2

    @ecore_EAnnotation2.setter
    def ecore_EAnnotation2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAnnotation__ecore_EAnnotation2", None)
        self.__ecore_EAnnotation2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EObject"):
                    opp_val = getattr(item, "ecore_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EObject"):
                    opp_val = getattr(item, "ecore_EObject", None)
                    
                    setattr(item, "ecore_EObject", self)
                    

    @property
    def eAnnotations(self):
        return self.__eAnnotations

    @eAnnotations.setter
    def eAnnotations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAnnotation__eAnnotations", None)
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
    def ecore_EAnnotation(self):
        return self.__ecore_EAnnotation

    @ecore_EAnnotation.setter
    def ecore_EAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAnnotation__ecore_EAnnotation", None)
        self.__ecore_EAnnotation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EStringToStringMapEntry"):
                    opp_val = getattr(item, "ecore_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EStringToStringMapEntry"):
                    opp_val = getattr(item, "ecore_EStringToStringMapEntry", None)
                    
                    setattr(item, "ecore_EStringToStringMapEntry", self)
                    

    @property
    def EAnnotation(self):
        return self.__EAnnotation

    @EAnnotation.setter
    def EAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAnnotation__EAnnotation", None)
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

    @property
    def ecore_EAnnotation4(self):
        return self.__ecore_EAnnotation4

    @ecore_EAnnotation4.setter
    def ecore_EAnnotation4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAnnotation__ecore_EAnnotation4", None)
        self.__ecore_EAnnotation4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EObject5"):
                    opp_val = getattr(item, "ecore_EObject5", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EObject5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EObject5"):
                    opp_val = getattr(item, "ecore_EObject5", None)
                    
                    setattr(item, "ecore_EObject5", self)
                    

class ecore_EModelElement(EObject):

    def __init__(self, EModelElement: "ecore_EAnnotation" = None, eModelElement: set["ecore_EAnnotation"] = None):
        self.EModelElement = EModelElement
        self.eModelElement = eModelElement if eModelElement is not None else set()
        
    @property
    def EModelElement(self):
        return self.__EModelElement

    @EModelElement.setter
    def EModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EModelElement__EModelElement", None)
        self.__EModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eAnnotations"):
                opp_val = getattr(old_value, "eAnnotations", None)
                if opp_val == self:
                    setattr(old_value, "eAnnotations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eAnnotations"):
                opp_val = getattr(value, "eAnnotations", None)
                setattr(value, "eAnnotations", self)

    @property
    def eModelElement(self):
        return self.__eModelElement

    @eModelElement.setter
    def eModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EModelElement__eModelElement", None)
        self.__eModelElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EAnnotation"):
                    opp_val = getattr(item, "EAnnotation", None)
                    
                    if opp_val == self:
                        setattr(item, "EAnnotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EAnnotation"):
                    opp_val = getattr(item, "EAnnotation", None)
                    
                    setattr(item, "EAnnotation", self)
                    

    def getEAnnotation(self, source: str) -> str:
        # TODO: Implement getEAnnotation method
        pass
