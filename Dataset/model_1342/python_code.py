from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class oclinEcoreCST_ReferenceRef(ABC):

    pass
class oclinEcoreCST_EClassifier:

    pass
class oclinEcoreCST_EClass:

    pass
class TypedElementCS:

    pass
class oclinEcoreCST_ParameterCS(TypedElementCS):

    pass
class oclinEcoreCST_ModelElementCS(ABC):

    pass
class oclinEcoreCST_EReference:

    pass
class ReferenceRef:

    pass
class oclinEcoreCST_ReferenceCSRef(ReferenceRef):

    pass
class oclinEcoreCST_EReferenceRef(ReferenceRef):

    pass
class oclinEcoreCST_EDataType:

    pass
class oclinEcoreCST_EAttribute:

    pass
class oclinEcoreCST_ImportCS:

    def __init__(self, importedNamespace: str, oclinEcoreCST_ImportCS: "oclinEcoreCST_DocumentCS" = None):
        self.importedNamespace = importedNamespace
        self.oclinEcoreCST_ImportCS = oclinEcoreCST_ImportCS
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def oclinEcoreCST_ImportCS(self):
        return self.__oclinEcoreCST_ImportCS

    @oclinEcoreCST_ImportCS.setter
    def oclinEcoreCST_ImportCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclinEcoreCST_ImportCS__oclinEcoreCST_ImportCS", None)
        self.__oclinEcoreCST_ImportCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclinEcoreCST_DocumentCS"):
                opp_val = getattr(old_value, "oclinEcoreCST_DocumentCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclinEcoreCST_DocumentCS"):
                opp_val = getattr(value, "oclinEcoreCST_DocumentCS", None)
                if opp_val is None:
                    setattr(value, "oclinEcoreCST_DocumentCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class oclinEcoreCST_DocumentCS:

    pass
class DataTypeRef:

    pass
class oclinEcoreCST_EDataTypeRef(DataTypeRef):

    pass
class oclinEcoreCST_DataTypeCSRef(DataTypeRef):

    pass
class DataTypeOrEnumCS:

    pass
class oclinEcoreCST_EnumCS(DataTypeOrEnumCS):

    pass
class oclinEcoreCST_DataTypeCS(DataTypeOrEnumCS):

    pass
class oclinEcoreCST_OclExpressionCS:

    pass
class oclinEcoreCST_ClassifierRef(ABC):

    pass
class NamedElementCS:

    pass
class oclinEcoreCST_TypedElementCS(NamedElementCS):

    def __init__(self, lower: int, multiplicity: str, qualifiers: str, upper: int, oclinEcoreCST_TypedElementCS: "oclinEcoreCST_ClassifierRef" = None):
        self.lower = lower
        self.multiplicity = multiplicity
        self.qualifiers = qualifiers
        self.upper = upper
        self.oclinEcoreCST_TypedElementCS = oclinEcoreCST_TypedElementCS
        
    @property
    def multiplicity(self) -> str:
        return self.__multiplicity

    @multiplicity.setter
    def multiplicity(self, multiplicity: str):
        self.__multiplicity = multiplicity

    @property
    def qualifiers(self) -> str:
        return self.__qualifiers

    @qualifiers.setter
    def qualifiers(self, qualifiers: str):
        self.__qualifiers = qualifiers

    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def oclinEcoreCST_TypedElementCS(self):
        return self.__oclinEcoreCST_TypedElementCS

    @oclinEcoreCST_TypedElementCS.setter
    def oclinEcoreCST_TypedElementCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclinEcoreCST_TypedElementCS__oclinEcoreCST_TypedElementCS", None)
        self.__oclinEcoreCST_TypedElementCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclinEcoreCST_ClassifierRef53"):
                opp_val = getattr(old_value, "oclinEcoreCST_ClassifierRef53", None)
                if opp_val == self:
                    setattr(old_value, "oclinEcoreCST_ClassifierRef53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclinEcoreCST_ClassifierRef53"):
                opp_val = getattr(value, "oclinEcoreCST_ClassifierRef53", None)
                setattr(value, "oclinEcoreCST_ClassifierRef53", self)

class oclinEcoreCST_PackageCS(NamedElementCS):

    pass
class oclinEcoreCST_TypeParameterCS(NamedElementCS):

    pass
class oclinEcoreCST_EnumLiteralCS(NamedElementCS):

    def __init__(self, value: int, oclinEcoreCST_EnumLiteralCS: "oclinEcoreCST_EnumCS" = None):
        self.value = value
        self.oclinEcoreCST_EnumLiteralCS = oclinEcoreCST_EnumLiteralCS
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def oclinEcoreCST_EnumLiteralCS(self):
        return self.__oclinEcoreCST_EnumLiteralCS

    @oclinEcoreCST_EnumLiteralCS.setter
    def oclinEcoreCST_EnumLiteralCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclinEcoreCST_EnumLiteralCS__oclinEcoreCST_EnumLiteralCS", None)
        self.__oclinEcoreCST_EnumLiteralCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclinEcoreCST_EnumCS"):
                opp_val = getattr(old_value, "oclinEcoreCST_EnumCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclinEcoreCST_EnumCS"):
                opp_val = getattr(value, "oclinEcoreCST_EnumCS", None)
                if opp_val is None:
                    setattr(value, "oclinEcoreCST_EnumCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class oclinEcoreCST_ClassifierCS(NamedElementCS):

    def __init__(self, instanceClassName: str, qualifiers: str, oclinEcoreCST_ClassifierCS: set["oclinEcoreCST_ConstraintCS"] = None, oclinEcoreCST_ClassifierCS11: set["oclinEcoreCST_TypeParameterCS"] = None, oclinEcoreCST_ClassifierCS13: "oclinEcoreCST_ClassifierCSRef" = None, oclinEcoreCST_ClassifierCS40: "oclinEcoreCST_PackageCS" = None):
        self.instanceClassName = instanceClassName
        self.qualifiers = qualifiers
        self.oclinEcoreCST_ClassifierCS = oclinEcoreCST_ClassifierCS if oclinEcoreCST_ClassifierCS is not None else set()
        self.oclinEcoreCST_ClassifierCS11 = oclinEcoreCST_ClassifierCS11 if oclinEcoreCST_ClassifierCS11 is not None else set()
        self.oclinEcoreCST_ClassifierCS13 = oclinEcoreCST_ClassifierCS13
        self.oclinEcoreCST_ClassifierCS40 = oclinEcoreCST_ClassifierCS40
        
    @property
    def qualifiers(self) -> str:
        return self.__qualifiers

    @qualifiers.setter
    def qualifiers(self, qualifiers: str):
        self.__qualifiers = qualifiers

    @property
    def instanceClassName(self) -> str:
        return self.__instanceClassName

    @instanceClassName.setter
    def instanceClassName(self, instanceClassName: str):
        self.__instanceClassName = instanceClassName

    @property
    def oclinEcoreCST_ClassifierCS11(self):
        return self.__oclinEcoreCST_ClassifierCS11

    @oclinEcoreCST_ClassifierCS11.setter
    def oclinEcoreCST_ClassifierCS11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclinEcoreCST_ClassifierCS__oclinEcoreCST_ClassifierCS11", None)
        self.__oclinEcoreCST_ClassifierCS11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oclinEcoreCST_TypeParameterCS"):
                    opp_val = getattr(item, "oclinEcoreCST_TypeParameterCS", None)
                    
                    if opp_val == self:
                        setattr(item, "oclinEcoreCST_TypeParameterCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oclinEcoreCST_TypeParameterCS"):
                    opp_val = getattr(item, "oclinEcoreCST_TypeParameterCS", None)
                    
                    setattr(item, "oclinEcoreCST_TypeParameterCS", self)
                    

    @property
    def oclinEcoreCST_ClassifierCS(self):
        return self.__oclinEcoreCST_ClassifierCS

    @oclinEcoreCST_ClassifierCS.setter
    def oclinEcoreCST_ClassifierCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclinEcoreCST_ClassifierCS__oclinEcoreCST_ClassifierCS", None)
        self.__oclinEcoreCST_ClassifierCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oclinEcoreCST_ConstraintCS"):
                    opp_val = getattr(item, "oclinEcoreCST_ConstraintCS", None)
                    
                    if opp_val == self:
                        setattr(item, "oclinEcoreCST_ConstraintCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oclinEcoreCST_ConstraintCS"):
                    opp_val = getattr(item, "oclinEcoreCST_ConstraintCS", None)
                    
                    setattr(item, "oclinEcoreCST_ConstraintCS", self)
                    

    @property
    def oclinEcoreCST_ClassifierCS40(self):
        return self.__oclinEcoreCST_ClassifierCS40

    @oclinEcoreCST_ClassifierCS40.setter
    def oclinEcoreCST_ClassifierCS40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclinEcoreCST_ClassifierCS__oclinEcoreCST_ClassifierCS40", None)
        self.__oclinEcoreCST_ClassifierCS40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclinEcoreCST_PackageCS39"):
                opp_val = getattr(old_value, "oclinEcoreCST_PackageCS39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclinEcoreCST_PackageCS39"):
                opp_val = getattr(value, "oclinEcoreCST_PackageCS39", None)
                if opp_val is None:
                    setattr(value, "oclinEcoreCST_PackageCS39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oclinEcoreCST_ClassifierCS13(self):
        return self.__oclinEcoreCST_ClassifierCS13

    @oclinEcoreCST_ClassifierCS13.setter
    def oclinEcoreCST_ClassifierCS13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclinEcoreCST_ClassifierCS__oclinEcoreCST_ClassifierCS13", None)
        self.__oclinEcoreCST_ClassifierCS13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclinEcoreCST_ClassifierCSRef"):
                opp_val = getattr(old_value, "oclinEcoreCST_ClassifierCSRef", None)
                if opp_val == self:
                    setattr(old_value, "oclinEcoreCST_ClassifierCSRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclinEcoreCST_ClassifierCSRef"):
                opp_val = getattr(value, "oclinEcoreCST_ClassifierCSRef", None)
                setattr(value, "oclinEcoreCST_ClassifierCSRef", self)

class oclinEcoreCST_ConstraintCS(NamedElementCS):

    def __init__(self, stereotype: str, oclinEcoreCST_ConstraintCS: "oclinEcoreCST_ClassifierCS" = None, oclinEcoreCST_ConstraintCS15: "oclinEcoreCST_OclExpressionCS" = None, oclinEcoreCST_ConstraintCS30: "oclinEcoreCST_OperationCS" = None, oclinEcoreCST_ConstraintCS51: "oclinEcoreCST_StructuralFeatureCS" = None):
        self.stereotype = stereotype
        self.oclinEcoreCST_ConstraintCS = oclinEcoreCST_ConstraintCS
        self.oclinEcoreCST_ConstraintCS15 = oclinEcoreCST_ConstraintCS15
        self.oclinEcoreCST_ConstraintCS30 = oclinEcoreCST_ConstraintCS30
        self.oclinEcoreCST_ConstraintCS51 = oclinEcoreCST_ConstraintCS51
        
    @property
    def stereotype(self) -> str:
        return self.__stereotype

    @stereotype.setter
    def stereotype(self, stereotype: str):
        self.__stereotype = stereotype

    @property
    def oclinEcoreCST_ConstraintCS15(self):
        return self.__oclinEcoreCST_ConstraintCS15

    @oclinEcoreCST_ConstraintCS15.setter
    def oclinEcoreCST_ConstraintCS15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclinEcoreCST_ConstraintCS__oclinEcoreCST_ConstraintCS15", None)
        self.__oclinEcoreCST_ConstraintCS15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclinEcoreCST_OclExpressionCS"):
                opp_val = getattr(old_value, "oclinEcoreCST_OclExpressionCS", None)
                if opp_val == self:
                    setattr(old_value, "oclinEcoreCST_OclExpressionCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclinEcoreCST_OclExpressionCS"):
                opp_val = getattr(value, "oclinEcoreCST_OclExpressionCS", None)
                setattr(value, "oclinEcoreCST_OclExpressionCS", self)

    @property
    def oclinEcoreCST_ConstraintCS51(self):
        return self.__oclinEcoreCST_ConstraintCS51

    @oclinEcoreCST_ConstraintCS51.setter
    def oclinEcoreCST_ConstraintCS51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclinEcoreCST_ConstraintCS__oclinEcoreCST_ConstraintCS51", None)
        self.__oclinEcoreCST_ConstraintCS51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclinEcoreCST_StructuralFeatureCS50"):
                opp_val = getattr(old_value, "oclinEcoreCST_StructuralFeatureCS50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclinEcoreCST_StructuralFeatureCS50"):
                opp_val = getattr(value, "oclinEcoreCST_StructuralFeatureCS50", None)
                if opp_val is None:
                    setattr(value, "oclinEcoreCST_StructuralFeatureCS50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oclinEcoreCST_ConstraintCS(self):
        return self.__oclinEcoreCST_ConstraintCS

    @oclinEcoreCST_ConstraintCS.setter
    def oclinEcoreCST_ConstraintCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclinEcoreCST_ConstraintCS__oclinEcoreCST_ConstraintCS", None)
        self.__oclinEcoreCST_ConstraintCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclinEcoreCST_ClassifierCS"):
                opp_val = getattr(old_value, "oclinEcoreCST_ClassifierCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclinEcoreCST_ClassifierCS"):
                opp_val = getattr(value, "oclinEcoreCST_ClassifierCS", None)
                if opp_val is None:
                    setattr(value, "oclinEcoreCST_ClassifierCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oclinEcoreCST_ConstraintCS30(self):
        return self.__oclinEcoreCST_ConstraintCS30

    @oclinEcoreCST_ConstraintCS30.setter
    def oclinEcoreCST_ConstraintCS30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclinEcoreCST_ConstraintCS__oclinEcoreCST_ConstraintCS30", None)
        self.__oclinEcoreCST_ConstraintCS30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclinEcoreCST_OperationCS29"):
                opp_val = getattr(old_value, "oclinEcoreCST_OperationCS29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclinEcoreCST_OperationCS29"):
                opp_val = getattr(value, "oclinEcoreCST_OperationCS29", None)
                if opp_val is None:
                    setattr(value, "oclinEcoreCST_OperationCS29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ClassRef:

    pass
class oclinEcoreCST_EClassRef(ClassRef):

    pass
class oclinEcoreCST_ClassCSRef(ClassRef):

    pass
class ClassifierRef:

    pass
class oclinEcoreCST_EClassifierRef(ClassifierRef):

    pass
class oclinEcoreCST_ClassifierCSRef(ClassifierRef):

    pass
class oclinEcoreCST_DataTypeRef(ClassifierRef):

    pass
class AttributeRef:

    pass
class oclinEcoreCST_EAttributeRef(AttributeRef):

    pass
class oclinEcoreCST_AttributeCSRef(AttributeRef):

    pass
class StructuralFeatureCS:

    pass
class oclinEcoreCST_ReferenceCS(StructuralFeatureCS):

    def __init__(self, containment: bool, oclinEcoreCST_ReferenceCS: "oclinEcoreCST_ReferenceRef" = None, oclinEcoreCST_ReferenceCS46: set["oclinEcoreCST_AttributeRef"] = None, oclinEcoreCST_ReferenceCS48: "oclinEcoreCST_ReferenceCSRef" = None):
        self.containment = containment
        self.oclinEcoreCST_ReferenceCS = oclinEcoreCST_ReferenceCS
        self.oclinEcoreCST_ReferenceCS46 = oclinEcoreCST_ReferenceCS46 if oclinEcoreCST_ReferenceCS46 is not None else set()
        self.oclinEcoreCST_ReferenceCS48 = oclinEcoreCST_ReferenceCS48
        
    @property
    def containment(self) -> bool:
        return self.__containment

    @containment.setter
    def containment(self, containment: bool):
        self.__containment = containment

    @property
    def oclinEcoreCST_ReferenceCS48(self):
        return self.__oclinEcoreCST_ReferenceCS48

    @oclinEcoreCST_ReferenceCS48.setter
    def oclinEcoreCST_ReferenceCS48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclinEcoreCST_ReferenceCS__oclinEcoreCST_ReferenceCS48", None)
        self.__oclinEcoreCST_ReferenceCS48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclinEcoreCST_ReferenceCSRef"):
                opp_val = getattr(old_value, "oclinEcoreCST_ReferenceCSRef", None)
                if opp_val == self:
                    setattr(old_value, "oclinEcoreCST_ReferenceCSRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclinEcoreCST_ReferenceCSRef"):
                opp_val = getattr(value, "oclinEcoreCST_ReferenceCSRef", None)
                setattr(value, "oclinEcoreCST_ReferenceCSRef", self)

    @property
    def oclinEcoreCST_ReferenceCS46(self):
        return self.__oclinEcoreCST_ReferenceCS46

    @oclinEcoreCST_ReferenceCS46.setter
    def oclinEcoreCST_ReferenceCS46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclinEcoreCST_ReferenceCS__oclinEcoreCST_ReferenceCS46", None)
        self.__oclinEcoreCST_ReferenceCS46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oclinEcoreCST_AttributeRef"):
                    opp_val = getattr(item, "oclinEcoreCST_AttributeRef", None)
                    
                    if opp_val == self:
                        setattr(item, "oclinEcoreCST_AttributeRef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oclinEcoreCST_AttributeRef"):
                    opp_val = getattr(item, "oclinEcoreCST_AttributeRef", None)
                    
                    setattr(item, "oclinEcoreCST_AttributeRef", self)
                    

    @property
    def oclinEcoreCST_ReferenceCS(self):
        return self.__oclinEcoreCST_ReferenceCS

    @oclinEcoreCST_ReferenceCS.setter
    def oclinEcoreCST_ReferenceCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclinEcoreCST_ReferenceCS__oclinEcoreCST_ReferenceCS", None)
        self.__oclinEcoreCST_ReferenceCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclinEcoreCST_ReferenceRef"):
                opp_val = getattr(old_value, "oclinEcoreCST_ReferenceRef", None)
                if opp_val == self:
                    setattr(old_value, "oclinEcoreCST_ReferenceRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclinEcoreCST_ReferenceRef"):
                opp_val = getattr(value, "oclinEcoreCST_ReferenceRef", None)
                setattr(value, "oclinEcoreCST_ReferenceRef", self)

class oclinEcoreCST_AttributeCS(StructuralFeatureCS):

    pass
class oclinEcoreCST_StructuralFeatureCS(TypedElementCS):

    pass
class oclinEcoreCST_OperationCS(TypedElementCS):

    pass
class oclinEcoreCST_ClassRef(ClassifierRef):

    pass
class ClassifierCS:

    pass
class oclinEcoreCST_DataTypeOrEnumCS(ClassifierCS):

    pass
class oclinEcoreCST_ClassCS(ClassifierCS):

    pass
class oclinEcoreCST_AttributeRef(ABC):

    pass
class oclinEcoreCST_DetailCS:

    def __init__(self, idName: str, stringName: str, value: str, oclinEcoreCST_DetailCS: "oclinEcoreCST_AnnotationCS" = None):
        self.idName = idName
        self.stringName = stringName
        self.value = value
        self.oclinEcoreCST_DetailCS = oclinEcoreCST_DetailCS
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def stringName(self) -> str:
        return self.__stringName

    @stringName.setter
    def stringName(self, stringName: str):
        self.__stringName = stringName

    @property
    def idName(self) -> str:
        return self.__idName

    @idName.setter
    def idName(self, idName: str):
        self.__idName = idName

    @property
    def oclinEcoreCST_DetailCS(self):
        return self.__oclinEcoreCST_DetailCS

    @oclinEcoreCST_DetailCS.setter
    def oclinEcoreCST_DetailCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclinEcoreCST_DetailCS__oclinEcoreCST_DetailCS", None)
        self.__oclinEcoreCST_DetailCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclinEcoreCST_AnnotationCS"):
                opp_val = getattr(old_value, "oclinEcoreCST_AnnotationCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclinEcoreCST_AnnotationCS"):
                opp_val = getattr(value, "oclinEcoreCST_AnnotationCS", None)
                if opp_val is None:
                    setattr(value, "oclinEcoreCST_AnnotationCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ModelElementCS:

    pass
class oclinEcoreCST_NamedElementCS(ModelElementCS):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class oclinEcoreCST_AnnotationCS(ModelElementCS):

    def __init__(self, idSource: str, stringSource: str, oclinEcoreCST_AnnotationCS: set["oclinEcoreCST_DetailCS"] = None, oclinEcoreCST_AnnotationCS27: "oclinEcoreCST_ModelElementCS" = None):
        self.idSource = idSource
        self.stringSource = stringSource
        self.oclinEcoreCST_AnnotationCS = oclinEcoreCST_AnnotationCS if oclinEcoreCST_AnnotationCS is not None else set()
        self.oclinEcoreCST_AnnotationCS27 = oclinEcoreCST_AnnotationCS27
        
    @property
    def idSource(self) -> str:
        return self.__idSource

    @idSource.setter
    def idSource(self, idSource: str):
        self.__idSource = idSource

    @property
    def stringSource(self) -> str:
        return self.__stringSource

    @stringSource.setter
    def stringSource(self, stringSource: str):
        self.__stringSource = stringSource

    @property
    def oclinEcoreCST_AnnotationCS(self):
        return self.__oclinEcoreCST_AnnotationCS

    @oclinEcoreCST_AnnotationCS.setter
    def oclinEcoreCST_AnnotationCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclinEcoreCST_AnnotationCS__oclinEcoreCST_AnnotationCS", None)
        self.__oclinEcoreCST_AnnotationCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oclinEcoreCST_DetailCS"):
                    opp_val = getattr(item, "oclinEcoreCST_DetailCS", None)
                    
                    if opp_val == self:
                        setattr(item, "oclinEcoreCST_DetailCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oclinEcoreCST_DetailCS"):
                    opp_val = getattr(item, "oclinEcoreCST_DetailCS", None)
                    
                    setattr(item, "oclinEcoreCST_DetailCS", self)
                    

    @property
    def oclinEcoreCST_AnnotationCS27(self):
        return self.__oclinEcoreCST_AnnotationCS27

    @oclinEcoreCST_AnnotationCS27.setter
    def oclinEcoreCST_AnnotationCS27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclinEcoreCST_AnnotationCS__oclinEcoreCST_AnnotationCS27", None)
        self.__oclinEcoreCST_AnnotationCS27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclinEcoreCST_ModelElementCS"):
                opp_val = getattr(old_value, "oclinEcoreCST_ModelElementCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclinEcoreCST_ModelElementCS"):
                opp_val = getattr(value, "oclinEcoreCST_ModelElementCS", None)
                if opp_val is None:
                    setattr(value, "oclinEcoreCST_ModelElementCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
