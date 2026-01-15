from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

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
class PseudostateKind(Enum):
    initial = "initial"
    deepHistory = "deepHistory"
    shallowHistory = "shallowHistory"
    join = "join"
    fork = "fork"
    junction = "junction"
    choice = "choice"
    entryPoint = "entryPoint"
    exitPoint = "exitPoint"
    terminate = "terminate"


############################################
# Definition of Classes
############################################

class pivot_Visitor(ABC):

    pass
class pivot_Visitable(ABC):

    pass
class pivot_ReferringElement(ABC):

    def __init__(self):
        
    def getReferredElement(self) -> Element:
        # TODO: Implement getReferredElement method
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
                if hasattr(item, "pivot_Type351"):
                    opp_val = getattr(item, "pivot_Type351", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Type351", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Type351"):
                    opp_val = getattr(item, "pivot_Type351", None)
                    
                    setattr(item, "pivot_Type351", self)
                    

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
class pivot_Nameable(ABC):

    pass
class pivot_MorePivotable(ABC):

    pass
class Nameable:

    pass
class Package:

    pass
class pivot_Profile(Package):

    pass
class pivot_Library(Package):

    pass
class Operation:

    pass
class pivot_Iteration(Operation):

    pass
class ReferringElement:

    pass
class pivot_OperationCallExp(FeatureCallExp, ReferringElement):

    def __init__(self, pivot_OperationCallExp: set["pivot_OCLExpression"] = None, pivot_OperationCallExp171: "pivot_Operation" = None):
        self.pivot_OperationCallExp = pivot_OperationCallExp if pivot_OperationCallExp is not None else set()
        self.pivot_OperationCallExp171 = pivot_OperationCallExp171
        
    @property
    def pivot_OperationCallExp171(self):
        return self.__pivot_OperationCallExp171

    @pivot_OperationCallExp171.setter
    def pivot_OperationCallExp171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_OperationCallExp__pivot_OperationCallExp171", None)
        self.__pivot_OperationCallExp171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation172"):
                opp_val = getattr(old_value, "pivot_Operation172", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Operation172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation172"):
                opp_val = getattr(value, "pivot_Operation172", None)
                setattr(value, "pivot_Operation172", self)

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
                if hasattr(item, "pivot_OCLExpression169"):
                    opp_val = getattr(item, "pivot_OCLExpression169", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_OCLExpression169", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_OCLExpression169"):
                    opp_val = getattr(item, "pivot_OCLExpression169", None)
                    
                    setattr(item, "pivot_OCLExpression169", self)
                    

    def ArgumentCount(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ArgumentCount method
        pass

    def ArgumentTypeIsConformant(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ArgumentTypeIsConformant method
        pass

class LoopExp:

    pass
class pivot_IteratorExp(LoopExp, ReferringElement):

    def __init__(self):
        
    def CollectTypeIsUnordered(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CollectTypeIsUnordered method
        pass

    def ClosureElementTypeIsSourceElementType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ClosureElementTypeIsSourceElementType method
        pass

    def ClosureSourceElementTypeIsBodyElementType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ClosureSourceElementTypeIsBodyElementType method
        pass

    def OneBodyTypeIsBoolean(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OneBodyTypeIsBoolean method
        pass

    def ExistsTypeIsBoolean(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ExistsTypeIsBoolean method
        pass

    def AnyBodyTypeIsBoolean(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AnyBodyTypeIsBoolean method
        pass

    def AnyHasOneIterator(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AnyHasOneIterator method
        pass

    def IteratorTypeIsSourceElementType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement IteratorTypeIsSourceElementType method
        pass

    def OneHasOneIterator(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement OneHasOneIterator method
        pass

    def CollectNestedTypeIsBag(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement CollectNestedTypeIsBag method
        pass

    def OneTypeIsBoolean(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement OneTypeIsBoolean method
        pass

    def CollectNestedTypeIsBodyType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CollectNestedTypeIsBodyType method
        pass

    def ClosureBodyTypeIsConformanttoIteratorType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ClosureBodyTypeIsConformanttoIteratorType method
        pass

    def ForAllTypeIsBoolean(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ForAllTypeIsBoolean method
        pass

    def SortedByIsOrderedIfSourceIsOrdered(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SortedByIsOrderedIfSourceIsOrdered method
        pass

    def RejectOrSelectTypeIsSourceType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RejectOrSelectTypeIsSourceType method
        pass

    def ExistsBodyTypeIsBoolean(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ExistsBodyTypeIsBoolean method
        pass

    def CollectNestedHasOneIterator(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CollectNestedHasOneIterator method
        pass

    def IsUniqueHasOneIterator(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement IsUniqueHasOneIterator method
        pass

    def SortedByHasOneIterator(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SortedByHasOneIterator method
        pass

    def RejectOrSelectHasOneIterator(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RejectOrSelectHasOneIterator method
        pass

    def CollectElementTypeIsSourceElementType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement CollectElementTypeIsSourceElementType method
        pass

    def IsUniqueTypeIsBoolean(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement IsUniqueTypeIsBoolean method
        pass

    def ClosureHasOneIterator(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ClosureHasOneIterator method
        pass

    def ForAllBodyTypeIsBoolean(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ForAllBodyTypeIsBoolean method
        pass

    def ClosureTypeIsUniqueCollection(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ClosureTypeIsUniqueCollection method
        pass

    def AnyTypeIsSourceElementType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AnyTypeIsSourceElementType method
        pass

    def CollectHasOneIterator(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CollectHasOneIterator method
        pass

    def SortedByElementTypeIsSourceElementType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SortedByElementTypeIsSourceElementType method
        pass

    def SortedByIteratorTypeIsComparable(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SortedByIteratorTypeIsComparable method
        pass

    def RejectOrSelectTypeIsBoolean(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RejectOrSelectTypeIsBoolean method
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
            if hasattr(old_value, "pivot_Variable91"):
                opp_val = getattr(old_value, "pivot_Variable91", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Variable91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Variable91"):
                opp_val = getattr(value, "pivot_Variable91", None)
                setattr(value, "pivot_Variable91", self)

    def BodyTypeConformsToResultType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BodyTypeConformsToResultType method
        pass

    def TypeIsResultType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement TypeIsResultType method
        pass

    def OneInitializer(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement OneInitializer method
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

    def TypeIsInteger(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement TypeIsInteger method
        pass

class State:

    pass
class pivot_FinalState(State):

    pass
class CallExp:

    pass
class pivot_LoopExp(CallExp):

    def __init__(self, pivot_LoopExp: "pivot_OCLExpression" = None, pivot_LoopExp113: set["pivot_Variable"] = None, pivot_LoopExp116: "pivot_Iteration" = None):
        self.pivot_LoopExp = pivot_LoopExp
        self.pivot_LoopExp113 = pivot_LoopExp113 if pivot_LoopExp113 is not None else set()
        self.pivot_LoopExp116 = pivot_LoopExp116
        
    @property
    def pivot_LoopExp113(self):
        return self.__pivot_LoopExp113

    @pivot_LoopExp113.setter
    def pivot_LoopExp113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_LoopExp__pivot_LoopExp113", None)
        self.__pivot_LoopExp113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Variable114"):
                    opp_val = getattr(item, "pivot_Variable114", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Variable114", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Variable114"):
                    opp_val = getattr(item, "pivot_Variable114", None)
                    
                    setattr(item, "pivot_Variable114", self)
                    

    @property
    def pivot_LoopExp116(self):
        return self.__pivot_LoopExp116

    @pivot_LoopExp116.setter
    def pivot_LoopExp116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_LoopExp__pivot_LoopExp116", None)
        self.__pivot_LoopExp116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Iteration117"):
                opp_val = getattr(old_value, "pivot_Iteration117", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Iteration117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Iteration117"):
                opp_val = getattr(value, "pivot_Iteration117", None)
                setattr(value, "pivot_Iteration117", self)

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
            if hasattr(old_value, "pivot_OCLExpression111"):
                opp_val = getattr(old_value, "pivot_OCLExpression111", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression111"):
                opp_val = getattr(value, "pivot_OCLExpression111", None)
                setattr(value, "pivot_OCLExpression111", self)

    def SourceIsCollection(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SourceIsCollection method
        pass

    def NoInitializers(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement NoInitializers method
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
class pivot_Parameter(TypedMultiplicityElement, VariableDeclaration):

    pass
class pivot_Feature(TypedMultiplicityElement):

    def __init__(self, implementation: str, implementationClass: str):
        self.implementation = implementation
        self.implementationClass = implementationClass
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def implementationClass(self) -> str:
        return self.__implementationClass

    @implementationClass.setter
    def implementationClass(self, implementationClass: str):
        self.__implementationClass = implementationClass

class pivot_Variable(VariableDeclaration):

    def __init__(self, implicit: str, pivot_Variable: "pivot_ExpressionInOCL" = None, pivot_Variable76: "pivot_ExpressionInOCL" = None, pivot_Variable79: "pivot_ExpressionInOCL" = None, pivot_Variable91: "pivot_IterateExp" = None, pivot_Variable108: "pivot_LetExp" = None, pivot_Variable114: "pivot_LoopExp" = None, pivot_Variable360: "pivot_OCLExpression" = None, pivot_Variable363: "pivot_Parameter" = None):
        self.implicit = implicit
        self.pivot_Variable = pivot_Variable
        self.pivot_Variable76 = pivot_Variable76
        self.pivot_Variable79 = pivot_Variable79
        self.pivot_Variable91 = pivot_Variable91
        self.pivot_Variable108 = pivot_Variable108
        self.pivot_Variable114 = pivot_Variable114
        self.pivot_Variable360 = pivot_Variable360
        self.pivot_Variable363 = pivot_Variable363
        
    @property
    def implicit(self) -> str:
        return self.__implicit

    @implicit.setter
    def implicit(self, implicit: str):
        self.__implicit = implicit

    @property
    def pivot_Variable114(self):
        return self.__pivot_Variable114

    @pivot_Variable114.setter
    def pivot_Variable114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable114", None)
        self.__pivot_Variable114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_LoopExp113"):
                opp_val = getattr(old_value, "pivot_LoopExp113", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_LoopExp113"):
                opp_val = getattr(value, "pivot_LoopExp113", None)
                if opp_val is None:
                    setattr(value, "pivot_LoopExp113", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Variable363(self):
        return self.__pivot_Variable363

    @pivot_Variable363.setter
    def pivot_Variable363(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable363", None)
        self.__pivot_Variable363 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Parameter364"):
                opp_val = getattr(old_value, "pivot_Parameter364", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Parameter364", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Parameter364"):
                opp_val = getattr(value, "pivot_Parameter364", None)
                setattr(value, "pivot_Parameter364", self)

    @property
    def pivot_Variable108(self):
        return self.__pivot_Variable108

    @pivot_Variable108.setter
    def pivot_Variable108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable108", None)
        self.__pivot_Variable108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_LetExp107"):
                opp_val = getattr(old_value, "pivot_LetExp107", None)
                if opp_val == self:
                    setattr(old_value, "pivot_LetExp107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_LetExp107"):
                opp_val = getattr(value, "pivot_LetExp107", None)
                setattr(value, "pivot_LetExp107", self)

    @property
    def pivot_Variable360(self):
        return self.__pivot_Variable360

    @pivot_Variable360.setter
    def pivot_Variable360(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable360", None)
        self.__pivot_Variable360 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OCLExpression361"):
                opp_val = getattr(old_value, "pivot_OCLExpression361", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression361", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression361"):
                opp_val = getattr(value, "pivot_OCLExpression361", None)
                setattr(value, "pivot_OCLExpression361", self)

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
            if hasattr(old_value, "pivot_ExpressionInOCL73"):
                opp_val = getattr(old_value, "pivot_ExpressionInOCL73", None)
                if opp_val == self:
                    setattr(old_value, "pivot_ExpressionInOCL73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ExpressionInOCL73"):
                opp_val = getattr(value, "pivot_ExpressionInOCL73", None)
                setattr(value, "pivot_ExpressionInOCL73", self)

    @property
    def pivot_Variable76(self):
        return self.__pivot_Variable76

    @pivot_Variable76.setter
    def pivot_Variable76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable76", None)
        self.__pivot_Variable76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_ExpressionInOCL75"):
                opp_val = getattr(old_value, "pivot_ExpressionInOCL75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ExpressionInOCL75"):
                opp_val = getattr(value, "pivot_ExpressionInOCL75", None)
                if opp_val is None:
                    setattr(value, "pivot_ExpressionInOCL75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Variable91(self):
        return self.__pivot_Variable91

    @pivot_Variable91.setter
    def pivot_Variable91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable91", None)
        self.__pivot_Variable91 = value
        
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
    def pivot_Variable79(self):
        return self.__pivot_Variable79

    @pivot_Variable79.setter
    def pivot_Variable79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable79", None)
        self.__pivot_Variable79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_ExpressionInOCL78"):
                opp_val = getattr(old_value, "pivot_ExpressionInOCL78", None)
                if opp_val == self:
                    setattr(old_value, "pivot_ExpressionInOCL78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ExpressionInOCL78"):
                opp_val = getattr(value, "pivot_ExpressionInOCL78", None)
                setattr(value, "pivot_ExpressionInOCL78", self)

    def CompatibleInitialiserType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement CompatibleInitialiserType method
        pass

class OpaqueExpression:

    pass
class pivot_ExpressionInOCL(OpaqueExpression):

    pass
class Visitable:

    pass
class DynamicElement:

    pass
class DynamicType:

    pass
class Behavior:

    pass
class pivot_StateMachine(Behavior):

    pass
class pivot_DynamicBehavior(Behavior, DynamicType):

    pass
class pivot_OpaqueExpression(ValueSpecification):

    def __init__(self, body: str, language: str, pivot_OpaqueExpression: "pivot_Constraint" = None, pivot_OpaqueExpression143: "pivot_ExpressionInOCL" = None, pivot_OpaqueExpression147: "pivot_Operation" = None, pivot_OpaqueExpression200: "pivot_Property" = None):
        self.body = body
        self.language = language
        self.pivot_OpaqueExpression = pivot_OpaqueExpression
        self.pivot_OpaqueExpression143 = pivot_OpaqueExpression143
        self.pivot_OpaqueExpression147 = pivot_OpaqueExpression147
        self.pivot_OpaqueExpression200 = pivot_OpaqueExpression200
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def pivot_OpaqueExpression143(self):
        return self.__pivot_OpaqueExpression143

    @pivot_OpaqueExpression143.setter
    def pivot_OpaqueExpression143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_OpaqueExpression__pivot_OpaqueExpression143", None)
        self.__pivot_OpaqueExpression143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_ExpressionInOCL144"):
                opp_val = getattr(old_value, "pivot_ExpressionInOCL144", None)
                if opp_val == self:
                    setattr(old_value, "pivot_ExpressionInOCL144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ExpressionInOCL144"):
                opp_val = getattr(value, "pivot_ExpressionInOCL144", None)
                setattr(value, "pivot_ExpressionInOCL144", self)

    @property
    def pivot_OpaqueExpression200(self):
        return self.__pivot_OpaqueExpression200

    @pivot_OpaqueExpression200.setter
    def pivot_OpaqueExpression200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_OpaqueExpression__pivot_OpaqueExpression200", None)
        self.__pivot_OpaqueExpression200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property199"):
                opp_val = getattr(old_value, "pivot_Property199", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property199"):
                opp_val = getattr(value, "pivot_Property199", None)
                setattr(value, "pivot_Property199", self)

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
            if hasattr(old_value, "pivot_Constraint41"):
                opp_val = getattr(old_value, "pivot_Constraint41", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Constraint41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Constraint41"):
                opp_val = getattr(value, "pivot_Constraint41", None)
                setattr(value, "pivot_Constraint41", self)

    @property
    def pivot_OpaqueExpression147(self):
        return self.__pivot_OpaqueExpression147

    @pivot_OpaqueExpression147.setter
    def pivot_OpaqueExpression147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_OpaqueExpression__pivot_OpaqueExpression147", None)
        self.__pivot_OpaqueExpression147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation146"):
                opp_val = getattr(old_value, "pivot_Operation146", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Operation146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation146"):
                opp_val = getattr(value, "pivot_Operation146", None)
                setattr(value, "pivot_Operation146", self)

class Vertex:

    pass
class pivot_Pseudostate(Vertex):

    def __init__(self, kind: str, pivot_Pseudostate: "pivot_ConnectionPointReference" = None, pivot_Pseudostate29: "pivot_ConnectionPointReference" = None, connectionPoint: "pivot_State" = None, pivot_Pseudostate223: "pivot_StateMachine" = None, Pseudostate: "pivot_State" = None, pivot_Pseudostate267: "pivot_StateMachine" = None):
        self.kind = kind
        self.pivot_Pseudostate = pivot_Pseudostate
        self.pivot_Pseudostate29 = pivot_Pseudostate29
        self.connectionPoint = connectionPoint
        self.pivot_Pseudostate223 = pivot_Pseudostate223
        self.Pseudostate = Pseudostate
        self.pivot_Pseudostate267 = pivot_Pseudostate267
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def Pseudostate(self):
        return self.__Pseudostate

    @Pseudostate.setter
    def Pseudostate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Pseudostate__Pseudostate", None)
        self.__Pseudostate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state244"):
                opp_val = getattr(old_value, "state244", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state244"):
                opp_val = getattr(value, "state244", None)
                if opp_val is None:
                    setattr(value, "state244", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Pseudostate267(self):
        return self.__pivot_Pseudostate267

    @pivot_Pseudostate267.setter
    def pivot_Pseudostate267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Pseudostate__pivot_Pseudostate267", None)
        self.__pivot_Pseudostate267 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_StateMachine266"):
                opp_val = getattr(old_value, "pivot_StateMachine266", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_StateMachine266"):
                opp_val = getattr(value, "pivot_StateMachine266", None)
                if opp_val is None:
                    setattr(value, "pivot_StateMachine266", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Pseudostate223(self):
        return self.__pivot_Pseudostate223

    @pivot_Pseudostate223.setter
    def pivot_Pseudostate223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Pseudostate__pivot_Pseudostate223", None)
        self.__pivot_Pseudostate223 = value
        
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
    def pivot_Pseudostate29(self):
        return self.__pivot_Pseudostate29

    @pivot_Pseudostate29.setter
    def pivot_Pseudostate29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Pseudostate__pivot_Pseudostate29", None)
        self.__pivot_Pseudostate29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_ConnectionPointReference28"):
                opp_val = getattr(old_value, "pivot_ConnectionPointReference28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ConnectionPointReference28"):
                opp_val = getattr(value, "pivot_ConnectionPointReference28", None)
                if opp_val is None:
                    setattr(value, "pivot_ConnectionPointReference28", set([self]))
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

    @property
    def connectionPoint(self):
        return self.__connectionPoint

    @connectionPoint.setter
    def connectionPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Pseudostate__connectionPoint", None)
        self.__connectionPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State221"):
                opp_val = getattr(old_value, "State221", None)
                if opp_val == self:
                    setattr(old_value, "State221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State221"):
                opp_val = getattr(value, "State221", None)
                setattr(value, "State221", self)

class pivot_ConnectionPointReference(Vertex):

    pass
class DataType:

    pass
class pivot_TupleType(DataType):

    pass
class pivot_PrimitiveType(DataType):

    pass
class pivot_Enumeration(DataType):

    pass
class pivot_LambdaType(DataType):

    pass
class pivot_CollectionType(DataType):

    def __init__(self, upper: str, lower: str, pivot_CollectionType: "pivot_Type" = None):
        self.upper = upper
        self.lower = lower
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

class TypedElement:

    pass
class pivot_VariableDeclaration(TypedElement):

    pass
class pivot_ValueSpecification(TypedElement, ParameterableElement):

    def __init__(self):
        
    def unlimitedValue(self) -> str:
        # TODO: Implement unlimitedValue method
        pass

    def isComputable(self) -> str:
        # TODO: Implement isComputable method
        pass

    def isNull(self) -> str:
        # TODO: Implement isNull method
        pass

    def booleanValue(self) -> str:
        # TODO: Implement booleanValue method
        pass

    def integerValue(self) -> str:
        # TODO: Implement integerValue method
        pass

    def stringValue(self) -> str:
        # TODO: Implement stringValue method
        pass

class pivot_TypedMultiplicityElement(TypedElement):

    def __init__(self):
        
    def makeParameter(self) -> str:
        # TODO: Implement makeParameter method
        pass

    def CompatibleBody(self, bodySpecification: ValueSpecification) -> str:
        # TODO: Implement CompatibleBody method
        pass

class pivot_ConstructorPart(TypedElement):

    pass
class pivot_CollectionLiteralPart(TypedElement):

    pass
class Element:

    pass
class pivot_NamedElement(Element, Nameable):

    def __init__(self, isStatic: str, name: str):
        self.isStatic = isStatic
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isStatic(self) -> str:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: str):
        self.__isStatic = isStatic

class pivot_TemplateSignature(Element):

    pass
class pivot_ProfileApplication(Element):

    def __init__(self, isStrict: str, ProfileApplication: "pivot_Package" = None, profileApplication: "pivot_Package" = None, ProfileApplication190: "pivot_Profile" = None, application: "pivot_Profile" = None):
        self.isStrict = isStrict
        self.ProfileApplication = ProfileApplication
        self.profileApplication = profileApplication
        self.ProfileApplication190 = ProfileApplication190
        self.application = application
        
    @property
    def isStrict(self) -> str:
        return self.__isStrict

    @isStrict.setter
    def isStrict(self, isStrict: str):
        self.__isStrict = isStrict

    @property
    def application(self):
        return self.__application

    @application.setter
    def application(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ProfileApplication__application", None)
        self.__application = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Profile"):
                opp_val = getattr(old_value, "Profile", None)
                if opp_val == self:
                    setattr(old_value, "Profile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Profile"):
                opp_val = getattr(value, "Profile", None)
                setattr(value, "Profile", self)

    @property
    def ProfileApplication(self):
        return self.__ProfileApplication

    @ProfileApplication.setter
    def ProfileApplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ProfileApplication__ProfileApplication", None)
        self.__ProfileApplication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applyingPackage"):
                opp_val = getattr(old_value, "applyingPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applyingPackage"):
                opp_val = getattr(value, "applyingPackage", None)
                if opp_val is None:
                    setattr(value, "applyingPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ProfileApplication190(self):
        return self.__ProfileApplication190

    @ProfileApplication190.setter
    def ProfileApplication190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ProfileApplication__ProfileApplication190", None)
        self.__ProfileApplication190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appliedProfile"):
                opp_val = getattr(old_value, "appliedProfile", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appliedProfile"):
                opp_val = getattr(value, "appliedProfile", None)
                if opp_val is None:
                    setattr(value, "appliedProfile", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def profileApplication(self):
        return self.__profileApplication

    @profileApplication.setter
    def profileApplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ProfileApplication__profileApplication", None)
        self.__profileApplication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package193"):
                opp_val = getattr(old_value, "Package193", None)
                if opp_val == self:
                    setattr(old_value, "Package193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package193"):
                opp_val = getattr(value, "Package193", None)
                setattr(value, "Package193", self)

class pivot_DynamicElement(Element):

    pass
class pivot_TemplateParameter(Element):

    pass
class pivot_TypeExtension(Element):

    def __init__(self, isRequired: str, TypeExtension: "pivot_Stereotype" = None, TypeExtension331: "pivot_Type" = None, extensionOfs: "pivot_Stereotype" = None, extendedBys: "pivot_Type" = None):
        self.isRequired = isRequired
        self.TypeExtension = TypeExtension
        self.TypeExtension331 = TypeExtension331
        self.extensionOfs = extensionOfs
        self.extendedBys = extendedBys
        
    @property
    def isRequired(self) -> str:
        return self.__isRequired

    @isRequired.setter
    def isRequired(self, isRequired: str):
        self.__isRequired = isRequired

    @property
    def extensionOfs(self):
        return self.__extensionOfs

    @extensionOfs.setter
    def extensionOfs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_TypeExtension__extensionOfs", None)
        self.__extensionOfs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Stereotype"):
                opp_val = getattr(old_value, "Stereotype", None)
                if opp_val == self:
                    setattr(old_value, "Stereotype", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Stereotype"):
                opp_val = getattr(value, "Stereotype", None)
                setattr(value, "Stereotype", self)

    @property
    def TypeExtension331(self):
        return self.__TypeExtension331

    @TypeExtension331.setter
    def TypeExtension331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_TypeExtension__TypeExtension331", None)
        self.__TypeExtension331 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type"):
                opp_val = getattr(old_value, "type", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type"):
                opp_val = getattr(value, "type", None)
                if opp_val is None:
                    setattr(value, "type", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def extendedBys(self):
        return self.__extendedBys

    @extendedBys.setter
    def extendedBys(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_TypeExtension__extendedBys", None)
        self.__extendedBys = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type349"):
                opp_val = getattr(old_value, "Type349", None)
                if opp_val == self:
                    setattr(old_value, "Type349", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type349"):
                opp_val = getattr(value, "Type349", None)
                setattr(value, "Type349", self)

    @property
    def TypeExtension(self):
        return self.__TypeExtension

    @TypeExtension.setter
    def TypeExtension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_TypeExtension__TypeExtension", None)
        self.__TypeExtension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stereotype"):
                opp_val = getattr(old_value, "stereotype", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stereotype"):
                opp_val = getattr(value, "stereotype", None)
                if opp_val is None:
                    setattr(value, "stereotype", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pivot_TemplateableElement(Element):

    def __init__(self, TemplateableElement: "pivot_TemplateBinding" = None, boundElement: set["pivot_TemplateBinding"] = None, TemplateableElement301: "pivot_TemplateSignature" = None, template: "pivot_TemplateSignature" = None, pivot_TemplateableElement: "pivot_TemplateableElement" = None, pivot_TemplateableElement306: "pivot_TemplateableElement" = None):
        self.TemplateableElement = TemplateableElement
        self.boundElement = boundElement if boundElement is not None else set()
        self.TemplateableElement301 = TemplateableElement301
        self.template = template
        self.pivot_TemplateableElement = pivot_TemplateableElement
        self.pivot_TemplateableElement306 = pivot_TemplateableElement306
        
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
                if hasattr(item, "TemplateBinding305"):
                    opp_val = getattr(item, "TemplateBinding305", None)
                    
                    if opp_val == self:
                        setattr(item, "TemplateBinding305", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TemplateBinding305"):
                    opp_val = getattr(item, "TemplateBinding305", None)
                    
                    setattr(item, "TemplateBinding305", self)
                    

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
            if hasattr(old_value, "TemplateSignature303"):
                opp_val = getattr(old_value, "TemplateSignature303", None)
                if opp_val == self:
                    setattr(old_value, "TemplateSignature303", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TemplateSignature303"):
                opp_val = getattr(value, "TemplateSignature303", None)
                setattr(value, "TemplateSignature303", self)

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
            if hasattr(old_value, "pivot_TemplateableElement306"):
                opp_val = getattr(old_value, "pivot_TemplateableElement306", None)
                if opp_val == self:
                    setattr(old_value, "pivot_TemplateableElement306", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_TemplateableElement306"):
                opp_val = getattr(value, "pivot_TemplateableElement306", None)
                setattr(value, "pivot_TemplateableElement306", self)

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
            if hasattr(old_value, "templateBinding"):
                opp_val = getattr(old_value, "templateBinding", None)
                if opp_val == self:
                    setattr(old_value, "templateBinding", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "templateBinding"):
                opp_val = getattr(value, "templateBinding", None)
                setattr(value, "templateBinding", self)

    @property
    def TemplateableElement301(self):
        return self.__TemplateableElement301

    @TemplateableElement301.setter
    def TemplateableElement301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_TemplateableElement__TemplateableElement301", None)
        self.__TemplateableElement301 = value
        
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
    def pivot_TemplateableElement306(self):
        return self.__pivot_TemplateableElement306

    @pivot_TemplateableElement306.setter
    def pivot_TemplateableElement306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_TemplateableElement__pivot_TemplateableElement306", None)
        self.__pivot_TemplateableElement306 = value
        
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

    def isTemplate(self) -> str:
        # TODO: Implement isTemplate method
        pass

    def parameterableElements(self) -> ParameterableElement:
        # TODO: Implement parameterableElements method
        pass

class pivot_TemplateBinding(Element):

    pass
class pivot_DynamicProperty(Element):

    def __init__(self, default: str, pivot_DynamicProperty57: "pivot_DynamicType" = None, pivot_DynamicProperty: "pivot_Property" = None):
        self.default = default
        self.pivot_DynamicProperty57 = pivot_DynamicProperty57
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
            if hasattr(old_value, "pivot_Property55"):
                opp_val = getattr(old_value, "pivot_Property55", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property55"):
                opp_val = getattr(value, "pivot_Property55", None)
                setattr(value, "pivot_Property55", self)

    @property
    def pivot_DynamicProperty57(self):
        return self.__pivot_DynamicProperty57

    @pivot_DynamicProperty57.setter
    def pivot_DynamicProperty57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_DynamicProperty__pivot_DynamicProperty57", None)
        self.__pivot_DynamicProperty57 = value
        
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

class pivot_ParameterableElement(Element):

    def __init__(self, ownedParameteredElement: "pivot_TemplateParameter" = None, parameteredElement: "pivot_TemplateParameter" = None, pivot_ParameterableElement: "pivot_TemplateParameter" = None, pivot_ParameterableElement283: "pivot_TemplateParameter" = None, ParameterableElement: "pivot_TemplateParameter" = None, ParameterableElement286: "pivot_TemplateParameter" = None, pivot_ParameterableElement290: "pivot_TemplateParameterSubstitution" = None, pivot_ParameterableElement296: "pivot_TemplateParameterSubstitution" = None):
        self.ownedParameteredElement = ownedParameteredElement
        self.parameteredElement = parameteredElement
        self.pivot_ParameterableElement = pivot_ParameterableElement
        self.pivot_ParameterableElement283 = pivot_ParameterableElement283
        self.ParameterableElement = ParameterableElement
        self.ParameterableElement286 = ParameterableElement286
        self.pivot_ParameterableElement290 = pivot_ParameterableElement290
        self.pivot_ParameterableElement296 = pivot_ParameterableElement296
        
    @property
    def pivot_ParameterableElement290(self):
        return self.__pivot_ParameterableElement290

    @pivot_ParameterableElement290.setter
    def pivot_ParameterableElement290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ParameterableElement__pivot_ParameterableElement290", None)
        self.__pivot_ParameterableElement290 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_TemplateParameterSubstitution"):
                opp_val = getattr(old_value, "pivot_TemplateParameterSubstitution", None)
                if opp_val == self:
                    setattr(old_value, "pivot_TemplateParameterSubstitution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_TemplateParameterSubstitution"):
                opp_val = getattr(value, "pivot_TemplateParameterSubstitution", None)
                setattr(value, "pivot_TemplateParameterSubstitution", self)

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
            if hasattr(old_value, "TemplateParameter188"):
                opp_val = getattr(old_value, "TemplateParameter188", None)
                if opp_val == self:
                    setattr(old_value, "TemplateParameter188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TemplateParameter188"):
                opp_val = getattr(value, "TemplateParameter188", None)
                setattr(value, "TemplateParameter188", self)

    @property
    def pivot_ParameterableElement296(self):
        return self.__pivot_ParameterableElement296

    @pivot_ParameterableElement296.setter
    def pivot_ParameterableElement296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ParameterableElement__pivot_ParameterableElement296", None)
        self.__pivot_ParameterableElement296 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_TemplateParameterSubstitution295"):
                opp_val = getattr(old_value, "pivot_TemplateParameterSubstitution295", None)
                if opp_val == self:
                    setattr(old_value, "pivot_TemplateParameterSubstitution295", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_TemplateParameterSubstitution295"):
                opp_val = getattr(value, "pivot_TemplateParameterSubstitution295", None)
                setattr(value, "pivot_TemplateParameterSubstitution295", self)

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
            if hasattr(old_value, "owningTemplateParameter"):
                opp_val = getattr(old_value, "owningTemplateParameter", None)
                if opp_val == self:
                    setattr(old_value, "owningTemplateParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningTemplateParameter"):
                opp_val = getattr(value, "owningTemplateParameter", None)
                setattr(value, "owningTemplateParameter", self)

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
    def pivot_ParameterableElement283(self):
        return self.__pivot_ParameterableElement283

    @pivot_ParameterableElement283.setter
    def pivot_ParameterableElement283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ParameterableElement__pivot_ParameterableElement283", None)
        self.__pivot_ParameterableElement283 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_TemplateParameter282"):
                opp_val = getattr(old_value, "pivot_TemplateParameter282", None)
                if opp_val == self:
                    setattr(old_value, "pivot_TemplateParameter282", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_TemplateParameter282"):
                opp_val = getattr(value, "pivot_TemplateParameter282", None)
                setattr(value, "pivot_TemplateParameter282", self)

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
    def ParameterableElement286(self):
        return self.__ParameterableElement286

    @ParameterableElement286.setter
    def ParameterableElement286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ParameterableElement__ParameterableElement286", None)
        self.__ParameterableElement286 = value
        
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

    def isTemplateParameter(self) -> str:
        # TODO: Implement isTemplateParameter method
        pass

    def isCompatibleWith(self, p: ParameterableElement) -> str:
        # TODO: Implement isCompatibleWith method
        pass

class pivot_TemplateParameterSubstitution(Element):

    pass
class pivot_Comment(Element):

    def __init__(self, body: str, pivot_Comment: set["pivot_Element"] = None, pivot_Comment64: "pivot_Element" = None):
        self.body = body
        self.pivot_Comment = pivot_Comment if pivot_Comment is not None else set()
        self.pivot_Comment64 = pivot_Comment64
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def pivot_Comment64(self):
        return self.__pivot_Comment64

    @pivot_Comment64.setter
    def pivot_Comment64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Comment__pivot_Comment64", None)
        self.__pivot_Comment64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Element63"):
                opp_val = getattr(old_value, "pivot_Element63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Element63"):
                opp_val = getattr(value, "pivot_Element63", None)
                if opp_val is None:
                    setattr(value, "pivot_Element63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "pivot_Element25"):
                    opp_val = getattr(item, "pivot_Element25", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Element25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Element25"):
                    opp_val = getattr(item, "pivot_Element25", None)
                    
                    setattr(item, "pivot_Element25", self)
                    

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
            if hasattr(old_value, "pivot_OCLExpression16"):
                opp_val = getattr(old_value, "pivot_OCLExpression16", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression16"):
                opp_val = getattr(value, "pivot_OCLExpression16", None)
                setattr(value, "pivot_OCLExpression16", self)

    def TypeIsItemType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement TypeIsItemType method
        pass

class Namespace:

    pass
class pivot_Package(Namespace, TemplateableElement):

    def __init__(self, nsPrefix: str, nsURI: str, applyingPackage: set["pivot_ProfileApplication"] = None, pivot_Package: "pivot_Package" = None, pivot_Package175: set["pivot_Package"] = None, Package: "pivot_Package" = None, nestingPackage: set["pivot_Package"] = None, Package181: "pivot_Package" = None, nestedPackage: "pivot_Package" = None, package: set["pivot_Type"] = None, Package193: "pivot_ProfileApplication" = None, pivot_Package238: "pivot_Root" = None, Package341: "pivot_Type" = None):
        self.nsPrefix = nsPrefix
        self.nsURI = nsURI
        self.applyingPackage = applyingPackage if applyingPackage is not None else set()
        self.pivot_Package = pivot_Package
        self.pivot_Package175 = pivot_Package175 if pivot_Package175 is not None else set()
        self.Package = Package
        self.nestingPackage = nestingPackage if nestingPackage is not None else set()
        self.Package181 = Package181
        self.nestedPackage = nestedPackage
        self.package = package if package is not None else set()
        self.Package193 = Package193
        self.pivot_Package238 = pivot_Package238
        self.Package341 = Package341
        
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
    def Package181(self):
        return self.__Package181

    @Package181.setter
    def Package181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__Package181", None)
        self.__Package181 = value
        
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
    def nestedPackage(self):
        return self.__nestedPackage

    @nestedPackage.setter
    def nestedPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__nestedPackage", None)
        self.__nestedPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package181"):
                opp_val = getattr(old_value, "Package181", None)
                if opp_val == self:
                    setattr(old_value, "Package181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package181"):
                opp_val = getattr(value, "Package181", None)
                setattr(value, "Package181", self)

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
    def Package193(self):
        return self.__Package193

    @Package193.setter
    def Package193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__Package193", None)
        self.__Package193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profileApplication"):
                opp_val = getattr(old_value, "profileApplication", None)
                if opp_val == self:
                    setattr(old_value, "profileApplication", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profileApplication"):
                opp_val = getattr(value, "profileApplication", None)
                setattr(value, "profileApplication", self)

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
            if hasattr(old_value, "pivot_Package175"):
                opp_val = getattr(old_value, "pivot_Package175", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Package175"):
                opp_val = getattr(value, "pivot_Package175", None)
                if opp_val is None:
                    setattr(value, "pivot_Package175", set([self]))
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
    def pivot_Package175(self):
        return self.__pivot_Package175

    @pivot_Package175.setter
    def pivot_Package175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__pivot_Package175", None)
        self.__pivot_Package175 = value if value is not None else set()
        
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
                if hasattr(item, "Type183"):
                    opp_val = getattr(item, "Type183", None)
                    
                    if opp_val == self:
                        setattr(item, "Type183", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type183"):
                    opp_val = getattr(item, "Type183", None)
                    
                    setattr(item, "Type183", self)
                    

    @property
    def pivot_Package238(self):
        return self.__pivot_Package238

    @pivot_Package238.setter
    def pivot_Package238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__pivot_Package238", None)
        self.__pivot_Package238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Root237"):
                opp_val = getattr(old_value, "pivot_Root237", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Root237"):
                opp_val = getattr(value, "pivot_Root237", None)
                if opp_val is None:
                    setattr(value, "pivot_Root237", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Package341(self):
        return self.__Package341

    @Package341.setter
    def Package341(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__Package341", None)
        self.__Package341 = value
        
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
    def applyingPackage(self):
        return self.__applyingPackage

    @applyingPackage.setter
    def applyingPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__applyingPackage", None)
        self.__applyingPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProfileApplication"):
                    opp_val = getattr(item, "ProfileApplication", None)
                    
                    if opp_val == self:
                        setattr(item, "ProfileApplication", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProfileApplication"):
                    opp_val = getattr(item, "ProfileApplication", None)
                    
                    setattr(item, "ProfileApplication", self)
                    

class pivot_Root(Namespace):

    def __init__(self, externalURI: str, pivot_Root: set["pivot_Import"] = None, pivot_Root237: set["pivot_Package"] = None):
        self.externalURI = externalURI
        self.pivot_Root = pivot_Root if pivot_Root is not None else set()
        self.pivot_Root237 = pivot_Root237 if pivot_Root237 is not None else set()
        
    @property
    def externalURI(self) -> str:
        return self.__externalURI

    @externalURI.setter
    def externalURI(self, externalURI: str):
        self.__externalURI = externalURI

    @property
    def pivot_Root237(self):
        return self.__pivot_Root237

    @pivot_Root237.setter
    def pivot_Root237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Root__pivot_Root237", None)
        self.__pivot_Root237 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Package238"):
                    opp_val = getattr(item, "pivot_Package238", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Package238", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Package238"):
                    opp_val = getattr(item, "pivot_Package238", None)
                    
                    setattr(item, "pivot_Package238", self)
                    

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
                if hasattr(item, "pivot_Import235"):
                    opp_val = getattr(item, "pivot_Import235", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Import235", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Import235"):
                    opp_val = getattr(item, "pivot_Import235", None)
                    
                    setattr(item, "pivot_Import235", self)
                    

class pivot_Region(Namespace):

    pass
class pivot_State(Namespace, Vertex):

    def __init__(self, isComposite: str, isOrthogonal: str, isSimple: str, isSubmachineState: str, State: "pivot_ConnectionPointReference" = None, State36: "pivot_Constraint" = None, State221: "pivot_Pseudostate" = None, State227: "pivot_Region" = None, state246: set["pivot_Trigger"] = None, state: set["pivot_ConnectionPointReference"] = None, state244: set["pivot_Pseudostate"] = None, pivot_State: "pivot_Behavior" = None, pivot_State250: "pivot_Behavior" = None, pivot_State253: "pivot_Behavior" = None, pivot_State264: "pivot_StateExp" = None, pivot_State257: "pivot_State" = None, pivot_State255: "pivot_State" = None, state259: set["pivot_Region"] = None, owningState: "pivot_Constraint" = None, submachineState: "pivot_StateMachine" = None, State274: "pivot_StateMachine" = None, State323: "pivot_Trigger" = None):
        self.isComposite = isComposite
        self.isOrthogonal = isOrthogonal
        self.isSimple = isSimple
        self.isSubmachineState = isSubmachineState
        self.State = State
        self.State36 = State36
        self.State221 = State221
        self.State227 = State227
        self.state246 = state246 if state246 is not None else set()
        self.state = state if state is not None else set()
        self.state244 = state244 if state244 is not None else set()
        self.pivot_State = pivot_State
        self.pivot_State250 = pivot_State250
        self.pivot_State253 = pivot_State253
        self.pivot_State264 = pivot_State264
        self.pivot_State257 = pivot_State257
        self.pivot_State255 = pivot_State255
        self.state259 = state259 if state259 is not None else set()
        self.owningState = owningState
        self.submachineState = submachineState
        self.State274 = State274
        self.State323 = State323
        
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
    def isSimple(self) -> str:
        return self.__isSimple

    @isSimple.setter
    def isSimple(self, isSimple: str):
        self.__isSimple = isSimple

    @property
    def isOrthogonal(self) -> str:
        return self.__isOrthogonal

    @isOrthogonal.setter
    def isOrthogonal(self, isOrthogonal: str):
        self.__isOrthogonal = isOrthogonal

    @property
    def State221(self):
        return self.__State221

    @State221.setter
    def State221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__State221", None)
        self.__State221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connectionPoint"):
                opp_val = getattr(old_value, "connectionPoint", None)
                if opp_val == self:
                    setattr(old_value, "connectionPoint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connectionPoint"):
                opp_val = getattr(value, "connectionPoint", None)
                setattr(value, "connectionPoint", self)

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
            if hasattr(old_value, "pivot_Behavior248"):
                opp_val = getattr(old_value, "pivot_Behavior248", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Behavior248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Behavior248"):
                opp_val = getattr(value, "pivot_Behavior248", None)
                setattr(value, "pivot_Behavior248", self)

    @property
    def pivot_State255(self):
        return self.__pivot_State255

    @pivot_State255.setter
    def pivot_State255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State255", None)
        self.__pivot_State255 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_State257"):
                opp_val = getattr(old_value, "pivot_State257", None)
                if opp_val == self:
                    setattr(old_value, "pivot_State257", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_State257"):
                opp_val = getattr(value, "pivot_State257", None)
                setattr(value, "pivot_State257", self)

    @property
    def pivot_State253(self):
        return self.__pivot_State253

    @pivot_State253.setter
    def pivot_State253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State253", None)
        self.__pivot_State253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Behavior254"):
                opp_val = getattr(old_value, "pivot_Behavior254", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Behavior254", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Behavior254"):
                opp_val = getattr(value, "pivot_Behavior254", None)
                setattr(value, "pivot_Behavior254", self)

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
            if hasattr(old_value, "StateMachine262"):
                opp_val = getattr(old_value, "StateMachine262", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine262"):
                opp_val = getattr(value, "StateMachine262", None)
                setattr(value, "StateMachine262", self)

    @property
    def State274(self):
        return self.__State274

    @State274.setter
    def State274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__State274", None)
        self.__State274 = value
        
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
    def state244(self):
        return self.__state244

    @state244.setter
    def state244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__state244", None)
        self.__state244 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Pseudostate"):
                    opp_val = getattr(item, "Pseudostate", None)
                    
                    if opp_val == self:
                        setattr(item, "Pseudostate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Pseudostate"):
                    opp_val = getattr(item, "Pseudostate", None)
                    
                    setattr(item, "Pseudostate", self)
                    

    @property
    def State36(self):
        return self.__State36

    @State36.setter
    def State36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__State36", None)
        self.__State36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateInvariant"):
                opp_val = getattr(old_value, "stateInvariant", None)
                if opp_val == self:
                    setattr(old_value, "stateInvariant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateInvariant"):
                opp_val = getattr(value, "stateInvariant", None)
                setattr(value, "stateInvariant", self)

    @property
    def pivot_State264(self):
        return self.__pivot_State264

    @pivot_State264.setter
    def pivot_State264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State264", None)
        self.__pivot_State264 = value
        
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
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__state", None)
        self.__state = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConnectionPointReference"):
                    opp_val = getattr(item, "ConnectionPointReference", None)
                    
                    if opp_val == self:
                        setattr(item, "ConnectionPointReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConnectionPointReference"):
                    opp_val = getattr(item, "ConnectionPointReference", None)
                    
                    setattr(item, "ConnectionPointReference", self)
                    

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
            if hasattr(old_value, "connection"):
                opp_val = getattr(old_value, "connection", None)
                if opp_val == self:
                    setattr(old_value, "connection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection"):
                opp_val = getattr(value, "connection", None)
                setattr(value, "connection", self)

    @property
    def pivot_State257(self):
        return self.__pivot_State257

    @pivot_State257.setter
    def pivot_State257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State257", None)
        self.__pivot_State257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_State255"):
                opp_val = getattr(old_value, "pivot_State255", None)
                if opp_val == self:
                    setattr(old_value, "pivot_State255", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_State255"):
                opp_val = getattr(value, "pivot_State255", None)
                setattr(value, "pivot_State255", self)

    @property
    def State227(self):
        return self.__State227

    @State227.setter
    def State227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__State227", None)
        self.__State227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "region"):
                opp_val = getattr(old_value, "region", None)
                if opp_val == self:
                    setattr(old_value, "region", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "region"):
                opp_val = getattr(value, "region", None)
                setattr(value, "region", self)

    @property
    def pivot_State250(self):
        return self.__pivot_State250

    @pivot_State250.setter
    def pivot_State250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State250", None)
        self.__pivot_State250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Behavior251"):
                opp_val = getattr(old_value, "pivot_Behavior251", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Behavior251", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Behavior251"):
                opp_val = getattr(value, "pivot_Behavior251", None)
                setattr(value, "pivot_Behavior251", self)

    @property
    def state259(self):
        return self.__state259

    @state259.setter
    def state259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__state259", None)
        self.__state259 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Region"):
                    opp_val = getattr(item, "Region", None)
                    
                    if opp_val == self:
                        setattr(item, "Region", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Region"):
                    opp_val = getattr(item, "Region", None)
                    
                    setattr(item, "Region", self)
                    

    @property
    def owningState(self):
        return self.__owningState

    @owningState.setter
    def owningState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__owningState", None)
        self.__owningState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Constraint"):
                opp_val = getattr(old_value, "Constraint", None)
                if opp_val == self:
                    setattr(old_value, "Constraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Constraint"):
                opp_val = getattr(value, "Constraint", None)
                setattr(value, "Constraint", self)

    @property
    def State323(self):
        return self.__State323

    @State323.setter
    def State323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__State323", None)
        self.__State323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deferrableTrigger"):
                opp_val = getattr(old_value, "deferrableTrigger", None)
                if opp_val == self:
                    setattr(old_value, "deferrableTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deferrableTrigger"):
                opp_val = getattr(value, "deferrableTrigger", None)
                setattr(value, "deferrableTrigger", self)

    @property
    def state246(self):
        return self.__state246

    @state246.setter
    def state246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__state246", None)
        self.__state246 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Trigger"):
                    opp_val = getattr(item, "Trigger", None)
                    
                    if opp_val == self:
                        setattr(item, "Trigger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trigger"):
                    opp_val = getattr(item, "Trigger", None)
                    
                    setattr(item, "Trigger", self)
                    

class Type:

    pass
class pivot_MessageType(Type):

    pass
class pivot_ElementExtension(Type):

    def __init__(self, isApplied: str, isRequired: str, ElementExtension: "pivot_Element" = None, extension: "pivot_Element" = None, pivot_ElementExtension: "pivot_Stereotype" = None):
        self.isApplied = isApplied
        self.isRequired = isRequired
        self.ElementExtension = ElementExtension
        self.extension = extension
        self.pivot_ElementExtension = pivot_ElementExtension
        
    @property
    def isRequired(self) -> str:
        return self.__isRequired

    @isRequired.setter
    def isRequired(self, isRequired: str):
        self.__isRequired = isRequired

    @property
    def isApplied(self) -> str:
        return self.__isApplied

    @isApplied.setter
    def isApplied(self, isApplied: str):
        self.__isApplied = isApplied

    @property
    def ElementExtension(self):
        return self.__ElementExtension

    @ElementExtension.setter
    def ElementExtension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ElementExtension__ElementExtension", None)
        self.__ElementExtension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "base"):
                opp_val = getattr(old_value, "base", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "base"):
                opp_val = getattr(value, "base", None)
                if opp_val is None:
                    setattr(value, "base", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_ElementExtension(self):
        return self.__pivot_ElementExtension

    @pivot_ElementExtension.setter
    def pivot_ElementExtension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ElementExtension__pivot_ElementExtension", None)
        self.__pivot_ElementExtension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Stereotype"):
                opp_val = getattr(old_value, "pivot_Stereotype", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Stereotype", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Stereotype"):
                opp_val = getattr(value, "pivot_Stereotype", None)
                setattr(value, "pivot_Stereotype", self)

    @property
    def extension(self):
        return self.__extension

    @extension.setter
    def extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ElementExtension__extension", None)
        self.__extension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element"):
                opp_val = getattr(old_value, "Element", None)
                if opp_val == self:
                    setattr(old_value, "Element", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element"):
                opp_val = getattr(value, "Element", None)
                setattr(value, "Element", self)

class pivot_TemplateParameterType(Type):

    def __init__(self, specification: str):
        self.specification = specification
        
    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

class pivot_DynamicType(Type, DynamicElement):

    pass
class pivot_Class(Namespace, Type):

    def __init__(self, isAbstract: str, isActive: str, isInterface: str, pivot_Class: "pivot_Class" = None, pivot_Class11: set["pivot_Class"] = None, pivot_Class14: set["pivot_Behavior"] = None, pivot_Class150: "pivot_Operation" = None, pivot_Class197: "pivot_Property" = None):
        self.isAbstract = isAbstract
        self.isActive = isActive
        self.isInterface = isInterface
        self.pivot_Class = pivot_Class
        self.pivot_Class11 = pivot_Class11 if pivot_Class11 is not None else set()
        self.pivot_Class14 = pivot_Class14 if pivot_Class14 is not None else set()
        self.pivot_Class150 = pivot_Class150
        self.pivot_Class197 = pivot_Class197
        
    @property
    def isActive(self) -> str:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: str):
        self.__isActive = isActive

    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def isInterface(self) -> str:
        return self.__isInterface

    @isInterface.setter
    def isInterface(self, isInterface: str):
        self.__isInterface = isInterface

    @property
    def pivot_Class11(self):
        return self.__pivot_Class11

    @pivot_Class11.setter
    def pivot_Class11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__pivot_Class11", None)
        self.__pivot_Class11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Class"):
                    opp_val = getattr(item, "pivot_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Class"):
                    opp_val = getattr(item, "pivot_Class", None)
                    
                    setattr(item, "pivot_Class", self)
                    

    @property
    def pivot_Class(self):
        return self.__pivot_Class

    @pivot_Class.setter
    def pivot_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__pivot_Class", None)
        self.__pivot_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Class11"):
                opp_val = getattr(old_value, "pivot_Class11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Class11"):
                opp_val = getattr(value, "pivot_Class11", None)
                if opp_val is None:
                    setattr(value, "pivot_Class11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Class197(self):
        return self.__pivot_Class197

    @pivot_Class197.setter
    def pivot_Class197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__pivot_Class197", None)
        self.__pivot_Class197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property196"):
                opp_val = getattr(old_value, "pivot_Property196", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property196"):
                opp_val = getattr(value, "pivot_Property196", None)
                setattr(value, "pivot_Property196", self)

    @property
    def pivot_Class150(self):
        return self.__pivot_Class150

    @pivot_Class150.setter
    def pivot_Class150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__pivot_Class150", None)
        self.__pivot_Class150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation149"):
                opp_val = getattr(old_value, "pivot_Operation149", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Operation149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation149"):
                opp_val = getattr(value, "pivot_Operation149", None)
                setattr(value, "pivot_Operation149", self)

    @property
    def pivot_Class14(self):
        return self.__pivot_Class14

    @pivot_Class14.setter
    def pivot_Class14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__pivot_Class14", None)
        self.__pivot_Class14 = value if value is not None else set()
        
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
                    

class pivot_Operation(TemplateableElement, Feature, ParameterableElement, Namespace):

    def __init__(self, isInvalidating: str, isValidating: str, pivot_Operation: "pivot_CallOperationAction" = None, pivot_Operation129: "pivot_MessageType" = None, pivot_Operation146: "pivot_OpaqueExpression" = None, pivot_Operation149: "pivot_Class" = None, operation: set["pivot_Parameter"] = None, ownedOperation: "pivot_Type" = None, pivot_Operation154: set["pivot_Constraint"] = None, pivot_Operation157: "pivot_Precedence" = None, pivot_Operation160: set["pivot_Constraint"] = None, pivot_Operation163: set["pivot_Type"] = None, pivot_Operation167: "pivot_Operation" = None, pivot_Operation165: set["pivot_Operation"] = None, pivot_Operation172: "pivot_OperationCallExp" = None, Operation: "pivot_Parameter" = None, Operation339: "pivot_Type" = None):
        self.isInvalidating = isInvalidating
        self.isValidating = isValidating
        self.pivot_Operation = pivot_Operation
        self.pivot_Operation129 = pivot_Operation129
        self.pivot_Operation146 = pivot_Operation146
        self.pivot_Operation149 = pivot_Operation149
        self.operation = operation if operation is not None else set()
        self.ownedOperation = ownedOperation
        self.pivot_Operation154 = pivot_Operation154 if pivot_Operation154 is not None else set()
        self.pivot_Operation157 = pivot_Operation157
        self.pivot_Operation160 = pivot_Operation160 if pivot_Operation160 is not None else set()
        self.pivot_Operation163 = pivot_Operation163 if pivot_Operation163 is not None else set()
        self.pivot_Operation167 = pivot_Operation167
        self.pivot_Operation165 = pivot_Operation165 if pivot_Operation165 is not None else set()
        self.pivot_Operation172 = pivot_Operation172
        self.Operation = Operation
        self.Operation339 = Operation339
        
    @property
    def isInvalidating(self) -> str:
        return self.__isInvalidating

    @isInvalidating.setter
    def isInvalidating(self, isInvalidating: str):
        self.__isInvalidating = isInvalidating

    @property
    def isValidating(self) -> str:
        return self.__isValidating

    @isValidating.setter
    def isValidating(self, isValidating: str):
        self.__isValidating = isValidating

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
    def pivot_Operation160(self):
        return self.__pivot_Operation160

    @pivot_Operation160.setter
    def pivot_Operation160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation160", None)
        self.__pivot_Operation160 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Constraint161"):
                    opp_val = getattr(item, "pivot_Constraint161", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Constraint161", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Constraint161"):
                    opp_val = getattr(item, "pivot_Constraint161", None)
                    
                    setattr(item, "pivot_Constraint161", self)
                    

    @property
    def pivot_Operation163(self):
        return self.__pivot_Operation163

    @pivot_Operation163.setter
    def pivot_Operation163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation163", None)
        self.__pivot_Operation163 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Type164"):
                    opp_val = getattr(item, "pivot_Type164", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Type164", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Type164"):
                    opp_val = getattr(item, "pivot_Type164", None)
                    
                    setattr(item, "pivot_Type164", self)
                    

    @property
    def pivot_Operation165(self):
        return self.__pivot_Operation165

    @pivot_Operation165.setter
    def pivot_Operation165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation165", None)
        self.__pivot_Operation165 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Operation167"):
                    opp_val = getattr(item, "pivot_Operation167", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Operation167", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Operation167"):
                    opp_val = getattr(item, "pivot_Operation167", None)
                    
                    setattr(item, "pivot_Operation167", self)
                    

    @property
    def pivot_Operation167(self):
        return self.__pivot_Operation167

    @pivot_Operation167.setter
    def pivot_Operation167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation167", None)
        self.__pivot_Operation167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation165"):
                opp_val = getattr(old_value, "pivot_Operation165", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation165"):
                opp_val = getattr(value, "pivot_Operation165", None)
                if opp_val is None:
                    setattr(value, "pivot_Operation165", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Operation157(self):
        return self.__pivot_Operation157

    @pivot_Operation157.setter
    def pivot_Operation157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation157", None)
        self.__pivot_Operation157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Precedence158"):
                opp_val = getattr(old_value, "pivot_Precedence158", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Precedence158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Precedence158"):
                opp_val = getattr(value, "pivot_Precedence158", None)
                setattr(value, "pivot_Precedence158", self)

    @property
    def pivot_Operation129(self):
        return self.__pivot_Operation129

    @pivot_Operation129.setter
    def pivot_Operation129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation129", None)
        self.__pivot_Operation129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_MessageType"):
                opp_val = getattr(old_value, "pivot_MessageType", None)
                if opp_val == self:
                    setattr(old_value, "pivot_MessageType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_MessageType"):
                opp_val = getattr(value, "pivot_MessageType", None)
                setattr(value, "pivot_MessageType", self)

    @property
    def pivot_Operation154(self):
        return self.__pivot_Operation154

    @pivot_Operation154.setter
    def pivot_Operation154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation154", None)
        self.__pivot_Operation154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Constraint155"):
                    opp_val = getattr(item, "pivot_Constraint155", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Constraint155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Constraint155"):
                    opp_val = getattr(item, "pivot_Constraint155", None)
                    
                    setattr(item, "pivot_Constraint155", self)
                    

    @property
    def pivot_Operation149(self):
        return self.__pivot_Operation149

    @pivot_Operation149.setter
    def pivot_Operation149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation149", None)
        self.__pivot_Operation149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Class150"):
                opp_val = getattr(old_value, "pivot_Class150", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Class150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Class150"):
                opp_val = getattr(value, "pivot_Class150", None)
                setattr(value, "pivot_Class150", self)

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

    @property
    def pivot_Operation172(self):
        return self.__pivot_Operation172

    @pivot_Operation172.setter
    def pivot_Operation172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation172", None)
        self.__pivot_Operation172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OperationCallExp171"):
                opp_val = getattr(old_value, "pivot_OperationCallExp171", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OperationCallExp171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OperationCallExp171"):
                opp_val = getattr(value, "pivot_OperationCallExp171", None)
                setattr(value, "pivot_OperationCallExp171", self)

    @property
    def Operation339(self):
        return self.__Operation339

    @Operation339.setter
    def Operation339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__Operation339", None)
        self.__Operation339 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningType338"):
                opp_val = getattr(old_value, "owningType338", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningType338"):
                opp_val = getattr(value, "owningType338", None)
                if opp_val is None:
                    setattr(value, "owningType338", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Operation146(self):
        return self.__pivot_Operation146

    @pivot_Operation146.setter
    def pivot_Operation146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation146", None)
        self.__pivot_Operation146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OpaqueExpression147"):
                opp_val = getattr(old_value, "pivot_OpaqueExpression147", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OpaqueExpression147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OpaqueExpression147"):
                opp_val = getattr(value, "pivot_OpaqueExpression147", None)
                setattr(value, "pivot_OpaqueExpression147", self)

    def CompatibleReturn(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CompatibleReturn method
        pass

    def LoadableImplementation(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement LoadableImplementation method
        pass

    def UniquePostconditionName(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement UniquePostconditionName method
        pass

    def UniquePreconditionName(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement UniquePreconditionName method
        pass

class pivot_OCLExpression(TypedElement):

    pass
class OCLExpression:

    pass
class pivot_IfExp(OCLExpression):

    def __init__(self, pivot_IfExp83: "pivot_OCLExpression" = None, pivot_IfExp: "pivot_OCLExpression" = None, pivot_IfExp86: "pivot_OCLExpression" = None):
        self.pivot_IfExp83 = pivot_IfExp83
        self.pivot_IfExp = pivot_IfExp
        self.pivot_IfExp86 = pivot_IfExp86
        
    @property
    def pivot_IfExp83(self):
        return self.__pivot_IfExp83

    @pivot_IfExp83.setter
    def pivot_IfExp83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_IfExp__pivot_IfExp83", None)
        self.__pivot_IfExp83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OCLExpression84"):
                opp_val = getattr(old_value, "pivot_OCLExpression84", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression84"):
                opp_val = getattr(value, "pivot_OCLExpression84", None)
                setattr(value, "pivot_OCLExpression84", self)

    @property
    def pivot_IfExp86(self):
        return self.__pivot_IfExp86

    @pivot_IfExp86.setter
    def pivot_IfExp86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_IfExp__pivot_IfExp86", None)
        self.__pivot_IfExp86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OCLExpression87"):
                opp_val = getattr(old_value, "pivot_OCLExpression87", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression87"):
                opp_val = getattr(value, "pivot_OCLExpression87", None)
                setattr(value, "pivot_OCLExpression87", self)

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
            if hasattr(old_value, "pivot_OCLExpression81"):
                opp_val = getattr(old_value, "pivot_OCLExpression81", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression81"):
                opp_val = getattr(value, "pivot_OCLExpression81", None)
                setattr(value, "pivot_OCLExpression81", self)

    def ConditionTypeIsBoolean(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ConditionTypeIsBoolean method
        pass

class pivot_TypeExp(OCLExpression, ReferringElement):

    pass
class pivot_LetExp(OCLExpression):

    def __init__(self, pivot_LetExp107: "pivot_Variable" = None, pivot_LetExp: "pivot_OCLExpression" = None):
        self.pivot_LetExp107 = pivot_LetExp107
        self.pivot_LetExp = pivot_LetExp
        
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
            if hasattr(old_value, "pivot_OCLExpression105"):
                opp_val = getattr(old_value, "pivot_OCLExpression105", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression105"):
                opp_val = getattr(value, "pivot_OCLExpression105", None)
                setattr(value, "pivot_OCLExpression105", self)

    @property
    def pivot_LetExp107(self):
        return self.__pivot_LetExp107

    @pivot_LetExp107.setter
    def pivot_LetExp107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_LetExp__pivot_LetExp107", None)
        self.__pivot_LetExp107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Variable108"):
                opp_val = getattr(old_value, "pivot_Variable108", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Variable108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Variable108"):
                opp_val = getattr(value, "pivot_Variable108", None)
                setattr(value, "pivot_Variable108", self)

    def TypeIsInType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement TypeIsInType method
        pass

class pivot_LiteralExp(OCLExpression):

    pass
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

class pivot_UnspecifiedValueExp(OCLExpression):

    pass
class pivot_MessageExp(OCLExpression):

    def __init__(self, pivot_MessageExp: set["pivot_OCLExpression"] = None, pivot_MessageExp121: "pivot_CallOperationAction" = None, pivot_MessageExp124: "pivot_SendSignalAction" = None, pivot_MessageExp126: "pivot_OCLExpression" = None):
        self.pivot_MessageExp = pivot_MessageExp if pivot_MessageExp is not None else set()
        self.pivot_MessageExp121 = pivot_MessageExp121
        self.pivot_MessageExp124 = pivot_MessageExp124
        self.pivot_MessageExp126 = pivot_MessageExp126
        
    @property
    def pivot_MessageExp126(self):
        return self.__pivot_MessageExp126

    @pivot_MessageExp126.setter
    def pivot_MessageExp126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_MessageExp__pivot_MessageExp126", None)
        self.__pivot_MessageExp126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OCLExpression127"):
                opp_val = getattr(old_value, "pivot_OCLExpression127", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression127"):
                opp_val = getattr(value, "pivot_OCLExpression127", None)
                setattr(value, "pivot_OCLExpression127", self)

    @property
    def pivot_MessageExp124(self):
        return self.__pivot_MessageExp124

    @pivot_MessageExp124.setter
    def pivot_MessageExp124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_MessageExp__pivot_MessageExp124", None)
        self.__pivot_MessageExp124 = value
        
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
    def pivot_MessageExp121(self):
        return self.__pivot_MessageExp121

    @pivot_MessageExp121.setter
    def pivot_MessageExp121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_MessageExp__pivot_MessageExp121", None)
        self.__pivot_MessageExp121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_CallOperationAction122"):
                opp_val = getattr(old_value, "pivot_CallOperationAction122", None)
                if opp_val == self:
                    setattr(old_value, "pivot_CallOperationAction122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_CallOperationAction122"):
                opp_val = getattr(value, "pivot_CallOperationAction122", None)
                setattr(value, "pivot_CallOperationAction122", self)

    @property
    def pivot_MessageExp(self):
        return self.__pivot_MessageExp

    @pivot_MessageExp.setter
    def pivot_MessageExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_MessageExp__pivot_MessageExp", None)
        self.__pivot_MessageExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_OCLExpression119"):
                    opp_val = getattr(item, "pivot_OCLExpression119", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_OCLExpression119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_OCLExpression119"):
                    opp_val = getattr(item, "pivot_OCLExpression119", None)
                    
                    setattr(item, "pivot_OCLExpression119", self)
                    

    def TargetIsNotACollection(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement TargetIsNotACollection method
        pass

    def OneCallOrOneSend(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement OneCallOrOneSend method
        pass

class pivot_StateExp(OCLExpression):

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

    def TypeIsBoolean(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement TypeIsBoolean method
        pass

class pivot_Transition(Namespace):

    def __init__(self, kind: str, Transition: "pivot_Behavior" = None, Transition43: "pivot_Constraint" = None, Transition233: "pivot_Region" = None, outgoing: "pivot_Vertex" = None, transition: "pivot_Region" = None, transition311: "pivot_Behavior" = None, transition313: "pivot_Constraint" = None, incoming: "pivot_Vertex" = None, transition320: set["pivot_Trigger"] = None, Transition325: "pivot_Trigger" = None, Transition369: "pivot_Vertex" = None, Transition371: "pivot_Vertex" = None):
        self.kind = kind
        self.Transition = Transition
        self.Transition43 = Transition43
        self.Transition233 = Transition233
        self.outgoing = outgoing
        self.transition = transition
        self.transition311 = transition311
        self.transition313 = transition313
        self.incoming = incoming
        self.transition320 = transition320 if transition320 is not None else set()
        self.Transition325 = Transition325
        self.Transition369 = Transition369
        self.Transition371 = Transition371
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def Transition371(self):
        return self.__Transition371

    @Transition371.setter
    def Transition371(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__Transition371", None)
        self.__Transition371 = value
        
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
    def Transition233(self):
        return self.__Transition233

    @Transition233.setter
    def Transition233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__Transition233", None)
        self.__Transition233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container232"):
                opp_val = getattr(old_value, "container232", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container232"):
                opp_val = getattr(value, "container232", None)
                if opp_val is None:
                    setattr(value, "container232", set([self]))
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
            if hasattr(old_value, "Region309"):
                opp_val = getattr(old_value, "Region309", None)
                if opp_val == self:
                    setattr(old_value, "Region309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Region309"):
                opp_val = getattr(value, "Region309", None)
                setattr(value, "Region309", self)

    @property
    def transition311(self):
        return self.__transition311

    @transition311.setter
    def transition311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__transition311", None)
        self.__transition311 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behavior"):
                opp_val = getattr(old_value, "Behavior", None)
                if opp_val == self:
                    setattr(old_value, "Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behavior"):
                opp_val = getattr(value, "Behavior", None)
                setattr(value, "Behavior", self)

    @property
    def Transition325(self):
        return self.__Transition325

    @Transition325.setter
    def Transition325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__Transition325", None)
        self.__Transition325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trigger"):
                opp_val = getattr(old_value, "trigger", None)
                if opp_val == self:
                    setattr(old_value, "trigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trigger"):
                opp_val = getattr(value, "trigger", None)
                setattr(value, "trigger", self)

    @property
    def Transition43(self):
        return self.__Transition43

    @Transition43.setter
    def Transition43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__Transition43", None)
        self.__Transition43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "guard"):
                opp_val = getattr(old_value, "guard", None)
                if opp_val == self:
                    setattr(old_value, "guard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "guard"):
                opp_val = getattr(value, "guard", None)
                setattr(value, "guard", self)

    @property
    def transition313(self):
        return self.__transition313

    @transition313.setter
    def transition313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__transition313", None)
        self.__transition313 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Constraint314"):
                opp_val = getattr(old_value, "Constraint314", None)
                if opp_val == self:
                    setattr(old_value, "Constraint314", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Constraint314"):
                opp_val = getattr(value, "Constraint314", None)
                setattr(value, "Constraint314", self)

    @property
    def Transition369(self):
        return self.__Transition369

    @Transition369.setter
    def Transition369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__Transition369", None)
        self.__Transition369 = value
        
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
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effect"):
                opp_val = getattr(old_value, "effect", None)
                if opp_val == self:
                    setattr(old_value, "effect", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effect"):
                opp_val = getattr(value, "effect", None)
                setattr(value, "effect", self)

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
            if hasattr(old_value, "Vertex318"):
                opp_val = getattr(old_value, "Vertex318", None)
                if opp_val == self:
                    setattr(old_value, "Vertex318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex318"):
                opp_val = getattr(value, "Vertex318", None)
                setattr(value, "Vertex318", self)

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
            if hasattr(old_value, "Vertex316"):
                opp_val = getattr(old_value, "Vertex316", None)
                if opp_val == self:
                    setattr(old_value, "Vertex316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex316"):
                opp_val = getattr(value, "Vertex316", None)
                setattr(value, "Vertex316", self)

    @property
    def transition320(self):
        return self.__transition320

    @transition320.setter
    def transition320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__transition320", None)
        self.__transition320 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Trigger321"):
                    opp_val = getattr(item, "Trigger321", None)
                    
                    if opp_val == self:
                        setattr(item, "Trigger321", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trigger321"):
                    opp_val = getattr(item, "Trigger321", None)
                    
                    setattr(item, "Trigger321", self)
                    

class CollectionType:

    pass
class pivot_OrderedSetType(CollectionType):

    pass
class pivot_SetType(CollectionType):

    pass
class pivot_SequenceType(CollectionType):

    pass
class pivot_BagType(CollectionType):

    pass
class LiteralExp:

    pass
class pivot_InvalidLiteralExp(LiteralExp):

    pass
class pivot_TupleLiteralExp(LiteralExp):

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
                    

    def SetKindIsSet(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SetKindIsSet method
        pass

    def CollectionKindIsConcrete(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement CollectionKindIsConcrete method
        pass

    def SequenceKindIsSequence(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SequenceKindIsSequence method
        pass

    def OrderedSetKindIsOrderedSet(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OrderedSetKindIsOrderedSet method
        pass

    def BagKindIsBag(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BagKindIsBag method
        pass

class pivot_Element(Visitable):

    def __init__(self, pivot_Element5: "pivot_Annotation" = None, pivot_Element: "pivot_Annotation" = None, pivot_Element25: "pivot_Comment" = None, pivot_Element32: "pivot_Constraint" = None, base: set["pivot_ElementExtension"] = None, pivot_Element61: "pivot_Element" = None, pivot_Element59: set["pivot_Element"] = None, pivot_Element63: set["pivot_Comment"] = None, Element: "pivot_ElementExtension" = None):
        self.pivot_Element5 = pivot_Element5
        self.pivot_Element = pivot_Element
        self.pivot_Element25 = pivot_Element25
        self.pivot_Element32 = pivot_Element32
        self.base = base if base is not None else set()
        self.pivot_Element61 = pivot_Element61
        self.pivot_Element59 = pivot_Element59 if pivot_Element59 is not None else set()
        self.pivot_Element63 = pivot_Element63 if pivot_Element63 is not None else set()
        self.Element = Element
        
    @property
    def pivot_Element63(self):
        return self.__pivot_Element63

    @pivot_Element63.setter
    def pivot_Element63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Element__pivot_Element63", None)
        self.__pivot_Element63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Comment64"):
                    opp_val = getattr(item, "pivot_Comment64", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Comment64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Comment64"):
                    opp_val = getattr(item, "pivot_Comment64", None)
                    
                    setattr(item, "pivot_Comment64", self)
                    

    @property
    def pivot_Element59(self):
        return self.__pivot_Element59

    @pivot_Element59.setter
    def pivot_Element59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Element__pivot_Element59", None)
        self.__pivot_Element59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Element61"):
                    opp_val = getattr(item, "pivot_Element61", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Element61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Element61"):
                    opp_val = getattr(item, "pivot_Element61", None)
                    
                    setattr(item, "pivot_Element61", self)
                    

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
    def pivot_Element25(self):
        return self.__pivot_Element25

    @pivot_Element25.setter
    def pivot_Element25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Element__pivot_Element25", None)
        self.__pivot_Element25 = value
        
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

    @property
    def pivot_Element61(self):
        return self.__pivot_Element61

    @pivot_Element61.setter
    def pivot_Element61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Element__pivot_Element61", None)
        self.__pivot_Element61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Element59"):
                opp_val = getattr(old_value, "pivot_Element59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Element59"):
                opp_val = getattr(value, "pivot_Element59", None)
                if opp_val is None:
                    setattr(value, "pivot_Element59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def pivot_Element32(self):
        return self.__pivot_Element32

    @pivot_Element32.setter
    def pivot_Element32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Element__pivot_Element32", None)
        self.__pivot_Element32 = value
        
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

    def getValue(self, stereotype: Type, propertyName: str) -> Element:
        # TODO: Implement getValue method
        pass

    def allOwnedElements(self) -> Element:
        # TODO: Implement allOwnedElements method
        pass

class NamedElement:

    pass
class pivot_Import(NamedElement):

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

class pivot_Constraint(NamedElement):

    def __init__(self, isCallable: str, pivot_Constraint: set["pivot_Element"] = None, pivot_Constraint34: "pivot_Namespace" = None, guard: "pivot_Transition" = None, stateInvariant: "pivot_State" = None, pivot_Constraint39: "pivot_Constraint" = None, pivot_Constraint37: set["pivot_Constraint"] = None, pivot_Constraint41: "pivot_OpaqueExpression" = None, pivot_Constraint136: "pivot_Namespace" = None, pivot_Constraint155: "pivot_Operation" = None, pivot_Constraint161: "pivot_Operation" = None, Constraint: "pivot_State" = None, Constraint314: "pivot_Transition" = None, pivot_Constraint336: "pivot_Type" = None):
        self.isCallable = isCallable
        self.pivot_Constraint = pivot_Constraint if pivot_Constraint is not None else set()
        self.pivot_Constraint34 = pivot_Constraint34
        self.guard = guard
        self.stateInvariant = stateInvariant
        self.pivot_Constraint39 = pivot_Constraint39
        self.pivot_Constraint37 = pivot_Constraint37 if pivot_Constraint37 is not None else set()
        self.pivot_Constraint41 = pivot_Constraint41
        self.pivot_Constraint136 = pivot_Constraint136
        self.pivot_Constraint155 = pivot_Constraint155
        self.pivot_Constraint161 = pivot_Constraint161
        self.Constraint = Constraint
        self.Constraint314 = Constraint314
        self.pivot_Constraint336 = pivot_Constraint336
        
    @property
    def isCallable(self) -> str:
        return self.__isCallable

    @isCallable.setter
    def isCallable(self, isCallable: str):
        self.__isCallable = isCallable

    @property
    def pivot_Constraint336(self):
        return self.__pivot_Constraint336

    @pivot_Constraint336.setter
    def pivot_Constraint336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint336", None)
        self.__pivot_Constraint336 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Type335"):
                opp_val = getattr(old_value, "pivot_Type335", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Type335"):
                opp_val = getattr(value, "pivot_Type335", None)
                if opp_val is None:
                    setattr(value, "pivot_Type335", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stateInvariant(self):
        return self.__stateInvariant

    @stateInvariant.setter
    def stateInvariant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__stateInvariant", None)
        self.__stateInvariant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State36"):
                opp_val = getattr(old_value, "State36", None)
                if opp_val == self:
                    setattr(old_value, "State36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State36"):
                opp_val = getattr(value, "State36", None)
                setattr(value, "State36", self)

    @property
    def pivot_Constraint34(self):
        return self.__pivot_Constraint34

    @pivot_Constraint34.setter
    def pivot_Constraint34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint34", None)
        self.__pivot_Constraint34 = value
        
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
    def pivot_Constraint39(self):
        return self.__pivot_Constraint39

    @pivot_Constraint39.setter
    def pivot_Constraint39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint39", None)
        self.__pivot_Constraint39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Constraint37"):
                opp_val = getattr(old_value, "pivot_Constraint37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Constraint37"):
                opp_val = getattr(value, "pivot_Constraint37", None)
                if opp_val is None:
                    setattr(value, "pivot_Constraint37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Constraint37(self):
        return self.__pivot_Constraint37

    @pivot_Constraint37.setter
    def pivot_Constraint37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint37", None)
        self.__pivot_Constraint37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Constraint39"):
                    opp_val = getattr(item, "pivot_Constraint39", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Constraint39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Constraint39"):
                    opp_val = getattr(item, "pivot_Constraint39", None)
                    
                    setattr(item, "pivot_Constraint39", self)
                    

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
                if hasattr(item, "pivot_Element32"):
                    opp_val = getattr(item, "pivot_Element32", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Element32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Element32"):
                    opp_val = getattr(item, "pivot_Element32", None)
                    
                    setattr(item, "pivot_Element32", self)
                    

    @property
    def Constraint(self):
        return self.__Constraint

    @Constraint.setter
    def Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__Constraint", None)
        self.__Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningState"):
                opp_val = getattr(old_value, "owningState", None)
                if opp_val == self:
                    setattr(old_value, "owningState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningState"):
                opp_val = getattr(value, "owningState", None)
                setattr(value, "owningState", self)

    @property
    def Constraint314(self):
        return self.__Constraint314

    @Constraint314.setter
    def Constraint314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__Constraint314", None)
        self.__Constraint314 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transition313"):
                opp_val = getattr(old_value, "transition313", None)
                if opp_val == self:
                    setattr(old_value, "transition313", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transition313"):
                opp_val = getattr(value, "transition313", None)
                setattr(value, "transition313", self)

    @property
    def pivot_Constraint161(self):
        return self.__pivot_Constraint161

    @pivot_Constraint161.setter
    def pivot_Constraint161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint161", None)
        self.__pivot_Constraint161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation160"):
                opp_val = getattr(old_value, "pivot_Operation160", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation160"):
                opp_val = getattr(value, "pivot_Operation160", None)
                if opp_val is None:
                    setattr(value, "pivot_Operation160", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Constraint41(self):
        return self.__pivot_Constraint41

    @pivot_Constraint41.setter
    def pivot_Constraint41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint41", None)
        self.__pivot_Constraint41 = value
        
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

    @property
    def pivot_Constraint136(self):
        return self.__pivot_Constraint136

    @pivot_Constraint136.setter
    def pivot_Constraint136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint136", None)
        self.__pivot_Constraint136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Namespace135"):
                opp_val = getattr(old_value, "pivot_Namespace135", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Namespace135"):
                opp_val = getattr(value, "pivot_Namespace135", None)
                if opp_val is None:
                    setattr(value, "pivot_Namespace135", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def guard(self):
        return self.__guard

    @guard.setter
    def guard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__guard", None)
        self.__guard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition43"):
                opp_val = getattr(old_value, "Transition43", None)
                if opp_val == self:
                    setattr(old_value, "Transition43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition43"):
                opp_val = getattr(value, "Transition43", None)
                setattr(value, "Transition43", self)

    @property
    def pivot_Constraint155(self):
        return self.__pivot_Constraint155

    @pivot_Constraint155.setter
    def pivot_Constraint155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint155", None)
        self.__pivot_Constraint155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation154"):
                opp_val = getattr(old_value, "pivot_Operation154", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation154"):
                opp_val = getattr(value, "pivot_Operation154", None)
                if opp_val is None:
                    setattr(value, "pivot_Operation154", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def UniqueName(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement UniqueName method
        pass

class pivot_SendSignalAction(NamedElement):

    pass
class pivot_Signal(NamedElement):

    pass
class pivot_Trigger(NamedElement):

    pass
class pivot_Type(TemplateableElement, NamedElement, ParameterableElement):

    def __init__(self, instanceClassName: str, pivot_Type: "pivot_CollectionType" = None, pivot_Type51: "pivot_DataType" = None, pivot_Type53: "pivot_DynamicElement" = None, pivot_Type97: "pivot_LambdaType" = None, pivot_Type100: "pivot_LambdaType" = None, pivot_Type103: "pivot_LambdaType" = None, pivot_Type133: "pivot_Metaclass" = None, Type: "pivot_Operation" = None, pivot_Type164: "pivot_Operation" = None, Type183: "pivot_Package" = None, Type208: "pivot_Property" = None, owningType: set["pivot_Property"] = None, type: set["pivot_TypeExtension"] = None, pivot_Type335: set["pivot_Constraint"] = None, owningType338: set["pivot_Operation"] = None, ownedType: "pivot_Package" = None, pivot_Type344: "pivot_Type" = None, pivot_Type342: set["pivot_Type"] = None, pivot_Type346: "pivot_TypeExp" = None, Type349: "pivot_TypeExtension" = None, pivot_Type351: "pivot_TypeTemplateParameter" = None, pivot_Type353: "pivot_TypedElement" = None, pivot_Type355: "pivot_UnspecifiedType" = None, pivot_Type358: "pivot_UnspecifiedType" = None):
        self.instanceClassName = instanceClassName
        self.pivot_Type = pivot_Type
        self.pivot_Type51 = pivot_Type51
        self.pivot_Type53 = pivot_Type53
        self.pivot_Type97 = pivot_Type97
        self.pivot_Type100 = pivot_Type100
        self.pivot_Type103 = pivot_Type103
        self.pivot_Type133 = pivot_Type133
        self.Type = Type
        self.pivot_Type164 = pivot_Type164
        self.Type183 = Type183
        self.Type208 = Type208
        self.owningType = owningType if owningType is not None else set()
        self.type = type if type is not None else set()
        self.pivot_Type335 = pivot_Type335 if pivot_Type335 is not None else set()
        self.owningType338 = owningType338 if owningType338 is not None else set()
        self.ownedType = ownedType
        self.pivot_Type344 = pivot_Type344
        self.pivot_Type342 = pivot_Type342 if pivot_Type342 is not None else set()
        self.pivot_Type346 = pivot_Type346
        self.Type349 = Type349
        self.pivot_Type351 = pivot_Type351
        self.pivot_Type353 = pivot_Type353
        self.pivot_Type355 = pivot_Type355
        self.pivot_Type358 = pivot_Type358
        
    @property
    def instanceClassName(self) -> str:
        return self.__instanceClassName

    @instanceClassName.setter
    def instanceClassName(self, instanceClassName: str):
        self.__instanceClassName = instanceClassName

    @property
    def pivot_Type342(self):
        return self.__pivot_Type342

    @pivot_Type342.setter
    def pivot_Type342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type342", None)
        self.__pivot_Type342 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Type344"):
                    opp_val = getattr(item, "pivot_Type344", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Type344", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Type344"):
                    opp_val = getattr(item, "pivot_Type344", None)
                    
                    setattr(item, "pivot_Type344", self)
                    

    @property
    def owningType338(self):
        return self.__owningType338

    @owningType338.setter
    def owningType338(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__owningType338", None)
        self.__owningType338 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation339"):
                    opp_val = getattr(item, "Operation339", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation339", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation339"):
                    opp_val = getattr(item, "Operation339", None)
                    
                    setattr(item, "Operation339", self)
                    

    @property
    def pivot_Type351(self):
        return self.__pivot_Type351

    @pivot_Type351.setter
    def pivot_Type351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type351", None)
        self.__pivot_Type351 = value
        
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
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__type", None)
        self.__type = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeExtension331"):
                    opp_val = getattr(item, "TypeExtension331", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeExtension331", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeExtension331"):
                    opp_val = getattr(item, "TypeExtension331", None)
                    
                    setattr(item, "TypeExtension331", self)
                    

    @property
    def pivot_Type346(self):
        return self.__pivot_Type346

    @pivot_Type346.setter
    def pivot_Type346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type346", None)
        self.__pivot_Type346 = value
        
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
                if hasattr(item, "Property333"):
                    opp_val = getattr(item, "Property333", None)
                    
                    if opp_val == self:
                        setattr(item, "Property333", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property333"):
                    opp_val = getattr(item, "Property333", None)
                    
                    setattr(item, "Property333", self)
                    

    @property
    def Type183(self):
        return self.__Type183

    @Type183.setter
    def Type183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__Type183", None)
        self.__Type183 = value
        
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
    def pivot_Type358(self):
        return self.__pivot_Type358

    @pivot_Type358.setter
    def pivot_Type358(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type358", None)
        self.__pivot_Type358 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_UnspecifiedType357"):
                opp_val = getattr(old_value, "pivot_UnspecifiedType357", None)
                if opp_val == self:
                    setattr(old_value, "pivot_UnspecifiedType357", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_UnspecifiedType357"):
                opp_val = getattr(value, "pivot_UnspecifiedType357", None)
                setattr(value, "pivot_UnspecifiedType357", self)

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
    def Type349(self):
        return self.__Type349

    @Type349.setter
    def Type349(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__Type349", None)
        self.__Type349 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedBys"):
                opp_val = getattr(old_value, "extendedBys", None)
                if opp_val == self:
                    setattr(old_value, "extendedBys", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedBys"):
                opp_val = getattr(value, "extendedBys", None)
                setattr(value, "extendedBys", self)

    @property
    def pivot_Type355(self):
        return self.__pivot_Type355

    @pivot_Type355.setter
    def pivot_Type355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type355", None)
        self.__pivot_Type355 = value
        
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
    def pivot_Type335(self):
        return self.__pivot_Type335

    @pivot_Type335.setter
    def pivot_Type335(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type335", None)
        self.__pivot_Type335 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Constraint336"):
                    opp_val = getattr(item, "pivot_Constraint336", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Constraint336", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Constraint336"):
                    opp_val = getattr(item, "pivot_Constraint336", None)
                    
                    setattr(item, "pivot_Constraint336", self)
                    

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
    def pivot_Type353(self):
        return self.__pivot_Type353

    @pivot_Type353.setter
    def pivot_Type353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type353", None)
        self.__pivot_Type353 = value
        
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
    def pivot_Type344(self):
        return self.__pivot_Type344

    @pivot_Type344.setter
    def pivot_Type344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type344", None)
        self.__pivot_Type344 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Type342"):
                opp_val = getattr(old_value, "pivot_Type342", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Type342"):
                opp_val = getattr(value, "pivot_Type342", None)
                if opp_val is None:
                    setattr(value, "pivot_Type342", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Type103(self):
        return self.__pivot_Type103

    @pivot_Type103.setter
    def pivot_Type103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type103", None)
        self.__pivot_Type103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_LambdaType102"):
                opp_val = getattr(old_value, "pivot_LambdaType102", None)
                if opp_val == self:
                    setattr(old_value, "pivot_LambdaType102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_LambdaType102"):
                opp_val = getattr(value, "pivot_LambdaType102", None)
                setattr(value, "pivot_LambdaType102", self)

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
            if hasattr(old_value, "Package341"):
                opp_val = getattr(old_value, "Package341", None)
                if opp_val == self:
                    setattr(old_value, "Package341", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package341"):
                opp_val = getattr(value, "Package341", None)
                setattr(value, "Package341", self)

    @property
    def pivot_Type100(self):
        return self.__pivot_Type100

    @pivot_Type100.setter
    def pivot_Type100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type100", None)
        self.__pivot_Type100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_LambdaType99"):
                opp_val = getattr(old_value, "pivot_LambdaType99", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_LambdaType99"):
                opp_val = getattr(value, "pivot_LambdaType99", None)
                if opp_val is None:
                    setattr(value, "pivot_LambdaType99", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Type164(self):
        return self.__pivot_Type164

    @pivot_Type164.setter
    def pivot_Type164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type164", None)
        self.__pivot_Type164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation163"):
                opp_val = getattr(old_value, "pivot_Operation163", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation163"):
                opp_val = getattr(value, "pivot_Operation163", None)
                if opp_val is None:
                    setattr(value, "pivot_Operation163", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Type133(self):
        return self.__pivot_Type133

    @pivot_Type133.setter
    def pivot_Type133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type133", None)
        self.__pivot_Type133 = value
        
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
    def pivot_Type51(self):
        return self.__pivot_Type51

    @pivot_Type51.setter
    def pivot_Type51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type51", None)
        self.__pivot_Type51 = value
        
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
    def pivot_Type97(self):
        return self.__pivot_Type97

    @pivot_Type97.setter
    def pivot_Type97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type97", None)
        self.__pivot_Type97 = value
        
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
    def Type208(self):
        return self.__Type208

    @Type208.setter
    def Type208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__Type208", None)
        self.__Type208 = value
        
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

    def UniqueInvariantName(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement UniqueInvariantName method
        pass

    def specializeIn(self, expr: OCLExpression, selfType: Type) -> Type:
        # TODO: Implement specializeIn method
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

class pivot_CallOperationAction(NamedElement):

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
            if hasattr(old_value, "pivot_Type353"):
                opp_val = getattr(old_value, "pivot_Type353", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Type353", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Type353"):
                opp_val = getattr(value, "pivot_Type353", None)
                setattr(value, "pivot_Type353", self)

class pivot_Vertex(NamedElement):

    pass
class pivot_Namespace(NamedElement):

    pass
class pivot_Precedence(NamedElement):

    def __init__(self, associativity: str, order: str, pivot_Precedence: "pivot_Library" = None, pivot_Precedence158: "pivot_Operation" = None):
        self.associativity = associativity
        self.order = order
        self.pivot_Precedence = pivot_Precedence
        self.pivot_Precedence158 = pivot_Precedence158
        
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
    def pivot_Precedence158(self):
        return self.__pivot_Precedence158

    @pivot_Precedence158.setter
    def pivot_Precedence158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Precedence__pivot_Precedence158", None)
        self.__pivot_Precedence158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation157"):
                opp_val = getattr(old_value, "pivot_Operation157", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Operation157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation157"):
                opp_val = getattr(value, "pivot_Operation157", None)
                setattr(value, "pivot_Operation157", self)

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
class NavigationCallExp:

    pass
class pivot_OppositePropertyCallExp(NavigationCallExp):

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
            if hasattr(old_value, "pivot_Property219"):
                opp_val = getattr(old_value, "pivot_Property219", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property219"):
                opp_val = getattr(value, "pivot_Property219", None)
                setattr(value, "pivot_Property219", self)

    def getSpecializedReferredPropertyType(self) -> Type:
        # TODO: Implement getSpecializedReferredPropertyType method
        pass

    def getSpecializedReferredPropertyOwningType(self) -> Type:
        # TODO: Implement getSpecializedReferredPropertyOwningType method
        pass

    def NonStaticSourceTypeIsConformant(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NonStaticSourceTypeIsConformant method
        pass

    def CompatibleResultType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement CompatibleResultType method
        pass

class pivot_AssociationClassCallExp(NavigationCallExp):

    pass
class pivot_Property(Feature, ParameterableElement):

    def __init__(self, default: str, implicit: str, isComposite: str, isDerived: str, isID: str, isReadOnly: str, isResolveProxies: str, isTransient: str, isUnsettable: str, isVolatile: str, Property: "pivot_AssociationClass" = None, pivot_Property: "pivot_ConstructorPart" = None, pivot_Property55: "pivot_DynamicProperty" = None, pivot_Property138: "pivot_NavigationCallExp" = None, pivot_Property174: "pivot_OppositePropertyCallExp" = None, unownedAttribute: "pivot_AssociationClass" = None, pivot_Property196: "pivot_Class" = None, pivot_Property199: "pivot_OpaqueExpression" = None, pivot_Property203: "pivot_Property" = None, pivot_Property201: set["pivot_Property"] = None, pivot_Property204: "pivot_Property" = None, pivot_Property206: "pivot_Property" = None, ownedAttribute: "pivot_Type" = None, pivot_Property211: "pivot_Property" = None, pivot_Property209: set["pivot_Property"] = None, pivot_Property214: "pivot_Property" = None, pivot_Property212: "pivot_Property" = None, pivot_Property217: "pivot_Property" = None, pivot_Property215: set["pivot_Property"] = None, pivot_Property219: "pivot_PropertyCallExp" = None, Property333: "pivot_Type" = None):
        self.default = default
        self.implicit = implicit
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isID = isID
        self.isReadOnly = isReadOnly
        self.isResolveProxies = isResolveProxies
        self.isTransient = isTransient
        self.isUnsettable = isUnsettable
        self.isVolatile = isVolatile
        self.Property = Property
        self.pivot_Property = pivot_Property
        self.pivot_Property55 = pivot_Property55
        self.pivot_Property138 = pivot_Property138
        self.pivot_Property174 = pivot_Property174
        self.unownedAttribute = unownedAttribute
        self.pivot_Property196 = pivot_Property196
        self.pivot_Property199 = pivot_Property199
        self.pivot_Property203 = pivot_Property203
        self.pivot_Property201 = pivot_Property201 if pivot_Property201 is not None else set()
        self.pivot_Property204 = pivot_Property204
        self.pivot_Property206 = pivot_Property206
        self.ownedAttribute = ownedAttribute
        self.pivot_Property211 = pivot_Property211
        self.pivot_Property209 = pivot_Property209 if pivot_Property209 is not None else set()
        self.pivot_Property214 = pivot_Property214
        self.pivot_Property212 = pivot_Property212
        self.pivot_Property217 = pivot_Property217
        self.pivot_Property215 = pivot_Property215 if pivot_Property215 is not None else set()
        self.pivot_Property219 = pivot_Property219
        self.Property333 = Property333
        
    @property
    def implicit(self) -> str:
        return self.__implicit

    @implicit.setter
    def implicit(self, implicit: str):
        self.__implicit = implicit

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
    def isID(self) -> str:
        return self.__isID

    @isID.setter
    def isID(self, isID: str):
        self.__isID = isID

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
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def isResolveProxies(self) -> str:
        return self.__isResolveProxies

    @isResolveProxies.setter
    def isResolveProxies(self, isResolveProxies: str):
        self.__isResolveProxies = isResolveProxies

    @property
    def pivot_Property199(self):
        return self.__pivot_Property199

    @pivot_Property199.setter
    def pivot_Property199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property199", None)
        self.__pivot_Property199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OpaqueExpression200"):
                opp_val = getattr(old_value, "pivot_OpaqueExpression200", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OpaqueExpression200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OpaqueExpression200"):
                opp_val = getattr(value, "pivot_OpaqueExpression200", None)
                setattr(value, "pivot_OpaqueExpression200", self)

    @property
    def pivot_Property215(self):
        return self.__pivot_Property215

    @pivot_Property215.setter
    def pivot_Property215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property215", None)
        self.__pivot_Property215 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Property217"):
                    opp_val = getattr(item, "pivot_Property217", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Property217", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Property217"):
                    opp_val = getattr(item, "pivot_Property217", None)
                    
                    setattr(item, "pivot_Property217", self)
                    

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
            if hasattr(old_value, "pivot_ConstructorPart49"):
                opp_val = getattr(old_value, "pivot_ConstructorPart49", None)
                if opp_val == self:
                    setattr(old_value, "pivot_ConstructorPart49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ConstructorPart49"):
                opp_val = getattr(value, "pivot_ConstructorPart49", None)
                setattr(value, "pivot_ConstructorPart49", self)

    @property
    def pivot_Property201(self):
        return self.__pivot_Property201

    @pivot_Property201.setter
    def pivot_Property201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property201", None)
        self.__pivot_Property201 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Property203"):
                    opp_val = getattr(item, "pivot_Property203", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Property203", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Property203"):
                    opp_val = getattr(item, "pivot_Property203", None)
                    
                    setattr(item, "pivot_Property203", self)
                    

    @property
    def pivot_Property55(self):
        return self.__pivot_Property55

    @pivot_Property55.setter
    def pivot_Property55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property55", None)
        self.__pivot_Property55 = value
        
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
    def pivot_Property203(self):
        return self.__pivot_Property203

    @pivot_Property203.setter
    def pivot_Property203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property203", None)
        self.__pivot_Property203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property201"):
                opp_val = getattr(old_value, "pivot_Property201", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property201"):
                opp_val = getattr(value, "pivot_Property201", None)
                if opp_val is None:
                    setattr(value, "pivot_Property201", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Property196(self):
        return self.__pivot_Property196

    @pivot_Property196.setter
    def pivot_Property196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property196", None)
        self.__pivot_Property196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Class197"):
                opp_val = getattr(old_value, "pivot_Class197", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Class197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Class197"):
                opp_val = getattr(value, "pivot_Class197", None)
                setattr(value, "pivot_Class197", self)

    @property
    def pivot_Property217(self):
        return self.__pivot_Property217

    @pivot_Property217.setter
    def pivot_Property217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property217", None)
        self.__pivot_Property217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property215"):
                opp_val = getattr(old_value, "pivot_Property215", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property215"):
                opp_val = getattr(value, "pivot_Property215", None)
                if opp_val is None:
                    setattr(value, "pivot_Property215", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Property174(self):
        return self.__pivot_Property174

    @pivot_Property174.setter
    def pivot_Property174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property174", None)
        self.__pivot_Property174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OppositePropertyCallExp"):
                opp_val = getattr(old_value, "pivot_OppositePropertyCallExp", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OppositePropertyCallExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OppositePropertyCallExp"):
                opp_val = getattr(value, "pivot_OppositePropertyCallExp", None)
                setattr(value, "pivot_OppositePropertyCallExp", self)

    @property
    def pivot_Property206(self):
        return self.__pivot_Property206

    @pivot_Property206.setter
    def pivot_Property206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property206", None)
        self.__pivot_Property206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property204"):
                opp_val = getattr(old_value, "pivot_Property204", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property204"):
                opp_val = getattr(value, "pivot_Property204", None)
                setattr(value, "pivot_Property204", self)

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
            if hasattr(old_value, "associationClass"):
                opp_val = getattr(old_value, "associationClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "associationClass"):
                opp_val = getattr(value, "associationClass", None)
                if opp_val is None:
                    setattr(value, "associationClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Property333(self):
        return self.__Property333

    @Property333.setter
    def Property333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__Property333", None)
        self.__Property333 = value
        
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
    def pivot_Property212(self):
        return self.__pivot_Property212

    @pivot_Property212.setter
    def pivot_Property212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property212", None)
        self.__pivot_Property212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property214"):
                opp_val = getattr(old_value, "pivot_Property214", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property214"):
                opp_val = getattr(value, "pivot_Property214", None)
                setattr(value, "pivot_Property214", self)

    @property
    def pivot_Property204(self):
        return self.__pivot_Property204

    @pivot_Property204.setter
    def pivot_Property204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property204", None)
        self.__pivot_Property204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property206"):
                opp_val = getattr(old_value, "pivot_Property206", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property206"):
                opp_val = getattr(value, "pivot_Property206", None)
                setattr(value, "pivot_Property206", self)

    @property
    def pivot_Property209(self):
        return self.__pivot_Property209

    @pivot_Property209.setter
    def pivot_Property209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property209", None)
        self.__pivot_Property209 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Property211"):
                    opp_val = getattr(item, "pivot_Property211", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Property211", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Property211"):
                    opp_val = getattr(item, "pivot_Property211", None)
                    
                    setattr(item, "pivot_Property211", self)
                    

    @property
    def pivot_Property211(self):
        return self.__pivot_Property211

    @pivot_Property211.setter
    def pivot_Property211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property211", None)
        self.__pivot_Property211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property209"):
                opp_val = getattr(old_value, "pivot_Property209", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property209"):
                opp_val = getattr(value, "pivot_Property209", None)
                if opp_val is None:
                    setattr(value, "pivot_Property209", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Property138(self):
        return self.__pivot_Property138

    @pivot_Property138.setter
    def pivot_Property138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property138", None)
        self.__pivot_Property138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_NavigationCallExp"):
                opp_val = getattr(old_value, "pivot_NavigationCallExp", None)
                if opp_val == self:
                    setattr(old_value, "pivot_NavigationCallExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_NavigationCallExp"):
                opp_val = getattr(value, "pivot_NavigationCallExp", None)
                setattr(value, "pivot_NavigationCallExp", self)

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
            if hasattr(old_value, "Type208"):
                opp_val = getattr(old_value, "Type208", None)
                if opp_val == self:
                    setattr(old_value, "Type208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type208"):
                opp_val = getattr(value, "Type208", None)
                setattr(value, "Type208", self)

    @property
    def pivot_Property219(self):
        return self.__pivot_Property219

    @pivot_Property219.setter
    def pivot_Property219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property219", None)
        self.__pivot_Property219 = value
        
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
    def pivot_Property214(self):
        return self.__pivot_Property214

    @pivot_Property214.setter
    def pivot_Property214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property214", None)
        self.__pivot_Property214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property212"):
                opp_val = getattr(old_value, "pivot_Property212", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property212"):
                opp_val = getattr(value, "pivot_Property212", None)
                setattr(value, "pivot_Property212", self)

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

    def isAttribute(self, p: str) -> str:
        # TODO: Implement isAttribute method
        pass

    def CompatibleDefaultExpression(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CompatibleDefaultExpression method
        pass

class Class:

    pass
class pivot_AssociationClass(Class):

    pass
class pivot_Stereotype(Class):

    pass
class pivot_Metaclass(Class):

    pass
class pivot_SelfType(Class):

    def __init__(self):
        
    def specializeIn(self, selfType: Type, expr: OCLExpression) -> Type:
        # TODO: Implement specializeIn method
        pass

class pivot_Behavior(Class):

    pass
class pivot_UnspecifiedType(Class):

    pass
class pivot_InvalidType(Class):

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
            if hasattr(old_value, "pivot_Type51"):
                opp_val = getattr(old_value, "pivot_Type51", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Type51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Type51"):
                opp_val = getattr(value, "pivot_Type51", None)
                setattr(value, "pivot_Type51", self)

class pivot_VoidType(Class):

    pass
class pivot_AnyType(Class):

    pass