from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class EStructuralFeature_Wildcard:

    pass
class ecoreDiff_DeletedEStructuralFeature_Wildcard(EStructuralFeature_Wildcard):

    pass
class ecoreDiff_AddedEStructuralFeature_Wildcard(EStructuralFeature_Wildcard):

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
class ecoreDiff_DeletedEEnum(EEnum):

    pass
class ecoreDiff_ChangedEEnum(EEnum):

    pass
class ecoreDiff_AddedEEnum(EEnum):

    pass
class EReference:

    pass
class ecoreDiff_DeletedEReference(EReference):

    pass
class ecoreDiff_ChangedEReference(EReference):

    pass
class ecoreDiff_AddedEReference(EReference):

    pass
class ecoreDiff_ChangedEStructuralFeature_Wildcard(EStructuralFeature_Wildcard):

    pass
class EOperation:

    pass
class ecoreDiff_DeletedEOperation(EOperation):

    pass
class ecoreDiff_AddedEOperation(EOperation):

    pass
class EClassifier_Wildcard:

    pass
class ecoreDiff_ChangedEClassifier_Wildcard(EClassifier_Wildcard):

    pass
class ecoreDiff_DeletedEClassifier_Wildcard(EClassifier_Wildcard):

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
class EAttribute:

    pass
class ecoreDiff_ChangedEAttribute(EAttribute):

    pass
class ecoreDiff_DeletedEAttribute(EAttribute):

    pass
class ecoreDiff_AddedEAttribute(EAttribute):

    pass
class EParameter:

    pass
class ecoreDiff_ChangedEParameter(EParameter):

    pass
class ecoreDiff_DeletedEParameter(EParameter):

    pass
class ecoreDiff_AddedEParameter(EParameter):

    pass
class ecoreDiff_ChangedEOperation(EOperation):

    pass
class EPackage:

    pass
class ecoreDiff_ChangedEPackage(EPackage):

    pass
class ecoreDiff_DeletedEPackage(EPackage):

    pass
class ecoreDiff_AddedEPackage(EPackage):

    pass
class ETypeParameter:

    pass
class ecoreDiff_DeletedETypeParameter(ETypeParameter):

    pass
class ecoreDiff_ChangedETypeParameter(ETypeParameter):

    pass
class ecoreDiff_AddedETypeParameter(ETypeParameter):

    pass
class EFactory:

    pass
class ecoreDiff_ChangedEFactory(EFactory):

    pass
class ecoreDiff_DeletedEFactory(EFactory):

    pass
class ecoreDiff_AddedEFactory(EFactory):

    pass
class EStringToStringMapEntry:

    pass
class ecoreDiff_DeletedEStringToStringMapEntry(EStringToStringMapEntry):

    pass
class ecoreDiff_ChangedEStringToStringMapEntry(EStringToStringMapEntry):

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
class EClass:

    pass
class ecoreDiff_ChangedEClass(EClass):

    pass
class ecoreDiff_DeletedEClass(EClass):

    pass
class ecoreDiff_AddedEClass(EClass):

    pass
class ecoreDiff_DifferenceModel:

    pass
class DifferenceElement:

    pass
class ecoreDiff_EStructuralFeature_Wildcard:

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
class EObject:

    pass
class ecoreDiff_ChangedEObject(EObject):

    pass
class ecoreDiff_AddedEObject(EObject):

    pass
class ecoreDiff_DeletedEObject(EObject):

    pass
class ETypedElement:

    pass
class ecoreDiff_DeletedETypedElement(ETypedElement):

    pass
class ecoreDiff_AddedETypedElement(ETypedElement):

    pass
class ecoreDiff_ChangedETypedElement(ETypedElement):

    pass
class ecoreDiff_EParameter(ETypedElement):

    pass
class ecoreDiff_EClassifier_Wildcard:

    pass
class ecoreDiff_EReference(EStructuralFeature):

    def __init__(self, containment: bool, container: bool, resolveProxies: bool, ecoreDiff_EReference: "ecoreDiff_EClass" = None, ecoreDiff_EReference22: "ecoreDiff_EClass" = None, ecoreDiff_EReference28: "ecoreDiff_EClass" = None, ecoreDiff_EReference111: "ecoreDiff_EReference" = None, ecoreDiff_EReference115: "ecoreDiff_EClass" = None, ecoreDiff_EReference118: set["ecoreDiff_EAttribute"] = None, ecoreDiff_EReference113: "ecoreDiff_EReference" = None, ecoreDiff_EReference161: "ecoreDiff_ChangedEReference" = None):
        self.containment = containment
        self.container = container
        self.resolveProxies = resolveProxies
        self.ecoreDiff_EReference = ecoreDiff_EReference
        self.ecoreDiff_EReference22 = ecoreDiff_EReference22
        self.ecoreDiff_EReference28 = ecoreDiff_EReference28
        self.ecoreDiff_EReference111 = ecoreDiff_EReference111
        self.ecoreDiff_EReference115 = ecoreDiff_EReference115
        self.ecoreDiff_EReference118 = ecoreDiff_EReference118 if ecoreDiff_EReference118 is not None else set()
        self.ecoreDiff_EReference113 = ecoreDiff_EReference113
        self.ecoreDiff_EReference161 = ecoreDiff_EReference161
        
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
    def resolveProxies(self) -> bool:
        return self.__resolveProxies

    @resolveProxies.setter
    def resolveProxies(self, resolveProxies: bool):
        self.__resolveProxies = resolveProxies

    @property
    def ecoreDiff_EReference118(self):
        return self.__ecoreDiff_EReference118

    @ecoreDiff_EReference118.setter
    def ecoreDiff_EReference118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference118", None)
        self.__ecoreDiff_EReference118 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EAttribute119"):
                    opp_val = getattr(item, "ecoreDiff_EAttribute119", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EAttribute119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EAttribute119"):
                    opp_val = getattr(item, "ecoreDiff_EAttribute119", None)
                    
                    setattr(item, "ecoreDiff_EAttribute119", self)
                    

    @property
    def ecoreDiff_EReference22(self):
        return self.__ecoreDiff_EReference22

    @ecoreDiff_EReference22.setter
    def ecoreDiff_EReference22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference22", None)
        self.__ecoreDiff_EReference22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EClass21"):
                opp_val = getattr(old_value, "ecoreDiff_EClass21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass21"):
                opp_val = getattr(value, "ecoreDiff_EClass21", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EClass21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EReference111(self):
        return self.__ecoreDiff_EReference111

    @ecoreDiff_EReference111.setter
    def ecoreDiff_EReference111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference111", None)
        self.__ecoreDiff_EReference111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EReference113"):
                opp_val = getattr(old_value, "ecoreDiff_EReference113", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EReference113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EReference113"):
                opp_val = getattr(value, "ecoreDiff_EReference113", None)
                setattr(value, "ecoreDiff_EReference113", self)

    @property
    def ecoreDiff_EReference28(self):
        return self.__ecoreDiff_EReference28

    @ecoreDiff_EReference28.setter
    def ecoreDiff_EReference28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference28", None)
        self.__ecoreDiff_EReference28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EClass27"):
                opp_val = getattr(old_value, "ecoreDiff_EClass27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass27"):
                opp_val = getattr(value, "ecoreDiff_EClass27", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EClass27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EReference115(self):
        return self.__ecoreDiff_EReference115

    @ecoreDiff_EReference115.setter
    def ecoreDiff_EReference115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference115", None)
        self.__ecoreDiff_EReference115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EClass116"):
                opp_val = getattr(old_value, "ecoreDiff_EClass116", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EClass116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass116"):
                opp_val = getattr(value, "ecoreDiff_EClass116", None)
                setattr(value, "ecoreDiff_EClass116", self)

    @property
    def ecoreDiff_EReference161(self):
        return self.__ecoreDiff_EReference161

    @ecoreDiff_EReference161.setter
    def ecoreDiff_EReference161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference161", None)
        self.__ecoreDiff_EReference161 = value
        
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
    def ecoreDiff_EReference(self):
        return self.__ecoreDiff_EReference

    @ecoreDiff_EReference.setter
    def ecoreDiff_EReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference", None)
        self.__ecoreDiff_EReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EClass19"):
                opp_val = getattr(old_value, "ecoreDiff_EClass19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass19"):
                opp_val = getattr(value, "ecoreDiff_EClass19", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EClass19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EReference113(self):
        return self.__ecoreDiff_EReference113

    @ecoreDiff_EReference113.setter
    def ecoreDiff_EReference113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EReference__ecoreDiff_EReference113", None)
        self.__ecoreDiff_EReference113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EReference111"):
                opp_val = getattr(old_value, "ecoreDiff_EReference111", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EReference111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EReference111"):
                opp_val = getattr(value, "ecoreDiff_EReference111", None)
                setattr(value, "ecoreDiff_EReference111", self)

class ecoreDiff_EStructuralFeature(ETypedElement):

    def __init__(self, changeable: bool, volatile: bool, transient: bool, defaultValueLiteral: str, defaultValue: str, unsettable: bool, derived: bool, ecoreDiff_EStructuralFeature: "ecoreDiff_EClass" = None, 17: "ecoreDiff_EClass" = None, 109: "ecoreDiff_EClass" = None, ecoreDiff_EStructuralFeature158: "ecoreDiff_ChangedEStructuralFeature" = None):
        self.changeable = changeable
        self.volatile = volatile
        self.transient = transient
        self.defaultValueLiteral = defaultValueLiteral
        self.defaultValue = defaultValue
        self.unsettable = unsettable
        self.derived = derived
        self.ecoreDiff_EStructuralFeature = ecoreDiff_EStructuralFeature
        self.17 = 17
        self.109 = 109
        self.ecoreDiff_EStructuralFeature158 = ecoreDiff_EStructuralFeature158
        
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
    def volatile(self) -> bool:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: bool):
        self.__volatile = volatile

    @property
    def ecoreDiff_EStructuralFeature158(self):
        return self.__ecoreDiff_EStructuralFeature158

    @ecoreDiff_EStructuralFeature158.setter
    def ecoreDiff_EStructuralFeature158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EStructuralFeature__ecoreDiff_EStructuralFeature158", None)
        self.__ecoreDiff_EStructuralFeature158 = value
        
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
    def 17(self):
        return self.__17

    @17.setter
    def 17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EStructuralFeature__17", None)
        self.__17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "16"):
                opp_val = getattr(old_value, "16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "16"):
                opp_val = getattr(value, "16", None)
                if opp_val is None:
                    setattr(value, "16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "ecoreDiff_EClass32"):
                opp_val = getattr(old_value, "ecoreDiff_EClass32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass32"):
                opp_val = getattr(value, "ecoreDiff_EClass32", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EClass32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 109(self):
        return self.__109

    @109.setter
    def 109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EStructuralFeature__109", None)
        self.__109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "110"):
                opp_val = getattr(old_value, "110", None)
                if opp_val == self:
                    setattr(old_value, "110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "110"):
                opp_val = getattr(value, "110", None)
                setattr(value, "110", self)

class ecoreDiff_EAttribute(EStructuralFeature):

    def __init__(self, iD: bool, ecoreDiff_EAttribute38: "ecoreDiff_EClass" = None, ecoreDiff_EAttribute: "ecoreDiff_EClass" = None, ecoreDiff_EAttribute25: "ecoreDiff_EClass" = None, ecoreDiff_EAttribute107: "ecoreDiff_EDataType" = None, ecoreDiff_EAttribute119: "ecoreDiff_EReference" = None, ecoreDiff_EAttribute156: "ecoreDiff_ChangedEAttribute" = None):
        self.iD = iD
        self.ecoreDiff_EAttribute38 = ecoreDiff_EAttribute38
        self.ecoreDiff_EAttribute = ecoreDiff_EAttribute
        self.ecoreDiff_EAttribute25 = ecoreDiff_EAttribute25
        self.ecoreDiff_EAttribute107 = ecoreDiff_EAttribute107
        self.ecoreDiff_EAttribute119 = ecoreDiff_EAttribute119
        self.ecoreDiff_EAttribute156 = ecoreDiff_EAttribute156
        
    @property
    def iD(self) -> bool:
        return self.__iD

    @iD.setter
    def iD(self, iD: bool):
        self.__iD = iD

    @property
    def ecoreDiff_EAttribute38(self):
        return self.__ecoreDiff_EAttribute38

    @ecoreDiff_EAttribute38.setter
    def ecoreDiff_EAttribute38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAttribute__ecoreDiff_EAttribute38", None)
        self.__ecoreDiff_EAttribute38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EClass37"):
                opp_val = getattr(old_value, "ecoreDiff_EClass37", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EClass37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass37"):
                opp_val = getattr(value, "ecoreDiff_EClass37", None)
                setattr(value, "ecoreDiff_EClass37", self)

    @property
    def ecoreDiff_EAttribute119(self):
        return self.__ecoreDiff_EAttribute119

    @ecoreDiff_EAttribute119.setter
    def ecoreDiff_EAttribute119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAttribute__ecoreDiff_EAttribute119", None)
        self.__ecoreDiff_EAttribute119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EReference118"):
                opp_val = getattr(old_value, "ecoreDiff_EReference118", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EReference118"):
                opp_val = getattr(value, "ecoreDiff_EReference118", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EReference118", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EAttribute25(self):
        return self.__ecoreDiff_EAttribute25

    @ecoreDiff_EAttribute25.setter
    def ecoreDiff_EAttribute25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAttribute__ecoreDiff_EAttribute25", None)
        self.__ecoreDiff_EAttribute25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EClass24"):
                opp_val = getattr(old_value, "ecoreDiff_EClass24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass24"):
                opp_val = getattr(value, "ecoreDiff_EClass24", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EClass24", set([self]))
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
            if hasattr(old_value, "ecoreDiff_EClass14"):
                opp_val = getattr(old_value, "ecoreDiff_EClass14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass14"):
                opp_val = getattr(value, "ecoreDiff_EClass14", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EClass14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EAttribute156(self):
        return self.__ecoreDiff_EAttribute156

    @ecoreDiff_EAttribute156.setter
    def ecoreDiff_EAttribute156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAttribute__ecoreDiff_EAttribute156", None)
        self.__ecoreDiff_EAttribute156 = value
        
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
    def ecoreDiff_EAttribute107(self):
        return self.__ecoreDiff_EAttribute107

    @ecoreDiff_EAttribute107.setter
    def ecoreDiff_EAttribute107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAttribute__ecoreDiff_EAttribute107", None)
        self.__ecoreDiff_EAttribute107 = value
        
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

class ecoreDiff_EOperation(ETypedElement):

    pass
class ENamedElement:

    pass
class ecoreDiff_ETypedElement(ENamedElement):

    def __init__(self, many: bool, required: str, ordered: bool, unique: bool, lowerBound: int, upperBound: int, ecoreDiff_ETypedElement: "ecoreDiff_EGenericType" = None, ecoreDiff_ETypedElement153: "ecoreDiff_ChangedETypedElement" = None):
        self.many = many
        self.required = required
        self.ordered = ordered
        self.unique = unique
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.ecoreDiff_ETypedElement = ecoreDiff_ETypedElement
        self.ecoreDiff_ETypedElement153 = ecoreDiff_ETypedElement153
        
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
    def required(self) -> str:
        return self.__required

    @required.setter
    def required(self, required: str):
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
    def ecoreDiff_ETypedElement153(self):
        return self.__ecoreDiff_ETypedElement153

    @ecoreDiff_ETypedElement153.setter
    def ecoreDiff_ETypedElement153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_ETypedElement__ecoreDiff_ETypedElement153", None)
        self.__ecoreDiff_ETypedElement153 = value
        
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
            if hasattr(old_value, "ecoreDiff_EGenericType102"):
                opp_val = getattr(old_value, "ecoreDiff_EGenericType102", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EGenericType102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EGenericType102"):
                opp_val = getattr(value, "ecoreDiff_EGenericType102", None)
                setattr(value, "ecoreDiff_EGenericType102", self)

class ecoreDiff_AddedENamedElement(ENamedElement):

    pass
class ecoreDiff_ChangedENamedElement(ENamedElement):

    pass
class ecoreDiff_ETypeParameter(ENamedElement):

    pass
class ecoreDiff_DeletedENamedElement(ENamedElement):

    pass
class ecoreDiff_EEnumLiteral(ENamedElement):

    def __init__(self, value: int, instance: str, literal: str, 122: "ecoreDiff_EEnum" = None, 124: "ecoreDiff_EEnum" = None, ecoreDiff_EEnumLiteral: "ecoreDiff_ChangedEEnumLiteral" = None):
        self.value = value
        self.instance = instance
        self.literal = literal
        self.122 = 122
        self.124 = 124
        self.ecoreDiff_EEnumLiteral = ecoreDiff_EEnumLiteral
        
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
    def 122(self):
        return self.__122

    @122.setter
    def 122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EEnumLiteral__122", None)
        self.__122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "121"):
                opp_val = getattr(old_value, "121", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "121"):
                opp_val = getattr(value, "121", None)
                if opp_val is None:
                    setattr(value, "121", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 124(self):
        return self.__124

    @124.setter
    def 124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EEnumLiteral__124", None)
        self.__124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "125"):
                opp_val = getattr(old_value, "125", None)
                if opp_val == self:
                    setattr(old_value, "125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "125"):
                opp_val = getattr(value, "125", None)
                setattr(value, "125", self)

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

class ecoreDiff_EPackage(ENamedElement):

    def __init__(self, nsURI: str, nsPrefix: str, 58: "ecoreDiff_EPackage" = None, 57: "ecoreDiff_EPackage" = None, 46: "ecoreDiff_EClassifier" = None, 49: "ecoreDiff_EFactory" = None, 54: "ecoreDiff_EPackage" = None, 53: set["ecoreDiff_EPackage"] = None, 60: set["ecoreDiff_EClassifier"] = None, 64: "ecoreDiff_EFactory" = None, ecoreDiff_EPackage: "ecoreDiff_ChangedEPackage" = None):
        self.nsURI = nsURI
        self.nsPrefix = nsPrefix
        self.58 = 58
        self.57 = 57
        self.46 = 46
        self.49 = 49
        self.54 = 54
        self.53 = 53 if 53 is not None else set()
        self.60 = 60 if 60 is not None else set()
        self.64 = 64
        self.ecoreDiff_EPackage = ecoreDiff_EPackage
        
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
    def 58(self):
        return self.__58

    @58.setter
    def 58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__58", None)
        self.__58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "57"):
                opp_val = getattr(old_value, "57", None)
                if opp_val == self:
                    setattr(old_value, "57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "57"):
                opp_val = getattr(value, "57", None)
                setattr(value, "57", self)

    @property
    def 49(self):
        return self.__49

    @49.setter
    def 49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__49", None)
        self.__49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "50"):
                opp_val = getattr(old_value, "50", None)
                if opp_val == self:
                    setattr(old_value, "50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "50"):
                opp_val = getattr(value, "50", None)
                setattr(value, "50", self)

    @property
    def 57(self):
        return self.__57

    @57.setter
    def 57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__57", None)
        self.__57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "58"):
                opp_val = getattr(old_value, "58", None)
                if opp_val == self:
                    setattr(old_value, "58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "58"):
                opp_val = getattr(value, "58", None)
                setattr(value, "58", self)

    @property
    def 53(self):
        return self.__53

    @53.setter
    def 53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__53", None)
        self.__53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "54"):
                    opp_val = getattr(item, "54", None)
                    
                    if opp_val == self:
                        setattr(item, "54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "54"):
                    opp_val = getattr(item, "54", None)
                    
                    setattr(item, "54", self)
                    

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

    @property
    def 60(self):
        return self.__60

    @60.setter
    def 60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__60", None)
        self.__60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "61"):
                    opp_val = getattr(item, "61", None)
                    
                    if opp_val == self:
                        setattr(item, "61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "61"):
                    opp_val = getattr(item, "61", None)
                    
                    setattr(item, "61", self)
                    

    @property
    def 46(self):
        return self.__46

    @46.setter
    def 46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__46", None)
        self.__46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "45"):
                opp_val = getattr(old_value, "45", None)
                if opp_val == self:
                    setattr(old_value, "45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "45"):
                opp_val = getattr(value, "45", None)
                setattr(value, "45", self)

    @property
    def 54(self):
        return self.__54

    @54.setter
    def 54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__54", None)
        self.__54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "53"):
                opp_val = getattr(old_value, "53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "53"):
                opp_val = getattr(value, "53", None)
                if opp_val is None:
                    setattr(value, "53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 64(self):
        return self.__64

    @64.setter
    def 64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EPackage__64", None)
        self.__64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "63"):
                opp_val = getattr(old_value, "63", None)
                if opp_val == self:
                    setattr(old_value, "63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "63"):
                opp_val = getattr(value, "63", None)
                setattr(value, "63", self)

class ecoreDiff_EClassifier(ENamedElement):

    def __init__(self, instanceClassName: str, instanceClass: str, defaultValue: str, instanceTypeName: str, 45: "ecoreDiff_EPackage" = None, ecoreDiff_EClassifier: set["ecoreDiff_ETypeParameter"] = None, ecoreDiff_EClassifier76: "ecoreDiff_EGenericType" = None, ecoreDiff_EClassifier85: "ecoreDiff_EGenericType" = None, ecoreDiff_EClassifier94: "ecoreDiff_EOperation" = None, 61: "ecoreDiff_EPackage" = None, ecoreDiff_EClassifier139: "ecoreDiff_ChangedEClassifier" = None):
        self.instanceClassName = instanceClassName
        self.instanceClass = instanceClass
        self.defaultValue = defaultValue
        self.instanceTypeName = instanceTypeName
        self.45 = 45
        self.ecoreDiff_EClassifier = ecoreDiff_EClassifier if ecoreDiff_EClassifier is not None else set()
        self.ecoreDiff_EClassifier76 = ecoreDiff_EClassifier76
        self.ecoreDiff_EClassifier85 = ecoreDiff_EClassifier85
        self.ecoreDiff_EClassifier94 = ecoreDiff_EClassifier94
        self.61 = 61
        self.ecoreDiff_EClassifier139 = ecoreDiff_EClassifier139
        
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
    def ecoreDiff_EClassifier85(self):
        return self.__ecoreDiff_EClassifier85

    @ecoreDiff_EClassifier85.setter
    def ecoreDiff_EClassifier85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClassifier__ecoreDiff_EClassifier85", None)
        self.__ecoreDiff_EClassifier85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EGenericType84"):
                opp_val = getattr(old_value, "ecoreDiff_EGenericType84", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EGenericType84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EGenericType84"):
                opp_val = getattr(value, "ecoreDiff_EGenericType84", None)
                setattr(value, "ecoreDiff_EGenericType84", self)

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
    def 45(self):
        return self.__45

    @45.setter
    def 45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClassifier__45", None)
        self.__45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "46"):
                opp_val = getattr(old_value, "46", None)
                if opp_val == self:
                    setattr(old_value, "46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "46"):
                opp_val = getattr(value, "46", None)
                setattr(value, "46", self)

    @property
    def ecoreDiff_EClassifier94(self):
        return self.__ecoreDiff_EClassifier94

    @ecoreDiff_EClassifier94.setter
    def ecoreDiff_EClassifier94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClassifier__ecoreDiff_EClassifier94", None)
        self.__ecoreDiff_EClassifier94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EOperation93"):
                opp_val = getattr(old_value, "ecoreDiff_EOperation93", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EOperation93"):
                opp_val = getattr(value, "ecoreDiff_EOperation93", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EOperation93", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 61(self):
        return self.__61

    @61.setter
    def 61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClassifier__61", None)
        self.__61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "60"):
                opp_val = getattr(old_value, "60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "60"):
                opp_val = getattr(value, "60", None)
                if opp_val is None:
                    setattr(value, "60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EClassifier139(self):
        return self.__ecoreDiff_EClassifier139

    @ecoreDiff_EClassifier139.setter
    def ecoreDiff_EClassifier139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClassifier__ecoreDiff_EClassifier139", None)
        self.__ecoreDiff_EClassifier139 = value
        
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
    def ecoreDiff_EClassifier76(self):
        return self.__ecoreDiff_EClassifier76

    @ecoreDiff_EClassifier76.setter
    def ecoreDiff_EClassifier76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClassifier__ecoreDiff_EClassifier76", None)
        self.__ecoreDiff_EClassifier76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EGenericType75"):
                opp_val = getattr(old_value, "ecoreDiff_EGenericType75", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EGenericType75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EGenericType75"):
                opp_val = getattr(value, "ecoreDiff_EGenericType75", None)
                setattr(value, "ecoreDiff_EGenericType75", self)

class ecoreDiff_EGenericType(EObject):

    pass
class EModelElement:

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
class ecoreDiff_AddedEModelElement(EModelElement):

    pass
class ecoreDiff_EFactory(EModelElement):

    pass
class ecoreDiff_EAnnotation(EModelElement):

    def __init__(self, source: str, ecoreDiff_EAnnotation: set["ecoreDiff_EStringToStringMapEntry"] = None, : "ecoreDiff_EModelElement" = None, ecoreDiff_EAnnotation4: set["ecoreDiff_EObject"] = None, ecoreDiff_EAnnotation6: set["ecoreDiff_EObject"] = None, 128: "ecoreDiff_EModelElement" = None, ecoreDiff_EAnnotation131: "ecoreDiff_ChangedEAnnotation" = None):
        self.source = source
        self.ecoreDiff_EAnnotation = ecoreDiff_EAnnotation if ecoreDiff_EAnnotation is not None else set()
        self. = 
        self.ecoreDiff_EAnnotation4 = ecoreDiff_EAnnotation4 if ecoreDiff_EAnnotation4 is not None else set()
        self.ecoreDiff_EAnnotation6 = ecoreDiff_EAnnotation6 if ecoreDiff_EAnnotation6 is not None else set()
        self.128 = 128
        self.ecoreDiff_EAnnotation131 = ecoreDiff_EAnnotation131
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def ecoreDiff_EAnnotation131(self):
        return self.__ecoreDiff_EAnnotation131

    @ecoreDiff_EAnnotation131.setter
    def ecoreDiff_EAnnotation131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAnnotation__ecoreDiff_EAnnotation131", None)
        self.__ecoreDiff_EAnnotation131 = value
        
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
    def 128(self):
        return self.__128

    @128.setter
    def 128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAnnotation__128", None)
        self.__128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "127"):
                opp_val = getattr(old_value, "127", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "127"):
                opp_val = getattr(value, "127", None)
                if opp_val is None:
                    setattr(value, "127", set([self]))
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
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EAnnotation__", None)
        self.__ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "2"):
                opp_val = getattr(old_value, "2", None)
                if opp_val == self:
                    setattr(old_value, "2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "2"):
                opp_val = getattr(value, "2", None)
                setattr(value, "2", self)

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
                    

class EClassifier:

    pass
class ecoreDiff_AddedEClassifier(EClassifier):

    pass
class ecoreDiff_DeletedEClassifier(EClassifier):

    pass
class ecoreDiff_ChangedEClassifier(EClassifier):

    pass
class ecoreDiff_EDataType(EClassifier):

    def __init__(self, serializable: bool, ecoreDiff_EDataType: "ecoreDiff_EAttribute" = None, ecoreDiff_EDataType144: "ecoreDiff_ChangedEDataType" = None):
        self.serializable = serializable
        self.ecoreDiff_EDataType = ecoreDiff_EDataType
        self.ecoreDiff_EDataType144 = ecoreDiff_EDataType144
        
    @property
    def serializable(self) -> bool:
        return self.__serializable

    @serializable.setter
    def serializable(self, serializable: bool):
        self.__serializable = serializable

    @property
    def ecoreDiff_EDataType144(self):
        return self.__ecoreDiff_EDataType144

    @ecoreDiff_EDataType144.setter
    def ecoreDiff_EDataType144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EDataType__ecoreDiff_EDataType144", None)
        self.__ecoreDiff_EDataType144 = value
        
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
            if hasattr(old_value, "ecoreDiff_EAttribute107"):
                opp_val = getattr(old_value, "ecoreDiff_EAttribute107", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EAttribute107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EAttribute107"):
                opp_val = getattr(value, "ecoreDiff_EAttribute107", None)
                setattr(value, "ecoreDiff_EAttribute107", self)

class ecoreDiff_EClass(EClassifier):

    def __init__(self, abstract: bool, interface: bool, ecoreDiff_EClass: "ecoreDiff_EClass" = None, ecoreDiff_EClass8: set["ecoreDiff_EClass"] = None, ecoreDiff_EClass30: set["ecoreDiff_EOperation"] = None, ecoreDiff_EClass32: set["ecoreDiff_EStructuralFeature"] = None, ecoreDiff_EClass35: "ecoreDiff_EClass" = None, ecoreDiff_EClass33: set["ecoreDiff_EClass"] = None, ecoreDiff_EClass37: "ecoreDiff_EAttribute" = None, ecoreDiff_EClass40: set["ecoreDiff_EGenericType"] = None, ecoreDiff_EClass42: set["ecoreDiff_EGenericType"] = None, 11: set["ecoreDiff_EOperation"] = None, ecoreDiff_EClass14: set["ecoreDiff_EAttribute"] = None, 16: set["ecoreDiff_EStructuralFeature"] = None, ecoreDiff_EClass19: set["ecoreDiff_EReference"] = None, ecoreDiff_EClass21: set["ecoreDiff_EReference"] = None, ecoreDiff_EClass24: set["ecoreDiff_EAttribute"] = None, ecoreDiff_EClass27: set["ecoreDiff_EReference"] = None, 100: "ecoreDiff_EOperation" = None, ecoreDiff_EClass116: "ecoreDiff_EReference" = None, 110: "ecoreDiff_EStructuralFeature" = None, ecoreDiff_EClass137: "ecoreDiff_ChangedEClass" = None):
        self.abstract = abstract
        self.interface = interface
        self.ecoreDiff_EClass = ecoreDiff_EClass
        self.ecoreDiff_EClass8 = ecoreDiff_EClass8 if ecoreDiff_EClass8 is not None else set()
        self.ecoreDiff_EClass30 = ecoreDiff_EClass30 if ecoreDiff_EClass30 is not None else set()
        self.ecoreDiff_EClass32 = ecoreDiff_EClass32 if ecoreDiff_EClass32 is not None else set()
        self.ecoreDiff_EClass35 = ecoreDiff_EClass35
        self.ecoreDiff_EClass33 = ecoreDiff_EClass33 if ecoreDiff_EClass33 is not None else set()
        self.ecoreDiff_EClass37 = ecoreDiff_EClass37
        self.ecoreDiff_EClass40 = ecoreDiff_EClass40 if ecoreDiff_EClass40 is not None else set()
        self.ecoreDiff_EClass42 = ecoreDiff_EClass42 if ecoreDiff_EClass42 is not None else set()
        self.11 = 11 if 11 is not None else set()
        self.ecoreDiff_EClass14 = ecoreDiff_EClass14 if ecoreDiff_EClass14 is not None else set()
        self.16 = 16 if 16 is not None else set()
        self.ecoreDiff_EClass19 = ecoreDiff_EClass19 if ecoreDiff_EClass19 is not None else set()
        self.ecoreDiff_EClass21 = ecoreDiff_EClass21 if ecoreDiff_EClass21 is not None else set()
        self.ecoreDiff_EClass24 = ecoreDiff_EClass24 if ecoreDiff_EClass24 is not None else set()
        self.ecoreDiff_EClass27 = ecoreDiff_EClass27 if ecoreDiff_EClass27 is not None else set()
        self.100 = 100
        self.ecoreDiff_EClass116 = ecoreDiff_EClass116
        self.110 = 110
        self.ecoreDiff_EClass137 = ecoreDiff_EClass137
        
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
    def ecoreDiff_EClass27(self):
        return self.__ecoreDiff_EClass27

    @ecoreDiff_EClass27.setter
    def ecoreDiff_EClass27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass27", None)
        self.__ecoreDiff_EClass27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EReference28"):
                    opp_val = getattr(item, "ecoreDiff_EReference28", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EReference28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EReference28"):
                    opp_val = getattr(item, "ecoreDiff_EReference28", None)
                    
                    setattr(item, "ecoreDiff_EReference28", self)
                    

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
    def 110(self):
        return self.__110

    @110.setter
    def 110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__110", None)
        self.__110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "109"):
                opp_val = getattr(old_value, "109", None)
                if opp_val == self:
                    setattr(old_value, "109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "109"):
                opp_val = getattr(value, "109", None)
                setattr(value, "109", self)

    @property
    def ecoreDiff_EClass24(self):
        return self.__ecoreDiff_EClass24

    @ecoreDiff_EClass24.setter
    def ecoreDiff_EClass24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass24", None)
        self.__ecoreDiff_EClass24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EAttribute25"):
                    opp_val = getattr(item, "ecoreDiff_EAttribute25", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EAttribute25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EAttribute25"):
                    opp_val = getattr(item, "ecoreDiff_EAttribute25", None)
                    
                    setattr(item, "ecoreDiff_EAttribute25", self)
                    

    @property
    def ecoreDiff_EClass32(self):
        return self.__ecoreDiff_EClass32

    @ecoreDiff_EClass32.setter
    def ecoreDiff_EClass32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass32", None)
        self.__ecoreDiff_EClass32 = value if value is not None else set()
        
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
    def ecoreDiff_EClass14(self):
        return self.__ecoreDiff_EClass14

    @ecoreDiff_EClass14.setter
    def ecoreDiff_EClass14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass14", None)
        self.__ecoreDiff_EClass14 = value if value is not None else set()
        
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
    def ecoreDiff_EClass33(self):
        return self.__ecoreDiff_EClass33

    @ecoreDiff_EClass33.setter
    def ecoreDiff_EClass33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass33", None)
        self.__ecoreDiff_EClass33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EClass35"):
                    opp_val = getattr(item, "ecoreDiff_EClass35", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EClass35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EClass35"):
                    opp_val = getattr(item, "ecoreDiff_EClass35", None)
                    
                    setattr(item, "ecoreDiff_EClass35", self)
                    

    @property
    def ecoreDiff_EClass42(self):
        return self.__ecoreDiff_EClass42

    @ecoreDiff_EClass42.setter
    def ecoreDiff_EClass42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass42", None)
        self.__ecoreDiff_EClass42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EGenericType43"):
                    opp_val = getattr(item, "ecoreDiff_EGenericType43", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EGenericType43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EGenericType43"):
                    opp_val = getattr(item, "ecoreDiff_EGenericType43", None)
                    
                    setattr(item, "ecoreDiff_EGenericType43", self)
                    

    @property
    def 100(self):
        return self.__100

    @100.setter
    def 100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__100", None)
        self.__100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "99"):
                opp_val = getattr(old_value, "99", None)
                if opp_val == self:
                    setattr(old_value, "99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "99"):
                opp_val = getattr(value, "99", None)
                setattr(value, "99", self)

    @property
    def ecoreDiff_EClass137(self):
        return self.__ecoreDiff_EClass137

    @ecoreDiff_EClass137.setter
    def ecoreDiff_EClass137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass137", None)
        self.__ecoreDiff_EClass137 = value
        
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
    def 16(self):
        return self.__16

    @16.setter
    def 16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__16", None)
        self.__16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "17"):
                    opp_val = getattr(item, "17", None)
                    
                    if opp_val == self:
                        setattr(item, "17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "17"):
                    opp_val = getattr(item, "17", None)
                    
                    setattr(item, "17", self)
                    

    @property
    def ecoreDiff_EClass30(self):
        return self.__ecoreDiff_EClass30

    @ecoreDiff_EClass30.setter
    def ecoreDiff_EClass30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass30", None)
        self.__ecoreDiff_EClass30 = value if value is not None else set()
        
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
    def ecoreDiff_EClass19(self):
        return self.__ecoreDiff_EClass19

    @ecoreDiff_EClass19.setter
    def ecoreDiff_EClass19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass19", None)
        self.__ecoreDiff_EClass19 = value if value is not None else set()
        
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
    def ecoreDiff_EClass37(self):
        return self.__ecoreDiff_EClass37

    @ecoreDiff_EClass37.setter
    def ecoreDiff_EClass37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass37", None)
        self.__ecoreDiff_EClass37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EAttribute38"):
                opp_val = getattr(old_value, "ecoreDiff_EAttribute38", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EAttribute38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EAttribute38"):
                opp_val = getattr(value, "ecoreDiff_EAttribute38", None)
                setattr(value, "ecoreDiff_EAttribute38", self)

    @property
    def ecoreDiff_EClass21(self):
        return self.__ecoreDiff_EClass21

    @ecoreDiff_EClass21.setter
    def ecoreDiff_EClass21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass21", None)
        self.__ecoreDiff_EClass21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreDiff_EReference22"):
                    opp_val = getattr(item, "ecoreDiff_EReference22", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreDiff_EReference22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreDiff_EReference22"):
                    opp_val = getattr(item, "ecoreDiff_EReference22", None)
                    
                    setattr(item, "ecoreDiff_EReference22", self)
                    

    @property
    def ecoreDiff_EClass40(self):
        return self.__ecoreDiff_EClass40

    @ecoreDiff_EClass40.setter
    def ecoreDiff_EClass40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass40", None)
        self.__ecoreDiff_EClass40 = value if value is not None else set()
        
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
    def 11(self):
        return self.__11

    @11.setter
    def 11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__11", None)
        self.__11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "12"):
                    opp_val = getattr(item, "12", None)
                    
                    if opp_val == self:
                        setattr(item, "12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "12"):
                    opp_val = getattr(item, "12", None)
                    
                    setattr(item, "12", self)
                    

    @property
    def ecoreDiff_EClass35(self):
        return self.__ecoreDiff_EClass35

    @ecoreDiff_EClass35.setter
    def ecoreDiff_EClass35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass35", None)
        self.__ecoreDiff_EClass35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EClass33"):
                opp_val = getattr(old_value, "ecoreDiff_EClass33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EClass33"):
                opp_val = getattr(value, "ecoreDiff_EClass33", None)
                if opp_val is None:
                    setattr(value, "ecoreDiff_EClass33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecoreDiff_EClass116(self):
        return self.__ecoreDiff_EClass116

    @ecoreDiff_EClass116.setter
    def ecoreDiff_EClass116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EClass__ecoreDiff_EClass116", None)
        self.__ecoreDiff_EClass116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreDiff_EReference115"):
                opp_val = getattr(old_value, "ecoreDiff_EReference115", None)
                if opp_val == self:
                    setattr(old_value, "ecoreDiff_EReference115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreDiff_EReference115"):
                opp_val = getattr(value, "ecoreDiff_EReference115", None)
                setattr(value, "ecoreDiff_EReference115", self)

class ecoreDiff_EObject:

    pass
class ecoreDiff_EModelElement(DifferenceElement, EObject):

    pass
class ecoreDiff_EStringToStringMapEntry:

    def __init__(self, key: str, value: str, ecoreDiff_EStringToStringMapEntry: "ecoreDiff_EAnnotation" = None, ecoreDiff_EStringToStringMapEntry133: "ecoreDiff_ChangedEStringToStringMapEntry" = None):
        self.key = key
        self.value = value
        self.ecoreDiff_EStringToStringMapEntry = ecoreDiff_EStringToStringMapEntry
        self.ecoreDiff_EStringToStringMapEntry133 = ecoreDiff_EStringToStringMapEntry133
        
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
    def ecoreDiff_EStringToStringMapEntry133(self):
        return self.__ecoreDiff_EStringToStringMapEntry133

    @ecoreDiff_EStringToStringMapEntry133.setter
    def ecoreDiff_EStringToStringMapEntry133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreDiff_EStringToStringMapEntry__ecoreDiff_EStringToStringMapEntry133", None)
        self.__ecoreDiff_EStringToStringMapEntry133 = value
        
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
