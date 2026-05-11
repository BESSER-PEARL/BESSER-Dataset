from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class EReference:

    pass
class ecoreDiff_DeletedEReference(EReference):

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
class EAttribute:

    pass
class ecoreDiff_DeletedEAttribute(EAttribute):

    pass
class ecoreDiff_ChangedEAttribute(EAttribute):

    pass
class ecoreDiff_AddedEAttribute(EAttribute):

    pass
class EEnumLiteral:

    pass
class ecoreDiff_DeletedEEnumLiteral(EEnumLiteral):

    pass
class ecoreDiff_ChangedEEnumLiteral(EEnumLiteral):

    pass
class ecoreDiff_AddedEEnumLiteral(EEnumLiteral):

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
class EOperation:

    pass
class ecoreDiff_ChangedEOperation(EOperation):

    pass
class ecoreDiff_DeletedEOperation(EOperation):

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
class EParameter:

    pass
class ecoreDiff_DeletedEParameter(EParameter):

    pass
class ecoreDiff_ChangedEParameter(EParameter):

    pass
class ecoreDiff_AddedEParameter(EParameter):

    pass
class EFactory:

    pass
class ecoreDiff_ChangedEFactory(EFactory):

    pass
class ecoreDiff_DeletedEFactory(EFactory):

    pass
class ecoreDiff_AddedEFactory(EFactory):

    pass
class EPackage:

    pass
class ecoreDiff_ChangedEPackage(EPackage):

    pass
class ecoreDiff_DeletedEPackage(EPackage):

    pass
class ecoreDiff_AddedEPackage(EPackage):

    pass
class EGenericType:

    pass
class ecoreDiff_DeletedEGenericType(EGenericType):

    pass
class ecoreDiff_ChangedEGenericType(EGenericType):

    pass
class ecoreDiff_AddedEGenericType(EGenericType):

    pass
class ETypeParameter:

    pass
class ecoreDiff_DeletedETypeParameter(ETypeParameter):

    pass
class ecoreDiff_ChangedETypeParameter(ETypeParameter):

    pass
class ecoreDiff_AddedETypeParameter(ETypeParameter):

    pass
class EClass:

    pass
class ecoreDiff_DeletedEClass(EClass):

    pass
class ecoreDiff_ChangedEClass(EClass):

    pass
class ecoreDiff_AddedEClass(EClass):

    pass
class EStringToStringMapEntry:

    pass
class ecoreDiff_ChangedEStringToStringMapEntry(EStringToStringMapEntry):

    pass
class ecoreDiff_DeletedEStringToStringMapEntry(EStringToStringMapEntry):

    pass
class ecoreDiff_AddedEStringToStringMapEntry(EStringToStringMapEntry):

    pass
class EAnnotation:

    pass
class ecoreDiff_DeletedEAnnotation(EAnnotation):

    pass
class ecoreDiff_ChangedEAnnotation(EAnnotation):

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
class ecoreDiff_DeletedEDataType(EDataType):

    pass
class ecoreDiff_AddedEDataType(EDataType):

    pass
class ecoreDiff_ChangedEDataType(EDataType):

    pass
class ecoreDiff_EEnum(EDataType):

    pass
class ecoreDiff_EStructuralFeature_Wildcard:

    pass
class EStructuralFeature:

    pass
class ecoreDiff_ChangedEStructuralFeature(EStructuralFeature):

    pass
class ecoreDiff_AddedEStructuralFeature(EStructuralFeature):

    pass
class ecoreDiff_DeletedEStructuralFeature(EStructuralFeature):

    pass
class EObject:

    pass
class ecoreDiff_AddedEObject(EObject):

    pass
class ecoreDiff_ChangedEObject(EObject):

    pass
class ecoreDiff_DeletedEObject(EObject):

    pass
class ETypedElement:

    pass
class ecoreDiff_AddedETypedElement(ETypedElement):

    pass
class ecoreDiff_EParameter(ETypedElement):

    pass
class ecoreDiff_ChangedETypedElement(ETypedElement):

    pass
class ecoreDiff_DeletedETypedElement(ETypedElement):

    pass
class ecoreDiff_EClassifier_Wildcard:

    pass
class ENamedElement:

    pass
class ecoreDiff_EEnumLiteral(ENamedElement):

    def __init__(self, literal: str, value: int, instance: str, ecoreDiff_EEnumLiteral: "ecoreDiff_ChangedEEnumLiteral" = None, eLiterals: "ecoreDiff_EEnum" = None, EEnumLiteral: "ecoreDiff_EEnum" = None):
        self.literal = literal
        self.value = value
        self.instance = instance
        self.ecoreDiff_EEnumLiteral = ecoreDiff_EEnumLiteral
        self.eLiterals = eLiterals
        self.EEnumLiteral = EEnumLiteral
        
        pass
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
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedEEnumLiteral"):
                opp_val = getattr(value, "ecoreDiff_ChangedEEnumLiteral", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_ChangedEEnumLiteral", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class ecoreDiff_DeletedENamedElement(ENamedElement):

    pass
class ecoreDiff_AddedENamedElement(ENamedElement):

    pass
class ecoreDiff_ETypeParameter(ENamedElement):

    pass
class ecoreDiff_EPackage(ENamedElement):

    def __init__(self, nsURI: str, nsPrefix: str, ePackage: "ecoreDiff_EFactory" = None, EPackage45: "ecoreDiff_EPackage" = None, eSuperPackage: set["ecoreDiff_EPackage"] = None, EPackage48: "ecoreDiff_EPackage" = None, eSubpackages: "ecoreDiff_EPackage" = None, EPackage: "ecoreDiff_EClassifier" = None, ePackage50: set["ecoreDiff_EClassifier"] = None, EPackage52: "ecoreDiff_EFactory" = None, ecoreDiff_EPackage: "ecoreDiff_ChangedEPackage" = None):
        self.nsURI = nsURI
        self.nsPrefix = nsPrefix
        self.ePackage = ePackage
        self.EPackage45 = EPackage45
        self.eSuperPackage = eSuperPackage if eSuperPackage is not None else set()
        self.EPackage48 = EPackage48
        self.eSubpackages = eSubpackages
        self.EPackage = EPackage
        self.ePackage50 = ePackage50 if ePackage50 is not None else set()
        self.EPackage52 = EPackage52
        self.ecoreDiff_EPackage = ecoreDiff_EPackage
        
        pass
    @property
    def nsURI(self):
        return self.__nsURI

    @nsURI.setter
    def nsURI(self, nsURI: str):
        self.__nsURI = nsURI


    @property
    def nsPrefix(self):
        return self.__nsPrefix

    @nsPrefix.setter
    def nsPrefix(self, nsPrefix: str):
        self.__nsPrefix = nsPrefix


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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedEPackage"):
                opp_val = getattr(value, "ecoreDiff_ChangedEPackage", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_ChangedEPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecoreDiff_ChangedENamedElement(ENamedElement):

    pass
class ecoreDiff_ETypedElement(ENamedElement):

    def __init__(self, ordered: bool, unique: bool, lowerBound: int, upperBound: int, many: bool, required: str, ecoreDiff_ETypedElement129: "ecoreDiff_ChangedETypedElement" = None, ecoreDiff_ETypedElement: "ecoreDiff_EGenericType" = None):
        self.ordered = ordered
        self.unique = unique
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.many = many
        self.required = required
        self.ecoreDiff_ETypedElement129 = ecoreDiff_ETypedElement129
        self.ecoreDiff_ETypedElement = ecoreDiff_ETypedElement
        
        pass
    @property
    def many(self):
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many


    @property
    def ordered(self):
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered


    @property
    def lowerBound(self):
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound


    @property
    def required(self):
        return self.__required

    @required.setter
    def required(self, required: str):
        self.__required = required


    @property
    def upperBound(self):
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound


    @property
    def unique(self):
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique


    @property
    def ecoreDiff_ETypedElement129(self):
        return self.__ecoreDiff_ETypedElement129

    @ecoreDiff_ETypedElement129.setter
    def ecoreDiff_ETypedElement129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_ETypedElement__ecoreDiff_ETypedElement129", None)
        self.__ecoreDiff_ETypedElement129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_ChangedETypedElement"):
                opp_val = getattr(old_value, "ecoreDiff_ChangedETypedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedETypedElement"):
                opp_val = getattr(value, "ecoreDiff_ChangedETypedElement", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_ChangedETypedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "ecoreDiff_EGenericType86"):
                opp_val = getattr(old_value, "ecoreDiff_EGenericType86", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EGenericType86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EGenericType86"):
                opp_val = getattr(value, "ecoreDiff_EGenericType86", None)
                setattr(value, "ecoreDiff_EGenericType86", self)

class ecoreDiff_EClassifier(ENamedElement):

    def __init__(self, instanceClassName: str, instanceClass: str, defaultValue: str, instanceTypeName: str, eClassifiers: "ecoreDiff_EPackage" = None, ecoreDiff_EClassifier: set["ecoreDiff_ETypeParameter"] = None, ecoreDiff_EClassifier80: "ecoreDiff_EOperation" = None, EClassifier: "ecoreDiff_EPackage" = None, ecoreDiff_EClassifier64: "ecoreDiff_EGenericType" = None, ecoreDiff_EClassifier73: "ecoreDiff_EGenericType" = None, ecoreDiff_EClassifier115: "ecoreDiff_ChangedEClassifier" = None):
        self.instanceClassName = instanceClassName
        self.instanceClass = instanceClass
        self.defaultValue = defaultValue
        self.instanceTypeName = instanceTypeName
        self.eClassifiers = eClassifiers
        self.ecoreDiff_EClassifier = ecoreDiff_EClassifier if ecoreDiff_EClassifier is not None else set()
        self.ecoreDiff_EClassifier80 = ecoreDiff_EClassifier80
        self.EClassifier = EClassifier
        self.ecoreDiff_EClassifier64 = ecoreDiff_EClassifier64
        self.ecoreDiff_EClassifier73 = ecoreDiff_EClassifier73
        self.ecoreDiff_EClassifier115 = ecoreDiff_EClassifier115
        
        pass
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
    def instanceClass(self):
        return self.__instanceClass

    @instanceClass.setter
    def instanceClass(self, instanceClass: str):
        self.__instanceClass = instanceClass


    @property
    def ecoreDiff_EClassifier115(self):
        return self.__ecoreDiff_EClassifier115

    @ecoreDiff_EClassifier115.setter
    def ecoreDiff_EClassifier115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClassifier__ecoreDiff_EClassifier115", None)
        self.__ecoreDiff_EClassifier115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_ChangedEClassifier"):
                opp_val = getattr(old_value, "ecoreDiff_ChangedEClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedEClassifier"):
                opp_val = getattr(value, "ecoreDiff_ChangedEClassifier", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_ChangedEClassifier", set([self]))
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

class ecoreDiff_EGenericType(EObject):

    pass
class ecoreDiff_EReference(EStructuralFeature):

    def __init__(self, containment: bool, container: bool, resolveProxies: bool, ecoreDiff_EReference: "ecoreDiff_EClass" = None, ecoreDiff_EReference18: "ecoreDiff_EClass" = None, ecoreDiff_EReference24: "ecoreDiff_EClass" = None, ecoreDiff_EReference137: "ecoreDiff_ChangedEReference" = None, ecoreDiff_EReference95: "ecoreDiff_EReference" = None, ecoreDiff_EReference93: "ecoreDiff_EReference" = None, ecoreDiff_EReference97: "ecoreDiff_EClass" = None, ecoreDiff_EReference100: set["ecoreDiff_EAttribute"] = None):
        self.containment = containment
        self.container = container
        self.resolveProxies = resolveProxies
        self.ecoreDiff_EReference = ecoreDiff_EReference
        self.ecoreDiff_EReference18 = ecoreDiff_EReference18
        self.ecoreDiff_EReference24 = ecoreDiff_EReference24
        self.ecoreDiff_EReference137 = ecoreDiff_EReference137
        self.ecoreDiff_EReference95 = ecoreDiff_EReference95
        self.ecoreDiff_EReference93 = ecoreDiff_EReference93
        self.ecoreDiff_EReference97 = ecoreDiff_EReference97
        self.ecoreDiff_EReference100 = ecoreDiff_EReference100 if ecoreDiff_EReference100 is not None else set()
        
        pass
    @property
    def resolveProxies(self):
        return self.__resolveProxies

    @resolveProxies.setter
    def resolveProxies(self, resolveProxies: bool):
        self.__resolveProxies = resolveProxies


    @property
    def containment(self):
        return self.__containment

    @containment.setter
    def containment(self, containment: bool):
        self.__containment = containment


    @property
    def container(self):
        return self.__container

    @container.setter
    def container(self, container: bool):
        self.__container = container


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
    def ecoreDiff_EReference97(self):
        return self.__ecoreDiff_EReference97

    @ecoreDiff_EReference97.setter
    def ecoreDiff_EReference97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference97", None)
        self.__ecoreDiff_EReference97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EClass98"):
                opp_val = getattr(old_value, "ecoreDiff_EClass98", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EClass98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass98"):
                opp_val = getattr(value, "ecoreDiff_EClass98", None)
                setattr(value, "ecoreDiff_EClass98", self)

    @property
    def ecoreDiff_EReference95(self):
        return self.__ecoreDiff_EReference95

    @ecoreDiff_EReference95.setter
    def ecoreDiff_EReference95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference95", None)
        self.__ecoreDiff_EReference95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EReference93"):
                opp_val = getattr(old_value, "ecoreDiff_EReference93", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EReference93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EReference93"):
                opp_val = getattr(value, "ecoreDiff_EReference93", None)
                setattr(value, "ecoreDiff_EReference93", self)

    @property
    def ecoreDiff_EReference100(self):
        return self.__ecoreDiff_EReference100

    @ecoreDiff_EReference100.setter
    def ecoreDiff_EReference100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference100", None)
        self.__ecoreDiff_EReference100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EAttribute101"):
                    opp_val = getattr(item, "ecoreDiff_EAttribute101", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EAttribute101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EAttribute101"):
                    opp_val = getattr(item, "ecoreDiff_EAttribute101", None)
                    
                    setattr(item, "ecoreDiff_EAttribute101", self)
                    

    @property
    def ecoreDiff_EReference93(self):
        return self.__ecoreDiff_EReference93

    @ecoreDiff_EReference93.setter
    def ecoreDiff_EReference93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference93", None)
        self.__ecoreDiff_EReference93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EReference95"):
                opp_val = getattr(old_value, "ecoreDiff_EReference95", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EReference95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EReference95"):
                opp_val = getattr(value, "ecoreDiff_EReference95", None)
                setattr(value, "ecoreDiff_EReference95", self)

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
    def ecoreDiff_EReference137(self):
        return self.__ecoreDiff_EReference137

    @ecoreDiff_EReference137.setter
    def ecoreDiff_EReference137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference137", None)
        self.__ecoreDiff_EReference137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_ChangedEReference"):
                opp_val = getattr(old_value, "ecoreDiff_ChangedEReference", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedEReference"):
                opp_val = getattr(value, "ecoreDiff_ChangedEReference", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_ChangedEReference", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecoreDiff_EStructuralFeature(ETypedElement):

    def __init__(self, changeable: bool, volatile: bool, transient: bool, defaultValueLiteral: str, defaultValue: str, unsettable: bool, derived: bool, ecoreDiff_EStructuralFeature: "ecoreDiff_EClass" = None, EStructuralFeature: "ecoreDiff_EClass" = None, ecoreDiff_EStructuralFeature134: "ecoreDiff_ChangedEStructuralFeature" = None, eStructuralFeatures: "ecoreDiff_EClass" = None):
        self.changeable = changeable
        self.volatile = volatile
        self.transient = transient
        self.defaultValueLiteral = defaultValueLiteral
        self.defaultValue = defaultValue
        self.unsettable = unsettable
        self.derived = derived
        self.ecoreDiff_EStructuralFeature = ecoreDiff_EStructuralFeature
        self.EStructuralFeature = EStructuralFeature
        self.ecoreDiff_EStructuralFeature134 = ecoreDiff_EStructuralFeature134
        self.eStructuralFeatures = eStructuralFeatures
        
        pass
    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


    @property
    def derived(self):
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived


    @property
    def transient(self):
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient


    @property
    def unsettable(self):
        return self.__unsettable

    @unsettable.setter
    def unsettable(self, unsettable: bool):
        self.__unsettable = unsettable


    @property
    def defaultValueLiteral(self):
        return self.__defaultValueLiteral

    @defaultValueLiteral.setter
    def defaultValueLiteral(self, defaultValueLiteral: str):
        self.__defaultValueLiteral = defaultValueLiteral


    @property
    def volatile(self):
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: bool):
        self.__volatile = volatile


    @property
    def changeable(self):
        return self.__changeable

    @changeable.setter
    def changeable(self, changeable: bool):
        self.__changeable = changeable


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
            if hasattr(old_value, "EClass92"):
                opp_val = getattr(old_value, "EClass92", None)
                if opp_val == self:
                    setattr(old_value, "EClass92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EClass92"):
                opp_val = getattr(value, "EClass92", None)
                setattr(value, "EClass92", self)

    @property
    def ecoreDiff_EStructuralFeature134(self):
        return self.__ecoreDiff_EStructuralFeature134

    @ecoreDiff_EStructuralFeature134.setter
    def ecoreDiff_EStructuralFeature134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EStructuralFeature__ecoreDiff_EStructuralFeature134", None)
        self.__ecoreDiff_EStructuralFeature134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_ChangedEStructuralFeature"):
                opp_val = getattr(old_value, "ecoreDiff_ChangedEStructuralFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedEStructuralFeature"):
                opp_val = getattr(value, "ecoreDiff_ChangedEStructuralFeature", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_ChangedEStructuralFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecoreDiff_EAttribute(EStructuralFeature):

    def __init__(self, iD: bool, ecoreDiff_EAttribute34: "ecoreDiff_EClass" = None, ecoreDiff_EAttribute90: "ecoreDiff_EDataType" = None, ecoreDiff_EAttribute21: "ecoreDiff_EClass" = None, ecoreDiff_EAttribute: "ecoreDiff_EClass" = None, ecoreDiff_EAttribute132: "ecoreDiff_ChangedEAttribute" = None, ecoreDiff_EAttribute101: "ecoreDiff_EReference" = None):
        self.iD = iD
        self.ecoreDiff_EAttribute34 = ecoreDiff_EAttribute34
        self.ecoreDiff_EAttribute90 = ecoreDiff_EAttribute90
        self.ecoreDiff_EAttribute21 = ecoreDiff_EAttribute21
        self.ecoreDiff_EAttribute = ecoreDiff_EAttribute
        self.ecoreDiff_EAttribute132 = ecoreDiff_EAttribute132
        self.ecoreDiff_EAttribute101 = ecoreDiff_EAttribute101
        
        pass
    @property
    def iD(self):
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
    def ecoreDiff_EAttribute101(self):
        return self.__ecoreDiff_EAttribute101

    @ecoreDiff_EAttribute101.setter
    def ecoreDiff_EAttribute101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAttribute__ecoreDiff_EAttribute101", None)
        self.__ecoreDiff_EAttribute101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EReference100"):
                opp_val = getattr(old_value, "ecoreDiff_EReference100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EReference100"):
                opp_val = getattr(value, "ecoreDiff_EReference100", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EReference100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def ecoreDiff_EAttribute90(self):
        return self.__ecoreDiff_EAttribute90

    @ecoreDiff_EAttribute90.setter
    def ecoreDiff_EAttribute90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAttribute__ecoreDiff_EAttribute90", None)
        self.__ecoreDiff_EAttribute90 = value
        
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
    def ecoreDiff_EAttribute132(self):
        return self.__ecoreDiff_EAttribute132

    @ecoreDiff_EAttribute132.setter
    def ecoreDiff_EAttribute132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAttribute__ecoreDiff_EAttribute132", None)
        self.__ecoreDiff_EAttribute132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_ChangedEAttribute"):
                opp_val = getattr(old_value, "ecoreDiff_ChangedEAttribute", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedEAttribute"):
                opp_val = getattr(value, "ecoreDiff_ChangedEAttribute", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_ChangedEAttribute", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
class ecoreDiff_ChangedEClassifier(EClassifier):

    pass
class ecoreDiff_EDataType(EClassifier):

    def __init__(self, serializable: bool, ecoreDiff_EDataType: "ecoreDiff_EAttribute" = None, ecoreDiff_EDataType120: "ecoreDiff_ChangedEDataType" = None):
        self.serializable = serializable
        self.ecoreDiff_EDataType = ecoreDiff_EDataType
        self.ecoreDiff_EDataType120 = ecoreDiff_EDataType120
        
        pass
    @property
    def serializable(self):
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
            if hasattr(old_value, "ecoreDiff_EAttribute90"):
                opp_val = getattr(old_value, "ecoreDiff_EAttribute90", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EAttribute90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EAttribute90"):
                opp_val = getattr(value, "ecoreDiff_EAttribute90", None)
                setattr(value, "ecoreDiff_EAttribute90", self)

    @property
    def ecoreDiff_EDataType120(self):
        return self.__ecoreDiff_EDataType120

    @ecoreDiff_EDataType120.setter
    def ecoreDiff_EDataType120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EDataType__ecoreDiff_EDataType120", None)
        self.__ecoreDiff_EDataType120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_ChangedEDataType"):
                opp_val = getattr(old_value, "ecoreDiff_ChangedEDataType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedEDataType"):
                opp_val = getattr(value, "ecoreDiff_ChangedEDataType", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_ChangedEDataType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecoreDiff_AddedEClassifier(EClassifier):

    pass
class ecoreDiff_DeletedEClassifier(EClassifier):

    pass
class ecoreDiff_EClass(EClassifier):

    def __init__(self, abstract: bool, interface: bool, ecoreDiff_EClass15: set["ecoreDiff_EReference"] = None, ecoreDiff_EClass33: "ecoreDiff_EAttribute" = None, ecoreDiff_EClass36: set["ecoreDiff_EGenericType"] = None, ecoreDiff_EClass38: set["ecoreDiff_EGenericType"] = None, ecoreDiff_EClass17: set["ecoreDiff_EReference"] = None, ecoreDiff_EClass20: set["ecoreDiff_EAttribute"] = None, ecoreDiff_EClass23: set["ecoreDiff_EReference"] = None, ecoreDiff_EClass26: set["ecoreDiff_EOperation"] = None, ecoreDiff_EClass28: set["ecoreDiff_EStructuralFeature"] = None, ecoreDiff_EClass31: "ecoreDiff_EClass" = None, ecoreDiff_EClass29: set["ecoreDiff_EClass"] = None, ecoreDiff_EClass: "ecoreDiff_EClass" = None, ecoreDiff_EClass7: set["ecoreDiff_EClass"] = None, eContainingClass: set["ecoreDiff_EOperation"] = None, ecoreDiff_EClass11: set["ecoreDiff_EAttribute"] = None, eContainingClass13: set["ecoreDiff_EStructuralFeature"] = None, EClass92: "ecoreDiff_EStructuralFeature" = None, EClass: "ecoreDiff_EOperation" = None, ecoreDiff_EClass98: "ecoreDiff_EReference" = None, ecoreDiff_EClass113: "ecoreDiff_ChangedEClass" = None):
        self.abstract = abstract
        self.interface = interface
        self.ecoreDiff_EClass15 = ecoreDiff_EClass15 if ecoreDiff_EClass15 is not None else set()
        self.ecoreDiff_EClass33 = ecoreDiff_EClass33
        self.ecoreDiff_EClass36 = ecoreDiff_EClass36 if ecoreDiff_EClass36 is not None else set()
        self.ecoreDiff_EClass38 = ecoreDiff_EClass38 if ecoreDiff_EClass38 is not None else set()
        self.ecoreDiff_EClass17 = ecoreDiff_EClass17 if ecoreDiff_EClass17 is not None else set()
        self.ecoreDiff_EClass20 = ecoreDiff_EClass20 if ecoreDiff_EClass20 is not None else set()
        self.ecoreDiff_EClass23 = ecoreDiff_EClass23 if ecoreDiff_EClass23 is not None else set()
        self.ecoreDiff_EClass26 = ecoreDiff_EClass26 if ecoreDiff_EClass26 is not None else set()
        self.ecoreDiff_EClass28 = ecoreDiff_EClass28 if ecoreDiff_EClass28 is not None else set()
        self.ecoreDiff_EClass31 = ecoreDiff_EClass31
        self.ecoreDiff_EClass29 = ecoreDiff_EClass29 if ecoreDiff_EClass29 is not None else set()
        self.ecoreDiff_EClass = ecoreDiff_EClass
        self.ecoreDiff_EClass7 = ecoreDiff_EClass7 if ecoreDiff_EClass7 is not None else set()
        self.eContainingClass = eContainingClass if eContainingClass is not None else set()
        self.ecoreDiff_EClass11 = ecoreDiff_EClass11 if ecoreDiff_EClass11 is not None else set()
        self.eContainingClass13 = eContainingClass13 if eContainingClass13 is not None else set()
        self.EClass92 = EClass92
        self.EClass = EClass
        self.ecoreDiff_EClass98 = ecoreDiff_EClass98
        self.ecoreDiff_EClass113 = ecoreDiff_EClass113
        
        pass
    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract


    @property
    def interface(self):
        return self.__interface

    @interface.setter
    def interface(self, interface: bool):
        self.__interface = interface


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
    def ecoreDiff_EClass113(self):
        return self.__ecoreDiff_EClass113

    @ecoreDiff_EClass113.setter
    def ecoreDiff_EClass113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass113", None)
        self.__ecoreDiff_EClass113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_ChangedEClass"):
                opp_val = getattr(old_value, "ecoreDiff_ChangedEClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedEClass"):
                opp_val = getattr(value, "ecoreDiff_ChangedEClass", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_ChangedEClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def ecoreDiff_EClass98(self):
        return self.__ecoreDiff_EClass98

    @ecoreDiff_EClass98.setter
    def ecoreDiff_EClass98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass98", None)
        self.__ecoreDiff_EClass98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EReference97"):
                opp_val = getattr(old_value, "ecoreDiff_EReference97", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EReference97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EReference97"):
                opp_val = getattr(value, "ecoreDiff_EReference97", None)
                setattr(value, "ecoreDiff_EReference97", self)

    @property
    def EClass92(self):
        return self.__EClass92

    @EClass92.setter
    def EClass92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__EClass92", None)
        self.__EClass92 = value
        
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

class EModelElement:

    pass
class ecoreDiff_DeletedEModelElement(EModelElement):

    pass
class ecoreDiff_ChangedEModelElement(EModelElement):

    pass
class ecoreDiff_AddedEModelElement(EModelElement):

    pass
class ecoreDiff_EFactory(EModelElement):

    pass
class ecoreDiff_ENamedElement(EModelElement):

    def __init__(self, name: str, ecoreDiff_ENamedElement: "ecoreDiff_ChangedENamedElement" = None):
        self.name = name
        self.ecoreDiff_ENamedElement = ecoreDiff_ENamedElement
        
        pass
    @property
    def name(self):
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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedENamedElement"):
                opp_val = getattr(value, "ecoreDiff_ChangedENamedElement", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_ChangedENamedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecoreDiff_EAnnotation(EModelElement):

    def __init__(self, source: str, ecoreDiff_EAnnotation: set["ecoreDiff_EStringToStringMapEntry"] = None, eAnnotations: "ecoreDiff_EModelElement" = None, ecoreDiff_EAnnotation3: set["ecoreDiff_EObject"] = None, ecoreDiff_EAnnotation5: set["ecoreDiff_EObject"] = None, EAnnotation: "ecoreDiff_EModelElement" = None, ecoreDiff_EAnnotation107: "ecoreDiff_ChangedEAnnotation" = None):
        self.source = source
        self.ecoreDiff_EAnnotation = ecoreDiff_EAnnotation if ecoreDiff_EAnnotation is not None else set()
        self.eAnnotations = eAnnotations
        self.ecoreDiff_EAnnotation3 = ecoreDiff_EAnnotation3 if ecoreDiff_EAnnotation3 is not None else set()
        self.ecoreDiff_EAnnotation5 = ecoreDiff_EAnnotation5 if ecoreDiff_EAnnotation5 is not None else set()
        self.EAnnotation = EAnnotation
        self.ecoreDiff_EAnnotation107 = ecoreDiff_EAnnotation107
        
        pass
    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source


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
    def ecoreDiff_EAnnotation107(self):
        return self.__ecoreDiff_EAnnotation107

    @ecoreDiff_EAnnotation107.setter
    def ecoreDiff_EAnnotation107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAnnotation__ecoreDiff_EAnnotation107", None)
        self.__ecoreDiff_EAnnotation107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_ChangedEAnnotation"):
                opp_val = getattr(old_value, "ecoreDiff_ChangedEAnnotation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedEAnnotation"):
                opp_val = getattr(value, "ecoreDiff_ChangedEAnnotation", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_ChangedEAnnotation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class ecoreDiff_EObject:

    pass
class ecoreDiff_EModelElement(DifferenceElement, EObject):

    pass
class ecoreDiff_EStringToStringMapEntry:

    def __init__(self, key: str, value: str, ecoreDiff_EStringToStringMapEntry: "ecoreDiff_EAnnotation" = None, ecoreDiff_EStringToStringMapEntry109: "ecoreDiff_ChangedEStringToStringMapEntry" = None):
        self.key = key
        self.value = value
        self.ecoreDiff_EStringToStringMapEntry = ecoreDiff_EStringToStringMapEntry
        self.ecoreDiff_EStringToStringMapEntry109 = ecoreDiff_EStringToStringMapEntry109
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def ecoreDiff_EStringToStringMapEntry109(self):
        return self.__ecoreDiff_EStringToStringMapEntry109

    @ecoreDiff_EStringToStringMapEntry109.setter
    def ecoreDiff_EStringToStringMapEntry109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EStringToStringMapEntry__ecoreDiff_EStringToStringMapEntry109", None)
        self.__ecoreDiff_EStringToStringMapEntry109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_ChangedEStringToStringMapEntry"):
                opp_val = getattr(old_value, "ecoreDiff_ChangedEStringToStringMapEntry", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_ChangedEStringToStringMapEntry"):
                opp_val = getattr(value, "ecoreDiff_ChangedEStringToStringMapEntry", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_ChangedEStringToStringMapEntry", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
