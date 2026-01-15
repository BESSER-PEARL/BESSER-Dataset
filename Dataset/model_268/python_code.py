from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ETypedElement:

    pass
class encore_EParameter(ETypedElement):

    pass
class EDataType:

    pass
class encore_EEnum(EDataType):

    def __init__(self, EEnum: "encore_EEnumLiteral" = None, eEnum: set["encore_EEnumLiteral"] = None):
        self.EEnum = EEnum
        self.eEnum = eEnum if eEnum is not None else set()
        
    @property
    def eEnum(self):
        return self.__eEnum

    @eEnum.setter
    def eEnum(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EEnum__eEnum", None)
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
        old_value = getattr(self, f"_encore_EEnum__EEnum", None)
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

    def getEEnumLiteral(self, value: int) -> str:
        # TODO: Implement getEEnumLiteral method
        pass

    def getEEnumLiteralByLiteral(self, literal: str) -> str:
        # TODO: Implement getEEnumLiteralByLiteral method
        pass

    def getEEnumLiteral(self, name: str) -> str:
        # TODO: Implement getEEnumLiteral method
        pass

class encore_EStructuralFeature(ETypedElement):

    def __init__(self, changeable: bool, volatile: bool, transient: bool, defaultValueLiteral: str, defaultValue: str, unsettable: bool, derived: bool, EStructuralFeature: "encore_EClass" = None, encore_EStructuralFeature: "encore_EClass" = None, eStructuralFeatures: "encore_EClass" = None):
        self.changeable = changeable
        self.volatile = volatile
        self.transient = transient
        self.defaultValueLiteral = defaultValueLiteral
        self.defaultValue = defaultValue
        self.unsettable = unsettable
        self.derived = derived
        self.EStructuralFeature = EStructuralFeature
        self.encore_EStructuralFeature = encore_EStructuralFeature
        self.eStructuralFeatures = eStructuralFeatures
        
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
    def encore_EStructuralFeature(self):
        return self.__encore_EStructuralFeature

    @encore_EStructuralFeature.setter
    def encore_EStructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EStructuralFeature__encore_EStructuralFeature", None)
        self.__encore_EStructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EClass28"):
                opp_val = getattr(old_value, "encore_EClass28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EClass28"):
                opp_val = getattr(value, "encore_EClass28", None)
                if opp_val is None:
                    setattr(value, "encore_EClass28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EStructuralFeature(self):
        return self.__EStructuralFeature

    @EStructuralFeature.setter
    def EStructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EStructuralFeature__EStructuralFeature", None)
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
        old_value = getattr(self, f"_encore_EStructuralFeature__eStructuralFeatures", None)
        self.__eStructuralFeatures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EClass82"):
                opp_val = getattr(old_value, "EClass82", None)
                if opp_val == self:
                    setattr(old_value, "EClass82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EClass82"):
                opp_val = getattr(value, "EClass82", None)
                setattr(value, "EClass82", self)

    def getContainerClass(self):
        # TODO: Implement getContainerClass method
        pass

    def getFeatureID(self) -> int:
        # TODO: Implement getFeatureID method
        pass

class ENamedElement:

    pass
class encore_ETypeParameter(ENamedElement):

    pass
class encore_EEnumLiteral(ENamedElement):

    def __init__(self, value: int, instance: str, literal: str, eLiterals: "encore_EEnum" = None, EEnumLiteral: "encore_EEnum" = None):
        self.value = value
        self.instance = instance
        self.literal = literal
        self.eLiterals = eLiterals
        self.EEnumLiteral = EEnumLiteral
        
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
    def EEnumLiteral(self):
        return self.__EEnumLiteral

    @EEnumLiteral.setter
    def EEnumLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EEnumLiteral__EEnumLiteral", None)
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
        old_value = getattr(self, f"_encore_EEnumLiteral__eLiterals", None)
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

class encore_EPackage(ENamedElement):

    def __init__(self, nsURI: str, nsPrefix: str, encore_EPackage: "encore_EClassifier" = None, EPackage: "encore_EFactory" = None, encore_EPackage66: "encore_EPackage" = None, encore_EPackage64: set["encore_EPackage"] = None, encore_EPackage69: "encore_EPackage" = None, encore_EPackage67: "encore_EPackage" = None, ePackage: "encore_EFactory" = None, encore_EPackage62: set["encore_EClassifier"] = None):
        self.nsURI = nsURI
        self.nsPrefix = nsPrefix
        self.encore_EPackage = encore_EPackage
        self.EPackage = EPackage
        self.encore_EPackage66 = encore_EPackage66
        self.encore_EPackage64 = encore_EPackage64 if encore_EPackage64 is not None else set()
        self.encore_EPackage69 = encore_EPackage69
        self.encore_EPackage67 = encore_EPackage67
        self.ePackage = ePackage
        self.encore_EPackage62 = encore_EPackage62 if encore_EPackage62 is not None else set()
        
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
    def encore_EPackage67(self):
        return self.__encore_EPackage67

    @encore_EPackage67.setter
    def encore_EPackage67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EPackage__encore_EPackage67", None)
        self.__encore_EPackage67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EPackage69"):
                opp_val = getattr(old_value, "encore_EPackage69", None)
                if opp_val == self:
                    setattr(old_value, "encore_EPackage69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EPackage69"):
                opp_val = getattr(value, "encore_EPackage69", None)
                setattr(value, "encore_EPackage69", self)

    @property
    def encore_EPackage66(self):
        return self.__encore_EPackage66

    @encore_EPackage66.setter
    def encore_EPackage66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EPackage__encore_EPackage66", None)
        self.__encore_EPackage66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EPackage64"):
                opp_val = getattr(old_value, "encore_EPackage64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EPackage64"):
                opp_val = getattr(value, "encore_EPackage64", None)
                if opp_val is None:
                    setattr(value, "encore_EPackage64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ePackage(self):
        return self.__ePackage

    @ePackage.setter
    def ePackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EPackage__ePackage", None)
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
    def encore_EPackage69(self):
        return self.__encore_EPackage69

    @encore_EPackage69.setter
    def encore_EPackage69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EPackage__encore_EPackage69", None)
        self.__encore_EPackage69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EPackage67"):
                opp_val = getattr(old_value, "encore_EPackage67", None)
                if opp_val == self:
                    setattr(old_value, "encore_EPackage67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EPackage67"):
                opp_val = getattr(value, "encore_EPackage67", None)
                setattr(value, "encore_EPackage67", self)

    @property
    def EPackage(self):
        return self.__EPackage

    @EPackage.setter
    def EPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EPackage__EPackage", None)
        self.__EPackage = value
        
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
    def encore_EPackage64(self):
        return self.__encore_EPackage64

    @encore_EPackage64.setter
    def encore_EPackage64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EPackage__encore_EPackage64", None)
        self.__encore_EPackage64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encore_EPackage66"):
                    opp_val = getattr(item, "encore_EPackage66", None)
                    
                    if opp_val == self:
                        setattr(item, "encore_EPackage66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encore_EPackage66"):
                    opp_val = getattr(item, "encore_EPackage66", None)
                    
                    setattr(item, "encore_EPackage66", self)
                    

    @property
    def encore_EPackage(self):
        return self.__encore_EPackage

    @encore_EPackage.setter
    def encore_EPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EPackage__encore_EPackage", None)
        self.__encore_EPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EClassifier"):
                opp_val = getattr(old_value, "encore_EClassifier", None)
                if opp_val == self:
                    setattr(old_value, "encore_EClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EClassifier"):
                opp_val = getattr(value, "encore_EClassifier", None)
                setattr(value, "encore_EClassifier", self)

    @property
    def encore_EPackage62(self):
        return self.__encore_EPackage62

    @encore_EPackage62.setter
    def encore_EPackage62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EPackage__encore_EPackage62", None)
        self.__encore_EPackage62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encore_EClassifier63"):
                    opp_val = getattr(item, "encore_EClassifier63", None)
                    
                    if opp_val == self:
                        setattr(item, "encore_EClassifier63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encore_EClassifier63"):
                    opp_val = getattr(item, "encore_EClassifier63", None)
                    
                    setattr(item, "encore_EClassifier63", self)
                    

    def getEClassifier(self, name: str) -> EClassifier:
        # TODO: Implement getEClassifier method
        pass

class encore_ETypedElement(ENamedElement):

    def __init__(self, ordered: bool, unique: bool, lowerBound: int, upperBound: int, many: bool, required: bool, encore_ETypedElement86: "encore_EGenericType" = None, encore_ETypedElement: "encore_EClassifier" = None):
        self.ordered = ordered
        self.unique = unique
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.many = many
        self.required = required
        self.encore_ETypedElement86 = encore_ETypedElement86
        self.encore_ETypedElement = encore_ETypedElement
        
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
    def encore_ETypedElement(self):
        return self.__encore_ETypedElement

    @encore_ETypedElement.setter
    def encore_ETypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_ETypedElement__encore_ETypedElement", None)
        self.__encore_ETypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EClassifier84"):
                opp_val = getattr(old_value, "encore_EClassifier84", None)
                if opp_val == self:
                    setattr(old_value, "encore_EClassifier84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EClassifier84"):
                opp_val = getattr(value, "encore_EClassifier84", None)
                setattr(value, "encore_EClassifier84", self)

    @property
    def encore_ETypedElement86(self):
        return self.__encore_ETypedElement86

    @encore_ETypedElement86.setter
    def encore_ETypedElement86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_ETypedElement__encore_ETypedElement86", None)
        self.__encore_ETypedElement86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EGenericType87"):
                opp_val = getattr(old_value, "encore_EGenericType87", None)
                if opp_val == self:
                    setattr(old_value, "encore_EGenericType87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EGenericType87"):
                opp_val = getattr(value, "encore_EGenericType87", None)
                setattr(value, "encore_EGenericType87", self)

class encore_EClassifier(ENamedElement):

    def __init__(self, defaultValue: str, instanceTypeName: str, instanceClassName: str, instanceClass: str, encore_EClassifier: "encore_EPackage" = None, encore_EClassifier44: set["encore_ETypeParameter"] = None, encore_EClassifier56: "encore_EOperation" = None, encore_EClassifier63: "encore_EPackage" = None, encore_EClassifier84: "encore_ETypedElement" = None, encore_EClassifier105: "encore_EGenericType" = None, encore_EClassifier96: "encore_EGenericType" = None):
        self.defaultValue = defaultValue
        self.instanceTypeName = instanceTypeName
        self.instanceClassName = instanceClassName
        self.instanceClass = instanceClass
        self.encore_EClassifier = encore_EClassifier
        self.encore_EClassifier44 = encore_EClassifier44 if encore_EClassifier44 is not None else set()
        self.encore_EClassifier56 = encore_EClassifier56
        self.encore_EClassifier63 = encore_EClassifier63
        self.encore_EClassifier84 = encore_EClassifier84
        self.encore_EClassifier105 = encore_EClassifier105
        self.encore_EClassifier96 = encore_EClassifier96
        
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
    def encore_EClassifier(self):
        return self.__encore_EClassifier

    @encore_EClassifier.setter
    def encore_EClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClassifier__encore_EClassifier", None)
        self.__encore_EClassifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EPackage"):
                opp_val = getattr(old_value, "encore_EPackage", None)
                if opp_val == self:
                    setattr(old_value, "encore_EPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EPackage"):
                opp_val = getattr(value, "encore_EPackage", None)
                setattr(value, "encore_EPackage", self)

    @property
    def encore_EClassifier56(self):
        return self.__encore_EClassifier56

    @encore_EClassifier56.setter
    def encore_EClassifier56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClassifier__encore_EClassifier56", None)
        self.__encore_EClassifier56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EOperation55"):
                opp_val = getattr(old_value, "encore_EOperation55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EOperation55"):
                opp_val = getattr(value, "encore_EOperation55", None)
                if opp_val is None:
                    setattr(value, "encore_EOperation55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def encore_EClassifier44(self):
        return self.__encore_EClassifier44

    @encore_EClassifier44.setter
    def encore_EClassifier44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClassifier__encore_EClassifier44", None)
        self.__encore_EClassifier44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encore_ETypeParameter"):
                    opp_val = getattr(item, "encore_ETypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "encore_ETypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encore_ETypeParameter"):
                    opp_val = getattr(item, "encore_ETypeParameter", None)
                    
                    setattr(item, "encore_ETypeParameter", self)
                    

    @property
    def encore_EClassifier96(self):
        return self.__encore_EClassifier96

    @encore_EClassifier96.setter
    def encore_EClassifier96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClassifier__encore_EClassifier96", None)
        self.__encore_EClassifier96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EGenericType95"):
                opp_val = getattr(old_value, "encore_EGenericType95", None)
                if opp_val == self:
                    setattr(old_value, "encore_EGenericType95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EGenericType95"):
                opp_val = getattr(value, "encore_EGenericType95", None)
                setattr(value, "encore_EGenericType95", self)

    @property
    def encore_EClassifier105(self):
        return self.__encore_EClassifier105

    @encore_EClassifier105.setter
    def encore_EClassifier105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClassifier__encore_EClassifier105", None)
        self.__encore_EClassifier105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EGenericType104"):
                opp_val = getattr(old_value, "encore_EGenericType104", None)
                if opp_val == self:
                    setattr(old_value, "encore_EGenericType104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EGenericType104"):
                opp_val = getattr(value, "encore_EGenericType104", None)
                setattr(value, "encore_EGenericType104", self)

    @property
    def encore_EClassifier63(self):
        return self.__encore_EClassifier63

    @encore_EClassifier63.setter
    def encore_EClassifier63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClassifier__encore_EClassifier63", None)
        self.__encore_EClassifier63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EPackage62"):
                opp_val = getattr(old_value, "encore_EPackage62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EPackage62"):
                opp_val = getattr(value, "encore_EPackage62", None)
                if opp_val is None:
                    setattr(value, "encore_EPackage62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def encore_EClassifier84(self):
        return self.__encore_EClassifier84

    @encore_EClassifier84.setter
    def encore_EClassifier84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClassifier__encore_EClassifier84", None)
        self.__encore_EClassifier84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_ETypedElement"):
                opp_val = getattr(old_value, "encore_ETypedElement", None)
                if opp_val == self:
                    setattr(old_value, "encore_ETypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_ETypedElement"):
                opp_val = getattr(value, "encore_ETypedElement", None)
                setattr(value, "encore_ETypedElement", self)

    def isInstance(self, object: str) -> bool:
        # TODO: Implement isInstance method
        pass

    def getClassifierID(self) -> int:
        # TODO: Implement getClassifierID method
        pass

class encore_EGenericType:

    pass
class encore_EOperation(ETypedElement):

    def __init__(self, encore_EOperation: "encore_EClass" = None, EOperation: "encore_EClass" = None, eOperation: set["encore_EParameter"] = None, encore_EOperation55: set["encore_EClassifier"] = None, encore_EOperation58: set["encore_EGenericType"] = None, eOperations: "encore_EClass" = None, encore_EOperation51: set["encore_ETypeParameter"] = None, EOperation71: "encore_EParameter" = None):
        self.encore_EOperation = encore_EOperation
        self.EOperation = EOperation
        self.eOperation = eOperation if eOperation is not None else set()
        self.encore_EOperation55 = encore_EOperation55 if encore_EOperation55 is not None else set()
        self.encore_EOperation58 = encore_EOperation58 if encore_EOperation58 is not None else set()
        self.eOperations = eOperations
        self.encore_EOperation51 = encore_EOperation51 if encore_EOperation51 is not None else set()
        self.EOperation71 = EOperation71
        
    @property
    def EOperation(self):
        return self.__EOperation

    @EOperation.setter
    def EOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EOperation__EOperation", None)
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
    def eOperation(self):
        return self.__eOperation

    @eOperation.setter
    def eOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EOperation__eOperation", None)
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
    def EOperation71(self):
        return self.__EOperation71

    @EOperation71.setter
    def EOperation71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EOperation__EOperation71", None)
        self.__EOperation71 = value
        
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
    def eOperations(self):
        return self.__eOperations

    @eOperations.setter
    def eOperations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EOperation__eOperations", None)
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
    def encore_EOperation(self):
        return self.__encore_EOperation

    @encore_EOperation.setter
    def encore_EOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EOperation__encore_EOperation", None)
        self.__encore_EOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EClass26"):
                opp_val = getattr(old_value, "encore_EClass26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EClass26"):
                opp_val = getattr(value, "encore_EClass26", None)
                if opp_val is None:
                    setattr(value, "encore_EClass26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def encore_EOperation51(self):
        return self.__encore_EOperation51

    @encore_EOperation51.setter
    def encore_EOperation51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EOperation__encore_EOperation51", None)
        self.__encore_EOperation51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encore_ETypeParameter52"):
                    opp_val = getattr(item, "encore_ETypeParameter52", None)
                    
                    if opp_val == self:
                        setattr(item, "encore_ETypeParameter52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encore_ETypeParameter52"):
                    opp_val = getattr(item, "encore_ETypeParameter52", None)
                    
                    setattr(item, "encore_ETypeParameter52", self)
                    

    @property
    def encore_EOperation58(self):
        return self.__encore_EOperation58

    @encore_EOperation58.setter
    def encore_EOperation58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EOperation__encore_EOperation58", None)
        self.__encore_EOperation58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encore_EGenericType59"):
                    opp_val = getattr(item, "encore_EGenericType59", None)
                    
                    if opp_val == self:
                        setattr(item, "encore_EGenericType59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encore_EGenericType59"):
                    opp_val = getattr(item, "encore_EGenericType59", None)
                    
                    setattr(item, "encore_EGenericType59", self)
                    

    @property
    def encore_EOperation55(self):
        return self.__encore_EOperation55

    @encore_EOperation55.setter
    def encore_EOperation55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EOperation__encore_EOperation55", None)
        self.__encore_EOperation55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encore_EClassifier56"):
                    opp_val = getattr(item, "encore_EClassifier56", None)
                    
                    if opp_val == self:
                        setattr(item, "encore_EClassifier56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encore_EClassifier56"):
                    opp_val = getattr(item, "encore_EClassifier56", None)
                    
                    setattr(item, "encore_EClassifier56", self)
                    

    def getOperationID(self) -> int:
        # TODO: Implement getOperationID method
        pass

    def isOverrideOf(self, someOperation: str) -> bool:
        # TODO: Implement isOverrideOf method
        pass

class EClassifier:

    pass
class encore_EClass(EClassifier):

    def __init__(self, abstract: bool, interface: bool, encore_EClass12: set["encore_EAttribute"] = None, encore_EClass15: set["encore_EReference"] = None, encore_EClass17: set["encore_EReference"] = None, encore_EClass20: set["encore_EAttribute"] = None, encore_EClass23: set["encore_EReference"] = None, encore_EClass26: set["encore_EOperation"] = None, encore_EClass: "encore_EClass" = None, encore_EClass8: set["encore_EClass"] = None, eContainingClass: set["encore_EOperation"] = None, encore_EClass33: "encore_EAttribute" = None, eContainingClass36: set["encore_EStructuralFeature"] = None, encore_EClass38: set["encore_EGenericType"] = None, encore_EClass40: set["encore_EGenericType"] = None, encore_EClass28: set["encore_EStructuralFeature"] = None, encore_EClass31: "encore_EClass" = None, encore_EClass29: set["encore_EClass"] = None, EClass: "encore_EOperation" = None, encore_EClass77: "encore_EReference" = None, EClass82: "encore_EStructuralFeature" = None):
        self.abstract = abstract
        self.interface = interface
        self.encore_EClass12 = encore_EClass12 if encore_EClass12 is not None else set()
        self.encore_EClass15 = encore_EClass15 if encore_EClass15 is not None else set()
        self.encore_EClass17 = encore_EClass17 if encore_EClass17 is not None else set()
        self.encore_EClass20 = encore_EClass20 if encore_EClass20 is not None else set()
        self.encore_EClass23 = encore_EClass23 if encore_EClass23 is not None else set()
        self.encore_EClass26 = encore_EClass26 if encore_EClass26 is not None else set()
        self.encore_EClass = encore_EClass
        self.encore_EClass8 = encore_EClass8 if encore_EClass8 is not None else set()
        self.eContainingClass = eContainingClass if eContainingClass is not None else set()
        self.encore_EClass33 = encore_EClass33
        self.eContainingClass36 = eContainingClass36 if eContainingClass36 is not None else set()
        self.encore_EClass38 = encore_EClass38 if encore_EClass38 is not None else set()
        self.encore_EClass40 = encore_EClass40 if encore_EClass40 is not None else set()
        self.encore_EClass28 = encore_EClass28 if encore_EClass28 is not None else set()
        self.encore_EClass31 = encore_EClass31
        self.encore_EClass29 = encore_EClass29 if encore_EClass29 is not None else set()
        self.EClass = EClass
        self.encore_EClass77 = encore_EClass77
        self.EClass82 = EClass82
        
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
    def eContainingClass36(self):
        return self.__eContainingClass36

    @eContainingClass36.setter
    def eContainingClass36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClass__eContainingClass36", None)
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
    def encore_EClass31(self):
        return self.__encore_EClass31

    @encore_EClass31.setter
    def encore_EClass31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClass__encore_EClass31", None)
        self.__encore_EClass31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EClass29"):
                opp_val = getattr(old_value, "encore_EClass29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EClass29"):
                opp_val = getattr(value, "encore_EClass29", None)
                if opp_val is None:
                    setattr(value, "encore_EClass29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def encore_EClass33(self):
        return self.__encore_EClass33

    @encore_EClass33.setter
    def encore_EClass33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClass__encore_EClass33", None)
        self.__encore_EClass33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EAttribute34"):
                opp_val = getattr(old_value, "encore_EAttribute34", None)
                if opp_val == self:
                    setattr(old_value, "encore_EAttribute34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EAttribute34"):
                opp_val = getattr(value, "encore_EAttribute34", None)
                setattr(value, "encore_EAttribute34", self)

    @property
    def encore_EClass15(self):
        return self.__encore_EClass15

    @encore_EClass15.setter
    def encore_EClass15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClass__encore_EClass15", None)
        self.__encore_EClass15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encore_EReference"):
                    opp_val = getattr(item, "encore_EReference", None)
                    
                    if opp_val == self:
                        setattr(item, "encore_EReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encore_EReference"):
                    opp_val = getattr(item, "encore_EReference", None)
                    
                    setattr(item, "encore_EReference", self)
                    

    @property
    def EClass82(self):
        return self.__EClass82

    @EClass82.setter
    def EClass82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClass__EClass82", None)
        self.__EClass82 = value
        
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
    def encore_EClass28(self):
        return self.__encore_EClass28

    @encore_EClass28.setter
    def encore_EClass28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClass__encore_EClass28", None)
        self.__encore_EClass28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encore_EStructuralFeature"):
                    opp_val = getattr(item, "encore_EStructuralFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "encore_EStructuralFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encore_EStructuralFeature"):
                    opp_val = getattr(item, "encore_EStructuralFeature", None)
                    
                    setattr(item, "encore_EStructuralFeature", self)
                    

    @property
    def encore_EClass8(self):
        return self.__encore_EClass8

    @encore_EClass8.setter
    def encore_EClass8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClass__encore_EClass8", None)
        self.__encore_EClass8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encore_EClass"):
                    opp_val = getattr(item, "encore_EClass", None)
                    
                    if opp_val == self:
                        setattr(item, "encore_EClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encore_EClass"):
                    opp_val = getattr(item, "encore_EClass", None)
                    
                    setattr(item, "encore_EClass", self)
                    

    @property
    def eContainingClass(self):
        return self.__eContainingClass

    @eContainingClass.setter
    def eContainingClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClass__eContainingClass", None)
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
    def encore_EClass17(self):
        return self.__encore_EClass17

    @encore_EClass17.setter
    def encore_EClass17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClass__encore_EClass17", None)
        self.__encore_EClass17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encore_EReference18"):
                    opp_val = getattr(item, "encore_EReference18", None)
                    
                    if opp_val == self:
                        setattr(item, "encore_EReference18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encore_EReference18"):
                    opp_val = getattr(item, "encore_EReference18", None)
                    
                    setattr(item, "encore_EReference18", self)
                    

    @property
    def encore_EClass(self):
        return self.__encore_EClass

    @encore_EClass.setter
    def encore_EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClass__encore_EClass", None)
        self.__encore_EClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EClass8"):
                opp_val = getattr(old_value, "encore_EClass8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EClass8"):
                opp_val = getattr(value, "encore_EClass8", None)
                if opp_val is None:
                    setattr(value, "encore_EClass8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def encore_EClass38(self):
        return self.__encore_EClass38

    @encore_EClass38.setter
    def encore_EClass38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClass__encore_EClass38", None)
        self.__encore_EClass38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encore_EGenericType"):
                    opp_val = getattr(item, "encore_EGenericType", None)
                    
                    if opp_val == self:
                        setattr(item, "encore_EGenericType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encore_EGenericType"):
                    opp_val = getattr(item, "encore_EGenericType", None)
                    
                    setattr(item, "encore_EGenericType", self)
                    

    @property
    def encore_EClass12(self):
        return self.__encore_EClass12

    @encore_EClass12.setter
    def encore_EClass12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClass__encore_EClass12", None)
        self.__encore_EClass12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encore_EAttribute13"):
                    opp_val = getattr(item, "encore_EAttribute13", None)
                    
                    if opp_val == self:
                        setattr(item, "encore_EAttribute13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encore_EAttribute13"):
                    opp_val = getattr(item, "encore_EAttribute13", None)
                    
                    setattr(item, "encore_EAttribute13", self)
                    

    @property
    def EClass(self):
        return self.__EClass

    @EClass.setter
    def EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClass__EClass", None)
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
    def encore_EClass26(self):
        return self.__encore_EClass26

    @encore_EClass26.setter
    def encore_EClass26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClass__encore_EClass26", None)
        self.__encore_EClass26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encore_EOperation"):
                    opp_val = getattr(item, "encore_EOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "encore_EOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encore_EOperation"):
                    opp_val = getattr(item, "encore_EOperation", None)
                    
                    setattr(item, "encore_EOperation", self)
                    

    @property
    def encore_EClass40(self):
        return self.__encore_EClass40

    @encore_EClass40.setter
    def encore_EClass40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClass__encore_EClass40", None)
        self.__encore_EClass40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encore_EGenericType41"):
                    opp_val = getattr(item, "encore_EGenericType41", None)
                    
                    if opp_val == self:
                        setattr(item, "encore_EGenericType41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encore_EGenericType41"):
                    opp_val = getattr(item, "encore_EGenericType41", None)
                    
                    setattr(item, "encore_EGenericType41", self)
                    

    @property
    def encore_EClass77(self):
        return self.__encore_EClass77

    @encore_EClass77.setter
    def encore_EClass77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClass__encore_EClass77", None)
        self.__encore_EClass77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EReference76"):
                opp_val = getattr(old_value, "encore_EReference76", None)
                if opp_val == self:
                    setattr(old_value, "encore_EReference76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EReference76"):
                opp_val = getattr(value, "encore_EReference76", None)
                setattr(value, "encore_EReference76", self)

    @property
    def encore_EClass23(self):
        return self.__encore_EClass23

    @encore_EClass23.setter
    def encore_EClass23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClass__encore_EClass23", None)
        self.__encore_EClass23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encore_EReference24"):
                    opp_val = getattr(item, "encore_EReference24", None)
                    
                    if opp_val == self:
                        setattr(item, "encore_EReference24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encore_EReference24"):
                    opp_val = getattr(item, "encore_EReference24", None)
                    
                    setattr(item, "encore_EReference24", self)
                    

    @property
    def encore_EClass29(self):
        return self.__encore_EClass29

    @encore_EClass29.setter
    def encore_EClass29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClass__encore_EClass29", None)
        self.__encore_EClass29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encore_EClass31"):
                    opp_val = getattr(item, "encore_EClass31", None)
                    
                    if opp_val == self:
                        setattr(item, "encore_EClass31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encore_EClass31"):
                    opp_val = getattr(item, "encore_EClass31", None)
                    
                    setattr(item, "encore_EClass31", self)
                    

    @property
    def encore_EClass20(self):
        return self.__encore_EClass20

    @encore_EClass20.setter
    def encore_EClass20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EClass__encore_EClass20", None)
        self.__encore_EClass20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encore_EAttribute21"):
                    opp_val = getattr(item, "encore_EAttribute21", None)
                    
                    if opp_val == self:
                        setattr(item, "encore_EAttribute21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encore_EAttribute21"):
                    opp_val = getattr(item, "encore_EAttribute21", None)
                    
                    setattr(item, "encore_EAttribute21", self)
                    

    def getFeatureCount(self) -> int:
        # TODO: Implement getFeatureCount method
        pass

    def getEOperation(self, operationID: int) -> str:
        # TODO: Implement getEOperation method
        pass

    def getEStructuralFeature(self, featureID: int) -> EStructuralFeature:
        # TODO: Implement getEStructuralFeature method
        pass

    def getEStructuralFeature(self, featureName: str) -> EStructuralFeature:
        # TODO: Implement getEStructuralFeature method
        pass

    def getOperationID(self, operation: str) -> int:
        # TODO: Implement getOperationID method
        pass

    def getFeatureID(self, feature: EStructuralFeature) -> int:
        # TODO: Implement getFeatureID method
        pass

    def getOverride(self, operation: str) -> str:
        # TODO: Implement getOverride method
        pass

    def getOperationCount(self) -> int:
        # TODO: Implement getOperationCount method
        pass

    def isSuperTypeOf(self, someClass: str) -> bool:
        # TODO: Implement isSuperTypeOf method
        pass

class encore_EObject:

    def __init__(self, encore_EObject: "encore_EAnnotation" = None, encore_EObject7: "encore_EAnnotation" = None):
        self.encore_EObject = encore_EObject
        self.encore_EObject7 = encore_EObject7
        
    @property
    def encore_EObject(self):
        return self.__encore_EObject

    @encore_EObject.setter
    def encore_EObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EObject__encore_EObject", None)
        self.__encore_EObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EAnnotation4"):
                opp_val = getattr(old_value, "encore_EAnnotation4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EAnnotation4"):
                opp_val = getattr(value, "encore_EAnnotation4", None)
                if opp_val is None:
                    setattr(value, "encore_EAnnotation4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def encore_EObject7(self):
        return self.__encore_EObject7

    @encore_EObject7.setter
    def encore_EObject7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EObject__encore_EObject7", None)
        self.__encore_EObject7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EAnnotation6"):
                opp_val = getattr(old_value, "encore_EAnnotation6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EAnnotation6"):
                opp_val = getattr(value, "encore_EAnnotation6", None)
                if opp_val is None:
                    setattr(value, "encore_EAnnotation6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def eAllContents(self):
        # TODO: Implement eAllContents method
        pass

    def eInvoke(self, arguments: str, operation: str) -> str:
        # TODO: Implement eInvoke method
        pass

    def eIsSet(self, feature: EStructuralFeature) -> bool:
        # TODO: Implement eIsSet method
        pass

    def eCrossReferences(self):
        # TODO: Implement eCrossReferences method
        pass

    def eIsProxy(self) -> bool:
        # TODO: Implement eIsProxy method
        pass

    def eContainmentFeature(self) -> str:
        # TODO: Implement eContainmentFeature method
        pass

    def eGet(self, feature: EStructuralFeature) -> str:
        # TODO: Implement eGet method
        pass

    def eGet(self, resolve: bool, feature: EStructuralFeature) -> str:
        # TODO: Implement eGet method
        pass

    def eContainingFeature(self) -> EStructuralFeature:
        # TODO: Implement eContainingFeature method
        pass

    def eSet(self, newValue: str, feature: EStructuralFeature):
        # TODO: Implement eSet method
        pass

    def eResource(self) -> str:
        # TODO: Implement eResource method
        pass

    def eContents(self):
        # TODO: Implement eContents method
        pass

    def eClass(self) -> str:
        # TODO: Implement eClass method
        pass

    def eContainer(self) -> str:
        # TODO: Implement eContainer method
        pass

    def eUnset(self, feature: EStructuralFeature):
        # TODO: Implement eUnset method
        pass

class encore_EModelElement(ABC):

    def __init__(self, EModelElement: "encore_EAnnotation" = None, eModelElement: set["encore_EAnnotation"] = None):
        self.EModelElement = EModelElement
        self.eModelElement = eModelElement if eModelElement is not None else set()
        
    @property
    def eModelElement(self):
        return self.__eModelElement

    @eModelElement.setter
    def eModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EModelElement__eModelElement", None)
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
        old_value = getattr(self, f"_encore_EModelElement__EModelElement", None)
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

class encore_EStringToStringMapEntry:

    def __init__(self, key: str, value: str, encore_EStringToStringMapEntry: "encore_EAnnotation" = None):
        self.key = key
        self.value = value
        self.encore_EStringToStringMapEntry = encore_EStringToStringMapEntry
        
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
    def encore_EStringToStringMapEntry(self):
        return self.__encore_EStringToStringMapEntry

    @encore_EStringToStringMapEntry.setter
    def encore_EStringToStringMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EStringToStringMapEntry__encore_EStringToStringMapEntry", None)
        self.__encore_EStringToStringMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EAnnotation"):
                opp_val = getattr(old_value, "encore_EAnnotation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EAnnotation"):
                opp_val = getattr(value, "encore_EAnnotation", None)
                if opp_val is None:
                    setattr(value, "encore_EAnnotation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EModelElement:

    pass
class encore_EFactory(EModelElement):

    def __init__(self, eFactoryInstance: "encore_EPackage" = None, EFactory: "encore_EPackage" = None):
        self.eFactoryInstance = eFactoryInstance
        self.EFactory = EFactory
        
    @property
    def EFactory(self):
        return self.__EFactory

    @EFactory.setter
    def EFactory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EFactory__EFactory", None)
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
        old_value = getattr(self, f"_encore_EFactory__eFactoryInstance", None)
        self.__eFactoryInstance = value
        
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

    def convertToString(self, instanceValue: str, eDataType: EDataType) -> str:
        # TODO: Implement convertToString method
        pass

    def create(self, eClass: str) -> str:
        # TODO: Implement create method
        pass

    def createFromString(self, eDataType: EDataType, literalValue: str) -> str:
        # TODO: Implement createFromString method
        pass

class encore_ENamedElement(EModelElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class encore_EAnnotation(EModelElement):

    def __init__(self, source: str, encore_EAnnotation: set["encore_EStringToStringMapEntry"] = None, eAnnotations: "encore_EModelElement" = None, encore_EAnnotation4: set["encore_EObject"] = None, encore_EAnnotation6: set["encore_EObject"] = None, EAnnotation: "encore_EModelElement" = None):
        self.source = source
        self.encore_EAnnotation = encore_EAnnotation if encore_EAnnotation is not None else set()
        self.eAnnotations = eAnnotations
        self.encore_EAnnotation4 = encore_EAnnotation4 if encore_EAnnotation4 is not None else set()
        self.encore_EAnnotation6 = encore_EAnnotation6 if encore_EAnnotation6 is not None else set()
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
        old_value = getattr(self, f"_encore_EAnnotation__EAnnotation", None)
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
    def encore_EAnnotation(self):
        return self.__encore_EAnnotation

    @encore_EAnnotation.setter
    def encore_EAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EAnnotation__encore_EAnnotation", None)
        self.__encore_EAnnotation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encore_EStringToStringMapEntry"):
                    opp_val = getattr(item, "encore_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "encore_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encore_EStringToStringMapEntry"):
                    opp_val = getattr(item, "encore_EStringToStringMapEntry", None)
                    
                    setattr(item, "encore_EStringToStringMapEntry", self)
                    

    @property
    def eAnnotations(self):
        return self.__eAnnotations

    @eAnnotations.setter
    def eAnnotations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EAnnotation__eAnnotations", None)
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
    def encore_EAnnotation6(self):
        return self.__encore_EAnnotation6

    @encore_EAnnotation6.setter
    def encore_EAnnotation6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EAnnotation__encore_EAnnotation6", None)
        self.__encore_EAnnotation6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encore_EObject7"):
                    opp_val = getattr(item, "encore_EObject7", None)
                    
                    if opp_val == self:
                        setattr(item, "encore_EObject7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encore_EObject7"):
                    opp_val = getattr(item, "encore_EObject7", None)
                    
                    setattr(item, "encore_EObject7", self)
                    

    @property
    def encore_EAnnotation4(self):
        return self.__encore_EAnnotation4

    @encore_EAnnotation4.setter
    def encore_EAnnotation4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EAnnotation__encore_EAnnotation4", None)
        self.__encore_EAnnotation4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encore_EObject"):
                    opp_val = getattr(item, "encore_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "encore_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encore_EObject"):
                    opp_val = getattr(item, "encore_EObject", None)
                    
                    setattr(item, "encore_EObject", self)
                    

class encore_EDataType(EClassifier):

    def __init__(self, serializable: bool, encore_EDataType: "encore_EAttribute" = None):
        self.serializable = serializable
        self.encore_EDataType = encore_EDataType
        
    @property
    def serializable(self) -> bool:
        return self.__serializable

    @serializable.setter
    def serializable(self, serializable: bool):
        self.__serializable = serializable

    @property
    def encore_EDataType(self):
        return self.__encore_EDataType

    @encore_EDataType.setter
    def encore_EDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EDataType__encore_EDataType", None)
        self.__encore_EDataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EAttribute"):
                opp_val = getattr(old_value, "encore_EAttribute", None)
                if opp_val == self:
                    setattr(old_value, "encore_EAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EAttribute"):
                opp_val = getattr(value, "encore_EAttribute", None)
                setattr(value, "encore_EAttribute", self)

class EStructuralFeature:

    pass
class encore_EReference(EStructuralFeature):

    def __init__(self, containment: bool, container: bool, resolveProxies: bool, encore_EReference: "encore_EClass" = None, encore_EReference18: "encore_EClass" = None, encore_EReference24: "encore_EClass" = None, encore_EReference74: "encore_EReference" = None, encore_EReference72: "encore_EReference" = None, encore_EReference76: "encore_EClass" = None, encore_EReference79: set["encore_EAttribute"] = None):
        self.containment = containment
        self.container = container
        self.resolveProxies = resolveProxies
        self.encore_EReference = encore_EReference
        self.encore_EReference18 = encore_EReference18
        self.encore_EReference24 = encore_EReference24
        self.encore_EReference74 = encore_EReference74
        self.encore_EReference72 = encore_EReference72
        self.encore_EReference76 = encore_EReference76
        self.encore_EReference79 = encore_EReference79 if encore_EReference79 is not None else set()
        
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
    def encore_EReference76(self):
        return self.__encore_EReference76

    @encore_EReference76.setter
    def encore_EReference76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EReference__encore_EReference76", None)
        self.__encore_EReference76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EClass77"):
                opp_val = getattr(old_value, "encore_EClass77", None)
                if opp_val == self:
                    setattr(old_value, "encore_EClass77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EClass77"):
                opp_val = getattr(value, "encore_EClass77", None)
                setattr(value, "encore_EClass77", self)

    @property
    def encore_EReference(self):
        return self.__encore_EReference

    @encore_EReference.setter
    def encore_EReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EReference__encore_EReference", None)
        self.__encore_EReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EClass15"):
                opp_val = getattr(old_value, "encore_EClass15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EClass15"):
                opp_val = getattr(value, "encore_EClass15", None)
                if opp_val is None:
                    setattr(value, "encore_EClass15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def encore_EReference72(self):
        return self.__encore_EReference72

    @encore_EReference72.setter
    def encore_EReference72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EReference__encore_EReference72", None)
        self.__encore_EReference72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EReference74"):
                opp_val = getattr(old_value, "encore_EReference74", None)
                if opp_val == self:
                    setattr(old_value, "encore_EReference74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EReference74"):
                opp_val = getattr(value, "encore_EReference74", None)
                setattr(value, "encore_EReference74", self)

    @property
    def encore_EReference79(self):
        return self.__encore_EReference79

    @encore_EReference79.setter
    def encore_EReference79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EReference__encore_EReference79", None)
        self.__encore_EReference79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encore_EAttribute80"):
                    opp_val = getattr(item, "encore_EAttribute80", None)
                    
                    if opp_val == self:
                        setattr(item, "encore_EAttribute80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encore_EAttribute80"):
                    opp_val = getattr(item, "encore_EAttribute80", None)
                    
                    setattr(item, "encore_EAttribute80", self)
                    

    @property
    def encore_EReference74(self):
        return self.__encore_EReference74

    @encore_EReference74.setter
    def encore_EReference74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EReference__encore_EReference74", None)
        self.__encore_EReference74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EReference72"):
                opp_val = getattr(old_value, "encore_EReference72", None)
                if opp_val == self:
                    setattr(old_value, "encore_EReference72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EReference72"):
                opp_val = getattr(value, "encore_EReference72", None)
                setattr(value, "encore_EReference72", self)

    @property
    def encore_EReference24(self):
        return self.__encore_EReference24

    @encore_EReference24.setter
    def encore_EReference24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EReference__encore_EReference24", None)
        self.__encore_EReference24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EClass23"):
                opp_val = getattr(old_value, "encore_EClass23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EClass23"):
                opp_val = getattr(value, "encore_EClass23", None)
                if opp_val is None:
                    setattr(value, "encore_EClass23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def encore_EReference18(self):
        return self.__encore_EReference18

    @encore_EReference18.setter
    def encore_EReference18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EReference__encore_EReference18", None)
        self.__encore_EReference18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EClass17"):
                opp_val = getattr(old_value, "encore_EClass17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EClass17"):
                opp_val = getattr(value, "encore_EClass17", None)
                if opp_val is None:
                    setattr(value, "encore_EClass17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class encore_EAttribute(EStructuralFeature):

    def __init__(self, iD: bool, encore_EAttribute: "encore_EDataType" = None, encore_EAttribute13: "encore_EClass" = None, encore_EAttribute21: "encore_EClass" = None, encore_EAttribute34: "encore_EClass" = None, encore_EAttribute80: "encore_EReference" = None):
        self.iD = iD
        self.encore_EAttribute = encore_EAttribute
        self.encore_EAttribute13 = encore_EAttribute13
        self.encore_EAttribute21 = encore_EAttribute21
        self.encore_EAttribute34 = encore_EAttribute34
        self.encore_EAttribute80 = encore_EAttribute80
        
    @property
    def iD(self) -> bool:
        return self.__iD

    @iD.setter
    def iD(self, iD: bool):
        self.__iD = iD

    @property
    def encore_EAttribute34(self):
        return self.__encore_EAttribute34

    @encore_EAttribute34.setter
    def encore_EAttribute34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EAttribute__encore_EAttribute34", None)
        self.__encore_EAttribute34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EClass33"):
                opp_val = getattr(old_value, "encore_EClass33", None)
                if opp_val == self:
                    setattr(old_value, "encore_EClass33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EClass33"):
                opp_val = getattr(value, "encore_EClass33", None)
                setattr(value, "encore_EClass33", self)

    @property
    def encore_EAttribute(self):
        return self.__encore_EAttribute

    @encore_EAttribute.setter
    def encore_EAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EAttribute__encore_EAttribute", None)
        self.__encore_EAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EDataType"):
                opp_val = getattr(old_value, "encore_EDataType", None)
                if opp_val == self:
                    setattr(old_value, "encore_EDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EDataType"):
                opp_val = getattr(value, "encore_EDataType", None)
                setattr(value, "encore_EDataType", self)

    @property
    def encore_EAttribute13(self):
        return self.__encore_EAttribute13

    @encore_EAttribute13.setter
    def encore_EAttribute13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EAttribute__encore_EAttribute13", None)
        self.__encore_EAttribute13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EClass12"):
                opp_val = getattr(old_value, "encore_EClass12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EClass12"):
                opp_val = getattr(value, "encore_EClass12", None)
                if opp_val is None:
                    setattr(value, "encore_EClass12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def encore_EAttribute80(self):
        return self.__encore_EAttribute80

    @encore_EAttribute80.setter
    def encore_EAttribute80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EAttribute__encore_EAttribute80", None)
        self.__encore_EAttribute80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EReference79"):
                opp_val = getattr(old_value, "encore_EReference79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EReference79"):
                opp_val = getattr(value, "encore_EReference79", None)
                if opp_val is None:
                    setattr(value, "encore_EReference79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def encore_EAttribute21(self):
        return self.__encore_EAttribute21

    @encore_EAttribute21.setter
    def encore_EAttribute21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_encore_EAttribute__encore_EAttribute21", None)
        self.__encore_EAttribute21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encore_EClass20"):
                opp_val = getattr(old_value, "encore_EClass20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encore_EClass20"):
                opp_val = getattr(value, "encore_EClass20", None)
                if opp_val is None:
                    setattr(value, "encore_EClass20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
