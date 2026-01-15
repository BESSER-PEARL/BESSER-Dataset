from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class EEnum:

    pass
class ecoreDiff_DeletedEEnum(EEnum):

    pass
class ecoreDiff_AddedEEnum(EEnum):

    pass
class EEnumLiteral:

    pass
class ecoreDiff_DeletedEEnumLiteral(EEnumLiteral):

    pass
class ecoreDiff_ChangedEEnumLiteral(EEnumLiteral):

    pass
class ecoreDiff_AddedEEnumLiteral(EEnumLiteral):

    pass
class ecoreDiff_ChangedEEnum(EEnum):

    pass
class EReference:

    pass
class ecoreDiff_AddedEReference(EReference):

    pass
class ecoreDiff_ChangedEReference(EReference):

    pass
class ecoreDiff_DeletedEReference(EReference):

    pass
class EStructuralFeature_Wildcard:

    pass
class ecoreDiff_ChangedEStructuralFeature_Wildcard(EStructuralFeature_Wildcard):

    pass
class ecoreDiff_DeletedEStructuralFeature_Wildcard(EStructuralFeature_Wildcard):

    pass
class ecoreDiff_AddedEStructuralFeature_Wildcard(EStructuralFeature_Wildcard):

    pass
class EParameter:

    pass
class ecoreDiff_AddedEParameter(EParameter):

    pass
class EAttribute:

    pass
class ecoreDiff_DeletedEAttribute(EAttribute):

    pass
class ecoreDiff_ChangedEAttribute(EAttribute):

    pass
class ecoreDiff_AddedEAttribute(EAttribute):

    pass
class ecoreDiff_ChangedEParameter(EParameter):

    pass
class ecoreDiff_DeletedEParameter(EParameter):

    pass
class EOperation:

    pass
class ecoreDiff_AddedEOperation(EOperation):

    pass
class ecoreDiff_ChangedEOperation(EOperation):

    pass
class ecoreDiff_DeletedEOperation(EOperation):

    pass
class ETypeParameter:

    pass
class ecoreDiff_DeletedETypeParameter(ETypeParameter):

    pass
class ecoreDiff_ChangedETypeParameter(ETypeParameter):

    pass
class ecoreDiff_AddedETypeParameter(ETypeParameter):

    pass
class EClassifier_Wildcard:

    pass
class ecoreDiff_DeletedEClassifier_Wildcard(EClassifier_Wildcard):

    pass
class ecoreDiff_ChangedEClassifier_Wildcard(EClassifier_Wildcard):

    pass
class ecoreDiff_AddedEClassifier_Wildcard(EClassifier_Wildcard):

    pass
class EGenericType:

    pass
class ecoreDiff_DeletedEGenericType(EGenericType):

    pass
class ecoreDiff_ChangedEGenericType(EGenericType):

    pass
class ecoreDiff_AddedEGenericType(EGenericType):

    pass
class EPackage:

    pass
class ecoreDiff_ChangedEPackage(EPackage):

    pass
class ecoreDiff_DeletedEPackage(EPackage):

    pass
class ecoreDiff_AddedEPackage(EPackage):

    pass
class EFactory:

    pass
class ecoreDiff_ChangedEFactory(EFactory):

    pass
class ecoreDiff_DeletedEFactory(EFactory):

    pass
class ecoreDiff_AddedEFactory(EFactory):

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
class ecoreDiff_DifferenceElement:

    pass
class ecoreDiff_DifferenceModel:

    pass
class DifferenceElement:

    pass
class EAnnotation:

    pass
class ecoreDiff_ChangedEAnnotation(EAnnotation):

    pass
class ecoreDiff_DeletedEAnnotation(EAnnotation):

    pass
class ecoreDiff_AddedEAnnotation(EAnnotation):

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
class EStructuralFeature:

    pass
class ecoreDiff_DeletedEStructuralFeature(EStructuralFeature):

    pass
class ecoreDiff_ChangedEStructuralFeature(EStructuralFeature):

    pass
class ecoreDiff_AddedEStructuralFeature(EStructuralFeature):

    pass
class ecoreDiff_EAttribute(EStructuralFeature):

    def __init__(self, iD: bool, ecoreDiff_EAttribute: "ecoreDiff_EReference" = None, ecoreDiff_EAttribute225: "ecoreDiff_ChangedEAttribute" = None):
        self.iD = iD
        self.ecoreDiff_EAttribute = ecoreDiff_EAttribute
        self.ecoreDiff_EAttribute225 = ecoreDiff_EAttribute225
        
    @property
    def iD(self) -> bool:
        return self.__iD

    @iD.setter
    def iD(self, iD: bool):
        self.__iD = iD

    @property
    def ecoreDiff_EAttribute225(self):
        return self.__ecoreDiff_EAttribute225

    @ecoreDiff_EAttribute225.setter
    def ecoreDiff_EAttribute225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAttribute__ecoreDiff_EAttribute225", None)
        self.__ecoreDiff_EAttribute225 = value
        
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
            if hasattr(old_value, "ecoreDiff_EReference79"):
                opp_val = getattr(old_value, "ecoreDiff_EReference79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EReference79"):
                opp_val = getattr(value, "ecoreDiff_EReference79", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EReference79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecoreDiff_EReference(EStructuralFeature):

    def __init__(self, containment: bool, resolveProxies: bool, ecoreDiff_EReference: "ecoreDiff_EReference" = None, ecoreDiff_EReference76: "ecoreDiff_EReference" = None, ecoreDiff_EReference79: set["ecoreDiff_EAttribute"] = None, ecoreDiff_EReference251: "ecoreDiff_ChangedEReference" = None):
        self.containment = containment
        self.resolveProxies = resolveProxies
        self.ecoreDiff_EReference = ecoreDiff_EReference
        self.ecoreDiff_EReference76 = ecoreDiff_EReference76
        self.ecoreDiff_EReference79 = ecoreDiff_EReference79 if ecoreDiff_EReference79 is not None else set()
        self.ecoreDiff_EReference251 = ecoreDiff_EReference251
        
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
    def ecoreDiff_EReference(self):
        return self.__ecoreDiff_EReference

    @ecoreDiff_EReference.setter
    def ecoreDiff_EReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference", None)
        self.__ecoreDiff_EReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EReference76"):
                opp_val = getattr(old_value, "ecoreDiff_EReference76", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EReference76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EReference76"):
                opp_val = getattr(value, "ecoreDiff_EReference76", None)
                setattr(value, "ecoreDiff_EReference76", self)

    @property
    def ecoreDiff_EReference251(self):
        return self.__ecoreDiff_EReference251

    @ecoreDiff_EReference251.setter
    def ecoreDiff_EReference251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference251", None)
        self.__ecoreDiff_EReference251 = value
        
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

    @property
    def ecoreDiff_EReference79(self):
        return self.__ecoreDiff_EReference79

    @ecoreDiff_EReference79.setter
    def ecoreDiff_EReference79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference79", None)
        self.__ecoreDiff_EReference79 = value if value is not None else set()
        
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
    def ecoreDiff_EReference76(self):
        return self.__ecoreDiff_EReference76

    @ecoreDiff_EReference76.setter
    def ecoreDiff_EReference76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference76", None)
        self.__ecoreDiff_EReference76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EReference"):
                opp_val = getattr(old_value, "ecoreDiff_EReference", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EReference"):
                opp_val = getattr(value, "ecoreDiff_EReference", None)
                setattr(value, "ecoreDiff_EReference", self)

class ecoreDiff_EStructuralFeature_Wildcard:

    pass
class EObject:

    pass
class ecoreDiff_DeletedEObject(EObject):

    pass
class ecoreDiff_AddedEObject(EObject):

    pass
class ecoreDiff_ChangedEObject(EObject):

    pass
class ETypedElement:

    pass
class ecoreDiff_DeletedETypedElement(ETypedElement):

    pass
class ecoreDiff_EParameter(ETypedElement):

    pass
class ecoreDiff_ChangedETypedElement(ETypedElement):

    pass
class ecoreDiff_AddedETypedElement(ETypedElement):

    pass
class ecoreDiff_EClassifier_Wildcard:

    pass
class ENamedElement:

    pass
class ecoreDiff_ChangedENamedElement(ENamedElement):

    pass
class ecoreDiff_DeletedENamedElement(ENamedElement):

    pass
class ecoreDiff_AddedENamedElement(ENamedElement):

    pass
class ecoreDiff_EEnumLiteral(ENamedElement):

    def __init__(self, value: int, instance: str, literal: str, ecoreDiff_EEnumLiteral: "ecoreDiff_EEnum" = None, ecoreDiff_EEnumLiteral82: "ecoreDiff_EEnum" = None, ecoreDiff_EEnumLiteral269: "ecoreDiff_ChangedEEnumLiteral" = None):
        self.value = value
        self.instance = instance
        self.literal = literal
        self.ecoreDiff_EEnumLiteral = ecoreDiff_EEnumLiteral
        self.ecoreDiff_EEnumLiteral82 = ecoreDiff_EEnumLiteral82
        self.ecoreDiff_EEnumLiteral269 = ecoreDiff_EEnumLiteral269
        
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
    def ecoreDiff_EEnumLiteral(self):
        return self.__ecoreDiff_EEnumLiteral

    @ecoreDiff_EEnumLiteral.setter
    def ecoreDiff_EEnumLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EEnumLiteral__ecoreDiff_EEnumLiteral", None)
        self.__ecoreDiff_EEnumLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EEnum"):
                opp_val = getattr(old_value, "ecoreDiff_EEnum", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EEnum"):
                opp_val = getattr(value, "ecoreDiff_EEnum", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EEnum", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EEnumLiteral269(self):
        return self.__ecoreDiff_EEnumLiteral269

    @ecoreDiff_EEnumLiteral269.setter
    def ecoreDiff_EEnumLiteral269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EEnumLiteral__ecoreDiff_EEnumLiteral269", None)
        self.__ecoreDiff_EEnumLiteral269 = value
        
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
    def ecoreDiff_EEnumLiteral82(self):
        return self.__ecoreDiff_EEnumLiteral82

    @ecoreDiff_EEnumLiteral82.setter
    def ecoreDiff_EEnumLiteral82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EEnumLiteral__ecoreDiff_EEnumLiteral82", None)
        self.__ecoreDiff_EEnumLiteral82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EEnum83"):
                opp_val = getattr(old_value, "ecoreDiff_EEnum83", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EEnum83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EEnum83"):
                opp_val = getattr(value, "ecoreDiff_EEnum83", None)
                setattr(value, "ecoreDiff_EEnum83", self)

class ecoreDiff_ETypeParameter(ENamedElement):

    pass
class ecoreDiff_ETypedElement(ENamedElement):

    def __init__(self, ordered: bool, unique: bool, lowerBound: int, upperBound: int, ecoreDiff_ETypedElement: "ecoreDiff_EObject" = None, ecoreDiff_ETypedElement68: "ecoreDiff_EGenericType" = None, ecoreDiff_ETypedElement207: "ecoreDiff_ChangedETypedElement" = None):
        self.ordered = ordered
        self.unique = unique
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.ecoreDiff_ETypedElement = ecoreDiff_ETypedElement
        self.ecoreDiff_ETypedElement68 = ecoreDiff_ETypedElement68
        self.ecoreDiff_ETypedElement207 = ecoreDiff_ETypedElement207
        
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
    def ecoreDiff_ETypedElement207(self):
        return self.__ecoreDiff_ETypedElement207

    @ecoreDiff_ETypedElement207.setter
    def ecoreDiff_ETypedElement207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_ETypedElement__ecoreDiff_ETypedElement207", None)
        self.__ecoreDiff_ETypedElement207 = value
        
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
            if hasattr(old_value, "ecoreDiff_EObject66"):
                opp_val = getattr(old_value, "ecoreDiff_EObject66", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EObject66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EObject66"):
                opp_val = getattr(value, "ecoreDiff_EObject66", None)
                setattr(value, "ecoreDiff_EObject66", self)

    @property
    def ecoreDiff_ETypedElement68(self):
        return self.__ecoreDiff_ETypedElement68

    @ecoreDiff_ETypedElement68.setter
    def ecoreDiff_ETypedElement68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_ETypedElement__ecoreDiff_ETypedElement68", None)
        self.__ecoreDiff_ETypedElement68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EGenericType69"):
                opp_val = getattr(old_value, "ecoreDiff_EGenericType69", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EGenericType69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EGenericType69"):
                opp_val = getattr(value, "ecoreDiff_EGenericType69", None)
                setattr(value, "ecoreDiff_EGenericType69", self)

class ecoreDiff_EClassifier(ENamedElement):

    def __init__(self, instanceClassName: str, instanceTypeName: str, ecoreDiff_EClassifier29: "ecoreDiff_EPackage" = None, ecoreDiff_EClassifier: "ecoreDiff_EObject" = None, ecoreDiff_EClassifier19: set["ecoreDiff_ETypeParameter"] = None, ecoreDiff_EClassifier58: "ecoreDiff_EOperation" = None, ecoreDiff_EClassifier50: "ecoreDiff_EGenericType" = None, ecoreDiff_EClassifier129: "ecoreDiff_ChangedEClassifier" = None):
        self.instanceClassName = instanceClassName
        self.instanceTypeName = instanceTypeName
        self.ecoreDiff_EClassifier29 = ecoreDiff_EClassifier29
        self.ecoreDiff_EClassifier = ecoreDiff_EClassifier
        self.ecoreDiff_EClassifier19 = ecoreDiff_EClassifier19 if ecoreDiff_EClassifier19 is not None else set()
        self.ecoreDiff_EClassifier58 = ecoreDiff_EClassifier58
        self.ecoreDiff_EClassifier50 = ecoreDiff_EClassifier50
        self.ecoreDiff_EClassifier129 = ecoreDiff_EClassifier129
        
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
    def ecoreDiff_EClassifier19(self):
        return self.__ecoreDiff_EClassifier19

    @ecoreDiff_EClassifier19.setter
    def ecoreDiff_EClassifier19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClassifier__ecoreDiff_EClassifier19", None)
        self.__ecoreDiff_EClassifier19 = value if value is not None else set()
        
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
    def ecoreDiff_EClassifier29(self):
        return self.__ecoreDiff_EClassifier29

    @ecoreDiff_EClassifier29.setter
    def ecoreDiff_EClassifier29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClassifier__ecoreDiff_EClassifier29", None)
        self.__ecoreDiff_EClassifier29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EPackage28"):
                opp_val = getattr(old_value, "ecoreDiff_EPackage28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EPackage28"):
                opp_val = getattr(value, "ecoreDiff_EPackage28", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EPackage28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EClassifier129(self):
        return self.__ecoreDiff_EClassifier129

    @ecoreDiff_EClassifier129.setter
    def ecoreDiff_EClassifier129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClassifier__ecoreDiff_EClassifier129", None)
        self.__ecoreDiff_EClassifier129 = value
        
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
    def ecoreDiff_EClassifier58(self):
        return self.__ecoreDiff_EClassifier58

    @ecoreDiff_EClassifier58.setter
    def ecoreDiff_EClassifier58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClassifier__ecoreDiff_EClassifier58", None)
        self.__ecoreDiff_EClassifier58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EOperation57"):
                opp_val = getattr(old_value, "ecoreDiff_EOperation57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EOperation57"):
                opp_val = getattr(value, "ecoreDiff_EOperation57", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EOperation57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EClassifier(self):
        return self.__ecoreDiff_EClassifier

    @ecoreDiff_EClassifier.setter
    def ecoreDiff_EClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClassifier__ecoreDiff_EClassifier", None)
        self.__ecoreDiff_EClassifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EObject17"):
                opp_val = getattr(old_value, "ecoreDiff_EObject17", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EObject17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EObject17"):
                opp_val = getattr(value, "ecoreDiff_EObject17", None)
                setattr(value, "ecoreDiff_EObject17", self)

    @property
    def ecoreDiff_EClassifier50(self):
        return self.__ecoreDiff_EClassifier50

    @ecoreDiff_EClassifier50.setter
    def ecoreDiff_EClassifier50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClassifier__ecoreDiff_EClassifier50", None)
        self.__ecoreDiff_EClassifier50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EGenericType49"):
                opp_val = getattr(old_value, "ecoreDiff_EGenericType49", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EGenericType49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EGenericType49"):
                opp_val = getattr(value, "ecoreDiff_EGenericType49", None)
                setattr(value, "ecoreDiff_EGenericType49", self)

class ecoreDiff_EPackage(ENamedElement):

    def __init__(self, nsURI: str, nsPrefix: str, ecoreDiff_EPackage: "ecoreDiff_EFactory" = None, ecoreDiff_EPackage23: "ecoreDiff_EPackage" = None, ecoreDiff_EPackage21: set["ecoreDiff_EPackage"] = None, ecoreDiff_EPackage26: "ecoreDiff_EPackage" = None, ecoreDiff_EPackage24: "ecoreDiff_EPackage" = None, ecoreDiff_EPackage28: set["ecoreDiff_EClassifier"] = None, ecoreDiff_EPackage146: "ecoreDiff_ChangedEPackage" = None):
        self.nsURI = nsURI
        self.nsPrefix = nsPrefix
        self.ecoreDiff_EPackage = ecoreDiff_EPackage
        self.ecoreDiff_EPackage23 = ecoreDiff_EPackage23
        self.ecoreDiff_EPackage21 = ecoreDiff_EPackage21 if ecoreDiff_EPackage21 is not None else set()
        self.ecoreDiff_EPackage26 = ecoreDiff_EPackage26
        self.ecoreDiff_EPackage24 = ecoreDiff_EPackage24
        self.ecoreDiff_EPackage28 = ecoreDiff_EPackage28 if ecoreDiff_EPackage28 is not None else set()
        self.ecoreDiff_EPackage146 = ecoreDiff_EPackage146
        
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
    def ecoreDiff_EPackage28(self):
        return self.__ecoreDiff_EPackage28

    @ecoreDiff_EPackage28.setter
    def ecoreDiff_EPackage28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__ecoreDiff_EPackage28", None)
        self.__ecoreDiff_EPackage28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EClassifier29"):
                    opp_val = getattr(item, "ecoreDiff_EClassifier29", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EClassifier29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EClassifier29"):
                    opp_val = getattr(item, "ecoreDiff_EClassifier29", None)
                    
                    setattr(item, "ecoreDiff_EClassifier29", self)
                    

    @property
    def ecoreDiff_EPackage146(self):
        return self.__ecoreDiff_EPackage146

    @ecoreDiff_EPackage146.setter
    def ecoreDiff_EPackage146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__ecoreDiff_EPackage146", None)
        self.__ecoreDiff_EPackage146 = value
        
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

    @property
    def ecoreDiff_EPackage24(self):
        return self.__ecoreDiff_EPackage24

    @ecoreDiff_EPackage24.setter
    def ecoreDiff_EPackage24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__ecoreDiff_EPackage24", None)
        self.__ecoreDiff_EPackage24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EPackage26"):
                opp_val = getattr(old_value, "ecoreDiff_EPackage26", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EPackage26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EPackage26"):
                opp_val = getattr(value, "ecoreDiff_EPackage26", None)
                setattr(value, "ecoreDiff_EPackage26", self)

    @property
    def ecoreDiff_EPackage26(self):
        return self.__ecoreDiff_EPackage26

    @ecoreDiff_EPackage26.setter
    def ecoreDiff_EPackage26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__ecoreDiff_EPackage26", None)
        self.__ecoreDiff_EPackage26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EPackage24"):
                opp_val = getattr(old_value, "ecoreDiff_EPackage24", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EPackage24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EPackage24"):
                opp_val = getattr(value, "ecoreDiff_EPackage24", None)
                setattr(value, "ecoreDiff_EPackage24", self)

    @property
    def ecoreDiff_EPackage21(self):
        return self.__ecoreDiff_EPackage21

    @ecoreDiff_EPackage21.setter
    def ecoreDiff_EPackage21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__ecoreDiff_EPackage21", None)
        self.__ecoreDiff_EPackage21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EPackage23"):
                    opp_val = getattr(item, "ecoreDiff_EPackage23", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EPackage23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EPackage23"):
                    opp_val = getattr(item, "ecoreDiff_EPackage23", None)
                    
                    setattr(item, "ecoreDiff_EPackage23", self)
                    

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
            if hasattr(old_value, "ecoreDiff_EFactory"):
                opp_val = getattr(old_value, "ecoreDiff_EFactory", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EFactory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EFactory"):
                opp_val = getattr(value, "ecoreDiff_EFactory", None)
                setattr(value, "ecoreDiff_EFactory", self)

    @property
    def ecoreDiff_EPackage23(self):
        return self.__ecoreDiff_EPackage23

    @ecoreDiff_EPackage23.setter
    def ecoreDiff_EPackage23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__ecoreDiff_EPackage23", None)
        self.__ecoreDiff_EPackage23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EPackage21"):
                opp_val = getattr(old_value, "ecoreDiff_EPackage21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EPackage21"):
                opp_val = getattr(value, "ecoreDiff_EPackage21", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EPackage21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecoreDiff_EModelElement(DifferenceElement, EObject):

    pass
class ecoreDiff_EStringToStringMapEntry:

    def __init__(self, key: str, value: str, ecoreDiff_EStringToStringMapEntry: "ecoreDiff_EAnnotation" = None, ecoreDiff_EStringToStringMapEntry102: "ecoreDiff_ChangedEStringToStringMapEntry" = None):
        self.key = key
        self.value = value
        self.ecoreDiff_EStringToStringMapEntry = ecoreDiff_EStringToStringMapEntry
        self.ecoreDiff_EStringToStringMapEntry102 = ecoreDiff_EStringToStringMapEntry102
        
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
    def ecoreDiff_EStringToStringMapEntry102(self):
        return self.__ecoreDiff_EStringToStringMapEntry102

    @ecoreDiff_EStringToStringMapEntry102.setter
    def ecoreDiff_EStringToStringMapEntry102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EStringToStringMapEntry__ecoreDiff_EStringToStringMapEntry102", None)
        self.__ecoreDiff_EStringToStringMapEntry102 = value
        
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

class EModelElement:

    pass
class ecoreDiff_AddedEModelElement(EModelElement):

    pass
class ecoreDiff_EFactory(EModelElement):

    pass
class ecoreDiff_ChangedEModelElement(EModelElement):

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

class ecoreDiff_DeletedEModelElement(EModelElement):

    pass
class ecoreDiff_EAnnotation(EModelElement):

    def __init__(self, source: str, ecoreDiff_EAnnotation4: set["ecoreDiff_EObject"] = None, ecoreDiff_EAnnotation6: set["ecoreDiff_EObject"] = None, ecoreDiff_EAnnotation: set["ecoreDiff_EStringToStringMapEntry"] = None, ecoreDiff_EAnnotation2: "ecoreDiff_EModelElement" = None, ecoreDiff_EAnnotation86: "ecoreDiff_EModelElement" = None, ecoreDiff_EAnnotation93: "ecoreDiff_ChangedEAnnotation" = None):
        self.source = source
        self.ecoreDiff_EAnnotation4 = ecoreDiff_EAnnotation4 if ecoreDiff_EAnnotation4 is not None else set()
        self.ecoreDiff_EAnnotation6 = ecoreDiff_EAnnotation6 if ecoreDiff_EAnnotation6 is not None else set()
        self.ecoreDiff_EAnnotation = ecoreDiff_EAnnotation if ecoreDiff_EAnnotation is not None else set()
        self.ecoreDiff_EAnnotation2 = ecoreDiff_EAnnotation2
        self.ecoreDiff_EAnnotation86 = ecoreDiff_EAnnotation86
        self.ecoreDiff_EAnnotation93 = ecoreDiff_EAnnotation93
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def ecoreDiff_EAnnotation2(self):
        return self.__ecoreDiff_EAnnotation2

    @ecoreDiff_EAnnotation2.setter
    def ecoreDiff_EAnnotation2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAnnotation__ecoreDiff_EAnnotation2", None)
        self.__ecoreDiff_EAnnotation2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EModelElement"):
                opp_val = getattr(old_value, "ecoreDiff_EModelElement", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EModelElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EModelElement"):
                opp_val = getattr(value, "ecoreDiff_EModelElement", None)
                setattr(value, "ecoreDiff_EModelElement", self)

    @property
    def ecoreDiff_EAnnotation86(self):
        return self.__ecoreDiff_EAnnotation86

    @ecoreDiff_EAnnotation86.setter
    def ecoreDiff_EAnnotation86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAnnotation__ecoreDiff_EAnnotation86", None)
        self.__ecoreDiff_EAnnotation86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EModelElement85"):
                opp_val = getattr(old_value, "ecoreDiff_EModelElement85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EModelElement85"):
                opp_val = getattr(value, "ecoreDiff_EModelElement85", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EModelElement85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EAnnotation6(self):
        return self.__ecoreDiff_EAnnotation6

    @ecoreDiff_EAnnotation6.setter
    def ecoreDiff_EAnnotation6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAnnotation__ecoreDiff_EAnnotation6", None)
        self.__ecoreDiff_EAnnotation6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EObject7"):
                    opp_val = getattr(item, "ecoreDiff_EObject7", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EObject7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EObject7"):
                    opp_val = getattr(item, "ecoreDiff_EObject7", None)
                    
                    setattr(item, "ecoreDiff_EObject7", self)
                    

    @property
    def ecoreDiff_EAnnotation4(self):
        return self.__ecoreDiff_EAnnotation4

    @ecoreDiff_EAnnotation4.setter
    def ecoreDiff_EAnnotation4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAnnotation__ecoreDiff_EAnnotation4", None)
        self.__ecoreDiff_EAnnotation4 = value if value is not None else set()
        
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
    def ecoreDiff_EAnnotation93(self):
        return self.__ecoreDiff_EAnnotation93

    @ecoreDiff_EAnnotation93.setter
    def ecoreDiff_EAnnotation93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAnnotation__ecoreDiff_EAnnotation93", None)
        self.__ecoreDiff_EAnnotation93 = value
        
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
                    

class ecoreDiff_EGenericType(EObject):

    pass
class ecoreDiff_EStructuralFeature(ETypedElement):

    def __init__(self, changeable: bool, volatile: bool, transient: bool, defaultValueLiteral: str, unsettable: bool, derived: bool, ecoreDiff_EStructuralFeature: "ecoreDiff_EClass" = None, ecoreDiff_EStructuralFeature74: "ecoreDiff_EObject" = None, ecoreDiff_EStructuralFeature234: "ecoreDiff_ChangedEStructuralFeature" = None):
        self.changeable = changeable
        self.volatile = volatile
        self.transient = transient
        self.defaultValueLiteral = defaultValueLiteral
        self.unsettable = unsettable
        self.derived = derived
        self.ecoreDiff_EStructuralFeature = ecoreDiff_EStructuralFeature
        self.ecoreDiff_EStructuralFeature74 = ecoreDiff_EStructuralFeature74
        self.ecoreDiff_EStructuralFeature234 = ecoreDiff_EStructuralFeature234
        
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
    def ecoreDiff_EStructuralFeature(self):
        return self.__ecoreDiff_EStructuralFeature

    @ecoreDiff_EStructuralFeature.setter
    def ecoreDiff_EStructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EStructuralFeature__ecoreDiff_EStructuralFeature", None)
        self.__ecoreDiff_EStructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EClass13"):
                opp_val = getattr(old_value, "ecoreDiff_EClass13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass13"):
                opp_val = getattr(value, "ecoreDiff_EClass13", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EClass13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EStructuralFeature234(self):
        return self.__ecoreDiff_EStructuralFeature234

    @ecoreDiff_EStructuralFeature234.setter
    def ecoreDiff_EStructuralFeature234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EStructuralFeature__ecoreDiff_EStructuralFeature234", None)
        self.__ecoreDiff_EStructuralFeature234 = value
        
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

    @property
    def ecoreDiff_EStructuralFeature74(self):
        return self.__ecoreDiff_EStructuralFeature74

    @ecoreDiff_EStructuralFeature74.setter
    def ecoreDiff_EStructuralFeature74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EStructuralFeature__ecoreDiff_EStructuralFeature74", None)
        self.__ecoreDiff_EStructuralFeature74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EObject75"):
                opp_val = getattr(old_value, "ecoreDiff_EObject75", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EObject75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EObject75"):
                opp_val = getattr(value, "ecoreDiff_EObject75", None)
                setattr(value, "ecoreDiff_EObject75", self)

class ecoreDiff_EOperation(ETypedElement):

    pass
class EClassifier:

    pass
class ecoreDiff_EDataType(EClassifier):

    def __init__(self, serializable: bool, ecoreDiff_EDataType: "ecoreDiff_ChangedEDataType" = None):
        self.serializable = serializable
        self.ecoreDiff_EDataType = ecoreDiff_EDataType
        
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
class ecoreDiff_ChangedEClassifier(EClassifier):

    pass
class ecoreDiff_EClass(EClassifier):

    def __init__(self, abstract: bool, interface: bool, ecoreDiff_EClass: "ecoreDiff_EClass" = None, ecoreDiff_EClass8: set["ecoreDiff_EClass"] = None, ecoreDiff_EClass11: set["ecoreDiff_EOperation"] = None, ecoreDiff_EClass13: set["ecoreDiff_EStructuralFeature"] = None, ecoreDiff_EClass15: set["ecoreDiff_EGenericType"] = None, ecoreDiff_EClass120: "ecoreDiff_ChangedEClass" = None):
        self.abstract = abstract
        self.interface = interface
        self.ecoreDiff_EClass = ecoreDiff_EClass
        self.ecoreDiff_EClass8 = ecoreDiff_EClass8 if ecoreDiff_EClass8 is not None else set()
        self.ecoreDiff_EClass11 = ecoreDiff_EClass11 if ecoreDiff_EClass11 is not None else set()
        self.ecoreDiff_EClass13 = ecoreDiff_EClass13 if ecoreDiff_EClass13 is not None else set()
        self.ecoreDiff_EClass15 = ecoreDiff_EClass15 if ecoreDiff_EClass15 is not None else set()
        self.ecoreDiff_EClass120 = ecoreDiff_EClass120
        
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
    def ecoreDiff_EClass8(self):
        return self.__ecoreDiff_EClass8

    @ecoreDiff_EClass8.setter
    def ecoreDiff_EClass8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass8", None)
        self.__ecoreDiff_EClass8 = value if value is not None else set()
        
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
    def ecoreDiff_EClass(self):
        return self.__ecoreDiff_EClass

    @ecoreDiff_EClass.setter
    def ecoreDiff_EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass", None)
        self.__ecoreDiff_EClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EClass8"):
                opp_val = getattr(old_value, "ecoreDiff_EClass8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass8"):
                opp_val = getattr(value, "ecoreDiff_EClass8", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EClass8", set([self]))
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
    def ecoreDiff_EClass120(self):
        return self.__ecoreDiff_EClass120

    @ecoreDiff_EClass120.setter
    def ecoreDiff_EClass120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass120", None)
        self.__ecoreDiff_EClass120 = value
        
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
    def ecoreDiff_EClass13(self):
        return self.__ecoreDiff_EClass13

    @ecoreDiff_EClass13.setter
    def ecoreDiff_EClass13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass13", None)
        self.__ecoreDiff_EClass13 = value if value is not None else set()
        
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
                    

class ecoreDiff_EObject:

    pass