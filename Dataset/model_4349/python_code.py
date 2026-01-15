from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class EEnumLiteral:

    pass
class ecoreDiff_ChangedEEnumLiteral(EEnumLiteral):

    pass
class ecoreDiff_DeletedEEnumLiteral(EEnumLiteral):

    pass
class ecoreDiff_AddedEEnumLiteral(EEnumLiteral):

    pass
class EReference:

    pass
class ecoreDiff_AddedEReference(EReference):

    pass
class EStructuralFeature_Wildcard:

    pass
class ecoreDiff_DeletedEStructuralFeature_Wildcard(EStructuralFeature_Wildcard):

    pass
class ecoreDiff_ChangedEStructuralFeature_Wildcard(EStructuralFeature_Wildcard):

    pass
class ecoreDiff_AddedEStructuralFeature_Wildcard(EStructuralFeature_Wildcard):

    pass
class EEnum:

    pass
class ecoreDiff_ChangedEEnum(EEnum):

    pass
class ecoreDiff_DeletedEEnum(EEnum):

    pass
class ecoreDiff_AddedEEnum(EEnum):

    pass
class ecoreDiff_ChangedEReference(EReference):

    pass
class ecoreDiff_DeletedEReference(EReference):

    pass
class EParameter:

    pass
class ecoreDiff_DeletedEParameter(EParameter):

    pass
class ecoreDiff_AddedEParameter(EParameter):

    pass
class EAttribute:

    pass
class ecoreDiff_ChangedEAttribute(EAttribute):

    pass
class ecoreDiff_DeletedEAttribute(EAttribute):

    pass
class ecoreDiff_AddedEAttribute(EAttribute):

    pass
class ecoreDiff_ChangedEParameter(EParameter):

    pass
class EGenericType:

    pass
class ecoreDiff_ChangedEGenericType(EGenericType):

    pass
class ecoreDiff_DeletedEGenericType(EGenericType):

    pass
class ecoreDiff_AddedEGenericType(EGenericType):

    pass
class ETypeParameter:

    pass
class ecoreDiff_ChangedETypeParameter(ETypeParameter):

    pass
class ecoreDiff_DeletedETypeParameter(ETypeParameter):

    pass
class ecoreDiff_AddedETypeParameter(ETypeParameter):

    pass
class EOperation:

    pass
class ecoreDiff_DeletedEOperation(EOperation):

    pass
class ecoreDiff_ChangedEOperation(EOperation):

    pass
class ecoreDiff_AddedEOperation(EOperation):

    pass
class EClassifier_Wildcard:

    pass
class ecoreDiff_DeletedEClassifier_Wildcard(EClassifier_Wildcard):

    pass
class ecoreDiff_ChangedEClassifier_Wildcard(EClassifier_Wildcard):

    pass
class ecoreDiff_AddedEClassifier_Wildcard(EClassifier_Wildcard):

    pass
class EPackage:

    pass
class ecoreDiff_DeletedEPackage(EPackage):

    pass
class ecoreDiff_ChangedEPackage(EPackage):

    pass
class ecoreDiff_AddedEPackage(EPackage):

    pass
class EFactory:

    pass
class ecoreDiff_DeletedEFactory(EFactory):

    pass
class ecoreDiff_ChangedEFactory(EFactory):

    pass
class ecoreDiff_AddedEFactory(EFactory):

    pass
class EStringToStringMapEntry:

    pass
class ecoreDiff_ChangedEStringToStringMapEntry(EStringToStringMapEntry):

    pass
class ecoreDiff_DeletedEStringToStringMapEntry(EStringToStringMapEntry):

    pass
class ecoreDiff_AddedEStringToStringMapEntry(EStringToStringMapEntry):

    pass
class EClass:

    pass
class ecoreDiff_ChangedEClass(EClass):

    pass
class ecoreDiff_DeletedEClass(EClass):

    pass
class ecoreDiff_AddedEClass(EClass):

    pass
class EAnnotation:

    pass
class ecoreDiff_ChangedEAnnotation(EAnnotation):

    pass
class ecoreDiff_DeletedEAnnotation(EAnnotation):

    pass
class ecoreDiff_AddedEAnnotation(EAnnotation):

    pass
class ecoreDiff_DifferenceElement:

    pass
class ecoreDiff_DifferenceModel:

    pass
class DifferenceElement:

    pass
class EDataType:

    pass
class ecoreDiff_ChangedEDataType(EDataType):

    pass
class ecoreDiff_DeletedEDataType(EDataType):

    pass
class ecoreDiff_AddedEDataType(EDataType):

    pass
class ecoreDiff_EEnum(EDataType):

    pass
class EStructuralFeature:

    pass
class ecoreDiff_DeletedEStructuralFeature(EStructuralFeature):

    pass
class ecoreDiff_AddedEStructuralFeature(EStructuralFeature):

    pass
class ecoreDiff_ChangedEStructuralFeature(EStructuralFeature):

    pass
class ecoreDiff_EStructuralFeature_Wildcard:

    pass
class EObject:

    pass
class ecoreDiff_ChangedEObject(EObject):

    pass
class ecoreDiff_DeletedEObject(EObject):

    pass
class ecoreDiff_AddedEObject(EObject):

    pass
class ETypedElement:

    pass
class ecoreDiff_EParameter(ETypedElement):

    pass
class ecoreDiff_DeletedETypedElement(ETypedElement):

    pass
class ecoreDiff_AddedETypedElement(ETypedElement):

    pass
class ecoreDiff_ChangedETypedElement(ETypedElement):

    pass
class ecoreDiff_EClassifier_Wildcard:

    pass
class ENamedElement:

    pass
class ecoreDiff_EPackage(ENamedElement):

    def __init__(self, nsURI: str, nsPrefix: str, ePackage: "ecoreDiff_EFactory" = None, EPackage45: "ecoreDiff_EPackage" = None, eSuperPackage: set["ecoreDiff_EPackage"] = None, EPackage48: "ecoreDiff_EPackage" = None, eSubpackages: "ecoreDiff_EPackage" = None, ePackage50: set["ecoreDiff_EClassifier"] = None, EPackage: "ecoreDiff_EClassifier" = None, EPackage52: "ecoreDiff_EFactory" = None, ecoreDiff_EPackage: "ecoreDiff_ChangedEPackage" = None):
        self.nsURI = nsURI
        self.nsPrefix = nsPrefix
        self.ePackage = ePackage
        self.EPackage45 = EPackage45
        self.eSuperPackage = eSuperPackage if eSuperPackage is not None else set()
        self.EPackage48 = EPackage48
        self.eSubpackages = eSubpackages
        self.ePackage50 = ePackage50 if ePackage50 is not None else set()
        self.EPackage = EPackage
        self.EPackage52 = EPackage52
        self.ecoreDiff_EPackage = ecoreDiff_EPackage
        
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
    def ePackage(self):
        return self.__ePackage

    @ePackage.setter
    def ePackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__ePackage", None)
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
    def EPackage48(self):
        return self.__EPackage48

    @EPackage48.setter
    def EPackage48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__EPackage48", None)
        self.__EPackage48 = value
        
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
    def eSuperPackage(self):
        return self.__eSuperPackage

    @eSuperPackage.setter
    def eSuperPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__eSuperPackage", None)
        self.__eSuperPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EPackage45"):
                    opp_val = getattr(item, "EPackage45", None)
                    
                    if opp_val == self:
                        setattr(item, "EPackage45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EPackage45"):
                    opp_val = getattr(item, "EPackage45", None)
                    
                    setattr(item, "EPackage45", self)
                    

    @property
    def EPackage45(self):
        return self.__EPackage45

    @EPackage45.setter
    def EPackage45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__EPackage45", None)
        self.__EPackage45 = value
        
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
    def ecoreDiff_EPackage(self):
        return self.__ecoreDiff_EPackage

    @ecoreDiff_EPackage.setter
    def ecoreDiff_EPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__ecoreDiff_EPackage", None)
        self.__ecoreDiff_EPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_ChangedEPackage"):
                opp_val = getattr(old_value, "ecoreDiff_ChangedEPackage", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_ChangedEPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedEPackage"):
                opp_val = getattr(value, "ecoreDiff_ChangedEPackage", None)
                setattr(value, "ecoreDiff_ChangedEPackage", self)

    @property
    def eSubpackages(self):
        return self.__eSubpackages

    @eSubpackages.setter
    def eSubpackages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__eSubpackages", None)
        self.__eSubpackages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EPackage48"):
                opp_val = getattr(old_value, "EPackage48", None)
                if opp_val == self:
                    setattr(old_value, "EPackage48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EPackage48"):
                opp_val = getattr(value, "EPackage48", None)
                setattr(value, "EPackage48", self)

    @property
    def ePackage50(self):
        return self.__ePackage50

    @ePackage50.setter
    def ePackage50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__ePackage50", None)
        self.__ePackage50 = value if value is not None else set()
        
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
        old_value = getattr(self, f"_ecoreDiff_EPackage__EPackage", None)
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
    def EPackage52(self):
        return self.__EPackage52

    @EPackage52.setter
    def EPackage52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__EPackage52", None)
        self.__EPackage52 = value
        
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

class ecoreDiff_AddedENamedElement(ENamedElement):

    pass
class ecoreDiff_ETypedElement(ENamedElement):

    def __init__(self, ordered: bool, unique: bool, lowerBound: int, upperBound: int, many: bool, required: bool, ecoreDiff_ETypedElement: "ecoreDiff_EObject" = None, ecoreDiff_ETypedElement88: "ecoreDiff_EGenericType" = None, ecoreDiff_ETypedElement199: "ecoreDiff_ChangedETypedElement" = None):
        self.ordered = ordered
        self.unique = unique
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.many = many
        self.required = required
        self.ecoreDiff_ETypedElement = ecoreDiff_ETypedElement
        self.ecoreDiff_ETypedElement88 = ecoreDiff_ETypedElement88
        self.ecoreDiff_ETypedElement199 = ecoreDiff_ETypedElement199
        
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
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def ecoreDiff_ETypedElement88(self):
        return self.__ecoreDiff_ETypedElement88

    @ecoreDiff_ETypedElement88.setter
    def ecoreDiff_ETypedElement88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_ETypedElement__ecoreDiff_ETypedElement88", None)
        self.__ecoreDiff_ETypedElement88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EGenericType89"):
                opp_val = getattr(old_value, "ecoreDiff_EGenericType89", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EGenericType89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EGenericType89"):
                opp_val = getattr(value, "ecoreDiff_EGenericType89", None)
                setattr(value, "ecoreDiff_EGenericType89", self)

    @property
    def ecoreDiff_ETypedElement(self):
        return self.__ecoreDiff_ETypedElement

    @ecoreDiff_ETypedElement.setter
    def ecoreDiff_ETypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_ETypedElement__ecoreDiff_ETypedElement", None)
        self.__ecoreDiff_ETypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EObject86"):
                opp_val = getattr(old_value, "ecoreDiff_EObject86", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EObject86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EObject86"):
                opp_val = getattr(value, "ecoreDiff_EObject86", None)
                setattr(value, "ecoreDiff_EObject86", self)

    @property
    def ecoreDiff_ETypedElement199(self):
        return self.__ecoreDiff_ETypedElement199

    @ecoreDiff_ETypedElement199.setter
    def ecoreDiff_ETypedElement199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_ETypedElement__ecoreDiff_ETypedElement199", None)
        self.__ecoreDiff_ETypedElement199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_ChangedETypedElement"):
                opp_val = getattr(old_value, "ecoreDiff_ChangedETypedElement", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_ChangedETypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedETypedElement"):
                opp_val = getattr(value, "ecoreDiff_ChangedETypedElement", None)
                setattr(value, "ecoreDiff_ChangedETypedElement", self)

class ecoreDiff_ETypeParameter(ENamedElement):

    pass
class ecoreDiff_EEnumLiteral(ENamedElement):

    def __init__(self, value: int, instance: str, literal: str, EEnumLiteral: "ecoreDiff_EEnum" = None, eLiterals: "ecoreDiff_EEnum" = None, ecoreDiff_EEnumLiteral: "ecoreDiff_ChangedEEnumLiteral" = None):
        self.value = value
        self.instance = instance
        self.literal = literal
        self.EEnumLiteral = EEnumLiteral
        self.eLiterals = eLiterals
        self.ecoreDiff_EEnumLiteral = ecoreDiff_EEnumLiteral
        
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
    def EEnumLiteral(self):
        return self.__EEnumLiteral

    @EEnumLiteral.setter
    def EEnumLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EEnumLiteral__EEnumLiteral", None)
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
        old_value = getattr(self, f"_ecoreDiff_EEnumLiteral__eLiterals", None)
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
    def ecoreDiff_EEnumLiteral(self):
        return self.__ecoreDiff_EEnumLiteral

    @ecoreDiff_EEnumLiteral.setter
    def ecoreDiff_EEnumLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EEnumLiteral__ecoreDiff_EEnumLiteral", None)
        self.__ecoreDiff_EEnumLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_ChangedEEnumLiteral"):
                opp_val = getattr(old_value, "ecoreDiff_ChangedEEnumLiteral", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_ChangedEEnumLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedEEnumLiteral"):
                opp_val = getattr(value, "ecoreDiff_ChangedEEnumLiteral", None)
                setattr(value, "ecoreDiff_ChangedEEnumLiteral", self)

class ecoreDiff_DeletedENamedElement(ENamedElement):

    pass
class ecoreDiff_ChangedENamedElement(ENamedElement):

    pass
class ecoreDiff_EClassifier(ENamedElement):

    def __init__(self, instanceClassName: str, instanceClass: str, defaultValue: str, instanceTypeName: str, EClassifier: "ecoreDiff_EPackage" = None, eClassifiers: "ecoreDiff_EPackage" = None, ecoreDiff_EClassifier: set["ecoreDiff_ETypeParameter"] = None, ecoreDiff_EClassifier64: "ecoreDiff_EGenericType" = None, ecoreDiff_EClassifier73: "ecoreDiff_EGenericType" = None, ecoreDiff_EClassifier80: "ecoreDiff_EOperation" = None, ecoreDiff_EClassifier140: "ecoreDiff_ChangedEClassifier" = None):
        self.instanceClassName = instanceClassName
        self.instanceClass = instanceClass
        self.defaultValue = defaultValue
        self.instanceTypeName = instanceTypeName
        self.EClassifier = EClassifier
        self.eClassifiers = eClassifiers
        self.ecoreDiff_EClassifier = ecoreDiff_EClassifier if ecoreDiff_EClassifier is not None else set()
        self.ecoreDiff_EClassifier64 = ecoreDiff_EClassifier64
        self.ecoreDiff_EClassifier73 = ecoreDiff_EClassifier73
        self.ecoreDiff_EClassifier80 = ecoreDiff_EClassifier80
        self.ecoreDiff_EClassifier140 = ecoreDiff_EClassifier140
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

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
    def ecoreDiff_EClassifier140(self):
        return self.__ecoreDiff_EClassifier140

    @ecoreDiff_EClassifier140.setter
    def ecoreDiff_EClassifier140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClassifier__ecoreDiff_EClassifier140", None)
        self.__ecoreDiff_EClassifier140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_ChangedEClassifier"):
                opp_val = getattr(old_value, "ecoreDiff_ChangedEClassifier", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_ChangedEClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedEClassifier"):
                opp_val = getattr(value, "ecoreDiff_ChangedEClassifier", None)
                setattr(value, "ecoreDiff_ChangedEClassifier", self)

    @property
    def eClassifiers(self):
        return self.__eClassifiers

    @eClassifiers.setter
    def eClassifiers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClassifier__eClassifiers", None)
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
    def ecoreDiff_EClassifier80(self):
        return self.__ecoreDiff_EClassifier80

    @ecoreDiff_EClassifier80.setter
    def ecoreDiff_EClassifier80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClassifier__ecoreDiff_EClassifier80", None)
        self.__ecoreDiff_EClassifier80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EOperation79"):
                opp_val = getattr(old_value, "ecoreDiff_EOperation79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EOperation79"):
                opp_val = getattr(value, "ecoreDiff_EOperation79", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EOperation79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EClassifier(self):
        return self.__ecoreDiff_EClassifier

    @ecoreDiff_EClassifier.setter
    def ecoreDiff_EClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClassifier__ecoreDiff_EClassifier", None)
        self.__ecoreDiff_EClassifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_ETypeParameter"):
                    opp_val = getattr(item, "ecoreDiff_ETypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_ETypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_ETypeParameter"):
                    opp_val = getattr(item, "ecoreDiff_ETypeParameter", None)
                    
                    setattr(item, "ecoreDiff_ETypeParameter", self)
                    

    @property
    def ecoreDiff_EClassifier73(self):
        return self.__ecoreDiff_EClassifier73

    @ecoreDiff_EClassifier73.setter
    def ecoreDiff_EClassifier73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClassifier__ecoreDiff_EClassifier73", None)
        self.__ecoreDiff_EClassifier73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EGenericType72"):
                opp_val = getattr(old_value, "ecoreDiff_EGenericType72", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EGenericType72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EGenericType72"):
                opp_val = getattr(value, "ecoreDiff_EGenericType72", None)
                setattr(value, "ecoreDiff_EGenericType72", self)

    @property
    def EClassifier(self):
        return self.__EClassifier

    @EClassifier.setter
    def EClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClassifier__EClassifier", None)
        self.__EClassifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ePackage50"):
                opp_val = getattr(old_value, "ePackage50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ePackage50"):
                opp_val = getattr(value, "ePackage50", None)
                if opp_val is None:
                    setattr(value, "ePackage50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EClassifier64(self):
        return self.__ecoreDiff_EClassifier64

    @ecoreDiff_EClassifier64.setter
    def ecoreDiff_EClassifier64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClassifier__ecoreDiff_EClassifier64", None)
        self.__ecoreDiff_EClassifier64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EGenericType63"):
                opp_val = getattr(old_value, "ecoreDiff_EGenericType63", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EGenericType63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EGenericType63"):
                opp_val = getattr(value, "ecoreDiff_EGenericType63", None)
                setattr(value, "ecoreDiff_EGenericType63", self)

class ecoreDiff_EGenericType(EObject):

    pass
class ecoreDiff_EReference(EStructuralFeature):

    def __init__(self, containment: bool, container: bool, resolveProxies: bool, ecoreDiff_EReference24: "ecoreDiff_EClass" = None, ecoreDiff_EReference: "ecoreDiff_EClass" = None, ecoreDiff_EReference18: "ecoreDiff_EClass" = None, ecoreDiff_EReference98: "ecoreDiff_EReference" = None, ecoreDiff_EReference96: "ecoreDiff_EReference" = None, ecoreDiff_EReference100: "ecoreDiff_EClass" = None, ecoreDiff_EReference103: set["ecoreDiff_EAttribute"] = None, ecoreDiff_EReference232: "ecoreDiff_ChangedEReference" = None):
        self.containment = containment
        self.container = container
        self.resolveProxies = resolveProxies
        self.ecoreDiff_EReference24 = ecoreDiff_EReference24
        self.ecoreDiff_EReference = ecoreDiff_EReference
        self.ecoreDiff_EReference18 = ecoreDiff_EReference18
        self.ecoreDiff_EReference98 = ecoreDiff_EReference98
        self.ecoreDiff_EReference96 = ecoreDiff_EReference96
        self.ecoreDiff_EReference100 = ecoreDiff_EReference100
        self.ecoreDiff_EReference103 = ecoreDiff_EReference103 if ecoreDiff_EReference103 is not None else set()
        self.ecoreDiff_EReference232 = ecoreDiff_EReference232
        
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
    def ecoreDiff_EReference98(self):
        return self.__ecoreDiff_EReference98

    @ecoreDiff_EReference98.setter
    def ecoreDiff_EReference98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference98", None)
        self.__ecoreDiff_EReference98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EReference96"):
                opp_val = getattr(old_value, "ecoreDiff_EReference96", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EReference96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EReference96"):
                opp_val = getattr(value, "ecoreDiff_EReference96", None)
                setattr(value, "ecoreDiff_EReference96", self)

    @property
    def ecoreDiff_EReference(self):
        return self.__ecoreDiff_EReference

    @ecoreDiff_EReference.setter
    def ecoreDiff_EReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference", None)
        self.__ecoreDiff_EReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EClass15"):
                opp_val = getattr(old_value, "ecoreDiff_EClass15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass15"):
                opp_val = getattr(value, "ecoreDiff_EClass15", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EClass15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EReference96(self):
        return self.__ecoreDiff_EReference96

    @ecoreDiff_EReference96.setter
    def ecoreDiff_EReference96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference96", None)
        self.__ecoreDiff_EReference96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EReference98"):
                opp_val = getattr(old_value, "ecoreDiff_EReference98", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EReference98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EReference98"):
                opp_val = getattr(value, "ecoreDiff_EReference98", None)
                setattr(value, "ecoreDiff_EReference98", self)

    @property
    def ecoreDiff_EReference103(self):
        return self.__ecoreDiff_EReference103

    @ecoreDiff_EReference103.setter
    def ecoreDiff_EReference103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference103", None)
        self.__ecoreDiff_EReference103 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EAttribute104"):
                    opp_val = getattr(item, "ecoreDiff_EAttribute104", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EAttribute104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EAttribute104"):
                    opp_val = getattr(item, "ecoreDiff_EAttribute104", None)
                    
                    setattr(item, "ecoreDiff_EAttribute104", self)
                    

    @property
    def ecoreDiff_EReference24(self):
        return self.__ecoreDiff_EReference24

    @ecoreDiff_EReference24.setter
    def ecoreDiff_EReference24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference24", None)
        self.__ecoreDiff_EReference24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EClass23"):
                opp_val = getattr(old_value, "ecoreDiff_EClass23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass23"):
                opp_val = getattr(value, "ecoreDiff_EClass23", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EClass23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EReference232(self):
        return self.__ecoreDiff_EReference232

    @ecoreDiff_EReference232.setter
    def ecoreDiff_EReference232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference232", None)
        self.__ecoreDiff_EReference232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_ChangedEReference"):
                opp_val = getattr(old_value, "ecoreDiff_ChangedEReference", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_ChangedEReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedEReference"):
                opp_val = getattr(value, "ecoreDiff_ChangedEReference", None)
                setattr(value, "ecoreDiff_ChangedEReference", self)

    @property
    def ecoreDiff_EReference100(self):
        return self.__ecoreDiff_EReference100

    @ecoreDiff_EReference100.setter
    def ecoreDiff_EReference100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference100", None)
        self.__ecoreDiff_EReference100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EClass101"):
                opp_val = getattr(old_value, "ecoreDiff_EClass101", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EClass101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass101"):
                opp_val = getattr(value, "ecoreDiff_EClass101", None)
                setattr(value, "ecoreDiff_EClass101", self)

    @property
    def ecoreDiff_EReference18(self):
        return self.__ecoreDiff_EReference18

    @ecoreDiff_EReference18.setter
    def ecoreDiff_EReference18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference18", None)
        self.__ecoreDiff_EReference18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EClass17"):
                opp_val = getattr(old_value, "ecoreDiff_EClass17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass17"):
                opp_val = getattr(value, "ecoreDiff_EClass17", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EClass17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecoreDiff_EStructuralFeature(ETypedElement):

    def __init__(self, changeable: bool, volatile: bool, transient: bool, defaultValueLiteral: str, defaultValue: str, unsettable: bool, derived: bool, EStructuralFeature: "ecoreDiff_EClass" = None, ecoreDiff_EStructuralFeature: "ecoreDiff_EClass" = None, eStructuralFeatures: "ecoreDiff_EClass" = None, ecoreDiff_EStructuralFeature219: "ecoreDiff_ChangedEStructuralFeature" = None):
        self.changeable = changeable
        self.volatile = volatile
        self.transient = transient
        self.defaultValueLiteral = defaultValueLiteral
        self.defaultValue = defaultValue
        self.unsettable = unsettable
        self.derived = derived
        self.EStructuralFeature = EStructuralFeature
        self.ecoreDiff_EStructuralFeature = ecoreDiff_EStructuralFeature
        self.eStructuralFeatures = eStructuralFeatures
        self.ecoreDiff_EStructuralFeature219 = ecoreDiff_EStructuralFeature219
        
    @property
    def unsettable(self) -> bool:
        return self.__unsettable

    @unsettable.setter
    def unsettable(self, unsettable: bool):
        self.__unsettable = unsettable

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

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
        old_value = getattr(self, f"_ecoreDiff_EStructuralFeature__eStructuralFeatures", None)
        self.__eStructuralFeatures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EClass95"):
                opp_val = getattr(old_value, "EClass95", None)
                if opp_val == self:
                    setattr(old_value, "EClass95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EClass95"):
                opp_val = getattr(value, "EClass95", None)
                setattr(value, "EClass95", self)

    @property
    def ecoreDiff_EStructuralFeature(self):
        return self.__ecoreDiff_EStructuralFeature

    @ecoreDiff_EStructuralFeature.setter
    def ecoreDiff_EStructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EStructuralFeature__ecoreDiff_EStructuralFeature", None)
        self.__ecoreDiff_EStructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EClass28"):
                opp_val = getattr(old_value, "ecoreDiff_EClass28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass28"):
                opp_val = getattr(value, "ecoreDiff_EClass28", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EClass28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EStructuralFeature219(self):
        return self.__ecoreDiff_EStructuralFeature219

    @ecoreDiff_EStructuralFeature219.setter
    def ecoreDiff_EStructuralFeature219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EStructuralFeature__ecoreDiff_EStructuralFeature219", None)
        self.__ecoreDiff_EStructuralFeature219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_ChangedEStructuralFeature"):
                opp_val = getattr(old_value, "ecoreDiff_ChangedEStructuralFeature", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_ChangedEStructuralFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedEStructuralFeature"):
                opp_val = getattr(value, "ecoreDiff_ChangedEStructuralFeature", None)
                setattr(value, "ecoreDiff_ChangedEStructuralFeature", self)

    @property
    def EStructuralFeature(self):
        return self.__EStructuralFeature

    @EStructuralFeature.setter
    def EStructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EStructuralFeature__EStructuralFeature", None)
        self.__EStructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eContainingClass13"):
                opp_val = getattr(old_value, "eContainingClass13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eContainingClass13"):
                opp_val = getattr(value, "eContainingClass13", None)
                if opp_val is None:
                    setattr(value, "eContainingClass13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecoreDiff_EAttribute(EStructuralFeature):

    def __init__(self, iD: bool, ecoreDiff_EAttribute: "ecoreDiff_EClass" = None, ecoreDiff_EAttribute21: "ecoreDiff_EClass" = None, ecoreDiff_EAttribute34: "ecoreDiff_EClass" = None, ecoreDiff_EAttribute93: "ecoreDiff_EDataType" = None, ecoreDiff_EAttribute104: "ecoreDiff_EReference" = None, ecoreDiff_EAttribute212: "ecoreDiff_ChangedEAttribute" = None):
        self.iD = iD
        self.ecoreDiff_EAttribute = ecoreDiff_EAttribute
        self.ecoreDiff_EAttribute21 = ecoreDiff_EAttribute21
        self.ecoreDiff_EAttribute34 = ecoreDiff_EAttribute34
        self.ecoreDiff_EAttribute93 = ecoreDiff_EAttribute93
        self.ecoreDiff_EAttribute104 = ecoreDiff_EAttribute104
        self.ecoreDiff_EAttribute212 = ecoreDiff_EAttribute212
        
    @property
    def iD(self) -> bool:
        return self.__iD

    @iD.setter
    def iD(self, iD: bool):
        self.__iD = iD

    @property
    def ecoreDiff_EAttribute34(self):
        return self.__ecoreDiff_EAttribute34

    @ecoreDiff_EAttribute34.setter
    def ecoreDiff_EAttribute34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAttribute__ecoreDiff_EAttribute34", None)
        self.__ecoreDiff_EAttribute34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EClass33"):
                opp_val = getattr(old_value, "ecoreDiff_EClass33", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EClass33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass33"):
                opp_val = getattr(value, "ecoreDiff_EClass33", None)
                setattr(value, "ecoreDiff_EClass33", self)

    @property
    def ecoreDiff_EAttribute104(self):
        return self.__ecoreDiff_EAttribute104

    @ecoreDiff_EAttribute104.setter
    def ecoreDiff_EAttribute104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAttribute__ecoreDiff_EAttribute104", None)
        self.__ecoreDiff_EAttribute104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EReference103"):
                opp_val = getattr(old_value, "ecoreDiff_EReference103", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EReference103"):
                opp_val = getattr(value, "ecoreDiff_EReference103", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EReference103", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EAttribute212(self):
        return self.__ecoreDiff_EAttribute212

    @ecoreDiff_EAttribute212.setter
    def ecoreDiff_EAttribute212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAttribute__ecoreDiff_EAttribute212", None)
        self.__ecoreDiff_EAttribute212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_ChangedEAttribute"):
                opp_val = getattr(old_value, "ecoreDiff_ChangedEAttribute", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_ChangedEAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedEAttribute"):
                opp_val = getattr(value, "ecoreDiff_ChangedEAttribute", None)
                setattr(value, "ecoreDiff_ChangedEAttribute", self)

    @property
    def ecoreDiff_EAttribute21(self):
        return self.__ecoreDiff_EAttribute21

    @ecoreDiff_EAttribute21.setter
    def ecoreDiff_EAttribute21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAttribute__ecoreDiff_EAttribute21", None)
        self.__ecoreDiff_EAttribute21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EClass20"):
                opp_val = getattr(old_value, "ecoreDiff_EClass20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass20"):
                opp_val = getattr(value, "ecoreDiff_EClass20", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EClass20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EAttribute93(self):
        return self.__ecoreDiff_EAttribute93

    @ecoreDiff_EAttribute93.setter
    def ecoreDiff_EAttribute93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAttribute__ecoreDiff_EAttribute93", None)
        self.__ecoreDiff_EAttribute93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EDataType"):
                opp_val = getattr(old_value, "ecoreDiff_EDataType", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EDataType"):
                opp_val = getattr(value, "ecoreDiff_EDataType", None)
                setattr(value, "ecoreDiff_EDataType", self)

    @property
    def ecoreDiff_EAttribute(self):
        return self.__ecoreDiff_EAttribute

    @ecoreDiff_EAttribute.setter
    def ecoreDiff_EAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAttribute__ecoreDiff_EAttribute", None)
        self.__ecoreDiff_EAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EClass11"):
                opp_val = getattr(old_value, "ecoreDiff_EClass11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass11"):
                opp_val = getattr(value, "ecoreDiff_EClass11", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EClass11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecoreDiff_EOperation(ETypedElement):

    pass
class EClassifier:

    pass
class ecoreDiff_DeletedEClassifier(EClassifier):

    pass
class ecoreDiff_AddedEClassifier(EClassifier):

    pass
class ecoreDiff_ChangedEClassifier(EClassifier):

    pass
class ecoreDiff_EDataType(EClassifier):

    def __init__(self, serializable: bool, ecoreDiff_EDataType: "ecoreDiff_EAttribute" = None, ecoreDiff_EDataType165: "ecoreDiff_ChangedEDataType" = None):
        self.serializable = serializable
        self.ecoreDiff_EDataType = ecoreDiff_EDataType
        self.ecoreDiff_EDataType165 = ecoreDiff_EDataType165
        
    @property
    def serializable(self) -> bool:
        return self.__serializable

    @serializable.setter
    def serializable(self, serializable: bool):
        self.__serializable = serializable

    @property
    def ecoreDiff_EDataType(self):
        return self.__ecoreDiff_EDataType

    @ecoreDiff_EDataType.setter
    def ecoreDiff_EDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EDataType__ecoreDiff_EDataType", None)
        self.__ecoreDiff_EDataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EAttribute93"):
                opp_val = getattr(old_value, "ecoreDiff_EAttribute93", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EAttribute93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EAttribute93"):
                opp_val = getattr(value, "ecoreDiff_EAttribute93", None)
                setattr(value, "ecoreDiff_EAttribute93", self)

    @property
    def ecoreDiff_EDataType165(self):
        return self.__ecoreDiff_EDataType165

    @ecoreDiff_EDataType165.setter
    def ecoreDiff_EDataType165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EDataType__ecoreDiff_EDataType165", None)
        self.__ecoreDiff_EDataType165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_ChangedEDataType"):
                opp_val = getattr(old_value, "ecoreDiff_ChangedEDataType", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_ChangedEDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedEDataType"):
                opp_val = getattr(value, "ecoreDiff_ChangedEDataType", None)
                setattr(value, "ecoreDiff_ChangedEDataType", self)

class ecoreDiff_EClass(EClassifier):

    def __init__(self, abstract: bool, interface: bool, ecoreDiff_EClass7: set["ecoreDiff_EClass"] = None, ecoreDiff_EClass: "ecoreDiff_EClass" = None, ecoreDiff_EClass23: set["ecoreDiff_EReference"] = None, ecoreDiff_EClass26: set["ecoreDiff_EOperation"] = None, eContainingClass: set["ecoreDiff_EOperation"] = None, ecoreDiff_EClass11: set["ecoreDiff_EAttribute"] = None, eContainingClass13: set["ecoreDiff_EStructuralFeature"] = None, ecoreDiff_EClass15: set["ecoreDiff_EReference"] = None, ecoreDiff_EClass17: set["ecoreDiff_EReference"] = None, ecoreDiff_EClass20: set["ecoreDiff_EAttribute"] = None, ecoreDiff_EClass28: set["ecoreDiff_EStructuralFeature"] = None, ecoreDiff_EClass31: "ecoreDiff_EClass" = None, ecoreDiff_EClass29: set["ecoreDiff_EClass"] = None, ecoreDiff_EClass33: "ecoreDiff_EAttribute" = None, ecoreDiff_EClass36: set["ecoreDiff_EGenericType"] = None, ecoreDiff_EClass38: set["ecoreDiff_EGenericType"] = None, EClass: "ecoreDiff_EOperation" = None, ecoreDiff_EClass101: "ecoreDiff_EReference" = None, EClass95: "ecoreDiff_EStructuralFeature" = None, ecoreDiff_EClass133: "ecoreDiff_ChangedEClass" = None):
        self.abstract = abstract
        self.interface = interface
        self.ecoreDiff_EClass7 = ecoreDiff_EClass7 if ecoreDiff_EClass7 is not None else set()
        self.ecoreDiff_EClass = ecoreDiff_EClass
        self.ecoreDiff_EClass23 = ecoreDiff_EClass23 if ecoreDiff_EClass23 is not None else set()
        self.ecoreDiff_EClass26 = ecoreDiff_EClass26 if ecoreDiff_EClass26 is not None else set()
        self.eContainingClass = eContainingClass if eContainingClass is not None else set()
        self.ecoreDiff_EClass11 = ecoreDiff_EClass11 if ecoreDiff_EClass11 is not None else set()
        self.eContainingClass13 = eContainingClass13 if eContainingClass13 is not None else set()
        self.ecoreDiff_EClass15 = ecoreDiff_EClass15 if ecoreDiff_EClass15 is not None else set()
        self.ecoreDiff_EClass17 = ecoreDiff_EClass17 if ecoreDiff_EClass17 is not None else set()
        self.ecoreDiff_EClass20 = ecoreDiff_EClass20 if ecoreDiff_EClass20 is not None else set()
        self.ecoreDiff_EClass28 = ecoreDiff_EClass28 if ecoreDiff_EClass28 is not None else set()
        self.ecoreDiff_EClass31 = ecoreDiff_EClass31
        self.ecoreDiff_EClass29 = ecoreDiff_EClass29 if ecoreDiff_EClass29 is not None else set()
        self.ecoreDiff_EClass33 = ecoreDiff_EClass33
        self.ecoreDiff_EClass36 = ecoreDiff_EClass36 if ecoreDiff_EClass36 is not None else set()
        self.ecoreDiff_EClass38 = ecoreDiff_EClass38 if ecoreDiff_EClass38 is not None else set()
        self.EClass = EClass
        self.ecoreDiff_EClass101 = ecoreDiff_EClass101
        self.EClass95 = EClass95
        self.ecoreDiff_EClass133 = ecoreDiff_EClass133
        
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
    def ecoreDiff_EClass20(self):
        return self.__ecoreDiff_EClass20

    @ecoreDiff_EClass20.setter
    def ecoreDiff_EClass20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass20", None)
        self.__ecoreDiff_EClass20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EAttribute21"):
                    opp_val = getattr(item, "ecoreDiff_EAttribute21", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EAttribute21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EAttribute21"):
                    opp_val = getattr(item, "ecoreDiff_EAttribute21", None)
                    
                    setattr(item, "ecoreDiff_EAttribute21", self)
                    

    @property
    def ecoreDiff_EClass17(self):
        return self.__ecoreDiff_EClass17

    @ecoreDiff_EClass17.setter
    def ecoreDiff_EClass17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass17", None)
        self.__ecoreDiff_EClass17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EReference18"):
                    opp_val = getattr(item, "ecoreDiff_EReference18", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EReference18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EReference18"):
                    opp_val = getattr(item, "ecoreDiff_EReference18", None)
                    
                    setattr(item, "ecoreDiff_EReference18", self)
                    

    @property
    def ecoreDiff_EClass23(self):
        return self.__ecoreDiff_EClass23

    @ecoreDiff_EClass23.setter
    def ecoreDiff_EClass23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass23", None)
        self.__ecoreDiff_EClass23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EReference24"):
                    opp_val = getattr(item, "ecoreDiff_EReference24", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EReference24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EReference24"):
                    opp_val = getattr(item, "ecoreDiff_EReference24", None)
                    
                    setattr(item, "ecoreDiff_EReference24", self)
                    

    @property
    def ecoreDiff_EClass29(self):
        return self.__ecoreDiff_EClass29

    @ecoreDiff_EClass29.setter
    def ecoreDiff_EClass29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass29", None)
        self.__ecoreDiff_EClass29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EClass31"):
                    opp_val = getattr(item, "ecoreDiff_EClass31", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EClass31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EClass31"):
                    opp_val = getattr(item, "ecoreDiff_EClass31", None)
                    
                    setattr(item, "ecoreDiff_EClass31", self)
                    

    @property
    def ecoreDiff_EClass26(self):
        return self.__ecoreDiff_EClass26

    @ecoreDiff_EClass26.setter
    def ecoreDiff_EClass26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass26", None)
        self.__ecoreDiff_EClass26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EOperation"):
                    opp_val = getattr(item, "ecoreDiff_EOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EOperation"):
                    opp_val = getattr(item, "ecoreDiff_EOperation", None)
                    
                    setattr(item, "ecoreDiff_EOperation", self)
                    

    @property
    def EClass(self):
        return self.__EClass

    @EClass.setter
    def EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__EClass", None)
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
    def eContainingClass13(self):
        return self.__eContainingClass13

    @eContainingClass13.setter
    def eContainingClass13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__eContainingClass13", None)
        self.__eContainingClass13 = value if value is not None else set()
        
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
    def EClass95(self):
        return self.__EClass95

    @EClass95.setter
    def EClass95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__EClass95", None)
        self.__EClass95 = value
        
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
    def ecoreDiff_EClass36(self):
        return self.__ecoreDiff_EClass36

    @ecoreDiff_EClass36.setter
    def ecoreDiff_EClass36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass36", None)
        self.__ecoreDiff_EClass36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EGenericType"):
                    opp_val = getattr(item, "ecoreDiff_EGenericType", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EGenericType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EGenericType"):
                    opp_val = getattr(item, "ecoreDiff_EGenericType", None)
                    
                    setattr(item, "ecoreDiff_EGenericType", self)
                    

    @property
    def ecoreDiff_EClass(self):
        return self.__ecoreDiff_EClass

    @ecoreDiff_EClass.setter
    def ecoreDiff_EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass", None)
        self.__ecoreDiff_EClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EClass7"):
                opp_val = getattr(old_value, "ecoreDiff_EClass7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass7"):
                opp_val = getattr(value, "ecoreDiff_EClass7", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EClass7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EClass101(self):
        return self.__ecoreDiff_EClass101

    @ecoreDiff_EClass101.setter
    def ecoreDiff_EClass101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass101", None)
        self.__ecoreDiff_EClass101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EReference100"):
                opp_val = getattr(old_value, "ecoreDiff_EReference100", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EReference100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EReference100"):
                opp_val = getattr(value, "ecoreDiff_EReference100", None)
                setattr(value, "ecoreDiff_EReference100", self)

    @property
    def ecoreDiff_EClass28(self):
        return self.__ecoreDiff_EClass28

    @ecoreDiff_EClass28.setter
    def ecoreDiff_EClass28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass28", None)
        self.__ecoreDiff_EClass28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EStructuralFeature"):
                    opp_val = getattr(item, "ecoreDiff_EStructuralFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EStructuralFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EStructuralFeature"):
                    opp_val = getattr(item, "ecoreDiff_EStructuralFeature", None)
                    
                    setattr(item, "ecoreDiff_EStructuralFeature", self)
                    

    @property
    def ecoreDiff_EClass33(self):
        return self.__ecoreDiff_EClass33

    @ecoreDiff_EClass33.setter
    def ecoreDiff_EClass33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass33", None)
        self.__ecoreDiff_EClass33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EAttribute34"):
                opp_val = getattr(old_value, "ecoreDiff_EAttribute34", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EAttribute34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EAttribute34"):
                opp_val = getattr(value, "ecoreDiff_EAttribute34", None)
                setattr(value, "ecoreDiff_EAttribute34", self)

    @property
    def eContainingClass(self):
        return self.__eContainingClass

    @eContainingClass.setter
    def eContainingClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__eContainingClass", None)
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
    def ecoreDiff_EClass31(self):
        return self.__ecoreDiff_EClass31

    @ecoreDiff_EClass31.setter
    def ecoreDiff_EClass31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass31", None)
        self.__ecoreDiff_EClass31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EClass29"):
                opp_val = getattr(old_value, "ecoreDiff_EClass29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass29"):
                opp_val = getattr(value, "ecoreDiff_EClass29", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EClass29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EClass11(self):
        return self.__ecoreDiff_EClass11

    @ecoreDiff_EClass11.setter
    def ecoreDiff_EClass11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass11", None)
        self.__ecoreDiff_EClass11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EAttribute"):
                    opp_val = getattr(item, "ecoreDiff_EAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EAttribute"):
                    opp_val = getattr(item, "ecoreDiff_EAttribute", None)
                    
                    setattr(item, "ecoreDiff_EAttribute", self)
                    

    @property
    def ecoreDiff_EClass133(self):
        return self.__ecoreDiff_EClass133

    @ecoreDiff_EClass133.setter
    def ecoreDiff_EClass133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass133", None)
        self.__ecoreDiff_EClass133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_ChangedEClass"):
                opp_val = getattr(old_value, "ecoreDiff_ChangedEClass", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_ChangedEClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedEClass"):
                opp_val = getattr(value, "ecoreDiff_ChangedEClass", None)
                setattr(value, "ecoreDiff_ChangedEClass", self)

    @property
    def ecoreDiff_EClass38(self):
        return self.__ecoreDiff_EClass38

    @ecoreDiff_EClass38.setter
    def ecoreDiff_EClass38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass38", None)
        self.__ecoreDiff_EClass38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EGenericType39"):
                    opp_val = getattr(item, "ecoreDiff_EGenericType39", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EGenericType39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EGenericType39"):
                    opp_val = getattr(item, "ecoreDiff_EGenericType39", None)
                    
                    setattr(item, "ecoreDiff_EGenericType39", self)
                    

    @property
    def ecoreDiff_EClass7(self):
        return self.__ecoreDiff_EClass7

    @ecoreDiff_EClass7.setter
    def ecoreDiff_EClass7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass7", None)
        self.__ecoreDiff_EClass7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EClass"):
                    opp_val = getattr(item, "ecoreDiff_EClass", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EClass"):
                    opp_val = getattr(item, "ecoreDiff_EClass", None)
                    
                    setattr(item, "ecoreDiff_EClass", self)
                    

    @property
    def ecoreDiff_EClass15(self):
        return self.__ecoreDiff_EClass15

    @ecoreDiff_EClass15.setter
    def ecoreDiff_EClass15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass15", None)
        self.__ecoreDiff_EClass15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EReference"):
                    opp_val = getattr(item, "ecoreDiff_EReference", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EReference"):
                    opp_val = getattr(item, "ecoreDiff_EReference", None)
                    
                    setattr(item, "ecoreDiff_EReference", self)
                    

class ecoreDiff_EObject:

    pass
class ecoreDiff_EModelElement(DifferenceElement, EObject):

    pass
class ecoreDiff_EStringToStringMapEntry:

    def __init__(self, key: str, value: str, ecoreDiff_EStringToStringMapEntry: "ecoreDiff_EAnnotation" = None, ecoreDiff_EStringToStringMapEntry119: "ecoreDiff_ChangedEStringToStringMapEntry" = None):
        self.key = key
        self.value = value
        self.ecoreDiff_EStringToStringMapEntry = ecoreDiff_EStringToStringMapEntry
        self.ecoreDiff_EStringToStringMapEntry119 = ecoreDiff_EStringToStringMapEntry119
        
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
    def ecoreDiff_EStringToStringMapEntry(self):
        return self.__ecoreDiff_EStringToStringMapEntry

    @ecoreDiff_EStringToStringMapEntry.setter
    def ecoreDiff_EStringToStringMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EStringToStringMapEntry__ecoreDiff_EStringToStringMapEntry", None)
        self.__ecoreDiff_EStringToStringMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EAnnotation"):
                opp_val = getattr(old_value, "ecoreDiff_EAnnotation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EAnnotation"):
                opp_val = getattr(value, "ecoreDiff_EAnnotation", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EAnnotation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EStringToStringMapEntry119(self):
        return self.__ecoreDiff_EStringToStringMapEntry119

    @ecoreDiff_EStringToStringMapEntry119.setter
    def ecoreDiff_EStringToStringMapEntry119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EStringToStringMapEntry__ecoreDiff_EStringToStringMapEntry119", None)
        self.__ecoreDiff_EStringToStringMapEntry119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_ChangedEStringToStringMapEntry"):
                opp_val = getattr(old_value, "ecoreDiff_ChangedEStringToStringMapEntry", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_ChangedEStringToStringMapEntry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedEStringToStringMapEntry"):
                opp_val = getattr(value, "ecoreDiff_ChangedEStringToStringMapEntry", None)
                setattr(value, "ecoreDiff_ChangedEStringToStringMapEntry", self)

class EModelElement:

    pass
class ecoreDiff_DeletedEModelElement(EModelElement):

    pass
class ecoreDiff_EFactory(EModelElement):

    pass
class ecoreDiff_ChangedEModelElement(EModelElement):

    pass
class ecoreDiff_AddedEModelElement(EModelElement):

    pass
class ecoreDiff_ENamedElement(EModelElement):

    def __init__(self, name: str, ecoreDiff_ENamedElement: "ecoreDiff_ChangedENamedElement" = None):
        self.name = name
        self.ecoreDiff_ENamedElement = ecoreDiff_ENamedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ecoreDiff_ENamedElement(self):
        return self.__ecoreDiff_ENamedElement

    @ecoreDiff_ENamedElement.setter
    def ecoreDiff_ENamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_ENamedElement__ecoreDiff_ENamedElement", None)
        self.__ecoreDiff_ENamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_ChangedENamedElement"):
                opp_val = getattr(old_value, "ecoreDiff_ChangedENamedElement", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_ChangedENamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedENamedElement"):
                opp_val = getattr(value, "ecoreDiff_ChangedENamedElement", None)
                setattr(value, "ecoreDiff_ChangedENamedElement", self)

class ecoreDiff_EAnnotation(EModelElement):

    def __init__(self, source: str, ecoreDiff_EAnnotation: set["ecoreDiff_EStringToStringMapEntry"] = None, eAnnotations: "ecoreDiff_EModelElement" = None, ecoreDiff_EAnnotation3: set["ecoreDiff_EObject"] = None, ecoreDiff_EAnnotation5: set["ecoreDiff_EObject"] = None, EAnnotation: "ecoreDiff_EModelElement" = None, ecoreDiff_EAnnotation112: "ecoreDiff_ChangedEAnnotation" = None):
        self.source = source
        self.ecoreDiff_EAnnotation = ecoreDiff_EAnnotation if ecoreDiff_EAnnotation is not None else set()
        self.eAnnotations = eAnnotations
        self.ecoreDiff_EAnnotation3 = ecoreDiff_EAnnotation3 if ecoreDiff_EAnnotation3 is not None else set()
        self.ecoreDiff_EAnnotation5 = ecoreDiff_EAnnotation5 if ecoreDiff_EAnnotation5 is not None else set()
        self.EAnnotation = EAnnotation
        self.ecoreDiff_EAnnotation112 = ecoreDiff_EAnnotation112
        
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
        old_value = getattr(self, f"_ecoreDiff_EAnnotation__EAnnotation", None)
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
    def ecoreDiff_EAnnotation3(self):
        return self.__ecoreDiff_EAnnotation3

    @ecoreDiff_EAnnotation3.setter
    def ecoreDiff_EAnnotation3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAnnotation__ecoreDiff_EAnnotation3", None)
        self.__ecoreDiff_EAnnotation3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EObject"):
                    opp_val = getattr(item, "ecoreDiff_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EObject"):
                    opp_val = getattr(item, "ecoreDiff_EObject", None)
                    
                    setattr(item, "ecoreDiff_EObject", self)
                    

    @property
    def ecoreDiff_EAnnotation112(self):
        return self.__ecoreDiff_EAnnotation112

    @ecoreDiff_EAnnotation112.setter
    def ecoreDiff_EAnnotation112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAnnotation__ecoreDiff_EAnnotation112", None)
        self.__ecoreDiff_EAnnotation112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_ChangedEAnnotation"):
                opp_val = getattr(old_value, "ecoreDiff_ChangedEAnnotation", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_ChangedEAnnotation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedEAnnotation"):
                opp_val = getattr(value, "ecoreDiff_ChangedEAnnotation", None)
                setattr(value, "ecoreDiff_ChangedEAnnotation", self)

    @property
    def ecoreDiff_EAnnotation(self):
        return self.__ecoreDiff_EAnnotation

    @ecoreDiff_EAnnotation.setter
    def ecoreDiff_EAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAnnotation__ecoreDiff_EAnnotation", None)
        self.__ecoreDiff_EAnnotation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EStringToStringMapEntry"):
                    opp_val = getattr(item, "ecoreDiff_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EStringToStringMapEntry"):
                    opp_val = getattr(item, "ecoreDiff_EStringToStringMapEntry", None)
                    
                    setattr(item, "ecoreDiff_EStringToStringMapEntry", self)
                    

    @property
    def ecoreDiff_EAnnotation5(self):
        return self.__ecoreDiff_EAnnotation5

    @ecoreDiff_EAnnotation5.setter
    def ecoreDiff_EAnnotation5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAnnotation__ecoreDiff_EAnnotation5", None)
        self.__ecoreDiff_EAnnotation5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EObject6"):
                    opp_val = getattr(item, "ecoreDiff_EObject6", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EObject6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EObject6"):
                    opp_val = getattr(item, "ecoreDiff_EObject6", None)
                    
                    setattr(item, "ecoreDiff_EObject6", self)
                    

    @property
    def eAnnotations(self):
        return self.__eAnnotations

    @eAnnotations.setter
    def eAnnotations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAnnotation__eAnnotations", None)
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
