from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

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
                    

    def getEEnumLiteral(self, name: str) -> str:
        # TODO: Implement getEEnumLiteral method
        pass

    def getEEnumLiteral(self, value: int) -> str:
        # TODO: Implement getEEnumLiteral method
        pass

    def getEEnumLiteralByLiteral(self, literal: str) -> str:
        # TODO: Implement getEEnumLiteralByLiteral method
        pass

class ecore_EStringToStringMapEntry:

    def __init__(self, key: str, value: str, ecore_EStringToStringMapEntry: "ecore_EAnnotation" = None):
        self.key = key
        self.value = value
        self.ecore_EStringToStringMapEntry = ecore_EStringToStringMapEntry
        
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

class EClassifier:

    pass
class ecore_EObject:

    def __init__(self, ecore_EObject: "ecore_EAnnotation" = None, ecore_EObject104: "ecore_EAnnotation" = None):
        self.ecore_EObject = ecore_EObject
        self.ecore_EObject104 = ecore_EObject104
        
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
            if hasattr(old_value, "ecore_EAnnotation101"):
                opp_val = getattr(old_value, "ecore_EAnnotation101", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EAnnotation101"):
                opp_val = getattr(value, "ecore_EAnnotation101", None)
                if opp_val is None:
                    setattr(value, "ecore_EAnnotation101", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EObject104(self):
        return self.__ecore_EObject104

    @ecore_EObject104.setter
    def ecore_EObject104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EObject__ecore_EObject104", None)
        self.__ecore_EObject104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EAnnotation103"):
                opp_val = getattr(old_value, "ecore_EAnnotation103", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EAnnotation103"):
                opp_val = getattr(value, "ecore_EAnnotation103", None)
                if opp_val is None:
                    setattr(value, "ecore_EAnnotation103", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def eGet(self, feature: EStructuralFeature) -> str:
        # TODO: Implement eGet method
        pass

    def eCrossReferences(self):
        # TODO: Implement eCrossReferences method
        pass

    def eAllContents(self):
        # TODO: Implement eAllContents method
        pass

    def eUnset(self, feature: EStructuralFeature):
        # TODO: Implement eUnset method
        pass

    def eIsSet(self, feature: EStructuralFeature) -> bool:
        # TODO: Implement eIsSet method
        pass

    def eContainer(self) -> EObject:
        # TODO: Implement eContainer method
        pass

    def eIsProxy(self) -> bool:
        # TODO: Implement eIsProxy method
        pass

    def eResource(self) -> str:
        # TODO: Implement eResource method
        pass

    def eContainingFeature(self) -> EStructuralFeature:
        # TODO: Implement eContainingFeature method
        pass

    def eContents(self):
        # TODO: Implement eContents method
        pass

    def eContainmentFeature(self) -> str:
        # TODO: Implement eContainmentFeature method
        pass

    def eClass(self) -> str:
        # TODO: Implement eClass method
        pass

    def eGet(self, feature: EStructuralFeature, resolve: bool) -> str:
        # TODO: Implement eGet method
        pass

    def eSet(self, feature: EStructuralFeature, newValue: str):
        # TODO: Implement eSet method
        pass

class EObject:

    pass
class ecore_EModelElement(EObject):

    def __init__(self, eModelElement: set["ecore_EAnnotation"] = None, EModelElement: "ecore_EAnnotation" = None):
        self.eModelElement = eModelElement if eModelElement is not None else set()
        self.EModelElement = EModelElement
        
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

class EModelElement:

    pass
class ecore_EAnnotation(EModelElement):

    def __init__(self, source: str, EAnnotation: "ecore_EModelElement" = None, ecore_EAnnotation: set["ecore_EStringToStringMapEntry"] = None, ecore_EAnnotation101: set["ecore_EObject"] = None, ecore_EAnnotation103: set["ecore_EObject"] = None, eAnnotations: "ecore_EModelElement" = None):
        self.source = source
        self.EAnnotation = EAnnotation
        self.ecore_EAnnotation = ecore_EAnnotation if ecore_EAnnotation is not None else set()
        self.ecore_EAnnotation101 = ecore_EAnnotation101 if ecore_EAnnotation101 is not None else set()
        self.ecore_EAnnotation103 = ecore_EAnnotation103 if ecore_EAnnotation103 is not None else set()
        self.eAnnotations = eAnnotations
        
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
    def ecore_EAnnotation101(self):
        return self.__ecore_EAnnotation101

    @ecore_EAnnotation101.setter
    def ecore_EAnnotation101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAnnotation__ecore_EAnnotation101", None)
        self.__ecore_EAnnotation101 = value if value is not None else set()
        
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
    def ecore_EAnnotation103(self):
        return self.__ecore_EAnnotation103

    @ecore_EAnnotation103.setter
    def ecore_EAnnotation103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAnnotation__ecore_EAnnotation103", None)
        self.__ecore_EAnnotation103 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EObject104"):
                    opp_val = getattr(item, "ecore_EObject104", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EObject104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EObject104"):
                    opp_val = getattr(item, "ecore_EObject104", None)
                    
                    setattr(item, "ecore_EObject104", self)
                    

class ecore_EFactory(EModelElement):

    def __init__(self, EFactory: "ecore_EPackage" = None, eFactoryInstance: "ecore_EPackage" = None):
        self.EFactory = EFactory
        self.eFactoryInstance = eFactoryInstance
        
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
            if hasattr(old_value, "ePackage"):
                opp_val = getattr(old_value, "ePackage", None)
                if opp_val == self:
                    setattr(old_value, "ePackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ePackage"):
                opp_val = getattr(value, "ePackage", None)
                setattr(value, "ePackage", self)

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
            if hasattr(old_value, "EPackage54"):
                opp_val = getattr(old_value, "EPackage54", None)
                if opp_val == self:
                    setattr(old_value, "EPackage54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EPackage54"):
                opp_val = getattr(value, "EPackage54", None)
                setattr(value, "EPackage54", self)

    def convertToString(self, instanceValue: str, eDataType: str) -> str:
        # TODO: Implement convertToString method
        pass

    def create(self, eClass: str) -> EObject:
        # TODO: Implement create method
        pass

    def createFromString(self, eDataType: str, literalValue: str) -> str:
        # TODO: Implement createFromString method
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

class ecore_EGenericType(EObject):

    pass
class ENamedElement:

    pass
class ecore_EClassifier(ENamedElement):

    def __init__(self, instanceClass: str, instanceClassName: str, defaultValue: str, instanceTypeName: str, ecore_EClassifier: "ecore_ETypedElement" = None, eClassifiers: "ecore_EPackage" = None, ecore_EClassifier43: set["ecore_ETypeParameter"] = None, EClassifier: "ecore_EPackage" = None, ecore_EClassifier66: "ecore_EGenericType" = None, ecore_EClassifier75: "ecore_EGenericType" = None, ecore_EClassifier82: "ecore_EOperation" = None):
        self.instanceClass = instanceClass
        self.instanceClassName = instanceClassName
        self.defaultValue = defaultValue
        self.instanceTypeName = instanceTypeName
        self.ecore_EClassifier = ecore_EClassifier
        self.eClassifiers = eClassifiers
        self.ecore_EClassifier43 = ecore_EClassifier43 if ecore_EClassifier43 is not None else set()
        self.EClassifier = EClassifier
        self.ecore_EClassifier66 = ecore_EClassifier66
        self.ecore_EClassifier75 = ecore_EClassifier75
        self.ecore_EClassifier82 = ecore_EClassifier82
        
    @property
    def instanceTypeName(self) -> str:
        return self.__instanceTypeName

    @instanceTypeName.setter
    def instanceTypeName(self, instanceTypeName: str):
        self.__instanceTypeName = instanceTypeName

    @property
    def instanceClassName(self) -> str:
        return self.__instanceClassName

    @instanceClassName.setter
    def instanceClassName(self, instanceClassName: str):
        self.__instanceClassName = instanceClassName

    @property
    def instanceClass(self) -> str:
        return self.__instanceClass

    @instanceClass.setter
    def instanceClass(self, instanceClass: str):
        self.__instanceClass = instanceClass

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def ecore_EClassifier(self):
        return self.__ecore_EClassifier

    @ecore_EClassifier.setter
    def ecore_EClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier", None)
        self.__ecore_EClassifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_ETypedElement"):
                opp_val = getattr(old_value, "ecore_ETypedElement", None)
                if opp_val == self:
                    setattr(old_value, "ecore_ETypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_ETypedElement"):
                opp_val = getattr(value, "ecore_ETypedElement", None)
                setattr(value, "ecore_ETypedElement", self)

    @property
    def ecore_EClassifier75(self):
        return self.__ecore_EClassifier75

    @ecore_EClassifier75.setter
    def ecore_EClassifier75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier75", None)
        self.__ecore_EClassifier75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EGenericType74"):
                opp_val = getattr(old_value, "ecore_EGenericType74", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EGenericType74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EGenericType74"):
                opp_val = getattr(value, "ecore_EGenericType74", None)
                setattr(value, "ecore_EGenericType74", self)

    @property
    def ecore_EClassifier43(self):
        return self.__ecore_EClassifier43

    @ecore_EClassifier43.setter
    def ecore_EClassifier43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier43", None)
        self.__ecore_EClassifier43 = value if value is not None else set()
        
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
    def ecore_EClassifier66(self):
        return self.__ecore_EClassifier66

    @ecore_EClassifier66.setter
    def ecore_EClassifier66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier66", None)
        self.__ecore_EClassifier66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EGenericType65"):
                opp_val = getattr(old_value, "ecore_EGenericType65", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EGenericType65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EGenericType65"):
                opp_val = getattr(value, "ecore_EGenericType65", None)
                setattr(value, "ecore_EGenericType65", self)

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
            if hasattr(old_value, "ePackage52"):
                opp_val = getattr(old_value, "ePackage52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ePackage52"):
                opp_val = getattr(value, "ePackage52", None)
                if opp_val is None:
                    setattr(value, "ePackage52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EClassifier82(self):
        return self.__ecore_EClassifier82

    @ecore_EClassifier82.setter
    def ecore_EClassifier82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier82", None)
        self.__ecore_EClassifier82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EOperation81"):
                opp_val = getattr(old_value, "ecore_EOperation81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EOperation81"):
                opp_val = getattr(value, "ecore_EOperation81", None)
                if opp_val is None:
                    setattr(value, "ecore_EOperation81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

    def getClassifierId(self) -> int:
        # TODO: Implement getClassifierId method
        pass

class ecore_EEnumLiteral(ENamedElement):

    def __init__(self, value: int, instance: str, literal: str, EEnumLiteral: "ecore_EEnum" = None, eLiterals: "ecore_EEnum" = None):
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

class ecore_ETypeParameter(ENamedElement):

    pass
class ecore_EPackage(ENamedElement):

    def __init__(self, nsUri: str, nsPrefix: str, EPackage47: "ecore_EPackage" = None, eSuperPackage: set["ecore_EPackage"] = None, EPackage: "ecore_EClassifier" = None, ePackage: "ecore_EFactory" = None, EPackage50: "ecore_EPackage" = None, eSubpackages: "ecore_EPackage" = None, ePackage52: set["ecore_EClassifier"] = None, EPackage54: "ecore_EFactory" = None):
        self.nsUri = nsUri
        self.nsPrefix = nsPrefix
        self.EPackage47 = EPackage47
        self.eSuperPackage = eSuperPackage if eSuperPackage is not None else set()
        self.EPackage = EPackage
        self.ePackage = ePackage
        self.EPackage50 = EPackage50
        self.eSubpackages = eSubpackages
        self.ePackage52 = ePackage52 if ePackage52 is not None else set()
        self.EPackage54 = EPackage54
        
    @property
    def nsPrefix(self) -> str:
        return self.__nsPrefix

    @nsPrefix.setter
    def nsPrefix(self, nsPrefix: str):
        self.__nsPrefix = nsPrefix

    @property
    def nsUri(self) -> str:
        return self.__nsUri

    @nsUri.setter
    def nsUri(self, nsUri: str):
        self.__nsUri = nsUri

    @property
    def ePackage52(self):
        return self.__ePackage52

    @ePackage52.setter
    def ePackage52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__ePackage52", None)
        self.__ePackage52 = value if value is not None else set()
        
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
    def EPackage47(self):
        return self.__EPackage47

    @EPackage47.setter
    def EPackage47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__EPackage47", None)
        self.__EPackage47 = value
        
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
    def EPackage54(self):
        return self.__EPackage54

    @EPackage54.setter
    def EPackage54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__EPackage54", None)
        self.__EPackage54 = value
        
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
    def EPackage50(self):
        return self.__EPackage50

    @EPackage50.setter
    def EPackage50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__EPackage50", None)
        self.__EPackage50 = value
        
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
                if hasattr(item, "EPackage47"):
                    opp_val = getattr(item, "EPackage47", None)
                    
                    if opp_val == self:
                        setattr(item, "EPackage47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EPackage47"):
                    opp_val = getattr(item, "EPackage47", None)
                    
                    setattr(item, "EPackage47", self)
                    

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
            if hasattr(old_value, "EPackage50"):
                opp_val = getattr(old_value, "EPackage50", None)
                if opp_val == self:
                    setattr(old_value, "EPackage50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EPackage50"):
                opp_val = getattr(value, "EPackage50", None)
                setattr(value, "EPackage50", self)

    def getEClassifier(self, name: str) -> EClassifier:
        # TODO: Implement getEClassifier method
        pass

class ecore_ETypedElement(ENamedElement):

    def __init__(self, ordered: bool, unique: bool, lowerBound: int, upperBound: int, many: bool, required: bool, ecore_ETypedElement: "ecore_EClassifier" = None, ecore_ETypedElement4: "ecore_EGenericType" = None):
        self.ordered = ordered
        self.unique = unique
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.many = many
        self.required = required
        self.ecore_ETypedElement = ecore_ETypedElement
        self.ecore_ETypedElement4 = ecore_ETypedElement4
        
    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

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
    def ecore_ETypedElement4(self):
        return self.__ecore_ETypedElement4

    @ecore_ETypedElement4.setter
    def ecore_ETypedElement4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_ETypedElement__ecore_ETypedElement4", None)
        self.__ecore_ETypedElement4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EGenericType"):
                opp_val = getattr(old_value, "ecore_EGenericType", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EGenericType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EGenericType"):
                opp_val = getattr(value, "ecore_EGenericType", None)
                setattr(value, "ecore_EGenericType", self)

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
            if hasattr(old_value, "ecore_EClassifier"):
                opp_val = getattr(old_value, "ecore_EClassifier", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClassifier"):
                opp_val = getattr(value, "ecore_EClassifier", None)
                setattr(value, "ecore_EClassifier", self)

class ecore_EClass(EClassifier):

    def __init__(self, abstract: bool, interface: bool, EClass: "ecore_EStructuralFeature" = None, eContainingClass: set["ecore_EOperation"] = None, ecore_EClass: "ecore_EClass" = None, ecore_EClass6: set["ecore_EClass"] = None, ecore_EClass29: "ecore_EClass" = None, ecore_EClass27: set["ecore_EClass"] = None, ecore_EClass10: set["ecore_EAttribute"] = None, ecore_EClass13: set["ecore_EReference"] = None, ecore_EClass15: set["ecore_EReference"] = None, ecore_EClass18: set["ecore_EAttribute"] = None, ecore_EClass21: set["ecore_EReference"] = None, ecore_EClass24: set["ecore_EOperation"] = None, ecore_EClass26: set["ecore_EStructuralFeature"] = None, ecore_EClass31: "ecore_EAttribute" = None, eContainingClass34: set["ecore_EStructuralFeature"] = None, ecore_EClass36: set["ecore_EGenericType"] = None, ecore_EClass39: set["ecore_EGenericType"] = None, EClass87: "ecore_EOperation" = None, ecore_EClass95: "ecore_EReference" = None):
        self.abstract = abstract
        self.interface = interface
        self.EClass = EClass
        self.eContainingClass = eContainingClass if eContainingClass is not None else set()
        self.ecore_EClass = ecore_EClass
        self.ecore_EClass6 = ecore_EClass6 if ecore_EClass6 is not None else set()
        self.ecore_EClass29 = ecore_EClass29
        self.ecore_EClass27 = ecore_EClass27 if ecore_EClass27 is not None else set()
        self.ecore_EClass10 = ecore_EClass10 if ecore_EClass10 is not None else set()
        self.ecore_EClass13 = ecore_EClass13 if ecore_EClass13 is not None else set()
        self.ecore_EClass15 = ecore_EClass15 if ecore_EClass15 is not None else set()
        self.ecore_EClass18 = ecore_EClass18 if ecore_EClass18 is not None else set()
        self.ecore_EClass21 = ecore_EClass21 if ecore_EClass21 is not None else set()
        self.ecore_EClass24 = ecore_EClass24 if ecore_EClass24 is not None else set()
        self.ecore_EClass26 = ecore_EClass26 if ecore_EClass26 is not None else set()
        self.ecore_EClass31 = ecore_EClass31
        self.eContainingClass34 = eContainingClass34 if eContainingClass34 is not None else set()
        self.ecore_EClass36 = ecore_EClass36 if ecore_EClass36 is not None else set()
        self.ecore_EClass39 = ecore_EClass39 if ecore_EClass39 is not None else set()
        self.EClass87 = EClass87
        self.ecore_EClass95 = ecore_EClass95
        
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
    def EClass(self):
        return self.__EClass

    @EClass.setter
    def EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__EClass", None)
        self.__EClass = value
        
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
                if hasattr(item, "ecore_EAttribute19"):
                    opp_val = getattr(item, "ecore_EAttribute19", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EAttribute19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EAttribute19"):
                    opp_val = getattr(item, "ecore_EAttribute19", None)
                    
                    setattr(item, "ecore_EAttribute19", self)
                    

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
                if hasattr(item, "ecore_EReference22"):
                    opp_val = getattr(item, "ecore_EReference22", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EReference22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EReference22"):
                    opp_val = getattr(item, "ecore_EReference22", None)
                    
                    setattr(item, "ecore_EReference22", self)
                    

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
                if hasattr(item, "ecore_EGenericType40"):
                    opp_val = getattr(item, "ecore_EGenericType40", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EGenericType40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EGenericType40"):
                    opp_val = getattr(item, "ecore_EGenericType40", None)
                    
                    setattr(item, "ecore_EGenericType40", self)
                    

    @property
    def ecore_EClass6(self):
        return self.__ecore_EClass6

    @ecore_EClass6.setter
    def ecore_EClass6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass6", None)
        self.__ecore_EClass6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EClass"):
                    opp_val = getattr(item, "ecore_EClass", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EClass"):
                    opp_val = getattr(item, "ecore_EClass", None)
                    
                    setattr(item, "ecore_EClass", self)
                    

    @property
    def ecore_EClass10(self):
        return self.__ecore_EClass10

    @ecore_EClass10.setter
    def ecore_EClass10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass10", None)
        self.__ecore_EClass10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EAttribute11"):
                    opp_val = getattr(item, "ecore_EAttribute11", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EAttribute11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EAttribute11"):
                    opp_val = getattr(item, "ecore_EAttribute11", None)
                    
                    setattr(item, "ecore_EAttribute11", self)
                    

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
    def ecore_EClass31(self):
        return self.__ecore_EClass31

    @ecore_EClass31.setter
    def ecore_EClass31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass31", None)
        self.__ecore_EClass31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EAttribute32"):
                opp_val = getattr(old_value, "ecore_EAttribute32", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EAttribute32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EAttribute32"):
                opp_val = getattr(value, "ecore_EAttribute32", None)
                setattr(value, "ecore_EAttribute32", self)

    @property
    def ecore_EClass36(self):
        return self.__ecore_EClass36

    @ecore_EClass36.setter
    def ecore_EClass36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass36", None)
        self.__ecore_EClass36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EGenericType37"):
                    opp_val = getattr(item, "ecore_EGenericType37", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EGenericType37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EGenericType37"):
                    opp_val = getattr(item, "ecore_EGenericType37", None)
                    
                    setattr(item, "ecore_EGenericType37", self)
                    

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
                if hasattr(item, "ecore_EReference16"):
                    opp_val = getattr(item, "ecore_EReference16", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EReference16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EReference16"):
                    opp_val = getattr(item, "ecore_EReference16", None)
                    
                    setattr(item, "ecore_EReference16", self)
                    

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
                    

    @property
    def eContainingClass34(self):
        return self.__eContainingClass34

    @eContainingClass34.setter
    def eContainingClass34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__eContainingClass34", None)
        self.__eContainingClass34 = value if value is not None else set()
        
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
    def ecore_EClass95(self):
        return self.__ecore_EClass95

    @ecore_EClass95.setter
    def ecore_EClass95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass95", None)
        self.__ecore_EClass95 = value
        
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
    def ecore_EClass(self):
        return self.__ecore_EClass

    @ecore_EClass.setter
    def ecore_EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass", None)
        self.__ecore_EClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass6"):
                opp_val = getattr(old_value, "ecore_EClass6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass6"):
                opp_val = getattr(value, "ecore_EClass6", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def EClass87(self):
        return self.__EClass87

    @EClass87.setter
    def EClass87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__EClass87", None)
        self.__EClass87 = value
        
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

    def isSuperTypeOf(self, someClass: str) -> bool:
        # TODO: Implement isSuperTypeOf method
        pass

    def getFeatureId(self, feature: EStructuralFeature) -> int:
        # TODO: Implement getFeatureId method
        pass

    def getEStructuralFeature(self, featureId: int) -> EStructuralFeature:
        # TODO: Implement getEStructuralFeature method
        pass

    def getFeatureCount(self) -> int:
        # TODO: Implement getFeatureCount method
        pass

    def getEStructuralFeature(self, featureName: str) -> EStructuralFeature:
        # TODO: Implement getEStructuralFeature method
        pass

class ETypedElement:

    pass
class ecore_EOperation(ETypedElement):

    pass
class ecore_EParameter(ETypedElement):

    pass
class ecore_EStructuralFeature(ETypedElement):

    def __init__(self, derived: bool, changeable: bool, volatile: bool, transient: bool, defaultValueLiteral: str, defaultValue: str, unsettable: bool, eStructuralFeatures: "ecore_EClass" = None, ecore_EStructuralFeature: "ecore_EClass" = None, EStructuralFeature: "ecore_EClass" = None):
        self.derived = derived
        self.changeable = changeable
        self.volatile = volatile
        self.transient = transient
        self.defaultValueLiteral = defaultValueLiteral
        self.defaultValue = defaultValue
        self.unsettable = unsettable
        self.eStructuralFeatures = eStructuralFeatures
        self.ecore_EStructuralFeature = ecore_EStructuralFeature
        self.EStructuralFeature = EStructuralFeature
        
    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def defaultValueLiteral(self) -> str:
        return self.__defaultValueLiteral

    @defaultValueLiteral.setter
    def defaultValueLiteral(self, defaultValueLiteral: str):
        self.__defaultValueLiteral = defaultValueLiteral

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
    def unsettable(self) -> bool:
        return self.__unsettable

    @unsettable.setter
    def unsettable(self, unsettable: bool):
        self.__unsettable = unsettable

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
            if hasattr(old_value, "EClass"):
                opp_val = getattr(old_value, "EClass", None)
                if opp_val == self:
                    setattr(old_value, "EClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EClass"):
                opp_val = getattr(value, "EClass", None)
                setattr(value, "EClass", self)

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
            if hasattr(old_value, "eContainingClass34"):
                opp_val = getattr(old_value, "eContainingClass34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eContainingClass34"):
                opp_val = getattr(value, "eContainingClass34", None)
                if opp_val is None:
                    setattr(value, "eContainingClass34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getContainerClass(self):
        # TODO: Implement getContainerClass method
        pass

    def getFeatureId(self) -> int:
        # TODO: Implement getFeatureId method
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

    def __init__(self, containment: bool, container: bool, resolveProxies: bool, ecore_EReference: "ecore_EClass" = None, ecore_EReference16: "ecore_EClass" = None, ecore_EReference22: "ecore_EClass" = None, ecore_EReference92: "ecore_EReference" = None, ecore_EReference90: "ecore_EReference" = None, ecore_EReference94: "ecore_EClass" = None, ecore_EReference97: set["ecore_EAttribute"] = None):
        self.containment = containment
        self.container = container
        self.resolveProxies = resolveProxies
        self.ecore_EReference = ecore_EReference
        self.ecore_EReference16 = ecore_EReference16
        self.ecore_EReference22 = ecore_EReference22
        self.ecore_EReference92 = ecore_EReference92
        self.ecore_EReference90 = ecore_EReference90
        self.ecore_EReference94 = ecore_EReference94
        self.ecore_EReference97 = ecore_EReference97 if ecore_EReference97 is not None else set()
        
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
    def ecore_EReference92(self):
        return self.__ecore_EReference92

    @ecore_EReference92.setter
    def ecore_EReference92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference92", None)
        self.__ecore_EReference92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EReference90"):
                opp_val = getattr(old_value, "ecore_EReference90", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EReference90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EReference90"):
                opp_val = getattr(value, "ecore_EReference90", None)
                setattr(value, "ecore_EReference90", self)

    @property
    def ecore_EReference90(self):
        return self.__ecore_EReference90

    @ecore_EReference90.setter
    def ecore_EReference90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference90", None)
        self.__ecore_EReference90 = value
        
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

    @property
    def ecore_EReference22(self):
        return self.__ecore_EReference22

    @ecore_EReference22.setter
    def ecore_EReference22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference22", None)
        self.__ecore_EReference22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass21"):
                opp_val = getattr(old_value, "ecore_EClass21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass21"):
                opp_val = getattr(value, "ecore_EClass21", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def ecore_EReference97(self):
        return self.__ecore_EReference97

    @ecore_EReference97.setter
    def ecore_EReference97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference97", None)
        self.__ecore_EReference97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EAttribute98"):
                    opp_val = getattr(item, "ecore_EAttribute98", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EAttribute98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EAttribute98"):
                    opp_val = getattr(item, "ecore_EAttribute98", None)
                    
                    setattr(item, "ecore_EAttribute98", self)
                    

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
            if hasattr(old_value, "ecore_EClass95"):
                opp_val = getattr(old_value, "ecore_EClass95", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EClass95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass95"):
                opp_val = getattr(value, "ecore_EClass95", None)
                setattr(value, "ecore_EClass95", self)

    @property
    def ecore_EReference16(self):
        return self.__ecore_EReference16

    @ecore_EReference16.setter
    def ecore_EReference16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference16", None)
        self.__ecore_EReference16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass15"):
                opp_val = getattr(old_value, "ecore_EClass15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass15"):
                opp_val = getattr(value, "ecore_EClass15", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecore_EAttribute(EStructuralFeature):

    def __init__(self, id: bool, ecore_EAttribute: "ecore_EDataType" = None, ecore_EAttribute11: "ecore_EClass" = None, ecore_EAttribute19: "ecore_EClass" = None, ecore_EAttribute32: "ecore_EClass" = None, ecore_EAttribute98: "ecore_EReference" = None):
        self.id = id
        self.ecore_EAttribute = ecore_EAttribute
        self.ecore_EAttribute11 = ecore_EAttribute11
        self.ecore_EAttribute19 = ecore_EAttribute19
        self.ecore_EAttribute32 = ecore_EAttribute32
        self.ecore_EAttribute98 = ecore_EAttribute98
        
    @property
    def id(self) -> bool:
        return self.__id

    @id.setter
    def id(self, id: bool):
        self.__id = id

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
                if opp_val == self:
                    setattr(old_value, "ecore_EClass31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass31"):
                opp_val = getattr(value, "ecore_EClass31", None)
                setattr(value, "ecore_EClass31", self)

    @property
    def ecore_EAttribute98(self):
        return self.__ecore_EAttribute98

    @ecore_EAttribute98.setter
    def ecore_EAttribute98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAttribute__ecore_EAttribute98", None)
        self.__ecore_EAttribute98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EReference97"):
                opp_val = getattr(old_value, "ecore_EReference97", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EReference97"):
                opp_val = getattr(value, "ecore_EReference97", None)
                if opp_val is None:
                    setattr(value, "ecore_EReference97", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EAttribute19(self):
        return self.__ecore_EAttribute19

    @ecore_EAttribute19.setter
    def ecore_EAttribute19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAttribute__ecore_EAttribute19", None)
        self.__ecore_EAttribute19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass18"):
                opp_val = getattr(old_value, "ecore_EClass18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass18"):
                opp_val = getattr(value, "ecore_EClass18", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass18", set([self]))
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
    def ecore_EAttribute11(self):
        return self.__ecore_EAttribute11

    @ecore_EAttribute11.setter
    def ecore_EAttribute11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAttribute__ecore_EAttribute11", None)
        self.__ecore_EAttribute11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass10"):
                opp_val = getattr(old_value, "ecore_EClass10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass10"):
                opp_val = getattr(value, "ecore_EClass10", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
