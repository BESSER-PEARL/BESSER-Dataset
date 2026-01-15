from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ETypedElement:

    pass
class ecoreO_EParameter(ETypedElement):

    pass
class EDataType:

    pass
class ecoreO_EEnum(EDataType):

    def __init__(self, EEnum: "ecoreO_EEnumLiteral" = None, eEnum: set["ecoreO_EEnumLiteral"] = None):
        self.EEnum = EEnum
        self.eEnum = eEnum if eEnum is not None else set()
        
    @property
    def EEnum(self):
        return self.__EEnum

    @EEnum.setter
    def EEnum(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EEnum__EEnum", None)
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
        old_value = getattr(self, f"_ecoreO_EEnum__eEnum", None)
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
                    

    def getEEnumLiteral(self, value: int) -> str:
        # TODO: Implement getEEnumLiteral method
        pass

    def getEEnumLiteralByLiteral(self, literal: str) -> str:
        # TODO: Implement getEEnumLiteralByLiteral method
        pass

    def getEEnumLiteral(self, name: str) -> str:
        # TODO: Implement getEEnumLiteral method
        pass

class ENamedElement:

    pass
class ecoreO_EEnumLiteral(ENamedElement):

    def __init__(self, literal: str, value: int, instance: str, eLiterals: "ecoreO_EEnum" = None, EEnumLiteral: "ecoreO_EEnum" = None):
        self.literal = literal
        self.value = value
        self.instance = instance
        self.eLiterals = eLiterals
        self.EEnumLiteral = EEnumLiteral
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

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
    def EEnumLiteral(self):
        return self.__EEnumLiteral

    @EEnumLiteral.setter
    def EEnumLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EEnumLiteral__EEnumLiteral", None)
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
        old_value = getattr(self, f"_ecoreO_EEnumLiteral__eLiterals", None)
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

class ecoreO_ETypedElement(ENamedElement):

    def __init__(self, unique: bool, lowerBound: int, upperBound: int, many: bool, required: bool, ordered: bool, ecoreO_ETypedElement: "ecoreO_EClassifier" = None, ecoreO_ETypedElement85: "ecoreO_EGenericType" = None):
        self.unique = unique
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.many = many
        self.required = required
        self.ordered = ordered
        self.ecoreO_ETypedElement = ecoreO_ETypedElement
        self.ecoreO_ETypedElement85 = ecoreO_ETypedElement85
        
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
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def ecoreO_ETypedElement(self):
        return self.__ecoreO_ETypedElement

    @ecoreO_ETypedElement.setter
    def ecoreO_ETypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_ETypedElement__ecoreO_ETypedElement", None)
        self.__ecoreO_ETypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EClassifier83"):
                opp_val = getattr(old_value, "ecoreO_EClassifier83", None)
                if opp_val == self:
                    setattr(old_value, "ecoreO_EClassifier83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EClassifier83"):
                opp_val = getattr(value, "ecoreO_EClassifier83", None)
                setattr(value, "ecoreO_EClassifier83", self)

    @property
    def ecoreO_ETypedElement85(self):
        return self.__ecoreO_ETypedElement85

    @ecoreO_ETypedElement85.setter
    def ecoreO_ETypedElement85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_ETypedElement__ecoreO_ETypedElement85", None)
        self.__ecoreO_ETypedElement85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EGenericType86"):
                opp_val = getattr(old_value, "ecoreO_EGenericType86", None)
                if opp_val == self:
                    setattr(old_value, "ecoreO_EGenericType86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EGenericType86"):
                opp_val = getattr(value, "ecoreO_EGenericType86", None)
                setattr(value, "ecoreO_EGenericType86", self)

class ecoreO_EClassifier(ENamedElement):

    def __init__(self, instanceClassName: str, instanceClass: str, defaultValue: str, instanceTypeName: str, eClassifiers: "ecoreO_EPackage" = None, ecoreO_EClassifier: set["ecoreO_ETypeParameter"] = None, ecoreO_EClassifier56: "ecoreO_EOperation" = None, EClassifier: "ecoreO_EPackage" = None, ecoreO_EClassifier83: "ecoreO_ETypedElement" = None, ecoreO_EClassifier95: "ecoreO_EGenericType" = None, ecoreO_EClassifier104: "ecoreO_EGenericType" = None):
        self.instanceClassName = instanceClassName
        self.instanceClass = instanceClass
        self.defaultValue = defaultValue
        self.instanceTypeName = instanceTypeName
        self.eClassifiers = eClassifiers
        self.ecoreO_EClassifier = ecoreO_EClassifier if ecoreO_EClassifier is not None else set()
        self.ecoreO_EClassifier56 = ecoreO_EClassifier56
        self.EClassifier = EClassifier
        self.ecoreO_EClassifier83 = ecoreO_EClassifier83
        self.ecoreO_EClassifier95 = ecoreO_EClassifier95
        self.ecoreO_EClassifier104 = ecoreO_EClassifier104
        
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
    def instanceTypeName(self) -> str:
        return self.__instanceTypeName

    @instanceTypeName.setter
    def instanceTypeName(self, instanceTypeName: str):
        self.__instanceTypeName = instanceTypeName

    @property
    def ecoreO_EClassifier83(self):
        return self.__ecoreO_EClassifier83

    @ecoreO_EClassifier83.setter
    def ecoreO_EClassifier83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClassifier__ecoreO_EClassifier83", None)
        self.__ecoreO_EClassifier83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_ETypedElement"):
                opp_val = getattr(old_value, "ecoreO_ETypedElement", None)
                if opp_val == self:
                    setattr(old_value, "ecoreO_ETypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_ETypedElement"):
                opp_val = getattr(value, "ecoreO_ETypedElement", None)
                setattr(value, "ecoreO_ETypedElement", self)

    @property
    def ecoreO_EClassifier(self):
        return self.__ecoreO_EClassifier

    @ecoreO_EClassifier.setter
    def ecoreO_EClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClassifier__ecoreO_EClassifier", None)
        self.__ecoreO_EClassifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreO_ETypeParameter"):
                    opp_val = getattr(item, "ecoreO_ETypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreO_ETypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreO_ETypeParameter"):
                    opp_val = getattr(item, "ecoreO_ETypeParameter", None)
                    
                    setattr(item, "ecoreO_ETypeParameter", self)
                    

    @property
    def EClassifier(self):
        return self.__EClassifier

    @EClassifier.setter
    def EClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClassifier__EClassifier", None)
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
    def ecoreO_EClassifier56(self):
        return self.__ecoreO_EClassifier56

    @ecoreO_EClassifier56.setter
    def ecoreO_EClassifier56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClassifier__ecoreO_EClassifier56", None)
        self.__ecoreO_EClassifier56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EOperation55"):
                opp_val = getattr(old_value, "ecoreO_EOperation55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EOperation55"):
                opp_val = getattr(value, "ecoreO_EOperation55", None)
                if opp_val is None:
                    setattr(value, "ecoreO_EOperation55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreO_EClassifier104(self):
        return self.__ecoreO_EClassifier104

    @ecoreO_EClassifier104.setter
    def ecoreO_EClassifier104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClassifier__ecoreO_EClassifier104", None)
        self.__ecoreO_EClassifier104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EGenericType103"):
                opp_val = getattr(old_value, "ecoreO_EGenericType103", None)
                if opp_val == self:
                    setattr(old_value, "ecoreO_EGenericType103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EGenericType103"):
                opp_val = getattr(value, "ecoreO_EGenericType103", None)
                setattr(value, "ecoreO_EGenericType103", self)

    @property
    def eClassifiers(self):
        return self.__eClassifiers

    @eClassifiers.setter
    def eClassifiers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClassifier__eClassifiers", None)
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
    def ecoreO_EClassifier95(self):
        return self.__ecoreO_EClassifier95

    @ecoreO_EClassifier95.setter
    def ecoreO_EClassifier95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClassifier__ecoreO_EClassifier95", None)
        self.__ecoreO_EClassifier95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EGenericType94"):
                opp_val = getattr(old_value, "ecoreO_EGenericType94", None)
                if opp_val == self:
                    setattr(old_value, "ecoreO_EGenericType94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EGenericType94"):
                opp_val = getattr(value, "ecoreO_EGenericType94", None)
                setattr(value, "ecoreO_EGenericType94", self)

    def getClassifierID(self) -> int:
        # TODO: Implement getClassifierID method
        pass

    def isInstance(self, object: str) -> bool:
        # TODO: Implement isInstance method
        pass

class ecoreO_ETypeParameter(ENamedElement):

    pass
class ecoreO_EPackage(ENamedElement):

    def __init__(self, nsURI: str, nsPrefix: str, EPackage: "ecoreO_EClassifier" = None, EPackage47: "ecoreO_EFactory" = None, ePackage: "ecoreO_EFactory" = None, ePackage62: set["ecoreO_EClassifier"] = None, EPackage65: "ecoreO_EPackage" = None, eSuperPackage: set["ecoreO_EPackage"] = None, EPackage68: "ecoreO_EPackage" = None, eSubpackages: "ecoreO_EPackage" = None):
        self.nsURI = nsURI
        self.nsPrefix = nsPrefix
        self.EPackage = EPackage
        self.EPackage47 = EPackage47
        self.ePackage = ePackage
        self.ePackage62 = ePackage62 if ePackage62 is not None else set()
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
    def EPackage65(self):
        return self.__EPackage65

    @EPackage65.setter
    def EPackage65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EPackage__EPackage65", None)
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
    def EPackage47(self):
        return self.__EPackage47

    @EPackage47.setter
    def EPackage47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EPackage__EPackage47", None)
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
    def EPackage68(self):
        return self.__EPackage68

    @EPackage68.setter
    def EPackage68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EPackage__EPackage68", None)
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
        old_value = getattr(self, f"_ecoreO_EPackage__ePackage62", None)
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
                    

    @property
    def ePackage(self):
        return self.__ePackage

    @ePackage.setter
    def ePackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EPackage__ePackage", None)
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
    def EPackage(self):
        return self.__EPackage

    @EPackage.setter
    def EPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EPackage__EPackage", None)
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
        old_value = getattr(self, f"_ecoreO_EPackage__eSuperPackage", None)
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
    def eSubpackages(self):
        return self.__eSubpackages

    @eSubpackages.setter
    def eSubpackages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EPackage__eSubpackages", None)
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

    def getEClassifier(self, name: str) -> EClassifier:
        # TODO: Implement getEClassifier method
        pass

class ecoreO_EStructuralFeature(ETypedElement):

    def __init__(self, changeable: bool, volatile: bool, transient: bool, defaultValueLiteral: str, defaultValue: str, unsettable: bool, derived: bool, ecoreO_EStructuralFeature: "ecoreO_EClass" = None, EStructuralFeature: "ecoreO_EClass" = None, eStructuralFeatures: "ecoreO_EClass" = None):
        self.changeable = changeable
        self.volatile = volatile
        self.transient = transient
        self.defaultValueLiteral = defaultValueLiteral
        self.defaultValue = defaultValue
        self.unsettable = unsettable
        self.derived = derived
        self.ecoreO_EStructuralFeature = ecoreO_EStructuralFeature
        self.EStructuralFeature = EStructuralFeature
        self.eStructuralFeatures = eStructuralFeatures
        
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
    def unsettable(self) -> bool:
        return self.__unsettable

    @unsettable.setter
    def unsettable(self, unsettable: bool):
        self.__unsettable = unsettable

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
    def changeable(self) -> bool:
        return self.__changeable

    @changeable.setter
    def changeable(self, changeable: bool):
        self.__changeable = changeable

    @property
    def ecoreO_EStructuralFeature(self):
        return self.__ecoreO_EStructuralFeature

    @ecoreO_EStructuralFeature.setter
    def ecoreO_EStructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EStructuralFeature__ecoreO_EStructuralFeature", None)
        self.__ecoreO_EStructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EClass28"):
                opp_val = getattr(old_value, "ecoreO_EClass28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EClass28"):
                opp_val = getattr(value, "ecoreO_EClass28", None)
                if opp_val is None:
                    setattr(value, "ecoreO_EClass28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EStructuralFeature(self):
        return self.__EStructuralFeature

    @EStructuralFeature.setter
    def EStructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EStructuralFeature__EStructuralFeature", None)
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
        old_value = getattr(self, f"_ecoreO_EStructuralFeature__eStructuralFeatures", None)
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

    def getContainerClass(self):
        # TODO: Implement getContainerClass method
        pass

    def getFeatureID(self) -> int:
        # TODO: Implement getFeatureID method
        pass

class ecoreO_EGenericType:

    pass
class ecoreO_EOperation(ETypedElement):

    def __init__(self, EOperation: "ecoreO_EClass" = None, ecoreO_EOperation: "ecoreO_EClass" = None, ecoreO_EOperation55: set["ecoreO_EClassifier"] = None, ecoreO_EOperation58: set["ecoreO_EGenericType"] = None, eOperations: "ecoreO_EClass" = None, ecoreO_EOperation51: set["ecoreO_ETypeParameter"] = None, eOperation: set["ecoreO_EParameter"] = None, EOperation70: "ecoreO_EParameter" = None):
        self.EOperation = EOperation
        self.ecoreO_EOperation = ecoreO_EOperation
        self.ecoreO_EOperation55 = ecoreO_EOperation55 if ecoreO_EOperation55 is not None else set()
        self.ecoreO_EOperation58 = ecoreO_EOperation58 if ecoreO_EOperation58 is not None else set()
        self.eOperations = eOperations
        self.ecoreO_EOperation51 = ecoreO_EOperation51 if ecoreO_EOperation51 is not None else set()
        self.eOperation = eOperation if eOperation is not None else set()
        self.EOperation70 = EOperation70
        
    @property
    def ecoreO_EOperation(self):
        return self.__ecoreO_EOperation

    @ecoreO_EOperation.setter
    def ecoreO_EOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EOperation__ecoreO_EOperation", None)
        self.__ecoreO_EOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EClass26"):
                opp_val = getattr(old_value, "ecoreO_EClass26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EClass26"):
                opp_val = getattr(value, "ecoreO_EClass26", None)
                if opp_val is None:
                    setattr(value, "ecoreO_EClass26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EOperation70(self):
        return self.__EOperation70

    @EOperation70.setter
    def EOperation70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EOperation__EOperation70", None)
        self.__EOperation70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eParameters"):
                opp_val = getattr(old_value, "eParameters", None)
                if opp_val == self:
                    setattr(old_value, "eParameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eParameters"):
                opp_val = getattr(value, "eParameters", None)
                setattr(value, "eParameters", self)

    @property
    def ecoreO_EOperation58(self):
        return self.__ecoreO_EOperation58

    @ecoreO_EOperation58.setter
    def ecoreO_EOperation58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EOperation__ecoreO_EOperation58", None)
        self.__ecoreO_EOperation58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreO_EGenericType59"):
                    opp_val = getattr(item, "ecoreO_EGenericType59", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreO_EGenericType59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreO_EGenericType59"):
                    opp_val = getattr(item, "ecoreO_EGenericType59", None)
                    
                    setattr(item, "ecoreO_EGenericType59", self)
                    

    @property
    def eOperation(self):
        return self.__eOperation

    @eOperation.setter
    def eOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EOperation__eOperation", None)
        self.__eOperation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EParameter"):
                    opp_val = getattr(item, "EParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "EParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EParameter"):
                    opp_val = getattr(item, "EParameter", None)
                    
                    setattr(item, "EParameter", self)
                    

    @property
    def eOperations(self):
        return self.__eOperations

    @eOperations.setter
    def eOperations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EOperation__eOperations", None)
        self.__eOperations = value
        
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
    def ecoreO_EOperation51(self):
        return self.__ecoreO_EOperation51

    @ecoreO_EOperation51.setter
    def ecoreO_EOperation51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EOperation__ecoreO_EOperation51", None)
        self.__ecoreO_EOperation51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreO_ETypeParameter52"):
                    opp_val = getattr(item, "ecoreO_ETypeParameter52", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreO_ETypeParameter52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreO_ETypeParameter52"):
                    opp_val = getattr(item, "ecoreO_ETypeParameter52", None)
                    
                    setattr(item, "ecoreO_ETypeParameter52", self)
                    

    @property
    def EOperation(self):
        return self.__EOperation

    @EOperation.setter
    def EOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EOperation__EOperation", None)
        self.__EOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eContainingClass"):
                opp_val = getattr(old_value, "eContainingClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eContainingClass"):
                opp_val = getattr(value, "eContainingClass", None)
                if opp_val is None:
                    setattr(value, "eContainingClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreO_EOperation55(self):
        return self.__ecoreO_EOperation55

    @ecoreO_EOperation55.setter
    def ecoreO_EOperation55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EOperation__ecoreO_EOperation55", None)
        self.__ecoreO_EOperation55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreO_EClassifier56"):
                    opp_val = getattr(item, "ecoreO_EClassifier56", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreO_EClassifier56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreO_EClassifier56"):
                    opp_val = getattr(item, "ecoreO_EClassifier56", None)
                    
                    setattr(item, "ecoreO_EClassifier56", self)
                    

    def isOverrideOf(self, someOperation: str) -> bool:
        # TODO: Implement isOverrideOf method
        pass

    def getOperationID(self) -> int:
        # TODO: Implement getOperationID method
        pass

class EClassifier:

    pass
class ecoreO_EClass(EClassifier):

    def __init__(self, abstract: bool, interface: bool, ecoreO_EClass17: set["ecoreO_EReference"] = None, ecoreO_EClass20: set["ecoreO_EAttribute"] = None, ecoreO_EClass23: set["ecoreO_EReference"] = None, ecoreO_EClass: "ecoreO_EClass" = None, ecoreO_EClass8: set["ecoreO_EClass"] = None, eContainingClass: set["ecoreO_EOperation"] = None, ecoreO_EClass12: set["ecoreO_EAttribute"] = None, ecoreO_EClass15: set["ecoreO_EReference"] = None, ecoreO_EClass38: set["ecoreO_EGenericType"] = None, ecoreO_EClass40: set["ecoreO_EGenericType"] = None, ecoreO_EClass26: set["ecoreO_EOperation"] = None, ecoreO_EClass28: set["ecoreO_EStructuralFeature"] = None, ecoreO_EClass31: "ecoreO_EClass" = None, ecoreO_EClass29: set["ecoreO_EClass"] = None, ecoreO_EClass33: "ecoreO_EAttribute" = None, eContainingClass36: set["ecoreO_EStructuralFeature"] = None, EClass: "ecoreO_EOperation" = None, ecoreO_EClass76: "ecoreO_EReference" = None, EClass81: "ecoreO_EStructuralFeature" = None):
        self.abstract = abstract
        self.interface = interface
        self.ecoreO_EClass17 = ecoreO_EClass17 if ecoreO_EClass17 is not None else set()
        self.ecoreO_EClass20 = ecoreO_EClass20 if ecoreO_EClass20 is not None else set()
        self.ecoreO_EClass23 = ecoreO_EClass23 if ecoreO_EClass23 is not None else set()
        self.ecoreO_EClass = ecoreO_EClass
        self.ecoreO_EClass8 = ecoreO_EClass8 if ecoreO_EClass8 is not None else set()
        self.eContainingClass = eContainingClass if eContainingClass is not None else set()
        self.ecoreO_EClass12 = ecoreO_EClass12 if ecoreO_EClass12 is not None else set()
        self.ecoreO_EClass15 = ecoreO_EClass15 if ecoreO_EClass15 is not None else set()
        self.ecoreO_EClass38 = ecoreO_EClass38 if ecoreO_EClass38 is not None else set()
        self.ecoreO_EClass40 = ecoreO_EClass40 if ecoreO_EClass40 is not None else set()
        self.ecoreO_EClass26 = ecoreO_EClass26 if ecoreO_EClass26 is not None else set()
        self.ecoreO_EClass28 = ecoreO_EClass28 if ecoreO_EClass28 is not None else set()
        self.ecoreO_EClass31 = ecoreO_EClass31
        self.ecoreO_EClass29 = ecoreO_EClass29 if ecoreO_EClass29 is not None else set()
        self.ecoreO_EClass33 = ecoreO_EClass33
        self.eContainingClass36 = eContainingClass36 if eContainingClass36 is not None else set()
        self.EClass = EClass
        self.ecoreO_EClass76 = ecoreO_EClass76
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
    def ecoreO_EClass8(self):
        return self.__ecoreO_EClass8

    @ecoreO_EClass8.setter
    def ecoreO_EClass8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClass__ecoreO_EClass8", None)
        self.__ecoreO_EClass8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreO_EClass"):
                    opp_val = getattr(item, "ecoreO_EClass", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreO_EClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreO_EClass"):
                    opp_val = getattr(item, "ecoreO_EClass", None)
                    
                    setattr(item, "ecoreO_EClass", self)
                    

    @property
    def EClass81(self):
        return self.__EClass81

    @EClass81.setter
    def EClass81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClass__EClass81", None)
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

    @property
    def ecoreO_EClass20(self):
        return self.__ecoreO_EClass20

    @ecoreO_EClass20.setter
    def ecoreO_EClass20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClass__ecoreO_EClass20", None)
        self.__ecoreO_EClass20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreO_EAttribute21"):
                    opp_val = getattr(item, "ecoreO_EAttribute21", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreO_EAttribute21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreO_EAttribute21"):
                    opp_val = getattr(item, "ecoreO_EAttribute21", None)
                    
                    setattr(item, "ecoreO_EAttribute21", self)
                    

    @property
    def ecoreO_EClass38(self):
        return self.__ecoreO_EClass38

    @ecoreO_EClass38.setter
    def ecoreO_EClass38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClass__ecoreO_EClass38", None)
        self.__ecoreO_EClass38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreO_EGenericType"):
                    opp_val = getattr(item, "ecoreO_EGenericType", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreO_EGenericType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreO_EGenericType"):
                    opp_val = getattr(item, "ecoreO_EGenericType", None)
                    
                    setattr(item, "ecoreO_EGenericType", self)
                    

    @property
    def ecoreO_EClass33(self):
        return self.__ecoreO_EClass33

    @ecoreO_EClass33.setter
    def ecoreO_EClass33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClass__ecoreO_EClass33", None)
        self.__ecoreO_EClass33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EAttribute34"):
                opp_val = getattr(old_value, "ecoreO_EAttribute34", None)
                if opp_val == self:
                    setattr(old_value, "ecoreO_EAttribute34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EAttribute34"):
                opp_val = getattr(value, "ecoreO_EAttribute34", None)
                setattr(value, "ecoreO_EAttribute34", self)

    @property
    def ecoreO_EClass26(self):
        return self.__ecoreO_EClass26

    @ecoreO_EClass26.setter
    def ecoreO_EClass26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClass__ecoreO_EClass26", None)
        self.__ecoreO_EClass26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreO_EOperation"):
                    opp_val = getattr(item, "ecoreO_EOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreO_EOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreO_EOperation"):
                    opp_val = getattr(item, "ecoreO_EOperation", None)
                    
                    setattr(item, "ecoreO_EOperation", self)
                    

    @property
    def ecoreO_EClass76(self):
        return self.__ecoreO_EClass76

    @ecoreO_EClass76.setter
    def ecoreO_EClass76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClass__ecoreO_EClass76", None)
        self.__ecoreO_EClass76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EReference75"):
                opp_val = getattr(old_value, "ecoreO_EReference75", None)
                if opp_val == self:
                    setattr(old_value, "ecoreO_EReference75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EReference75"):
                opp_val = getattr(value, "ecoreO_EReference75", None)
                setattr(value, "ecoreO_EReference75", self)

    @property
    def EClass(self):
        return self.__EClass

    @EClass.setter
    def EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClass__EClass", None)
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
    def ecoreO_EClass12(self):
        return self.__ecoreO_EClass12

    @ecoreO_EClass12.setter
    def ecoreO_EClass12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClass__ecoreO_EClass12", None)
        self.__ecoreO_EClass12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreO_EAttribute13"):
                    opp_val = getattr(item, "ecoreO_EAttribute13", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreO_EAttribute13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreO_EAttribute13"):
                    opp_val = getattr(item, "ecoreO_EAttribute13", None)
                    
                    setattr(item, "ecoreO_EAttribute13", self)
                    

    @property
    def eContainingClass36(self):
        return self.__eContainingClass36

    @eContainingClass36.setter
    def eContainingClass36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClass__eContainingClass36", None)
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
    def ecoreO_EClass31(self):
        return self.__ecoreO_EClass31

    @ecoreO_EClass31.setter
    def ecoreO_EClass31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClass__ecoreO_EClass31", None)
        self.__ecoreO_EClass31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EClass29"):
                opp_val = getattr(old_value, "ecoreO_EClass29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EClass29"):
                opp_val = getattr(value, "ecoreO_EClass29", None)
                if opp_val is None:
                    setattr(value, "ecoreO_EClass29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eContainingClass(self):
        return self.__eContainingClass

    @eContainingClass.setter
    def eContainingClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClass__eContainingClass", None)
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
    def ecoreO_EClass28(self):
        return self.__ecoreO_EClass28

    @ecoreO_EClass28.setter
    def ecoreO_EClass28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClass__ecoreO_EClass28", None)
        self.__ecoreO_EClass28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreO_EStructuralFeature"):
                    opp_val = getattr(item, "ecoreO_EStructuralFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreO_EStructuralFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreO_EStructuralFeature"):
                    opp_val = getattr(item, "ecoreO_EStructuralFeature", None)
                    
                    setattr(item, "ecoreO_EStructuralFeature", self)
                    

    @property
    def ecoreO_EClass(self):
        return self.__ecoreO_EClass

    @ecoreO_EClass.setter
    def ecoreO_EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClass__ecoreO_EClass", None)
        self.__ecoreO_EClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EClass8"):
                opp_val = getattr(old_value, "ecoreO_EClass8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EClass8"):
                opp_val = getattr(value, "ecoreO_EClass8", None)
                if opp_val is None:
                    setattr(value, "ecoreO_EClass8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreO_EClass40(self):
        return self.__ecoreO_EClass40

    @ecoreO_EClass40.setter
    def ecoreO_EClass40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClass__ecoreO_EClass40", None)
        self.__ecoreO_EClass40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreO_EGenericType41"):
                    opp_val = getattr(item, "ecoreO_EGenericType41", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreO_EGenericType41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreO_EGenericType41"):
                    opp_val = getattr(item, "ecoreO_EGenericType41", None)
                    
                    setattr(item, "ecoreO_EGenericType41", self)
                    

    @property
    def ecoreO_EClass23(self):
        return self.__ecoreO_EClass23

    @ecoreO_EClass23.setter
    def ecoreO_EClass23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClass__ecoreO_EClass23", None)
        self.__ecoreO_EClass23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreO_EReference24"):
                    opp_val = getattr(item, "ecoreO_EReference24", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreO_EReference24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreO_EReference24"):
                    opp_val = getattr(item, "ecoreO_EReference24", None)
                    
                    setattr(item, "ecoreO_EReference24", self)
                    

    @property
    def ecoreO_EClass29(self):
        return self.__ecoreO_EClass29

    @ecoreO_EClass29.setter
    def ecoreO_EClass29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClass__ecoreO_EClass29", None)
        self.__ecoreO_EClass29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreO_EClass31"):
                    opp_val = getattr(item, "ecoreO_EClass31", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreO_EClass31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreO_EClass31"):
                    opp_val = getattr(item, "ecoreO_EClass31", None)
                    
                    setattr(item, "ecoreO_EClass31", self)
                    

    @property
    def ecoreO_EClass17(self):
        return self.__ecoreO_EClass17

    @ecoreO_EClass17.setter
    def ecoreO_EClass17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClass__ecoreO_EClass17", None)
        self.__ecoreO_EClass17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreO_EReference18"):
                    opp_val = getattr(item, "ecoreO_EReference18", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreO_EReference18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreO_EReference18"):
                    opp_val = getattr(item, "ecoreO_EReference18", None)
                    
                    setattr(item, "ecoreO_EReference18", self)
                    

    @property
    def ecoreO_EClass15(self):
        return self.__ecoreO_EClass15

    @ecoreO_EClass15.setter
    def ecoreO_EClass15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EClass__ecoreO_EClass15", None)
        self.__ecoreO_EClass15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreO_EReference"):
                    opp_val = getattr(item, "ecoreO_EReference", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreO_EReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreO_EReference"):
                    opp_val = getattr(item, "ecoreO_EReference", None)
                    
                    setattr(item, "ecoreO_EReference", self)
                    

    def getOperationCount(self) -> int:
        # TODO: Implement getOperationCount method
        pass

    def getOperationID(self, operation: str) -> int:
        # TODO: Implement getOperationID method
        pass

    def getEStructuralFeature(self, featureID: int) -> EStructuralFeature:
        # TODO: Implement getEStructuralFeature method
        pass

    def getFeatureCount(self) -> int:
        # TODO: Implement getFeatureCount method
        pass

    def isSuperTypeOf(self, someClass: str) -> bool:
        # TODO: Implement isSuperTypeOf method
        pass

    def getEOperation(self, operationID: int) -> str:
        # TODO: Implement getEOperation method
        pass

    def getFeatureID(self, feature: EStructuralFeature) -> int:
        # TODO: Implement getFeatureID method
        pass

    def getEStructuralFeature(self, featureName: str) -> EStructuralFeature:
        # TODO: Implement getEStructuralFeature method
        pass

    def getOverride(self, operation: str) -> str:
        # TODO: Implement getOverride method
        pass

class ecoreO_EObject:

    def __init__(self, ecoreO_EObject: "ecoreO_EAnnotation" = None, ecoreO_EObject7: "ecoreO_EAnnotation" = None):
        self.ecoreO_EObject = ecoreO_EObject
        self.ecoreO_EObject7 = ecoreO_EObject7
        
    @property
    def ecoreO_EObject7(self):
        return self.__ecoreO_EObject7

    @ecoreO_EObject7.setter
    def ecoreO_EObject7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EObject__ecoreO_EObject7", None)
        self.__ecoreO_EObject7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EAnnotation6"):
                opp_val = getattr(old_value, "ecoreO_EAnnotation6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EAnnotation6"):
                opp_val = getattr(value, "ecoreO_EAnnotation6", None)
                if opp_val is None:
                    setattr(value, "ecoreO_EAnnotation6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreO_EObject(self):
        return self.__ecoreO_EObject

    @ecoreO_EObject.setter
    def ecoreO_EObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EObject__ecoreO_EObject", None)
        self.__ecoreO_EObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EAnnotation4"):
                opp_val = getattr(old_value, "ecoreO_EAnnotation4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EAnnotation4"):
                opp_val = getattr(value, "ecoreO_EAnnotation4", None)
                if opp_val is None:
                    setattr(value, "ecoreO_EAnnotation4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def eAllContents(self):
        # TODO: Implement eAllContents method
        pass

    def eGet(self, feature: EStructuralFeature, resolve: bool) -> str:
        # TODO: Implement eGet method
        pass

    def eIsSet(self, feature: EStructuralFeature) -> bool:
        # TODO: Implement eIsSet method
        pass

    def eInvoke(self, arguments: str, operation: str) -> str:
        # TODO: Implement eInvoke method
        pass

    def eContainingFeature(self) -> EStructuralFeature:
        # TODO: Implement eContainingFeature method
        pass

    def eCrossReferences(self):
        # TODO: Implement eCrossReferences method
        pass

    def eUnset(self, feature: EStructuralFeature):
        # TODO: Implement eUnset method
        pass

    def eContainer(self) -> str:
        # TODO: Implement eContainer method
        pass

    def eResource(self) -> str:
        # TODO: Implement eResource method
        pass

    def eIsProxy(self) -> bool:
        # TODO: Implement eIsProxy method
        pass

    def eClass(self) -> str:
        # TODO: Implement eClass method
        pass

    def eGet(self, feature: EStructuralFeature) -> str:
        # TODO: Implement eGet method
        pass

    def eSet(self, feature: EStructuralFeature, newValue: str):
        # TODO: Implement eSet method
        pass

    def eContents(self):
        # TODO: Implement eContents method
        pass

    def eContainmentFeature(self) -> str:
        # TODO: Implement eContainmentFeature method
        pass

class ecoreO_EDataType(EClassifier):

    def __init__(self, serializable: bool, ecoreO_EDataType: "ecoreO_EAttribute" = None):
        self.serializable = serializable
        self.ecoreO_EDataType = ecoreO_EDataType
        
    @property
    def serializable(self) -> bool:
        return self.__serializable

    @serializable.setter
    def serializable(self, serializable: bool):
        self.__serializable = serializable

    @property
    def ecoreO_EDataType(self):
        return self.__ecoreO_EDataType

    @ecoreO_EDataType.setter
    def ecoreO_EDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EDataType__ecoreO_EDataType", None)
        self.__ecoreO_EDataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EAttribute"):
                opp_val = getattr(old_value, "ecoreO_EAttribute", None)
                if opp_val == self:
                    setattr(old_value, "ecoreO_EAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EAttribute"):
                opp_val = getattr(value, "ecoreO_EAttribute", None)
                setattr(value, "ecoreO_EAttribute", self)

class EStructuralFeature:

    pass
class ecoreO_EReference(EStructuralFeature):

    def __init__(self, resolveProxies: bool, containment: bool, container: bool, ecoreO_EReference18: "ecoreO_EClass" = None, ecoreO_EReference24: "ecoreO_EClass" = None, ecoreO_EReference: "ecoreO_EClass" = None, ecoreO_EReference73: "ecoreO_EReference" = None, ecoreO_EReference71: "ecoreO_EReference" = None, ecoreO_EReference75: "ecoreO_EClass" = None, ecoreO_EReference78: set["ecoreO_EAttribute"] = None):
        self.resolveProxies = resolveProxies
        self.containment = containment
        self.container = container
        self.ecoreO_EReference18 = ecoreO_EReference18
        self.ecoreO_EReference24 = ecoreO_EReference24
        self.ecoreO_EReference = ecoreO_EReference
        self.ecoreO_EReference73 = ecoreO_EReference73
        self.ecoreO_EReference71 = ecoreO_EReference71
        self.ecoreO_EReference75 = ecoreO_EReference75
        self.ecoreO_EReference78 = ecoreO_EReference78 if ecoreO_EReference78 is not None else set()
        
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
    def ecoreO_EReference78(self):
        return self.__ecoreO_EReference78

    @ecoreO_EReference78.setter
    def ecoreO_EReference78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EReference__ecoreO_EReference78", None)
        self.__ecoreO_EReference78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreO_EAttribute79"):
                    opp_val = getattr(item, "ecoreO_EAttribute79", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreO_EAttribute79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreO_EAttribute79"):
                    opp_val = getattr(item, "ecoreO_EAttribute79", None)
                    
                    setattr(item, "ecoreO_EAttribute79", self)
                    

    @property
    def ecoreO_EReference75(self):
        return self.__ecoreO_EReference75

    @ecoreO_EReference75.setter
    def ecoreO_EReference75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EReference__ecoreO_EReference75", None)
        self.__ecoreO_EReference75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EClass76"):
                opp_val = getattr(old_value, "ecoreO_EClass76", None)
                if opp_val == self:
                    setattr(old_value, "ecoreO_EClass76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EClass76"):
                opp_val = getattr(value, "ecoreO_EClass76", None)
                setattr(value, "ecoreO_EClass76", self)

    @property
    def ecoreO_EReference71(self):
        return self.__ecoreO_EReference71

    @ecoreO_EReference71.setter
    def ecoreO_EReference71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EReference__ecoreO_EReference71", None)
        self.__ecoreO_EReference71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EReference73"):
                opp_val = getattr(old_value, "ecoreO_EReference73", None)
                if opp_val == self:
                    setattr(old_value, "ecoreO_EReference73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EReference73"):
                opp_val = getattr(value, "ecoreO_EReference73", None)
                setattr(value, "ecoreO_EReference73", self)

    @property
    def ecoreO_EReference(self):
        return self.__ecoreO_EReference

    @ecoreO_EReference.setter
    def ecoreO_EReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EReference__ecoreO_EReference", None)
        self.__ecoreO_EReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EClass15"):
                opp_val = getattr(old_value, "ecoreO_EClass15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EClass15"):
                opp_val = getattr(value, "ecoreO_EClass15", None)
                if opp_val is None:
                    setattr(value, "ecoreO_EClass15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreO_EReference18(self):
        return self.__ecoreO_EReference18

    @ecoreO_EReference18.setter
    def ecoreO_EReference18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EReference__ecoreO_EReference18", None)
        self.__ecoreO_EReference18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EClass17"):
                opp_val = getattr(old_value, "ecoreO_EClass17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EClass17"):
                opp_val = getattr(value, "ecoreO_EClass17", None)
                if opp_val is None:
                    setattr(value, "ecoreO_EClass17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreO_EReference73(self):
        return self.__ecoreO_EReference73

    @ecoreO_EReference73.setter
    def ecoreO_EReference73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EReference__ecoreO_EReference73", None)
        self.__ecoreO_EReference73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EReference71"):
                opp_val = getattr(old_value, "ecoreO_EReference71", None)
                if opp_val == self:
                    setattr(old_value, "ecoreO_EReference71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EReference71"):
                opp_val = getattr(value, "ecoreO_EReference71", None)
                setattr(value, "ecoreO_EReference71", self)

    @property
    def ecoreO_EReference24(self):
        return self.__ecoreO_EReference24

    @ecoreO_EReference24.setter
    def ecoreO_EReference24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EReference__ecoreO_EReference24", None)
        self.__ecoreO_EReference24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EClass23"):
                opp_val = getattr(old_value, "ecoreO_EClass23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EClass23"):
                opp_val = getattr(value, "ecoreO_EClass23", None)
                if opp_val is None:
                    setattr(value, "ecoreO_EClass23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecoreO_EAttribute(EStructuralFeature):

    def __init__(self, iD: bool, ecoreO_EAttribute: "ecoreO_EDataType" = None, ecoreO_EAttribute21: "ecoreO_EClass" = None, ecoreO_EAttribute13: "ecoreO_EClass" = None, ecoreO_EAttribute34: "ecoreO_EClass" = None, ecoreO_EAttribute79: "ecoreO_EReference" = None):
        self.iD = iD
        self.ecoreO_EAttribute = ecoreO_EAttribute
        self.ecoreO_EAttribute21 = ecoreO_EAttribute21
        self.ecoreO_EAttribute13 = ecoreO_EAttribute13
        self.ecoreO_EAttribute34 = ecoreO_EAttribute34
        self.ecoreO_EAttribute79 = ecoreO_EAttribute79
        
    @property
    def iD(self) -> bool:
        return self.__iD

    @iD.setter
    def iD(self, iD: bool):
        self.__iD = iD

    @property
    def ecoreO_EAttribute21(self):
        return self.__ecoreO_EAttribute21

    @ecoreO_EAttribute21.setter
    def ecoreO_EAttribute21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EAttribute__ecoreO_EAttribute21", None)
        self.__ecoreO_EAttribute21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EClass20"):
                opp_val = getattr(old_value, "ecoreO_EClass20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EClass20"):
                opp_val = getattr(value, "ecoreO_EClass20", None)
                if opp_val is None:
                    setattr(value, "ecoreO_EClass20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreO_EAttribute79(self):
        return self.__ecoreO_EAttribute79

    @ecoreO_EAttribute79.setter
    def ecoreO_EAttribute79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EAttribute__ecoreO_EAttribute79", None)
        self.__ecoreO_EAttribute79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EReference78"):
                opp_val = getattr(old_value, "ecoreO_EReference78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EReference78"):
                opp_val = getattr(value, "ecoreO_EReference78", None)
                if opp_val is None:
                    setattr(value, "ecoreO_EReference78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreO_EAttribute13(self):
        return self.__ecoreO_EAttribute13

    @ecoreO_EAttribute13.setter
    def ecoreO_EAttribute13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EAttribute__ecoreO_EAttribute13", None)
        self.__ecoreO_EAttribute13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EClass12"):
                opp_val = getattr(old_value, "ecoreO_EClass12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EClass12"):
                opp_val = getattr(value, "ecoreO_EClass12", None)
                if opp_val is None:
                    setattr(value, "ecoreO_EClass12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreO_EAttribute(self):
        return self.__ecoreO_EAttribute

    @ecoreO_EAttribute.setter
    def ecoreO_EAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EAttribute__ecoreO_EAttribute", None)
        self.__ecoreO_EAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EDataType"):
                opp_val = getattr(old_value, "ecoreO_EDataType", None)
                if opp_val == self:
                    setattr(old_value, "ecoreO_EDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EDataType"):
                opp_val = getattr(value, "ecoreO_EDataType", None)
                setattr(value, "ecoreO_EDataType", self)

    @property
    def ecoreO_EAttribute34(self):
        return self.__ecoreO_EAttribute34

    @ecoreO_EAttribute34.setter
    def ecoreO_EAttribute34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EAttribute__ecoreO_EAttribute34", None)
        self.__ecoreO_EAttribute34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EClass33"):
                opp_val = getattr(old_value, "ecoreO_EClass33", None)
                if opp_val == self:
                    setattr(old_value, "ecoreO_EClass33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EClass33"):
                opp_val = getattr(value, "ecoreO_EClass33", None)
                setattr(value, "ecoreO_EClass33", self)

class ecoreO_EModelElement(ABC):

    def __init__(self, EModelElement: "ecoreO_EAnnotation" = None, eModelElement: set["ecoreO_EAnnotation"] = None):
        self.EModelElement = EModelElement
        self.eModelElement = eModelElement if eModelElement is not None else set()
        
    @property
    def EModelElement(self):
        return self.__EModelElement

    @EModelElement.setter
    def EModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EModelElement__EModelElement", None)
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
        old_value = getattr(self, f"_ecoreO_EModelElement__eModelElement", None)
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

class ecoreO_EStringToStringMapEntry:

    def __init__(self, value: str, key: str, ecoreO_EStringToStringMapEntry: "ecoreO_EAnnotation" = None):
        self.value = value
        self.key = key
        self.ecoreO_EStringToStringMapEntry = ecoreO_EStringToStringMapEntry
        
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
    def ecoreO_EStringToStringMapEntry(self):
        return self.__ecoreO_EStringToStringMapEntry

    @ecoreO_EStringToStringMapEntry.setter
    def ecoreO_EStringToStringMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EStringToStringMapEntry__ecoreO_EStringToStringMapEntry", None)
        self.__ecoreO_EStringToStringMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreO_EAnnotation"):
                opp_val = getattr(old_value, "ecoreO_EAnnotation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreO_EAnnotation"):
                opp_val = getattr(value, "ecoreO_EAnnotation", None)
                if opp_val is None:
                    setattr(value, "ecoreO_EAnnotation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EModelElement:

    pass
class ecoreO_EFactory(EModelElement):

    def __init__(self, eFactoryInstance: "ecoreO_EPackage" = None, EFactory: "ecoreO_EPackage" = None):
        self.eFactoryInstance = eFactoryInstance
        self.EFactory = EFactory
        
    @property
    def EFactory(self):
        return self.__EFactory

    @EFactory.setter
    def EFactory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EFactory__EFactory", None)
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
        old_value = getattr(self, f"_ecoreO_EFactory__eFactoryInstance", None)
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

    def create(self, eClass: str) -> str:
        # TODO: Implement create method
        pass

    def createFromString(self, eDataType: EDataType, literalValue: str) -> str:
        # TODO: Implement createFromString method
        pass

    def convertToString(self, instanceValue: str, eDataType: EDataType) -> str:
        # TODO: Implement convertToString method
        pass

class ecoreO_ENamedElement(EModelElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ecoreO_EAnnotation(EModelElement):

    def __init__(self, source: str, ecoreO_EAnnotation: set["ecoreO_EStringToStringMapEntry"] = None, eAnnotations: "ecoreO_EModelElement" = None, ecoreO_EAnnotation4: set["ecoreO_EObject"] = None, ecoreO_EAnnotation6: set["ecoreO_EObject"] = None, EAnnotation: "ecoreO_EModelElement" = None):
        self.source = source
        self.ecoreO_EAnnotation = ecoreO_EAnnotation if ecoreO_EAnnotation is not None else set()
        self.eAnnotations = eAnnotations
        self.ecoreO_EAnnotation4 = ecoreO_EAnnotation4 if ecoreO_EAnnotation4 is not None else set()
        self.ecoreO_EAnnotation6 = ecoreO_EAnnotation6 if ecoreO_EAnnotation6 is not None else set()
        self.EAnnotation = EAnnotation
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def ecoreO_EAnnotation(self):
        return self.__ecoreO_EAnnotation

    @ecoreO_EAnnotation.setter
    def ecoreO_EAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EAnnotation__ecoreO_EAnnotation", None)
        self.__ecoreO_EAnnotation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreO_EStringToStringMapEntry"):
                    opp_val = getattr(item, "ecoreO_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreO_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreO_EStringToStringMapEntry"):
                    opp_val = getattr(item, "ecoreO_EStringToStringMapEntry", None)
                    
                    setattr(item, "ecoreO_EStringToStringMapEntry", self)
                    

    @property
    def ecoreO_EAnnotation6(self):
        return self.__ecoreO_EAnnotation6

    @ecoreO_EAnnotation6.setter
    def ecoreO_EAnnotation6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EAnnotation__ecoreO_EAnnotation6", None)
        self.__ecoreO_EAnnotation6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreO_EObject7"):
                    opp_val = getattr(item, "ecoreO_EObject7", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreO_EObject7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreO_EObject7"):
                    opp_val = getattr(item, "ecoreO_EObject7", None)
                    
                    setattr(item, "ecoreO_EObject7", self)
                    

    @property
    def EAnnotation(self):
        return self.__EAnnotation

    @EAnnotation.setter
    def EAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EAnnotation__EAnnotation", None)
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
        old_value = getattr(self, f"_ecoreO_EAnnotation__eAnnotations", None)
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
    def ecoreO_EAnnotation4(self):
        return self.__ecoreO_EAnnotation4

    @ecoreO_EAnnotation4.setter
    def ecoreO_EAnnotation4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreO_EAnnotation__ecoreO_EAnnotation4", None)
        self.__ecoreO_EAnnotation4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreO_EObject"):
                    opp_val = getattr(item, "ecoreO_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreO_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreO_EObject"):
                    opp_val = getattr(item, "ecoreO_EObject", None)
                    
                    setattr(item, "ecoreO_EObject", self)
                    
