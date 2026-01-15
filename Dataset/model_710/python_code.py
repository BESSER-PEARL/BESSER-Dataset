from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PseudostateKind(Enum):
    initial = "initial"
    deepHistory = "deepHistory"
    shallowHistory = "shallowHistory"
    join = "join"
    entryPoint = "entryPoint"
    exitPoint = "exitPoint"
    terminate = "terminate"
    fork = "fork"
    junction = "junction"
    choice = "choice"
class CollectionKind(Enum):
    Collection = "Collection"
    Set = "Set"
    OrderedSet = "OrderedSet"
    Bag = "Bag"
    Sequence = "Sequence"
class AssociativityKind(Enum):
    Left = "Left"
    Right = "Right"
class TransitionKind(Enum):
    internal = "internal"
    local = "local"
    external = "external"


############################################
# Definition of Classes
############################################

class pivot_Visitor(ABC):

    pass
class pivot_Visitable(ABC):

    pass
class Behavior:

    pass
class pivot_ReferringElement(ABC):

    def __init__(self):
        
    def getReferredElement(self) -> Element:
        # TODO: Implement getReferredElement method
        pass

class pivot_StateMachine(Behavior):

    pass
class pivot_Pivotable(ABC):

    pass
class VariableDeclaration:

    pass
class pivot_TupleLiteralPart(VariableDeclaration):

    pass
class TemplateParameter:

    pass
class pivot_TypeTemplateParameter(TemplateParameter):

    def __init__(self, allowSubstitutable: str, pivot_TypeTemplateParameter: set["pivot_Type"] = None):
        self.allowSubstitutable = allowSubstitutable
        self.pivot_TypeTemplateParameter = pivot_TypeTemplateParameter if pivot_TypeTemplateParameter is not None else set()
        
    @property
    def allowSubstitutable(self) -> str:
        return self.__allowSubstitutable

    @allowSubstitutable.setter
    def allowSubstitutable(self, allowSubstitutable: str):
        self.__allowSubstitutable = allowSubstitutable

    @property
    def pivot_TypeTemplateParameter(self):
        return self.__pivot_TypeTemplateParameter

    @pivot_TypeTemplateParameter.setter
    def pivot_TypeTemplateParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_TypeTemplateParameter__pivot_TypeTemplateParameter", None)
        self.__pivot_TypeTemplateParameter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Type333"):
                    opp_val = getattr(item, "pivot_Type333", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Type333", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Type333"):
                    opp_val = getattr(item, "pivot_Type333", None)
                    
                    setattr(item, "pivot_Type333", self)
                    

class pivot_OperationTemplateParameter(TemplateParameter):

    pass
class ParameterableElement:

    pass
class pivot_PackageableElement(ParameterableElement):

    pass
class TemplateableElement:

    pass
class Feature:

    pass
class ValueSpecification:

    pass
class FeatureCallExp:

    pass
class pivot_NavigationCallExp(FeatureCallExp):

    pass
class Nameable:

    pass
class pivot_Nameable(ABC):

    pass
class pivot_MorePivotable(ABC):

    pass
class Package:

    pass
class pivot_Profile(Package):

    pass
class pivot_Library(Package):

    pass
class ReferringElement:

    pass
class pivot_OperationCallExp(FeatureCallExp, ReferringElement):

    def __init__(self, pivot_OperationCallExp: set["pivot_OCLExpression"] = None, pivot_OperationCallExp161: "pivot_Operation" = None):
        self.pivot_OperationCallExp = pivot_OperationCallExp if pivot_OperationCallExp is not None else set()
        self.pivot_OperationCallExp161 = pivot_OperationCallExp161
        
    @property
    def pivot_OperationCallExp(self):
        return self.__pivot_OperationCallExp

    @pivot_OperationCallExp.setter
    def pivot_OperationCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_OperationCallExp__pivot_OperationCallExp", None)
        self.__pivot_OperationCallExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_OCLExpression159"):
                    opp_val = getattr(item, "pivot_OCLExpression159", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_OCLExpression159", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_OCLExpression159"):
                    opp_val = getattr(item, "pivot_OCLExpression159", None)
                    
                    setattr(item, "pivot_OCLExpression159", self)
                    

    @property
    def pivot_OperationCallExp161(self):
        return self.__pivot_OperationCallExp161

    @pivot_OperationCallExp161.setter
    def pivot_OperationCallExp161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_OperationCallExp__pivot_OperationCallExp161", None)
        self.__pivot_OperationCallExp161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation162"):
                opp_val = getattr(old_value, "pivot_Operation162", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Operation162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation162"):
                opp_val = getattr(value, "pivot_Operation162", None)
                setattr(value, "pivot_Operation162", self)

    def ArgumentCount(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ArgumentCount method
        pass

    def ArgumentTypeIsConformant(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ArgumentTypeIsConformant method
        pass

class LoopExp:

    pass
class pivot_IteratorExp(LoopExp, ReferringElement):

    def __init__(self):
        
    def ExistsBodyTypeIsBoolean(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ExistsBodyTypeIsBoolean method
        pass

    def OneTypeIsBoolean(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OneTypeIsBoolean method
        pass

    def AnyBodyTypeIsBoolean(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AnyBodyTypeIsBoolean method
        pass

    def IsUniqueTypeIsBoolean(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement IsUniqueTypeIsBoolean method
        pass

    def CollectTypeIsUnordered(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CollectTypeIsUnordered method
        pass

    def SortedByIteratorTypeIsComparable(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SortedByIteratorTypeIsComparable method
        pass

    def CollectNestedTypeIsBag(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CollectNestedTypeIsBag method
        pass

    def OneHasOneIterator(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OneHasOneIterator method
        pass

    def RejectOrSelectTypeIsSourceType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RejectOrSelectTypeIsSourceType method
        pass

    def ForAllBodyTypeIsBoolean(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ForAllBodyTypeIsBoolean method
        pass

    def RejectOrSelectTypeIsBoolean(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RejectOrSelectTypeIsBoolean method
        pass

    def CollectNestedHasOneIterator(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CollectNestedHasOneIterator method
        pass

    def ClosureTypeIsUniqueCollection(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ClosureTypeIsUniqueCollection method
        pass

    def CollectNestedTypeIsBodyType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CollectNestedTypeIsBodyType method
        pass

    def RejectOrSelectHasOneIterator(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RejectOrSelectHasOneIterator method
        pass

    def IteratorTypeIsSourceElementType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement IteratorTypeIsSourceElementType method
        pass

    def ClosureElementTypeIsSourceElementType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ClosureElementTypeIsSourceElementType method
        pass

    def ExistsTypeIsBoolean(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ExistsTypeIsBoolean method
        pass

    def SortedByIsOrderedIfSourceIsOrdered(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SortedByIsOrderedIfSourceIsOrdered method
        pass

    def ForAllTypeIsBoolean(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ForAllTypeIsBoolean method
        pass

    def CollectElementTypeIsSourceElementType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CollectElementTypeIsSourceElementType method
        pass

    def OneBodyTypeIsBoolean(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement OneBodyTypeIsBoolean method
        pass

    def ClosureHasOneIterator(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ClosureHasOneIterator method
        pass

    def ClosureSourceElementTypeIsBodyElementType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ClosureSourceElementTypeIsBodyElementType method
        pass

    def AnyHasOneIterator(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AnyHasOneIterator method
        pass

    def SortedByElementTypeIsSourceElementType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SortedByElementTypeIsSourceElementType method
        pass

    def IsUniqueHasOneIterator(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement IsUniqueHasOneIterator method
        pass

    def SortedByHasOneIterator(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SortedByHasOneIterator method
        pass

    def ClosureBodyTypeIsConformanttoIteratorType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ClosureBodyTypeIsConformanttoIteratorType method
        pass

    def AnyTypeIsSourceElementType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AnyTypeIsSourceElementType method
        pass

    def CollectHasOneIterator(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CollectHasOneIterator method
        pass

class pivot_IterateExp(LoopExp, ReferringElement):

    def __init__(self, pivot_IterateExp: "pivot_Variable" = None):
        self.pivot_IterateExp = pivot_IterateExp
        
    @property
    def pivot_IterateExp(self):
        return self.__pivot_IterateExp

    @pivot_IterateExp.setter
    def pivot_IterateExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_IterateExp__pivot_IterateExp", None)
        self.__pivot_IterateExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Variable82"):
                opp_val = getattr(old_value, "pivot_Variable82", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Variable82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Variable82"):
                opp_val = getattr(value, "pivot_Variable82", None)
                setattr(value, "pivot_Variable82", self)

    def TypeIsResultType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement TypeIsResultType method
        pass

    def BodyTypeConformsToResultType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BodyTypeConformsToResultType method
        pass

    def OneInitializer(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OneInitializer method
        pass

class Operation:

    pass
class pivot_Iteration(Operation):

    pass
class NumericLiteralExp:

    pass
class pivot_UnlimitedNaturalLiteralExp(NumericLiteralExp):

    def __init__(self, unlimitedNaturalSymbol: str):
        self.unlimitedNaturalSymbol = unlimitedNaturalSymbol
        
    @property
    def unlimitedNaturalSymbol(self) -> str:
        return self.__unlimitedNaturalSymbol

    @unlimitedNaturalSymbol.setter
    def unlimitedNaturalSymbol(self, unlimitedNaturalSymbol: str):
        self.__unlimitedNaturalSymbol = unlimitedNaturalSymbol

class pivot_RealLiteralExp(NumericLiteralExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> str:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol

class pivot_IntegerLiteralExp(NumericLiteralExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

    def TypeIsInteger(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement TypeIsInteger method
        pass

class pivot_Variable(VariableDeclaration):

    def __init__(self, implicit: str, pivot_Variable64: "pivot_ExpressionInOCL" = None, pivot_Variable67: "pivot_ExpressionInOCL" = None, pivot_Variable: "pivot_ExpressionInOCL" = None, pivot_Variable82: "pivot_IterateExp" = None, pivot_Variable99: "pivot_LetExp" = None, pivot_Variable105: "pivot_LoopExp" = None, pivot_Variable342: "pivot_OCLExpression" = None, pivot_Variable345: "pivot_Parameter" = None):
        self.implicit = implicit
        self.pivot_Variable64 = pivot_Variable64
        self.pivot_Variable67 = pivot_Variable67
        self.pivot_Variable = pivot_Variable
        self.pivot_Variable82 = pivot_Variable82
        self.pivot_Variable99 = pivot_Variable99
        self.pivot_Variable105 = pivot_Variable105
        self.pivot_Variable342 = pivot_Variable342
        self.pivot_Variable345 = pivot_Variable345
        
    @property
    def implicit(self) -> str:
        return self.__implicit

    @implicit.setter
    def implicit(self, implicit: str):
        self.__implicit = implicit

    @property
    def pivot_Variable105(self):
        return self.__pivot_Variable105

    @pivot_Variable105.setter
    def pivot_Variable105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable105", None)
        self.__pivot_Variable105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_LoopExp104"):
                opp_val = getattr(old_value, "pivot_LoopExp104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_LoopExp104"):
                opp_val = getattr(value, "pivot_LoopExp104", None)
                if opp_val is None:
                    setattr(value, "pivot_LoopExp104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Variable82(self):
        return self.__pivot_Variable82

    @pivot_Variable82.setter
    def pivot_Variable82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable82", None)
        self.__pivot_Variable82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_IterateExp"):
                opp_val = getattr(old_value, "pivot_IterateExp", None)
                if opp_val == self:
                    setattr(old_value, "pivot_IterateExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_IterateExp"):
                opp_val = getattr(value, "pivot_IterateExp", None)
                setattr(value, "pivot_IterateExp", self)

    @property
    def pivot_Variable64(self):
        return self.__pivot_Variable64

    @pivot_Variable64.setter
    def pivot_Variable64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable64", None)
        self.__pivot_Variable64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_ExpressionInOCL63"):
                opp_val = getattr(old_value, "pivot_ExpressionInOCL63", None)
                if opp_val == self:
                    setattr(old_value, "pivot_ExpressionInOCL63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ExpressionInOCL63"):
                opp_val = getattr(value, "pivot_ExpressionInOCL63", None)
                setattr(value, "pivot_ExpressionInOCL63", self)

    @property
    def pivot_Variable99(self):
        return self.__pivot_Variable99

    @pivot_Variable99.setter
    def pivot_Variable99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable99", None)
        self.__pivot_Variable99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_LetExp98"):
                opp_val = getattr(old_value, "pivot_LetExp98", None)
                if opp_val == self:
                    setattr(old_value, "pivot_LetExp98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_LetExp98"):
                opp_val = getattr(value, "pivot_LetExp98", None)
                setattr(value, "pivot_LetExp98", self)

    @property
    def pivot_Variable(self):
        return self.__pivot_Variable

    @pivot_Variable.setter
    def pivot_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable", None)
        self.__pivot_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_ExpressionInOCL61"):
                opp_val = getattr(old_value, "pivot_ExpressionInOCL61", None)
                if opp_val == self:
                    setattr(old_value, "pivot_ExpressionInOCL61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ExpressionInOCL61"):
                opp_val = getattr(value, "pivot_ExpressionInOCL61", None)
                setattr(value, "pivot_ExpressionInOCL61", self)

    @property
    def pivot_Variable67(self):
        return self.__pivot_Variable67

    @pivot_Variable67.setter
    def pivot_Variable67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable67", None)
        self.__pivot_Variable67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_ExpressionInOCL66"):
                opp_val = getattr(old_value, "pivot_ExpressionInOCL66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ExpressionInOCL66"):
                opp_val = getattr(value, "pivot_ExpressionInOCL66", None)
                if opp_val is None:
                    setattr(value, "pivot_ExpressionInOCL66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Variable342(self):
        return self.__pivot_Variable342

    @pivot_Variable342.setter
    def pivot_Variable342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable342", None)
        self.__pivot_Variable342 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OCLExpression343"):
                opp_val = getattr(old_value, "pivot_OCLExpression343", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression343", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression343"):
                opp_val = getattr(value, "pivot_OCLExpression343", None)
                setattr(value, "pivot_OCLExpression343", self)

    @property
    def pivot_Variable345(self):
        return self.__pivot_Variable345

    @pivot_Variable345.setter
    def pivot_Variable345(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable345", None)
        self.__pivot_Variable345 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Parameter346"):
                opp_val = getattr(old_value, "pivot_Parameter346", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Parameter346", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Parameter346"):
                opp_val = getattr(value, "pivot_Parameter346", None)
                setattr(value, "pivot_Parameter346", self)

class OpaqueExpression:

    pass
class pivot_ExpressionInOCL(OpaqueExpression):

    pass
class State:

    pass
class pivot_FinalState(State):

    pass
class CallExp:

    pass
class pivot_LoopExp(CallExp):

    def __init__(self, pivot_LoopExp: "pivot_OCLExpression" = None, pivot_LoopExp104: set["pivot_Variable"] = None, pivot_LoopExp107: "pivot_Iteration" = None):
        self.pivot_LoopExp = pivot_LoopExp
        self.pivot_LoopExp104 = pivot_LoopExp104 if pivot_LoopExp104 is not None else set()
        self.pivot_LoopExp107 = pivot_LoopExp107
        
    @property
    def pivot_LoopExp107(self):
        return self.__pivot_LoopExp107

    @pivot_LoopExp107.setter
    def pivot_LoopExp107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_LoopExp__pivot_LoopExp107", None)
        self.__pivot_LoopExp107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Iteration108"):
                opp_val = getattr(old_value, "pivot_Iteration108", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Iteration108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Iteration108"):
                opp_val = getattr(value, "pivot_Iteration108", None)
                setattr(value, "pivot_Iteration108", self)

    @property
    def pivot_LoopExp(self):
        return self.__pivot_LoopExp

    @pivot_LoopExp.setter
    def pivot_LoopExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_LoopExp__pivot_LoopExp", None)
        self.__pivot_LoopExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OCLExpression102"):
                opp_val = getattr(old_value, "pivot_OCLExpression102", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression102"):
                opp_val = getattr(value, "pivot_OCLExpression102", None)
                setattr(value, "pivot_OCLExpression102", self)

    @property
    def pivot_LoopExp104(self):
        return self.__pivot_LoopExp104

    @pivot_LoopExp104.setter
    def pivot_LoopExp104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_LoopExp__pivot_LoopExp104", None)
        self.__pivot_LoopExp104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Variable105"):
                    opp_val = getattr(item, "pivot_Variable105", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Variable105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Variable105"):
                    opp_val = getattr(item, "pivot_Variable105", None)
                    
                    setattr(item, "pivot_Variable105", self)
                    

    def NoInitializers(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NoInitializers method
        pass

    def SourceIsCollection(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SourceIsCollection method
        pass

class pivot_FeatureCallExp(CallExp):

    def __init__(self, isPre: str):
        self.isPre = isPre
        
    @property
    def isPre(self) -> str:
        return self.__isPre

    @isPre.setter
    def isPre(self, isPre: str):
        self.__isPre = isPre

class TypedMultiplicityElement:

    pass
class pivot_Parameter(VariableDeclaration, TypedMultiplicityElement):

    pass
class pivot_Feature(TypedMultiplicityElement):

    def __init__(self, implementationClass: str, implementation: str):
        self.implementationClass = implementationClass
        self.implementation = implementation
        
    @property
    def implementationClass(self) -> str:
        return self.__implementationClass

    @implementationClass.setter
    def implementationClass(self, implementationClass: str):
        self.__implementationClass = implementationClass

    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

class DynamicElement:

    pass
class Visitable:

    pass
class pivot_OpaqueExpression(ValueSpecification):

    def __init__(self, body: str, language: str, message: str, pivot_OpaqueExpression: "pivot_Constraint" = None, pivot_OpaqueExpression148: "pivot_Operation" = None, pivot_OpaqueExpression185: "pivot_Property" = None):
        self.body = body
        self.language = language
        self.message = message
        self.pivot_OpaqueExpression = pivot_OpaqueExpression
        self.pivot_OpaqueExpression148 = pivot_OpaqueExpression148
        self.pivot_OpaqueExpression185 = pivot_OpaqueExpression185
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def pivot_OpaqueExpression185(self):
        return self.__pivot_OpaqueExpression185

    @pivot_OpaqueExpression185.setter
    def pivot_OpaqueExpression185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_OpaqueExpression__pivot_OpaqueExpression185", None)
        self.__pivot_OpaqueExpression185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property184"):
                opp_val = getattr(old_value, "pivot_Property184", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property184"):
                opp_val = getattr(value, "pivot_Property184", None)
                setattr(value, "pivot_Property184", self)

    @property
    def pivot_OpaqueExpression(self):
        return self.__pivot_OpaqueExpression

    @pivot_OpaqueExpression.setter
    def pivot_OpaqueExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_OpaqueExpression__pivot_OpaqueExpression", None)
        self.__pivot_OpaqueExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Constraint31"):
                opp_val = getattr(old_value, "pivot_Constraint31", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Constraint31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Constraint31"):
                opp_val = getattr(value, "pivot_Constraint31", None)
                setattr(value, "pivot_Constraint31", self)

    @property
    def pivot_OpaqueExpression148(self):
        return self.__pivot_OpaqueExpression148

    @pivot_OpaqueExpression148.setter
    def pivot_OpaqueExpression148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_OpaqueExpression__pivot_OpaqueExpression148", None)
        self.__pivot_OpaqueExpression148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation147"):
                opp_val = getattr(old_value, "pivot_Operation147", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Operation147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation147"):
                opp_val = getattr(value, "pivot_Operation147", None)
                setattr(value, "pivot_Operation147", self)

class DataType:

    pass
class pivot_LambdaType(DataType):

    pass
class pivot_Enumeration(DataType):

    pass
class pivot_TupleType(DataType):

    pass
class pivot_PrimitiveType(DataType):

    pass
class pivot_CollectionType(DataType):

    def __init__(self, lower: str, upper: str, pivot_CollectionType: "pivot_Type" = None):
        self.lower = lower
        self.upper = upper
        self.pivot_CollectionType = pivot_CollectionType
        
    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def pivot_CollectionType(self):
        return self.__pivot_CollectionType

    @pivot_CollectionType.setter
    def pivot_CollectionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_CollectionType__pivot_CollectionType", None)
        self.__pivot_CollectionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Type"):
                opp_val = getattr(old_value, "pivot_Type", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Type"):
                opp_val = getattr(value, "pivot_Type", None)
                setattr(value, "pivot_Type", self)

class Vertex:

    pass
class pivot_Pseudostate(Vertex):

    def __init__(self, kind: str, pivot_Pseudostate: "pivot_ConnectionPointReference" = None, pivot_Pseudostate27: "pivot_ConnectionPointReference" = None, pivot_Pseudostate203: "pivot_StateMachine" = None, pivot_Pseudostate205: "pivot_State" = None, pivot_Pseudostate250: "pivot_State" = None, pivot_Pseudostate260: "pivot_StateMachine" = None):
        self.kind = kind
        self.pivot_Pseudostate = pivot_Pseudostate
        self.pivot_Pseudostate27 = pivot_Pseudostate27
        self.pivot_Pseudostate203 = pivot_Pseudostate203
        self.pivot_Pseudostate205 = pivot_Pseudostate205
        self.pivot_Pseudostate250 = pivot_Pseudostate250
        self.pivot_Pseudostate260 = pivot_Pseudostate260
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def pivot_Pseudostate250(self):
        return self.__pivot_Pseudostate250

    @pivot_Pseudostate250.setter
    def pivot_Pseudostate250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Pseudostate__pivot_Pseudostate250", None)
        self.__pivot_Pseudostate250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_State249"):
                opp_val = getattr(old_value, "pivot_State249", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_State249"):
                opp_val = getattr(value, "pivot_State249", None)
                if opp_val is None:
                    setattr(value, "pivot_State249", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Pseudostate205(self):
        return self.__pivot_Pseudostate205

    @pivot_Pseudostate205.setter
    def pivot_Pseudostate205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Pseudostate__pivot_Pseudostate205", None)
        self.__pivot_Pseudostate205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_State206"):
                opp_val = getattr(old_value, "pivot_State206", None)
                if opp_val == self:
                    setattr(old_value, "pivot_State206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_State206"):
                opp_val = getattr(value, "pivot_State206", None)
                setattr(value, "pivot_State206", self)

    @property
    def pivot_Pseudostate260(self):
        return self.__pivot_Pseudostate260

    @pivot_Pseudostate260.setter
    def pivot_Pseudostate260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Pseudostate__pivot_Pseudostate260", None)
        self.__pivot_Pseudostate260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_StateMachine259"):
                opp_val = getattr(old_value, "pivot_StateMachine259", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_StateMachine259"):
                opp_val = getattr(value, "pivot_StateMachine259", None)
                if opp_val is None:
                    setattr(value, "pivot_StateMachine259", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Pseudostate203(self):
        return self.__pivot_Pseudostate203

    @pivot_Pseudostate203.setter
    def pivot_Pseudostate203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Pseudostate__pivot_Pseudostate203", None)
        self.__pivot_Pseudostate203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_StateMachine"):
                opp_val = getattr(old_value, "pivot_StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "pivot_StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_StateMachine"):
                opp_val = getattr(value, "pivot_StateMachine", None)
                setattr(value, "pivot_StateMachine", self)

    @property
    def pivot_Pseudostate27(self):
        return self.__pivot_Pseudostate27

    @pivot_Pseudostate27.setter
    def pivot_Pseudostate27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Pseudostate__pivot_Pseudostate27", None)
        self.__pivot_Pseudostate27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_ConnectionPointReference26"):
                opp_val = getattr(old_value, "pivot_ConnectionPointReference26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ConnectionPointReference26"):
                opp_val = getattr(value, "pivot_ConnectionPointReference26", None)
                if opp_val is None:
                    setattr(value, "pivot_ConnectionPointReference26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Pseudostate(self):
        return self.__pivot_Pseudostate

    @pivot_Pseudostate.setter
    def pivot_Pseudostate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Pseudostate__pivot_Pseudostate", None)
        self.__pivot_Pseudostate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_ConnectionPointReference"):
                opp_val = getattr(old_value, "pivot_ConnectionPointReference", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ConnectionPointReference"):
                opp_val = getattr(value, "pivot_ConnectionPointReference", None)
                if opp_val is None:
                    setattr(value, "pivot_ConnectionPointReference", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pivot_ConnectionPointReference(Vertex):

    pass
class Element:

    pass
class pivot_TemplateParameterSubstitution(Element):

    pass
class pivot_DynamicElement(Element):

    pass
class pivot_TemplateParameter(Element):

    pass
class pivot_NamedElement(Element, Nameable):

    def __init__(self, name: str, isStatic: str, pivot_NamedElement: set["pivot_Annotation"] = None):
        self.name = name
        self.isStatic = isStatic
        self.pivot_NamedElement = pivot_NamedElement if pivot_NamedElement is not None else set()
        
    @property
    def isStatic(self) -> str:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: str):
        self.__isStatic = isStatic

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pivot_NamedElement(self):
        return self.__pivot_NamedElement

    @pivot_NamedElement.setter
    def pivot_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_NamedElement__pivot_NamedElement", None)
        self.__pivot_NamedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Annotation126"):
                    opp_val = getattr(item, "pivot_Annotation126", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Annotation126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Annotation126"):
                    opp_val = getattr(item, "pivot_Annotation126", None)
                    
                    setattr(item, "pivot_Annotation126", self)
                    

class pivot_TemplateBinding(Element):

    pass
class pivot_TemplateableElement(Element):

    def __init__(self, TemplateableElement: "pivot_TemplateBinding" = None, TemplateableElement293: "pivot_TemplateSignature" = None, boundElement: set["pivot_TemplateBinding"] = None, template: "pivot_TemplateSignature" = None, pivot_TemplateableElement: "pivot_TemplateableElement" = None, pivot_TemplateableElement298: "pivot_TemplateableElement" = None):
        self.TemplateableElement = TemplateableElement
        self.TemplateableElement293 = TemplateableElement293
        self.boundElement = boundElement if boundElement is not None else set()
        self.template = template
        self.pivot_TemplateableElement = pivot_TemplateableElement
        self.pivot_TemplateableElement298 = pivot_TemplateableElement298
        
    @property
    def boundElement(self):
        return self.__boundElement

    @boundElement.setter
    def boundElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_TemplateableElement__boundElement", None)
        self.__boundElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TemplateBinding295"):
                    opp_val = getattr(item, "TemplateBinding295", None)
                    
                    if opp_val == self:
                        setattr(item, "TemplateBinding295", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TemplateBinding295"):
                    opp_val = getattr(item, "TemplateBinding295", None)
                    
                    setattr(item, "TemplateBinding295", self)
                    

    @property
    def template(self):
        return self.__template

    @template.setter
    def template(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_TemplateableElement__template", None)
        self.__template = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TemplateSignature297"):
                opp_val = getattr(old_value, "TemplateSignature297", None)
                if opp_val == self:
                    setattr(old_value, "TemplateSignature297", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TemplateSignature297"):
                opp_val = getattr(value, "TemplateSignature297", None)
                setattr(value, "TemplateSignature297", self)

    @property
    def TemplateableElement293(self):
        return self.__TemplateableElement293

    @TemplateableElement293.setter
    def TemplateableElement293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_TemplateableElement__TemplateableElement293", None)
        self.__TemplateableElement293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedTemplateSignature"):
                opp_val = getattr(old_value, "ownedTemplateSignature", None)
                if opp_val == self:
                    setattr(old_value, "ownedTemplateSignature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedTemplateSignature"):
                opp_val = getattr(value, "ownedTemplateSignature", None)
                setattr(value, "ownedTemplateSignature", self)

    @property
    def pivot_TemplateableElement298(self):
        return self.__pivot_TemplateableElement298

    @pivot_TemplateableElement298.setter
    def pivot_TemplateableElement298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_TemplateableElement__pivot_TemplateableElement298", None)
        self.__pivot_TemplateableElement298 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_TemplateableElement"):
                opp_val = getattr(old_value, "pivot_TemplateableElement", None)
                if opp_val == self:
                    setattr(old_value, "pivot_TemplateableElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_TemplateableElement"):
                opp_val = getattr(value, "pivot_TemplateableElement", None)
                setattr(value, "pivot_TemplateableElement", self)

    @property
    def TemplateableElement(self):
        return self.__TemplateableElement

    @TemplateableElement.setter
    def TemplateableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_TemplateableElement__TemplateableElement", None)
        self.__TemplateableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "templateBinding268"):
                opp_val = getattr(old_value, "templateBinding268", None)
                if opp_val == self:
                    setattr(old_value, "templateBinding268", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "templateBinding268"):
                opp_val = getattr(value, "templateBinding268", None)
                setattr(value, "templateBinding268", self)

    @property
    def pivot_TemplateableElement(self):
        return self.__pivot_TemplateableElement

    @pivot_TemplateableElement.setter
    def pivot_TemplateableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_TemplateableElement__pivot_TemplateableElement", None)
        self.__pivot_TemplateableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_TemplateableElement298"):
                opp_val = getattr(old_value, "pivot_TemplateableElement298", None)
                if opp_val == self:
                    setattr(old_value, "pivot_TemplateableElement298", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_TemplateableElement298"):
                opp_val = getattr(value, "pivot_TemplateableElement298", None)
                setattr(value, "pivot_TemplateableElement298", self)

    def isTemplate(self) -> str:
        # TODO: Implement isTemplate method
        pass

    def parameterableElements(self) -> ParameterableElement:
        # TODO: Implement parameterableElements method
        pass

class pivot_TemplateSignature(Element):

    pass
class pivot_ParameterableElement(Element):

    def __init__(self, ownedParameteredElement: "pivot_TemplateParameter" = None, parameteredElement: "pivot_TemplateParameter" = None, ParameterableElement: "pivot_TemplateParameter" = None, ParameterableElement273: "pivot_TemplateParameter" = None, pivot_ParameterableElement: "pivot_TemplateParameter" = None, pivot_ParameterableElement277: "pivot_TemplateParameter" = None, pivot_ParameterableElement282: "pivot_TemplateParameterSubstitution" = None, pivot_ParameterableElement285: "pivot_TemplateParameterSubstitution" = None):
        self.ownedParameteredElement = ownedParameteredElement
        self.parameteredElement = parameteredElement
        self.ParameterableElement = ParameterableElement
        self.ParameterableElement273 = ParameterableElement273
        self.pivot_ParameterableElement = pivot_ParameterableElement
        self.pivot_ParameterableElement277 = pivot_ParameterableElement277
        self.pivot_ParameterableElement282 = pivot_ParameterableElement282
        self.pivot_ParameterableElement285 = pivot_ParameterableElement285
        
    @property
    def pivot_ParameterableElement(self):
        return self.__pivot_ParameterableElement

    @pivot_ParameterableElement.setter
    def pivot_ParameterableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ParameterableElement__pivot_ParameterableElement", None)
        self.__pivot_ParameterableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_TemplateParameter"):
                opp_val = getattr(old_value, "pivot_TemplateParameter", None)
                if opp_val == self:
                    setattr(old_value, "pivot_TemplateParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_TemplateParameter"):
                opp_val = getattr(value, "pivot_TemplateParameter", None)
                setattr(value, "pivot_TemplateParameter", self)

    @property
    def pivot_ParameterableElement282(self):
        return self.__pivot_ParameterableElement282

    @pivot_ParameterableElement282.setter
    def pivot_ParameterableElement282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ParameterableElement__pivot_ParameterableElement282", None)
        self.__pivot_ParameterableElement282 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_TemplateParameterSubstitution281"):
                opp_val = getattr(old_value, "pivot_TemplateParameterSubstitution281", None)
                if opp_val == self:
                    setattr(old_value, "pivot_TemplateParameterSubstitution281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_TemplateParameterSubstitution281"):
                opp_val = getattr(value, "pivot_TemplateParameterSubstitution281", None)
                setattr(value, "pivot_TemplateParameterSubstitution281", self)

    @property
    def pivot_ParameterableElement285(self):
        return self.__pivot_ParameterableElement285

    @pivot_ParameterableElement285.setter
    def pivot_ParameterableElement285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ParameterableElement__pivot_ParameterableElement285", None)
        self.__pivot_ParameterableElement285 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_TemplateParameterSubstitution284"):
                opp_val = getattr(old_value, "pivot_TemplateParameterSubstitution284", None)
                if opp_val == self:
                    setattr(old_value, "pivot_TemplateParameterSubstitution284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_TemplateParameterSubstitution284"):
                opp_val = getattr(value, "pivot_TemplateParameterSubstitution284", None)
                setattr(value, "pivot_TemplateParameterSubstitution284", self)

    @property
    def ownedParameteredElement(self):
        return self.__ownedParameteredElement

    @ownedParameteredElement.setter
    def ownedParameteredElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ParameterableElement__ownedParameteredElement", None)
        self.__ownedParameteredElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TemplateParameter"):
                opp_val = getattr(old_value, "TemplateParameter", None)
                if opp_val == self:
                    setattr(old_value, "TemplateParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TemplateParameter"):
                opp_val = getattr(value, "TemplateParameter", None)
                setattr(value, "TemplateParameter", self)

    @property
    def ParameterableElement(self):
        return self.__ParameterableElement

    @ParameterableElement.setter
    def ParameterableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ParameterableElement__ParameterableElement", None)
        self.__ParameterableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "templateParameter"):
                opp_val = getattr(old_value, "templateParameter", None)
                if opp_val == self:
                    setattr(old_value, "templateParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "templateParameter"):
                opp_val = getattr(value, "templateParameter", None)
                setattr(value, "templateParameter", self)

    @property
    def pivot_ParameterableElement277(self):
        return self.__pivot_ParameterableElement277

    @pivot_ParameterableElement277.setter
    def pivot_ParameterableElement277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ParameterableElement__pivot_ParameterableElement277", None)
        self.__pivot_ParameterableElement277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_TemplateParameter276"):
                opp_val = getattr(old_value, "pivot_TemplateParameter276", None)
                if opp_val == self:
                    setattr(old_value, "pivot_TemplateParameter276", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_TemplateParameter276"):
                opp_val = getattr(value, "pivot_TemplateParameter276", None)
                setattr(value, "pivot_TemplateParameter276", self)

    @property
    def parameteredElement(self):
        return self.__parameteredElement

    @parameteredElement.setter
    def parameteredElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ParameterableElement__parameteredElement", None)
        self.__parameteredElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TemplateParameter175"):
                opp_val = getattr(old_value, "TemplateParameter175", None)
                if opp_val == self:
                    setattr(old_value, "TemplateParameter175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TemplateParameter175"):
                opp_val = getattr(value, "TemplateParameter175", None)
                setattr(value, "TemplateParameter175", self)

    @property
    def ParameterableElement273(self):
        return self.__ParameterableElement273

    @ParameterableElement273.setter
    def ParameterableElement273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ParameterableElement__ParameterableElement273", None)
        self.__ParameterableElement273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningTemplateParameter"):
                opp_val = getattr(old_value, "owningTemplateParameter", None)
                if opp_val == self:
                    setattr(old_value, "owningTemplateParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningTemplateParameter"):
                opp_val = getattr(value, "owningTemplateParameter", None)
                setattr(value, "owningTemplateParameter", self)

    def isCompatibleWith(self, p: ParameterableElement) -> str:
        # TODO: Implement isCompatibleWith method
        pass

    def isTemplateParameter(self) -> str:
        # TODO: Implement isTemplateParameter method
        pass

class pivot_DynamicProperty(Element):

    def __init__(self, default: str, pivot_DynamicProperty47: "pivot_DynamicType" = None, pivot_DynamicProperty: "pivot_Property" = None):
        self.default = default
        self.pivot_DynamicProperty47 = pivot_DynamicProperty47
        self.pivot_DynamicProperty = pivot_DynamicProperty
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def pivot_DynamicProperty(self):
        return self.__pivot_DynamicProperty

    @pivot_DynamicProperty.setter
    def pivot_DynamicProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_DynamicProperty__pivot_DynamicProperty", None)
        self.__pivot_DynamicProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property45"):
                opp_val = getattr(old_value, "pivot_Property45", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property45"):
                opp_val = getattr(value, "pivot_Property45", None)
                setattr(value, "pivot_Property45", self)

    @property
    def pivot_DynamicProperty47(self):
        return self.__pivot_DynamicProperty47

    @pivot_DynamicProperty47.setter
    def pivot_DynamicProperty47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_DynamicProperty__pivot_DynamicProperty47", None)
        self.__pivot_DynamicProperty47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_DynamicType"):
                opp_val = getattr(old_value, "pivot_DynamicType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_DynamicType"):
                opp_val = getattr(value, "pivot_DynamicType", None)
                if opp_val is None:
                    setattr(value, "pivot_DynamicType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pivot_Comment(Element):

    def __init__(self, body: str, pivot_Comment: set["pivot_Element"] = None, pivot_Comment50: "pivot_Element" = None):
        self.body = body
        self.pivot_Comment = pivot_Comment if pivot_Comment is not None else set()
        self.pivot_Comment50 = pivot_Comment50
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def pivot_Comment(self):
        return self.__pivot_Comment

    @pivot_Comment.setter
    def pivot_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Comment__pivot_Comment", None)
        self.__pivot_Comment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Element21"):
                    opp_val = getattr(item, "pivot_Element21", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Element21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Element21"):
                    opp_val = getattr(item, "pivot_Element21", None)
                    
                    setattr(item, "pivot_Element21", self)
                    

    @property
    def pivot_Comment50(self):
        return self.__pivot_Comment50

    @pivot_Comment50.setter
    def pivot_Comment50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Comment__pivot_Comment50", None)
        self.__pivot_Comment50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Element49"):
                opp_val = getattr(old_value, "pivot_Element49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Element49"):
                opp_val = getattr(value, "pivot_Element49", None)
                if opp_val is None:
                    setattr(value, "pivot_Element49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TypedElement:

    pass
class pivot_VariableDeclaration(TypedElement):

    pass
class pivot_ValueSpecification(TypedElement, ParameterableElement):

    def __init__(self):
        
    def stringValue(self) -> str:
        # TODO: Implement stringValue method
        pass

    def unlimitedValue(self) -> str:
        # TODO: Implement unlimitedValue method
        pass

    def integerValue(self) -> str:
        # TODO: Implement integerValue method
        pass

    def booleanValue(self) -> str:
        # TODO: Implement booleanValue method
        pass

    def isNull(self) -> str:
        # TODO: Implement isNull method
        pass

    def isComputable(self) -> str:
        # TODO: Implement isComputable method
        pass

class pivot_ConstructorPart(TypedElement):

    pass
class pivot_TypedMultiplicityElement(TypedElement):

    def __init__(self):
        
    def CompatibleBody(self, bodySpecification: ValueSpecification) -> str:
        # TODO: Implement CompatibleBody method
        pass

    def makeParameter(self) -> str:
        # TODO: Implement makeParameter method
        pass

class pivot_CollectionLiteralPart(TypedElement):

    pass
class LiteralExp:

    pass
class pivot_EnumLiteralExp(LiteralExp):

    def __init__(self, pivot_EnumLiteralExp: "pivot_EnumerationLiteral" = None):
        self.pivot_EnumLiteralExp = pivot_EnumLiteralExp
        
    @property
    def pivot_EnumLiteralExp(self):
        return self.__pivot_EnumLiteralExp

    @pivot_EnumLiteralExp.setter
    def pivot_EnumLiteralExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_EnumLiteralExp__pivot_EnumLiteralExp", None)
        self.__pivot_EnumLiteralExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_EnumerationLiteral"):
                opp_val = getattr(old_value, "pivot_EnumerationLiteral", None)
                if opp_val == self:
                    setattr(old_value, "pivot_EnumerationLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_EnumerationLiteral"):
                opp_val = getattr(value, "pivot_EnumerationLiteral", None)
                setattr(value, "pivot_EnumerationLiteral", self)

    def TypeIsEnumerationType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement TypeIsEnumerationType method
        pass

class pivot_InvalidLiteralExp(LiteralExp):

    pass
class pivot_TupleLiteralExp(LiteralExp):

    pass
class pivot_PrimitiveLiteralExp(LiteralExp):

    pass
class pivot_CollectionLiteralExp(LiteralExp):

    def __init__(self, kind: str, pivot_CollectionLiteralExp: set["pivot_CollectionLiteralPart"] = None):
        self.kind = kind
        self.pivot_CollectionLiteralExp = pivot_CollectionLiteralExp if pivot_CollectionLiteralExp is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def pivot_CollectionLiteralExp(self):
        return self.__pivot_CollectionLiteralExp

    @pivot_CollectionLiteralExp.setter
    def pivot_CollectionLiteralExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_CollectionLiteralExp__pivot_CollectionLiteralExp", None)
        self.__pivot_CollectionLiteralExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_CollectionLiteralPart"):
                    opp_val = getattr(item, "pivot_CollectionLiteralPart", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_CollectionLiteralPart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_CollectionLiteralPart"):
                    opp_val = getattr(item, "pivot_CollectionLiteralPart", None)
                    
                    setattr(item, "pivot_CollectionLiteralPart", self)
                    

    def BagKindIsBag(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BagKindIsBag method
        pass

    def OrderedSetKindIsOrderedSet(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement OrderedSetKindIsOrderedSet method
        pass

    def SequenceKindIsSequence(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement SequenceKindIsSequence method
        pass

    def CollectionKindIsConcrete(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CollectionKindIsConcrete method
        pass

    def SetKindIsSet(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SetKindIsSet method
        pass

class CollectionLiteralPart:

    pass
class pivot_CollectionRange(CollectionLiteralPart):

    pass
class pivot_CollectionItem(CollectionLiteralPart):

    def __init__(self, pivot_CollectionItem: "pivot_OCLExpression" = None):
        self.pivot_CollectionItem = pivot_CollectionItem
        
    @property
    def pivot_CollectionItem(self):
        return self.__pivot_CollectionItem

    @pivot_CollectionItem.setter
    def pivot_CollectionItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_CollectionItem__pivot_CollectionItem", None)
        self.__pivot_CollectionItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OCLExpression12"):
                opp_val = getattr(old_value, "pivot_OCLExpression12", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression12"):
                opp_val = getattr(value, "pivot_OCLExpression12", None)
                setattr(value, "pivot_OCLExpression12", self)

    def TypeIsItemType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement TypeIsItemType method
        pass

class pivot_OCLExpression(TypedElement):

    pass
class OCLExpression:

    pass
class pivot_UnspecifiedValueExp(OCLExpression):

    pass
class pivot_VariableExp(OCLExpression, ReferringElement):

    def __init__(self, implicit: str, pivot_VariableExp: "pivot_VariableDeclaration" = None):
        self.implicit = implicit
        self.pivot_VariableExp = pivot_VariableExp
        
    @property
    def implicit(self) -> str:
        return self.__implicit

    @implicit.setter
    def implicit(self, implicit: str):
        self.__implicit = implicit

    @property
    def pivot_VariableExp(self):
        return self.__pivot_VariableExp

    @pivot_VariableExp.setter
    def pivot_VariableExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_VariableExp__pivot_VariableExp", None)
        self.__pivot_VariableExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_VariableDeclaration"):
                opp_val = getattr(old_value, "pivot_VariableDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "pivot_VariableDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_VariableDeclaration"):
                opp_val = getattr(value, "pivot_VariableDeclaration", None)
                setattr(value, "pivot_VariableDeclaration", self)

class pivot_ConstructorExp(OCLExpression):

    def __init__(self, value: str, pivot_ConstructorExp: set["pivot_ConstructorPart"] = None):
        self.value = value
        self.pivot_ConstructorExp = pivot_ConstructorExp if pivot_ConstructorExp is not None else set()
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def pivot_ConstructorExp(self):
        return self.__pivot_ConstructorExp

    @pivot_ConstructorExp.setter
    def pivot_ConstructorExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ConstructorExp__pivot_ConstructorExp", None)
        self.__pivot_ConstructorExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_ConstructorPart"):
                    opp_val = getattr(item, "pivot_ConstructorPart", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_ConstructorPart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_ConstructorPart"):
                    opp_val = getattr(item, "pivot_ConstructorPart", None)
                    
                    setattr(item, "pivot_ConstructorPart", self)
                    

class pivot_StateExp(OCLExpression):

    pass
class pivot_IfExp(OCLExpression):

    def __init__(self, pivot_IfExp: "pivot_OCLExpression" = None, pivot_IfExp74: "pivot_OCLExpression" = None, pivot_IfExp77: "pivot_OCLExpression" = None):
        self.pivot_IfExp = pivot_IfExp
        self.pivot_IfExp74 = pivot_IfExp74
        self.pivot_IfExp77 = pivot_IfExp77
        
    @property
    def pivot_IfExp(self):
        return self.__pivot_IfExp

    @pivot_IfExp.setter
    def pivot_IfExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_IfExp__pivot_IfExp", None)
        self.__pivot_IfExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OCLExpression72"):
                opp_val = getattr(old_value, "pivot_OCLExpression72", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression72"):
                opp_val = getattr(value, "pivot_OCLExpression72", None)
                setattr(value, "pivot_OCLExpression72", self)

    @property
    def pivot_IfExp74(self):
        return self.__pivot_IfExp74

    @pivot_IfExp74.setter
    def pivot_IfExp74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_IfExp__pivot_IfExp74", None)
        self.__pivot_IfExp74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OCLExpression75"):
                opp_val = getattr(old_value, "pivot_OCLExpression75", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression75"):
                opp_val = getattr(value, "pivot_OCLExpression75", None)
                setattr(value, "pivot_OCLExpression75", self)

    @property
    def pivot_IfExp77(self):
        return self.__pivot_IfExp77

    @pivot_IfExp77.setter
    def pivot_IfExp77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_IfExp__pivot_IfExp77", None)
        self.__pivot_IfExp77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OCLExpression78"):
                opp_val = getattr(old_value, "pivot_OCLExpression78", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression78"):
                opp_val = getattr(value, "pivot_OCLExpression78", None)
                setattr(value, "pivot_OCLExpression78", self)

    def ConditionTypeIsBoolean(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ConditionTypeIsBoolean method
        pass

class pivot_LetExp(OCLExpression):

    def __init__(self, pivot_LetExp: "pivot_OCLExpression" = None, pivot_LetExp98: "pivot_Variable" = None):
        self.pivot_LetExp = pivot_LetExp
        self.pivot_LetExp98 = pivot_LetExp98
        
    @property
    def pivot_LetExp98(self):
        return self.__pivot_LetExp98

    @pivot_LetExp98.setter
    def pivot_LetExp98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_LetExp__pivot_LetExp98", None)
        self.__pivot_LetExp98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Variable99"):
                opp_val = getattr(old_value, "pivot_Variable99", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Variable99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Variable99"):
                opp_val = getattr(value, "pivot_Variable99", None)
                setattr(value, "pivot_Variable99", self)

    @property
    def pivot_LetExp(self):
        return self.__pivot_LetExp

    @pivot_LetExp.setter
    def pivot_LetExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_LetExp__pivot_LetExp", None)
        self.__pivot_LetExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OCLExpression96"):
                opp_val = getattr(old_value, "pivot_OCLExpression96", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression96"):
                opp_val = getattr(value, "pivot_OCLExpression96", None)
                setattr(value, "pivot_OCLExpression96", self)

    def TypeIsInType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement TypeIsInType method
        pass

class pivot_TypeExp(OCLExpression, ReferringElement):

    pass
class pivot_MessageExp(OCLExpression):

    def __init__(self, pivot_MessageExp: "pivot_OCLExpression" = None, pivot_MessageExp112: set["pivot_OCLExpression"] = None, pivot_MessageExp115: "pivot_CallOperationAction" = None, pivot_MessageExp118: "pivot_SendSignalAction" = None):
        self.pivot_MessageExp = pivot_MessageExp
        self.pivot_MessageExp112 = pivot_MessageExp112 if pivot_MessageExp112 is not None else set()
        self.pivot_MessageExp115 = pivot_MessageExp115
        self.pivot_MessageExp118 = pivot_MessageExp118
        
    @property
    def pivot_MessageExp112(self):
        return self.__pivot_MessageExp112

    @pivot_MessageExp112.setter
    def pivot_MessageExp112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_MessageExp__pivot_MessageExp112", None)
        self.__pivot_MessageExp112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_OCLExpression113"):
                    opp_val = getattr(item, "pivot_OCLExpression113", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_OCLExpression113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_OCLExpression113"):
                    opp_val = getattr(item, "pivot_OCLExpression113", None)
                    
                    setattr(item, "pivot_OCLExpression113", self)
                    

    @property
    def pivot_MessageExp118(self):
        return self.__pivot_MessageExp118

    @pivot_MessageExp118.setter
    def pivot_MessageExp118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_MessageExp__pivot_MessageExp118", None)
        self.__pivot_MessageExp118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_SendSignalAction"):
                opp_val = getattr(old_value, "pivot_SendSignalAction", None)
                if opp_val == self:
                    setattr(old_value, "pivot_SendSignalAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_SendSignalAction"):
                opp_val = getattr(value, "pivot_SendSignalAction", None)
                setattr(value, "pivot_SendSignalAction", self)

    @property
    def pivot_MessageExp115(self):
        return self.__pivot_MessageExp115

    @pivot_MessageExp115.setter
    def pivot_MessageExp115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_MessageExp__pivot_MessageExp115", None)
        self.__pivot_MessageExp115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_CallOperationAction116"):
                opp_val = getattr(old_value, "pivot_CallOperationAction116", None)
                if opp_val == self:
                    setattr(old_value, "pivot_CallOperationAction116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_CallOperationAction116"):
                opp_val = getattr(value, "pivot_CallOperationAction116", None)
                setattr(value, "pivot_CallOperationAction116", self)

    @property
    def pivot_MessageExp(self):
        return self.__pivot_MessageExp

    @pivot_MessageExp.setter
    def pivot_MessageExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_MessageExp__pivot_MessageExp", None)
        self.__pivot_MessageExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OCLExpression110"):
                opp_val = getattr(old_value, "pivot_OCLExpression110", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression110"):
                opp_val = getattr(value, "pivot_OCLExpression110", None)
                setattr(value, "pivot_OCLExpression110", self)

    def OneCallOrOneSend(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OneCallOrOneSend method
        pass

    def TargetIsNotACollection(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement TargetIsNotACollection method
        pass

class pivot_LiteralExp(OCLExpression):

    pass
class pivot_CallExp(OCLExpression):

    def __init__(self, implicit: str, pivot_CallExp: "pivot_OCLExpression" = None):
        self.implicit = implicit
        self.pivot_CallExp = pivot_CallExp
        
    @property
    def implicit(self) -> str:
        return self.__implicit

    @implicit.setter
    def implicit(self, implicit: str):
        self.__implicit = implicit

    @property
    def pivot_CallExp(self):
        return self.__pivot_CallExp

    @pivot_CallExp.setter
    def pivot_CallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_CallExp__pivot_CallExp", None)
        self.__pivot_CallExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OCLExpression"):
                opp_val = getattr(old_value, "pivot_OCLExpression", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression"):
                opp_val = getattr(value, "pivot_OCLExpression", None)
                setattr(value, "pivot_OCLExpression", self)

class Namespace:

    pass
class pivot_Root(Namespace):

    def __init__(self, externalURI: str, pivot_Root: set["pivot_Package"] = None, pivot_Root221: set["pivot_Import"] = None):
        self.externalURI = externalURI
        self.pivot_Root = pivot_Root if pivot_Root is not None else set()
        self.pivot_Root221 = pivot_Root221 if pivot_Root221 is not None else set()
        
    @property
    def externalURI(self) -> str:
        return self.__externalURI

    @externalURI.setter
    def externalURI(self, externalURI: str):
        self.__externalURI = externalURI

    @property
    def pivot_Root221(self):
        return self.__pivot_Root221

    @pivot_Root221.setter
    def pivot_Root221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Root__pivot_Root221", None)
        self.__pivot_Root221 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Import222"):
                    opp_val = getattr(item, "pivot_Import222", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Import222", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Import222"):
                    opp_val = getattr(item, "pivot_Import222", None)
                    
                    setattr(item, "pivot_Import222", self)
                    

    @property
    def pivot_Root(self):
        return self.__pivot_Root

    @pivot_Root.setter
    def pivot_Root(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Root__pivot_Root", None)
        self.__pivot_Root = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Package219"):
                    opp_val = getattr(item, "pivot_Package219", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Package219", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Package219"):
                    opp_val = getattr(item, "pivot_Package219", None)
                    
                    setattr(item, "pivot_Package219", self)
                    

class pivot_State(Vertex, Namespace):

    def __init__(self, isComposite: str, isOrthogonal: str, isSimple: str, isSubmachineState: str, pivot_State: "pivot_ConnectionPointReference" = None, pivot_State206: "pivot_Pseudostate" = None, pivot_State212: "pivot_Region" = None, submachineState: "pivot_StateMachine" = None, pivot_State228: set["pivot_ConnectionPointReference"] = None, pivot_State237: "pivot_Constraint" = None, pivot_State240: "pivot_Behavior" = None, pivot_State243: "pivot_Behavior" = None, pivot_State246: "pivot_Behavior" = None, pivot_State249: set["pivot_Pseudostate"] = None, pivot_State232: "pivot_State" = None, pivot_State230: "pivot_State" = None, pivot_State252: set["pivot_Trigger"] = None, pivot_State234: set["pivot_Region"] = None, pivot_State254: "pivot_StateExp" = None, State: "pivot_StateMachine" = None):
        self.isComposite = isComposite
        self.isOrthogonal = isOrthogonal
        self.isSimple = isSimple
        self.isSubmachineState = isSubmachineState
        self.pivot_State = pivot_State
        self.pivot_State206 = pivot_State206
        self.pivot_State212 = pivot_State212
        self.submachineState = submachineState
        self.pivot_State228 = pivot_State228 if pivot_State228 is not None else set()
        self.pivot_State237 = pivot_State237
        self.pivot_State240 = pivot_State240
        self.pivot_State243 = pivot_State243
        self.pivot_State246 = pivot_State246
        self.pivot_State249 = pivot_State249 if pivot_State249 is not None else set()
        self.pivot_State232 = pivot_State232
        self.pivot_State230 = pivot_State230
        self.pivot_State252 = pivot_State252 if pivot_State252 is not None else set()
        self.pivot_State234 = pivot_State234 if pivot_State234 is not None else set()
        self.pivot_State254 = pivot_State254
        self.State = State
        
    @property
    def isSimple(self) -> str:
        return self.__isSimple

    @isSimple.setter
    def isSimple(self, isSimple: str):
        self.__isSimple = isSimple

    @property
    def isComposite(self) -> str:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite

    @property
    def isSubmachineState(self) -> str:
        return self.__isSubmachineState

    @isSubmachineState.setter
    def isSubmachineState(self, isSubmachineState: str):
        self.__isSubmachineState = isSubmachineState

    @property
    def isOrthogonal(self) -> str:
        return self.__isOrthogonal

    @isOrthogonal.setter
    def isOrthogonal(self, isOrthogonal: str):
        self.__isOrthogonal = isOrthogonal

    @property
    def pivot_State240(self):
        return self.__pivot_State240

    @pivot_State240.setter
    def pivot_State240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State240", None)
        self.__pivot_State240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Behavior241"):
                opp_val = getattr(old_value, "pivot_Behavior241", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Behavior241", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Behavior241"):
                opp_val = getattr(value, "pivot_Behavior241", None)
                setattr(value, "pivot_Behavior241", self)

    @property
    def pivot_State252(self):
        return self.__pivot_State252

    @pivot_State252.setter
    def pivot_State252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State252", None)
        self.__pivot_State252 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Trigger"):
                    opp_val = getattr(item, "pivot_Trigger", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Trigger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Trigger"):
                    opp_val = getattr(item, "pivot_Trigger", None)
                    
                    setattr(item, "pivot_Trigger", self)
                    

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "submachine"):
                opp_val = getattr(old_value, "submachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "submachine"):
                opp_val = getattr(value, "submachine", None)
                if opp_val is None:
                    setattr(value, "submachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_State228(self):
        return self.__pivot_State228

    @pivot_State228.setter
    def pivot_State228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State228", None)
        self.__pivot_State228 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_ConnectionPointReference229"):
                    opp_val = getattr(item, "pivot_ConnectionPointReference229", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_ConnectionPointReference229", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_ConnectionPointReference229"):
                    opp_val = getattr(item, "pivot_ConnectionPointReference229", None)
                    
                    setattr(item, "pivot_ConnectionPointReference229", self)
                    

    @property
    def submachineState(self):
        return self.__submachineState

    @submachineState.setter
    def submachineState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__submachineState", None)
        self.__submachineState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine"):
                opp_val = getattr(old_value, "StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine"):
                opp_val = getattr(value, "StateMachine", None)
                setattr(value, "StateMachine", self)

    @property
    def pivot_State234(self):
        return self.__pivot_State234

    @pivot_State234.setter
    def pivot_State234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State234", None)
        self.__pivot_State234 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Region235"):
                    opp_val = getattr(item, "pivot_Region235", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Region235", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Region235"):
                    opp_val = getattr(item, "pivot_Region235", None)
                    
                    setattr(item, "pivot_Region235", self)
                    

    @property
    def pivot_State(self):
        return self.__pivot_State

    @pivot_State.setter
    def pivot_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State", None)
        self.__pivot_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_ConnectionPointReference24"):
                opp_val = getattr(old_value, "pivot_ConnectionPointReference24", None)
                if opp_val == self:
                    setattr(old_value, "pivot_ConnectionPointReference24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ConnectionPointReference24"):
                opp_val = getattr(value, "pivot_ConnectionPointReference24", None)
                setattr(value, "pivot_ConnectionPointReference24", self)

    @property
    def pivot_State254(self):
        return self.__pivot_State254

    @pivot_State254.setter
    def pivot_State254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State254", None)
        self.__pivot_State254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_StateExp"):
                opp_val = getattr(old_value, "pivot_StateExp", None)
                if opp_val == self:
                    setattr(old_value, "pivot_StateExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_StateExp"):
                opp_val = getattr(value, "pivot_StateExp", None)
                setattr(value, "pivot_StateExp", self)

    @property
    def pivot_State212(self):
        return self.__pivot_State212

    @pivot_State212.setter
    def pivot_State212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State212", None)
        self.__pivot_State212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Region211"):
                opp_val = getattr(old_value, "pivot_Region211", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Region211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Region211"):
                opp_val = getattr(value, "pivot_Region211", None)
                setattr(value, "pivot_Region211", self)

    @property
    def pivot_State243(self):
        return self.__pivot_State243

    @pivot_State243.setter
    def pivot_State243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State243", None)
        self.__pivot_State243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Behavior244"):
                opp_val = getattr(old_value, "pivot_Behavior244", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Behavior244", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Behavior244"):
                opp_val = getattr(value, "pivot_Behavior244", None)
                setattr(value, "pivot_Behavior244", self)

    @property
    def pivot_State230(self):
        return self.__pivot_State230

    @pivot_State230.setter
    def pivot_State230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State230", None)
        self.__pivot_State230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_State232"):
                opp_val = getattr(old_value, "pivot_State232", None)
                if opp_val == self:
                    setattr(old_value, "pivot_State232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_State232"):
                opp_val = getattr(value, "pivot_State232", None)
                setattr(value, "pivot_State232", self)

    @property
    def pivot_State249(self):
        return self.__pivot_State249

    @pivot_State249.setter
    def pivot_State249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State249", None)
        self.__pivot_State249 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Pseudostate250"):
                    opp_val = getattr(item, "pivot_Pseudostate250", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Pseudostate250", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Pseudostate250"):
                    opp_val = getattr(item, "pivot_Pseudostate250", None)
                    
                    setattr(item, "pivot_Pseudostate250", self)
                    

    @property
    def pivot_State237(self):
        return self.__pivot_State237

    @pivot_State237.setter
    def pivot_State237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State237", None)
        self.__pivot_State237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Constraint238"):
                opp_val = getattr(old_value, "pivot_Constraint238", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Constraint238", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Constraint238"):
                opp_val = getattr(value, "pivot_Constraint238", None)
                setattr(value, "pivot_Constraint238", self)

    @property
    def pivot_State206(self):
        return self.__pivot_State206

    @pivot_State206.setter
    def pivot_State206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State206", None)
        self.__pivot_State206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Pseudostate205"):
                opp_val = getattr(old_value, "pivot_Pseudostate205", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Pseudostate205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Pseudostate205"):
                opp_val = getattr(value, "pivot_Pseudostate205", None)
                setattr(value, "pivot_Pseudostate205", self)

    @property
    def pivot_State246(self):
        return self.__pivot_State246

    @pivot_State246.setter
    def pivot_State246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State246", None)
        self.__pivot_State246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Behavior247"):
                opp_val = getattr(old_value, "pivot_Behavior247", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Behavior247", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Behavior247"):
                opp_val = getattr(value, "pivot_Behavior247", None)
                setattr(value, "pivot_Behavior247", self)

    @property
    def pivot_State232(self):
        return self.__pivot_State232

    @pivot_State232.setter
    def pivot_State232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State232", None)
        self.__pivot_State232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_State230"):
                opp_val = getattr(old_value, "pivot_State230", None)
                if opp_val == self:
                    setattr(old_value, "pivot_State230", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_State230"):
                opp_val = getattr(value, "pivot_State230", None)
                setattr(value, "pivot_State230", self)

class pivot_Package(Namespace, TemplateableElement):

    def __init__(self, nsPrefix: str, nsURI: str, pivot_Package168: set["pivot_Package"] = None, Package: "pivot_Package" = None, nestingPackage: set["pivot_Package"] = None, Package167: "pivot_Package" = None, nestedPackage: "pivot_Package" = None, pivot_Package: "pivot_Package" = None, package: set["pivot_Type"] = None, pivot_Package219: "pivot_Root" = None, Package318: "pivot_Type" = None):
        self.nsPrefix = nsPrefix
        self.nsURI = nsURI
        self.pivot_Package168 = pivot_Package168 if pivot_Package168 is not None else set()
        self.Package = Package
        self.nestingPackage = nestingPackage if nestingPackage is not None else set()
        self.Package167 = Package167
        self.nestedPackage = nestedPackage
        self.pivot_Package = pivot_Package
        self.package = package if package is not None else set()
        self.pivot_Package219 = pivot_Package219
        self.Package318 = Package318
        
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
    def nestedPackage(self):
        return self.__nestedPackage

    @nestedPackage.setter
    def nestedPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__nestedPackage", None)
        self.__nestedPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package167"):
                opp_val = getattr(old_value, "Package167", None)
                if opp_val == self:
                    setattr(old_value, "Package167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package167"):
                opp_val = getattr(value, "Package167", None)
                setattr(value, "Package167", self)

    @property
    def pivot_Package219(self):
        return self.__pivot_Package219

    @pivot_Package219.setter
    def pivot_Package219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__pivot_Package219", None)
        self.__pivot_Package219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Root"):
                opp_val = getattr(old_value, "pivot_Root", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Root"):
                opp_val = getattr(value, "pivot_Root", None)
                if opp_val is None:
                    setattr(value, "pivot_Root", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Package(self):
        return self.__Package

    @Package.setter
    def Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__Package", None)
        self.__Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nestingPackage"):
                opp_val = getattr(old_value, "nestingPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nestingPackage"):
                opp_val = getattr(value, "nestingPackage", None)
                if opp_val is None:
                    setattr(value, "nestingPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Package168(self):
        return self.__pivot_Package168

    @pivot_Package168.setter
    def pivot_Package168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__pivot_Package168", None)
        self.__pivot_Package168 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Package"):
                    opp_val = getattr(item, "pivot_Package", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Package", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Package"):
                    opp_val = getattr(item, "pivot_Package", None)
                    
                    setattr(item, "pivot_Package", self)
                    

    @property
    def package(self):
        return self.__package

    @package.setter
    def package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__package", None)
        self.__package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type171"):
                    opp_val = getattr(item, "Type171", None)
                    
                    if opp_val == self:
                        setattr(item, "Type171", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type171"):
                    opp_val = getattr(item, "Type171", None)
                    
                    setattr(item, "Type171", self)
                    

    @property
    def pivot_Package(self):
        return self.__pivot_Package

    @pivot_Package.setter
    def pivot_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__pivot_Package", None)
        self.__pivot_Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Package168"):
                opp_val = getattr(old_value, "pivot_Package168", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Package168"):
                opp_val = getattr(value, "pivot_Package168", None)
                if opp_val is None:
                    setattr(value, "pivot_Package168", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nestingPackage(self):
        return self.__nestingPackage

    @nestingPackage.setter
    def nestingPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__nestingPackage", None)
        self.__nestingPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    if opp_val == self:
                        setattr(item, "Package", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    setattr(item, "Package", self)
                    

    @property
    def Package167(self):
        return self.__Package167

    @Package167.setter
    def Package167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__Package167", None)
        self.__Package167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nestedPackage"):
                opp_val = getattr(old_value, "nestedPackage", None)
                if opp_val == self:
                    setattr(old_value, "nestedPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nestedPackage"):
                opp_val = getattr(value, "nestedPackage", None)
                setattr(value, "nestedPackage", self)

    @property
    def Package318(self):
        return self.__Package318

    @Package318.setter
    def Package318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__Package318", None)
        self.__Package318 = value
        
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

class pivot_Transition(Namespace):

    def __init__(self, kind: str, Transition: "pivot_Region" = None, outgoing: "pivot_Vertex" = None, incoming: "pivot_Vertex" = None, pivot_Transition: "pivot_Constraint" = None, pivot_Transition307: "pivot_Behavior" = None, pivot_Transition310: set["pivot_Trigger"] = None, transition: "pivot_Region" = None, Transition351: "pivot_Vertex" = None, Transition353: "pivot_Vertex" = None):
        self.kind = kind
        self.Transition = Transition
        self.outgoing = outgoing
        self.incoming = incoming
        self.pivot_Transition = pivot_Transition
        self.pivot_Transition307 = pivot_Transition307
        self.pivot_Transition310 = pivot_Transition310 if pivot_Transition310 is not None else set()
        self.transition = transition
        self.Transition351 = Transition351
        self.Transition353 = Transition353
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def pivot_Transition(self):
        return self.__pivot_Transition

    @pivot_Transition.setter
    def pivot_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__pivot_Transition", None)
        self.__pivot_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Constraint305"):
                opp_val = getattr(old_value, "pivot_Constraint305", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Constraint305", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Constraint305"):
                opp_val = getattr(value, "pivot_Constraint305", None)
                setattr(value, "pivot_Constraint305", self)

    @property
    def Transition353(self):
        return self.__Transition353

    @Transition353.setter
    def Transition353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__Transition353", None)
        self.__Transition353 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transition(self):
        return self.__transition

    @transition.setter
    def transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__transition", None)
        self.__transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Region"):
                opp_val = getattr(old_value, "Region", None)
                if opp_val == self:
                    setattr(old_value, "Region", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Region"):
                opp_val = getattr(value, "Region", None)
                setattr(value, "Region", self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex301"):
                opp_val = getattr(old_value, "Vertex301", None)
                if opp_val == self:
                    setattr(old_value, "Vertex301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex301"):
                opp_val = getattr(value, "Vertex301", None)
                setattr(value, "Vertex301", self)

    @property
    def pivot_Transition310(self):
        return self.__pivot_Transition310

    @pivot_Transition310.setter
    def pivot_Transition310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__pivot_Transition310", None)
        self.__pivot_Transition310 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Trigger311"):
                    opp_val = getattr(item, "pivot_Trigger311", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Trigger311", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Trigger311"):
                    opp_val = getattr(item, "pivot_Trigger311", None)
                    
                    setattr(item, "pivot_Trigger311", self)
                    

    @property
    def pivot_Transition307(self):
        return self.__pivot_Transition307

    @pivot_Transition307.setter
    def pivot_Transition307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__pivot_Transition307", None)
        self.__pivot_Transition307 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Behavior308"):
                opp_val = getattr(old_value, "pivot_Behavior308", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Behavior308", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Behavior308"):
                opp_val = getattr(value, "pivot_Behavior308", None)
                setattr(value, "pivot_Behavior308", self)

    @property
    def Transition351(self):
        return self.__Transition351

    @Transition351.setter
    def Transition351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__Transition351", None)
        self.__Transition351 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex303"):
                opp_val = getattr(old_value, "Vertex303", None)
                if opp_val == self:
                    setattr(old_value, "Vertex303", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex303"):
                opp_val = getattr(value, "Vertex303", None)
                setattr(value, "Vertex303", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container"):
                opp_val = getattr(old_value, "container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container"):
                opp_val = getattr(value, "container", None)
                if opp_val is None:
                    setattr(value, "container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pivot_Region(Namespace):

    pass
class Type:

    pass
class pivot_TemplateParameterType(Type):

    def __init__(self, specification: str):
        self.specification = specification
        
    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

class pivot_MessageType(Type):

    pass
class pivot_DynamicType(Type, DynamicElement):

    pass
class pivot_ElementExtension(Type):

    pass
class pivot_Class(Type, Namespace):

    def __init__(self, isAbstract: str, isInterface: str, pivot_Class: set["pivot_Behavior"] = None, pivot_Class157: "pivot_Operation" = None, pivot_Class178: "pivot_Property" = None):
        self.isAbstract = isAbstract
        self.isInterface = isInterface
        self.pivot_Class = pivot_Class if pivot_Class is not None else set()
        self.pivot_Class157 = pivot_Class157
        self.pivot_Class178 = pivot_Class178
        
    @property
    def isInterface(self) -> str:
        return self.__isInterface

    @isInterface.setter
    def isInterface(self, isInterface: str):
        self.__isInterface = isInterface

    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def pivot_Class157(self):
        return self.__pivot_Class157

    @pivot_Class157.setter
    def pivot_Class157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__pivot_Class157", None)
        self.__pivot_Class157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation156"):
                opp_val = getattr(old_value, "pivot_Operation156", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Operation156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation156"):
                opp_val = getattr(value, "pivot_Operation156", None)
                setattr(value, "pivot_Operation156", self)

    @property
    def pivot_Class178(self):
        return self.__pivot_Class178

    @pivot_Class178.setter
    def pivot_Class178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__pivot_Class178", None)
        self.__pivot_Class178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property177"):
                opp_val = getattr(old_value, "pivot_Property177", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property177"):
                opp_val = getattr(value, "pivot_Property177", None)
                setattr(value, "pivot_Property177", self)

    @property
    def pivot_Class(self):
        return self.__pivot_Class

    @pivot_Class.setter
    def pivot_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__pivot_Class", None)
        self.__pivot_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Behavior"):
                    opp_val = getattr(item, "pivot_Behavior", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Behavior", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Behavior"):
                    opp_val = getattr(item, "pivot_Behavior", None)
                    
                    setattr(item, "pivot_Behavior", self)
                    

class pivot_Operation(Feature, ParameterableElement, Namespace, TemplateableElement):

    def __init__(self, isInvalidating: str, isValidating: str, pivot_Operation: "pivot_CallOperationAction" = None, pivot_Operation122: "pivot_MessageType" = None, pivot_Operation147: "pivot_OpaqueExpression" = None, pivot_Operation136: set["pivot_Type"] = None, operation: set["pivot_Parameter"] = None, ownedOperation: "pivot_Type" = None, pivot_Operation141: set["pivot_Constraint"] = None, pivot_Operation144: set["pivot_Constraint"] = None, pivot_Operation150: "pivot_Precedence" = None, pivot_Operation154: "pivot_Operation" = None, pivot_Operation152: set["pivot_Operation"] = None, pivot_Operation156: "pivot_Class" = None, pivot_Operation162: "pivot_OperationCallExp" = None, Operation: "pivot_Parameter" = None, Operation323: "pivot_Type" = None):
        self.isInvalidating = isInvalidating
        self.isValidating = isValidating
        self.pivot_Operation = pivot_Operation
        self.pivot_Operation122 = pivot_Operation122
        self.pivot_Operation147 = pivot_Operation147
        self.pivot_Operation136 = pivot_Operation136 if pivot_Operation136 is not None else set()
        self.operation = operation if operation is not None else set()
        self.ownedOperation = ownedOperation
        self.pivot_Operation141 = pivot_Operation141 if pivot_Operation141 is not None else set()
        self.pivot_Operation144 = pivot_Operation144 if pivot_Operation144 is not None else set()
        self.pivot_Operation150 = pivot_Operation150
        self.pivot_Operation154 = pivot_Operation154
        self.pivot_Operation152 = pivot_Operation152 if pivot_Operation152 is not None else set()
        self.pivot_Operation156 = pivot_Operation156
        self.pivot_Operation162 = pivot_Operation162
        self.Operation = Operation
        self.Operation323 = Operation323
        
    @property
    def isValidating(self) -> str:
        return self.__isValidating

    @isValidating.setter
    def isValidating(self, isValidating: str):
        self.__isValidating = isValidating

    @property
    def isInvalidating(self) -> str:
        return self.__isInvalidating

    @isInvalidating.setter
    def isInvalidating(self, isInvalidating: str):
        self.__isInvalidating = isInvalidating

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__Operation", None)
        self.__Operation = value
        
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
    def pivot_Operation156(self):
        return self.__pivot_Operation156

    @pivot_Operation156.setter
    def pivot_Operation156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation156", None)
        self.__pivot_Operation156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Class157"):
                opp_val = getattr(old_value, "pivot_Class157", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Class157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Class157"):
                opp_val = getattr(value, "pivot_Class157", None)
                setattr(value, "pivot_Class157", self)

    @property
    def Operation323(self):
        return self.__Operation323

    @Operation323.setter
    def Operation323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__Operation323", None)
        self.__Operation323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningType322"):
                opp_val = getattr(old_value, "owningType322", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningType322"):
                opp_val = getattr(value, "owningType322", None)
                if opp_val is None:
                    setattr(value, "owningType322", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Operation136(self):
        return self.__pivot_Operation136

    @pivot_Operation136.setter
    def pivot_Operation136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation136", None)
        self.__pivot_Operation136 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Type137"):
                    opp_val = getattr(item, "pivot_Type137", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Type137", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Type137"):
                    opp_val = getattr(item, "pivot_Type137", None)
                    
                    setattr(item, "pivot_Type137", self)
                    

    @property
    def pivot_Operation144(self):
        return self.__pivot_Operation144

    @pivot_Operation144.setter
    def pivot_Operation144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation144", None)
        self.__pivot_Operation144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Constraint145"):
                    opp_val = getattr(item, "pivot_Constraint145", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Constraint145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Constraint145"):
                    opp_val = getattr(item, "pivot_Constraint145", None)
                    
                    setattr(item, "pivot_Constraint145", self)
                    

    @property
    def pivot_Operation162(self):
        return self.__pivot_Operation162

    @pivot_Operation162.setter
    def pivot_Operation162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation162", None)
        self.__pivot_Operation162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OperationCallExp161"):
                opp_val = getattr(old_value, "pivot_OperationCallExp161", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OperationCallExp161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OperationCallExp161"):
                opp_val = getattr(value, "pivot_OperationCallExp161", None)
                setattr(value, "pivot_OperationCallExp161", self)

    @property
    def pivot_Operation154(self):
        return self.__pivot_Operation154

    @pivot_Operation154.setter
    def pivot_Operation154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation154", None)
        self.__pivot_Operation154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation152"):
                opp_val = getattr(old_value, "pivot_Operation152", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation152"):
                opp_val = getattr(value, "pivot_Operation152", None)
                if opp_val is None:
                    setattr(value, "pivot_Operation152", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Operation122(self):
        return self.__pivot_Operation122

    @pivot_Operation122.setter
    def pivot_Operation122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation122", None)
        self.__pivot_Operation122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_MessageType121"):
                opp_val = getattr(old_value, "pivot_MessageType121", None)
                if opp_val == self:
                    setattr(old_value, "pivot_MessageType121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_MessageType121"):
                opp_val = getattr(value, "pivot_MessageType121", None)
                setattr(value, "pivot_MessageType121", self)

    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__operation", None)
        self.__operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

    @property
    def pivot_Operation152(self):
        return self.__pivot_Operation152

    @pivot_Operation152.setter
    def pivot_Operation152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation152", None)
        self.__pivot_Operation152 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Operation154"):
                    opp_val = getattr(item, "pivot_Operation154", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Operation154", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Operation154"):
                    opp_val = getattr(item, "pivot_Operation154", None)
                    
                    setattr(item, "pivot_Operation154", self)
                    

    @property
    def pivot_Operation(self):
        return self.__pivot_Operation

    @pivot_Operation.setter
    def pivot_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation", None)
        self.__pivot_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_CallOperationAction"):
                opp_val = getattr(old_value, "pivot_CallOperationAction", None)
                if opp_val == self:
                    setattr(old_value, "pivot_CallOperationAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_CallOperationAction"):
                opp_val = getattr(value, "pivot_CallOperationAction", None)
                setattr(value, "pivot_CallOperationAction", self)

    @property
    def pivot_Operation150(self):
        return self.__pivot_Operation150

    @pivot_Operation150.setter
    def pivot_Operation150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation150", None)
        self.__pivot_Operation150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Precedence151"):
                opp_val = getattr(old_value, "pivot_Precedence151", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Precedence151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Precedence151"):
                opp_val = getattr(value, "pivot_Precedence151", None)
                setattr(value, "pivot_Precedence151", self)

    @property
    def pivot_Operation141(self):
        return self.__pivot_Operation141

    @pivot_Operation141.setter
    def pivot_Operation141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation141", None)
        self.__pivot_Operation141 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Constraint142"):
                    opp_val = getattr(item, "pivot_Constraint142", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Constraint142", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Constraint142"):
                    opp_val = getattr(item, "pivot_Constraint142", None)
                    
                    setattr(item, "pivot_Constraint142", self)
                    

    @property
    def pivot_Operation147(self):
        return self.__pivot_Operation147

    @pivot_Operation147.setter
    def pivot_Operation147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation147", None)
        self.__pivot_Operation147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OpaqueExpression148"):
                opp_val = getattr(old_value, "pivot_OpaqueExpression148", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OpaqueExpression148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OpaqueExpression148"):
                opp_val = getattr(value, "pivot_OpaqueExpression148", None)
                setattr(value, "pivot_OpaqueExpression148", self)

    @property
    def ownedOperation(self):
        return self.__ownedOperation

    @ownedOperation.setter
    def ownedOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__ownedOperation", None)
        self.__ownedOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type"):
                opp_val = getattr(old_value, "Type", None)
                if opp_val == self:
                    setattr(old_value, "Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type"):
                opp_val = getattr(value, "Type", None)
                setattr(value, "Type", self)

    def CompatibleReturn(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CompatibleReturn method
        pass

    def UniquePreconditionName(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement UniquePreconditionName method
        pass

    def LoadableImplementation(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement LoadableImplementation method
        pass

    def UniquePostconditionName(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement UniquePostconditionName method
        pass

class pivot_Element(Visitable):

    def __init__(self, pivot_Element: "pivot_Annotation" = None, pivot_Element5: "pivot_Annotation" = None, pivot_Element21: "pivot_Comment" = None, pivot_Element29: "pivot_Constraint" = None, pivot_Element49: set["pivot_Comment"] = None, base: set["pivot_ElementExtension"] = None, Element: "pivot_ElementExtension" = None):
        self.pivot_Element = pivot_Element
        self.pivot_Element5 = pivot_Element5
        self.pivot_Element21 = pivot_Element21
        self.pivot_Element29 = pivot_Element29
        self.pivot_Element49 = pivot_Element49 if pivot_Element49 is not None else set()
        self.base = base if base is not None else set()
        self.Element = Element
        
    @property
    def Element(self):
        return self.__Element

    @Element.setter
    def Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Element__Element", None)
        self.__Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extension"):
                opp_val = getattr(old_value, "extension", None)
                if opp_val == self:
                    setattr(old_value, "extension", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extension"):
                opp_val = getattr(value, "extension", None)
                setattr(value, "extension", self)

    @property
    def pivot_Element(self):
        return self.__pivot_Element

    @pivot_Element.setter
    def pivot_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Element__pivot_Element", None)
        self.__pivot_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Annotation"):
                opp_val = getattr(old_value, "pivot_Annotation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Annotation"):
                opp_val = getattr(value, "pivot_Annotation", None)
                if opp_val is None:
                    setattr(value, "pivot_Annotation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Element29(self):
        return self.__pivot_Element29

    @pivot_Element29.setter
    def pivot_Element29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Element__pivot_Element29", None)
        self.__pivot_Element29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Constraint"):
                opp_val = getattr(old_value, "pivot_Constraint", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Constraint"):
                opp_val = getattr(value, "pivot_Constraint", None)
                if opp_val is None:
                    setattr(value, "pivot_Constraint", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Element49(self):
        return self.__pivot_Element49

    @pivot_Element49.setter
    def pivot_Element49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Element__pivot_Element49", None)
        self.__pivot_Element49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Comment50"):
                    opp_val = getattr(item, "pivot_Comment50", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Comment50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Comment50"):
                    opp_val = getattr(item, "pivot_Comment50", None)
                    
                    setattr(item, "pivot_Comment50", self)
                    

    @property
    def pivot_Element5(self):
        return self.__pivot_Element5

    @pivot_Element5.setter
    def pivot_Element5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Element__pivot_Element5", None)
        self.__pivot_Element5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Annotation4"):
                opp_val = getattr(old_value, "pivot_Annotation4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Annotation4"):
                opp_val = getattr(value, "pivot_Annotation4", None)
                if opp_val is None:
                    setattr(value, "pivot_Annotation4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Element__base", None)
        self.__base = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElementExtension"):
                    opp_val = getattr(item, "ElementExtension", None)
                    
                    if opp_val == self:
                        setattr(item, "ElementExtension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElementExtension"):
                    opp_val = getattr(item, "ElementExtension", None)
                    
                    setattr(item, "ElementExtension", self)
                    

    @property
    def pivot_Element21(self):
        return self.__pivot_Element21

    @pivot_Element21.setter
    def pivot_Element21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Element__pivot_Element21", None)
        self.__pivot_Element21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Comment"):
                opp_val = getattr(old_value, "pivot_Comment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Comment"):
                opp_val = getattr(value, "pivot_Comment", None)
                if opp_val is None:
                    setattr(value, "pivot_Comment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def allOwnedElements(self) -> Element:
        # TODO: Implement allOwnedElements method
        pass

    def getValue(self, stereotype: Type, propertyName: str) -> Element:
        # TODO: Implement getValue method
        pass

class PrimitiveLiteralExp:

    pass
class pivot_NullLiteralExp(PrimitiveLiteralExp):

    pass
class pivot_StringLiteralExp(PrimitiveLiteralExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class pivot_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class pivot_BooleanLiteralExp(PrimitiveLiteralExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

    def TypeIsBoolean(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement TypeIsBoolean method
        pass

class CollectionType:

    pass
class pivot_SequenceType(CollectionType):

    pass
class pivot_SetType(CollectionType):

    pass
class pivot_OrderedSetType(CollectionType):

    pass
class pivot_BagType(CollectionType):

    pass
class NavigationCallExp:

    pass
class pivot_PropertyCallExp(NavigationCallExp, ReferringElement):

    def __init__(self, pivot_PropertyCallExp: "pivot_Property" = None):
        self.pivot_PropertyCallExp = pivot_PropertyCallExp
        
    @property
    def pivot_PropertyCallExp(self):
        return self.__pivot_PropertyCallExp

    @pivot_PropertyCallExp.setter
    def pivot_PropertyCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_PropertyCallExp__pivot_PropertyCallExp", None)
        self.__pivot_PropertyCallExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property201"):
                opp_val = getattr(old_value, "pivot_Property201", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property201"):
                opp_val = getattr(value, "pivot_Property201", None)
                setattr(value, "pivot_Property201", self)

    def NonStaticSourceTypeIsConformant(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NonStaticSourceTypeIsConformant method
        pass

    def getSpecializedReferredPropertyOwningType(self) -> Type:
        # TODO: Implement getSpecializedReferredPropertyOwningType method
        pass

    def CompatibleResultType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement CompatibleResultType method
        pass

    def getSpecializedReferredPropertyType(self) -> Type:
        # TODO: Implement getSpecializedReferredPropertyType method
        pass

class pivot_AssociationClassCallExp(NavigationCallExp):

    pass
class pivot_Property(Feature, ParameterableElement):

    def __init__(self, isID: str, isReadOnly: str, default: str, isComposite: str, isDerived: str, implicit: str, isResolveProxies: str, isTransient: str, isUnsettable: str, isVolatile: str, Property: "pivot_AssociationClass" = None, pivot_Property: "pivot_ConstructorPart" = None, pivot_Property45: "pivot_DynamicProperty" = None, pivot_Property134: "pivot_NavigationCallExp" = None, pivot_Property188: "pivot_Property" = None, pivot_Property177: "pivot_Class" = None, pivot_Property181: "pivot_Property" = None, pivot_Property179: "pivot_Property" = None, unownedAttribute: "pivot_AssociationClass" = None, pivot_Property184: "pivot_OpaqueExpression" = None, pivot_Property186: set["pivot_Property"] = None, pivot_Property191: "pivot_Property" = None, pivot_Property189: set["pivot_Property"] = None, pivot_Property194: "pivot_Property" = None, pivot_Property192: set["pivot_Property"] = None, pivot_Property197: "pivot_Property" = None, pivot_Property195: "pivot_Property" = None, ownedAttribute: "pivot_Type" = None, pivot_Property201: "pivot_PropertyCallExp" = None, Property320: "pivot_Type" = None):
        self.isID = isID
        self.isReadOnly = isReadOnly
        self.default = default
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.implicit = implicit
        self.isResolveProxies = isResolveProxies
        self.isTransient = isTransient
        self.isUnsettable = isUnsettable
        self.isVolatile = isVolatile
        self.Property = Property
        self.pivot_Property = pivot_Property
        self.pivot_Property45 = pivot_Property45
        self.pivot_Property134 = pivot_Property134
        self.pivot_Property188 = pivot_Property188
        self.pivot_Property177 = pivot_Property177
        self.pivot_Property181 = pivot_Property181
        self.pivot_Property179 = pivot_Property179
        self.unownedAttribute = unownedAttribute
        self.pivot_Property184 = pivot_Property184
        self.pivot_Property186 = pivot_Property186 if pivot_Property186 is not None else set()
        self.pivot_Property191 = pivot_Property191
        self.pivot_Property189 = pivot_Property189 if pivot_Property189 is not None else set()
        self.pivot_Property194 = pivot_Property194
        self.pivot_Property192 = pivot_Property192 if pivot_Property192 is not None else set()
        self.pivot_Property197 = pivot_Property197
        self.pivot_Property195 = pivot_Property195
        self.ownedAttribute = ownedAttribute
        self.pivot_Property201 = pivot_Property201
        self.Property320 = Property320
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def isTransient(self) -> str:
        return self.__isTransient

    @isTransient.setter
    def isTransient(self, isTransient: str):
        self.__isTransient = isTransient

    @property
    def isVolatile(self) -> str:
        return self.__isVolatile

    @isVolatile.setter
    def isVolatile(self, isVolatile: str):
        self.__isVolatile = isVolatile

    @property
    def isUnsettable(self) -> str:
        return self.__isUnsettable

    @isUnsettable.setter
    def isUnsettable(self, isUnsettable: str):
        self.__isUnsettable = isUnsettable

    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

    @property
    def isComposite(self) -> str:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite

    @property
    def implicit(self) -> str:
        return self.__implicit

    @implicit.setter
    def implicit(self, implicit: str):
        self.__implicit = implicit

    @property
    def isID(self) -> str:
        return self.__isID

    @isID.setter
    def isID(self, isID: str):
        self.__isID = isID

    @property
    def isResolveProxies(self) -> str:
        return self.__isResolveProxies

    @isResolveProxies.setter
    def isResolveProxies(self, isResolveProxies: str):
        self.__isResolveProxies = isResolveProxies

    @property
    def unownedAttribute(self):
        return self.__unownedAttribute

    @unownedAttribute.setter
    def unownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__unownedAttribute", None)
        self.__unownedAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssociationClass"):
                opp_val = getattr(old_value, "AssociationClass", None)
                if opp_val == self:
                    setattr(old_value, "AssociationClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssociationClass"):
                opp_val = getattr(value, "AssociationClass", None)
                setattr(value, "AssociationClass", self)

    @property
    def ownedAttribute(self):
        return self.__ownedAttribute

    @ownedAttribute.setter
    def ownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__ownedAttribute", None)
        self.__ownedAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type199"):
                opp_val = getattr(old_value, "Type199", None)
                if opp_val == self:
                    setattr(old_value, "Type199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type199"):
                opp_val = getattr(value, "Type199", None)
                setattr(value, "Type199", self)

    @property
    def pivot_Property191(self):
        return self.__pivot_Property191

    @pivot_Property191.setter
    def pivot_Property191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property191", None)
        self.__pivot_Property191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property189"):
                opp_val = getattr(old_value, "pivot_Property189", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property189"):
                opp_val = getattr(value, "pivot_Property189", None)
                if opp_val is None:
                    setattr(value, "pivot_Property189", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Property184(self):
        return self.__pivot_Property184

    @pivot_Property184.setter
    def pivot_Property184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property184", None)
        self.__pivot_Property184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OpaqueExpression185"):
                opp_val = getattr(old_value, "pivot_OpaqueExpression185", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OpaqueExpression185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OpaqueExpression185"):
                opp_val = getattr(value, "pivot_OpaqueExpression185", None)
                setattr(value, "pivot_OpaqueExpression185", self)

    @property
    def pivot_Property197(self):
        return self.__pivot_Property197

    @pivot_Property197.setter
    def pivot_Property197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property197", None)
        self.__pivot_Property197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property195"):
                opp_val = getattr(old_value, "pivot_Property195", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property195"):
                opp_val = getattr(value, "pivot_Property195", None)
                setattr(value, "pivot_Property195", self)

    @property
    def pivot_Property201(self):
        return self.__pivot_Property201

    @pivot_Property201.setter
    def pivot_Property201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property201", None)
        self.__pivot_Property201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_PropertyCallExp"):
                opp_val = getattr(old_value, "pivot_PropertyCallExp", None)
                if opp_val == self:
                    setattr(old_value, "pivot_PropertyCallExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_PropertyCallExp"):
                opp_val = getattr(value, "pivot_PropertyCallExp", None)
                setattr(value, "pivot_PropertyCallExp", self)

    @property
    def pivot_Property188(self):
        return self.__pivot_Property188

    @pivot_Property188.setter
    def pivot_Property188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property188", None)
        self.__pivot_Property188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property186"):
                opp_val = getattr(old_value, "pivot_Property186", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property186"):
                opp_val = getattr(value, "pivot_Property186", None)
                if opp_val is None:
                    setattr(value, "pivot_Property186", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Property194(self):
        return self.__pivot_Property194

    @pivot_Property194.setter
    def pivot_Property194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property194", None)
        self.__pivot_Property194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property192"):
                opp_val = getattr(old_value, "pivot_Property192", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property192"):
                opp_val = getattr(value, "pivot_Property192", None)
                if opp_val is None:
                    setattr(value, "pivot_Property192", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Property(self):
        return self.__pivot_Property

    @pivot_Property.setter
    def pivot_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property", None)
        self.__pivot_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_ConstructorPart36"):
                opp_val = getattr(old_value, "pivot_ConstructorPart36", None)
                if opp_val == self:
                    setattr(old_value, "pivot_ConstructorPart36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ConstructorPart36"):
                opp_val = getattr(value, "pivot_ConstructorPart36", None)
                setattr(value, "pivot_ConstructorPart36", self)

    @property
    def Property320(self):
        return self.__Property320

    @Property320.setter
    def Property320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__Property320", None)
        self.__Property320 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningType"):
                opp_val = getattr(old_value, "owningType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningType"):
                opp_val = getattr(value, "owningType", None)
                if opp_val is None:
                    setattr(value, "owningType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Property134(self):
        return self.__pivot_Property134

    @pivot_Property134.setter
    def pivot_Property134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property134", None)
        self.__pivot_Property134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_NavigationCallExp133"):
                opp_val = getattr(old_value, "pivot_NavigationCallExp133", None)
                if opp_val == self:
                    setattr(old_value, "pivot_NavigationCallExp133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_NavigationCallExp133"):
                opp_val = getattr(value, "pivot_NavigationCallExp133", None)
                setattr(value, "pivot_NavigationCallExp133", self)

    @property
    def pivot_Property186(self):
        return self.__pivot_Property186

    @pivot_Property186.setter
    def pivot_Property186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property186", None)
        self.__pivot_Property186 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Property188"):
                    opp_val = getattr(item, "pivot_Property188", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Property188", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Property188"):
                    opp_val = getattr(item, "pivot_Property188", None)
                    
                    setattr(item, "pivot_Property188", self)
                    

    @property
    def pivot_Property45(self):
        return self.__pivot_Property45

    @pivot_Property45.setter
    def pivot_Property45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property45", None)
        self.__pivot_Property45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_DynamicProperty"):
                opp_val = getattr(old_value, "pivot_DynamicProperty", None)
                if opp_val == self:
                    setattr(old_value, "pivot_DynamicProperty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_DynamicProperty"):
                opp_val = getattr(value, "pivot_DynamicProperty", None)
                setattr(value, "pivot_DynamicProperty", self)

    @property
    def pivot_Property189(self):
        return self.__pivot_Property189

    @pivot_Property189.setter
    def pivot_Property189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property189", None)
        self.__pivot_Property189 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Property191"):
                    opp_val = getattr(item, "pivot_Property191", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Property191", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Property191"):
                    opp_val = getattr(item, "pivot_Property191", None)
                    
                    setattr(item, "pivot_Property191", self)
                    

    @property
    def pivot_Property177(self):
        return self.__pivot_Property177

    @pivot_Property177.setter
    def pivot_Property177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property177", None)
        self.__pivot_Property177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Class178"):
                opp_val = getattr(old_value, "pivot_Class178", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Class178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Class178"):
                opp_val = getattr(value, "pivot_Class178", None)
                setattr(value, "pivot_Class178", self)

    @property
    def pivot_Property195(self):
        return self.__pivot_Property195

    @pivot_Property195.setter
    def pivot_Property195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property195", None)
        self.__pivot_Property195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property197"):
                opp_val = getattr(old_value, "pivot_Property197", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property197"):
                opp_val = getattr(value, "pivot_Property197", None)
                setattr(value, "pivot_Property197", self)

    @property
    def pivot_Property192(self):
        return self.__pivot_Property192

    @pivot_Property192.setter
    def pivot_Property192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property192", None)
        self.__pivot_Property192 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Property194"):
                    opp_val = getattr(item, "pivot_Property194", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Property194", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Property194"):
                    opp_val = getattr(item, "pivot_Property194", None)
                    
                    setattr(item, "pivot_Property194", self)
                    

    @property
    def Property(self):
        return self.__Property

    @Property.setter
    def Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__Property", None)
        self.__Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "association"):
                opp_val = getattr(old_value, "association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "association"):
                opp_val = getattr(value, "association", None)
                if opp_val is None:
                    setattr(value, "association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Property179(self):
        return self.__pivot_Property179

    @pivot_Property179.setter
    def pivot_Property179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property179", None)
        self.__pivot_Property179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property181"):
                opp_val = getattr(old_value, "pivot_Property181", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property181"):
                opp_val = getattr(value, "pivot_Property181", None)
                setattr(value, "pivot_Property181", self)

    @property
    def pivot_Property181(self):
        return self.__pivot_Property181

    @pivot_Property181.setter
    def pivot_Property181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property181", None)
        self.__pivot_Property181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property179"):
                opp_val = getattr(old_value, "pivot_Property179", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property179"):
                opp_val = getattr(value, "pivot_Property179", None)
                setattr(value, "pivot_Property179", self)

    def isAttribute(self, p: str) -> str:
        # TODO: Implement isAttribute method
        pass

    def CompatibleDefaultExpression(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement CompatibleDefaultExpression method
        pass

class Class:

    pass
class pivot_Metaclass(Class):

    pass
class pivot_DataType(Class):

    def __init__(self, isSerializable: str, pivot_DataType: "pivot_Type" = None):
        self.isSerializable = isSerializable
        self.pivot_DataType = pivot_DataType
        
    @property
    def isSerializable(self) -> str:
        return self.__isSerializable

    @isSerializable.setter
    def isSerializable(self, isSerializable: str):
        self.__isSerializable = isSerializable

    @property
    def pivot_DataType(self):
        return self.__pivot_DataType

    @pivot_DataType.setter
    def pivot_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_DataType__pivot_DataType", None)
        self.__pivot_DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Type41"):
                opp_val = getattr(old_value, "pivot_Type41", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Type41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Type41"):
                opp_val = getattr(value, "pivot_Type41", None)
                setattr(value, "pivot_Type41", self)

class pivot_SelfType(Class):

    def __init__(self):
        
    def specializeIn(self, expr: OCLExpression, selfType: Type) -> Type:
        # TODO: Implement specializeIn method
        pass

class pivot_Stereotype(Class):

    pass
class pivot_InvalidType(Class):

    pass
class pivot_UnspecifiedType(Class):

    pass
class pivot_Behavior(Class):

    pass
class pivot_AssociationClass(Class):

    pass
class pivot_VoidType(Class):

    pass
class pivot_AnyType(Class):

    pass
class NamedElement:

    pass
class pivot_Type(NamedElement, ParameterableElement, TemplateableElement):

    def __init__(self, instanceClassName: str, pivot_Type: "pivot_CollectionType" = None, pivot_Type41: "pivot_DataType" = None, pivot_Type43: "pivot_DynamicElement" = None, pivot_Type53: "pivot_ElementExtension" = None, pivot_Type88: "pivot_LambdaType" = None, pivot_Type91: "pivot_LambdaType" = None, pivot_Type94: "pivot_LambdaType" = None, pivot_Type124: "pivot_Metaclass" = None, pivot_Type137: "pivot_Operation" = None, Type: "pivot_Operation" = None, Type171: "pivot_Package" = None, Type199: "pivot_Property" = None, ownedType: "pivot_Package" = None, owningType: set["pivot_Property"] = None, owningType322: set["pivot_Operation"] = None, pivot_Type326: "pivot_Type" = None, pivot_Type324: set["pivot_Type"] = None, pivot_Type328: set["pivot_Constraint"] = None, pivot_Type333: "pivot_TypeTemplateParameter" = None, pivot_Type335: "pivot_TypedElement" = None, pivot_Type331: "pivot_TypeExp" = None, pivot_Type337: "pivot_UnspecifiedType" = None, pivot_Type340: "pivot_UnspecifiedType" = None):
        self.instanceClassName = instanceClassName
        self.pivot_Type = pivot_Type
        self.pivot_Type41 = pivot_Type41
        self.pivot_Type43 = pivot_Type43
        self.pivot_Type53 = pivot_Type53
        self.pivot_Type88 = pivot_Type88
        self.pivot_Type91 = pivot_Type91
        self.pivot_Type94 = pivot_Type94
        self.pivot_Type124 = pivot_Type124
        self.pivot_Type137 = pivot_Type137
        self.Type = Type
        self.Type171 = Type171
        self.Type199 = Type199
        self.ownedType = ownedType
        self.owningType = owningType if owningType is not None else set()
        self.owningType322 = owningType322 if owningType322 is not None else set()
        self.pivot_Type326 = pivot_Type326
        self.pivot_Type324 = pivot_Type324 if pivot_Type324 is not None else set()
        self.pivot_Type328 = pivot_Type328 if pivot_Type328 is not None else set()
        self.pivot_Type333 = pivot_Type333
        self.pivot_Type335 = pivot_Type335
        self.pivot_Type331 = pivot_Type331
        self.pivot_Type337 = pivot_Type337
        self.pivot_Type340 = pivot_Type340
        
    @property
    def instanceClassName(self) -> str:
        return self.__instanceClassName

    @instanceClassName.setter
    def instanceClassName(self, instanceClassName: str):
        self.__instanceClassName = instanceClassName

    @property
    def Type199(self):
        return self.__Type199

    @Type199.setter
    def Type199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__Type199", None)
        self.__Type199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedAttribute"):
                opp_val = getattr(old_value, "ownedAttribute", None)
                if opp_val == self:
                    setattr(old_value, "ownedAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedAttribute"):
                opp_val = getattr(value, "ownedAttribute", None)
                setattr(value, "ownedAttribute", self)

    @property
    def pivot_Type94(self):
        return self.__pivot_Type94

    @pivot_Type94.setter
    def pivot_Type94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type94", None)
        self.__pivot_Type94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_LambdaType93"):
                opp_val = getattr(old_value, "pivot_LambdaType93", None)
                if opp_val == self:
                    setattr(old_value, "pivot_LambdaType93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_LambdaType93"):
                opp_val = getattr(value, "pivot_LambdaType93", None)
                setattr(value, "pivot_LambdaType93", self)

    @property
    def pivot_Type328(self):
        return self.__pivot_Type328

    @pivot_Type328.setter
    def pivot_Type328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type328", None)
        self.__pivot_Type328 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Constraint329"):
                    opp_val = getattr(item, "pivot_Constraint329", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Constraint329", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Constraint329"):
                    opp_val = getattr(item, "pivot_Constraint329", None)
                    
                    setattr(item, "pivot_Constraint329", self)
                    

    @property
    def pivot_Type53(self):
        return self.__pivot_Type53

    @pivot_Type53.setter
    def pivot_Type53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type53", None)
        self.__pivot_Type53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_ElementExtension"):
                opp_val = getattr(old_value, "pivot_ElementExtension", None)
                if opp_val == self:
                    setattr(old_value, "pivot_ElementExtension", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ElementExtension"):
                opp_val = getattr(value, "pivot_ElementExtension", None)
                setattr(value, "pivot_ElementExtension", self)

    @property
    def pivot_Type43(self):
        return self.__pivot_Type43

    @pivot_Type43.setter
    def pivot_Type43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type43", None)
        self.__pivot_Type43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_DynamicElement"):
                opp_val = getattr(old_value, "pivot_DynamicElement", None)
                if opp_val == self:
                    setattr(old_value, "pivot_DynamicElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_DynamicElement"):
                opp_val = getattr(value, "pivot_DynamicElement", None)
                setattr(value, "pivot_DynamicElement", self)

    @property
    def owningType322(self):
        return self.__owningType322

    @owningType322.setter
    def owningType322(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__owningType322", None)
        self.__owningType322 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation323"):
                    opp_val = getattr(item, "Operation323", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation323", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation323"):
                    opp_val = getattr(item, "Operation323", None)
                    
                    setattr(item, "Operation323", self)
                    

    @property
    def pivot_Type91(self):
        return self.__pivot_Type91

    @pivot_Type91.setter
    def pivot_Type91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type91", None)
        self.__pivot_Type91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_LambdaType90"):
                opp_val = getattr(old_value, "pivot_LambdaType90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_LambdaType90"):
                opp_val = getattr(value, "pivot_LambdaType90", None)
                if opp_val is None:
                    setattr(value, "pivot_LambdaType90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Type333(self):
        return self.__pivot_Type333

    @pivot_Type333.setter
    def pivot_Type333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type333", None)
        self.__pivot_Type333 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_TypeTemplateParameter"):
                opp_val = getattr(old_value, "pivot_TypeTemplateParameter", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_TypeTemplateParameter"):
                opp_val = getattr(value, "pivot_TypeTemplateParameter", None)
                if opp_val is None:
                    setattr(value, "pivot_TypeTemplateParameter", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Type340(self):
        return self.__pivot_Type340

    @pivot_Type340.setter
    def pivot_Type340(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type340", None)
        self.__pivot_Type340 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_UnspecifiedType339"):
                opp_val = getattr(old_value, "pivot_UnspecifiedType339", None)
                if opp_val == self:
                    setattr(old_value, "pivot_UnspecifiedType339", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_UnspecifiedType339"):
                opp_val = getattr(value, "pivot_UnspecifiedType339", None)
                setattr(value, "pivot_UnspecifiedType339", self)

    @property
    def Type171(self):
        return self.__Type171

    @Type171.setter
    def Type171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__Type171", None)
        self.__Type171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package"):
                opp_val = getattr(old_value, "package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package"):
                opp_val = getattr(value, "package", None)
                if opp_val is None:
                    setattr(value, "package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Type331(self):
        return self.__pivot_Type331

    @pivot_Type331.setter
    def pivot_Type331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type331", None)
        self.__pivot_Type331 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_TypeExp"):
                opp_val = getattr(old_value, "pivot_TypeExp", None)
                if opp_val == self:
                    setattr(old_value, "pivot_TypeExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_TypeExp"):
                opp_val = getattr(value, "pivot_TypeExp", None)
                setattr(value, "pivot_TypeExp", self)

    @property
    def pivot_Type124(self):
        return self.__pivot_Type124

    @pivot_Type124.setter
    def pivot_Type124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type124", None)
        self.__pivot_Type124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Metaclass"):
                opp_val = getattr(old_value, "pivot_Metaclass", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Metaclass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Metaclass"):
                opp_val = getattr(value, "pivot_Metaclass", None)
                setattr(value, "pivot_Metaclass", self)

    @property
    def pivot_Type324(self):
        return self.__pivot_Type324

    @pivot_Type324.setter
    def pivot_Type324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type324", None)
        self.__pivot_Type324 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Type326"):
                    opp_val = getattr(item, "pivot_Type326", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Type326", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Type326"):
                    opp_val = getattr(item, "pivot_Type326", None)
                    
                    setattr(item, "pivot_Type326", self)
                    

    @property
    def pivot_Type(self):
        return self.__pivot_Type

    @pivot_Type.setter
    def pivot_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type", None)
        self.__pivot_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_CollectionType"):
                opp_val = getattr(old_value, "pivot_CollectionType", None)
                if opp_val == self:
                    setattr(old_value, "pivot_CollectionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_CollectionType"):
                opp_val = getattr(value, "pivot_CollectionType", None)
                setattr(value, "pivot_CollectionType", self)

    @property
    def ownedType(self):
        return self.__ownedType

    @ownedType.setter
    def ownedType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__ownedType", None)
        self.__ownedType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package318"):
                opp_val = getattr(old_value, "Package318", None)
                if opp_val == self:
                    setattr(old_value, "Package318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package318"):
                opp_val = getattr(value, "Package318", None)
                setattr(value, "Package318", self)

    @property
    def pivot_Type88(self):
        return self.__pivot_Type88

    @pivot_Type88.setter
    def pivot_Type88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type88", None)
        self.__pivot_Type88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_LambdaType"):
                opp_val = getattr(old_value, "pivot_LambdaType", None)
                if opp_val == self:
                    setattr(old_value, "pivot_LambdaType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_LambdaType"):
                opp_val = getattr(value, "pivot_LambdaType", None)
                setattr(value, "pivot_LambdaType", self)

    @property
    def Type(self):
        return self.__Type

    @Type.setter
    def Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__Type", None)
        self.__Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedOperation"):
                opp_val = getattr(old_value, "ownedOperation", None)
                if opp_val == self:
                    setattr(old_value, "ownedOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedOperation"):
                opp_val = getattr(value, "ownedOperation", None)
                setattr(value, "ownedOperation", self)

    @property
    def owningType(self):
        return self.__owningType

    @owningType.setter
    def owningType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__owningType", None)
        self.__owningType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property320"):
                    opp_val = getattr(item, "Property320", None)
                    
                    if opp_val == self:
                        setattr(item, "Property320", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property320"):
                    opp_val = getattr(item, "Property320", None)
                    
                    setattr(item, "Property320", self)
                    

    @property
    def pivot_Type41(self):
        return self.__pivot_Type41

    @pivot_Type41.setter
    def pivot_Type41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type41", None)
        self.__pivot_Type41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_DataType"):
                opp_val = getattr(old_value, "pivot_DataType", None)
                if opp_val == self:
                    setattr(old_value, "pivot_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_DataType"):
                opp_val = getattr(value, "pivot_DataType", None)
                setattr(value, "pivot_DataType", self)

    @property
    def pivot_Type335(self):
        return self.__pivot_Type335

    @pivot_Type335.setter
    def pivot_Type335(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type335", None)
        self.__pivot_Type335 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_TypedElement"):
                opp_val = getattr(old_value, "pivot_TypedElement", None)
                if opp_val == self:
                    setattr(old_value, "pivot_TypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_TypedElement"):
                opp_val = getattr(value, "pivot_TypedElement", None)
                setattr(value, "pivot_TypedElement", self)

    @property
    def pivot_Type137(self):
        return self.__pivot_Type137

    @pivot_Type137.setter
    def pivot_Type137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type137", None)
        self.__pivot_Type137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation136"):
                opp_val = getattr(old_value, "pivot_Operation136", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation136"):
                opp_val = getattr(value, "pivot_Operation136", None)
                if opp_val is None:
                    setattr(value, "pivot_Operation136", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Type337(self):
        return self.__pivot_Type337

    @pivot_Type337.setter
    def pivot_Type337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type337", None)
        self.__pivot_Type337 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_UnspecifiedType"):
                opp_val = getattr(old_value, "pivot_UnspecifiedType", None)
                if opp_val == self:
                    setattr(old_value, "pivot_UnspecifiedType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_UnspecifiedType"):
                opp_val = getattr(value, "pivot_UnspecifiedType", None)
                setattr(value, "pivot_UnspecifiedType", self)

    @property
    def pivot_Type326(self):
        return self.__pivot_Type326

    @pivot_Type326.setter
    def pivot_Type326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type326", None)
        self.__pivot_Type326 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Type324"):
                opp_val = getattr(old_value, "pivot_Type324", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Type324"):
                opp_val = getattr(value, "pivot_Type324", None)
                if opp_val is None:
                    setattr(value, "pivot_Type324", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def specializeIn(self, expr: OCLExpression, selfType: Type) -> Type:
        # TODO: Implement specializeIn method
        pass

    def UniqueInvariantName(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement UniqueInvariantName method
        pass

class pivot_CallOperationAction(NamedElement):

    pass
class pivot_Trigger(NamedElement):

    pass
class pivot_Detail(NamedElement):

    def __init__(self, value: str, pivot_Detail: "pivot_Annotation" = None):
        self.value = value
        self.pivot_Detail = pivot_Detail
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def pivot_Detail(self):
        return self.__pivot_Detail

    @pivot_Detail.setter
    def pivot_Detail(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Detail__pivot_Detail", None)
        self.__pivot_Detail = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Annotation2"):
                opp_val = getattr(old_value, "pivot_Annotation2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Annotation2"):
                opp_val = getattr(value, "pivot_Annotation2", None)
                if opp_val is None:
                    setattr(value, "pivot_Annotation2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pivot_Constraint(NamedElement):

    def __init__(self, isCallable: str, pivot_Constraint: set["pivot_Element"] = None, pivot_Constraint31: "pivot_OpaqueExpression" = None, pivot_Constraint33: "pivot_Namespace" = None, pivot_Constraint129: "pivot_Namespace" = None, pivot_Constraint142: "pivot_Operation" = None, pivot_Constraint145: "pivot_Operation" = None, pivot_Constraint238: "pivot_State" = None, pivot_Constraint305: "pivot_Transition" = None, pivot_Constraint329: "pivot_Type" = None):
        self.isCallable = isCallable
        self.pivot_Constraint = pivot_Constraint if pivot_Constraint is not None else set()
        self.pivot_Constraint31 = pivot_Constraint31
        self.pivot_Constraint33 = pivot_Constraint33
        self.pivot_Constraint129 = pivot_Constraint129
        self.pivot_Constraint142 = pivot_Constraint142
        self.pivot_Constraint145 = pivot_Constraint145
        self.pivot_Constraint238 = pivot_Constraint238
        self.pivot_Constraint305 = pivot_Constraint305
        self.pivot_Constraint329 = pivot_Constraint329
        
    @property
    def isCallable(self) -> str:
        return self.__isCallable

    @isCallable.setter
    def isCallable(self, isCallable: str):
        self.__isCallable = isCallable

    @property
    def pivot_Constraint305(self):
        return self.__pivot_Constraint305

    @pivot_Constraint305.setter
    def pivot_Constraint305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint305", None)
        self.__pivot_Constraint305 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Transition"):
                opp_val = getattr(old_value, "pivot_Transition", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Transition"):
                opp_val = getattr(value, "pivot_Transition", None)
                setattr(value, "pivot_Transition", self)

    @property
    def pivot_Constraint329(self):
        return self.__pivot_Constraint329

    @pivot_Constraint329.setter
    def pivot_Constraint329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint329", None)
        self.__pivot_Constraint329 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Type328"):
                opp_val = getattr(old_value, "pivot_Type328", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Type328"):
                opp_val = getattr(value, "pivot_Type328", None)
                if opp_val is None:
                    setattr(value, "pivot_Type328", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Constraint238(self):
        return self.__pivot_Constraint238

    @pivot_Constraint238.setter
    def pivot_Constraint238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint238", None)
        self.__pivot_Constraint238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_State237"):
                opp_val = getattr(old_value, "pivot_State237", None)
                if opp_val == self:
                    setattr(old_value, "pivot_State237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_State237"):
                opp_val = getattr(value, "pivot_State237", None)
                setattr(value, "pivot_State237", self)

    @property
    def pivot_Constraint145(self):
        return self.__pivot_Constraint145

    @pivot_Constraint145.setter
    def pivot_Constraint145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint145", None)
        self.__pivot_Constraint145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation144"):
                opp_val = getattr(old_value, "pivot_Operation144", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation144"):
                opp_val = getattr(value, "pivot_Operation144", None)
                if opp_val is None:
                    setattr(value, "pivot_Operation144", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Constraint142(self):
        return self.__pivot_Constraint142

    @pivot_Constraint142.setter
    def pivot_Constraint142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint142", None)
        self.__pivot_Constraint142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation141"):
                opp_val = getattr(old_value, "pivot_Operation141", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation141"):
                opp_val = getattr(value, "pivot_Operation141", None)
                if opp_val is None:
                    setattr(value, "pivot_Operation141", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Constraint(self):
        return self.__pivot_Constraint

    @pivot_Constraint.setter
    def pivot_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint", None)
        self.__pivot_Constraint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Element29"):
                    opp_val = getattr(item, "pivot_Element29", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Element29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Element29"):
                    opp_val = getattr(item, "pivot_Element29", None)
                    
                    setattr(item, "pivot_Element29", self)
                    

    @property
    def pivot_Constraint33(self):
        return self.__pivot_Constraint33

    @pivot_Constraint33.setter
    def pivot_Constraint33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint33", None)
        self.__pivot_Constraint33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Namespace"):
                opp_val = getattr(old_value, "pivot_Namespace", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Namespace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Namespace"):
                opp_val = getattr(value, "pivot_Namespace", None)
                setattr(value, "pivot_Namespace", self)

    @property
    def pivot_Constraint129(self):
        return self.__pivot_Constraint129

    @pivot_Constraint129.setter
    def pivot_Constraint129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint129", None)
        self.__pivot_Constraint129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Namespace128"):
                opp_val = getattr(old_value, "pivot_Namespace128", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Namespace128"):
                opp_val = getattr(value, "pivot_Namespace128", None)
                if opp_val is None:
                    setattr(value, "pivot_Namespace128", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Constraint31(self):
        return self.__pivot_Constraint31

    @pivot_Constraint31.setter
    def pivot_Constraint31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint31", None)
        self.__pivot_Constraint31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OpaqueExpression"):
                opp_val = getattr(old_value, "pivot_OpaqueExpression", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OpaqueExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OpaqueExpression"):
                opp_val = getattr(value, "pivot_OpaqueExpression", None)
                setattr(value, "pivot_OpaqueExpression", self)

    def UniqueName(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement UniqueName method
        pass

class pivot_Vertex(NamedElement):

    pass
class pivot_Signal(NamedElement):

    pass
class pivot_SendSignalAction(NamedElement):

    pass
class pivot_EnumerationLiteral(NamedElement):

    def __init__(self, value: str, pivot_EnumerationLiteral: "pivot_EnumLiteralExp" = None, EnumerationLiteral: "pivot_Enumeration" = None, ownedLiteral: "pivot_Enumeration" = None):
        self.value = value
        self.pivot_EnumerationLiteral = pivot_EnumerationLiteral
        self.EnumerationLiteral = EnumerationLiteral
        self.ownedLiteral = ownedLiteral
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def EnumerationLiteral(self):
        return self.__EnumerationLiteral

    @EnumerationLiteral.setter
    def EnumerationLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_EnumerationLiteral__EnumerationLiteral", None)
        self.__EnumerationLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "enumeration"):
                opp_val = getattr(old_value, "enumeration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "enumeration"):
                opp_val = getattr(value, "enumeration", None)
                if opp_val is None:
                    setattr(value, "enumeration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_EnumerationLiteral(self):
        return self.__pivot_EnumerationLiteral

    @pivot_EnumerationLiteral.setter
    def pivot_EnumerationLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_EnumerationLiteral__pivot_EnumerationLiteral", None)
        self.__pivot_EnumerationLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_EnumLiteralExp"):
                opp_val = getattr(old_value, "pivot_EnumLiteralExp", None)
                if opp_val == self:
                    setattr(old_value, "pivot_EnumLiteralExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_EnumLiteralExp"):
                opp_val = getattr(value, "pivot_EnumLiteralExp", None)
                setattr(value, "pivot_EnumLiteralExp", self)

    @property
    def ownedLiteral(self):
        return self.__ownedLiteral

    @ownedLiteral.setter
    def ownedLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_EnumerationLiteral__ownedLiteral", None)
        self.__ownedLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Enumeration"):
                opp_val = getattr(old_value, "Enumeration", None)
                if opp_val == self:
                    setattr(old_value, "Enumeration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Enumeration"):
                opp_val = getattr(value, "Enumeration", None)
                setattr(value, "Enumeration", self)

class pivot_Import(NamedElement):

    pass
class pivot_TypedElement(NamedElement):

    def __init__(self, isRequired: str, pivot_TypedElement: "pivot_Type" = None):
        self.isRequired = isRequired
        self.pivot_TypedElement = pivot_TypedElement
        
    @property
    def isRequired(self) -> str:
        return self.__isRequired

    @isRequired.setter
    def isRequired(self, isRequired: str):
        self.__isRequired = isRequired

    @property
    def pivot_TypedElement(self):
        return self.__pivot_TypedElement

    @pivot_TypedElement.setter
    def pivot_TypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_TypedElement__pivot_TypedElement", None)
        self.__pivot_TypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Type335"):
                opp_val = getattr(old_value, "pivot_Type335", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Type335", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Type335"):
                opp_val = getattr(value, "pivot_Type335", None)
                setattr(value, "pivot_Type335", self)

class pivot_Namespace(NamedElement):

    pass
class pivot_Precedence(NamedElement):

    def __init__(self, associativity: str, order: str, pivot_Precedence: "pivot_Library" = None, pivot_Precedence151: "pivot_Operation" = None):
        self.associativity = associativity
        self.order = order
        self.pivot_Precedence = pivot_Precedence
        self.pivot_Precedence151 = pivot_Precedence151
        
    @property
    def order(self) -> str:
        return self.__order

    @order.setter
    def order(self, order: str):
        self.__order = order

    @property
    def associativity(self) -> str:
        return self.__associativity

    @associativity.setter
    def associativity(self, associativity: str):
        self.__associativity = associativity

    @property
    def pivot_Precedence151(self):
        return self.__pivot_Precedence151

    @pivot_Precedence151.setter
    def pivot_Precedence151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Precedence__pivot_Precedence151", None)
        self.__pivot_Precedence151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation150"):
                opp_val = getattr(old_value, "pivot_Operation150", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Operation150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation150"):
                opp_val = getattr(value, "pivot_Operation150", None)
                setattr(value, "pivot_Operation150", self)

    @property
    def pivot_Precedence(self):
        return self.__pivot_Precedence

    @pivot_Precedence.setter
    def pivot_Precedence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Precedence__pivot_Precedence", None)
        self.__pivot_Precedence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Library"):
                opp_val = getattr(old_value, "pivot_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Library"):
                opp_val = getattr(value, "pivot_Library", None)
                if opp_val is None:
                    setattr(value, "pivot_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pivot_Annotation(NamedElement):

    pass