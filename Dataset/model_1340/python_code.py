from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class IteratorKind(Enum):
    Parameter = "Parameter"
    Iterator = "Iterator"
    Accumulator = "Accumulator"


############################################
# Definition of Classes
############################################

class TypeRefCS:

    pass
class baseCST_WildcardTypeRefCS(TypeRefCS):

    pass
class baseCST_VisitableCS(ABC):

    pass
class baseCST_Type:

    pass
class TemplateParameterCS:

    pass
class baseCST_Property:

    pass
class RootCS:

    pass
class PackageCS:

    pass
class baseCST_RootPackageCS(RootCS, PackageCS):

    pass
class Pivotable:

    pass
class PathElementCS:

    pass
class baseCST_PathElementWithURICS(PathElementCS):

    def __init__(self, uri: str):
        self.uri = uri
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

class baseCST_EClassifier:

    pass
class FeatureCS:

    pass
class ModelElementCS:

    pass
class baseCST_TypeCS(ModelElementCS):

    pass
class baseCST_RootCS(ModelElementCS):

    pass
class baseCST_TemplateSignatureCS(ModelElementCS):

    pass
class baseCST_TemplateParameterSubstitutionCS(ModelElementCS):

    pass
class ElementCS:

    pass
class baseCST_TemplateableElementCS(ElementCS):

    pass
class baseCST_PathElementCS(Pivotable, ElementCS):

    pass
class baseCST_PivotableElementCS(Pivotable, ElementCS):

    pass
class baseCST_MultiplicityCS(ElementCS):

    def __init__(self, baseCST_MultiplicityCS: "baseCST_TypedRefCS" = None):
        self.baseCST_MultiplicityCS = baseCST_MultiplicityCS
        
    @property
    def baseCST_MultiplicityCS(self):
        return self.__baseCST_MultiplicityCS

    @baseCST_MultiplicityCS.setter
    def baseCST_MultiplicityCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_MultiplicityCS__baseCST_MultiplicityCS", None)
        self.__baseCST_MultiplicityCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_TypedRefCS108"):
                opp_val = getattr(old_value, "baseCST_TypedRefCS108", None)
                if opp_val == self:
                    setattr(old_value, "baseCST_TypedRefCS108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_TypedRefCS108"):
                opp_val = getattr(value, "baseCST_TypedRefCS108", None)
                setattr(value, "baseCST_TypedRefCS108", self)

    def getUpper(self) -> int:
        # TODO: Implement getUpper method
        pass

    def getLower(self) -> int:
        # TODO: Implement getLower method
        pass

class MultiplicityCS:

    pass
class baseCST_MultiplicityStringCS(MultiplicityCS):

    def __init__(self, stringBounds: str):
        self.stringBounds = stringBounds
        
    @property
    def stringBounds(self) -> str:
        return self.__stringBounds

    @stringBounds.setter
    def stringBounds(self, stringBounds: str):
        self.__stringBounds = stringBounds

class baseCST_MultiplicityBoundsCS(MultiplicityCS):

    def __init__(self, lowerBound: int, upperBound: str):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        
    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def upperBound(self) -> str:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: str):
        self.__upperBound = upperBound

class baseCST_Element:

    pass
class ElementRefCS:

    pass
class baseCST_TemplateBindingCS(ElementRefCS):

    pass
class baseCST_TypeRefCS(ElementRefCS):

    pass
class Nameable:

    pass
class baseCST_NamedElementCS(Nameable, ModelElementCS):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class TypedRefCS:

    pass
class baseCST_PrimitiveTypeRefCS(Nameable, TypedRefCS):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class baseCST_TypedTypeRefCS(TypedRefCS):

    pass
class baseCST_TupleTypeCS(Nameable, TypedRefCS):

    def __init__(self, name: str, baseCST_TupleTypeCS: set["baseCST_TuplePartCS"] = None):
        self.name = name
        self.baseCST_TupleTypeCS = baseCST_TupleTypeCS if baseCST_TupleTypeCS is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def baseCST_TupleTypeCS(self):
        return self.__baseCST_TupleTypeCS

    @baseCST_TupleTypeCS.setter
    def baseCST_TupleTypeCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_TupleTypeCS__baseCST_TupleTypeCS", None)
        self.__baseCST_TupleTypeCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "baseCST_TuplePartCS"):
                    opp_val = getattr(item, "baseCST_TuplePartCS", None)
                    
                    if opp_val == self:
                        setattr(item, "baseCST_TuplePartCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "baseCST_TuplePartCS"):
                    opp_val = getattr(item, "baseCST_TuplePartCS", None)
                    
                    setattr(item, "baseCST_TuplePartCS", self)
                    

class baseCST_Namespace:

    pass
class baseCST_PathNameCS(Pivotable, ElementCS):

    def __init__(self, scopeFilter: str, baseCST_PathNameCS: "baseCST_ImportCS" = None, baseCST_PathNameCS40: "baseCST_ModelElementRefCS" = None, pathName: set["baseCST_PathElementCS"] = None, baseCST_PathNameCS70: "baseCST_Element" = None, baseCST_PathNameCS73: "baseCST_ElementCS" = None, PathNameCS: "baseCST_PathElementCS" = None, baseCST_PathNameCS110: "baseCST_TypedTypeRefCS" = None):
        self.scopeFilter = scopeFilter
        self.baseCST_PathNameCS = baseCST_PathNameCS
        self.baseCST_PathNameCS40 = baseCST_PathNameCS40
        self.pathName = pathName if pathName is not None else set()
        self.baseCST_PathNameCS70 = baseCST_PathNameCS70
        self.baseCST_PathNameCS73 = baseCST_PathNameCS73
        self.PathNameCS = PathNameCS
        self.baseCST_PathNameCS110 = baseCST_PathNameCS110
        
    @property
    def scopeFilter(self) -> str:
        return self.__scopeFilter

    @scopeFilter.setter
    def scopeFilter(self, scopeFilter: str):
        self.__scopeFilter = scopeFilter

    @property
    def baseCST_PathNameCS110(self):
        return self.__baseCST_PathNameCS110

    @baseCST_PathNameCS110.setter
    def baseCST_PathNameCS110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_PathNameCS__baseCST_PathNameCS110", None)
        self.__baseCST_PathNameCS110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_TypedTypeRefCS"):
                opp_val = getattr(old_value, "baseCST_TypedTypeRefCS", None)
                if opp_val == self:
                    setattr(old_value, "baseCST_TypedTypeRefCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_TypedTypeRefCS"):
                opp_val = getattr(value, "baseCST_TypedTypeRefCS", None)
                setattr(value, "baseCST_TypedTypeRefCS", self)

    @property
    def PathNameCS(self):
        return self.__PathNameCS

    @PathNameCS.setter
    def PathNameCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_PathNameCS__PathNameCS", None)
        self.__PathNameCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "path"):
                opp_val = getattr(old_value, "path", None)
                if opp_val == self:
                    setattr(old_value, "path", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "path"):
                opp_val = getattr(value, "path", None)
                setattr(value, "path", self)

    @property
    def baseCST_PathNameCS(self):
        return self.__baseCST_PathNameCS

    @baseCST_PathNameCS.setter
    def baseCST_PathNameCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_PathNameCS__baseCST_PathNameCS", None)
        self.__baseCST_PathNameCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_ImportCS"):
                opp_val = getattr(old_value, "baseCST_ImportCS", None)
                if opp_val == self:
                    setattr(old_value, "baseCST_ImportCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_ImportCS"):
                opp_val = getattr(value, "baseCST_ImportCS", None)
                setattr(value, "baseCST_ImportCS", self)

    @property
    def baseCST_PathNameCS70(self):
        return self.__baseCST_PathNameCS70

    @baseCST_PathNameCS70.setter
    def baseCST_PathNameCS70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_PathNameCS__baseCST_PathNameCS70", None)
        self.__baseCST_PathNameCS70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_Element71"):
                opp_val = getattr(old_value, "baseCST_Element71", None)
                if opp_val == self:
                    setattr(old_value, "baseCST_Element71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_Element71"):
                opp_val = getattr(value, "baseCST_Element71", None)
                setattr(value, "baseCST_Element71", self)

    @property
    def baseCST_PathNameCS73(self):
        return self.__baseCST_PathNameCS73

    @baseCST_PathNameCS73.setter
    def baseCST_PathNameCS73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_PathNameCS__baseCST_PathNameCS73", None)
        self.__baseCST_PathNameCS73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_ElementCS74"):
                opp_val = getattr(old_value, "baseCST_ElementCS74", None)
                if opp_val == self:
                    setattr(old_value, "baseCST_ElementCS74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_ElementCS74"):
                opp_val = getattr(value, "baseCST_ElementCS74", None)
                setattr(value, "baseCST_ElementCS74", self)

    @property
    def baseCST_PathNameCS40(self):
        return self.__baseCST_PathNameCS40

    @baseCST_PathNameCS40.setter
    def baseCST_PathNameCS40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_PathNameCS__baseCST_PathNameCS40", None)
        self.__baseCST_PathNameCS40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_ModelElementRefCS39"):
                opp_val = getattr(old_value, "baseCST_ModelElementRefCS39", None)
                if opp_val == self:
                    setattr(old_value, "baseCST_ModelElementRefCS39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_ModelElementRefCS39"):
                opp_val = getattr(value, "baseCST_ModelElementRefCS39", None)
                setattr(value, "baseCST_ModelElementRefCS39", self)

    @property
    def pathName(self):
        return self.__pathName

    @pathName.setter
    def pathName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_PathNameCS__pathName", None)
        self.__pathName = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PathElementCS"):
                    opp_val = getattr(item, "PathElementCS", None)
                    
                    if opp_val == self:
                        setattr(item, "PathElementCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PathElementCS"):
                    opp_val = getattr(item, "PathElementCS", None)
                    
                    setattr(item, "PathElementCS", self)
                    

class TypedElementCS:

    pass
class baseCST_TuplePartCS(TypedElementCS):

    pass
class baseCST_ParameterCS(TypedElementCS):

    pass
class baseCST_FeatureCS(TypedElementCS):

    pass
class PivotableElementCS:

    pass
class baseCST_ElementRefCS(PivotableElementCS):

    pass
class VisitableCS:

    pass
class baseCST_ElementCS(VisitableCS):

    def __init__(self, baseCST_ElementCS: "baseCST_ElementCS" = None, baseCST_ElementCS18: "baseCST_ElementCS" = None, baseCST_ElementCS74: "baseCST_PathNameCS" = None):
        self.baseCST_ElementCS = baseCST_ElementCS
        self.baseCST_ElementCS18 = baseCST_ElementCS18
        self.baseCST_ElementCS74 = baseCST_ElementCS74
        
    @property
    def baseCST_ElementCS74(self):
        return self.__baseCST_ElementCS74

    @baseCST_ElementCS74.setter
    def baseCST_ElementCS74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_ElementCS__baseCST_ElementCS74", None)
        self.__baseCST_ElementCS74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_PathNameCS73"):
                opp_val = getattr(old_value, "baseCST_PathNameCS73", None)
                if opp_val == self:
                    setattr(old_value, "baseCST_PathNameCS73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_PathNameCS73"):
                opp_val = getattr(value, "baseCST_PathNameCS73", None)
                setattr(value, "baseCST_PathNameCS73", self)

    @property
    def baseCST_ElementCS18(self):
        return self.__baseCST_ElementCS18

    @baseCST_ElementCS18.setter
    def baseCST_ElementCS18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_ElementCS__baseCST_ElementCS18", None)
        self.__baseCST_ElementCS18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_ElementCS"):
                opp_val = getattr(old_value, "baseCST_ElementCS", None)
                if opp_val == self:
                    setattr(old_value, "baseCST_ElementCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_ElementCS"):
                opp_val = getattr(value, "baseCST_ElementCS", None)
                setattr(value, "baseCST_ElementCS", self)

    @property
    def baseCST_ElementCS(self):
        return self.__baseCST_ElementCS

    @baseCST_ElementCS.setter
    def baseCST_ElementCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_ElementCS__baseCST_ElementCS", None)
        self.__baseCST_ElementCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_ElementCS18"):
                opp_val = getattr(old_value, "baseCST_ElementCS18", None)
                if opp_val == self:
                    setattr(old_value, "baseCST_ElementCS18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_ElementCS18"):
                opp_val = getattr(value, "baseCST_ElementCS18", None)
                setattr(value, "baseCST_ElementCS18", self)

    def getDescription(self) -> str:
        # TODO: Implement getDescription method
        pass

class baseCST_SpecificationCS(ModelElementCS):

    def __init__(self, exprString: str, baseCST_SpecificationCS: "baseCST_ConstraintCS" = None, baseCST_SpecificationCS16: "baseCST_ConstraintCS" = None, baseCST_SpecificationCS56: "baseCST_OperationCS" = None, baseCST_SpecificationCS89: "baseCST_StructuralFeatureCS" = None):
        self.exprString = exprString
        self.baseCST_SpecificationCS = baseCST_SpecificationCS
        self.baseCST_SpecificationCS16 = baseCST_SpecificationCS16
        self.baseCST_SpecificationCS56 = baseCST_SpecificationCS56
        self.baseCST_SpecificationCS89 = baseCST_SpecificationCS89
        
    @property
    def exprString(self) -> str:
        return self.__exprString

    @exprString.setter
    def exprString(self, exprString: str):
        self.__exprString = exprString

    @property
    def baseCST_SpecificationCS16(self):
        return self.__baseCST_SpecificationCS16

    @baseCST_SpecificationCS16.setter
    def baseCST_SpecificationCS16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_SpecificationCS__baseCST_SpecificationCS16", None)
        self.__baseCST_SpecificationCS16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_ConstraintCS15"):
                opp_val = getattr(old_value, "baseCST_ConstraintCS15", None)
                if opp_val == self:
                    setattr(old_value, "baseCST_ConstraintCS15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_ConstraintCS15"):
                opp_val = getattr(value, "baseCST_ConstraintCS15", None)
                setattr(value, "baseCST_ConstraintCS15", self)

    @property
    def baseCST_SpecificationCS89(self):
        return self.__baseCST_SpecificationCS89

    @baseCST_SpecificationCS89.setter
    def baseCST_SpecificationCS89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_SpecificationCS__baseCST_SpecificationCS89", None)
        self.__baseCST_SpecificationCS89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_StructuralFeatureCS"):
                opp_val = getattr(old_value, "baseCST_StructuralFeatureCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_StructuralFeatureCS"):
                opp_val = getattr(value, "baseCST_StructuralFeatureCS", None)
                if opp_val is None:
                    setattr(value, "baseCST_StructuralFeatureCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def baseCST_SpecificationCS(self):
        return self.__baseCST_SpecificationCS

    @baseCST_SpecificationCS.setter
    def baseCST_SpecificationCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_SpecificationCS__baseCST_SpecificationCS", None)
        self.__baseCST_SpecificationCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_ConstraintCS13"):
                opp_val = getattr(old_value, "baseCST_ConstraintCS13", None)
                if opp_val == self:
                    setattr(old_value, "baseCST_ConstraintCS13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_ConstraintCS13"):
                opp_val = getattr(value, "baseCST_ConstraintCS13", None)
                setattr(value, "baseCST_ConstraintCS13", self)

    @property
    def baseCST_SpecificationCS56(self):
        return self.__baseCST_SpecificationCS56

    @baseCST_SpecificationCS56.setter
    def baseCST_SpecificationCS56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_SpecificationCS__baseCST_SpecificationCS56", None)
        self.__baseCST_SpecificationCS56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_OperationCS55"):
                opp_val = getattr(old_value, "baseCST_OperationCS55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_OperationCS55"):
                opp_val = getattr(value, "baseCST_OperationCS55", None)
                if opp_val is None:
                    setattr(value, "baseCST_OperationCS55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TemplateableElementCS:

    pass
class baseCST_LambdaTypeCS(Nameable, TypedRefCS, TemplateableElementCS):

    def __init__(self, name: str, baseCST_LambdaTypeCS: "baseCST_TypedRefCS" = None, baseCST_LambdaTypeCS28: set["baseCST_TypedRefCS"] = None, baseCST_LambdaTypeCS31: "baseCST_TypedRefCS" = None):
        self.name = name
        self.baseCST_LambdaTypeCS = baseCST_LambdaTypeCS
        self.baseCST_LambdaTypeCS28 = baseCST_LambdaTypeCS28 if baseCST_LambdaTypeCS28 is not None else set()
        self.baseCST_LambdaTypeCS31 = baseCST_LambdaTypeCS31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def baseCST_LambdaTypeCS28(self):
        return self.__baseCST_LambdaTypeCS28

    @baseCST_LambdaTypeCS28.setter
    def baseCST_LambdaTypeCS28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_LambdaTypeCS__baseCST_LambdaTypeCS28", None)
        self.__baseCST_LambdaTypeCS28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "baseCST_TypedRefCS29"):
                    opp_val = getattr(item, "baseCST_TypedRefCS29", None)
                    
                    if opp_val == self:
                        setattr(item, "baseCST_TypedRefCS29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "baseCST_TypedRefCS29"):
                    opp_val = getattr(item, "baseCST_TypedRefCS29", None)
                    
                    setattr(item, "baseCST_TypedRefCS29", self)
                    

    @property
    def baseCST_LambdaTypeCS(self):
        return self.__baseCST_LambdaTypeCS

    @baseCST_LambdaTypeCS.setter
    def baseCST_LambdaTypeCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_LambdaTypeCS__baseCST_LambdaTypeCS", None)
        self.__baseCST_LambdaTypeCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_TypedRefCS26"):
                opp_val = getattr(old_value, "baseCST_TypedRefCS26", None)
                if opp_val == self:
                    setattr(old_value, "baseCST_TypedRefCS26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_TypedRefCS26"):
                opp_val = getattr(value, "baseCST_TypedRefCS26", None)
                setattr(value, "baseCST_TypedRefCS26", self)

    @property
    def baseCST_LambdaTypeCS31(self):
        return self.__baseCST_LambdaTypeCS31

    @baseCST_LambdaTypeCS31.setter
    def baseCST_LambdaTypeCS31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_LambdaTypeCS__baseCST_LambdaTypeCS31", None)
        self.__baseCST_LambdaTypeCS31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_TypedRefCS32"):
                opp_val = getattr(old_value, "baseCST_TypedRefCS32", None)
                if opp_val == self:
                    setattr(old_value, "baseCST_TypedRefCS32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_TypedRefCS32"):
                opp_val = getattr(value, "baseCST_TypedRefCS32", None)
                setattr(value, "baseCST_TypedRefCS32", self)

class TypeCS:

    pass
class baseCST_TypeParameterCS(TypeCS, TemplateParameterCS):

    pass
class baseCST_StructuralFeatureCS(FeatureCS):

    def __init__(self, default: str, StructuralFeatureCS: "baseCST_ClassCS" = None, ownedProperty: "baseCST_ClassCS" = None, baseCST_StructuralFeatureCS: set["baseCST_SpecificationCS"] = None):
        self.default = default
        self.StructuralFeatureCS = StructuralFeatureCS
        self.ownedProperty = ownedProperty
        self.baseCST_StructuralFeatureCS = baseCST_StructuralFeatureCS if baseCST_StructuralFeatureCS is not None else set()
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def baseCST_StructuralFeatureCS(self):
        return self.__baseCST_StructuralFeatureCS

    @baseCST_StructuralFeatureCS.setter
    def baseCST_StructuralFeatureCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_StructuralFeatureCS__baseCST_StructuralFeatureCS", None)
        self.__baseCST_StructuralFeatureCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "baseCST_SpecificationCS89"):
                    opp_val = getattr(item, "baseCST_SpecificationCS89", None)
                    
                    if opp_val == self:
                        setattr(item, "baseCST_SpecificationCS89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "baseCST_SpecificationCS89"):
                    opp_val = getattr(item, "baseCST_SpecificationCS89", None)
                    
                    setattr(item, "baseCST_SpecificationCS89", self)
                    

    @property
    def StructuralFeatureCS(self):
        return self.__StructuralFeatureCS

    @StructuralFeatureCS.setter
    def StructuralFeatureCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_StructuralFeatureCS__StructuralFeatureCS", None)
        self.__StructuralFeatureCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedProperty(self):
        return self.__ownedProperty

    @ownedProperty.setter
    def ownedProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_StructuralFeatureCS__ownedProperty", None)
        self.__ownedProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassCS87"):
                opp_val = getattr(old_value, "ClassCS87", None)
                if opp_val == self:
                    setattr(old_value, "ClassCS87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassCS87"):
                opp_val = getattr(value, "ClassCS87", None)
                setattr(value, "ClassCS87", self)

class baseCST_OperationCS(FeatureCS, TemplateableElementCS):

    pass
class baseCST_TypedRefCS(TypeRefCS):

    pass
class StructuralFeatureCS:

    pass
class baseCST_ReferenceCS(StructuralFeatureCS):

    pass
class baseCST_AttributeCS(StructuralFeatureCS):

    pass
class NamedElementCS:

    pass
class baseCST_NamespaceCS(NamedElementCS):

    pass
class baseCST_DetailCS(NamedElementCS):

    def __init__(self, value: str, baseCST_DetailCS: "baseCST_AnnotationElementCS" = None):
        self.value = value
        self.baseCST_DetailCS = baseCST_DetailCS
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def baseCST_DetailCS(self):
        return self.__baseCST_DetailCS

    @baseCST_DetailCS.setter
    def baseCST_DetailCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_DetailCS__baseCST_DetailCS", None)
        self.__baseCST_DetailCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_AnnotationElementCS"):
                opp_val = getattr(old_value, "baseCST_AnnotationElementCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_AnnotationElementCS"):
                opp_val = getattr(value, "baseCST_AnnotationElementCS", None)
                if opp_val is None:
                    setattr(value, "baseCST_AnnotationElementCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class baseCST_EnumerationLiteralCS(NamedElementCS):

    def __init__(self, value: int, baseCST_EnumerationLiteralCS: "baseCST_DataTypeCS" = None, baseCST_EnumerationLiteralCS21: "baseCST_EnumerationCS" = None):
        self.value = value
        self.baseCST_EnumerationLiteralCS = baseCST_EnumerationLiteralCS
        self.baseCST_EnumerationLiteralCS21 = baseCST_EnumerationLiteralCS21
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def baseCST_EnumerationLiteralCS(self):
        return self.__baseCST_EnumerationLiteralCS

    @baseCST_EnumerationLiteralCS.setter
    def baseCST_EnumerationLiteralCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_EnumerationLiteralCS__baseCST_EnumerationLiteralCS", None)
        self.__baseCST_EnumerationLiteralCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_DataTypeCS"):
                opp_val = getattr(old_value, "baseCST_DataTypeCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_DataTypeCS"):
                opp_val = getattr(value, "baseCST_DataTypeCS", None)
                if opp_val is None:
                    setattr(value, "baseCST_DataTypeCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def baseCST_EnumerationLiteralCS21(self):
        return self.__baseCST_EnumerationLiteralCS21

    @baseCST_EnumerationLiteralCS21.setter
    def baseCST_EnumerationLiteralCS21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_EnumerationLiteralCS__baseCST_EnumerationLiteralCS21", None)
        self.__baseCST_EnumerationLiteralCS21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_EnumerationCS"):
                opp_val = getattr(old_value, "baseCST_EnumerationCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_EnumerationCS"):
                opp_val = getattr(value, "baseCST_EnumerationCS", None)
                if opp_val is None:
                    setattr(value, "baseCST_EnumerationCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class baseCST_ClassifierCS(TypeCS, NamedElementCS, TemplateableElementCS):

    def __init__(self, instanceClassName: str, qualifier: str, ownedType: "baseCST_PackageCS" = None, baseCST_ClassifierCS: set["baseCST_ConstraintCS"] = None, ClassifierCS: "baseCST_PackageCS" = None):
        self.instanceClassName = instanceClassName
        self.qualifier = qualifier
        self.ownedType = ownedType
        self.baseCST_ClassifierCS = baseCST_ClassifierCS if baseCST_ClassifierCS is not None else set()
        self.ClassifierCS = ClassifierCS
        
    @property
    def qualifier(self) -> str:
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, qualifier: str):
        self.__qualifier = qualifier

    @property
    def instanceClassName(self) -> str:
        return self.__instanceClassName

    @instanceClassName.setter
    def instanceClassName(self, instanceClassName: str):
        self.__instanceClassName = instanceClassName

    @property
    def baseCST_ClassifierCS(self):
        return self.__baseCST_ClassifierCS

    @baseCST_ClassifierCS.setter
    def baseCST_ClassifierCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_ClassifierCS__baseCST_ClassifierCS", None)
        self.__baseCST_ClassifierCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "baseCST_ConstraintCS"):
                    opp_val = getattr(item, "baseCST_ConstraintCS", None)
                    
                    if opp_val == self:
                        setattr(item, "baseCST_ConstraintCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "baseCST_ConstraintCS"):
                    opp_val = getattr(item, "baseCST_ConstraintCS", None)
                    
                    setattr(item, "baseCST_ConstraintCS", self)
                    

    @property
    def ownedType(self):
        return self.__ownedType

    @ownedType.setter
    def ownedType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_ClassifierCS__ownedType", None)
        self.__ownedType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PackageCS"):
                opp_val = getattr(old_value, "PackageCS", None)
                if opp_val == self:
                    setattr(old_value, "PackageCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PackageCS"):
                opp_val = getattr(value, "PackageCS", None)
                setattr(value, "PackageCS", self)

    @property
    def ClassifierCS(self):
        return self.__ClassifierCS

    @ClassifierCS.setter
    def ClassifierCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_ClassifierCS__ClassifierCS", None)
        self.__ClassifierCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner58"):
                opp_val = getattr(old_value, "owner58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner58"):
                opp_val = getattr(value, "owner58", None)
                if opp_val is None:
                    setattr(value, "owner58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class baseCST_TemplateParameterCS(NamedElementCS):

    pass
class baseCST_TypedElementCS(NamedElementCS):

    def __init__(self, qualifier: str, optional: bool, baseCST_TypedElementCS: "baseCST_TypedRefCS" = None):
        self.qualifier = qualifier
        self.optional = optional
        self.baseCST_TypedElementCS = baseCST_TypedElementCS
        
    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

    @property
    def qualifier(self) -> str:
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, qualifier: str):
        self.__qualifier = qualifier

    @property
    def baseCST_TypedElementCS(self):
        return self.__baseCST_TypedElementCS

    @baseCST_TypedElementCS.setter
    def baseCST_TypedElementCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_TypedElementCS__baseCST_TypedElementCS", None)
        self.__baseCST_TypedElementCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_TypedRefCS106"):
                opp_val = getattr(old_value, "baseCST_TypedRefCS106", None)
                if opp_val == self:
                    setattr(old_value, "baseCST_TypedRefCS106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_TypedRefCS106"):
                opp_val = getattr(value, "baseCST_TypedRefCS106", None)
                setattr(value, "baseCST_TypedRefCS106", self)

class baseCST_ConstraintCS(NamedElementCS):

    def __init__(self, stereotype: str, baseCST_ConstraintCS: "baseCST_ClassifierCS" = None, baseCST_ConstraintCS13: "baseCST_SpecificationCS" = None, baseCST_ConstraintCS15: "baseCST_SpecificationCS" = None, baseCST_ConstraintCS50: "baseCST_OperationCS" = None, baseCST_ConstraintCS53: "baseCST_OperationCS" = None):
        self.stereotype = stereotype
        self.baseCST_ConstraintCS = baseCST_ConstraintCS
        self.baseCST_ConstraintCS13 = baseCST_ConstraintCS13
        self.baseCST_ConstraintCS15 = baseCST_ConstraintCS15
        self.baseCST_ConstraintCS50 = baseCST_ConstraintCS50
        self.baseCST_ConstraintCS53 = baseCST_ConstraintCS53
        
    @property
    def stereotype(self) -> str:
        return self.__stereotype

    @stereotype.setter
    def stereotype(self, stereotype: str):
        self.__stereotype = stereotype

    @property
    def baseCST_ConstraintCS15(self):
        return self.__baseCST_ConstraintCS15

    @baseCST_ConstraintCS15.setter
    def baseCST_ConstraintCS15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_ConstraintCS__baseCST_ConstraintCS15", None)
        self.__baseCST_ConstraintCS15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_SpecificationCS16"):
                opp_val = getattr(old_value, "baseCST_SpecificationCS16", None)
                if opp_val == self:
                    setattr(old_value, "baseCST_SpecificationCS16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_SpecificationCS16"):
                opp_val = getattr(value, "baseCST_SpecificationCS16", None)
                setattr(value, "baseCST_SpecificationCS16", self)

    @property
    def baseCST_ConstraintCS50(self):
        return self.__baseCST_ConstraintCS50

    @baseCST_ConstraintCS50.setter
    def baseCST_ConstraintCS50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_ConstraintCS__baseCST_ConstraintCS50", None)
        self.__baseCST_ConstraintCS50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_OperationCS49"):
                opp_val = getattr(old_value, "baseCST_OperationCS49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_OperationCS49"):
                opp_val = getattr(value, "baseCST_OperationCS49", None)
                if opp_val is None:
                    setattr(value, "baseCST_OperationCS49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def baseCST_ConstraintCS53(self):
        return self.__baseCST_ConstraintCS53

    @baseCST_ConstraintCS53.setter
    def baseCST_ConstraintCS53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_ConstraintCS__baseCST_ConstraintCS53", None)
        self.__baseCST_ConstraintCS53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_OperationCS52"):
                opp_val = getattr(old_value, "baseCST_OperationCS52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_OperationCS52"):
                opp_val = getattr(value, "baseCST_OperationCS52", None)
                if opp_val is None:
                    setattr(value, "baseCST_OperationCS52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def baseCST_ConstraintCS(self):
        return self.__baseCST_ConstraintCS

    @baseCST_ConstraintCS.setter
    def baseCST_ConstraintCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_ConstraintCS__baseCST_ConstraintCS", None)
        self.__baseCST_ConstraintCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_ClassifierCS"):
                opp_val = getattr(old_value, "baseCST_ClassifierCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_ClassifierCS"):
                opp_val = getattr(value, "baseCST_ClassifierCS", None)
                if opp_val is None:
                    setattr(value, "baseCST_ClassifierCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def baseCST_ConstraintCS13(self):
        return self.__baseCST_ConstraintCS13

    @baseCST_ConstraintCS13.setter
    def baseCST_ConstraintCS13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_ConstraintCS__baseCST_ConstraintCS13", None)
        self.__baseCST_ConstraintCS13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_SpecificationCS"):
                opp_val = getattr(old_value, "baseCST_SpecificationCS", None)
                if opp_val == self:
                    setattr(old_value, "baseCST_SpecificationCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_SpecificationCS"):
                opp_val = getattr(value, "baseCST_SpecificationCS", None)
                setattr(value, "baseCST_SpecificationCS", self)

class baseCST_AnnotationElementCS(NamedElementCS):

    pass
class baseCST_ModelElementRefCS(ElementRefCS):

    pass
class baseCST_ModelElementCS(PivotableElementCS):

    def __init__(self, originalXmiId: str, csi: str, baseCST_ModelElementCS: "baseCST_AnnotationCS" = None, baseCST_ModelElementCS36: set["baseCST_AnnotationElementCS"] = None):
        self.originalXmiId = originalXmiId
        self.csi = csi
        self.baseCST_ModelElementCS = baseCST_ModelElementCS
        self.baseCST_ModelElementCS36 = baseCST_ModelElementCS36 if baseCST_ModelElementCS36 is not None else set()
        
    @property
    def csi(self) -> str:
        return self.__csi

    @csi.setter
    def csi(self, csi: str):
        self.__csi = csi

    @property
    def originalXmiId(self) -> str:
        return self.__originalXmiId

    @originalXmiId.setter
    def originalXmiId(self, originalXmiId: str):
        self.__originalXmiId = originalXmiId

    @property
    def baseCST_ModelElementCS36(self):
        return self.__baseCST_ModelElementCS36

    @baseCST_ModelElementCS36.setter
    def baseCST_ModelElementCS36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_ModelElementCS__baseCST_ModelElementCS36", None)
        self.__baseCST_ModelElementCS36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "baseCST_AnnotationElementCS37"):
                    opp_val = getattr(item, "baseCST_AnnotationElementCS37", None)
                    
                    if opp_val == self:
                        setattr(item, "baseCST_AnnotationElementCS37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "baseCST_AnnotationElementCS37"):
                    opp_val = getattr(item, "baseCST_AnnotationElementCS37", None)
                    
                    setattr(item, "baseCST_AnnotationElementCS37", self)
                    

    @property
    def baseCST_ModelElementCS(self):
        return self.__baseCST_ModelElementCS

    @baseCST_ModelElementCS.setter
    def baseCST_ModelElementCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_ModelElementCS__baseCST_ModelElementCS", None)
        self.__baseCST_ModelElementCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_AnnotationCS"):
                opp_val = getattr(old_value, "baseCST_AnnotationCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_AnnotationCS"):
                opp_val = getattr(value, "baseCST_AnnotationCS", None)
                if opp_val is None:
                    setattr(value, "baseCST_AnnotationCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AnnotationElementCS:

    pass
class baseCST_DocumentationCS(AnnotationElementCS):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class baseCST_AnnotationCS(AnnotationElementCS):

    pass
class NamespaceCS:

    pass
class baseCST_PackageCS(NamespaceCS):

    def __init__(self, nsPrefix: str, nsURI: str, PackageCS: "baseCST_ClassifierCS" = None, owner58: set["baseCST_ClassifierCS"] = None, baseCST_PackageCS: "baseCST_PackageCS" = None, baseCST_PackageCS59: set["baseCST_PackageCS"] = None):
        self.nsPrefix = nsPrefix
        self.nsURI = nsURI
        self.PackageCS = PackageCS
        self.owner58 = owner58 if owner58 is not None else set()
        self.baseCST_PackageCS = baseCST_PackageCS
        self.baseCST_PackageCS59 = baseCST_PackageCS59 if baseCST_PackageCS59 is not None else set()
        
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
    def PackageCS(self):
        return self.__PackageCS

    @PackageCS.setter
    def PackageCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_PackageCS__PackageCS", None)
        self.__PackageCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedType"):
                opp_val = getattr(old_value, "ownedType", None)
                if opp_val == self:
                    setattr(old_value, "ownedType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedType"):
                opp_val = getattr(value, "ownedType", None)
                setattr(value, "ownedType", self)

    @property
    def baseCST_PackageCS59(self):
        return self.__baseCST_PackageCS59

    @baseCST_PackageCS59.setter
    def baseCST_PackageCS59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_PackageCS__baseCST_PackageCS59", None)
        self.__baseCST_PackageCS59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "baseCST_PackageCS"):
                    opp_val = getattr(item, "baseCST_PackageCS", None)
                    
                    if opp_val == self:
                        setattr(item, "baseCST_PackageCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "baseCST_PackageCS"):
                    opp_val = getattr(item, "baseCST_PackageCS", None)
                    
                    setattr(item, "baseCST_PackageCS", self)
                    

    @property
    def baseCST_PackageCS(self):
        return self.__baseCST_PackageCS

    @baseCST_PackageCS.setter
    def baseCST_PackageCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_PackageCS__baseCST_PackageCS", None)
        self.__baseCST_PackageCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_PackageCS59"):
                opp_val = getattr(old_value, "baseCST_PackageCS59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_PackageCS59"):
                opp_val = getattr(value, "baseCST_PackageCS59", None)
                if opp_val is None:
                    setattr(value, "baseCST_PackageCS59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owner58(self):
        return self.__owner58

    @owner58.setter
    def owner58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_PackageCS__owner58", None)
        self.__owner58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassifierCS"):
                    opp_val = getattr(item, "ClassifierCS", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassifierCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassifierCS"):
                    opp_val = getattr(item, "ClassifierCS", None)
                    
                    setattr(item, "ClassifierCS", self)
                    

    def getClassifier(self, name: str) -> ClassifierCS:
        # TODO: Implement getClassifier method
        pass

class baseCST_ImportCS(NamespaceCS):

    def __init__(self, all: bool, baseCST_ImportCS: "baseCST_PathNameCS" = None, baseCST_ImportCS24: "baseCST_Namespace" = None, baseCST_ImportCS82: "baseCST_RootCS" = None):
        self.all = all
        self.baseCST_ImportCS = baseCST_ImportCS
        self.baseCST_ImportCS24 = baseCST_ImportCS24
        self.baseCST_ImportCS82 = baseCST_ImportCS82
        
    @property
    def all(self) -> bool:
        return self.__all

    @all.setter
    def all(self, all: bool):
        self.__all = all

    @property
    def baseCST_ImportCS82(self):
        return self.__baseCST_ImportCS82

    @baseCST_ImportCS82.setter
    def baseCST_ImportCS82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_ImportCS__baseCST_ImportCS82", None)
        self.__baseCST_ImportCS82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_RootCS"):
                opp_val = getattr(old_value, "baseCST_RootCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_RootCS"):
                opp_val = getattr(value, "baseCST_RootCS", None)
                if opp_val is None:
                    setattr(value, "baseCST_RootCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def baseCST_ImportCS(self):
        return self.__baseCST_ImportCS

    @baseCST_ImportCS.setter
    def baseCST_ImportCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_ImportCS__baseCST_ImportCS", None)
        self.__baseCST_ImportCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_PathNameCS"):
                opp_val = getattr(old_value, "baseCST_PathNameCS", None)
                if opp_val == self:
                    setattr(old_value, "baseCST_PathNameCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_PathNameCS"):
                opp_val = getattr(value, "baseCST_PathNameCS", None)
                setattr(value, "baseCST_PathNameCS", self)

    @property
    def baseCST_ImportCS24(self):
        return self.__baseCST_ImportCS24

    @baseCST_ImportCS24.setter
    def baseCST_ImportCS24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_baseCST_ImportCS__baseCST_ImportCS24", None)
        self.__baseCST_ImportCS24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseCST_Namespace"):
                opp_val = getattr(old_value, "baseCST_Namespace", None)
                if opp_val == self:
                    setattr(old_value, "baseCST_Namespace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseCST_Namespace"):
                opp_val = getattr(value, "baseCST_Namespace", None)
                setattr(value, "baseCST_Namespace", self)

class baseCST_LibraryCS(NamespaceCS):

    pass
class ClassifierCS:

    pass
class baseCST_EnumerationCS(NamespaceCS, ClassifierCS):

    pass
class baseCST_DataTypeCS(NamespaceCS, ClassifierCS):

    pass
class baseCST_ClassCS(NamespaceCS, ClassifierCS):

    pass