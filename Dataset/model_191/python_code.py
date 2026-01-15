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

class ecore_EGenericType(EObject):

    pass
class ENamedElement:

    pass
class ecore_ETypeParameter(ENamedElement):

    pass
class ecore_ETypedElement(ENamedElement):

    def __init__(self, ordered: bool, unique: bool, required: bool, lowerBound: int, upperBound: int, many: bool, ecore_ETypedElement: "ecore_EClassifier" = None, ecore_ETypedElement85: "ecore_EGenericType" = None):
        self.ordered = ordered
        self.unique = unique
        self.required = required
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.many = many
        self.ecore_ETypedElement = ecore_ETypedElement
        self.ecore_ETypedElement85 = ecore_ETypedElement85
        
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
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def ecore_ETypedElement85(self):
        return self.__ecore_ETypedElement85

    @ecore_ETypedElement85.setter
    def ecore_ETypedElement85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_ETypedElement__ecore_ETypedElement85", None)
        self.__ecore_ETypedElement85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EGenericType86"):
                opp_val = getattr(old_value, "ecore_EGenericType86", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EGenericType86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EGenericType86"):
                opp_val = getattr(value, "ecore_EGenericType86", None)
                setattr(value, "ecore_EGenericType86", self)

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
            if hasattr(old_value, "ecore_EClassifier83"):
                opp_val = getattr(old_value, "ecore_EClassifier83", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EClassifier83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClassifier83"):
                opp_val = getattr(value, "ecore_EClassifier83", None)
                setattr(value, "ecore_EClassifier83", self)

class ecore_EEnumLiteral(ENamedElement):

    def __init__(self, instance: str, value: int, literal: str, EEnumLiteral: "ecore_EEnum" = None, eLiterals: "ecore_EEnum" = None):
        self.instance = instance
        self.value = value
        self.literal = literal
        self.EEnumLiteral = EEnumLiteral
        self.eLiterals = eLiterals
        
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
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

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

class ecore_EPackage(ENamedElement):

    def __init__(self, nsURI: str, nsPrefix: str, EPackage: "ecore_EClassifier" = None, EPackage47: "ecore_EFactory" = None, ePackage62: set["ecore_EClassifier"] = None, ePackage: "ecore_EFactory" = None, EPackage65: "ecore_EPackage" = None, eSuperPackage: set["ecore_EPackage"] = None, EPackage68: "ecore_EPackage" = None, eSubpackages: "ecore_EPackage" = None):
        self.nsURI = nsURI
        self.nsPrefix = nsPrefix
        self.EPackage = EPackage
        self.EPackage47 = EPackage47
        self.ePackage62 = ePackage62 if ePackage62 is not None else set()
        self.ePackage = ePackage
        self.EPackage65 = EPackage65
        self.eSuperPackage = eSuperPackage if eSuperPackage is not None else set()
        self.EPackage68 = EPackage68
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
    def EPackage65(self):
        return self.__EPackage65

    @EPackage65.setter
    def EPackage65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__EPackage65", None)
        self.__EPackage65 = value
        
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
                if hasattr(item, "EPackage65"):
                    opp_val = getattr(item, "EPackage65", None)
                    
                    if opp_val == self:
                        setattr(item, "EPackage65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EPackage65"):
                    opp_val = getattr(item, "EPackage65", None)
                    
                    setattr(item, "EPackage65", self)
                    

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
            if hasattr(old_value, "EPackage68"):
                opp_val = getattr(old_value, "EPackage68", None)
                if opp_val == self:
                    setattr(old_value, "EPackage68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EPackage68"):
                opp_val = getattr(value, "EPackage68", None)
                setattr(value, "EPackage68", self)

    @property
    def EPackage68(self):
        return self.__EPackage68

    @EPackage68.setter
    def EPackage68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__EPackage68", None)
        self.__EPackage68 = value
        
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
    def ePackage62(self):
        return self.__ePackage62

    @ePackage62.setter
    def ePackage62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__ePackage62", None)
        self.__ePackage62 = value if value is not None else set()
        
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

class ecore_EClassifier(ENamedElement):

    def __init__(self, instanceClass: str, instanceClassName: str, defaultValue: str, instanceTypeName: str, eClassifiers: "ecore_EPackage" = None, ecore_EClassifier: set["ecore_ETypeParameter"] = None, ecore_EClassifier56: "ecore_EOperation" = None, EClassifier: "ecore_EPackage" = None, ecore_EClassifier83: "ecore_ETypedElement" = None, ecore_EClassifier95: "ecore_EGenericType" = None, ecore_EClassifier104: "ecore_EGenericType" = None):
        self.instanceClass = instanceClass
        self.instanceClassName = instanceClassName
        self.defaultValue = defaultValue
        self.instanceTypeName = instanceTypeName
        self.eClassifiers = eClassifiers
        self.ecore_EClassifier = ecore_EClassifier if ecore_EClassifier is not None else set()
        self.ecore_EClassifier56 = ecore_EClassifier56
        self.EClassifier = EClassifier
        self.ecore_EClassifier83 = ecore_EClassifier83
        self.ecore_EClassifier95 = ecore_EClassifier95
        self.ecore_EClassifier104 = ecore_EClassifier104
        
    @property
    def instanceClass(self) -> str:
        return self.__instanceClass

    @instanceClass.setter
    def instanceClass(self, instanceClass: str):
        self.__instanceClass = instanceClass

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
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

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
            if hasattr(old_value, "ePackage62"):
                opp_val = getattr(old_value, "ePackage62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ePackage62"):
                opp_val = getattr(value, "ePackage62", None)
                if opp_val is None:
                    setattr(value, "ePackage62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EClassifier83(self):
        return self.__ecore_EClassifier83

    @ecore_EClassifier83.setter
    def ecore_EClassifier83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier83", None)
        self.__ecore_EClassifier83 = value
        
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
    def ecore_EClassifier95(self):
        return self.__ecore_EClassifier95

    @ecore_EClassifier95.setter
    def ecore_EClassifier95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier95", None)
        self.__ecore_EClassifier95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EGenericType94"):
                opp_val = getattr(old_value, "ecore_EGenericType94", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EGenericType94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EGenericType94"):
                opp_val = getattr(value, "ecore_EGenericType94", None)
                setattr(value, "ecore_EGenericType94", self)

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
            if hasattr(old_value, "ecore_EGenericType103"):
                opp_val = getattr(old_value, "ecore_EGenericType103", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EGenericType103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EGenericType103"):
                opp_val = getattr(value, "ecore_EGenericType103", None)
                setattr(value, "ecore_EGenericType103", self)

    @property
    def ecore_EClassifier56(self):
        return self.__ecore_EClassifier56

    @ecore_EClassifier56.setter
    def ecore_EClassifier56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier56", None)
        self.__ecore_EClassifier56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EOperation55"):
                opp_val = getattr(old_value, "ecore_EOperation55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EOperation55"):
                opp_val = getattr(value, "ecore_EOperation55", None)
                if opp_val is None:
                    setattr(value, "ecore_EOperation55", set([self]))
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

class ecore_EStructuralFeature(ETypedElement):

    def __init__(self, changeable: bool, unsettable: bool, volatile: bool, transient: bool, defaultValueLiteral: str, defaultValue: str, derived: bool, EStructuralFeature: "ecore_EClass" = None, ecore_EStructuralFeature: "ecore_EClass" = None, eStructuralFeatures: "ecore_EClass" = None):
        self.changeable = changeable
        self.unsettable = unsettable
        self.volatile = volatile
        self.transient = transient
        self.defaultValueLiteral = defaultValueLiteral
        self.defaultValue = defaultValue
        self.derived = derived
        self.EStructuralFeature = EStructuralFeature
        self.ecore_EStructuralFeature = ecore_EStructuralFeature
        self.eStructuralFeatures = eStructuralFeatures
        
    @property
    def defaultValueLiteral(self) -> str:
        return self.__defaultValueLiteral

    @defaultValueLiteral.setter
    def defaultValueLiteral(self, defaultValueLiteral: str):
        self.__defaultValueLiteral = defaultValueLiteral

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
    def volatile(self) -> bool:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: bool):
        self.__volatile = volatile

    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

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
            if hasattr(old_value, "EClass81"):
                opp_val = getattr(old_value, "EClass81", None)
                if opp_val == self:
                    setattr(old_value, "EClass81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EClass81"):
                opp_val = getattr(value, "EClass81", None)
                setattr(value, "EClass81", self)

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
            if hasattr(old_value, "ecore_EClass28"):
                opp_val = getattr(old_value, "ecore_EClass28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass28"):
                opp_val = getattr(value, "ecore_EClass28", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass28", set([self]))
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

    def __init__(self, abstract: bool, interface: bool, ecore_EClass: "ecore_EClass" = None, ecore_EClass8: set["ecore_EClass"] = None, ecore_EClass15: set["ecore_EReference"] = None, ecore_EClass17: set["ecore_EReference"] = None, eContainingClass: set["ecore_EOperation"] = None, ecore_EClass12: set["ecore_EAttribute"] = None, ecore_EClass26: set["ecore_EOperation"] = None, ecore_EClass20: set["ecore_EAttribute"] = None, ecore_EClass23: set["ecore_EReference"] = None, eContainingClass36: set["ecore_EStructuralFeature"] = None, ecore_EClass28: set["ecore_EStructuralFeature"] = None, ecore_EClass31: "ecore_EClass" = None, ecore_EClass29: set["ecore_EClass"] = None, ecore_EClass33: "ecore_EAttribute" = None, ecore_EClass38: set["ecore_EGenericType"] = None, ecore_EClass40: set["ecore_EGenericType"] = None, EClass: "ecore_EOperation" = None, ecore_EClass76: "ecore_EReference" = None, EClass81: "ecore_EStructuralFeature" = None):
        self.abstract = abstract
        self.interface = interface
        self.ecore_EClass = ecore_EClass
        self.ecore_EClass8 = ecore_EClass8 if ecore_EClass8 is not None else set()
        self.ecore_EClass15 = ecore_EClass15 if ecore_EClass15 is not None else set()
        self.ecore_EClass17 = ecore_EClass17 if ecore_EClass17 is not None else set()
        self.eContainingClass = eContainingClass if eContainingClass is not None else set()
        self.ecore_EClass12 = ecore_EClass12 if ecore_EClass12 is not None else set()
        self.ecore_EClass26 = ecore_EClass26 if ecore_EClass26 is not None else set()
        self.ecore_EClass20 = ecore_EClass20 if ecore_EClass20 is not None else set()
        self.ecore_EClass23 = ecore_EClass23 if ecore_EClass23 is not None else set()
        self.eContainingClass36 = eContainingClass36 if eContainingClass36 is not None else set()
        self.ecore_EClass28 = ecore_EClass28 if ecore_EClass28 is not None else set()
        self.ecore_EClass31 = ecore_EClass31
        self.ecore_EClass29 = ecore_EClass29 if ecore_EClass29 is not None else set()
        self.ecore_EClass33 = ecore_EClass33
        self.ecore_EClass38 = ecore_EClass38 if ecore_EClass38 is not None else set()
        self.ecore_EClass40 = ecore_EClass40 if ecore_EClass40 is not None else set()
        self.EClass = EClass
        self.ecore_EClass76 = ecore_EClass76
        self.EClass81 = EClass81
        
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
    def ecore_EClass17(self):
        return self.__ecore_EClass17

    @ecore_EClass17.setter
    def ecore_EClass17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass17", None)
        self.__ecore_EClass17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EReference18"):
                    opp_val = getattr(item, "ecore_EReference18", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EReference18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EReference18"):
                    opp_val = getattr(item, "ecore_EReference18", None)
                    
                    setattr(item, "ecore_EReference18", self)
                    

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
                if hasattr(item, "ecore_EClass31"):
                    opp_val = getattr(item, "ecore_EClass31", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EClass31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EClass31"):
                    opp_val = getattr(item, "ecore_EClass31", None)
                    
                    setattr(item, "ecore_EClass31", self)
                    

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
    def eContainingClass36(self):
        return self.__eContainingClass36

    @eContainingClass36.setter
    def eContainingClass36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__eContainingClass36", None)
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
    def ecore_EClass33(self):
        return self.__ecore_EClass33

    @ecore_EClass33.setter
    def ecore_EClass33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass33", None)
        self.__ecore_EClass33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EAttribute34"):
                opp_val = getattr(old_value, "ecore_EAttribute34", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EAttribute34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EAttribute34"):
                opp_val = getattr(value, "ecore_EAttribute34", None)
                setattr(value, "ecore_EAttribute34", self)

    @property
    def ecore_EClass28(self):
        return self.__ecore_EClass28

    @ecore_EClass28.setter
    def ecore_EClass28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass28", None)
        self.__ecore_EClass28 = value if value is not None else set()
        
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
                if hasattr(item, "ecore_EGenericType41"):
                    opp_val = getattr(item, "ecore_EGenericType41", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EGenericType41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EGenericType41"):
                    opp_val = getattr(item, "ecore_EGenericType41", None)
                    
                    setattr(item, "ecore_EGenericType41", self)
                    

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
    def ecore_EClass31(self):
        return self.__ecore_EClass31

    @ecore_EClass31.setter
    def ecore_EClass31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass31", None)
        self.__ecore_EClass31 = value
        
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

    @property
    def ecore_EClass76(self):
        return self.__ecore_EClass76

    @ecore_EClass76.setter
    def ecore_EClass76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass76", None)
        self.__ecore_EClass76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EReference75"):
                opp_val = getattr(old_value, "ecore_EReference75", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EReference75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EReference75"):
                opp_val = getattr(value, "ecore_EReference75", None)
                setattr(value, "ecore_EReference75", self)

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
                if hasattr(item, "ecore_EAttribute13"):
                    opp_val = getattr(item, "ecore_EAttribute13", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EAttribute13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EAttribute13"):
                    opp_val = getattr(item, "ecore_EAttribute13", None)
                    
                    setattr(item, "ecore_EAttribute13", self)
                    

    @property
    def ecore_EClass20(self):
        return self.__ecore_EClass20

    @ecore_EClass20.setter
    def ecore_EClass20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass20", None)
        self.__ecore_EClass20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EAttribute21"):
                    opp_val = getattr(item, "ecore_EAttribute21", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EAttribute21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EAttribute21"):
                    opp_val = getattr(item, "ecore_EAttribute21", None)
                    
                    setattr(item, "ecore_EAttribute21", self)
                    

    @property
    def EClass81(self):
        return self.__EClass81

    @EClass81.setter
    def EClass81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__EClass81", None)
        self.__EClass81 = value
        
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

    def getFeatureID(self, feature: EStructuralFeature) -> int:
        # TODO: Implement getFeatureID method
        pass

    def isSuperTypeOf(self, someClass: str) -> bool:
        # TODO: Implement isSuperTypeOf method
        pass

    def getEStructuralFeature(self, featureName: str) -> EStructuralFeature:
        # TODO: Implement getEStructuralFeature method
        pass

    def getEStructuralFeature(self, featureID: int) -> EStructuralFeature:
        # TODO: Implement getEStructuralFeature method
        pass

    def getFeatureCount(self) -> int:
        # TODO: Implement getFeatureCount method
        pass

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

class ecore_EObject:

    def __init__(self, ecore_EObject: "ecore_EAnnotation" = None, ecore_EObject7: "ecore_EAnnotation" = None):
        self.ecore_EObject = ecore_EObject
        self.ecore_EObject7 = ecore_EObject7
        
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

    @property
    def ecore_EObject7(self):
        return self.__ecore_EObject7

    @ecore_EObject7.setter
    def ecore_EObject7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EObject__ecore_EObject7", None)
        self.__ecore_EObject7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EAnnotation6"):
                opp_val = getattr(old_value, "ecore_EAnnotation6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EAnnotation6"):
                opp_val = getattr(value, "ecore_EAnnotation6", None)
                if opp_val is None:
                    setattr(value, "ecore_EAnnotation6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def eGet(self, feature: EStructuralFeature) -> str:
        # TODO: Implement eGet method
        pass

    def eGet(self, feature: EStructuralFeature, resolve: bool) -> str:
        # TODO: Implement eGet method
        pass

    def eAllContents(self):
        # TODO: Implement eAllContents method
        pass

    def eContainingFeature(self) -> EStructuralFeature:
        # TODO: Implement eContainingFeature method
        pass

    def eIsProxy(self) -> bool:
        # TODO: Implement eIsProxy method
        pass

    def eResource(self) -> str:
        # TODO: Implement eResource method
        pass

    def eClass(self) -> str:
        # TODO: Implement eClass method
        pass

    def eSet(self, feature: EStructuralFeature, newValue: str):
        # TODO: Implement eSet method
        pass

    def eContainer(self) -> EObject:
        # TODO: Implement eContainer method
        pass

    def eContainmentFeature(self) -> str:
        # TODO: Implement eContainmentFeature method
        pass

    def eIsSet(self, feature: EStructuralFeature) -> bool:
        # TODO: Implement eIsSet method
        pass

    def eCrossReferences(self):
        # TODO: Implement eCrossReferences method
        pass

    def eUnset(self, feature: EStructuralFeature):
        # TODO: Implement eUnset method
        pass

    def eContents(self):
        # TODO: Implement eContents method
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

class EModelElement:

    pass
class ecore_EFactory(EModelElement):

    def __init__(self, eFactoryInstance: "ecore_EPackage" = None, EFactory: "ecore_EPackage" = None):
        self.eFactoryInstance = eFactoryInstance
        self.EFactory = EFactory
        
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

    def createFromString(self, literalValue: str, eDataType: EDataType) -> str:
        # TODO: Implement createFromString method
        pass

    def convertToString(self, eDataType: EDataType, instanceValue: str) -> str:
        # TODO: Implement convertToString method
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

    def __init__(self, source: str, ecore_EAnnotation4: set["ecore_EObject"] = None, ecore_EAnnotation: set["ecore_EStringToStringMapEntry"] = None, eAnnotations: "ecore_EModelElement" = None, ecore_EAnnotation6: set["ecore_EObject"] = None, EAnnotation: "ecore_EModelElement" = None):
        self.source = source
        self.ecore_EAnnotation4 = ecore_EAnnotation4 if ecore_EAnnotation4 is not None else set()
        self.ecore_EAnnotation = ecore_EAnnotation if ecore_EAnnotation is not None else set()
        self.eAnnotations = eAnnotations
        self.ecore_EAnnotation6 = ecore_EAnnotation6 if ecore_EAnnotation6 is not None else set()
        self.EAnnotation = EAnnotation
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

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
                if hasattr(item, "ecore_EObject7"):
                    opp_val = getattr(item, "ecore_EObject7", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EObject7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EObject7"):
                    opp_val = getattr(item, "ecore_EObject7", None)
                    
                    setattr(item, "ecore_EObject7", self)
                    

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

class EStructuralFeature:

    pass
class ecore_EReference(EStructuralFeature):

    def __init__(self, container: bool, containment: bool, resolveProxies: bool, ecore_EReference18: "ecore_EClass" = None, ecore_EReference: "ecore_EClass" = None, ecore_EReference24: "ecore_EClass" = None, ecore_EReference78: set["ecore_EAttribute"] = None, ecore_EReference73: "ecore_EReference" = None, ecore_EReference71: "ecore_EReference" = None, ecore_EReference75: "ecore_EClass" = None):
        self.container = container
        self.containment = containment
        self.resolveProxies = resolveProxies
        self.ecore_EReference18 = ecore_EReference18
        self.ecore_EReference = ecore_EReference
        self.ecore_EReference24 = ecore_EReference24
        self.ecore_EReference78 = ecore_EReference78 if ecore_EReference78 is not None else set()
        self.ecore_EReference73 = ecore_EReference73
        self.ecore_EReference71 = ecore_EReference71
        self.ecore_EReference75 = ecore_EReference75
        
    @property
    def containment(self) -> bool:
        return self.__containment

    @containment.setter
    def containment(self, containment: bool):
        self.__containment = containment

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
    def ecore_EReference71(self):
        return self.__ecore_EReference71

    @ecore_EReference71.setter
    def ecore_EReference71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference71", None)
        self.__ecore_EReference71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EReference73"):
                opp_val = getattr(old_value, "ecore_EReference73", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EReference73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EReference73"):
                opp_val = getattr(value, "ecore_EReference73", None)
                setattr(value, "ecore_EReference73", self)

    @property
    def ecore_EReference73(self):
        return self.__ecore_EReference73

    @ecore_EReference73.setter
    def ecore_EReference73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference73", None)
        self.__ecore_EReference73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EReference71"):
                opp_val = getattr(old_value, "ecore_EReference71", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EReference71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EReference71"):
                opp_val = getattr(value, "ecore_EReference71", None)
                setattr(value, "ecore_EReference71", self)

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

    @property
    def ecore_EReference78(self):
        return self.__ecore_EReference78

    @ecore_EReference78.setter
    def ecore_EReference78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference78", None)
        self.__ecore_EReference78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EAttribute79"):
                    opp_val = getattr(item, "ecore_EAttribute79", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EAttribute79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EAttribute79"):
                    opp_val = getattr(item, "ecore_EAttribute79", None)
                    
                    setattr(item, "ecore_EAttribute79", self)
                    

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
    def ecore_EReference18(self):
        return self.__ecore_EReference18

    @ecore_EReference18.setter
    def ecore_EReference18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference18", None)
        self.__ecore_EReference18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass17"):
                opp_val = getattr(old_value, "ecore_EClass17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass17"):
                opp_val = getattr(value, "ecore_EClass17", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EReference75(self):
        return self.__ecore_EReference75

    @ecore_EReference75.setter
    def ecore_EReference75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference75", None)
        self.__ecore_EReference75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass76"):
                opp_val = getattr(old_value, "ecore_EClass76", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EClass76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass76"):
                opp_val = getattr(value, "ecore_EClass76", None)
                setattr(value, "ecore_EClass76", self)

class ecore_EAttribute(EStructuralFeature):

    def __init__(self, iD: bool, ecore_EAttribute: "ecore_EDataType" = None, ecore_EAttribute13: "ecore_EClass" = None, ecore_EAttribute21: "ecore_EClass" = None, ecore_EAttribute34: "ecore_EClass" = None, ecore_EAttribute79: "ecore_EReference" = None):
        self.iD = iD
        self.ecore_EAttribute = ecore_EAttribute
        self.ecore_EAttribute13 = ecore_EAttribute13
        self.ecore_EAttribute21 = ecore_EAttribute21
        self.ecore_EAttribute34 = ecore_EAttribute34
        self.ecore_EAttribute79 = ecore_EAttribute79
        
    @property
    def iD(self) -> bool:
        return self.__iD

    @iD.setter
    def iD(self, iD: bool):
        self.__iD = iD

    @property
    def ecore_EAttribute34(self):
        return self.__ecore_EAttribute34

    @ecore_EAttribute34.setter
    def ecore_EAttribute34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAttribute__ecore_EAttribute34", None)
        self.__ecore_EAttribute34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass33"):
                opp_val = getattr(old_value, "ecore_EClass33", None)
                if opp_val == self:
                    setattr(old_value, "ecore_EClass33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass33"):
                opp_val = getattr(value, "ecore_EClass33", None)
                setattr(value, "ecore_EClass33", self)

    @property
    def ecore_EAttribute21(self):
        return self.__ecore_EAttribute21

    @ecore_EAttribute21.setter
    def ecore_EAttribute21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAttribute__ecore_EAttribute21", None)
        self.__ecore_EAttribute21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EClass20"):
                opp_val = getattr(old_value, "ecore_EClass20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EClass20"):
                opp_val = getattr(value, "ecore_EClass20", None)
                if opp_val is None:
                    setattr(value, "ecore_EClass20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EAttribute79(self):
        return self.__ecore_EAttribute79

    @ecore_EAttribute79.setter
    def ecore_EAttribute79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAttribute__ecore_EAttribute79", None)
        self.__ecore_EAttribute79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_EReference78"):
                opp_val = getattr(old_value, "ecore_EReference78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_EReference78"):
                opp_val = getattr(value, "ecore_EReference78", None)
                if opp_val is None:
                    setattr(value, "ecore_EReference78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_EAttribute13(self):
        return self.__ecore_EAttribute13

    @ecore_EAttribute13.setter
    def ecore_EAttribute13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAttribute__ecore_EAttribute13", None)
        self.__ecore_EAttribute13 = value
        
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
