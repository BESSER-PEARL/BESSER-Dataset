from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TransitionKind(Enum):
    internal = "internal"
    local = "local"
    external = "external"
class PseudostateKind(Enum):
    choice = "choice"
    entryPoint = "entryPoint"
    exitPoint = "exitPoint"
    terminate = "terminate"
    initial = "initial"
    deepHistory = "deepHistory"
    shallowHistory = "shallowHistory"
    join = "join"
    fork = "fork"
    junction = "junction"
class CollectionKind(Enum):
    Collection = "Collection"
    Set = "Set"
    OrderedSet = "OrderedSet"
    Bag = "Bag"
    Sequence = "Sequence"
class AssociativityKind(Enum):
    Left = "Left"
    Right = "Right"


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
        
        pass
    def getReferredElement(self) :
        # TODO: Implement getReferredElement method
        pass

class pivot_StateMachine(Behavior):

    pass
class pivot_Pivotable(ABC):

    pass
class TemplateParameter:

    pass
class pivot_TypeTemplateParameter(TemplateParameter):

    def __init__(self, allowSubstitutable: str, pivot_TypeTemplateParameter: set["pivot_Type"] = None):
        self.allowSubstitutable = allowSubstitutable
        self.pivot_TypeTemplateParameter = pivot_TypeTemplateParameter if pivot_TypeTemplateParameter is not None else set()
        
        pass
    @property
    def allowSubstitutable(self):
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
                if hasattr(item, "pivot_Type336"):
                    opp_val = getattr(item, "pivot_Type336", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Type336", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Type336"):
                    opp_val = getattr(item, "pivot_Type336", None)
                    
                    setattr(item, "pivot_Type336", self)
                    

class pivot_OperationTemplateParameter(TemplateParameter):

    pass
class VariableDeclaration:

    pass
class pivot_TupleLiteralPart(VariableDeclaration):

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
class ParameterableElement:

    pass
class pivot_PackageableElement(ParameterableElement):

    pass
class TemplateableElement:

    pass
class Feature:

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
class NumericLiteralExp:

    pass
class pivot_RealLiteralExp(NumericLiteralExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
        pass
    @property
    def realSymbol(self):
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol


class pivot_UnlimitedNaturalLiteralExp(NumericLiteralExp):

    def __init__(self, unlimitedNaturalSymbol: str):
        self.unlimitedNaturalSymbol = unlimitedNaturalSymbol
        
        pass
    @property
    def unlimitedNaturalSymbol(self):
        return self.__unlimitedNaturalSymbol

    @unlimitedNaturalSymbol.setter
    def unlimitedNaturalSymbol(self, unlimitedNaturalSymbol: str):
        self.__unlimitedNaturalSymbol = unlimitedNaturalSymbol


class pivot_IntegerLiteralExp(NumericLiteralExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
        pass
    @property
    def integerSymbol(self):
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol


    def TypeIsInteger(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement TypeIsInteger method
        pass

class ReferringElement:

    pass
class pivot_OperationCallExp(ReferringElement, FeatureCallExp):

    def __init__(self, pivot_OperationCallExp: set["pivot_OCLExpression"] = None, pivot_OperationCallExp164: "pivot_Operation" = None):
        self.pivot_OperationCallExp = pivot_OperationCallExp if pivot_OperationCallExp is not None else set()
        self.pivot_OperationCallExp164 = pivot_OperationCallExp164
        
        pass
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
                if hasattr(item, "pivot_OCLExpression162"):
                    opp_val = getattr(item, "pivot_OCLExpression162", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_OCLExpression162", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_OCLExpression162"):
                    opp_val = getattr(item, "pivot_OCLExpression162", None)
                    
                    setattr(item, "pivot_OCLExpression162", self)
                    

    @property
    def pivot_OperationCallExp164(self):
        return self.__pivot_OperationCallExp164

    @pivot_OperationCallExp164.setter
    def pivot_OperationCallExp164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_OperationCallExp__pivot_OperationCallExp164", None)
        self.__pivot_OperationCallExp164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation165"):
                opp_val = getattr(old_value, "pivot_Operation165", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Operation165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation165"):
                opp_val = getattr(value, "pivot_Operation165", None)
                setattr(value, "pivot_Operation165", self)

    def ArgumentTypeIsConformant(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement ArgumentTypeIsConformant method
        pass

    def ArgumentCount(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement ArgumentCount method
        pass

class LoopExp:

    pass
class pivot_IteratorExp(ReferringElement, LoopExp):

    def __init__(self):
        
        pass
    def OneTypeIsBoolean(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement OneTypeIsBoolean method
        pass

    def SortedByIteratorTypeIsComparable(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement SortedByIteratorTypeIsComparable method
        pass

    def RejectOrSelectHasOneIterator(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement RejectOrSelectHasOneIterator method
        pass

    def CollectElementTypeIsSourceElementType(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement CollectElementTypeIsSourceElementType method
        pass

    def IteratorTypeIsSourceElementType(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement IteratorTypeIsSourceElementType method
        pass

    def SortedByElementTypeIsSourceElementType(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement SortedByElementTypeIsSourceElementType method
        pass

    def CollectNestedTypeIsBodyType(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement CollectNestedTypeIsBodyType method
        pass

    def ClosureElementTypeIsSourceElementType(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement ClosureElementTypeIsSourceElementType method
        pass

    def AnyBodyTypeIsBoolean(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement AnyBodyTypeIsBoolean method
        pass

    def IsUniqueTypeIsBoolean(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement IsUniqueTypeIsBoolean method
        pass

    def ClosureTypeIsUniqueCollection(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement ClosureTypeIsUniqueCollection method
        pass

    def RejectOrSelectTypeIsSourceType(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement RejectOrSelectTypeIsSourceType method
        pass

    def ExistsTypeIsBoolean(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement ExistsTypeIsBoolean method
        pass

    def SortedByHasOneIterator(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement SortedByHasOneIterator method
        pass

    def SortedByIsOrderedIfSourceIsOrdered(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement SortedByIsOrderedIfSourceIsOrdered method
        pass

    def ForAllTypeIsBoolean(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement ForAllTypeIsBoolean method
        pass

    def ExistsBodyTypeIsBoolean(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement ExistsBodyTypeIsBoolean method
        pass

    def AnyTypeIsSourceElementType(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement AnyTypeIsSourceElementType method
        pass

    def ClosureSourceElementTypeIsBodyElementType(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement ClosureSourceElementTypeIsBodyElementType method
        pass

    def CollectHasOneIterator(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement CollectHasOneIterator method
        pass

    def CollectNestedHasOneIterator(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement CollectNestedHasOneIterator method
        pass

    def ClosureHasOneIterator(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement ClosureHasOneIterator method
        pass

    def OneBodyTypeIsBoolean(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement OneBodyTypeIsBoolean method
        pass

    def CollectTypeIsUnordered(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement CollectTypeIsUnordered method
        pass

    def CollectNestedTypeIsBag(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement CollectNestedTypeIsBag method
        pass

    def OneHasOneIterator(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement OneHasOneIterator method
        pass

    def IsUniqueHasOneIterator(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement IsUniqueHasOneIterator method
        pass

    def AnyHasOneIterator(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement AnyHasOneIterator method
        pass

    def ClosureBodyTypeIsConformanttoIteratorType(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement ClosureBodyTypeIsConformanttoIteratorType method
        pass

    def ForAllBodyTypeIsBoolean(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement ForAllBodyTypeIsBoolean method
        pass

    def RejectOrSelectTypeIsBoolean(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement RejectOrSelectTypeIsBoolean method
        pass

class pivot_IterateExp(ReferringElement, LoopExp):

    def __init__(self, pivot_IterateExp: "pivot_Variable" = None):
        self.pivot_IterateExp = pivot_IterateExp
        
        pass
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
            if hasattr(old_value, "pivot_Variable85"):
                opp_val = getattr(old_value, "pivot_Variable85", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Variable85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Variable85"):
                opp_val = getattr(value, "pivot_Variable85", None)
                setattr(value, "pivot_Variable85", self)

    def BodyTypeConformsToResultType(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement BodyTypeConformsToResultType method
        pass

    def OneInitializer(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement OneInitializer method
        pass

    def TypeIsResultType(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement TypeIsResultType method
        pass

class State:

    pass
class pivot_FinalState(State):

    pass
class CallExp:

    pass
class pivot_LoopExp(CallExp):

    def __init__(self, pivot_LoopExp: "pivot_OCLExpression" = None, pivot_LoopExp107: set["pivot_Variable"] = None, pivot_LoopExp110: "pivot_Iteration" = None):
        self.pivot_LoopExp = pivot_LoopExp
        self.pivot_LoopExp107 = pivot_LoopExp107 if pivot_LoopExp107 is not None else set()
        self.pivot_LoopExp110 = pivot_LoopExp110
        
        pass
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
    def pivot_LoopExp107(self):
        return self.__pivot_LoopExp107

    @pivot_LoopExp107.setter
    def pivot_LoopExp107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_LoopExp__pivot_LoopExp107", None)
        self.__pivot_LoopExp107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Variable108"):
                    opp_val = getattr(item, "pivot_Variable108", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Variable108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Variable108"):
                    opp_val = getattr(item, "pivot_Variable108", None)
                    
                    setattr(item, "pivot_Variable108", self)
                    

    @property
    def pivot_LoopExp110(self):
        return self.__pivot_LoopExp110

    @pivot_LoopExp110.setter
    def pivot_LoopExp110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_LoopExp__pivot_LoopExp110", None)
        self.__pivot_LoopExp110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Iteration111"):
                opp_val = getattr(old_value, "pivot_Iteration111", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Iteration111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Iteration111"):
                opp_val = getattr(value, "pivot_Iteration111", None)
                setattr(value, "pivot_Iteration111", self)

    def NoInitializers(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement NoInitializers method
        pass

    def SourceIsCollection(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement SourceIsCollection method
        pass

class pivot_FeatureCallExp(CallExp):

    def __init__(self, isPre: str):
        self.isPre = isPre
        
        pass
    @property
    def isPre(self):
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
        
        pass
    @property
    def implementationClass(self):
        return self.__implementationClass

    @implementationClass.setter
    def implementationClass(self, implementationClass: str):
        self.__implementationClass = implementationClass


    @property
    def implementation(self):
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation


class pivot_Variable(VariableDeclaration):

    def __init__(self, implicit: str, pivot_Variable102: "pivot_LetExp" = None, pivot_Variable: "pivot_ExpressionInOCL" = None, pivot_Variable70: "pivot_ExpressionInOCL" = None, pivot_Variable73: "pivot_ExpressionInOCL" = None, pivot_Variable85: "pivot_IterateExp" = None, pivot_Variable108: "pivot_LoopExp" = None, pivot_Variable345: "pivot_OCLExpression" = None, pivot_Variable348: "pivot_Parameter" = None):
        self.implicit = implicit
        self.pivot_Variable102 = pivot_Variable102
        self.pivot_Variable = pivot_Variable
        self.pivot_Variable70 = pivot_Variable70
        self.pivot_Variable73 = pivot_Variable73
        self.pivot_Variable85 = pivot_Variable85
        self.pivot_Variable108 = pivot_Variable108
        self.pivot_Variable345 = pivot_Variable345
        self.pivot_Variable348 = pivot_Variable348
        
        pass
    @property
    def implicit(self):
        return self.__implicit

    @implicit.setter
    def implicit(self, implicit: str):
        self.__implicit = implicit


    @property
    def pivot_Variable102(self):
        return self.__pivot_Variable102

    @pivot_Variable102.setter
    def pivot_Variable102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable102", None)
        self.__pivot_Variable102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_LetExp101"):
                opp_val = getattr(old_value, "pivot_LetExp101", None)
                if opp_val == self:
                    setattr(old_value, "pivot_LetExp101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_LetExp101"):
                opp_val = getattr(value, "pivot_LetExp101", None)
                setattr(value, "pivot_LetExp101", self)

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
            if hasattr(old_value, "pivot_OCLExpression346"):
                opp_val = getattr(old_value, "pivot_OCLExpression346", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression346", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression346"):
                opp_val = getattr(value, "pivot_OCLExpression346", None)
                setattr(value, "pivot_OCLExpression346", self)

    @property
    def pivot_Variable73(self):
        return self.__pivot_Variable73

    @pivot_Variable73.setter
    def pivot_Variable73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable73", None)
        self.__pivot_Variable73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_ExpressionInOCL72"):
                opp_val = getattr(old_value, "pivot_ExpressionInOCL72", None)
                if opp_val == self:
                    setattr(old_value, "pivot_ExpressionInOCL72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ExpressionInOCL72"):
                opp_val = getattr(value, "pivot_ExpressionInOCL72", None)
                setattr(value, "pivot_ExpressionInOCL72", self)

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
            if hasattr(old_value, "pivot_LoopExp107"):
                opp_val = getattr(old_value, "pivot_LoopExp107", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_LoopExp107"):
                opp_val = getattr(value, "pivot_LoopExp107", None)
                if opp_val is None:
                    setattr(value, "pivot_LoopExp107", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Variable70(self):
        return self.__pivot_Variable70

    @pivot_Variable70.setter
    def pivot_Variable70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable70", None)
        self.__pivot_Variable70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_ExpressionInOCL69"):
                opp_val = getattr(old_value, "pivot_ExpressionInOCL69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ExpressionInOCL69"):
                opp_val = getattr(value, "pivot_ExpressionInOCL69", None)
                if opp_val is None:
                    setattr(value, "pivot_ExpressionInOCL69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Variable85(self):
        return self.__pivot_Variable85

    @pivot_Variable85.setter
    def pivot_Variable85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable85", None)
        self.__pivot_Variable85 = value
        
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
    def pivot_Variable348(self):
        return self.__pivot_Variable348

    @pivot_Variable348.setter
    def pivot_Variable348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable348", None)
        self.__pivot_Variable348 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Parameter349"):
                opp_val = getattr(old_value, "pivot_Parameter349", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Parameter349", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Parameter349"):
                opp_val = getattr(value, "pivot_Parameter349", None)
                setattr(value, "pivot_Parameter349", self)

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
            if hasattr(old_value, "pivot_ExpressionInOCL64"):
                opp_val = getattr(old_value, "pivot_ExpressionInOCL64", None)
                if opp_val == self:
                    setattr(old_value, "pivot_ExpressionInOCL64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ExpressionInOCL64"):
                opp_val = getattr(value, "pivot_ExpressionInOCL64", None)
                setattr(value, "pivot_ExpressionInOCL64", self)

    def CompatibleInitialiserType(self, pivot_diagnostics, pivot_context) :
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
class pivot_OpaqueExpression(ValueSpecification):

    def __init__(self, body: str, language: str, message: str, pivot_OpaqueExpression: "pivot_Constraint" = None, pivot_OpaqueExpression140: "pivot_Operation" = None, pivot_OpaqueExpression185: "pivot_Property" = None):
        self.body = body
        self.language = language
        self.message = message
        self.pivot_OpaqueExpression = pivot_OpaqueExpression
        self.pivot_OpaqueExpression140 = pivot_OpaqueExpression140
        self.pivot_OpaqueExpression185 = pivot_OpaqueExpression185
        
        pass
    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


    @property
    def pivot_OpaqueExpression140(self):
        return self.__pivot_OpaqueExpression140

    @pivot_OpaqueExpression140.setter
    def pivot_OpaqueExpression140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_OpaqueExpression__pivot_OpaqueExpression140", None)
        self.__pivot_OpaqueExpression140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation139"):
                opp_val = getattr(old_value, "pivot_Operation139", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Operation139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation139"):
                opp_val = getattr(value, "pivot_Operation139", None)
                setattr(value, "pivot_Operation139", self)

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
            if hasattr(old_value, "pivot_Constraint36"):
                opp_val = getattr(old_value, "pivot_Constraint36", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Constraint36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Constraint36"):
                opp_val = getattr(value, "pivot_Constraint36", None)
                setattr(value, "pivot_Constraint36", self)

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

class Vertex:

    pass
class pivot_Pseudostate(Vertex):

    def __init__(self, kind: str, pivot_Pseudostate: "pivot_ConnectionPointReference" = None, pivot_Pseudostate28: "pivot_ConnectionPointReference" = None, pivot_Pseudostate206: "pivot_State" = None, pivot_Pseudostate209: "pivot_StateMachine" = None, pivot_Pseudostate234: "pivot_State" = None, pivot_Pseudostate260: "pivot_StateMachine" = None):
        self.kind = kind
        self.pivot_Pseudostate = pivot_Pseudostate
        self.pivot_Pseudostate28 = pivot_Pseudostate28
        self.pivot_Pseudostate206 = pivot_Pseudostate206
        self.pivot_Pseudostate209 = pivot_Pseudostate209
        self.pivot_Pseudostate234 = pivot_Pseudostate234
        self.pivot_Pseudostate260 = pivot_Pseudostate260
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def pivot_Pseudostate234(self):
        return self.__pivot_Pseudostate234

    @pivot_Pseudostate234.setter
    def pivot_Pseudostate234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Pseudostate__pivot_Pseudostate234", None)
        self.__pivot_Pseudostate234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_State233"):
                opp_val = getattr(old_value, "pivot_State233", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_State233"):
                opp_val = getattr(value, "pivot_State233", None)
                if opp_val is None:
                    setattr(value, "pivot_State233", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Pseudostate206(self):
        return self.__pivot_Pseudostate206

    @pivot_Pseudostate206.setter
    def pivot_Pseudostate206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Pseudostate__pivot_Pseudostate206", None)
        self.__pivot_Pseudostate206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_State207"):
                opp_val = getattr(old_value, "pivot_State207", None)
                if opp_val == self:
                    setattr(old_value, "pivot_State207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_State207"):
                opp_val = getattr(value, "pivot_State207", None)
                setattr(value, "pivot_State207", self)

    @property
    def pivot_Pseudostate209(self):
        return self.__pivot_Pseudostate209

    @pivot_Pseudostate209.setter
    def pivot_Pseudostate209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Pseudostate__pivot_Pseudostate209", None)
        self.__pivot_Pseudostate209 = value
        
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
    def pivot_Pseudostate28(self):
        return self.__pivot_Pseudostate28

    @pivot_Pseudostate28.setter
    def pivot_Pseudostate28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Pseudostate__pivot_Pseudostate28", None)
        self.__pivot_Pseudostate28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_ConnectionPointReference27"):
                opp_val = getattr(old_value, "pivot_ConnectionPointReference27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ConnectionPointReference27"):
                opp_val = getattr(value, "pivot_ConnectionPointReference27", None)
                if opp_val is None:
                    setattr(value, "pivot_ConnectionPointReference27", set([self]))
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
class pivot_TemplateBinding(Element):

    pass
class pivot_ParameterableElement(Element):

    def __init__(self, ownedParameteredElement: "pivot_TemplateParameter" = None, parameteredElement: "pivot_TemplateParameter" = None, pivot_ParameterableElement: "pivot_TemplateParameter" = None, pivot_ParameterableElement275: "pivot_TemplateParameter" = None, ParameterableElement: "pivot_TemplateParameter" = None, ParameterableElement278: "pivot_TemplateParameter" = None, pivot_ParameterableElement282: "pivot_TemplateParameterSubstitution" = None, pivot_ParameterableElement288: "pivot_TemplateParameterSubstitution" = None):
        self.ownedParameteredElement = ownedParameteredElement
        self.parameteredElement = parameteredElement
        self.pivot_ParameterableElement = pivot_ParameterableElement
        self.pivot_ParameterableElement275 = pivot_ParameterableElement275
        self.ParameterableElement = ParameterableElement
        self.ParameterableElement278 = ParameterableElement278
        self.pivot_ParameterableElement282 = pivot_ParameterableElement282
        self.pivot_ParameterableElement288 = pivot_ParameterableElement288
        
        pass
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
    def pivot_ParameterableElement288(self):
        return self.__pivot_ParameterableElement288

    @pivot_ParameterableElement288.setter
    def pivot_ParameterableElement288(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ParameterableElement__pivot_ParameterableElement288", None)
        self.__pivot_ParameterableElement288 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_TemplateParameterSubstitution287"):
                opp_val = getattr(old_value, "pivot_TemplateParameterSubstitution287", None)
                if opp_val == self:
                    setattr(old_value, "pivot_TemplateParameterSubstitution287", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_TemplateParameterSubstitution287"):
                opp_val = getattr(value, "pivot_TemplateParameterSubstitution287", None)
                setattr(value, "pivot_TemplateParameterSubstitution287", self)

    @property
    def ParameterableElement278(self):
        return self.__ParameterableElement278

    @ParameterableElement278.setter
    def ParameterableElement278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ParameterableElement__ParameterableElement278", None)
        self.__ParameterableElement278 = value
        
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
    def parameteredElement(self):
        return self.__parameteredElement

    @parameteredElement.setter
    def parameteredElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ParameterableElement__parameteredElement", None)
        self.__parameteredElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TemplateParameter178"):
                opp_val = getattr(old_value, "TemplateParameter178", None)
                if opp_val == self:
                    setattr(old_value, "TemplateParameter178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TemplateParameter178"):
                opp_val = getattr(value, "TemplateParameter178", None)
                setattr(value, "TemplateParameter178", self)

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
    def pivot_ParameterableElement275(self):
        return self.__pivot_ParameterableElement275

    @pivot_ParameterableElement275.setter
    def pivot_ParameterableElement275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ParameterableElement__pivot_ParameterableElement275", None)
        self.__pivot_ParameterableElement275 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_TemplateParameter274"):
                opp_val = getattr(old_value, "pivot_TemplateParameter274", None)
                if opp_val == self:
                    setattr(old_value, "pivot_TemplateParameter274", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_TemplateParameter274"):
                opp_val = getattr(value, "pivot_TemplateParameter274", None)
                setattr(value, "pivot_TemplateParameter274", self)

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
            if hasattr(old_value, "pivot_TemplateParameterSubstitution"):
                opp_val = getattr(old_value, "pivot_TemplateParameterSubstitution", None)
                if opp_val == self:
                    setattr(old_value, "pivot_TemplateParameterSubstitution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_TemplateParameterSubstitution"):
                opp_val = getattr(value, "pivot_TemplateParameterSubstitution", None)
                setattr(value, "pivot_TemplateParameterSubstitution", self)

    def isCompatibleWith(self, pivot_p) :
        # TODO: Implement isCompatibleWith method
        pass

    def isTemplateParameter(self) :
        # TODO: Implement isTemplateParameter method
        pass

class pivot_TemplateParameter(Element):

    pass
class pivot_DynamicProperty(Element):

    def __init__(self, default: str, pivot_DynamicProperty: "pivot_Property" = None, pivot_DynamicProperty50: "pivot_DynamicType" = None):
        self.default = default
        self.pivot_DynamicProperty = pivot_DynamicProperty
        self.pivot_DynamicProperty50 = pivot_DynamicProperty50
        
        pass
    @property
    def default(self):
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
            if hasattr(old_value, "pivot_Property48"):
                opp_val = getattr(old_value, "pivot_Property48", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property48"):
                opp_val = getattr(value, "pivot_Property48", None)
                setattr(value, "pivot_Property48", self)

    @property
    def pivot_DynamicProperty50(self):
        return self.__pivot_DynamicProperty50

    @pivot_DynamicProperty50.setter
    def pivot_DynamicProperty50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_DynamicProperty__pivot_DynamicProperty50", None)
        self.__pivot_DynamicProperty50 = value
        
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

class pivot_DynamicElement(Element):

    pass
class pivot_TemplateSignature(Element):

    pass
class pivot_TemplateParameterSubstitution(Element):

    pass
class pivot_TemplateableElement(Element):

    def __init__(self, TemplateableElement: "pivot_TemplateBinding" = None, TemplateableElement296: "pivot_TemplateSignature" = None, template: "pivot_TemplateSignature" = None, boundElement: set["pivot_TemplateBinding"] = None, pivot_TemplateableElement: "pivot_TemplateableElement" = None, pivot_TemplateableElement301: "pivot_TemplateableElement" = None):
        self.TemplateableElement = TemplateableElement
        self.TemplateableElement296 = TemplateableElement296
        self.template = template
        self.boundElement = boundElement if boundElement is not None else set()
        self.pivot_TemplateableElement = pivot_TemplateableElement
        self.pivot_TemplateableElement301 = pivot_TemplateableElement301
        
        pass
    @property
    def TemplateableElement296(self):
        return self.__TemplateableElement296

    @TemplateableElement296.setter
    def TemplateableElement296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_TemplateableElement__TemplateableElement296", None)
        self.__TemplateableElement296 = value
        
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
                if hasattr(item, "TemplateBinding300"):
                    opp_val = getattr(item, "TemplateBinding300", None)
                    
                    if opp_val == self:
                        setattr(item, "TemplateBinding300", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TemplateBinding300"):
                    opp_val = getattr(item, "TemplateBinding300", None)
                    
                    setattr(item, "TemplateBinding300", self)
                    

    @property
    def pivot_TemplateableElement301(self):
        return self.__pivot_TemplateableElement301

    @pivot_TemplateableElement301.setter
    def pivot_TemplateableElement301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_TemplateableElement__pivot_TemplateableElement301", None)
        self.__pivot_TemplateableElement301 = value
        
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
    def pivot_TemplateableElement(self):
        return self.__pivot_TemplateableElement

    @pivot_TemplateableElement.setter
    def pivot_TemplateableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_TemplateableElement__pivot_TemplateableElement", None)
        self.__pivot_TemplateableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_TemplateableElement301"):
                opp_val = getattr(old_value, "pivot_TemplateableElement301", None)
                if opp_val == self:
                    setattr(old_value, "pivot_TemplateableElement301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_TemplateableElement301"):
                opp_val = getattr(value, "pivot_TemplateableElement301", None)
                setattr(value, "pivot_TemplateableElement301", self)

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
            if hasattr(old_value, "TemplateSignature298"):
                opp_val = getattr(old_value, "TemplateSignature298", None)
                if opp_val == self:
                    setattr(old_value, "TemplateSignature298", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TemplateSignature298"):
                opp_val = getattr(value, "TemplateSignature298", None)
                setattr(value, "TemplateSignature298", self)

    def parameterableElements(self) :
        # TODO: Implement parameterableElements method
        pass

    def isTemplate(self) :
        # TODO: Implement isTemplate method
        pass

class pivot_NamedElement(Element, Nameable):

    def __init__(self, isStatic: str, name: str, pivot_NamedElement: set["pivot_Annotation"] = None):
        self.isStatic = isStatic
        self.name = name
        self.pivot_NamedElement = pivot_NamedElement if pivot_NamedElement is not None else set()
        
        pass
    @property
    def isStatic(self):
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: str):
        self.__isStatic = isStatic


    @property
    def name(self):
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
                if hasattr(item, "pivot_Annotation129"):
                    opp_val = getattr(item, "pivot_Annotation129", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Annotation129", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Annotation129"):
                    opp_val = getattr(item, "pivot_Annotation129", None)
                    
                    setattr(item, "pivot_Annotation129", self)
                    

class pivot_Comment(Element):

    def __init__(self, body: str, pivot_Comment: set["pivot_Element"] = None, pivot_Comment54: "pivot_Element" = None):
        self.body = body
        self.pivot_Comment = pivot_Comment if pivot_Comment is not None else set()
        self.pivot_Comment54 = pivot_Comment54
        
        pass
    @property
    def body(self):
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
                if hasattr(item, "pivot_Element24"):
                    opp_val = getattr(item, "pivot_Element24", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Element24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Element24"):
                    opp_val = getattr(item, "pivot_Element24", None)
                    
                    setattr(item, "pivot_Element24", self)
                    

    @property
    def pivot_Comment54(self):
        return self.__pivot_Comment54

    @pivot_Comment54.setter
    def pivot_Comment54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Comment__pivot_Comment54", None)
        self.__pivot_Comment54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Element53"):
                opp_val = getattr(old_value, "pivot_Element53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Element53"):
                opp_val = getattr(value, "pivot_Element53", None)
                if opp_val is None:
                    setattr(value, "pivot_Element53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DataType:

    pass
class pivot_Enumeration(DataType):

    pass
class pivot_TupleType(DataType):

    pass
class pivot_PrimitiveType(DataType):

    pass
class pivot_LambdaType(DataType):

    pass
class pivot_CollectionType(DataType):

    def __init__(self, lower: str, upper: str, pivot_CollectionType: "pivot_Type" = None):
        self.lower = lower
        self.upper = upper
        self.pivot_CollectionType = pivot_CollectionType
        
        pass
    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower


    @property
    def upper(self):
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

class LiteralExp:

    pass
class pivot_EnumLiteralExp(LiteralExp):

    def __init__(self, pivot_EnumLiteralExp: "pivot_EnumerationLiteral" = None):
        self.pivot_EnumLiteralExp = pivot_EnumLiteralExp
        
        pass
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

    def TypeIsEnumerationType(self, pivot_diagnostics, pivot_context) :
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
        
        pass
    @property
    def kind(self):
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
                    

    def SetKindIsSet(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement SetKindIsSet method
        pass

    def OrderedSetKindIsOrderedSet(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement OrderedSetKindIsOrderedSet method
        pass

    def SequenceKindIsSequence(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement SequenceKindIsSequence method
        pass

    def BagKindIsBag(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement BagKindIsBag method
        pass

    def CollectionKindIsConcrete(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement CollectionKindIsConcrete method
        pass

class CollectionLiteralPart:

    pass
class pivot_CollectionItem(CollectionLiteralPart):

    def __init__(self, pivot_CollectionItem: "pivot_OCLExpression" = None):
        self.pivot_CollectionItem = pivot_CollectionItem
        
        pass
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
            if hasattr(old_value, "pivot_OCLExpression15"):
                opp_val = getattr(old_value, "pivot_OCLExpression15", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression15"):
                opp_val = getattr(value, "pivot_OCLExpression15", None)
                setattr(value, "pivot_OCLExpression15", self)

    def TypeIsItemType(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement TypeIsItemType method
        pass

class pivot_CollectionRange(CollectionLiteralPart):

    pass
class TypedElement:

    pass
class pivot_TypedMultiplicityElement(TypedElement):

    def __init__(self):
        
        pass
    def CompatibleBody(self, pivot_bodySpecification) :
        # TODO: Implement CompatibleBody method
        pass

    def makeParameter(self) :
        # TODO: Implement makeParameter method
        pass

class pivot_VariableDeclaration(TypedElement):

    pass
class pivot_ConstructorPart(TypedElement):

    pass
class pivot_ValueSpecification(TypedElement, ParameterableElement):

    def __init__(self):
        
        pass
    def isComputable(self) :
        # TODO: Implement isComputable method
        pass

    def unlimitedValue(self) :
        # TODO: Implement unlimitedValue method
        pass

    def integerValue(self) :
        # TODO: Implement integerValue method
        pass

    def stringValue(self) :
        # TODO: Implement stringValue method
        pass

    def isNull(self) :
        # TODO: Implement isNull method
        pass

    def booleanValue(self) :
        # TODO: Implement booleanValue method
        pass

class pivot_CollectionLiteralPart(TypedElement):

    pass
class pivot_OCLExpression(TypedElement):

    pass
class OCLExpression:

    pass
class pivot_ConstructorExp(OCLExpression):

    def __init__(self, value: str, pivot_ConstructorExp: set["pivot_ConstructorPart"] = None):
        self.value = value
        self.pivot_ConstructorExp = pivot_ConstructorExp if pivot_ConstructorExp is not None else set()
        
        pass
    @property
    def value(self):
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
                    

class pivot_LiteralExp(OCLExpression):

    pass
class pivot_VariableExp(OCLExpression, ReferringElement):

    def __init__(self, implicit: str, pivot_VariableExp: "pivot_VariableDeclaration" = None):
        self.implicit = implicit
        self.pivot_VariableExp = pivot_VariableExp
        
        pass
    @property
    def implicit(self):
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

class pivot_StateExp(OCLExpression):

    pass
class pivot_MessageExp(OCLExpression):

    def __init__(self, pivot_MessageExp115: "pivot_CallOperationAction" = None, pivot_MessageExp118: "pivot_SendSignalAction" = None, pivot_MessageExp120: "pivot_OCLExpression" = None, pivot_MessageExp: set["pivot_OCLExpression"] = None):
        self.pivot_MessageExp115 = pivot_MessageExp115
        self.pivot_MessageExp118 = pivot_MessageExp118
        self.pivot_MessageExp120 = pivot_MessageExp120
        self.pivot_MessageExp = pivot_MessageExp if pivot_MessageExp is not None else set()
        
        pass
    @property
    def pivot_MessageExp120(self):
        return self.__pivot_MessageExp120

    @pivot_MessageExp120.setter
    def pivot_MessageExp120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_MessageExp__pivot_MessageExp120", None)
        self.__pivot_MessageExp120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OCLExpression121"):
                opp_val = getattr(old_value, "pivot_OCLExpression121", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression121"):
                opp_val = getattr(value, "pivot_OCLExpression121", None)
                setattr(value, "pivot_OCLExpression121", self)

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

    def TargetIsNotACollection(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement TargetIsNotACollection method
        pass

    def OneCallOrOneSend(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement OneCallOrOneSend method
        pass

class pivot_IfExp(OCLExpression):

    def __init__(self, pivot_IfExp: "pivot_OCLExpression" = None, pivot_IfExp77: "pivot_OCLExpression" = None, pivot_IfExp80: "pivot_OCLExpression" = None):
        self.pivot_IfExp = pivot_IfExp
        self.pivot_IfExp77 = pivot_IfExp77
        self.pivot_IfExp80 = pivot_IfExp80
        
        pass
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

    @property
    def pivot_IfExp80(self):
        return self.__pivot_IfExp80

    @pivot_IfExp80.setter
    def pivot_IfExp80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_IfExp__pivot_IfExp80", None)
        self.__pivot_IfExp80 = value
        
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
            if hasattr(old_value, "pivot_OCLExpression75"):
                opp_val = getattr(old_value, "pivot_OCLExpression75", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression75"):
                opp_val = getattr(value, "pivot_OCLExpression75", None)
                setattr(value, "pivot_OCLExpression75", self)

    def ConditionTypeIsBoolean(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement ConditionTypeIsBoolean method
        pass

class pivot_TypeExp(ReferringElement, OCLExpression):

    pass
class pivot_UnspecifiedValueExp(OCLExpression):

    pass
class pivot_LetExp(OCLExpression):

    def __init__(self, pivot_LetExp: "pivot_OCLExpression" = None, pivot_LetExp101: "pivot_Variable" = None):
        self.pivot_LetExp = pivot_LetExp
        self.pivot_LetExp101 = pivot_LetExp101
        
        pass
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
            if hasattr(old_value, "pivot_OCLExpression99"):
                opp_val = getattr(old_value, "pivot_OCLExpression99", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression99"):
                opp_val = getattr(value, "pivot_OCLExpression99", None)
                setattr(value, "pivot_OCLExpression99", self)

    @property
    def pivot_LetExp101(self):
        return self.__pivot_LetExp101

    @pivot_LetExp101.setter
    def pivot_LetExp101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_LetExp__pivot_LetExp101", None)
        self.__pivot_LetExp101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Variable102"):
                opp_val = getattr(old_value, "pivot_Variable102", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Variable102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Variable102"):
                opp_val = getattr(value, "pivot_Variable102", None)
                setattr(value, "pivot_Variable102", self)

    def TypeIsInType(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement TypeIsInType method
        pass

class pivot_CallExp(OCLExpression):

    def __init__(self, implicit: str, pivot_CallExp: "pivot_OCLExpression" = None):
        self.implicit = implicit
        self.pivot_CallExp = pivot_CallExp
        
        pass
    @property
    def implicit(self):
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
class pivot_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class pivot_StringLiteralExp(PrimitiveLiteralExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
        pass
    @property
    def stringSymbol(self):
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol


class pivot_NullLiteralExp(PrimitiveLiteralExp):

    pass
class pivot_BooleanLiteralExp(PrimitiveLiteralExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
        pass
    @property
    def booleanSymbol(self):
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol


    def TypeIsBoolean(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement TypeIsBoolean method
        pass

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
class NavigationCallExp:

    pass
class pivot_PropertyCallExp(ReferringElement, NavigationCallExp):

    def __init__(self, pivot_PropertyCallExp: "pivot_Property" = None):
        self.pivot_PropertyCallExp = pivot_PropertyCallExp
        
        pass
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
            if hasattr(old_value, "pivot_Property204"):
                opp_val = getattr(old_value, "pivot_Property204", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property204"):
                opp_val = getattr(value, "pivot_Property204", None)
                setattr(value, "pivot_Property204", self)

    def CompatibleResultType(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement CompatibleResultType method
        pass

    def getSpecializedReferredPropertyType(self) :
        # TODO: Implement getSpecializedReferredPropertyType method
        pass

    def NonStaticSourceTypeIsConformant(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement NonStaticSourceTypeIsConformant method
        pass

    def getSpecializedReferredPropertyOwningType(self) :
        # TODO: Implement getSpecializedReferredPropertyOwningType method
        pass

class pivot_AssociationClassCallExp(NavigationCallExp):

    pass
class pivot_Property(Feature, ParameterableElement):

    def __init__(self, default: str, implicit: str, isComposite: str, isDerived: str, isID: str, isReadOnly: str, isResolveProxies: str, isTransient: str, isUnsettable: str, isVolatile: str, Property: "pivot_AssociationClass" = None, pivot_Property: "pivot_ConstructorPart" = None, pivot_Property48: "pivot_DynamicProperty" = None, pivot_Property134: "pivot_NavigationCallExp" = None, unownedAttribute: "pivot_AssociationClass" = None, pivot_Property181: "pivot_Class" = None, pivot_Property184: "pivot_OpaqueExpression" = None, pivot_Property204: "pivot_PropertyCallExp" = None, pivot_Property188: "pivot_Property" = None, pivot_Property186: set["pivot_Property"] = None, pivot_Property191: "pivot_Property" = None, pivot_Property189: "pivot_Property" = None, ownedAttribute: "pivot_Type" = None, pivot_Property196: "pivot_Property" = None, pivot_Property194: set["pivot_Property"] = None, pivot_Property199: "pivot_Property" = None, pivot_Property197: "pivot_Property" = None, pivot_Property202: "pivot_Property" = None, pivot_Property200: set["pivot_Property"] = None, Property321: "pivot_Type" = None):
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
        self.pivot_Property48 = pivot_Property48
        self.pivot_Property134 = pivot_Property134
        self.unownedAttribute = unownedAttribute
        self.pivot_Property181 = pivot_Property181
        self.pivot_Property184 = pivot_Property184
        self.pivot_Property204 = pivot_Property204
        self.pivot_Property188 = pivot_Property188
        self.pivot_Property186 = pivot_Property186 if pivot_Property186 is not None else set()
        self.pivot_Property191 = pivot_Property191
        self.pivot_Property189 = pivot_Property189
        self.ownedAttribute = ownedAttribute
        self.pivot_Property196 = pivot_Property196
        self.pivot_Property194 = pivot_Property194 if pivot_Property194 is not None else set()
        self.pivot_Property199 = pivot_Property199
        self.pivot_Property197 = pivot_Property197
        self.pivot_Property202 = pivot_Property202
        self.pivot_Property200 = pivot_Property200 if pivot_Property200 is not None else set()
        self.Property321 = Property321
        
        pass
    @property
    def implicit(self):
        return self.__implicit

    @implicit.setter
    def implicit(self, implicit: str):
        self.__implicit = implicit


    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default


    @property
    def isID(self):
        return self.__isID

    @isID.setter
    def isID(self, isID: str):
        self.__isID = isID


    @property
    def isVolatile(self):
        return self.__isVolatile

    @isVolatile.setter
    def isVolatile(self, isVolatile: str):
        self.__isVolatile = isVolatile


    @property
    def isComposite(self):
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite


    @property
    def isUnsettable(self):
        return self.__isUnsettable

    @isUnsettable.setter
    def isUnsettable(self, isUnsettable: str):
        self.__isUnsettable = isUnsettable


    @property
    def isReadOnly(self):
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly


    @property
    def isResolveProxies(self):
        return self.__isResolveProxies

    @isResolveProxies.setter
    def isResolveProxies(self, isResolveProxies: str):
        self.__isResolveProxies = isResolveProxies


    @property
    def isDerived(self):
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived


    @property
    def isTransient(self):
        return self.__isTransient

    @isTransient.setter
    def isTransient(self, isTransient: str):
        self.__isTransient = isTransient


    @property
    def pivot_Property48(self):
        return self.__pivot_Property48

    @pivot_Property48.setter
    def pivot_Property48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property48", None)
        self.__pivot_Property48 = value
        
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
    def pivot_Property134(self):
        return self.__pivot_Property134

    @pivot_Property134.setter
    def pivot_Property134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property134", None)
        self.__pivot_Property134 = value
        
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
    def pivot_Property199(self):
        return self.__pivot_Property199

    @pivot_Property199.setter
    def pivot_Property199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property199", None)
        self.__pivot_Property199 = value
        
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
    def pivot_Property189(self):
        return self.__pivot_Property189

    @pivot_Property189.setter
    def pivot_Property189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property189", None)
        self.__pivot_Property189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property191"):
                opp_val = getattr(old_value, "pivot_Property191", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property191"):
                opp_val = getattr(value, "pivot_Property191", None)
                setattr(value, "pivot_Property191", self)

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
    def pivot_Property202(self):
        return self.__pivot_Property202

    @pivot_Property202.setter
    def pivot_Property202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property202", None)
        self.__pivot_Property202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property200"):
                opp_val = getattr(old_value, "pivot_Property200", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property200"):
                opp_val = getattr(value, "pivot_Property200", None)
                if opp_val is None:
                    setattr(value, "pivot_Property200", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def pivot_Property200(self):
        return self.__pivot_Property200

    @pivot_Property200.setter
    def pivot_Property200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property200", None)
        self.__pivot_Property200 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Property202"):
                    opp_val = getattr(item, "pivot_Property202", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Property202", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Property202"):
                    opp_val = getattr(item, "pivot_Property202", None)
                    
                    setattr(item, "pivot_Property202", self)
                    

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
    def pivot_Property181(self):
        return self.__pivot_Property181

    @pivot_Property181.setter
    def pivot_Property181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property181", None)
        self.__pivot_Property181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Class182"):
                opp_val = getattr(old_value, "pivot_Class182", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Class182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Class182"):
                opp_val = getattr(value, "pivot_Class182", None)
                setattr(value, "pivot_Class182", self)

    @property
    def Property321(self):
        return self.__Property321

    @Property321.setter
    def Property321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__Property321", None)
        self.__Property321 = value
        
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
    def pivot_Property(self):
        return self.__pivot_Property

    @pivot_Property.setter
    def pivot_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property", None)
        self.__pivot_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_ConstructorPart42"):
                opp_val = getattr(old_value, "pivot_ConstructorPart42", None)
                if opp_val == self:
                    setattr(old_value, "pivot_ConstructorPart42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ConstructorPart42"):
                opp_val = getattr(value, "pivot_ConstructorPart42", None)
                setattr(value, "pivot_ConstructorPart42", self)

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
                if opp_val == self:
                    setattr(old_value, "pivot_Property189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property189"):
                opp_val = getattr(value, "pivot_Property189", None)
                setattr(value, "pivot_Property189", self)

    @property
    def pivot_Property194(self):
        return self.__pivot_Property194

    @pivot_Property194.setter
    def pivot_Property194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property194", None)
        self.__pivot_Property194 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Property196"):
                    opp_val = getattr(item, "pivot_Property196", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Property196", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Property196"):
                    opp_val = getattr(item, "pivot_Property196", None)
                    
                    setattr(item, "pivot_Property196", self)
                    

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
            if hasattr(old_value, "pivot_Property194"):
                opp_val = getattr(old_value, "pivot_Property194", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property194"):
                opp_val = getattr(value, "pivot_Property194", None)
                if opp_val is None:
                    setattr(value, "pivot_Property194", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def ownedAttribute(self):
        return self.__ownedAttribute

    @ownedAttribute.setter
    def ownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__ownedAttribute", None)
        self.__ownedAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type193"):
                opp_val = getattr(old_value, "Type193", None)
                if opp_val == self:
                    setattr(old_value, "Type193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type193"):
                opp_val = getattr(value, "Type193", None)
                setattr(value, "Type193", self)

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
            if hasattr(old_value, "pivot_PropertyCallExp"):
                opp_val = getattr(old_value, "pivot_PropertyCallExp", None)
                if opp_val == self:
                    setattr(old_value, "pivot_PropertyCallExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_PropertyCallExp"):
                opp_val = getattr(value, "pivot_PropertyCallExp", None)
                setattr(value, "pivot_PropertyCallExp", self)

    def CompatibleDefaultExpression(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement CompatibleDefaultExpression method
        pass

    def isAttribute(self, pivot_p) :
        # TODO: Implement isAttribute method
        pass

class Class:

    pass
class pivot_InvalidType(Class):

    pass
class pivot_AssociationClass(Class):

    pass
class pivot_Stereotype(Class):

    pass
class pivot_SelfType(Class):

    def __init__(self):
        
        pass
    def specializeIn(self, pivot_expr, pivot_selfType) :
        # TODO: Implement specializeIn method
        pass

class pivot_UnspecifiedType(Class):

    pass
class pivot_VoidType(Class):

    pass
class pivot_DataType(Class):

    def __init__(self, isSerializable: str, pivot_DataType: "pivot_Type" = None):
        self.isSerializable = isSerializable
        self.pivot_DataType = pivot_DataType
        
        pass
    @property
    def isSerializable(self):
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
            if hasattr(old_value, "pivot_Type44"):
                opp_val = getattr(old_value, "pivot_Type44", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Type44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Type44"):
                opp_val = getattr(value, "pivot_Type44", None)
                setattr(value, "pivot_Type44", self)

class pivot_Metaclass(Class):

    pass
class pivot_Behavior(Class):

    pass
class pivot_AnyType(Class):

    pass
class pivot_Element(Visitable):

    def __init__(self, pivot_Element: "pivot_Annotation" = None, pivot_Element5: "pivot_Annotation" = None, pivot_Element24: "pivot_Comment" = None, pivot_Element32: "pivot_Constraint" = None, base: set["pivot_ElementExtension"] = None, pivot_Element53: set["pivot_Comment"] = None, Element: "pivot_ElementExtension" = None):
        self.pivot_Element = pivot_Element
        self.pivot_Element5 = pivot_Element5
        self.pivot_Element24 = pivot_Element24
        self.pivot_Element32 = pivot_Element32
        self.base = base if base is not None else set()
        self.pivot_Element53 = pivot_Element53 if pivot_Element53 is not None else set()
        self.Element = Element
        
        pass
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
    def pivot_Element53(self):
        return self.__pivot_Element53

    @pivot_Element53.setter
    def pivot_Element53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Element__pivot_Element53", None)
        self.__pivot_Element53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Comment54"):
                    opp_val = getattr(item, "pivot_Comment54", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Comment54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Comment54"):
                    opp_val = getattr(item, "pivot_Comment54", None)
                    
                    setattr(item, "pivot_Comment54", self)
                    

    @property
    def pivot_Element24(self):
        return self.__pivot_Element24

    @pivot_Element24.setter
    def pivot_Element24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Element__pivot_Element24", None)
        self.__pivot_Element24 = value
        
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

    def allOwnedElements(self) :
        # TODO: Implement allOwnedElements method
        pass

    def getValue(self, pivot_propertyName, pivot_stereotype) :
        # TODO: Implement getValue method
        pass

class NamedElement:

    pass
class pivot_Signal(NamedElement):

    pass
class pivot_EnumerationLiteral(NamedElement):

    def __init__(self, value: str, EnumerationLiteral: "pivot_Enumeration" = None, ownedLiteral: "pivot_Enumeration" = None, pivot_EnumerationLiteral: "pivot_EnumLiteralExp" = None):
        self.value = value
        self.EnumerationLiteral = EnumerationLiteral
        self.ownedLiteral = ownedLiteral
        self.pivot_EnumerationLiteral = pivot_EnumerationLiteral
        
        pass
    @property
    def value(self):
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

class pivot_SendSignalAction(NamedElement):

    pass
class pivot_TypedElement(NamedElement):

    def __init__(self, isRequired: str, pivot_TypedElement: "pivot_Type" = None):
        self.isRequired = isRequired
        self.pivot_TypedElement = pivot_TypedElement
        
        pass
    @property
    def isRequired(self):
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
            if hasattr(old_value, "pivot_Type338"):
                opp_val = getattr(old_value, "pivot_Type338", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Type338", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Type338"):
                opp_val = getattr(value, "pivot_Type338", None)
                setattr(value, "pivot_Type338", self)

class pivot_Type(TemplateableElement, NamedElement, ParameterableElement):

    def __init__(self, instanceClassName: str, pivot_Type: "pivot_CollectionType" = None, pivot_Type44: "pivot_DataType" = None, pivot_Type46: "pivot_DynamicElement" = None, pivot_Type57: "pivot_ElementExtension" = None, pivot_Type97: "pivot_LambdaType" = None, pivot_Type91: "pivot_LambdaType" = None, pivot_Type94: "pivot_LambdaType" = None, pivot_Type127: "pivot_Metaclass" = None, pivot_Type157: "pivot_Operation" = None, Type: "pivot_Operation" = None, Type174: "pivot_Package" = None, Type193: "pivot_Property" = None, ownedType: "pivot_Package" = None, pivot_Type332: "pivot_Type" = None, pivot_Type330: set["pivot_Type"] = None, pivot_Type334: "pivot_TypeExp" = None, owningType: set["pivot_Property"] = None, pivot_Type323: set["pivot_Constraint"] = None, owningType326: set["pivot_Operation"] = None, pivot_Type336: "pivot_TypeTemplateParameter" = None, pivot_Type338: "pivot_TypedElement" = None, pivot_Type340: "pivot_UnspecifiedType" = None, pivot_Type343: "pivot_UnspecifiedType" = None):
        self.instanceClassName = instanceClassName
        self.pivot_Type = pivot_Type
        self.pivot_Type44 = pivot_Type44
        self.pivot_Type46 = pivot_Type46
        self.pivot_Type57 = pivot_Type57
        self.pivot_Type97 = pivot_Type97
        self.pivot_Type91 = pivot_Type91
        self.pivot_Type94 = pivot_Type94
        self.pivot_Type127 = pivot_Type127
        self.pivot_Type157 = pivot_Type157
        self.Type = Type
        self.Type174 = Type174
        self.Type193 = Type193
        self.ownedType = ownedType
        self.pivot_Type332 = pivot_Type332
        self.pivot_Type330 = pivot_Type330 if pivot_Type330 is not None else set()
        self.pivot_Type334 = pivot_Type334
        self.owningType = owningType if owningType is not None else set()
        self.pivot_Type323 = pivot_Type323 if pivot_Type323 is not None else set()
        self.owningType326 = owningType326 if owningType326 is not None else set()
        self.pivot_Type336 = pivot_Type336
        self.pivot_Type338 = pivot_Type338
        self.pivot_Type340 = pivot_Type340
        self.pivot_Type343 = pivot_Type343
        
        pass
    @property
    def instanceClassName(self):
        return self.__instanceClassName

    @instanceClassName.setter
    def instanceClassName(self, instanceClassName: str):
        self.__instanceClassName = instanceClassName


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
    def pivot_Type336(self):
        return self.__pivot_Type336

    @pivot_Type336.setter
    def pivot_Type336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type336", None)
        self.__pivot_Type336 = value
        
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
    def Type193(self):
        return self.__Type193

    @Type193.setter
    def Type193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__Type193", None)
        self.__Type193 = value
        
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
    def pivot_Type338(self):
        return self.__pivot_Type338

    @pivot_Type338.setter
    def pivot_Type338(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type338", None)
        self.__pivot_Type338 = value
        
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
    def pivot_Type46(self):
        return self.__pivot_Type46

    @pivot_Type46.setter
    def pivot_Type46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type46", None)
        self.__pivot_Type46 = value
        
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
    def pivot_Type157(self):
        return self.__pivot_Type157

    @pivot_Type157.setter
    def pivot_Type157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type157", None)
        self.__pivot_Type157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation156"):
                opp_val = getattr(old_value, "pivot_Operation156", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation156"):
                opp_val = getattr(value, "pivot_Operation156", None)
                if opp_val is None:
                    setattr(value, "pivot_Operation156", set([self]))
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
    def pivot_Type323(self):
        return self.__pivot_Type323

    @pivot_Type323.setter
    def pivot_Type323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type323", None)
        self.__pivot_Type323 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Constraint324"):
                    opp_val = getattr(item, "pivot_Constraint324", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Constraint324", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Constraint324"):
                    opp_val = getattr(item, "pivot_Constraint324", None)
                    
                    setattr(item, "pivot_Constraint324", self)
                    

    @property
    def pivot_Type44(self):
        return self.__pivot_Type44

    @pivot_Type44.setter
    def pivot_Type44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type44", None)
        self.__pivot_Type44 = value
        
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
    def pivot_Type127(self):
        return self.__pivot_Type127

    @pivot_Type127.setter
    def pivot_Type127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type127", None)
        self.__pivot_Type127 = value
        
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
    def pivot_Type91(self):
        return self.__pivot_Type91

    @pivot_Type91.setter
    def pivot_Type91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type91", None)
        self.__pivot_Type91 = value
        
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
    def pivot_Type343(self):
        return self.__pivot_Type343

    @pivot_Type343.setter
    def pivot_Type343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type343", None)
        self.__pivot_Type343 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_UnspecifiedType342"):
                opp_val = getattr(old_value, "pivot_UnspecifiedType342", None)
                if opp_val == self:
                    setattr(old_value, "pivot_UnspecifiedType342", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_UnspecifiedType342"):
                opp_val = getattr(value, "pivot_UnspecifiedType342", None)
                setattr(value, "pivot_UnspecifiedType342", self)

    @property
    def pivot_Type330(self):
        return self.__pivot_Type330

    @pivot_Type330.setter
    def pivot_Type330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type330", None)
        self.__pivot_Type330 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Type332"):
                    opp_val = getattr(item, "pivot_Type332", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Type332", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Type332"):
                    opp_val = getattr(item, "pivot_Type332", None)
                    
                    setattr(item, "pivot_Type332", self)
                    

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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_LambdaType93"):
                opp_val = getattr(value, "pivot_LambdaType93", None)
                if opp_val is None:
                    setattr(value, "pivot_LambdaType93", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "Package329"):
                opp_val = getattr(old_value, "Package329", None)
                if opp_val == self:
                    setattr(old_value, "Package329", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package329"):
                opp_val = getattr(value, "Package329", None)
                setattr(value, "Package329", self)

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
                if hasattr(item, "Property321"):
                    opp_val = getattr(item, "Property321", None)
                    
                    if opp_val == self:
                        setattr(item, "Property321", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property321"):
                    opp_val = getattr(item, "Property321", None)
                    
                    setattr(item, "Property321", self)
                    

    @property
    def pivot_Type332(self):
        return self.__pivot_Type332

    @pivot_Type332.setter
    def pivot_Type332(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type332", None)
        self.__pivot_Type332 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Type330"):
                opp_val = getattr(old_value, "pivot_Type330", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Type330"):
                opp_val = getattr(value, "pivot_Type330", None)
                if opp_val is None:
                    setattr(value, "pivot_Type330", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Type57(self):
        return self.__pivot_Type57

    @pivot_Type57.setter
    def pivot_Type57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type57", None)
        self.__pivot_Type57 = value
        
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
    def Type174(self):
        return self.__Type174

    @Type174.setter
    def Type174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__Type174", None)
        self.__Type174 = value
        
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
    def owningType326(self):
        return self.__owningType326

    @owningType326.setter
    def owningType326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__owningType326", None)
        self.__owningType326 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation327"):
                    opp_val = getattr(item, "Operation327", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation327", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation327"):
                    opp_val = getattr(item, "Operation327", None)
                    
                    setattr(item, "Operation327", self)
                    

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
    def pivot_Type97(self):
        return self.__pivot_Type97

    @pivot_Type97.setter
    def pivot_Type97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type97", None)
        self.__pivot_Type97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_LambdaType96"):
                opp_val = getattr(old_value, "pivot_LambdaType96", None)
                if opp_val == self:
                    setattr(old_value, "pivot_LambdaType96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_LambdaType96"):
                opp_val = getattr(value, "pivot_LambdaType96", None)
                setattr(value, "pivot_LambdaType96", self)

    @property
    def pivot_Type334(self):
        return self.__pivot_Type334

    @pivot_Type334.setter
    def pivot_Type334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type334", None)
        self.__pivot_Type334 = value
        
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

    def specializeIn(self, pivot_selfType, pivot_expr) :
        # TODO: Implement specializeIn method
        pass

    def UniqueInvariantName(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement UniqueInvariantName method
        pass

class pivot_Vertex(NamedElement):

    pass
class pivot_Import(NamedElement):

    pass
class pivot_Detail(NamedElement):

    def __init__(self, value: str, pivot_Detail: "pivot_Annotation" = None):
        self.value = value
        self.pivot_Detail = pivot_Detail
        
        pass
    @property
    def value(self):
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

class pivot_Precedence(NamedElement):

    def __init__(self, associativity: str, order: str, pivot_Precedence: "pivot_Library" = None, pivot_Precedence151: "pivot_Operation" = None):
        self.associativity = associativity
        self.order = order
        self.pivot_Precedence = pivot_Precedence
        self.pivot_Precedence151 = pivot_Precedence151
        
        pass
    @property
    def associativity(self):
        return self.__associativity

    @associativity.setter
    def associativity(self, associativity: str):
        self.__associativity = associativity


    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order: str):
        self.__order = order


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

class pivot_CallOperationAction(NamedElement):

    pass
class pivot_Trigger(NamedElement):

    pass
class pivot_Namespace(NamedElement):

    pass
class pivot_Constraint(NamedElement):

    def __init__(self, isCallable: str, pivot_Constraint: set["pivot_Element"] = None, pivot_Constraint34: "pivot_Namespace" = None, pivot_Constraint36: "pivot_OpaqueExpression" = None, pivot_Constraint132: "pivot_Namespace" = None, pivot_Constraint154: "pivot_Operation" = None, pivot_Constraint148: "pivot_Operation" = None, pivot_Constraint254: "pivot_State" = None, pivot_Constraint308: "pivot_Transition" = None, pivot_Constraint324: "pivot_Type" = None):
        self.isCallable = isCallable
        self.pivot_Constraint = pivot_Constraint if pivot_Constraint is not None else set()
        self.pivot_Constraint34 = pivot_Constraint34
        self.pivot_Constraint36 = pivot_Constraint36
        self.pivot_Constraint132 = pivot_Constraint132
        self.pivot_Constraint154 = pivot_Constraint154
        self.pivot_Constraint148 = pivot_Constraint148
        self.pivot_Constraint254 = pivot_Constraint254
        self.pivot_Constraint308 = pivot_Constraint308
        self.pivot_Constraint324 = pivot_Constraint324
        
        pass
    @property
    def isCallable(self):
        return self.__isCallable

    @isCallable.setter
    def isCallable(self, isCallable: str):
        self.__isCallable = isCallable


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
    def pivot_Constraint148(self):
        return self.__pivot_Constraint148

    @pivot_Constraint148.setter
    def pivot_Constraint148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint148", None)
        self.__pivot_Constraint148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation147"):
                opp_val = getattr(old_value, "pivot_Operation147", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation147"):
                opp_val = getattr(value, "pivot_Operation147", None)
                if opp_val is None:
                    setattr(value, "pivot_Operation147", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Constraint36(self):
        return self.__pivot_Constraint36

    @pivot_Constraint36.setter
    def pivot_Constraint36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint36", None)
        self.__pivot_Constraint36 = value
        
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
    def pivot_Constraint254(self):
        return self.__pivot_Constraint254

    @pivot_Constraint254.setter
    def pivot_Constraint254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint254", None)
        self.__pivot_Constraint254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_State253"):
                opp_val = getattr(old_value, "pivot_State253", None)
                if opp_val == self:
                    setattr(old_value, "pivot_State253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_State253"):
                opp_val = getattr(value, "pivot_State253", None)
                setattr(value, "pivot_State253", self)

    @property
    def pivot_Constraint154(self):
        return self.__pivot_Constraint154

    @pivot_Constraint154.setter
    def pivot_Constraint154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint154", None)
        self.__pivot_Constraint154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation153"):
                opp_val = getattr(old_value, "pivot_Operation153", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation153"):
                opp_val = getattr(value, "pivot_Operation153", None)
                if opp_val is None:
                    setattr(value, "pivot_Operation153", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Constraint324(self):
        return self.__pivot_Constraint324

    @pivot_Constraint324.setter
    def pivot_Constraint324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint324", None)
        self.__pivot_Constraint324 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Type323"):
                opp_val = getattr(old_value, "pivot_Type323", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Type323"):
                opp_val = getattr(value, "pivot_Type323", None)
                if opp_val is None:
                    setattr(value, "pivot_Type323", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Constraint132(self):
        return self.__pivot_Constraint132

    @pivot_Constraint132.setter
    def pivot_Constraint132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint132", None)
        self.__pivot_Constraint132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Namespace131"):
                opp_val = getattr(old_value, "pivot_Namespace131", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Namespace131"):
                opp_val = getattr(value, "pivot_Namespace131", None)
                if opp_val is None:
                    setattr(value, "pivot_Namespace131", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Constraint308(self):
        return self.__pivot_Constraint308

    @pivot_Constraint308.setter
    def pivot_Constraint308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint308", None)
        self.__pivot_Constraint308 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Transition307"):
                opp_val = getattr(old_value, "pivot_Transition307", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Transition307", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Transition307"):
                opp_val = getattr(value, "pivot_Transition307", None)
                setattr(value, "pivot_Transition307", self)

    def UniqueName(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement UniqueName method
        pass

class pivot_Annotation(NamedElement):

    pass
class Namespace:

    pass
class pivot_Transition(Namespace):

    def __init__(self, kind: str, incoming: "pivot_Vertex" = None, Transition: "pivot_Region" = None, outgoing: "pivot_Vertex" = None, pivot_Transition314: set["pivot_Trigger"] = None, transition: "pivot_Region" = None, pivot_Transition: "pivot_Behavior" = None, pivot_Transition307: "pivot_Constraint" = None, Transition354: "pivot_Vertex" = None, Transition356: "pivot_Vertex" = None):
        self.kind = kind
        self.incoming = incoming
        self.Transition = Transition
        self.outgoing = outgoing
        self.pivot_Transition314 = pivot_Transition314 if pivot_Transition314 is not None else set()
        self.transition = transition
        self.pivot_Transition = pivot_Transition
        self.pivot_Transition307 = pivot_Transition307
        self.Transition354 = Transition354
        self.Transition356 = Transition356
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


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
    def Transition354(self):
        return self.__Transition354

    @Transition354.setter
    def Transition354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__Transition354", None)
        self.__Transition354 = value
        
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
    def pivot_Transition314(self):
        return self.__pivot_Transition314

    @pivot_Transition314.setter
    def pivot_Transition314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__pivot_Transition314", None)
        self.__pivot_Transition314 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Trigger315"):
                    opp_val = getattr(item, "pivot_Trigger315", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Trigger315", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Trigger315"):
                    opp_val = getattr(item, "pivot_Trigger315", None)
                    
                    setattr(item, "pivot_Trigger315", self)
                    

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
            if hasattr(old_value, "pivot_Constraint308"):
                opp_val = getattr(old_value, "pivot_Constraint308", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Constraint308", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Constraint308"):
                opp_val = getattr(value, "pivot_Constraint308", None)
                setattr(value, "pivot_Constraint308", self)

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
            if hasattr(old_value, "Vertex312"):
                opp_val = getattr(old_value, "Vertex312", None)
                if opp_val == self:
                    setattr(old_value, "Vertex312", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex312"):
                opp_val = getattr(value, "Vertex312", None)
                setattr(value, "Vertex312", self)

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
            if hasattr(old_value, "container220"):
                opp_val = getattr(old_value, "container220", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container220"):
                opp_val = getattr(value, "container220", None)
                if opp_val is None:
                    setattr(value, "container220", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "Vertex310"):
                opp_val = getattr(old_value, "Vertex310", None)
                if opp_val == self:
                    setattr(old_value, "Vertex310", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex310"):
                opp_val = getattr(value, "Vertex310", None)
                setattr(value, "Vertex310", self)

    @property
    def Transition356(self):
        return self.__Transition356

    @Transition356.setter
    def Transition356(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__Transition356", None)
        self.__Transition356 = value
        
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
    def pivot_Transition(self):
        return self.__pivot_Transition

    @pivot_Transition.setter
    def pivot_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__pivot_Transition", None)
        self.__pivot_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Behavior305"):
                opp_val = getattr(old_value, "pivot_Behavior305", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Behavior305", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Behavior305"):
                opp_val = getattr(value, "pivot_Behavior305", None)
                setattr(value, "pivot_Behavior305", self)

class pivot_Region(Namespace):

    pass
class pivot_State(Namespace, Vertex):

    def __init__(self, isComposite: str, isOrthogonal: str, isSimple: str, isSubmachineState: str, pivot_State: "pivot_ConnectionPointReference" = None, pivot_State207: "pivot_Pseudostate" = None, pivot_State230: set["pivot_ConnectionPointReference"] = None, pivot_State214: "pivot_Region" = None, pivot_State248: "pivot_State" = None, pivot_State246: "pivot_State" = None, pivot_State250: set["pivot_Region"] = None, pivot_State233: set["pivot_Pseudostate"] = None, pivot_State236: set["pivot_Trigger"] = None, pivot_State238: "pivot_Behavior" = None, pivot_State241: "pivot_Behavior" = None, pivot_State244: "pivot_Behavior" = None, pivot_State253: "pivot_Constraint" = None, submachineState: "pivot_StateMachine" = None, pivot_State257: "pivot_StateExp" = None, State: "pivot_StateMachine" = None):
        self.isComposite = isComposite
        self.isOrthogonal = isOrthogonal
        self.isSimple = isSimple
        self.isSubmachineState = isSubmachineState
        self.pivot_State = pivot_State
        self.pivot_State207 = pivot_State207
        self.pivot_State230 = pivot_State230 if pivot_State230 is not None else set()
        self.pivot_State214 = pivot_State214
        self.pivot_State248 = pivot_State248
        self.pivot_State246 = pivot_State246
        self.pivot_State250 = pivot_State250 if pivot_State250 is not None else set()
        self.pivot_State233 = pivot_State233 if pivot_State233 is not None else set()
        self.pivot_State236 = pivot_State236 if pivot_State236 is not None else set()
        self.pivot_State238 = pivot_State238
        self.pivot_State241 = pivot_State241
        self.pivot_State244 = pivot_State244
        self.pivot_State253 = pivot_State253
        self.submachineState = submachineState
        self.pivot_State257 = pivot_State257
        self.State = State
        
        pass
    @property
    def isSubmachineState(self):
        return self.__isSubmachineState

    @isSubmachineState.setter
    def isSubmachineState(self, isSubmachineState: str):
        self.__isSubmachineState = isSubmachineState


    @property
    def isOrthogonal(self):
        return self.__isOrthogonal

    @isOrthogonal.setter
    def isOrthogonal(self, isOrthogonal: str):
        self.__isOrthogonal = isOrthogonal


    @property
    def isSimple(self):
        return self.__isSimple

    @isSimple.setter
    def isSimple(self, isSimple: str):
        self.__isSimple = isSimple


    @property
    def isComposite(self):
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite


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
            if hasattr(old_value, "pivot_Constraint254"):
                opp_val = getattr(old_value, "pivot_Constraint254", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Constraint254", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Constraint254"):
                opp_val = getattr(value, "pivot_Constraint254", None)
                setattr(value, "pivot_Constraint254", self)

    @property
    def pivot_State214(self):
        return self.__pivot_State214

    @pivot_State214.setter
    def pivot_State214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State214", None)
        self.__pivot_State214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Region213"):
                opp_val = getattr(old_value, "pivot_Region213", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Region213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Region213"):
                opp_val = getattr(value, "pivot_Region213", None)
                setattr(value, "pivot_Region213", self)

    @property
    def pivot_State238(self):
        return self.__pivot_State238

    @pivot_State238.setter
    def pivot_State238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State238", None)
        self.__pivot_State238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Behavior239"):
                opp_val = getattr(old_value, "pivot_Behavior239", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Behavior239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Behavior239"):
                opp_val = getattr(value, "pivot_Behavior239", None)
                setattr(value, "pivot_Behavior239", self)

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
    def pivot_State207(self):
        return self.__pivot_State207

    @pivot_State207.setter
    def pivot_State207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State207", None)
        self.__pivot_State207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Pseudostate206"):
                opp_val = getattr(old_value, "pivot_Pseudostate206", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Pseudostate206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Pseudostate206"):
                opp_val = getattr(value, "pivot_Pseudostate206", None)
                setattr(value, "pivot_Pseudostate206", self)

    @property
    def pivot_State244(self):
        return self.__pivot_State244

    @pivot_State244.setter
    def pivot_State244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State244", None)
        self.__pivot_State244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Behavior245"):
                opp_val = getattr(old_value, "pivot_Behavior245", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Behavior245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Behavior245"):
                opp_val = getattr(value, "pivot_Behavior245", None)
                setattr(value, "pivot_Behavior245", self)

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
            if hasattr(old_value, "pivot_State248"):
                opp_val = getattr(old_value, "pivot_State248", None)
                if opp_val == self:
                    setattr(old_value, "pivot_State248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_State248"):
                opp_val = getattr(value, "pivot_State248", None)
                setattr(value, "pivot_State248", self)

    @property
    def pivot_State230(self):
        return self.__pivot_State230

    @pivot_State230.setter
    def pivot_State230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State230", None)
        self.__pivot_State230 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_ConnectionPointReference231"):
                    opp_val = getattr(item, "pivot_ConnectionPointReference231", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_ConnectionPointReference231", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_ConnectionPointReference231"):
                    opp_val = getattr(item, "pivot_ConnectionPointReference231", None)
                    
                    setattr(item, "pivot_ConnectionPointReference231", self)
                    

    @property
    def pivot_State250(self):
        return self.__pivot_State250

    @pivot_State250.setter
    def pivot_State250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State250", None)
        self.__pivot_State250 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Region251"):
                    opp_val = getattr(item, "pivot_Region251", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Region251", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Region251"):
                    opp_val = getattr(item, "pivot_Region251", None)
                    
                    setattr(item, "pivot_Region251", self)
                    

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
            if hasattr(old_value, "pivot_ConnectionPointReference30"):
                opp_val = getattr(old_value, "pivot_ConnectionPointReference30", None)
                if opp_val == self:
                    setattr(old_value, "pivot_ConnectionPointReference30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ConnectionPointReference30"):
                opp_val = getattr(value, "pivot_ConnectionPointReference30", None)
                setattr(value, "pivot_ConnectionPointReference30", self)

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
    def pivot_State233(self):
        return self.__pivot_State233

    @pivot_State233.setter
    def pivot_State233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State233", None)
        self.__pivot_State233 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Pseudostate234"):
                    opp_val = getattr(item, "pivot_Pseudostate234", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Pseudostate234", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Pseudostate234"):
                    opp_val = getattr(item, "pivot_Pseudostate234", None)
                    
                    setattr(item, "pivot_Pseudostate234", self)
                    

    @property
    def pivot_State241(self):
        return self.__pivot_State241

    @pivot_State241.setter
    def pivot_State241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State241", None)
        self.__pivot_State241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Behavior242"):
                opp_val = getattr(old_value, "pivot_Behavior242", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Behavior242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Behavior242"):
                opp_val = getattr(value, "pivot_Behavior242", None)
                setattr(value, "pivot_Behavior242", self)

    @property
    def pivot_State236(self):
        return self.__pivot_State236

    @pivot_State236.setter
    def pivot_State236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State236", None)
        self.__pivot_State236 = value if value is not None else set()
        
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
    def pivot_State248(self):
        return self.__pivot_State248

    @pivot_State248.setter
    def pivot_State248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State248", None)
        self.__pivot_State248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_State246"):
                opp_val = getattr(old_value, "pivot_State246", None)
                if opp_val == self:
                    setattr(old_value, "pivot_State246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_State246"):
                opp_val = getattr(value, "pivot_State246", None)
                setattr(value, "pivot_State246", self)

class pivot_Root(Namespace):

    def __init__(self, externalURI: str, pivot_Root224: set["pivot_Package"] = None, pivot_Root: set["pivot_Import"] = None):
        self.externalURI = externalURI
        self.pivot_Root224 = pivot_Root224 if pivot_Root224 is not None else set()
        self.pivot_Root = pivot_Root if pivot_Root is not None else set()
        
        pass
    @property
    def externalURI(self):
        return self.__externalURI

    @externalURI.setter
    def externalURI(self, externalURI: str):
        self.__externalURI = externalURI


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
    def pivot_Root224(self):
        return self.__pivot_Root224

    @pivot_Root224.setter
    def pivot_Root224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Root__pivot_Root224", None)
        self.__pivot_Root224 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Package225"):
                    opp_val = getattr(item, "pivot_Package225", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Package225", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Package225"):
                    opp_val = getattr(item, "pivot_Package225", None)
                    
                    setattr(item, "pivot_Package225", self)
                    

class pivot_Package(Namespace, TemplateableElement):

    def __init__(self, nsPrefix: str, nsURI: str, Package172: "pivot_Package" = None, nestedPackage: "pivot_Package" = None, package: set["pivot_Type"] = None, pivot_Package: "pivot_Package" = None, pivot_Package166: set["pivot_Package"] = None, Package: "pivot_Package" = None, nestingPackage: set["pivot_Package"] = None, pivot_Package225: "pivot_Root" = None, Package329: "pivot_Type" = None):
        self.nsPrefix = nsPrefix
        self.nsURI = nsURI
        self.Package172 = Package172
        self.nestedPackage = nestedPackage
        self.package = package if package is not None else set()
        self.pivot_Package = pivot_Package
        self.pivot_Package166 = pivot_Package166 if pivot_Package166 is not None else set()
        self.Package = Package
        self.nestingPackage = nestingPackage if nestingPackage is not None else set()
        self.pivot_Package225 = pivot_Package225
        self.Package329 = Package329
        
        pass
    @property
    def nsPrefix(self):
        return self.__nsPrefix

    @nsPrefix.setter
    def nsPrefix(self, nsPrefix: str):
        self.__nsPrefix = nsPrefix


    @property
    def nsURI(self):
        return self.__nsURI

    @nsURI.setter
    def nsURI(self, nsURI: str):
        self.__nsURI = nsURI


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
            if hasattr(old_value, "pivot_Package166"):
                opp_val = getattr(old_value, "pivot_Package166", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Package166"):
                opp_val = getattr(value, "pivot_Package166", None)
                if opp_val is None:
                    setattr(value, "pivot_Package166", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Package166(self):
        return self.__pivot_Package166

    @pivot_Package166.setter
    def pivot_Package166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__pivot_Package166", None)
        self.__pivot_Package166 = value if value is not None else set()
        
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
    def Package329(self):
        return self.__Package329

    @Package329.setter
    def Package329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__Package329", None)
        self.__Package329 = value
        
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
    def pivot_Package225(self):
        return self.__pivot_Package225

    @pivot_Package225.setter
    def pivot_Package225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__pivot_Package225", None)
        self.__pivot_Package225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Root224"):
                opp_val = getattr(old_value, "pivot_Root224", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Root224"):
                opp_val = getattr(value, "pivot_Root224", None)
                if opp_val is None:
                    setattr(value, "pivot_Root224", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "Type174"):
                    opp_val = getattr(item, "Type174", None)
                    
                    if opp_val == self:
                        setattr(item, "Type174", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type174"):
                    opp_val = getattr(item, "Type174", None)
                    
                    setattr(item, "Type174", self)
                    

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
            if hasattr(old_value, "Package172"):
                opp_val = getattr(old_value, "Package172", None)
                if opp_val == self:
                    setattr(old_value, "Package172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package172"):
                opp_val = getattr(value, "Package172", None)
                setattr(value, "Package172", self)

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
    def Package172(self):
        return self.__Package172

    @Package172.setter
    def Package172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__Package172", None)
        self.__Package172 = value
        
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
                    

class pivot_Operation(Namespace, TemplateableElement, Feature, ParameterableElement):

    def __init__(self, isValidating: str, isInvalidating: str, pivot_Operation: "pivot_CallOperationAction" = None, pivot_Operation123: "pivot_MessageType" = None, pivot_Operation150: "pivot_Precedence" = None, pivot_Operation153: set["pivot_Constraint"] = None, pivot_Operation156: set["pivot_Type"] = None, pivot_Operation160: "pivot_Operation" = None, pivot_Operation158: set["pivot_Operation"] = None, pivot_Operation139: "pivot_OpaqueExpression" = None, pivot_Operation142: "pivot_Class" = None, operation: set["pivot_Parameter"] = None, ownedOperation: "pivot_Type" = None, pivot_Operation147: set["pivot_Constraint"] = None, Operation: "pivot_Parameter" = None, pivot_Operation165: "pivot_OperationCallExp" = None, Operation327: "pivot_Type" = None):
        self.isValidating = isValidating
        self.isInvalidating = isInvalidating
        self.pivot_Operation = pivot_Operation
        self.pivot_Operation123 = pivot_Operation123
        self.pivot_Operation150 = pivot_Operation150
        self.pivot_Operation153 = pivot_Operation153 if pivot_Operation153 is not None else set()
        self.pivot_Operation156 = pivot_Operation156 if pivot_Operation156 is not None else set()
        self.pivot_Operation160 = pivot_Operation160
        self.pivot_Operation158 = pivot_Operation158 if pivot_Operation158 is not None else set()
        self.pivot_Operation139 = pivot_Operation139
        self.pivot_Operation142 = pivot_Operation142
        self.operation = operation if operation is not None else set()
        self.ownedOperation = ownedOperation
        self.pivot_Operation147 = pivot_Operation147 if pivot_Operation147 is not None else set()
        self.Operation = Operation
        self.pivot_Operation165 = pivot_Operation165
        self.Operation327 = Operation327
        
        pass
    @property
    def isInvalidating(self):
        return self.__isInvalidating

    @isInvalidating.setter
    def isInvalidating(self, isInvalidating: str):
        self.__isInvalidating = isInvalidating


    @property
    def isValidating(self):
        return self.__isValidating

    @isValidating.setter
    def isValidating(self, isValidating: str):
        self.__isValidating = isValidating


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
    def pivot_Operation158(self):
        return self.__pivot_Operation158

    @pivot_Operation158.setter
    def pivot_Operation158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation158", None)
        self.__pivot_Operation158 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Operation160"):
                    opp_val = getattr(item, "pivot_Operation160", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Operation160", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Operation160"):
                    opp_val = getattr(item, "pivot_Operation160", None)
                    
                    setattr(item, "pivot_Operation160", self)
                    

    @property
    def pivot_Operation147(self):
        return self.__pivot_Operation147

    @pivot_Operation147.setter
    def pivot_Operation147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation147", None)
        self.__pivot_Operation147 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Constraint148"):
                    opp_val = getattr(item, "pivot_Constraint148", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Constraint148", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Constraint148"):
                    opp_val = getattr(item, "pivot_Constraint148", None)
                    
                    setattr(item, "pivot_Constraint148", self)
                    

    @property
    def pivot_Operation139(self):
        return self.__pivot_Operation139

    @pivot_Operation139.setter
    def pivot_Operation139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation139", None)
        self.__pivot_Operation139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OpaqueExpression140"):
                opp_val = getattr(old_value, "pivot_OpaqueExpression140", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OpaqueExpression140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OpaqueExpression140"):
                opp_val = getattr(value, "pivot_OpaqueExpression140", None)
                setattr(value, "pivot_OpaqueExpression140", self)

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
    def Operation327(self):
        return self.__Operation327

    @Operation327.setter
    def Operation327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__Operation327", None)
        self.__Operation327 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningType326"):
                opp_val = getattr(old_value, "owningType326", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningType326"):
                opp_val = getattr(value, "owningType326", None)
                if opp_val is None:
                    setattr(value, "owningType326", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def pivot_Operation142(self):
        return self.__pivot_Operation142

    @pivot_Operation142.setter
    def pivot_Operation142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation142", None)
        self.__pivot_Operation142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Class143"):
                opp_val = getattr(old_value, "pivot_Class143", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Class143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Class143"):
                opp_val = getattr(value, "pivot_Class143", None)
                setattr(value, "pivot_Class143", self)

    @property
    def pivot_Operation156(self):
        return self.__pivot_Operation156

    @pivot_Operation156.setter
    def pivot_Operation156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation156", None)
        self.__pivot_Operation156 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Type157"):
                    opp_val = getattr(item, "pivot_Type157", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Type157", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Type157"):
                    opp_val = getattr(item, "pivot_Type157", None)
                    
                    setattr(item, "pivot_Type157", self)
                    

    @property
    def pivot_Operation123(self):
        return self.__pivot_Operation123

    @pivot_Operation123.setter
    def pivot_Operation123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation123", None)
        self.__pivot_Operation123 = value
        
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
    def pivot_Operation160(self):
        return self.__pivot_Operation160

    @pivot_Operation160.setter
    def pivot_Operation160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation160", None)
        self.__pivot_Operation160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation158"):
                opp_val = getattr(old_value, "pivot_Operation158", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation158"):
                opp_val = getattr(value, "pivot_Operation158", None)
                if opp_val is None:
                    setattr(value, "pivot_Operation158", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Operation153(self):
        return self.__pivot_Operation153

    @pivot_Operation153.setter
    def pivot_Operation153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation153", None)
        self.__pivot_Operation153 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Constraint154"):
                    opp_val = getattr(item, "pivot_Constraint154", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Constraint154", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Constraint154"):
                    opp_val = getattr(item, "pivot_Constraint154", None)
                    
                    setattr(item, "pivot_Constraint154", self)
                    

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
    def pivot_Operation165(self):
        return self.__pivot_Operation165

    @pivot_Operation165.setter
    def pivot_Operation165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation165", None)
        self.__pivot_Operation165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OperationCallExp164"):
                opp_val = getattr(old_value, "pivot_OperationCallExp164", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OperationCallExp164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OperationCallExp164"):
                opp_val = getattr(value, "pivot_OperationCallExp164", None)
                setattr(value, "pivot_OperationCallExp164", self)

    def UniquePreconditionName(self, pivot_context, pivot_diagnostics) :
        # TODO: Implement UniquePreconditionName method
        pass

    def UniquePostconditionName(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement UniquePostconditionName method
        pass

    def CompatibleReturn(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement CompatibleReturn method
        pass

    def LoadableImplementation(self, pivot_diagnostics, pivot_context) :
        # TODO: Implement LoadableImplementation method
        pass

class Type:

    pass
class pivot_MessageType(Type):

    pass
class pivot_ElementExtension(Type):

    pass
class pivot_DynamicType(DynamicElement, Type):

    pass
class pivot_TemplateParameterType(Type):

    def __init__(self, specification: str):
        self.specification = specification
        
        pass
    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification


class pivot_Class(Namespace, Type):

    def __init__(self, isAbstract: str, isInterface: str, pivot_Class: "pivot_Class" = None, pivot_Class10: set["pivot_Class"] = None, pivot_Class13: set["pivot_Behavior"] = None, pivot_Class143: "pivot_Operation" = None, pivot_Class182: "pivot_Property" = None):
        self.isAbstract = isAbstract
        self.isInterface = isInterface
        self.pivot_Class = pivot_Class
        self.pivot_Class10 = pivot_Class10 if pivot_Class10 is not None else set()
        self.pivot_Class13 = pivot_Class13 if pivot_Class13 is not None else set()
        self.pivot_Class143 = pivot_Class143
        self.pivot_Class182 = pivot_Class182
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def isInterface(self):
        return self.__isInterface

    @isInterface.setter
    def isInterface(self, isInterface: str):
        self.__isInterface = isInterface


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
            if hasattr(old_value, "pivot_Class10"):
                opp_val = getattr(old_value, "pivot_Class10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Class10"):
                opp_val = getattr(value, "pivot_Class10", None)
                if opp_val is None:
                    setattr(value, "pivot_Class10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Class13(self):
        return self.__pivot_Class13

    @pivot_Class13.setter
    def pivot_Class13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__pivot_Class13", None)
        self.__pivot_Class13 = value if value is not None else set()
        
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
                    

    @property
    def pivot_Class143(self):
        return self.__pivot_Class143

    @pivot_Class143.setter
    def pivot_Class143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__pivot_Class143", None)
        self.__pivot_Class143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation142"):
                opp_val = getattr(old_value, "pivot_Operation142", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Operation142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation142"):
                opp_val = getattr(value, "pivot_Operation142", None)
                setattr(value, "pivot_Operation142", self)

    @property
    def pivot_Class10(self):
        return self.__pivot_Class10

    @pivot_Class10.setter
    def pivot_Class10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__pivot_Class10", None)
        self.__pivot_Class10 = value if value is not None else set()
        
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
    def pivot_Class182(self):
        return self.__pivot_Class182

    @pivot_Class182.setter
    def pivot_Class182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__pivot_Class182", None)
        self.__pivot_Class182 = value
        
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
