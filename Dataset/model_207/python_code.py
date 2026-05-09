from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ecore_EStringToStringMapEntry:

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class EParameter:

    pass
class ETypedElement:

    pass
class ecore_EStructuralFeature(ETypedElement):

    def __init__(self, changeable: str, volatile: str, transient: str, defaultValueLiteral: str, defaultValue: str, unsettable: str, derived: str, eStructuralFeatures: "EClass" = None):
        self.changeable = changeable
        self.volatile = volatile
        self.transient = transient
        self.defaultValueLiteral = defaultValueLiteral
        self.defaultValue = defaultValue
        self.unsettable = unsettable
        self.derived = derived
        self.eStructuralFeatures = eStructuralFeatures
        
        pass
    @property
    def derived(self):
        return self.__derived

    @derived.setter
    def derived(self, derived: str):
        self.__derived = derived


    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


    @property
    def changeable(self):
        return self.__changeable

    @changeable.setter
    def changeable(self, changeable: str):
        self.__changeable = changeable


    @property
    def defaultValueLiteral(self):
        return self.__defaultValueLiteral

    @defaultValueLiteral.setter
    def defaultValueLiteral(self, defaultValueLiteral: str):
        self.__defaultValueLiteral = defaultValueLiteral


    @property
    def unsettable(self):
        return self.__unsettable

    @unsettable.setter
    def unsettable(self, unsettable: str):
        self.__unsettable = unsettable


    @property
    def transient(self):
        return self.__transient

    @transient.setter
    def transient(self, transient: str):
        self.__transient = transient


    @property
    def volatile(self):
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: str):
        self.__volatile = volatile


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
            if hasattr(old_value, "EClass67"):
                opp_val = getattr(old_value, "EClass67", None)
                if opp_val == self:
                    setattr(old_value, "EClass67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EClass67"):
                opp_val = getattr(value, "EClass67", None)
                setattr(value, "EClass67", self)

    def getContainerClass(self) :
        # TODO: Implement getContainerClass method
        pass

    def getFeatureID(self) :
        # TODO: Implement getFeatureID method
        pass

class ecore_EOperation(ETypedElement):

    pass
class ecore_EParameter(ETypedElement):

    pass
class EFactory:

    pass
class ecore_EObject:

    def __init__(self):
        
        pass
    def eContents(self) :
        # TODO: Implement eContents method
        pass

    def eSet(self, ecore_feature, ecore_newValue):
        # TODO: Implement eSet method
        pass

    def eGet(self, ecore_resolve, ecore_feature) :
        # TODO: Implement eGet method
        pass

    def eContainingFeature(self) :
        # TODO: Implement eContainingFeature method
        pass

    def eClass(self) :
        # TODO: Implement eClass method
        pass

    def eUnset(self, ecore_feature):
        # TODO: Implement eUnset method
        pass

    def eIsProxy(self) :
        # TODO: Implement eIsProxy method
        pass

    def eAllContents(self) :
        # TODO: Implement eAllContents method
        pass

    def eContainmentFeature(self) :
        # TODO: Implement eContainmentFeature method
        pass

    def eContainer(self) :
        # TODO: Implement eContainer method
        pass

    def eResource(self) :
        # TODO: Implement eResource method
        pass

    def eCrossReferences(self) :
        # TODO: Implement eCrossReferences method
        pass

    def eIsSet(self, ecore_feature) :
        # TODO: Implement eIsSet method
        pass

    def op_eGet(self, ecore_feature) :
        # TODO: Implement op_eGet method
        pass

class EAnnotation:

    pass
class EEnum:

    pass
class EEnumLiteral:

    pass
class ETypeParameter:

    pass
class EPackage:

    pass
class ENamedElement:

    pass
class ecore_ETypeParameter(ENamedElement):

    pass
class ecore_EPackage(ENamedElement):

    def __init__(self, nsURI: str, nsPrefix: str, ePackage: "EFactory" = None, ePackage51: set["EClassifier"] = None, eSuperPackage: set["EPackage"] = None, eSubpackages: "EPackage" = None):
        self.nsURI = nsURI
        self.nsPrefix = nsPrefix
        self.ePackage = ePackage
        self.ePackage51 = ePackage51 if ePackage51 is not None else set()
        self.eSuperPackage = eSuperPackage if eSuperPackage is not None else set()
        self.eSubpackages = eSubpackages
        
        pass
    @property
    def nsPrefix(self):
        return self.__nsPrefix

    @nsPrefix.setter
    def nsPrefix(self, nsPrefix: str):
        self.__nsPrefix = nsPrefix


    @property
    def nsURI(self):
        return self.__nsURI

    @nsURI.setter
    def nsURI(self, nsURI: str):
        self.__nsURI = nsURI


    @property
    def ePackage(self):
        return self.__ePackage

    @ePackage.setter
    def ePackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__ePackage", None)
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
    def eSubpackages(self):
        return self.__eSubpackages

    @eSubpackages.setter
    def eSubpackages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__eSubpackages", None)
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
                if hasattr(item, "EPackage53"):
                    opp_val = getattr(item, "EPackage53", None)
                    
                    if opp_val == self:
                        setattr(item, "EPackage53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EPackage53"):
                    opp_val = getattr(item, "EPackage53", None)
                    
                    setattr(item, "EPackage53", self)
                    

    @property
    def ePackage51(self):
        return self.__ePackage51

    @ePackage51.setter
    def ePackage51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__ePackage51", None)
        self.__ePackage51 = value if value is not None else set()
        
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
                    

    def getEClassifier(self, ecore_name) :
        # TODO: Implement getEClassifier method
        pass

class ecore_ETypedElement(ENamedElement):

    def __init__(self, ordered: str, unique: str, lowerBound: str, upperBound: str, many: str, required: str, ecore_ETypedElement: "EClassifier" = None, ecore_ETypedElement82: "EGenericType" = None):
        self.ordered = ordered
        self.unique = unique
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.many = many
        self.required = required
        self.ecore_ETypedElement = ecore_ETypedElement
        self.ecore_ETypedElement82 = ecore_ETypedElement82
        
        pass
    @property
    def required(self):
        return self.__required

    @required.setter
    def required(self, required: str):
        self.__required = required


    @property
    def unique(self):
        return self.__unique

    @unique.setter
    def unique(self, unique: str):
        self.__unique = unique


    @property
    def lowerBound(self):
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: str):
        self.__lowerBound = lowerBound


    @property
    def many(self):
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many


    @property
    def ordered(self):
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: str):
        self.__ordered = ordered


    @property
    def upperBound(self):
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: str):
        self.__upperBound = upperBound


    @property
    def ecore_ETypedElement82(self):
        return self.__ecore_ETypedElement82

    @ecore_ETypedElement82.setter
    def ecore_ETypedElement82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_ETypedElement__ecore_ETypedElement82", None)
        self.__ecore_ETypedElement82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EGenericType83"):
                opp_val = getattr(old_value, "EGenericType83", None)
                if opp_val == self:
                    setattr(old_value, "EGenericType83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EGenericType83"):
                opp_val = getattr(value, "EGenericType83", None)
                setattr(value, "EGenericType83", self)

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
            if hasattr(old_value, "EClassifier80"):
                opp_val = getattr(old_value, "EClassifier80", None)
                if opp_val == self:
                    setattr(old_value, "EClassifier80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EClassifier80"):
                opp_val = getattr(value, "EClassifier80", None)
                setattr(value, "EClassifier80", self)

class ecore_EEnumLiteral(ENamedElement):

    def __init__(self, value: str, instance: str, literal: str, eLiterals: "EEnum" = None):
        self.value = value
        self.instance = instance
        self.literal = literal
        self.eLiterals = eLiterals
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def literal(self):
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal


    @property
    def instance(self):
        return self.__instance

    @instance.setter
    def instance(self, instance: str):
        self.__instance = instance


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

class ecore_EClassifier(ENamedElement):

    def __init__(self, instanceClassName: str, instanceClass: str, defaultValue: str, instanceTypeName: str, eClassifiers: "EPackage" = None, ecore_EClassifier: set["ETypeParameter"] = None):
        self.instanceClassName = instanceClassName
        self.instanceClass = instanceClass
        self.defaultValue = defaultValue
        self.instanceTypeName = instanceTypeName
        self.eClassifiers = eClassifiers
        self.ecore_EClassifier = ecore_EClassifier if ecore_EClassifier is not None else set()
        
        pass
    @property
    def instanceClass(self):
        return self.__instanceClass

    @instanceClass.setter
    def instanceClass(self, instanceClass: str):
        self.__instanceClass = instanceClass


    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


    @property
    def instanceTypeName(self):
        return self.__instanceTypeName

    @instanceTypeName.setter
    def instanceTypeName(self, instanceTypeName: str):
        self.__instanceTypeName = instanceTypeName


    @property
    def instanceClassName(self):
        return self.__instanceClassName

    @instanceClassName.setter
    def instanceClassName(self, instanceClassName: str):
        self.__instanceClassName = instanceClassName


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
                if hasattr(item, "ETypeParameter"):
                    opp_val = getattr(item, "ETypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "ETypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ETypeParameter"):
                    opp_val = getattr(item, "ETypeParameter", None)
                    
                    setattr(item, "ETypeParameter", self)
                    

    def getClassifierID(self) :
        # TODO: Implement getClassifierID method
        pass

    def isInstance(self, ecore_object) :
        # TODO: Implement isInstance method
        pass

class EGenericType:

    pass
class EReference:

    pass
class EAttribute:

    pass
class EOperation:

    pass
class EClass:

    pass
class EClassifier:

    pass
class ecore_EDataType(EClassifier):

    def __init__(self, serializable: str, EClassifier91: "ecore_EGenericType" = None, EClassifier80: "ecore_ETypedElement" = None, EClassifier: "ecore_EPackage" = None, EClassifier100: "ecore_EGenericType" = None, EClassifier75: "ecore_EOperation" = None):
        self.serializable = serializable
        
        pass
    @property
    def serializable(self):
        return self.__serializable

    @serializable.setter
    def serializable(self, serializable: str):
        self.__serializable = serializable


class ecore_EClass(EClassifier):

    def __init__(self, abstract: str, interface: str, ecore_EClass: set["EClass"] = None, eContainingClass: set["EOperation"] = None, ecore_EClass11: set["EAttribute"] = None, ecore_EClass13: set["EReference"] = None, ecore_EClass15: set["EReference"] = None, ecore_EClass18: set["EAttribute"] = None, ecore_EClass21: set["EReference"] = None, ecore_EClass24: set["EOperation"] = None, ecore_EClass27: set["EStructuralFeature"] = None, ecore_EClass29: set["EClass"] = None, ecore_EClass32: "EAttribute" = None, eContainingClass35: set["EStructuralFeature"] = None, ecore_EClass38: set["EGenericType"] = None, ecore_EClass40: set["EGenericType"] = None, EClassifier91: "ecore_EGenericType" = None, EClassifier80: "ecore_ETypedElement" = None, EClassifier: "ecore_EPackage" = None, EClassifier100: "ecore_EGenericType" = None, EClassifier75: "ecore_EOperation" = None):
        self.abstract = abstract
        self.interface = interface
        self.ecore_EClass = ecore_EClass if ecore_EClass is not None else set()
        self.eContainingClass = eContainingClass if eContainingClass is not None else set()
        self.ecore_EClass11 = ecore_EClass11 if ecore_EClass11 is not None else set()
        self.ecore_EClass13 = ecore_EClass13 if ecore_EClass13 is not None else set()
        self.ecore_EClass15 = ecore_EClass15 if ecore_EClass15 is not None else set()
        self.ecore_EClass18 = ecore_EClass18 if ecore_EClass18 is not None else set()
        self.ecore_EClass21 = ecore_EClass21 if ecore_EClass21 is not None else set()
        self.ecore_EClass24 = ecore_EClass24 if ecore_EClass24 is not None else set()
        self.ecore_EClass27 = ecore_EClass27 if ecore_EClass27 is not None else set()
        self.ecore_EClass29 = ecore_EClass29 if ecore_EClass29 is not None else set()
        self.ecore_EClass32 = ecore_EClass32
        self.eContainingClass35 = eContainingClass35 if eContainingClass35 is not None else set()
        self.ecore_EClass38 = ecore_EClass38 if ecore_EClass38 is not None else set()
        self.ecore_EClass40 = ecore_EClass40 if ecore_EClass40 is not None else set()
        
        pass
    @property
    def interface(self):
        return self.__interface

    @interface.setter
    def interface(self, interface: str):
        self.__interface = interface


    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract


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
                if hasattr(item, "EReference"):
                    opp_val = getattr(item, "EReference", None)
                    
                    if opp_val == self:
                        setattr(item, "EReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EReference"):
                    opp_val = getattr(item, "EReference", None)
                    
                    setattr(item, "EReference", self)
                    

    @property
    def ecore_EClass15(self):
        return self.__ecore_EClass15

    @ecore_EClass15.setter
    def ecore_EClass15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass15", None)
        self.__ecore_EClass15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EReference16"):
                    opp_val = getattr(item, "EReference16", None)
                    
                    if opp_val == self:
                        setattr(item, "EReference16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EReference16"):
                    opp_val = getattr(item, "EReference16", None)
                    
                    setattr(item, "EReference16", self)
                    

    @property
    def ecore_EClass24(self):
        return self.__ecore_EClass24

    @ecore_EClass24.setter
    def ecore_EClass24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass24", None)
        self.__ecore_EClass24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EOperation25"):
                    opp_val = getattr(item, "EOperation25", None)
                    
                    if opp_val == self:
                        setattr(item, "EOperation25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EOperation25"):
                    opp_val = getattr(item, "EOperation25", None)
                    
                    setattr(item, "EOperation25", self)
                    

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
    def eContainingClass35(self):
        return self.__eContainingClass35

    @eContainingClass35.setter
    def eContainingClass35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__eContainingClass35", None)
        self.__eContainingClass35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EStructuralFeature36"):
                    opp_val = getattr(item, "EStructuralFeature36", None)
                    
                    if opp_val == self:
                        setattr(item, "EStructuralFeature36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EStructuralFeature36"):
                    opp_val = getattr(item, "EStructuralFeature36", None)
                    
                    setattr(item, "EStructuralFeature36", self)
                    

    @property
    def ecore_EClass32(self):
        return self.__ecore_EClass32

    @ecore_EClass32.setter
    def ecore_EClass32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass32", None)
        self.__ecore_EClass32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EAttribute33"):
                opp_val = getattr(old_value, "EAttribute33", None)
                if opp_val == self:
                    setattr(old_value, "EAttribute33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EAttribute33"):
                opp_val = getattr(value, "EAttribute33", None)
                setattr(value, "EAttribute33", self)

    @property
    def ecore_EClass40(self):
        return self.__ecore_EClass40

    @ecore_EClass40.setter
    def ecore_EClass40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass40", None)
        self.__ecore_EClass40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EGenericType41"):
                    opp_val = getattr(item, "EGenericType41", None)
                    
                    if opp_val == self:
                        setattr(item, "EGenericType41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EGenericType41"):
                    opp_val = getattr(item, "EGenericType41", None)
                    
                    setattr(item, "EGenericType41", self)
                    

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
                if hasattr(item, "EReference22"):
                    opp_val = getattr(item, "EReference22", None)
                    
                    if opp_val == self:
                        setattr(item, "EReference22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EReference22"):
                    opp_val = getattr(item, "EReference22", None)
                    
                    setattr(item, "EReference22", self)
                    

    @property
    def ecore_EClass29(self):
        return self.__ecore_EClass29

    @ecore_EClass29.setter
    def ecore_EClass29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass29", None)
        self.__ecore_EClass29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EClass30"):
                    opp_val = getattr(item, "EClass30", None)
                    
                    if opp_val == self:
                        setattr(item, "EClass30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EClass30"):
                    opp_val = getattr(item, "EClass30", None)
                    
                    setattr(item, "EClass30", self)
                    

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
                if hasattr(item, "EClass"):
                    opp_val = getattr(item, "EClass", None)
                    
                    if opp_val == self:
                        setattr(item, "EClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EClass"):
                    opp_val = getattr(item, "EClass", None)
                    
                    setattr(item, "EClass", self)
                    

    @property
    def ecore_EClass38(self):
        return self.__ecore_EClass38

    @ecore_EClass38.setter
    def ecore_EClass38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass38", None)
        self.__ecore_EClass38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EGenericType"):
                    opp_val = getattr(item, "EGenericType", None)
                    
                    if opp_val == self:
                        setattr(item, "EGenericType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EGenericType"):
                    opp_val = getattr(item, "EGenericType", None)
                    
                    setattr(item, "EGenericType", self)
                    

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
                if hasattr(item, "EAttribute19"):
                    opp_val = getattr(item, "EAttribute19", None)
                    
                    if opp_val == self:
                        setattr(item, "EAttribute19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EAttribute19"):
                    opp_val = getattr(item, "EAttribute19", None)
                    
                    setattr(item, "EAttribute19", self)
                    

    @property
    def ecore_EClass11(self):
        return self.__ecore_EClass11

    @ecore_EClass11.setter
    def ecore_EClass11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass11", None)
        self.__ecore_EClass11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EAttribute"):
                    opp_val = getattr(item, "EAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "EAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EAttribute"):
                    opp_val = getattr(item, "EAttribute", None)
                    
                    setattr(item, "EAttribute", self)
                    

    def op_getEStructuralFeature(self, ecore_featureID) :
        # TODO: Implement op_getEStructuralFeature method
        pass

    def getEStructuralFeature(self, ecore_featureName) :
        # TODO: Implement getEStructuralFeature method
        pass

    def isSuperTypeOf(self, ecore_someClass) :
        # TODO: Implement isSuperTypeOf method
        pass

    def getFeatureID(self, ecore_feature) :
        # TODO: Implement getFeatureID method
        pass

    def getFeatureCount(self) :
        # TODO: Implement getFeatureCount method
        pass

class EObject:

    pass
class ecore_EModelElement(EObject):

    def __init__(self, eModelElement: set["EAnnotation"] = None, EObject: "ecore_EAnnotation" = None, EObject7: "ecore_EAnnotation" = None):
        self.eModelElement = eModelElement if eModelElement is not None else set()
        
        pass
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
                    

    def getEAnnotation(self, ecore_source) :
        # TODO: Implement getEAnnotation method
        pass

class ecore_EGenericType(EObject):

    pass
class EStringToStringMapEntry:

    pass
class EModelElement:

    pass
class ecore_EFactory(EModelElement):

    def __init__(self, eFactoryInstance: "EPackage" = None, EModelElement: "ecore_EAnnotation" = None):
        self.eFactoryInstance = eFactoryInstance
        
        pass
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

    def createFromString(self, ecore_eDataType, ecore_literalValue) :
        # TODO: Implement createFromString method
        pass

    def create(self, ecore_eClass) :
        # TODO: Implement create method
        pass

    def convertToString(self, ecore_eDataType, ecore_instanceValue) :
        # TODO: Implement convertToString method
        pass

class ecore_ENamedElement(EModelElement):

    def __init__(self, name: str, EModelElement: "ecore_EAnnotation" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class ecore_EAnnotation(EModelElement):

    def __init__(self, source: str, ecore_EAnnotation4: set["EObject"] = None, ecore_EAnnotation6: set["EObject"] = None, ecore_EAnnotation: set["EStringToStringMapEntry"] = None, eAnnotations: "EModelElement" = None, EModelElement: "ecore_EAnnotation" = None):
        self.source = source
        self.ecore_EAnnotation4 = ecore_EAnnotation4 if ecore_EAnnotation4 is not None else set()
        self.ecore_EAnnotation6 = ecore_EAnnotation6 if ecore_EAnnotation6 is not None else set()
        self.ecore_EAnnotation = ecore_EAnnotation if ecore_EAnnotation is not None else set()
        self.eAnnotations = eAnnotations
        
        pass
    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source


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
                if hasattr(item, "EObject"):
                    opp_val = getattr(item, "EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EObject"):
                    opp_val = getattr(item, "EObject", None)
                    
                    setattr(item, "EObject", self)
                    

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
                if hasattr(item, "EStringToStringMapEntry"):
                    opp_val = getattr(item, "EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EStringToStringMapEntry"):
                    opp_val = getattr(item, "EStringToStringMapEntry", None)
                    
                    setattr(item, "EStringToStringMapEntry", self)
                    

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
    def ecore_EAnnotation6(self):
        return self.__ecore_EAnnotation6

    @ecore_EAnnotation6.setter
    def ecore_EAnnotation6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAnnotation__ecore_EAnnotation6", None)
        self.__ecore_EAnnotation6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EObject7"):
                    opp_val = getattr(item, "EObject7", None)
                    
                    if opp_val == self:
                        setattr(item, "EObject7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EObject7"):
                    opp_val = getattr(item, "EObject7", None)
                    
                    setattr(item, "EObject7", self)
                    

class EDataType:

    pass
class ecore_EEnum(EDataType):

    def __init__(self, eEnum: set["EEnumLiteral"] = None, EDataType: "ecore_EAttribute" = None):
        self.eEnum = eEnum if eEnum is not None else set()
        
        pass
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
                    

    def getEEnumLiteral(self, ecore_value) :
        # TODO: Implement getEEnumLiteral method
        pass

    def getEEnumLiteralByLiteral(self, ecore_literal) :
        # TODO: Implement getEEnumLiteralByLiteral method
        pass

    def op_getEEnumLiteral(self, ecore_name) :
        # TODO: Implement op_getEEnumLiteral method
        pass

class EStructuralFeature:

    pass
class ecore_EReference(EStructuralFeature):

    def __init__(self, containment: str, container: str, resolveProxies: str, ecore_EReference: "EReference" = None, ecore_EReference61: "EClass" = None, ecore_EReference64: set["EAttribute"] = None, EStructuralFeature: "ecore_EClass" = None, EStructuralFeature36: "ecore_EClass" = None):
        self.containment = containment
        self.container = container
        self.resolveProxies = resolveProxies
        self.ecore_EReference = ecore_EReference
        self.ecore_EReference61 = ecore_EReference61
        self.ecore_EReference64 = ecore_EReference64 if ecore_EReference64 is not None else set()
        
        pass
    @property
    def container(self):
        return self.__container

    @container.setter
    def container(self, container: str):
        self.__container = container


    @property
    def containment(self):
        return self.__containment

    @containment.setter
    def containment(self, containment: str):
        self.__containment = containment


    @property
    def resolveProxies(self):
        return self.__resolveProxies

    @resolveProxies.setter
    def resolveProxies(self, resolveProxies: str):
        self.__resolveProxies = resolveProxies


    @property
    def ecore_EReference61(self):
        return self.__ecore_EReference61

    @ecore_EReference61.setter
    def ecore_EReference61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference61", None)
        self.__ecore_EReference61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EClass62"):
                opp_val = getattr(old_value, "EClass62", None)
                if opp_val == self:
                    setattr(old_value, "EClass62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EClass62"):
                opp_val = getattr(value, "EClass62", None)
                setattr(value, "EClass62", self)

    @property
    def ecore_EReference64(self):
        return self.__ecore_EReference64

    @ecore_EReference64.setter
    def ecore_EReference64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference64", None)
        self.__ecore_EReference64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EAttribute65"):
                    opp_val = getattr(item, "EAttribute65", None)
                    
                    if opp_val == self:
                        setattr(item, "EAttribute65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EAttribute65"):
                    opp_val = getattr(item, "EAttribute65", None)
                    
                    setattr(item, "EAttribute65", self)
                    

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
            if hasattr(old_value, "EReference59"):
                opp_val = getattr(old_value, "EReference59", None)
                if opp_val == self:
                    setattr(old_value, "EReference59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EReference59"):
                opp_val = getattr(value, "EReference59", None)
                setattr(value, "EReference59", self)

class ecore_EAttribute(EStructuralFeature):

    def __init__(self, iD: str, ecore_EAttribute: "EDataType" = None, EStructuralFeature: "ecore_EClass" = None, EStructuralFeature36: "ecore_EClass" = None):
        self.iD = iD
        self.ecore_EAttribute = ecore_EAttribute
        
        pass
    @property
    def iD(self):
        return self.__iD

    @iD.setter
    def iD(self, iD: str):
        self.__iD = iD


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
            if hasattr(old_value, "EDataType"):
                opp_val = getattr(old_value, "EDataType", None)
                if opp_val == self:
                    setattr(old_value, "EDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EDataType"):
                opp_val = getattr(value, "EDataType", None)
                setattr(value, "EDataType", self)
