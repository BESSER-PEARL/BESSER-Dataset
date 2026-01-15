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

    def getEEnumLiteral(self, name: str) -> str:
        # TODO: Implement getEEnumLiteral method
        pass

    def getEEnumLiteral(self, value: int) -> str:
        # TODO: Implement getEEnumLiteral method
        pass

    def getEEnumLiteralByLiteral(self, literal: str) -> str:
        # TODO: Implement getEEnumLiteralByLiteral method
        pass

class EStructuralFeature:

    pass
class ecore_EStructuralFeature_Wildcard:

    pass
class ETypedElement:

    pass
class ecore_EParameter(ETypedElement):

    pass
class ecore_EClassifier_Wildcard:

    pass
class ENamedElement:

    pass
class ecore_ETypedElement(ENamedElement):

    def __init__(self, ordered: bool, unique: bool, lowerBound: int, upperBound: int, many: bool, required: bool, ecore_ETypedElement: "ecore_EClassifier" = None, ecore_ETypedElement89: "ecore_EGenericType" = None):
        self.ordered = ordered
        self.unique = unique
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.many = many
        self.required = required
        self.ecore_ETypedElement = ecore_ETypedElement
        self.ecore_ETypedElement89 = ecore_ETypedElement89
        
    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

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
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

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
            if hasattr(old_value, "ecore_EClassifier87"):
                opp_val = getattr(old_value, "ecore_EClassifier87", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EClassifier87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClassifier87"):
                opp_val = getattr(value, "ecore_EClassifier87", None)
                setattr(value, "ecore_EClassifier87", self)

    @property
    def ecore_ETypedElement89(self):
        return self.__ecore_ETypedElement89

    @ecore_ETypedElement89.setter
    def ecore_ETypedElement89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_ETypedElement__ecore_ETypedElement89", None)
        self.__ecore_ETypedElement89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EGenericType90"):
                opp_val = getattr(old_value, "ecore_EGenericType90", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EGenericType90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EGenericType90"):
                opp_val = getattr(value, "ecore_EGenericType90", None)
                setattr(value, "ecore_EGenericType90", self)

class ecore_EPackage(ENamedElement):

    def __init__(self, nsURI: str, nsPrefix: str, EPackage: "ecore_EClassifier" = None, eSubpackages: "ecore_EPackage" = None, ePackage51: set["ecore_EClassifier"] = None, ePackage: "ecore_EFactory" = None, EPackage46: "ecore_EPackage" = None, eSuperPackage: set["ecore_EPackage"] = None, EPackage49: "ecore_EPackage" = None, EPackage53: "ecore_EFactory" = None):
        self.nsURI = nsURI
        self.nsPrefix = nsPrefix
        self.EPackage = EPackage
        self.eSubpackages = eSubpackages
        self.ePackage51 = ePackage51 if ePackage51 is not None else set()
        self.ePackage = ePackage
        self.EPackage46 = EPackage46
        self.eSuperPackage = eSuperPackage if eSuperPackage is not None else set()
        self.EPackage49 = EPackage49
        self.EPackage53 = EPackage53
        
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
    def EPackage49(self):
        return self.__EPackage49

    @EPackage49.setter
    def EPackage49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__EPackage49", None)
        self.__EPackage49 = value
        
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
                if hasattr(item, "EPackage46"):
                    opp_val = getattr(item, "EPackage46", None)
                    
                    if opp_val == self:
                        setattr(item, "EPackage46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EPackage46"):
                    opp_val = getattr(item, "EPackage46", None)
                    
                    setattr(item, "EPackage46", self)
                    

    @property
    def EPackage53(self):
        return self.__EPackage53

    @EPackage53.setter
    def EPackage53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__EPackage53", None)
        self.__EPackage53 = value
        
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
            if hasattr(old_value, "EPackage49"):
                opp_val = getattr(old_value, "EPackage49", None)
                if opp_val == self:
                    setattr(old_value, "EPackage49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EPackage49"):
                opp_val = getattr(value, "EPackage49", None)
                setattr(value, "EPackage49", self)

    @property
    def EPackage46(self):
        return self.__EPackage46

    @EPackage46.setter
    def EPackage46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__EPackage46", None)
        self.__EPackage46 = value
        
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
                    

    def getEClassifier(self, name: str) -> EClassifier:
        # TODO: Implement getEClassifier method
        pass

class ecore_ETypeParameter(ENamedElement):

    pass
class ecore_EEnumLiteral(ENamedElement):

    def __init__(self, value: int, instance: str, literal: str, EEnumLiteral: "ecore_EEnum" = None, eLiterals: "ecore_EEnum" = None):
        self.value = value
        self.instance = instance
        self.literal = literal
        self.EEnumLiteral = EEnumLiteral
        self.eLiterals = eLiterals
        
    @property
    def instance(self) -> str:
        return self.__instance

    @instance.setter
    def instance(self, instance: str):
        self.__instance = instance

    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

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

class ecore_EClassifier(ENamedElement):

    def __init__(self, instanceClassName: str, instanceClass: str, defaultValue: str, instanceTypeName: str, ecore_EClassifier: set["ecore_ETypeParameter"] = None, eClassifiers: "ecore_EPackage" = None, EClassifier: "ecore_EPackage" = None, ecore_EClassifier74: "ecore_EGenericType" = None, ecore_EClassifier65: "ecore_EGenericType" = None, ecore_EClassifier81: "ecore_EOperation" = None, ecore_EClassifier87: "ecore_ETypedElement" = None):
        self.instanceClassName = instanceClassName
        self.instanceClass = instanceClass
        self.defaultValue = defaultValue
        self.instanceTypeName = instanceTypeName
        self.ecore_EClassifier = ecore_EClassifier if ecore_EClassifier is not None else set()
        self.eClassifiers = eClassifiers
        self.EClassifier = EClassifier
        self.ecore_EClassifier74 = ecore_EClassifier74
        self.ecore_EClassifier65 = ecore_EClassifier65
        self.ecore_EClassifier81 = ecore_EClassifier81
        self.ecore_EClassifier87 = ecore_EClassifier87
        
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
    def ecore_EClassifier65(self):
        return self.__ecore_EClassifier65

    @ecore_EClassifier65.setter
    def ecore_EClassifier65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier65", None)
        self.__ecore_EClassifier65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EGenericType64"):
                opp_val = getattr(old_value, "ecore_EGenericType64", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EGenericType64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EGenericType64"):
                opp_val = getattr(value, "ecore_EGenericType64", None)
                setattr(value, "ecore_EGenericType64", self)

    @property
    def ecore_EClassifier81(self):
        return self.__ecore_EClassifier81

    @ecore_EClassifier81.setter
    def ecore_EClassifier81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier81", None)
        self.__ecore_EClassifier81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EOperation80"):
                opp_val = getattr(old_value, "ecore_EOperation80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EOperation80"):
                opp_val = getattr(value, "ecore_EOperation80", None)
                if opp_val is None:
                    setattr(value, "ecore_EOperation80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EClassifier87(self):
        return self.__ecore_EClassifier87

    @ecore_EClassifier87.setter
    def ecore_EClassifier87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier87", None)
        self.__ecore_EClassifier87 = value
        
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
    def EClassifier(self):
        return self.__EClassifier

    @EClassifier.setter
    def EClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__EClassifier", None)
        self.__EClassifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ePackage51"):
                opp_val = getattr(old_value, "ePackage51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ePackage51"):
                opp_val = getattr(value, "ePackage51", None)
                if opp_val is None:
                    setattr(value, "ePackage51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EClassifier74(self):
        return self.__ecore_EClassifier74

    @ecore_EClassifier74.setter
    def ecore_EClassifier74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier74", None)
        self.__ecore_EClassifier74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EGenericType73"):
                opp_val = getattr(old_value, "ecore_EGenericType73", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EGenericType73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EGenericType73"):
                opp_val = getattr(value, "ecore_EGenericType73", None)
                setattr(value, "ecore_EGenericType73", self)

    def isInstance(self, object: str) -> bool:
        # TODO: Implement isInstance method
        pass

    def getClassifierID(self) -> int:
        # TODO: Implement getClassifierID method
        pass

class ecore_EReference(EStructuralFeature):

    def __init__(self, containment: bool, container: bool, resolveProxies: bool, ecore_EReference: "ecore_EClass" = None, ecore_EReference19: "ecore_EClass" = None, ecore_EReference25: "ecore_EClass" = None, ecore_EReference99: "ecore_EReference" = None, ecore_EReference97: "ecore_EReference" = None, ecore_EReference101: "ecore_EClass" = None, ecore_EReference104: set["ecore_EAttribute"] = None):
        self.containment = containment
        self.container = container
        self.resolveProxies = resolveProxies
        self.ecore_EReference = ecore_EReference
        self.ecore_EReference19 = ecore_EReference19
        self.ecore_EReference25 = ecore_EReference25
        self.ecore_EReference99 = ecore_EReference99
        self.ecore_EReference97 = ecore_EReference97
        self.ecore_EReference101 = ecore_EReference101
        self.ecore_EReference104 = ecore_EReference104 if ecore_EReference104 is not None else set()
        
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
    def containment(self) -> bool:
        return self.__containment

    @containment.setter
    def containment(self, containment: bool):
        self.__containment = containment

    @property
    def ecore_EReference97(self):
        return self.__ecore_EReference97

    @ecore_EReference97.setter
    def ecore_EReference97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference97", None)
        self.__ecore_EReference97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EReference99"):
                opp_val = getattr(old_value, "ecore_EReference99", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EReference99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EReference99"):
                opp_val = getattr(value, "ecore_EReference99", None)
                setattr(value, "ecore_EReference99", self)

    @property
    def ecore_EReference104(self):
        return self.__ecore_EReference104

    @ecore_EReference104.setter
    def ecore_EReference104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference104", None)
        self.__ecore_EReference104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EAttribute105"):
                    opp_val = getattr(item, "ecore_EAttribute105", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EAttribute105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EAttribute105"):
                    opp_val = getattr(item, "ecore_EAttribute105", None)
                    
                    setattr(item, "ecore_EAttribute105", self)
                    

    @property
    def ecore_EReference101(self):
        return self.__ecore_EReference101

    @ecore_EReference101.setter
    def ecore_EReference101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference101", None)
        self.__ecore_EReference101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass102"):
                opp_val = getattr(old_value, "ecore_EClass102", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EClass102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass102"):
                opp_val = getattr(value, "ecore_EClass102", None)
                setattr(value, "ecore_EClass102", self)

    @property
    def ecore_EReference19(self):
        return self.__ecore_EReference19

    @ecore_EReference19.setter
    def ecore_EReference19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference19", None)
        self.__ecore_EReference19 = value
        
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
    def ecore_EReference25(self):
        return self.__ecore_EReference25

    @ecore_EReference25.setter
    def ecore_EReference25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference25", None)
        self.__ecore_EReference25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass24"):
                opp_val = getattr(old_value, "ecore_EClass24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass24"):
                opp_val = getattr(value, "ecore_EClass24", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EReference99(self):
        return self.__ecore_EReference99

    @ecore_EReference99.setter
    def ecore_EReference99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference99", None)
        self.__ecore_EReference99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EReference97"):
                opp_val = getattr(old_value, "ecore_EReference97", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EReference97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EReference97"):
                opp_val = getattr(value, "ecore_EReference97", None)
                setattr(value, "ecore_EReference97", self)

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

class ecore_EStructuralFeature(ETypedElement):

    def __init__(self, transient: bool, defaultValueLiteral: str, defaultValue: str, unsettable: bool, derived: bool, changeable: bool, volatile: bool, EStructuralFeature: "ecore_EClass" = None, ecore_EStructuralFeature: "ecore_EClass" = None, eStructuralFeatures: "ecore_EClass" = None):
        self.transient = transient
        self.defaultValueLiteral = defaultValueLiteral
        self.defaultValue = defaultValue
        self.unsettable = unsettable
        self.derived = derived
        self.changeable = changeable
        self.volatile = volatile
        self.EStructuralFeature = EStructuralFeature
        self.ecore_EStructuralFeature = ecore_EStructuralFeature
        self.eStructuralFeatures = eStructuralFeatures
        
    @property
    def changeable(self) -> bool:
        return self.__changeable

    @changeable.setter
    def changeable(self, changeable: bool):
        self.__changeable = changeable

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
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

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
            if hasattr(old_value, "EClass96"):
                opp_val = getattr(old_value, "EClass96", None)
                if opp_val == self:
                    setattr(old_value, "EClass96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EClass96"):
                opp_val = getattr(value, "EClass96", None)
                setattr(value, "EClass96", self)

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
            if hasattr(old_value, "eContainingClass14"):
                opp_val = getattr(old_value, "eContainingClass14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eContainingClass14"):
                opp_val = getattr(value, "eContainingClass14", None)
                if opp_val is None:
                    setattr(value, "eContainingClass14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "ecore_EClass29"):
                opp_val = getattr(old_value, "ecore_EClass29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass29"):
                opp_val = getattr(value, "ecore_EClass29", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getContainerClass(self) -> str:
        # TODO: Implement getContainerClass method
        pass

    def getFeatureID(self) -> int:
        # TODO: Implement getFeatureID method
        pass

class ecore_EAttribute(EStructuralFeature):

    def __init__(self, iD: bool, ecore_EAttribute: "ecore_EClass" = None, ecore_EAttribute22: "ecore_EClass" = None, ecore_EAttribute35: "ecore_EClass" = None, ecore_EAttribute94: "ecore_EDataType" = None, ecore_EAttribute105: "ecore_EReference" = None):
        self.iD = iD
        self.ecore_EAttribute = ecore_EAttribute
        self.ecore_EAttribute22 = ecore_EAttribute22
        self.ecore_EAttribute35 = ecore_EAttribute35
        self.ecore_EAttribute94 = ecore_EAttribute94
        self.ecore_EAttribute105 = ecore_EAttribute105
        
    @property
    def iD(self) -> bool:
        return self.__iD

    @iD.setter
    def iD(self, iD: bool):
        self.__iD = iD

    @property
    def ecore_EAttribute94(self):
        return self.__ecore_EAttribute94

    @ecore_EAttribute94.setter
    def ecore_EAttribute94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAttribute__ecore_EAttribute94", None)
        self.__ecore_EAttribute94 = value
        
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

    @property
    def ecore_EAttribute105(self):
        return self.__ecore_EAttribute105

    @ecore_EAttribute105.setter
    def ecore_EAttribute105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAttribute__ecore_EAttribute105", None)
        self.__ecore_EAttribute105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EReference104"):
                opp_val = getattr(old_value, "ecore_EReference104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EReference104"):
                opp_val = getattr(value, "ecore_EReference104", None)
                if opp_val is None:
                    setattr(value, "ecore_EReference104", set([self]))
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
            if hasattr(old_value, "ecore_EClass12"):
                opp_val = getattr(old_value, "ecore_EClass12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass12"):
                opp_val = getattr(value, "ecore_EClass12", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EAttribute22(self):
        return self.__ecore_EAttribute22

    @ecore_EAttribute22.setter
    def ecore_EAttribute22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAttribute__ecore_EAttribute22", None)
        self.__ecore_EAttribute22 = value
        
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

class ecore_EOperation(ETypedElement):

    pass
class EObject:

    pass
class ecore_EGenericType(EObject):

    pass
class ecore_EObject:

    def __init__(self, ecore_EObject: "ecore_EAnnotation" = None, ecore_EObject6: "ecore_EAnnotation" = None):
        self.ecore_EObject = ecore_EObject
        self.ecore_EObject6 = ecore_EObject6
        
    @property
    def ecore_EObject6(self):
        return self.__ecore_EObject6

    @ecore_EObject6.setter
    def ecore_EObject6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EObject__ecore_EObject6", None)
        self.__ecore_EObject6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EAnnotation5"):
                opp_val = getattr(old_value, "ecore_EAnnotation5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EAnnotation5"):
                opp_val = getattr(value, "ecore_EAnnotation5", None)
                if opp_val is None:
                    setattr(value, "ecore_EAnnotation5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "ecore_EAnnotation3"):
                opp_val = getattr(old_value, "ecore_EAnnotation3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EAnnotation3"):
                opp_val = getattr(value, "ecore_EAnnotation3", None)
                if opp_val is None:
                    setattr(value, "ecore_EAnnotation3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def eAllContents(self) -> str:
        # TODO: Implement eAllContents method
        pass

    def eResource(self) -> str:
        # TODO: Implement eResource method
        pass

    def eClass(self) -> str:
        # TODO: Implement eClass method
        pass

    def eGet(self, feature: str) -> str:
        # TODO: Implement eGet method
        pass

    def eUnset(self, feature: str):
        # TODO: Implement eUnset method
        pass

    def eIsProxy(self) -> bool:
        # TODO: Implement eIsProxy method
        pass

    def eIsSet(self, feature: str) -> bool:
        # TODO: Implement eIsSet method
        pass

    def eGet(self, feature: str, resolve: bool) -> str:
        # TODO: Implement eGet method
        pass

    def eContainer(self) -> EObject:
        # TODO: Implement eContainer method
        pass

    def eContainingFeature(self) -> str:
        # TODO: Implement eContainingFeature method
        pass

    def eContents(self) -> str:
        # TODO: Implement eContents method
        pass

    def eCrossReferences(self) -> str:
        # TODO: Implement eCrossReferences method
        pass

    def eSet(self, newValue: str, feature: str):
        # TODO: Implement eSet method
        pass

    def eContainmentFeature(self) -> str:
        # TODO: Implement eContainmentFeature method
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
            if hasattr(old_value, "ecore_EAttribute94"):
                opp_val = getattr(old_value, "ecore_EAttribute94", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EAttribute94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EAttribute94"):
                opp_val = getattr(value, "ecore_EAttribute94", None)
                setattr(value, "ecore_EAttribute94", self)

class ecore_EClass(EClassifier):

    def __init__(self, abstract: bool, interface: bool, ecore_EClass: "ecore_EClass" = None, ecore_EClass8: set["ecore_EClass"] = None, eContainingClass: set["ecore_EOperation"] = None, ecore_EClass12: set["ecore_EAttribute"] = None, eContainingClass14: set["ecore_EStructuralFeature"] = None, ecore_EClass16: set["ecore_EReference"] = None, ecore_EClass39: set["ecore_EGenericType"] = None, ecore_EClass18: set["ecore_EReference"] = None, ecore_EClass21: set["ecore_EAttribute"] = None, ecore_EClass24: set["ecore_EReference"] = None, ecore_EClass27: set["ecore_EOperation"] = None, ecore_EClass29: set["ecore_EStructuralFeature"] = None, ecore_EClass32: "ecore_EClass" = None, ecore_EClass30: set["ecore_EClass"] = None, ecore_EClass34: "ecore_EAttribute" = None, ecore_EClass37: set["ecore_EGenericType"] = None, EClass: "ecore_EOperation" = None, EClass96: "ecore_EStructuralFeature" = None, ecore_EClass102: "ecore_EReference" = None):
        self.abstract = abstract
        self.interface = interface
        self.ecore_EClass = ecore_EClass
        self.ecore_EClass8 = ecore_EClass8 if ecore_EClass8 is not None else set()
        self.eContainingClass = eContainingClass if eContainingClass is not None else set()
        self.ecore_EClass12 = ecore_EClass12 if ecore_EClass12 is not None else set()
        self.eContainingClass14 = eContainingClass14 if eContainingClass14 is not None else set()
        self.ecore_EClass16 = ecore_EClass16 if ecore_EClass16 is not None else set()
        self.ecore_EClass39 = ecore_EClass39 if ecore_EClass39 is not None else set()
        self.ecore_EClass18 = ecore_EClass18 if ecore_EClass18 is not None else set()
        self.ecore_EClass21 = ecore_EClass21 if ecore_EClass21 is not None else set()
        self.ecore_EClass24 = ecore_EClass24 if ecore_EClass24 is not None else set()
        self.ecore_EClass27 = ecore_EClass27 if ecore_EClass27 is not None else set()
        self.ecore_EClass29 = ecore_EClass29 if ecore_EClass29 is not None else set()
        self.ecore_EClass32 = ecore_EClass32
        self.ecore_EClass30 = ecore_EClass30 if ecore_EClass30 is not None else set()
        self.ecore_EClass34 = ecore_EClass34
        self.ecore_EClass37 = ecore_EClass37 if ecore_EClass37 is not None else set()
        self.EClass = EClass
        self.EClass96 = EClass96
        self.ecore_EClass102 = ecore_EClass102
        
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
    def ecore_EClass(self):
        return self.__ecore_EClass

    @ecore_EClass.setter
    def ecore_EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass", None)
        self.__ecore_EClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass8"):
                opp_val = getattr(old_value, "ecore_EClass8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass8"):
                opp_val = getattr(value, "ecore_EClass8", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                    

    @property
    def ecore_EClass30(self):
        return self.__ecore_EClass30

    @ecore_EClass30.setter
    def ecore_EClass30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass30", None)
        self.__ecore_EClass30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EClass32"):
                    opp_val = getattr(item, "ecore_EClass32", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EClass32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EClass32"):
                    opp_val = getattr(item, "ecore_EClass32", None)
                    
                    setattr(item, "ecore_EClass32", self)
                    

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
            if hasattr(old_value, "ecore_EClass30"):
                opp_val = getattr(old_value, "ecore_EClass30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass30"):
                opp_val = getattr(value, "ecore_EClass30", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "ecore_EReference19"):
                    opp_val = getattr(item, "ecore_EReference19", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EReference19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EReference19"):
                    opp_val = getattr(item, "ecore_EReference19", None)
                    
                    setattr(item, "ecore_EReference19", self)
                    

    @property
    def ecore_EClass102(self):
        return self.__ecore_EClass102

    @ecore_EClass102.setter
    def ecore_EClass102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass102", None)
        self.__ecore_EClass102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EReference101"):
                opp_val = getattr(old_value, "ecore_EReference101", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EReference101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EReference101"):
                opp_val = getattr(value, "ecore_EReference101", None)
                setattr(value, "ecore_EReference101", self)

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
    def EClass96(self):
        return self.__EClass96

    @EClass96.setter
    def EClass96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__EClass96", None)
        self.__EClass96 = value
        
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
                if hasattr(item, "ecore_EAttribute22"):
                    opp_val = getattr(item, "ecore_EAttribute22", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EAttribute22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EAttribute22"):
                    opp_val = getattr(item, "ecore_EAttribute22", None)
                    
                    setattr(item, "ecore_EAttribute22", self)
                    

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
                if hasattr(item, "ecore_EReference25"):
                    opp_val = getattr(item, "ecore_EReference25", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EReference25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EReference25"):
                    opp_val = getattr(item, "ecore_EReference25", None)
                    
                    setattr(item, "ecore_EReference25", self)
                    

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
    def eContainingClass14(self):
        return self.__eContainingClass14

    @eContainingClass14.setter
    def eContainingClass14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__eContainingClass14", None)
        self.__eContainingClass14 = value if value is not None else set()
        
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
    def ecore_EClass8(self):
        return self.__ecore_EClass8

    @ecore_EClass8.setter
    def ecore_EClass8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass8", None)
        self.__ecore_EClass8 = value if value is not None else set()
        
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
    def ecore_EClass12(self):
        return self.__ecore_EClass12

    @ecore_EClass12.setter
    def ecore_EClass12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass12", None)
        self.__ecore_EClass12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EAttribute"):
                    opp_val = getattr(item, "ecore_EAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EAttribute"):
                    opp_val = getattr(item, "ecore_EAttribute", None)
                    
                    setattr(item, "ecore_EAttribute", self)
                    

    def getEStructuralFeature(self, featureName: str) -> str:
        # TODO: Implement getEStructuralFeature method
        pass

    def getEStructuralFeature(self, featureID: int) -> str:
        # TODO: Implement getEStructuralFeature method
        pass

    def getFeatureID(self, feature: str) -> int:
        # TODO: Implement getFeatureID method
        pass

    def isSuperTypeOf(self, someClass: str) -> bool:
        # TODO: Implement isSuperTypeOf method
        pass

    def getFeatureCount(self) -> int:
        # TODO: Implement getFeatureCount method
        pass

class ecore_EModelElement(EObject):

    def __init__(self, EModelElement: "ecore_EAnnotation" = None, eModelElement: set["ecore_EAnnotation"] = None):
        self.EModelElement = EModelElement
        self.eModelElement = eModelElement if eModelElement is not None else set()
        
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

    def getEAnnotation(self, source: str) -> str:
        # TODO: Implement getEAnnotation method
        pass

class EModelElement:

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

class ecore_EFactory(EModelElement):

    def __init__(self, EFactory: "ecore_EPackage" = None, eFactoryInstance: "ecore_EPackage" = None):
        self.EFactory = EFactory
        self.eFactoryInstance = eFactoryInstance
        
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
            if hasattr(old_value, "EPackage53"):
                opp_val = getattr(old_value, "EPackage53", None)
                if opp_val == self:
                    setattr(old_value, "EPackage53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EPackage53"):
                opp_val = getattr(value, "EPackage53", None)
                setattr(value, "EPackage53", self)

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

    def convertToString(self, instanceValue: str, eDataType: str) -> str:
        # TODO: Implement convertToString method
        pass

    def create(self, eClass: str) -> EObject:
        # TODO: Implement create method
        pass

    def createFromString(self, eDataType: str, literalValue: str) -> str:
        # TODO: Implement createFromString method
        pass

class ecore_EAnnotation(EModelElement):

    def __init__(self, source: str, eAnnotations: "ecore_EModelElement" = None, ecore_EAnnotation: set["ecore_EStringToStringMapEntry"] = None, ecore_EAnnotation3: set["ecore_EObject"] = None, ecore_EAnnotation5: set["ecore_EObject"] = None, EAnnotation: "ecore_EModelElement" = None):
        self.source = source
        self.eAnnotations = eAnnotations
        self.ecore_EAnnotation = ecore_EAnnotation if ecore_EAnnotation is not None else set()
        self.ecore_EAnnotation3 = ecore_EAnnotation3 if ecore_EAnnotation3 is not None else set()
        self.ecore_EAnnotation5 = ecore_EAnnotation5 if ecore_EAnnotation5 is not None else set()
        self.EAnnotation = EAnnotation
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def ecore_EAnnotation5(self):
        return self.__ecore_EAnnotation5

    @ecore_EAnnotation5.setter
    def ecore_EAnnotation5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAnnotation__ecore_EAnnotation5", None)
        self.__ecore_EAnnotation5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EObject6"):
                    opp_val = getattr(item, "ecore_EObject6", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EObject6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EObject6"):
                    opp_val = getattr(item, "ecore_EObject6", None)
                    
                    setattr(item, "ecore_EObject6", self)
                    

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
    def ecore_EAnnotation3(self):
        return self.__ecore_EAnnotation3

    @ecore_EAnnotation3.setter
    def ecore_EAnnotation3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAnnotation__ecore_EAnnotation3", None)
        self.__ecore_EAnnotation3 = value if value is not None else set()
        
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
