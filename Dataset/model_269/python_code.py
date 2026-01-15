from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ETypedElement:

    pass
class javaless_EParameter(ETypedElement):

    pass
class EObject:

    pass
class EDataType:

    pass
class javaless_EEnum(EDataType):

    def __init__(self, eEnum: set["javaless_EEnumLiteral"] = None, EEnum: "javaless_EEnumLiteral" = None):
        self.eEnum = eEnum if eEnum is not None else set()
        self.EEnum = EEnum
        
    @property
    def EEnum(self):
        return self.__EEnum

    @EEnum.setter
    def EEnum(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EEnum__EEnum", None)
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
        old_value = getattr(self, f"_javaless_EEnum__eEnum", None)
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
                    

    def getEEnumLiteral(self, name: str) -> str:
        # TODO: Implement getEEnumLiteral method
        pass

    def getEEnumLiteralByLiteral(self, literal: str) -> str:
        # TODO: Implement getEEnumLiteralByLiteral method
        pass

    def getEEnumLiteral(self, value: int) -> str:
        # TODO: Implement getEEnumLiteral method
        pass

class javaless_EStructuralFeature(ETypedElement):

    def __init__(self, changeable: bool, volatile: bool, transient: bool, defaultValueLiteral: str, defaultValue: str, unsettable: bool, derived: bool, EStructuralFeature: "javaless_EClass" = None, javaless_EStructuralFeature: "javaless_EClass" = None, eStructuralFeatures: "javaless_EClass" = None):
        self.changeable = changeable
        self.volatile = volatile
        self.transient = transient
        self.defaultValueLiteral = defaultValueLiteral
        self.defaultValue = defaultValue
        self.unsettable = unsettable
        self.derived = derived
        self.EStructuralFeature = EStructuralFeature
        self.javaless_EStructuralFeature = javaless_EStructuralFeature
        self.eStructuralFeatures = eStructuralFeatures
        
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
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def unsettable(self) -> bool:
        return self.__unsettable

    @unsettable.setter
    def unsettable(self, unsettable: bool):
        self.__unsettable = unsettable

    @property
    def volatile(self) -> bool:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: bool):
        self.__volatile = volatile

    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def javaless_EStructuralFeature(self):
        return self.__javaless_EStructuralFeature

    @javaless_EStructuralFeature.setter
    def javaless_EStructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EStructuralFeature__javaless_EStructuralFeature", None)
        self.__javaless_EStructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_EClass28"):
                opp_val = getattr(old_value, "javaless_EClass28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_EClass28"):
                opp_val = getattr(value, "javaless_EClass28", None)
                if opp_val is None:
                    setattr(value, "javaless_EClass28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eStructuralFeatures(self):
        return self.__eStructuralFeatures

    @eStructuralFeatures.setter
    def eStructuralFeatures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EStructuralFeature__eStructuralFeatures", None)
        self.__eStructuralFeatures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EClass65"):
                opp_val = getattr(old_value, "EClass65", None)
                if opp_val == self:
                    setattr(old_value, "EClass65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EClass65"):
                opp_val = getattr(value, "EClass65", None)
                setattr(value, "EClass65", self)

    @property
    def EStructuralFeature(self):
        return self.__EStructuralFeature

    @EStructuralFeature.setter
    def EStructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EStructuralFeature__EStructuralFeature", None)
        self.__EStructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eContainingClass36"):
                opp_val = getattr(old_value, "eContainingClass36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eContainingClass36"):
                opp_val = getattr(value, "eContainingClass36", None)
                if opp_val is None:
                    setattr(value, "eContainingClass36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getFeatureID(self) -> int:
        # TODO: Implement getFeatureID method
        pass

    def getContainerClass(self) -> str:
        # TODO: Implement getContainerClass method
        pass

class ENamedElement:

    pass
class javaless_EEnumLiteral(ENamedElement):

    def __init__(self, value: int, instance: str, literal: str, EEnumLiteral: "javaless_EEnum" = None, eLiterals: "javaless_EEnum" = None):
        self.value = value
        self.instance = instance
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
    def instance(self) -> str:
        return self.__instance

    @instance.setter
    def instance(self, instance: str):
        self.__instance = instance

    @property
    def EEnumLiteral(self):
        return self.__EEnumLiteral

    @EEnumLiteral.setter
    def EEnumLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EEnumLiteral__EEnumLiteral", None)
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

    @property
    def eLiterals(self):
        return self.__eLiterals

    @eLiterals.setter
    def eLiterals(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EEnumLiteral__eLiterals", None)
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

class javaless_EPackage(ENamedElement):

    def __init__(self, nsURI: str, nsPrefix: str, EPackage: "javaless_EClassifier" = None, EPackage41: "javaless_EFactory" = None, ePackage49: set["javaless_EClassifier"] = None, EPackage52: "javaless_EPackage" = None, eSuperPackage: set["javaless_EPackage"] = None, EPackage55: "javaless_EPackage" = None, eSubpackages: "javaless_EPackage" = None, ePackage: "javaless_EFactory" = None):
        self.nsURI = nsURI
        self.nsPrefix = nsPrefix
        self.EPackage = EPackage
        self.EPackage41 = EPackage41
        self.ePackage49 = ePackage49 if ePackage49 is not None else set()
        self.EPackage52 = EPackage52
        self.eSuperPackage = eSuperPackage if eSuperPackage is not None else set()
        self.EPackage55 = EPackage55
        self.eSubpackages = eSubpackages
        self.ePackage = ePackage
        
    @property
    def nsURI(self) -> str:
        return self.__nsURI

    @nsURI.setter
    def nsURI(self, nsURI: str):
        self.__nsURI = nsURI

    @property
    def nsPrefix(self) -> str:
        return self.__nsPrefix

    @nsPrefix.setter
    def nsPrefix(self, nsPrefix: str):
        self.__nsPrefix = nsPrefix

    @property
    def EPackage55(self):
        return self.__EPackage55

    @EPackage55.setter
    def EPackage55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EPackage__EPackage55", None)
        self.__EPackage55 = value
        
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
    def ePackage(self):
        return self.__ePackage

    @ePackage.setter
    def ePackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EPackage__ePackage", None)
        self.__ePackage = value
        
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
    def EPackage52(self):
        return self.__EPackage52

    @EPackage52.setter
    def EPackage52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EPackage__EPackage52", None)
        self.__EPackage52 = value
        
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
    def EPackage(self):
        return self.__EPackage

    @EPackage.setter
    def EPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EPackage__EPackage", None)
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
    def ePackage49(self):
        return self.__ePackage49

    @ePackage49.setter
    def ePackage49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EPackage__ePackage49", None)
        self.__ePackage49 = value if value is not None else set()
        
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
    def eSuperPackage(self):
        return self.__eSuperPackage

    @eSuperPackage.setter
    def eSuperPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EPackage__eSuperPackage", None)
        self.__eSuperPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EPackage52"):
                    opp_val = getattr(item, "EPackage52", None)
                    
                    if opp_val == self:
                        setattr(item, "EPackage52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EPackage52"):
                    opp_val = getattr(item, "EPackage52", None)
                    
                    setattr(item, "EPackage52", self)
                    

    @property
    def EPackage41(self):
        return self.__EPackage41

    @EPackage41.setter
    def EPackage41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EPackage__EPackage41", None)
        self.__EPackage41 = value
        
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
        old_value = getattr(self, f"_javaless_EPackage__eSubpackages", None)
        self.__eSubpackages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EPackage55"):
                opp_val = getattr(old_value, "EPackage55", None)
                if opp_val == self:
                    setattr(old_value, "EPackage55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EPackage55"):
                opp_val = getattr(value, "EPackage55", None)
                setattr(value, "EPackage55", self)

    def getEClassifier(self, name: str) -> EClassifier:
        # TODO: Implement getEClassifier method
        pass

class javaless_ETypedElement(ENamedElement):

    def __init__(self, ordered: bool, unique: bool, lowerBound: int, upperBound: int, many: bool, required: bool, javaless_ETypedElement: "javaless_EClassifier" = None):
        self.ordered = ordered
        self.unique = unique
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.many = many
        self.required = required
        self.javaless_ETypedElement = javaless_ETypedElement
        
    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

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
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def javaless_ETypedElement(self):
        return self.__javaless_ETypedElement

    @javaless_ETypedElement.setter
    def javaless_ETypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_ETypedElement__javaless_ETypedElement", None)
        self.__javaless_ETypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_EClassifier67"):
                opp_val = getattr(old_value, "javaless_EClassifier67", None)
                if opp_val == self:
                    setattr(old_value, "javaless_EClassifier67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_EClassifier67"):
                opp_val = getattr(value, "javaless_EClassifier67", None)
                setattr(value, "javaless_EClassifier67", self)

class javaless_EClassifier(ENamedElement):

    def __init__(self, instanceClassName: str, instanceClass: str, defaultValue: str, eClassifiers: "javaless_EPackage" = None, javaless_EClassifier: "javaless_EOperation" = None, EClassifier: "javaless_EPackage" = None, javaless_EClassifier67: "javaless_ETypedElement" = None):
        self.instanceClassName = instanceClassName
        self.instanceClass = instanceClass
        self.defaultValue = defaultValue
        self.eClassifiers = eClassifiers
        self.javaless_EClassifier = javaless_EClassifier
        self.EClassifier = EClassifier
        self.javaless_EClassifier67 = javaless_EClassifier67
        
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
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def javaless_EClassifier(self):
        return self.__javaless_EClassifier

    @javaless_EClassifier.setter
    def javaless_EClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EClassifier__javaless_EClassifier", None)
        self.__javaless_EClassifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_EOperation46"):
                opp_val = getattr(old_value, "javaless_EOperation46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_EOperation46"):
                opp_val = getattr(value, "javaless_EOperation46", None)
                if opp_val is None:
                    setattr(value, "javaless_EOperation46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaless_EClassifier67(self):
        return self.__javaless_EClassifier67

    @javaless_EClassifier67.setter
    def javaless_EClassifier67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EClassifier__javaless_EClassifier67", None)
        self.__javaless_EClassifier67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_ETypedElement"):
                opp_val = getattr(old_value, "javaless_ETypedElement", None)
                if opp_val == self:
                    setattr(old_value, "javaless_ETypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_ETypedElement"):
                opp_val = getattr(value, "javaless_ETypedElement", None)
                setattr(value, "javaless_ETypedElement", self)

    @property
    def EClassifier(self):
        return self.__EClassifier

    @EClassifier.setter
    def EClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EClassifier__EClassifier", None)
        self.__EClassifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ePackage49"):
                opp_val = getattr(old_value, "ePackage49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ePackage49"):
                opp_val = getattr(value, "ePackage49", None)
                if opp_val is None:
                    setattr(value, "ePackage49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eClassifiers(self):
        return self.__eClassifiers

    @eClassifiers.setter
    def eClassifiers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EClassifier__eClassifiers", None)
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

class javaless_EOperation(ETypedElement):

    pass
class javaless_EObject:

    def __init__(self, javaless_EObject: "javaless_EAnnotation" = None, javaless_EObject7: "javaless_EAnnotation" = None):
        self.javaless_EObject = javaless_EObject
        self.javaless_EObject7 = javaless_EObject7
        
    @property
    def javaless_EObject(self):
        return self.__javaless_EObject

    @javaless_EObject.setter
    def javaless_EObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EObject__javaless_EObject", None)
        self.__javaless_EObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_EAnnotation4"):
                opp_val = getattr(old_value, "javaless_EAnnotation4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_EAnnotation4"):
                opp_val = getattr(value, "javaless_EAnnotation4", None)
                if opp_val is None:
                    setattr(value, "javaless_EAnnotation4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaless_EObject7(self):
        return self.__javaless_EObject7

    @javaless_EObject7.setter
    def javaless_EObject7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EObject__javaless_EObject7", None)
        self.__javaless_EObject7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_EAnnotation6"):
                opp_val = getattr(old_value, "javaless_EAnnotation6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_EAnnotation6"):
                opp_val = getattr(value, "javaless_EAnnotation6", None)
                if opp_val is None:
                    setattr(value, "javaless_EAnnotation6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def eContainmentFeature(self) -> str:
        # TODO: Implement eContainmentFeature method
        pass

    def eCrossReferences(self) -> str:
        # TODO: Implement eCrossReferences method
        pass

    def eContents(self) -> str:
        # TODO: Implement eContents method
        pass

    def eAllContents(self) -> str:
        # TODO: Implement eAllContents method
        pass

    def eSet(self, newValue: str, feature: EStructuralFeature):
        # TODO: Implement eSet method
        pass

    def eResource(self) -> str:
        # TODO: Implement eResource method
        pass

    def eIsSet(self, feature: EStructuralFeature) -> bool:
        # TODO: Implement eIsSet method
        pass

    def eIsProxy(self) -> bool:
        # TODO: Implement eIsProxy method
        pass

    def eUnset(self, feature: EStructuralFeature):
        # TODO: Implement eUnset method
        pass

    def eGet(self, feature: EStructuralFeature) -> str:
        # TODO: Implement eGet method
        pass

    def eContainingFeature(self) -> EStructuralFeature:
        # TODO: Implement eContainingFeature method
        pass

    def eClass(self) -> str:
        # TODO: Implement eClass method
        pass

    def eContainer(self) -> EObject:
        # TODO: Implement eContainer method
        pass

    def eGet(self, feature: EStructuralFeature, resolve: bool) -> str:
        # TODO: Implement eGet method
        pass

class javaless_EModelElement(EObject):

    def __init__(self, EModelElement: "javaless_EAnnotation" = None, eModelElement: set["javaless_EAnnotation"] = None):
        self.EModelElement = EModelElement
        self.eModelElement = eModelElement if eModelElement is not None else set()
        
    @property
    def eModelElement(self):
        return self.__eModelElement

    @eModelElement.setter
    def eModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EModelElement__eModelElement", None)
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
                    

    @property
    def EModelElement(self):
        return self.__EModelElement

    @EModelElement.setter
    def EModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EModelElement__EModelElement", None)
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

    def getEAnnotation(self, source: str) -> str:
        # TODO: Implement getEAnnotation method
        pass

class javaless_EStringToStringMapEntry:

    def __init__(self, key: str, value: str, javaless_EStringToStringMapEntry: "javaless_EAnnotation" = None):
        self.key = key
        self.value = value
        self.javaless_EStringToStringMapEntry = javaless_EStringToStringMapEntry
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def javaless_EStringToStringMapEntry(self):
        return self.__javaless_EStringToStringMapEntry

    @javaless_EStringToStringMapEntry.setter
    def javaless_EStringToStringMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EStringToStringMapEntry__javaless_EStringToStringMapEntry", None)
        self.__javaless_EStringToStringMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_EAnnotation"):
                opp_val = getattr(old_value, "javaless_EAnnotation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_EAnnotation"):
                opp_val = getattr(value, "javaless_EAnnotation", None)
                if opp_val is None:
                    setattr(value, "javaless_EAnnotation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EModelElement:

    pass
class javaless_ENamedElement(EModelElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class javaless_EFactory(EModelElement):

    def __init__(self, eFactoryInstance: "javaless_EPackage" = None, EFactory: "javaless_EPackage" = None):
        self.eFactoryInstance = eFactoryInstance
        self.EFactory = EFactory
        
    @property
    def eFactoryInstance(self):
        return self.__eFactoryInstance

    @eFactoryInstance.setter
    def eFactoryInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EFactory__eFactoryInstance", None)
        self.__eFactoryInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EPackage41"):
                opp_val = getattr(old_value, "EPackage41", None)
                if opp_val == self:
                    setattr(old_value, "EPackage41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EPackage41"):
                opp_val = getattr(value, "EPackage41", None)
                setattr(value, "EPackage41", self)

    @property
    def EFactory(self):
        return self.__EFactory

    @EFactory.setter
    def EFactory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EFactory__EFactory", None)
        self.__EFactory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ePackage"):
                opp_val = getattr(old_value, "ePackage", None)
                if opp_val == self:
                    setattr(old_value, "ePackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ePackage"):
                opp_val = getattr(value, "ePackage", None)
                setattr(value, "ePackage", self)

    def convertToString(self, instanceValue: str, eDataType: EDataType) -> str:
        # TODO: Implement convertToString method
        pass

    def createFromString(self, literalValue: str, eDataType: EDataType) -> str:
        # TODO: Implement createFromString method
        pass

    def create(self, eClass: str) -> str:
        # TODO: Implement create method
        pass

class javaless_EAnnotation(EModelElement):

    def __init__(self, source: str, javaless_EAnnotation4: set["javaless_EObject"] = None, javaless_EAnnotation6: set["javaless_EObject"] = None, javaless_EAnnotation: set["javaless_EStringToStringMapEntry"] = None, eAnnotations: "javaless_EModelElement" = None, EAnnotation: "javaless_EModelElement" = None):
        self.source = source
        self.javaless_EAnnotation4 = javaless_EAnnotation4 if javaless_EAnnotation4 is not None else set()
        self.javaless_EAnnotation6 = javaless_EAnnotation6 if javaless_EAnnotation6 is not None else set()
        self.javaless_EAnnotation = javaless_EAnnotation if javaless_EAnnotation is not None else set()
        self.eAnnotations = eAnnotations
        self.EAnnotation = EAnnotation
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def EAnnotation(self):
        return self.__EAnnotation

    @EAnnotation.setter
    def EAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EAnnotation__EAnnotation", None)
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
    def eAnnotations(self):
        return self.__eAnnotations

    @eAnnotations.setter
    def eAnnotations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EAnnotation__eAnnotations", None)
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
    def javaless_EAnnotation6(self):
        return self.__javaless_EAnnotation6

    @javaless_EAnnotation6.setter
    def javaless_EAnnotation6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EAnnotation__javaless_EAnnotation6", None)
        self.__javaless_EAnnotation6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaless_EObject7"):
                    opp_val = getattr(item, "javaless_EObject7", None)
                    
                    if opp_val == self:
                        setattr(item, "javaless_EObject7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaless_EObject7"):
                    opp_val = getattr(item, "javaless_EObject7", None)
                    
                    setattr(item, "javaless_EObject7", self)
                    

    @property
    def javaless_EAnnotation(self):
        return self.__javaless_EAnnotation

    @javaless_EAnnotation.setter
    def javaless_EAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EAnnotation__javaless_EAnnotation", None)
        self.__javaless_EAnnotation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaless_EStringToStringMapEntry"):
                    opp_val = getattr(item, "javaless_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "javaless_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaless_EStringToStringMapEntry"):
                    opp_val = getattr(item, "javaless_EStringToStringMapEntry", None)
                    
                    setattr(item, "javaless_EStringToStringMapEntry", self)
                    

    @property
    def javaless_EAnnotation4(self):
        return self.__javaless_EAnnotation4

    @javaless_EAnnotation4.setter
    def javaless_EAnnotation4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EAnnotation__javaless_EAnnotation4", None)
        self.__javaless_EAnnotation4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaless_EObject"):
                    opp_val = getattr(item, "javaless_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "javaless_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaless_EObject"):
                    opp_val = getattr(item, "javaless_EObject", None)
                    
                    setattr(item, "javaless_EObject", self)
                    

class EClassifier:

    pass
class javaless_EDataType(EClassifier):

    def __init__(self, serializable: bool, javaless_EDataType: "javaless_EAttribute" = None):
        self.serializable = serializable
        self.javaless_EDataType = javaless_EDataType
        
    @property
    def serializable(self) -> bool:
        return self.__serializable

    @serializable.setter
    def serializable(self, serializable: bool):
        self.__serializable = serializable

    @property
    def javaless_EDataType(self):
        return self.__javaless_EDataType

    @javaless_EDataType.setter
    def javaless_EDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EDataType__javaless_EDataType", None)
        self.__javaless_EDataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_EAttribute"):
                opp_val = getattr(old_value, "javaless_EAttribute", None)
                if opp_val == self:
                    setattr(old_value, "javaless_EAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_EAttribute"):
                opp_val = getattr(value, "javaless_EAttribute", None)
                setattr(value, "javaless_EAttribute", self)

class javaless_EClass(EClassifier):

    def __init__(self, abstract: bool, interface: bool, javaless_EClass15: set["javaless_EReference"] = None, javaless_EClass17: set["javaless_EReference"] = None, javaless_EClass20: set["javaless_EAttribute"] = None, javaless_EClass23: set["javaless_EReference"] = None, javaless_EClass: "javaless_EClass" = None, javaless_EClass8: set["javaless_EClass"] = None, eContainingClass: set["javaless_EOperation"] = None, javaless_EClass12: set["javaless_EAttribute"] = None, javaless_EClass33: "javaless_EAttribute" = None, eContainingClass36: set["javaless_EStructuralFeature"] = None, javaless_EClass26: set["javaless_EOperation"] = None, javaless_EClass28: set["javaless_EStructuralFeature"] = None, javaless_EClass31: "javaless_EClass" = None, javaless_EClass29: set["javaless_EClass"] = None, EClass: "javaless_EOperation" = None, EClass65: "javaless_EStructuralFeature" = None, javaless_EClass63: "javaless_EReference" = None):
        self.abstract = abstract
        self.interface = interface
        self.javaless_EClass15 = javaless_EClass15 if javaless_EClass15 is not None else set()
        self.javaless_EClass17 = javaless_EClass17 if javaless_EClass17 is not None else set()
        self.javaless_EClass20 = javaless_EClass20 if javaless_EClass20 is not None else set()
        self.javaless_EClass23 = javaless_EClass23 if javaless_EClass23 is not None else set()
        self.javaless_EClass = javaless_EClass
        self.javaless_EClass8 = javaless_EClass8 if javaless_EClass8 is not None else set()
        self.eContainingClass = eContainingClass if eContainingClass is not None else set()
        self.javaless_EClass12 = javaless_EClass12 if javaless_EClass12 is not None else set()
        self.javaless_EClass33 = javaless_EClass33
        self.eContainingClass36 = eContainingClass36 if eContainingClass36 is not None else set()
        self.javaless_EClass26 = javaless_EClass26 if javaless_EClass26 is not None else set()
        self.javaless_EClass28 = javaless_EClass28 if javaless_EClass28 is not None else set()
        self.javaless_EClass31 = javaless_EClass31
        self.javaless_EClass29 = javaless_EClass29 if javaless_EClass29 is not None else set()
        self.EClass = EClass
        self.EClass65 = EClass65
        self.javaless_EClass63 = javaless_EClass63
        
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
    def javaless_EClass15(self):
        return self.__javaless_EClass15

    @javaless_EClass15.setter
    def javaless_EClass15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EClass__javaless_EClass15", None)
        self.__javaless_EClass15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaless_EReference"):
                    opp_val = getattr(item, "javaless_EReference", None)
                    
                    if opp_val == self:
                        setattr(item, "javaless_EReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaless_EReference"):
                    opp_val = getattr(item, "javaless_EReference", None)
                    
                    setattr(item, "javaless_EReference", self)
                    

    @property
    def javaless_EClass29(self):
        return self.__javaless_EClass29

    @javaless_EClass29.setter
    def javaless_EClass29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EClass__javaless_EClass29", None)
        self.__javaless_EClass29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaless_EClass31"):
                    opp_val = getattr(item, "javaless_EClass31", None)
                    
                    if opp_val == self:
                        setattr(item, "javaless_EClass31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaless_EClass31"):
                    opp_val = getattr(item, "javaless_EClass31", None)
                    
                    setattr(item, "javaless_EClass31", self)
                    

    @property
    def EClass65(self):
        return self.__EClass65

    @EClass65.setter
    def EClass65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EClass__EClass65", None)
        self.__EClass65 = value
        
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
    def eContainingClass(self):
        return self.__eContainingClass

    @eContainingClass.setter
    def eContainingClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EClass__eContainingClass", None)
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
    def javaless_EClass17(self):
        return self.__javaless_EClass17

    @javaless_EClass17.setter
    def javaless_EClass17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EClass__javaless_EClass17", None)
        self.__javaless_EClass17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaless_EReference18"):
                    opp_val = getattr(item, "javaless_EReference18", None)
                    
                    if opp_val == self:
                        setattr(item, "javaless_EReference18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaless_EReference18"):
                    opp_val = getattr(item, "javaless_EReference18", None)
                    
                    setattr(item, "javaless_EReference18", self)
                    

    @property
    def javaless_EClass26(self):
        return self.__javaless_EClass26

    @javaless_EClass26.setter
    def javaless_EClass26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EClass__javaless_EClass26", None)
        self.__javaless_EClass26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaless_EOperation"):
                    opp_val = getattr(item, "javaless_EOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "javaless_EOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaless_EOperation"):
                    opp_val = getattr(item, "javaless_EOperation", None)
                    
                    setattr(item, "javaless_EOperation", self)
                    

    @property
    def javaless_EClass33(self):
        return self.__javaless_EClass33

    @javaless_EClass33.setter
    def javaless_EClass33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EClass__javaless_EClass33", None)
        self.__javaless_EClass33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_EAttribute34"):
                opp_val = getattr(old_value, "javaless_EAttribute34", None)
                if opp_val == self:
                    setattr(old_value, "javaless_EAttribute34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_EAttribute34"):
                opp_val = getattr(value, "javaless_EAttribute34", None)
                setattr(value, "javaless_EAttribute34", self)

    @property
    def javaless_EClass12(self):
        return self.__javaless_EClass12

    @javaless_EClass12.setter
    def javaless_EClass12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EClass__javaless_EClass12", None)
        self.__javaless_EClass12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaless_EAttribute13"):
                    opp_val = getattr(item, "javaless_EAttribute13", None)
                    
                    if opp_val == self:
                        setattr(item, "javaless_EAttribute13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaless_EAttribute13"):
                    opp_val = getattr(item, "javaless_EAttribute13", None)
                    
                    setattr(item, "javaless_EAttribute13", self)
                    

    @property
    def javaless_EClass8(self):
        return self.__javaless_EClass8

    @javaless_EClass8.setter
    def javaless_EClass8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EClass__javaless_EClass8", None)
        self.__javaless_EClass8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaless_EClass"):
                    opp_val = getattr(item, "javaless_EClass", None)
                    
                    if opp_val == self:
                        setattr(item, "javaless_EClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaless_EClass"):
                    opp_val = getattr(item, "javaless_EClass", None)
                    
                    setattr(item, "javaless_EClass", self)
                    

    @property
    def javaless_EClass28(self):
        return self.__javaless_EClass28

    @javaless_EClass28.setter
    def javaless_EClass28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EClass__javaless_EClass28", None)
        self.__javaless_EClass28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaless_EStructuralFeature"):
                    opp_val = getattr(item, "javaless_EStructuralFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "javaless_EStructuralFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaless_EStructuralFeature"):
                    opp_val = getattr(item, "javaless_EStructuralFeature", None)
                    
                    setattr(item, "javaless_EStructuralFeature", self)
                    

    @property
    def javaless_EClass31(self):
        return self.__javaless_EClass31

    @javaless_EClass31.setter
    def javaless_EClass31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EClass__javaless_EClass31", None)
        self.__javaless_EClass31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_EClass29"):
                opp_val = getattr(old_value, "javaless_EClass29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_EClass29"):
                opp_val = getattr(value, "javaless_EClass29", None)
                if opp_val is None:
                    setattr(value, "javaless_EClass29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaless_EClass63(self):
        return self.__javaless_EClass63

    @javaless_EClass63.setter
    def javaless_EClass63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EClass__javaless_EClass63", None)
        self.__javaless_EClass63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_EReference62"):
                opp_val = getattr(old_value, "javaless_EReference62", None)
                if opp_val == self:
                    setattr(old_value, "javaless_EReference62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_EReference62"):
                opp_val = getattr(value, "javaless_EReference62", None)
                setattr(value, "javaless_EReference62", self)

    @property
    def javaless_EClass(self):
        return self.__javaless_EClass

    @javaless_EClass.setter
    def javaless_EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EClass__javaless_EClass", None)
        self.__javaless_EClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_EClass8"):
                opp_val = getattr(old_value, "javaless_EClass8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_EClass8"):
                opp_val = getattr(value, "javaless_EClass8", None)
                if opp_val is None:
                    setattr(value, "javaless_EClass8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaless_EClass23(self):
        return self.__javaless_EClass23

    @javaless_EClass23.setter
    def javaless_EClass23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EClass__javaless_EClass23", None)
        self.__javaless_EClass23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaless_EReference24"):
                    opp_val = getattr(item, "javaless_EReference24", None)
                    
                    if opp_val == self:
                        setattr(item, "javaless_EReference24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaless_EReference24"):
                    opp_val = getattr(item, "javaless_EReference24", None)
                    
                    setattr(item, "javaless_EReference24", self)
                    

    @property
    def EClass(self):
        return self.__EClass

    @EClass.setter
    def EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EClass__EClass", None)
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
    def eContainingClass36(self):
        return self.__eContainingClass36

    @eContainingClass36.setter
    def eContainingClass36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EClass__eContainingClass36", None)
        self.__eContainingClass36 = value if value is not None else set()
        
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
    def javaless_EClass20(self):
        return self.__javaless_EClass20

    @javaless_EClass20.setter
    def javaless_EClass20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EClass__javaless_EClass20", None)
        self.__javaless_EClass20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaless_EAttribute21"):
                    opp_val = getattr(item, "javaless_EAttribute21", None)
                    
                    if opp_val == self:
                        setattr(item, "javaless_EAttribute21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaless_EAttribute21"):
                    opp_val = getattr(item, "javaless_EAttribute21", None)
                    
                    setattr(item, "javaless_EAttribute21", self)
                    

    def getEStructuralFeature(self, featureID: int) -> EStructuralFeature:
        # TODO: Implement getEStructuralFeature method
        pass

    def isSuperTypeOf(self, someClass: str) -> bool:
        # TODO: Implement isSuperTypeOf method
        pass

    def getEStructuralFeature(self, featureName: str) -> EStructuralFeature:
        # TODO: Implement getEStructuralFeature method
        pass

    def getFeatureCount(self) -> int:
        # TODO: Implement getFeatureCount method
        pass

    def getFeatureID(self, feature: EStructuralFeature) -> int:
        # TODO: Implement getFeatureID method
        pass

class EStructuralFeature:

    pass
class javaless_EReference(EStructuralFeature):

    def __init__(self, containment: bool, container: bool, resolveProxies: bool, javaless_EReference: "javaless_EClass" = None, javaless_EReference18: "javaless_EClass" = None, javaless_EReference24: "javaless_EClass" = None, javaless_EReference60: "javaless_EReference" = None, javaless_EReference58: "javaless_EReference" = None, javaless_EReference62: "javaless_EClass" = None):
        self.containment = containment
        self.container = container
        self.resolveProxies = resolveProxies
        self.javaless_EReference = javaless_EReference
        self.javaless_EReference18 = javaless_EReference18
        self.javaless_EReference24 = javaless_EReference24
        self.javaless_EReference60 = javaless_EReference60
        self.javaless_EReference58 = javaless_EReference58
        self.javaless_EReference62 = javaless_EReference62
        
    @property
    def resolveProxies(self) -> bool:
        return self.__resolveProxies

    @resolveProxies.setter
    def resolveProxies(self, resolveProxies: bool):
        self.__resolveProxies = resolveProxies

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
    def javaless_EReference(self):
        return self.__javaless_EReference

    @javaless_EReference.setter
    def javaless_EReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EReference__javaless_EReference", None)
        self.__javaless_EReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_EClass15"):
                opp_val = getattr(old_value, "javaless_EClass15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_EClass15"):
                opp_val = getattr(value, "javaless_EClass15", None)
                if opp_val is None:
                    setattr(value, "javaless_EClass15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaless_EReference62(self):
        return self.__javaless_EReference62

    @javaless_EReference62.setter
    def javaless_EReference62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EReference__javaless_EReference62", None)
        self.__javaless_EReference62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_EClass63"):
                opp_val = getattr(old_value, "javaless_EClass63", None)
                if opp_val == self:
                    setattr(old_value, "javaless_EClass63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_EClass63"):
                opp_val = getattr(value, "javaless_EClass63", None)
                setattr(value, "javaless_EClass63", self)

    @property
    def javaless_EReference60(self):
        return self.__javaless_EReference60

    @javaless_EReference60.setter
    def javaless_EReference60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EReference__javaless_EReference60", None)
        self.__javaless_EReference60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_EReference58"):
                opp_val = getattr(old_value, "javaless_EReference58", None)
                if opp_val == self:
                    setattr(old_value, "javaless_EReference58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_EReference58"):
                opp_val = getattr(value, "javaless_EReference58", None)
                setattr(value, "javaless_EReference58", self)

    @property
    def javaless_EReference58(self):
        return self.__javaless_EReference58

    @javaless_EReference58.setter
    def javaless_EReference58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EReference__javaless_EReference58", None)
        self.__javaless_EReference58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_EReference60"):
                opp_val = getattr(old_value, "javaless_EReference60", None)
                if opp_val == self:
                    setattr(old_value, "javaless_EReference60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_EReference60"):
                opp_val = getattr(value, "javaless_EReference60", None)
                setattr(value, "javaless_EReference60", self)

    @property
    def javaless_EReference24(self):
        return self.__javaless_EReference24

    @javaless_EReference24.setter
    def javaless_EReference24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EReference__javaless_EReference24", None)
        self.__javaless_EReference24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_EClass23"):
                opp_val = getattr(old_value, "javaless_EClass23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_EClass23"):
                opp_val = getattr(value, "javaless_EClass23", None)
                if opp_val is None:
                    setattr(value, "javaless_EClass23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaless_EReference18(self):
        return self.__javaless_EReference18

    @javaless_EReference18.setter
    def javaless_EReference18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EReference__javaless_EReference18", None)
        self.__javaless_EReference18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_EClass17"):
                opp_val = getattr(old_value, "javaless_EClass17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_EClass17"):
                opp_val = getattr(value, "javaless_EClass17", None)
                if opp_val is None:
                    setattr(value, "javaless_EClass17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class javaless_EAttribute(EStructuralFeature):

    def __init__(self, iD: bool, javaless_EAttribute: "javaless_EDataType" = None, javaless_EAttribute21: "javaless_EClass" = None, javaless_EAttribute13: "javaless_EClass" = None, javaless_EAttribute34: "javaless_EClass" = None):
        self.iD = iD
        self.javaless_EAttribute = javaless_EAttribute
        self.javaless_EAttribute21 = javaless_EAttribute21
        self.javaless_EAttribute13 = javaless_EAttribute13
        self.javaless_EAttribute34 = javaless_EAttribute34
        
    @property
    def iD(self) -> bool:
        return self.__iD

    @iD.setter
    def iD(self, iD: bool):
        self.__iD = iD

    @property
    def javaless_EAttribute34(self):
        return self.__javaless_EAttribute34

    @javaless_EAttribute34.setter
    def javaless_EAttribute34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EAttribute__javaless_EAttribute34", None)
        self.__javaless_EAttribute34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_EClass33"):
                opp_val = getattr(old_value, "javaless_EClass33", None)
                if opp_val == self:
                    setattr(old_value, "javaless_EClass33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_EClass33"):
                opp_val = getattr(value, "javaless_EClass33", None)
                setattr(value, "javaless_EClass33", self)

    @property
    def javaless_EAttribute13(self):
        return self.__javaless_EAttribute13

    @javaless_EAttribute13.setter
    def javaless_EAttribute13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EAttribute__javaless_EAttribute13", None)
        self.__javaless_EAttribute13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_EClass12"):
                opp_val = getattr(old_value, "javaless_EClass12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_EClass12"):
                opp_val = getattr(value, "javaless_EClass12", None)
                if opp_val is None:
                    setattr(value, "javaless_EClass12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaless_EAttribute(self):
        return self.__javaless_EAttribute

    @javaless_EAttribute.setter
    def javaless_EAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EAttribute__javaless_EAttribute", None)
        self.__javaless_EAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_EDataType"):
                opp_val = getattr(old_value, "javaless_EDataType", None)
                if opp_val == self:
                    setattr(old_value, "javaless_EDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_EDataType"):
                opp_val = getattr(value, "javaless_EDataType", None)
                setattr(value, "javaless_EDataType", self)

    @property
    def javaless_EAttribute21(self):
        return self.__javaless_EAttribute21

    @javaless_EAttribute21.setter
    def javaless_EAttribute21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaless_EAttribute__javaless_EAttribute21", None)
        self.__javaless_EAttribute21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaless_EClass20"):
                opp_val = getattr(old_value, "javaless_EClass20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaless_EClass20"):
                opp_val = getattr(value, "javaless_EClass20", None)
                if opp_val is None:
                    setattr(value, "javaless_EClass20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
