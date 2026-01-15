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

class basecs_VisitableCS(ABC):

    pass
class basecs_Type:

    pass
class TypeRefCS:

    pass
class basecs_WildcardTypeRefCS(TypeRefCS):

    pass
class TemplateParameterCS:

    pass
class RootCS:

    pass
class basecs_Property:

    pass
class PathElementCS:

    pass
class basecs_PathElementWithURICS(PathElementCS):

    def __init__(self, uri: str):
        self.uri = uri
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

class basecs_EClassifier:

    pass
class Pivotable:

    pass
class PackageOwnerCS:

    pass
class basecs_RootPackageCS(RootCS, PackageOwnerCS):

    pass
class FeatureCS:

    pass
class ModelElementCS:

    pass
class basecs_RootCS(ModelElementCS):

    pass
class basecs_PackageOwnerCS(ModelElementCS):

    pass
class basecs_TypeCS(ModelElementCS):

    pass
class basecs_TemplateParameterSubstitutionCS(ModelElementCS):

    pass
class basecs_TemplateSignatureCS(ModelElementCS):

    pass
class ElementCS:

    pass
class basecs_TemplateableElementCS(ElementCS):

    pass
class basecs_PivotableElementCS(ElementCS, Pivotable):

    pass
class basecs_PathElementCS(ElementCS, Pivotable):

    pass
class basecs_MultiplicityCS(ElementCS):

    def __init__(self, basecs_MultiplicityCS: "basecs_TypedRefCS" = None):
        self.basecs_MultiplicityCS = basecs_MultiplicityCS
        
    @property
    def basecs_MultiplicityCS(self):
        return self.__basecs_MultiplicityCS

    @basecs_MultiplicityCS.setter
    def basecs_MultiplicityCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_MultiplicityCS__basecs_MultiplicityCS", None)
        self.__basecs_MultiplicityCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_TypedRefCS107"):
                opp_val = getattr(old_value, "basecs_TypedRefCS107", None)
                if opp_val == self:
                    setattr(old_value, "basecs_TypedRefCS107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_TypedRefCS107"):
                opp_val = getattr(value, "basecs_TypedRefCS107", None)
                setattr(value, "basecs_TypedRefCS107", self)

    def getLower(self) -> int:
        # TODO: Implement getLower method
        pass

    def getUpper(self) -> int:
        # TODO: Implement getUpper method
        pass

class MultiplicityCS:

    pass
class basecs_MultiplicityStringCS(MultiplicityCS):

    def __init__(self, stringBounds: str):
        self.stringBounds = stringBounds
        
    @property
    def stringBounds(self) -> str:
        return self.__stringBounds

    @stringBounds.setter
    def stringBounds(self, stringBounds: str):
        self.__stringBounds = stringBounds

class basecs_MultiplicityBoundsCS(MultiplicityCS):

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

class basecs_Element:

    pass
class ElementRefCS:

    pass
class basecs_TypeRefCS(ElementRefCS):

    pass
class basecs_TemplateBindingCS(ElementRefCS):

    pass
class Nameable:

    pass
class basecs_NamedElementCS(Nameable, ModelElementCS):

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
class basecs_PrimitiveTypeRefCS(Nameable, TypedRefCS):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class basecs_TypedTypeRefCS(TypedRefCS):

    pass
class basecs_TupleTypeCS(Nameable, TypedRefCS):

    def __init__(self, name: str, basecs_TupleTypeCS: set["basecs_TuplePartCS"] = None):
        self.name = name
        self.basecs_TupleTypeCS = basecs_TupleTypeCS if basecs_TupleTypeCS is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def basecs_TupleTypeCS(self):
        return self.__basecs_TupleTypeCS

    @basecs_TupleTypeCS.setter
    def basecs_TupleTypeCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_TupleTypeCS__basecs_TupleTypeCS", None)
        self.__basecs_TupleTypeCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basecs_TuplePartCS"):
                    opp_val = getattr(item, "basecs_TuplePartCS", None)
                    
                    if opp_val == self:
                        setattr(item, "basecs_TuplePartCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basecs_TuplePartCS"):
                    opp_val = getattr(item, "basecs_TuplePartCS", None)
                    
                    setattr(item, "basecs_TuplePartCS", self)
                    

class basecs_Namespace:

    pass
class basecs_PathNameCS(ElementCS, Pivotable):

    def __init__(self, scopeFilter: str, basecs_PathNameCS: "basecs_ImportCS" = None, basecs_PathNameCS40: "basecs_ModelElementRefCS" = None, PathNameCS: "basecs_PathElementCS" = None, pathName: set["basecs_PathElementCS"] = None, basecs_PathNameCS69: "basecs_Element" = None, basecs_PathNameCS72: "basecs_ElementCS" = None, basecs_PathNameCS109: "basecs_TypedTypeRefCS" = None):
        self.scopeFilter = scopeFilter
        self.basecs_PathNameCS = basecs_PathNameCS
        self.basecs_PathNameCS40 = basecs_PathNameCS40
        self.PathNameCS = PathNameCS
        self.pathName = pathName if pathName is not None else set()
        self.basecs_PathNameCS69 = basecs_PathNameCS69
        self.basecs_PathNameCS72 = basecs_PathNameCS72
        self.basecs_PathNameCS109 = basecs_PathNameCS109
        
    @property
    def scopeFilter(self) -> str:
        return self.__scopeFilter

    @scopeFilter.setter
    def scopeFilter(self, scopeFilter: str):
        self.__scopeFilter = scopeFilter

    @property
    def PathNameCS(self):
        return self.__PathNameCS

    @PathNameCS.setter
    def PathNameCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_PathNameCS__PathNameCS", None)
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
    def basecs_PathNameCS69(self):
        return self.__basecs_PathNameCS69

    @basecs_PathNameCS69.setter
    def basecs_PathNameCS69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_PathNameCS__basecs_PathNameCS69", None)
        self.__basecs_PathNameCS69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_Element70"):
                opp_val = getattr(old_value, "basecs_Element70", None)
                if opp_val == self:
                    setattr(old_value, "basecs_Element70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_Element70"):
                opp_val = getattr(value, "basecs_Element70", None)
                setattr(value, "basecs_Element70", self)

    @property
    def basecs_PathNameCS109(self):
        return self.__basecs_PathNameCS109

    @basecs_PathNameCS109.setter
    def basecs_PathNameCS109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_PathNameCS__basecs_PathNameCS109", None)
        self.__basecs_PathNameCS109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_TypedTypeRefCS"):
                opp_val = getattr(old_value, "basecs_TypedTypeRefCS", None)
                if opp_val == self:
                    setattr(old_value, "basecs_TypedTypeRefCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_TypedTypeRefCS"):
                opp_val = getattr(value, "basecs_TypedTypeRefCS", None)
                setattr(value, "basecs_TypedTypeRefCS", self)

    @property
    def basecs_PathNameCS(self):
        return self.__basecs_PathNameCS

    @basecs_PathNameCS.setter
    def basecs_PathNameCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_PathNameCS__basecs_PathNameCS", None)
        self.__basecs_PathNameCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_ImportCS"):
                opp_val = getattr(old_value, "basecs_ImportCS", None)
                if opp_val == self:
                    setattr(old_value, "basecs_ImportCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_ImportCS"):
                opp_val = getattr(value, "basecs_ImportCS", None)
                setattr(value, "basecs_ImportCS", self)

    @property
    def basecs_PathNameCS72(self):
        return self.__basecs_PathNameCS72

    @basecs_PathNameCS72.setter
    def basecs_PathNameCS72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_PathNameCS__basecs_PathNameCS72", None)
        self.__basecs_PathNameCS72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_ElementCS73"):
                opp_val = getattr(old_value, "basecs_ElementCS73", None)
                if opp_val == self:
                    setattr(old_value, "basecs_ElementCS73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_ElementCS73"):
                opp_val = getattr(value, "basecs_ElementCS73", None)
                setattr(value, "basecs_ElementCS73", self)

    @property
    def pathName(self):
        return self.__pathName

    @pathName.setter
    def pathName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_PathNameCS__pathName", None)
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
                    

    @property
    def basecs_PathNameCS40(self):
        return self.__basecs_PathNameCS40

    @basecs_PathNameCS40.setter
    def basecs_PathNameCS40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_PathNameCS__basecs_PathNameCS40", None)
        self.__basecs_PathNameCS40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_ModelElementRefCS39"):
                opp_val = getattr(old_value, "basecs_ModelElementRefCS39", None)
                if opp_val == self:
                    setattr(old_value, "basecs_ModelElementRefCS39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_ModelElementRefCS39"):
                opp_val = getattr(value, "basecs_ModelElementRefCS39", None)
                setattr(value, "basecs_ModelElementRefCS39", self)

class TypedElementCS:

    pass
class basecs_ParameterCS(TypedElementCS):

    def __init__(self, ParameterCS: "basecs_OperationCS" = None, ownedParameter: "basecs_OperationCS" = None):
        self.ParameterCS = ParameterCS
        self.ownedParameter = ownedParameter
        
    @property
    def ownedParameter(self):
        return self.__ownedParameter

    @ownedParameter.setter
    def ownedParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_ParameterCS__ownedParameter", None)
        self.__ownedParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationCS61"):
                opp_val = getattr(old_value, "OperationCS61", None)
                if opp_val == self:
                    setattr(old_value, "OperationCS61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationCS61"):
                opp_val = getattr(value, "OperationCS61", None)
                setattr(value, "OperationCS61", self)

    @property
    def ParameterCS(self):
        return self.__ParameterCS

    @ParameterCS.setter
    def ParameterCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_ParameterCS__ParameterCS", None)
        self.__ParameterCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner45"):
                opp_val = getattr(old_value, "owner45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner45"):
                opp_val = getattr(value, "owner45", None)
                if opp_val is None:
                    setattr(value, "owner45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def ast(self) -> str:
        # TODO: Implement ast method
        pass

class basecs_TuplePartCS(TypedElementCS):

    pass
class basecs_FeatureCS(TypedElementCS):

    pass
class PivotableElementCS:

    pass
class basecs_ElementRefCS(PivotableElementCS):

    pass
class VisitableCS:

    pass
class basecs_ElementCS(VisitableCS):

    def __init__(self, basecs_ElementCS: "basecs_ElementCS" = None, basecs_ElementCS18: "basecs_ElementCS" = None, basecs_ElementCS73: "basecs_PathNameCS" = None):
        self.basecs_ElementCS = basecs_ElementCS
        self.basecs_ElementCS18 = basecs_ElementCS18
        self.basecs_ElementCS73 = basecs_ElementCS73
        
    @property
    def basecs_ElementCS18(self):
        return self.__basecs_ElementCS18

    @basecs_ElementCS18.setter
    def basecs_ElementCS18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_ElementCS__basecs_ElementCS18", None)
        self.__basecs_ElementCS18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_ElementCS"):
                opp_val = getattr(old_value, "basecs_ElementCS", None)
                if opp_val == self:
                    setattr(old_value, "basecs_ElementCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_ElementCS"):
                opp_val = getattr(value, "basecs_ElementCS", None)
                setattr(value, "basecs_ElementCS", self)

    @property
    def basecs_ElementCS73(self):
        return self.__basecs_ElementCS73

    @basecs_ElementCS73.setter
    def basecs_ElementCS73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_ElementCS__basecs_ElementCS73", None)
        self.__basecs_ElementCS73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_PathNameCS72"):
                opp_val = getattr(old_value, "basecs_PathNameCS72", None)
                if opp_val == self:
                    setattr(old_value, "basecs_PathNameCS72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_PathNameCS72"):
                opp_val = getattr(value, "basecs_PathNameCS72", None)
                setattr(value, "basecs_PathNameCS72", self)

    @property
    def basecs_ElementCS(self):
        return self.__basecs_ElementCS

    @basecs_ElementCS.setter
    def basecs_ElementCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_ElementCS__basecs_ElementCS", None)
        self.__basecs_ElementCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_ElementCS18"):
                opp_val = getattr(old_value, "basecs_ElementCS18", None)
                if opp_val == self:
                    setattr(old_value, "basecs_ElementCS18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_ElementCS18"):
                opp_val = getattr(value, "basecs_ElementCS18", None)
                setattr(value, "basecs_ElementCS18", self)

    def getDescription(self) -> str:
        # TODO: Implement getDescription method
        pass

class basecs_SpecificationCS(ModelElementCS):

    def __init__(self, exprString: str, basecs_SpecificationCS: "basecs_ConstraintCS" = None, basecs_SpecificationCS16: "basecs_ConstraintCS" = None, basecs_SpecificationCS56: "basecs_OperationCS" = None, basecs_SpecificationCS88: "basecs_StructuralFeatureCS" = None):
        self.exprString = exprString
        self.basecs_SpecificationCS = basecs_SpecificationCS
        self.basecs_SpecificationCS16 = basecs_SpecificationCS16
        self.basecs_SpecificationCS56 = basecs_SpecificationCS56
        self.basecs_SpecificationCS88 = basecs_SpecificationCS88
        
    @property
    def exprString(self) -> str:
        return self.__exprString

    @exprString.setter
    def exprString(self, exprString: str):
        self.__exprString = exprString

    @property
    def basecs_SpecificationCS(self):
        return self.__basecs_SpecificationCS

    @basecs_SpecificationCS.setter
    def basecs_SpecificationCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_SpecificationCS__basecs_SpecificationCS", None)
        self.__basecs_SpecificationCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_ConstraintCS13"):
                opp_val = getattr(old_value, "basecs_ConstraintCS13", None)
                if opp_val == self:
                    setattr(old_value, "basecs_ConstraintCS13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_ConstraintCS13"):
                opp_val = getattr(value, "basecs_ConstraintCS13", None)
                setattr(value, "basecs_ConstraintCS13", self)

    @property
    def basecs_SpecificationCS16(self):
        return self.__basecs_SpecificationCS16

    @basecs_SpecificationCS16.setter
    def basecs_SpecificationCS16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_SpecificationCS__basecs_SpecificationCS16", None)
        self.__basecs_SpecificationCS16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_ConstraintCS15"):
                opp_val = getattr(old_value, "basecs_ConstraintCS15", None)
                if opp_val == self:
                    setattr(old_value, "basecs_ConstraintCS15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_ConstraintCS15"):
                opp_val = getattr(value, "basecs_ConstraintCS15", None)
                setattr(value, "basecs_ConstraintCS15", self)

    @property
    def basecs_SpecificationCS88(self):
        return self.__basecs_SpecificationCS88

    @basecs_SpecificationCS88.setter
    def basecs_SpecificationCS88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_SpecificationCS__basecs_SpecificationCS88", None)
        self.__basecs_SpecificationCS88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_StructuralFeatureCS"):
                opp_val = getattr(old_value, "basecs_StructuralFeatureCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_StructuralFeatureCS"):
                opp_val = getattr(value, "basecs_StructuralFeatureCS", None)
                if opp_val is None:
                    setattr(value, "basecs_StructuralFeatureCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def basecs_SpecificationCS56(self):
        return self.__basecs_SpecificationCS56

    @basecs_SpecificationCS56.setter
    def basecs_SpecificationCS56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_SpecificationCS__basecs_SpecificationCS56", None)
        self.__basecs_SpecificationCS56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_OperationCS55"):
                opp_val = getattr(old_value, "basecs_OperationCS55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_OperationCS55"):
                opp_val = getattr(value, "basecs_OperationCS55", None)
                if opp_val is None:
                    setattr(value, "basecs_OperationCS55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TemplateableElementCS:

    pass
class basecs_LambdaTypeCS(Nameable, TypedRefCS, TemplateableElementCS):

    def __init__(self, name: str, basecs_LambdaTypeCS: "basecs_TypedRefCS" = None, basecs_LambdaTypeCS28: set["basecs_TypedRefCS"] = None, basecs_LambdaTypeCS31: "basecs_TypedRefCS" = None):
        self.name = name
        self.basecs_LambdaTypeCS = basecs_LambdaTypeCS
        self.basecs_LambdaTypeCS28 = basecs_LambdaTypeCS28 if basecs_LambdaTypeCS28 is not None else set()
        self.basecs_LambdaTypeCS31 = basecs_LambdaTypeCS31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def basecs_LambdaTypeCS31(self):
        return self.__basecs_LambdaTypeCS31

    @basecs_LambdaTypeCS31.setter
    def basecs_LambdaTypeCS31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_LambdaTypeCS__basecs_LambdaTypeCS31", None)
        self.__basecs_LambdaTypeCS31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_TypedRefCS32"):
                opp_val = getattr(old_value, "basecs_TypedRefCS32", None)
                if opp_val == self:
                    setattr(old_value, "basecs_TypedRefCS32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_TypedRefCS32"):
                opp_val = getattr(value, "basecs_TypedRefCS32", None)
                setattr(value, "basecs_TypedRefCS32", self)

    @property
    def basecs_LambdaTypeCS(self):
        return self.__basecs_LambdaTypeCS

    @basecs_LambdaTypeCS.setter
    def basecs_LambdaTypeCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_LambdaTypeCS__basecs_LambdaTypeCS", None)
        self.__basecs_LambdaTypeCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_TypedRefCS26"):
                opp_val = getattr(old_value, "basecs_TypedRefCS26", None)
                if opp_val == self:
                    setattr(old_value, "basecs_TypedRefCS26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_TypedRefCS26"):
                opp_val = getattr(value, "basecs_TypedRefCS26", None)
                setattr(value, "basecs_TypedRefCS26", self)

    @property
    def basecs_LambdaTypeCS28(self):
        return self.__basecs_LambdaTypeCS28

    @basecs_LambdaTypeCS28.setter
    def basecs_LambdaTypeCS28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_LambdaTypeCS__basecs_LambdaTypeCS28", None)
        self.__basecs_LambdaTypeCS28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basecs_TypedRefCS29"):
                    opp_val = getattr(item, "basecs_TypedRefCS29", None)
                    
                    if opp_val == self:
                        setattr(item, "basecs_TypedRefCS29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basecs_TypedRefCS29"):
                    opp_val = getattr(item, "basecs_TypedRefCS29", None)
                    
                    setattr(item, "basecs_TypedRefCS29", self)
                    

class TypeCS:

    pass
class basecs_TypeParameterCS(TemplateParameterCS, TypeCS):

    pass
class basecs_StructuralFeatureCS(FeatureCS):

    def __init__(self, default: str, StructuralFeatureCS: "basecs_ClassCS" = None, ownedProperty: "basecs_ClassCS" = None, basecs_StructuralFeatureCS: set["basecs_SpecificationCS"] = None):
        self.default = default
        self.StructuralFeatureCS = StructuralFeatureCS
        self.ownedProperty = ownedProperty
        self.basecs_StructuralFeatureCS = basecs_StructuralFeatureCS if basecs_StructuralFeatureCS is not None else set()
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def ownedProperty(self):
        return self.__ownedProperty

    @ownedProperty.setter
    def ownedProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_StructuralFeatureCS__ownedProperty", None)
        self.__ownedProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassCS86"):
                opp_val = getattr(old_value, "ClassCS86", None)
                if opp_val == self:
                    setattr(old_value, "ClassCS86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassCS86"):
                opp_val = getattr(value, "ClassCS86", None)
                setattr(value, "ClassCS86", self)

    @property
    def basecs_StructuralFeatureCS(self):
        return self.__basecs_StructuralFeatureCS

    @basecs_StructuralFeatureCS.setter
    def basecs_StructuralFeatureCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_StructuralFeatureCS__basecs_StructuralFeatureCS", None)
        self.__basecs_StructuralFeatureCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basecs_SpecificationCS88"):
                    opp_val = getattr(item, "basecs_SpecificationCS88", None)
                    
                    if opp_val == self:
                        setattr(item, "basecs_SpecificationCS88", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basecs_SpecificationCS88"):
                    opp_val = getattr(item, "basecs_SpecificationCS88", None)
                    
                    setattr(item, "basecs_SpecificationCS88", self)
                    

    @property
    def StructuralFeatureCS(self):
        return self.__StructuralFeatureCS

    @StructuralFeatureCS.setter
    def StructuralFeatureCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_StructuralFeatureCS__StructuralFeatureCS", None)
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

    def ast(self) -> str:
        # TODO: Implement ast method
        pass

class basecs_OperationCS(TemplateableElementCS, FeatureCS):

    def __init__(self, OperationCS: "basecs_ClassCS" = None, ownedOperation: "basecs_ClassCS" = None, owner45: set["basecs_ParameterCS"] = None, basecs_OperationCS: set["basecs_TypedRefCS"] = None, basecs_OperationCS49: set["basecs_ConstraintCS"] = None, basecs_OperationCS52: set["basecs_ConstraintCS"] = None, basecs_OperationCS55: set["basecs_SpecificationCS"] = None, OperationCS61: "basecs_ParameterCS" = None):
        self.OperationCS = OperationCS
        self.ownedOperation = ownedOperation
        self.owner45 = owner45 if owner45 is not None else set()
        self.basecs_OperationCS = basecs_OperationCS if basecs_OperationCS is not None else set()
        self.basecs_OperationCS49 = basecs_OperationCS49 if basecs_OperationCS49 is not None else set()
        self.basecs_OperationCS52 = basecs_OperationCS52 if basecs_OperationCS52 is not None else set()
        self.basecs_OperationCS55 = basecs_OperationCS55 if basecs_OperationCS55 is not None else set()
        self.OperationCS61 = OperationCS61
        
    @property
    def basecs_OperationCS52(self):
        return self.__basecs_OperationCS52

    @basecs_OperationCS52.setter
    def basecs_OperationCS52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_OperationCS__basecs_OperationCS52", None)
        self.__basecs_OperationCS52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basecs_ConstraintCS53"):
                    opp_val = getattr(item, "basecs_ConstraintCS53", None)
                    
                    if opp_val == self:
                        setattr(item, "basecs_ConstraintCS53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basecs_ConstraintCS53"):
                    opp_val = getattr(item, "basecs_ConstraintCS53", None)
                    
                    setattr(item, "basecs_ConstraintCS53", self)
                    

    @property
    def OperationCS(self):
        return self.__OperationCS

    @OperationCS.setter
    def OperationCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_OperationCS__OperationCS", None)
        self.__OperationCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningClass"):
                opp_val = getattr(old_value, "owningClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningClass"):
                opp_val = getattr(value, "owningClass", None)
                if opp_val is None:
                    setattr(value, "owningClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def basecs_OperationCS(self):
        return self.__basecs_OperationCS

    @basecs_OperationCS.setter
    def basecs_OperationCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_OperationCS__basecs_OperationCS", None)
        self.__basecs_OperationCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basecs_TypedRefCS47"):
                    opp_val = getattr(item, "basecs_TypedRefCS47", None)
                    
                    if opp_val == self:
                        setattr(item, "basecs_TypedRefCS47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basecs_TypedRefCS47"):
                    opp_val = getattr(item, "basecs_TypedRefCS47", None)
                    
                    setattr(item, "basecs_TypedRefCS47", self)
                    

    @property
    def basecs_OperationCS49(self):
        return self.__basecs_OperationCS49

    @basecs_OperationCS49.setter
    def basecs_OperationCS49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_OperationCS__basecs_OperationCS49", None)
        self.__basecs_OperationCS49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basecs_ConstraintCS50"):
                    opp_val = getattr(item, "basecs_ConstraintCS50", None)
                    
                    if opp_val == self:
                        setattr(item, "basecs_ConstraintCS50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basecs_ConstraintCS50"):
                    opp_val = getattr(item, "basecs_ConstraintCS50", None)
                    
                    setattr(item, "basecs_ConstraintCS50", self)
                    

    @property
    def basecs_OperationCS55(self):
        return self.__basecs_OperationCS55

    @basecs_OperationCS55.setter
    def basecs_OperationCS55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_OperationCS__basecs_OperationCS55", None)
        self.__basecs_OperationCS55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basecs_SpecificationCS56"):
                    opp_val = getattr(item, "basecs_SpecificationCS56", None)
                    
                    if opp_val == self:
                        setattr(item, "basecs_SpecificationCS56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basecs_SpecificationCS56"):
                    opp_val = getattr(item, "basecs_SpecificationCS56", None)
                    
                    setattr(item, "basecs_SpecificationCS56", self)
                    

    @property
    def OperationCS61(self):
        return self.__OperationCS61

    @OperationCS61.setter
    def OperationCS61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_OperationCS__OperationCS61", None)
        self.__OperationCS61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedParameter"):
                opp_val = getattr(old_value, "ownedParameter", None)
                if opp_val == self:
                    setattr(old_value, "ownedParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedParameter"):
                opp_val = getattr(value, "ownedParameter", None)
                setattr(value, "ownedParameter", self)

    @property
    def owner45(self):
        return self.__owner45

    @owner45.setter
    def owner45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_OperationCS__owner45", None)
        self.__owner45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ParameterCS"):
                    opp_val = getattr(item, "ParameterCS", None)
                    
                    if opp_val == self:
                        setattr(item, "ParameterCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ParameterCS"):
                    opp_val = getattr(item, "ParameterCS", None)
                    
                    setattr(item, "ParameterCS", self)
                    

    @property
    def ownedOperation(self):
        return self.__ownedOperation

    @ownedOperation.setter
    def ownedOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_OperationCS__ownedOperation", None)
        self.__ownedOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassCS"):
                opp_val = getattr(old_value, "ClassCS", None)
                if opp_val == self:
                    setattr(old_value, "ClassCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassCS"):
                opp_val = getattr(value, "ClassCS", None)
                setattr(value, "ClassCS", self)

    def ast(self) -> str:
        # TODO: Implement ast method
        pass

class basecs_TypedRefCS(TypeRefCS):

    pass
class NamespaceCS:

    pass
class basecs_PackageCS(PackageOwnerCS, NamespaceCS):

    def __init__(self, nsPrefix: str, nsURI: str, PackageCS: "basecs_ClassifierCS" = None, owner58: set["basecs_ClassifierCS"] = None, basecs_PackageCS: "basecs_PackageOwnerCS" = None):
        self.nsPrefix = nsPrefix
        self.nsURI = nsURI
        self.PackageCS = PackageCS
        self.owner58 = owner58 if owner58 is not None else set()
        self.basecs_PackageCS = basecs_PackageCS
        
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
    def basecs_PackageCS(self):
        return self.__basecs_PackageCS

    @basecs_PackageCS.setter
    def basecs_PackageCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_PackageCS__basecs_PackageCS", None)
        self.__basecs_PackageCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_PackageOwnerCS"):
                opp_val = getattr(old_value, "basecs_PackageOwnerCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_PackageOwnerCS"):
                opp_val = getattr(value, "basecs_PackageOwnerCS", None)
                if opp_val is None:
                    setattr(value, "basecs_PackageOwnerCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PackageCS(self):
        return self.__PackageCS

    @PackageCS.setter
    def PackageCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_PackageCS__PackageCS", None)
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
    def owner58(self):
        return self.__owner58

    @owner58.setter
    def owner58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_PackageCS__owner58", None)
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
                    

    def ast(self) -> str:
        # TODO: Implement ast method
        pass

    def getClassifier(self, name: str) -> ClassifierCS:
        # TODO: Implement getClassifier method
        pass

class basecs_ImportCS(NamespaceCS):

    def __init__(self, all: bool, basecs_ImportCS: "basecs_PathNameCS" = None, basecs_ImportCS24: "basecs_Namespace" = None, basecs_ImportCS81: "basecs_RootCS" = None):
        self.all = all
        self.basecs_ImportCS = basecs_ImportCS
        self.basecs_ImportCS24 = basecs_ImportCS24
        self.basecs_ImportCS81 = basecs_ImportCS81
        
    @property
    def all(self) -> bool:
        return self.__all

    @all.setter
    def all(self, all: bool):
        self.__all = all

    @property
    def basecs_ImportCS81(self):
        return self.__basecs_ImportCS81

    @basecs_ImportCS81.setter
    def basecs_ImportCS81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_ImportCS__basecs_ImportCS81", None)
        self.__basecs_ImportCS81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_RootCS"):
                opp_val = getattr(old_value, "basecs_RootCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_RootCS"):
                opp_val = getattr(value, "basecs_RootCS", None)
                if opp_val is None:
                    setattr(value, "basecs_RootCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def basecs_ImportCS24(self):
        return self.__basecs_ImportCS24

    @basecs_ImportCS24.setter
    def basecs_ImportCS24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_ImportCS__basecs_ImportCS24", None)
        self.__basecs_ImportCS24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_Namespace"):
                opp_val = getattr(old_value, "basecs_Namespace", None)
                if opp_val == self:
                    setattr(old_value, "basecs_Namespace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_Namespace"):
                opp_val = getattr(value, "basecs_Namespace", None)
                setattr(value, "basecs_Namespace", self)

    @property
    def basecs_ImportCS(self):
        return self.__basecs_ImportCS

    @basecs_ImportCS.setter
    def basecs_ImportCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_ImportCS__basecs_ImportCS", None)
        self.__basecs_ImportCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_PathNameCS"):
                opp_val = getattr(old_value, "basecs_PathNameCS", None)
                if opp_val == self:
                    setattr(old_value, "basecs_PathNameCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_PathNameCS"):
                opp_val = getattr(value, "basecs_PathNameCS", None)
                setattr(value, "basecs_PathNameCS", self)

class basecs_LibraryCS(NamespaceCS):

    pass
class ClassifierCS:

    pass
class basecs_DataTypeCS(ClassifierCS, NamespaceCS):

    pass
class basecs_EnumerationCS(ClassifierCS, NamespaceCS):

    def __init__(self, basecs_EnumerationCS: set["basecs_EnumerationLiteralCS"] = None):
        self.basecs_EnumerationCS = basecs_EnumerationCS if basecs_EnumerationCS is not None else set()
        
    @property
    def basecs_EnumerationCS(self):
        return self.__basecs_EnumerationCS

    @basecs_EnumerationCS.setter
    def basecs_EnumerationCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_EnumerationCS__basecs_EnumerationCS", None)
        self.__basecs_EnumerationCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basecs_EnumerationLiteralCS21"):
                    opp_val = getattr(item, "basecs_EnumerationLiteralCS21", None)
                    
                    if opp_val == self:
                        setattr(item, "basecs_EnumerationLiteralCS21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basecs_EnumerationLiteralCS21"):
                    opp_val = getattr(item, "basecs_EnumerationLiteralCS21", None)
                    
                    setattr(item, "basecs_EnumerationLiteralCS21", self)
                    

    def ast(self) -> str:
        # TODO: Implement ast method
        pass

class basecs_ClassCS(ClassifierCS, NamespaceCS):

    pass
class StructuralFeatureCS:

    pass
class basecs_ReferenceCS(StructuralFeatureCS):

    pass
class basecs_AttributeCS(StructuralFeatureCS):

    pass
class NamedElementCS:

    pass
class basecs_TemplateParameterCS(NamedElementCS):

    pass
class basecs_EnumerationLiteralCS(NamedElementCS):

    def __init__(self, value: int, basecs_EnumerationLiteralCS: "basecs_DataTypeCS" = None, basecs_EnumerationLiteralCS21: "basecs_EnumerationCS" = None):
        self.value = value
        self.basecs_EnumerationLiteralCS = basecs_EnumerationLiteralCS
        self.basecs_EnumerationLiteralCS21 = basecs_EnumerationLiteralCS21
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def basecs_EnumerationLiteralCS(self):
        return self.__basecs_EnumerationLiteralCS

    @basecs_EnumerationLiteralCS.setter
    def basecs_EnumerationLiteralCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_EnumerationLiteralCS__basecs_EnumerationLiteralCS", None)
        self.__basecs_EnumerationLiteralCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_DataTypeCS"):
                opp_val = getattr(old_value, "basecs_DataTypeCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_DataTypeCS"):
                opp_val = getattr(value, "basecs_DataTypeCS", None)
                if opp_val is None:
                    setattr(value, "basecs_DataTypeCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def basecs_EnumerationLiteralCS21(self):
        return self.__basecs_EnumerationLiteralCS21

    @basecs_EnumerationLiteralCS21.setter
    def basecs_EnumerationLiteralCS21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_EnumerationLiteralCS__basecs_EnumerationLiteralCS21", None)
        self.__basecs_EnumerationLiteralCS21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_EnumerationCS"):
                opp_val = getattr(old_value, "basecs_EnumerationCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_EnumerationCS"):
                opp_val = getattr(value, "basecs_EnumerationCS", None)
                if opp_val is None:
                    setattr(value, "basecs_EnumerationCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def ast(self) -> str:
        # TODO: Implement ast method
        pass

class basecs_DetailCS(NamedElementCS):

    def __init__(self, value: str, basecs_DetailCS: "basecs_AnnotationElementCS" = None):
        self.value = value
        self.basecs_DetailCS = basecs_DetailCS
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def basecs_DetailCS(self):
        return self.__basecs_DetailCS

    @basecs_DetailCS.setter
    def basecs_DetailCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_DetailCS__basecs_DetailCS", None)
        self.__basecs_DetailCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_AnnotationElementCS"):
                opp_val = getattr(old_value, "basecs_AnnotationElementCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_AnnotationElementCS"):
                opp_val = getattr(value, "basecs_AnnotationElementCS", None)
                if opp_val is None:
                    setattr(value, "basecs_AnnotationElementCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class basecs_ClassifierCS(NamedElementCS, TemplateableElementCS, TypeCS):

    def __init__(self, instanceClassName: str, qualifier: str, ownedType: "basecs_PackageCS" = None, basecs_ClassifierCS: set["basecs_ConstraintCS"] = None, ClassifierCS: "basecs_PackageCS" = None):
        self.instanceClassName = instanceClassName
        self.qualifier = qualifier
        self.ownedType = ownedType
        self.basecs_ClassifierCS = basecs_ClassifierCS if basecs_ClassifierCS is not None else set()
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
    def ownedType(self):
        return self.__ownedType

    @ownedType.setter
    def ownedType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_ClassifierCS__ownedType", None)
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
    def basecs_ClassifierCS(self):
        return self.__basecs_ClassifierCS

    @basecs_ClassifierCS.setter
    def basecs_ClassifierCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_ClassifierCS__basecs_ClassifierCS", None)
        self.__basecs_ClassifierCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basecs_ConstraintCS"):
                    opp_val = getattr(item, "basecs_ConstraintCS", None)
                    
                    if opp_val == self:
                        setattr(item, "basecs_ConstraintCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basecs_ConstraintCS"):
                    opp_val = getattr(item, "basecs_ConstraintCS", None)
                    
                    setattr(item, "basecs_ConstraintCS", self)
                    

    @property
    def ClassifierCS(self):
        return self.__ClassifierCS

    @ClassifierCS.setter
    def ClassifierCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_ClassifierCS__ClassifierCS", None)
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

    def ast(self) -> str:
        # TODO: Implement ast method
        pass

class basecs_NamespaceCS(NamedElementCS):

    pass
class basecs_ConstraintCS(NamedElementCS):

    def __init__(self, stereotype: str, basecs_ConstraintCS: "basecs_ClassifierCS" = None, basecs_ConstraintCS13: "basecs_SpecificationCS" = None, basecs_ConstraintCS15: "basecs_SpecificationCS" = None, basecs_ConstraintCS50: "basecs_OperationCS" = None, basecs_ConstraintCS53: "basecs_OperationCS" = None):
        self.stereotype = stereotype
        self.basecs_ConstraintCS = basecs_ConstraintCS
        self.basecs_ConstraintCS13 = basecs_ConstraintCS13
        self.basecs_ConstraintCS15 = basecs_ConstraintCS15
        self.basecs_ConstraintCS50 = basecs_ConstraintCS50
        self.basecs_ConstraintCS53 = basecs_ConstraintCS53
        
    @property
    def stereotype(self) -> str:
        return self.__stereotype

    @stereotype.setter
    def stereotype(self, stereotype: str):
        self.__stereotype = stereotype

    @property
    def basecs_ConstraintCS13(self):
        return self.__basecs_ConstraintCS13

    @basecs_ConstraintCS13.setter
    def basecs_ConstraintCS13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_ConstraintCS__basecs_ConstraintCS13", None)
        self.__basecs_ConstraintCS13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_SpecificationCS"):
                opp_val = getattr(old_value, "basecs_SpecificationCS", None)
                if opp_val == self:
                    setattr(old_value, "basecs_SpecificationCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_SpecificationCS"):
                opp_val = getattr(value, "basecs_SpecificationCS", None)
                setattr(value, "basecs_SpecificationCS", self)

    @property
    def basecs_ConstraintCS53(self):
        return self.__basecs_ConstraintCS53

    @basecs_ConstraintCS53.setter
    def basecs_ConstraintCS53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_ConstraintCS__basecs_ConstraintCS53", None)
        self.__basecs_ConstraintCS53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_OperationCS52"):
                opp_val = getattr(old_value, "basecs_OperationCS52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_OperationCS52"):
                opp_val = getattr(value, "basecs_OperationCS52", None)
                if opp_val is None:
                    setattr(value, "basecs_OperationCS52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def basecs_ConstraintCS15(self):
        return self.__basecs_ConstraintCS15

    @basecs_ConstraintCS15.setter
    def basecs_ConstraintCS15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_ConstraintCS__basecs_ConstraintCS15", None)
        self.__basecs_ConstraintCS15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_SpecificationCS16"):
                opp_val = getattr(old_value, "basecs_SpecificationCS16", None)
                if opp_val == self:
                    setattr(old_value, "basecs_SpecificationCS16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_SpecificationCS16"):
                opp_val = getattr(value, "basecs_SpecificationCS16", None)
                setattr(value, "basecs_SpecificationCS16", self)

    @property
    def basecs_ConstraintCS(self):
        return self.__basecs_ConstraintCS

    @basecs_ConstraintCS.setter
    def basecs_ConstraintCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_ConstraintCS__basecs_ConstraintCS", None)
        self.__basecs_ConstraintCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_ClassifierCS"):
                opp_val = getattr(old_value, "basecs_ClassifierCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_ClassifierCS"):
                opp_val = getattr(value, "basecs_ClassifierCS", None)
                if opp_val is None:
                    setattr(value, "basecs_ClassifierCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def basecs_ConstraintCS50(self):
        return self.__basecs_ConstraintCS50

    @basecs_ConstraintCS50.setter
    def basecs_ConstraintCS50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_ConstraintCS__basecs_ConstraintCS50", None)
        self.__basecs_ConstraintCS50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_OperationCS49"):
                opp_val = getattr(old_value, "basecs_OperationCS49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_OperationCS49"):
                opp_val = getattr(value, "basecs_OperationCS49", None)
                if opp_val is None:
                    setattr(value, "basecs_OperationCS49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class basecs_TypedElementCS(NamedElementCS):

    def __init__(self, qualifier: str, optional: bool, basecs_TypedElementCS: "basecs_TypedRefCS" = None):
        self.qualifier = qualifier
        self.optional = optional
        self.basecs_TypedElementCS = basecs_TypedElementCS
        
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
    def basecs_TypedElementCS(self):
        return self.__basecs_TypedElementCS

    @basecs_TypedElementCS.setter
    def basecs_TypedElementCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_TypedElementCS__basecs_TypedElementCS", None)
        self.__basecs_TypedElementCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_TypedRefCS105"):
                opp_val = getattr(old_value, "basecs_TypedRefCS105", None)
                if opp_val == self:
                    setattr(old_value, "basecs_TypedRefCS105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_TypedRefCS105"):
                opp_val = getattr(value, "basecs_TypedRefCS105", None)
                setattr(value, "basecs_TypedRefCS105", self)

class basecs_AnnotationElementCS(NamedElementCS):

    pass
class basecs_ModelElementRefCS(ElementRefCS):

    pass
class basecs_ModelElementCS(PivotableElementCS):

    def __init__(self, originalXmiId: str, csi: str, basecs_ModelElementCS: "basecs_AnnotationCS" = None, basecs_ModelElementCS36: set["basecs_AnnotationElementCS"] = None):
        self.originalXmiId = originalXmiId
        self.csi = csi
        self.basecs_ModelElementCS = basecs_ModelElementCS
        self.basecs_ModelElementCS36 = basecs_ModelElementCS36 if basecs_ModelElementCS36 is not None else set()
        
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
    def basecs_ModelElementCS36(self):
        return self.__basecs_ModelElementCS36

    @basecs_ModelElementCS36.setter
    def basecs_ModelElementCS36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_ModelElementCS__basecs_ModelElementCS36", None)
        self.__basecs_ModelElementCS36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basecs_AnnotationElementCS37"):
                    opp_val = getattr(item, "basecs_AnnotationElementCS37", None)
                    
                    if opp_val == self:
                        setattr(item, "basecs_AnnotationElementCS37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basecs_AnnotationElementCS37"):
                    opp_val = getattr(item, "basecs_AnnotationElementCS37", None)
                    
                    setattr(item, "basecs_AnnotationElementCS37", self)
                    

    @property
    def basecs_ModelElementCS(self):
        return self.__basecs_ModelElementCS

    @basecs_ModelElementCS.setter
    def basecs_ModelElementCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basecs_ModelElementCS__basecs_ModelElementCS", None)
        self.__basecs_ModelElementCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basecs_AnnotationCS"):
                opp_val = getattr(old_value, "basecs_AnnotationCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basecs_AnnotationCS"):
                opp_val = getattr(value, "basecs_AnnotationCS", None)
                if opp_val is None:
                    setattr(value, "basecs_AnnotationCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AnnotationElementCS:

    pass
class basecs_DocumentationCS(AnnotationElementCS):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class basecs_AnnotationCS(AnnotationElementCS):

    pass