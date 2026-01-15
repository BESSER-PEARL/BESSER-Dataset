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
class AssociativityKind(Enum):
    left = "left"
    right = "right"
class CollectionKind(Enum):
    Collection = "Collection"
    Set = "Set"
    OrderedSet = "OrderedSet"
    Bag = "Bag"
    Sequence = "Sequence"
class PseudostateKind(Enum):
    exitPoint = "exitPoint"
    terminate = "terminate"
    initial = "initial"
    deepHistory = "deepHistory"
    shallowHistory = "shallowHistory"
    join = "join"
    fork = "fork"
    junction = "junction"
    choice = "choice"
    entryPoint = "entryPoint"


############################################
# Definition of Classes
############################################

class pivot_Visitable(ABC):

    pass
class pivot_ReferringElement(ABC):

    def __init__(self):
        
    def getReferredElement(self) -> Element:
        # TODO: Implement getReferredElement method
        pass

class VariableDeclaration:

    pass
class pivot_TupleLiteralPart(VariableDeclaration):

    pass
class pivot_Pivotable(ABC):

    pass
class CompletePackage:

    pass
class Feature:

    pass
class Nameable:

    pass
class pivot_Nameable(ABC):

    pass
class pivot_MorePivotable(ABC):

    pass
class FeatureCallExp:

    pass
class pivot_NavigationCallExp(FeatureCallExp):

    pass
class Package:

    pass
class pivot_Profile(Package):

    pass
class pivot_Library(Package):

    pass
class pivot_Parameter(VariableDeclaration):

    def __init__(self, isTypeof: str, pivot_Parameter: "pivot_Iteration" = None, pivot_Parameter135: "pivot_Iteration" = None, Parameter: "pivot_Operation" = None, ownedParameters: "pivot_Operation" = None, pivot_Parameter403: "pivot_Variable" = None):
        self.isTypeof = isTypeof
        self.pivot_Parameter = pivot_Parameter
        self.pivot_Parameter135 = pivot_Parameter135
        self.Parameter = Parameter
        self.ownedParameters = ownedParameters
        self.pivot_Parameter403 = pivot_Parameter403
        
    @property
    def isTypeof(self) -> str:
        return self.__isTypeof

    @isTypeof.setter
    def isTypeof(self, isTypeof: str):
        self.__isTypeof = isTypeof

    @property
    def ownedParameters(self):
        return self.__ownedParameters

    @ownedParameters.setter
    def ownedParameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Parameter__ownedParameters", None)
        self.__ownedParameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation244"):
                opp_val = getattr(old_value, "Operation244", None)
                if opp_val == self:
                    setattr(old_value, "Operation244", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation244"):
                opp_val = getattr(value, "Operation244", None)
                setattr(value, "Operation244", self)

    @property
    def pivot_Parameter403(self):
        return self.__pivot_Parameter403

    @pivot_Parameter403.setter
    def pivot_Parameter403(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Parameter__pivot_Parameter403", None)
        self.__pivot_Parameter403 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Variable402"):
                opp_val = getattr(old_value, "pivot_Variable402", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Variable402", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Variable402"):
                opp_val = getattr(value, "pivot_Variable402", None)
                setattr(value, "pivot_Variable402", self)

    @property
    def Parameter(self):
        return self.__Parameter

    @Parameter.setter
    def Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Parameter__Parameter", None)
        self.__Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningOperation"):
                opp_val = getattr(old_value, "owningOperation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningOperation"):
                opp_val = getattr(value, "owningOperation", None)
                if opp_val is None:
                    setattr(value, "owningOperation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Parameter135(self):
        return self.__pivot_Parameter135

    @pivot_Parameter135.setter
    def pivot_Parameter135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Parameter__pivot_Parameter135", None)
        self.__pivot_Parameter135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Iteration134"):
                opp_val = getattr(old_value, "pivot_Iteration134", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Iteration134"):
                opp_val = getattr(value, "pivot_Iteration134", None)
                if opp_val is None:
                    setattr(value, "pivot_Iteration134", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Parameter(self):
        return self.__pivot_Parameter

    @pivot_Parameter.setter
    def pivot_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Parameter__pivot_Parameter", None)
        self.__pivot_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Iteration"):
                opp_val = getattr(old_value, "pivot_Iteration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Iteration"):
                opp_val = getattr(value, "pivot_Iteration", None)
                if opp_val is None:
                    setattr(value, "pivot_Iteration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Operation:

    pass
class pivot_Iteration(Operation):

    pass
class NumericLiteralExp:

    pass
class pivot_RealLiteralExp(NumericLiteralExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> str:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol

class pivot_UnlimitedNaturalLiteralExp(NumericLiteralExp):

    def __init__(self, unlimitedNaturalSymbol: str):
        self.unlimitedNaturalSymbol = unlimitedNaturalSymbol
        
    @property
    def unlimitedNaturalSymbol(self) -> str:
        return self.__unlimitedNaturalSymbol

    @unlimitedNaturalSymbol.setter
    def unlimitedNaturalSymbol(self, unlimitedNaturalSymbol: str):
        self.__unlimitedNaturalSymbol = unlimitedNaturalSymbol

class pivot_IntegerLiteralExp(NumericLiteralExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

    def validateTypeIsInteger(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateTypeIsInteger method
        pass

class ReferringElement:

    pass
class pivot_OperationCallExp(FeatureCallExp, ReferringElement):

    def __init__(self, pivot_OperationCallExp223: "pivot_Operation" = None, pivot_OperationCallExp: set["pivot_OCLExpression"] = None):
        self.pivot_OperationCallExp223 = pivot_OperationCallExp223
        self.pivot_OperationCallExp = pivot_OperationCallExp if pivot_OperationCallExp is not None else set()
        
    @property
    def pivot_OperationCallExp223(self):
        return self.__pivot_OperationCallExp223

    @pivot_OperationCallExp223.setter
    def pivot_OperationCallExp223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_OperationCallExp__pivot_OperationCallExp223", None)
        self.__pivot_OperationCallExp223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation224"):
                opp_val = getattr(old_value, "pivot_Operation224", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Operation224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation224"):
                opp_val = getattr(value, "pivot_Operation224", None)
                setattr(value, "pivot_Operation224", self)

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
                if hasattr(item, "pivot_OCLExpression221"):
                    opp_val = getattr(item, "pivot_OCLExpression221", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_OCLExpression221", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_OCLExpression221"):
                    opp_val = getattr(item, "pivot_OCLExpression221", None)
                    
                    setattr(item, "pivot_OCLExpression221", self)
                    

    def validateSafeSourceCanBeNull(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateSafeSourceCanBeNull method
        pass

    def validateArgumentTypeIsConformant(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateArgumentTypeIsConformant method
        pass

    def validateArgumentCount(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateArgumentCount method
        pass

class LoopExp:

    pass
class pivot_IteratorExp(LoopExp, ReferringElement):

    def __init__(self):
        
    def validateAnyBodyTypeIsBoolean(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateAnyBodyTypeIsBoolean method
        pass

    def validateSortedByIsOrderedIfSourceIsOrdered(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateSortedByIsOrderedIfSourceIsOrdered method
        pass

    def validateAnyHasOneIterator(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateAnyHasOneIterator method
        pass

    def validateCollectElementTypeIsFlattenedBodyType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateCollectElementTypeIsFlattenedBodyType method
        pass

    def validateClosureHasOneIterator(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateClosureHasOneIterator method
        pass

    def validateSafeIteratorIsRequired(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateSafeIteratorIsRequired method
        pass

    def validateAnyTypeIsSourceElementType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateAnyTypeIsSourceElementType method
        pass

    def validateUnsafeSourceCanNotBeNull(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateUnsafeSourceCanNotBeNull method
        pass

    def validateSortedByElementTypeIsSourceElementType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateSortedByElementTypeIsSourceElementType method
        pass

    def validateIteratorTypeIsSourceElementType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateIteratorTypeIsSourceElementType method
        pass

    def validateClosureTypeIsUniqueCollection(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateClosureTypeIsUniqueCollection method
        pass

    def validateClosureElementTypeIsSourceElementType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateClosureElementTypeIsSourceElementType method
        pass

    def validateSortedByIteratorTypeIsComparable(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateSortedByIteratorTypeIsComparable method
        pass

    def validateSafeSourceCanBeNull(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateSafeSourceCanBeNull method
        pass

    def validateCollectTypeIsUnordered(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateCollectTypeIsUnordered method
        pass

    def validateClosureSourceElementTypeIsBodyElementType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateClosureSourceElementTypeIsBodyElementType method
        pass

    def validateClosureBodyTypeIsConformanttoIteratorType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateClosureBodyTypeIsConformanttoIteratorType method
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
            if hasattr(old_value, "pivot_Variable131"):
                opp_val = getattr(old_value, "pivot_Variable131", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Variable131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Variable131"):
                opp_val = getattr(value, "pivot_Variable131", None)
                setattr(value, "pivot_Variable131", self)

    def validateTypeIsResultType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateTypeIsResultType method
        pass

    def validateSafeSourceCanBeNull(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateSafeSourceCanBeNull method
        pass

    def validateBodyTypeConformsToResultType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateBodyTypeConformsToResultType method
        pass

    def validateOneInitializer(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateOneInitializer method
        pass

    def validateUnsafeSourceCanNotBeNull(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateUnsafeSourceCanNotBeNull method
        pass

    def validateSafeIteratorIsRequired(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateSafeIteratorIsRequired method
        pass

class State:

    pass
class pivot_FinalState(State):

    pass
class CallExp:

    pass
class pivot_LoopExp(CallExp):

    def __init__(self, pivot_LoopExp: "pivot_OCLExpression" = None, pivot_LoopExp154: set["pivot_Variable"] = None, pivot_LoopExp157: "pivot_Iteration" = None):
        self.pivot_LoopExp = pivot_LoopExp
        self.pivot_LoopExp154 = pivot_LoopExp154 if pivot_LoopExp154 is not None else set()
        self.pivot_LoopExp157 = pivot_LoopExp157
        
    @property
    def pivot_LoopExp154(self):
        return self.__pivot_LoopExp154

    @pivot_LoopExp154.setter
    def pivot_LoopExp154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_LoopExp__pivot_LoopExp154", None)
        self.__pivot_LoopExp154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Variable155"):
                    opp_val = getattr(item, "pivot_Variable155", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Variable155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Variable155"):
                    opp_val = getattr(item, "pivot_Variable155", None)
                    
                    setattr(item, "pivot_Variable155", self)
                    

    @property
    def pivot_LoopExp157(self):
        return self.__pivot_LoopExp157

    @pivot_LoopExp157.setter
    def pivot_LoopExp157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_LoopExp__pivot_LoopExp157", None)
        self.__pivot_LoopExp157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Iteration158"):
                opp_val = getattr(old_value, "pivot_Iteration158", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Iteration158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Iteration158"):
                opp_val = getattr(value, "pivot_Iteration158", None)
                setattr(value, "pivot_Iteration158", self)

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
            if hasattr(old_value, "pivot_OCLExpression152"):
                opp_val = getattr(old_value, "pivot_OCLExpression152", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression152"):
                opp_val = getattr(value, "pivot_OCLExpression152", None)
                setattr(value, "pivot_OCLExpression152", self)

    def validateNoInitializers(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateNoInitializers method
        pass

    def validateSourceIsCollection(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateSourceIsCollection method
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

class InstanceSpecification:

    pass
class pivot_EnumerationLiteral(InstanceSpecification):

    def __init__(self, value: str, pivot_EnumerationLiteral: "pivot_EnumLiteralExp" = None, EnumerationLiteral: "pivot_Enumeration" = None, ownedLiterals: "pivot_Enumeration" = None):
        self.value = value
        self.pivot_EnumerationLiteral = pivot_EnumerationLiteral
        self.EnumerationLiteral = EnumerationLiteral
        self.ownedLiterals = ownedLiterals
        
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
            if hasattr(old_value, "owningEnumeration"):
                opp_val = getattr(old_value, "owningEnumeration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningEnumeration"):
                opp_val = getattr(value, "owningEnumeration", None)
                if opp_val is None:
                    setattr(value, "owningEnumeration", set([self]))
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
    def ownedLiterals(self):
        return self.__ownedLiterals

    @ownedLiterals.setter
    def ownedLiterals(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_EnumerationLiteral__ownedLiterals", None)
        self.__ownedLiterals = value
        
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

class pivot_Variable(VariableDeclaration):

    def __init__(self, isImplicit: str, pivot_Variable: "pivot_ExpressionInOCL" = None, pivot_Variable109: "pivot_ExpressionInOCL" = None, pivot_Variable112: "pivot_ExpressionInOCL" = None, pivot_Variable131: "pivot_IterateExp" = None, pivot_Variable149: "pivot_LetExp" = None, pivot_Variable155: "pivot_LoopExp" = None, pivot_Variable399: "pivot_OCLExpression" = None, pivot_Variable402: "pivot_Parameter" = None):
        self.isImplicit = isImplicit
        self.pivot_Variable = pivot_Variable
        self.pivot_Variable109 = pivot_Variable109
        self.pivot_Variable112 = pivot_Variable112
        self.pivot_Variable131 = pivot_Variable131
        self.pivot_Variable149 = pivot_Variable149
        self.pivot_Variable155 = pivot_Variable155
        self.pivot_Variable399 = pivot_Variable399
        self.pivot_Variable402 = pivot_Variable402
        
    @property
    def isImplicit(self) -> str:
        return self.__isImplicit

    @isImplicit.setter
    def isImplicit(self, isImplicit: str):
        self.__isImplicit = isImplicit

    @property
    def pivot_Variable402(self):
        return self.__pivot_Variable402

    @pivot_Variable402.setter
    def pivot_Variable402(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable402", None)
        self.__pivot_Variable402 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Parameter403"):
                opp_val = getattr(old_value, "pivot_Parameter403", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Parameter403", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Parameter403"):
                opp_val = getattr(value, "pivot_Parameter403", None)
                setattr(value, "pivot_Parameter403", self)

    @property
    def pivot_Variable112(self):
        return self.__pivot_Variable112

    @pivot_Variable112.setter
    def pivot_Variable112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable112", None)
        self.__pivot_Variable112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_ExpressionInOCL111"):
                opp_val = getattr(old_value, "pivot_ExpressionInOCL111", None)
                if opp_val == self:
                    setattr(old_value, "pivot_ExpressionInOCL111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ExpressionInOCL111"):
                opp_val = getattr(value, "pivot_ExpressionInOCL111", None)
                setattr(value, "pivot_ExpressionInOCL111", self)

    @property
    def pivot_Variable149(self):
        return self.__pivot_Variable149

    @pivot_Variable149.setter
    def pivot_Variable149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable149", None)
        self.__pivot_Variable149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_LetExp148"):
                opp_val = getattr(old_value, "pivot_LetExp148", None)
                if opp_val == self:
                    setattr(old_value, "pivot_LetExp148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_LetExp148"):
                opp_val = getattr(value, "pivot_LetExp148", None)
                setattr(value, "pivot_LetExp148", self)

    @property
    def pivot_Variable399(self):
        return self.__pivot_Variable399

    @pivot_Variable399.setter
    def pivot_Variable399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable399", None)
        self.__pivot_Variable399 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OCLExpression400"):
                opp_val = getattr(old_value, "pivot_OCLExpression400", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression400", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression400"):
                opp_val = getattr(value, "pivot_OCLExpression400", None)
                setattr(value, "pivot_OCLExpression400", self)

    @property
    def pivot_Variable131(self):
        return self.__pivot_Variable131

    @pivot_Variable131.setter
    def pivot_Variable131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable131", None)
        self.__pivot_Variable131 = value
        
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
    def pivot_Variable155(self):
        return self.__pivot_Variable155

    @pivot_Variable155.setter
    def pivot_Variable155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable155", None)
        self.__pivot_Variable155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_LoopExp154"):
                opp_val = getattr(old_value, "pivot_LoopExp154", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_LoopExp154"):
                opp_val = getattr(value, "pivot_LoopExp154", None)
                if opp_val is None:
                    setattr(value, "pivot_LoopExp154", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "pivot_ExpressionInOCL106"):
                opp_val = getattr(old_value, "pivot_ExpressionInOCL106", None)
                if opp_val == self:
                    setattr(old_value, "pivot_ExpressionInOCL106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ExpressionInOCL106"):
                opp_val = getattr(value, "pivot_ExpressionInOCL106", None)
                setattr(value, "pivot_ExpressionInOCL106", self)

    @property
    def pivot_Variable109(self):
        return self.__pivot_Variable109

    @pivot_Variable109.setter
    def pivot_Variable109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Variable__pivot_Variable109", None)
        self.__pivot_Variable109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_ExpressionInOCL108"):
                opp_val = getattr(old_value, "pivot_ExpressionInOCL108", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ExpressionInOCL108"):
                opp_val = getattr(value, "pivot_ExpressionInOCL108", None)
                if opp_val is None:
                    setattr(value, "pivot_ExpressionInOCL108", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def validateCompatibleInitialiserType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateCompatibleInitialiserType method
        pass

class LanguageExpression:

    pass
class pivot_ExpressionInOCL(LanguageExpression):

    pass
class Visitable:

    pass
class ValueSpecification:

    pass
class pivot_DynamicValueSpecification(ValueSpecification):

    pass
class DynamicType:

    pass
class Behavior:

    pass
class pivot_StateMachine(Behavior):

    pass
class pivot_DynamicBehavior(DynamicType, Behavior):

    pass
class pivot_LanguageExpression(ValueSpecification):

    def __init__(self, body: str, language: str, LanguageExpression: "pivot_Constraint" = None, pivot_LanguageExpression: "pivot_InstanceSpecification" = None, ownedSpecification: "pivot_Constraint" = None, pivot_LanguageExpression204: "pivot_Operation" = None, pivot_LanguageExpression261: "pivot_Property" = None):
        self.body = body
        self.language = language
        self.LanguageExpression = LanguageExpression
        self.pivot_LanguageExpression = pivot_LanguageExpression
        self.ownedSpecification = ownedSpecification
        self.pivot_LanguageExpression204 = pivot_LanguageExpression204
        self.pivot_LanguageExpression261 = pivot_LanguageExpression261
        
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
    def ownedSpecification(self):
        return self.__ownedSpecification

    @ownedSpecification.setter
    def ownedSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_LanguageExpression__ownedSpecification", None)
        self.__ownedSpecification = value
        
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
    def pivot_LanguageExpression(self):
        return self.__pivot_LanguageExpression

    @pivot_LanguageExpression.setter
    def pivot_LanguageExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_LanguageExpression__pivot_LanguageExpression", None)
        self.__pivot_LanguageExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_InstanceSpecification127"):
                opp_val = getattr(old_value, "pivot_InstanceSpecification127", None)
                if opp_val == self:
                    setattr(old_value, "pivot_InstanceSpecification127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_InstanceSpecification127"):
                opp_val = getattr(value, "pivot_InstanceSpecification127", None)
                setattr(value, "pivot_InstanceSpecification127", self)

    @property
    def pivot_LanguageExpression261(self):
        return self.__pivot_LanguageExpression261

    @pivot_LanguageExpression261.setter
    def pivot_LanguageExpression261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_LanguageExpression__pivot_LanguageExpression261", None)
        self.__pivot_LanguageExpression261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property260"):
                opp_val = getattr(old_value, "pivot_Property260", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property260", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property260"):
                opp_val = getattr(value, "pivot_Property260", None)
                setattr(value, "pivot_Property260", self)

    @property
    def LanguageExpression(self):
        return self.__LanguageExpression

    @LanguageExpression.setter
    def LanguageExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_LanguageExpression__LanguageExpression", None)
        self.__LanguageExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningConstraint"):
                opp_val = getattr(old_value, "owningConstraint", None)
                if opp_val == self:
                    setattr(old_value, "owningConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningConstraint"):
                opp_val = getattr(value, "owningConstraint", None)
                setattr(value, "owningConstraint", self)

    @property
    def pivot_LanguageExpression204(self):
        return self.__pivot_LanguageExpression204

    @pivot_LanguageExpression204.setter
    def pivot_LanguageExpression204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_LanguageExpression__pivot_LanguageExpression204", None)
        self.__pivot_LanguageExpression204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation203"):
                opp_val = getattr(old_value, "pivot_Operation203", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Operation203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation203"):
                opp_val = getattr(value, "pivot_Operation203", None)
                setattr(value, "pivot_Operation203", self)

class DynamicElement:

    pass
class Vertex:

    pass
class pivot_Pseudostate(Vertex):

    def __init__(self, kind: str, pivot_Pseudostate: "pivot_ConnectionPointReference" = None, pivot_Pseudostate64: "pivot_ConnectionPointReference" = None, ownedConnectionPoints: "pivot_State" = None, ownedConnectionPoints278: "pivot_StateMachine" = None, Pseudostate: "pivot_State" = None, Pseudostate336: "pivot_StateMachine" = None):
        self.kind = kind
        self.pivot_Pseudostate = pivot_Pseudostate
        self.pivot_Pseudostate64 = pivot_Pseudostate64
        self.ownedConnectionPoints = ownedConnectionPoints
        self.ownedConnectionPoints278 = ownedConnectionPoints278
        self.Pseudostate = Pseudostate
        self.Pseudostate336 = Pseudostate336
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

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
    def Pseudostate(self):
        return self.__Pseudostate

    @Pseudostate.setter
    def Pseudostate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Pseudostate__Pseudostate", None)
        self.__Pseudostate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningState"):
                opp_val = getattr(old_value, "owningState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningState"):
                opp_val = getattr(value, "owningState", None)
                if opp_val is None:
                    setattr(value, "owningState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedConnectionPoints(self):
        return self.__ownedConnectionPoints

    @ownedConnectionPoints.setter
    def ownedConnectionPoints(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Pseudostate__ownedConnectionPoints", None)
        self.__ownedConnectionPoints = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State276"):
                opp_val = getattr(old_value, "State276", None)
                if opp_val == self:
                    setattr(old_value, "State276", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State276"):
                opp_val = getattr(value, "State276", None)
                setattr(value, "State276", self)

    @property
    def ownedConnectionPoints278(self):
        return self.__ownedConnectionPoints278

    @ownedConnectionPoints278.setter
    def ownedConnectionPoints278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Pseudostate__ownedConnectionPoints278", None)
        self.__ownedConnectionPoints278 = value
        
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
    def pivot_Pseudostate64(self):
        return self.__pivot_Pseudostate64

    @pivot_Pseudostate64.setter
    def pivot_Pseudostate64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Pseudostate__pivot_Pseudostate64", None)
        self.__pivot_Pseudostate64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_ConnectionPointReference63"):
                opp_val = getattr(old_value, "pivot_ConnectionPointReference63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ConnectionPointReference63"):
                opp_val = getattr(value, "pivot_ConnectionPointReference63", None)
                if opp_val is None:
                    setattr(value, "pivot_ConnectionPointReference63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Pseudostate336(self):
        return self.__Pseudostate336

    @Pseudostate336.setter
    def Pseudostate336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Pseudostate__Pseudostate336", None)
        self.__Pseudostate336 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningStateMachine"):
                opp_val = getattr(old_value, "owningStateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningStateMachine"):
                opp_val = getattr(value, "owningStateMachine", None)
                if opp_val is None:
                    setattr(value, "owningStateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pivot_ConnectionPointReference(Vertex):

    pass
class pivot_OrphanCompletePackage(CompletePackage):

    pass
class pivot_PrimitiveCompletePackage(CompletePackage):

    pass
class Element:

    pass
class pivot_TemplateParameterSubstitution(Element):

    pass
class pivot_Slot(Element):

    pass
class pivot_ProfileApplication(Element):

    def __init__(self, isStrict: str, ProfileApplication: "pivot_Package" = None, ownedProfileApplications: "pivot_Package" = None, ProfileApplication248: "pivot_Profile" = None, profileApplications: "pivot_Profile" = None):
        self.isStrict = isStrict
        self.ProfileApplication = ProfileApplication
        self.ownedProfileApplications = ownedProfileApplications
        self.ProfileApplication248 = ProfileApplication248
        self.profileApplications = profileApplications
        
    @property
    def isStrict(self) -> str:
        return self.__isStrict

    @isStrict.setter
    def isStrict(self, isStrict: str):
        self.__isStrict = isStrict

    @property
    def profileApplications(self):
        return self.__profileApplications

    @profileApplications.setter
    def profileApplications(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ProfileApplication__profileApplications", None)
        self.__profileApplications = value
        
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
    def ProfileApplication248(self):
        return self.__ProfileApplication248

    @ProfileApplication248.setter
    def ProfileApplication248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ProfileApplication__ProfileApplication248", None)
        self.__ProfileApplication248 = value
        
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
    def ProfileApplication(self):
        return self.__ProfileApplication

    @ProfileApplication.setter
    def ProfileApplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ProfileApplication__ProfileApplication", None)
        self.__ProfileApplication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningPackage239"):
                opp_val = getattr(old_value, "owningPackage239", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningPackage239"):
                opp_val = getattr(value, "owningPackage239", None)
                if opp_val is None:
                    setattr(value, "owningPackage239", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedProfileApplications(self):
        return self.__ownedProfileApplications

    @ownedProfileApplications.setter
    def ownedProfileApplications(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ProfileApplication__ownedProfileApplications", None)
        self.__ownedProfileApplications = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package251"):
                opp_val = getattr(old_value, "Package251", None)
                if opp_val == self:
                    setattr(old_value, "Package251", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package251"):
                opp_val = getattr(value, "Package251", None)
                setattr(value, "Package251", self)

class pivot_TemplateSignature(Element):

    pass
class pivot_DynamicProperty(Element):

    def __init__(self, default: str, pivot_DynamicProperty: "pivot_Property" = None, pivot_DynamicProperty89: "pivot_DynamicType" = None):
        self.default = default
        self.pivot_DynamicProperty = pivot_DynamicProperty
        self.pivot_DynamicProperty89 = pivot_DynamicProperty89
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def pivot_DynamicProperty89(self):
        return self.__pivot_DynamicProperty89

    @pivot_DynamicProperty89.setter
    def pivot_DynamicProperty89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_DynamicProperty__pivot_DynamicProperty89", None)
        self.__pivot_DynamicProperty89 = value
        
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
            if hasattr(old_value, "pivot_Property"):
                opp_val = getattr(old_value, "pivot_Property", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property"):
                opp_val = getattr(value, "pivot_Property", None)
                setattr(value, "pivot_Property", self)

class pivot_CompleteEnvironment(Element):

    pass
class pivot_NamedElement(Element, Nameable):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class pivot_TemplateableElement(Element):

    pass
class pivot_MapLiteralPart(Element):

    pass
class pivot_StandardLibrary(Element):

    pass
class pivot_TemplateBinding(Element):

    pass
class pivot_DynamicElement(Element):

    pass
class pivot_Comment(Element):

    def __init__(self, body: str, ownedComments: "pivot_Element" = None, annotatingComments: set["pivot_Element"] = None, Comment95: "pivot_Element" = None, Comment: "pivot_Element" = None):
        self.body = body
        self.ownedComments = ownedComments
        self.annotatingComments = annotatingComments if annotatingComments is not None else set()
        self.Comment95 = Comment95
        self.Comment = Comment
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def annotatingComments(self):
        return self.__annotatingComments

    @annotatingComments.setter
    def annotatingComments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Comment__annotatingComments", None)
        self.__annotatingComments = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    if opp_val == self:
                        setattr(item, "Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    setattr(item, "Element", self)
                    

    @property
    def Comment(self):
        return self.__Comment

    @Comment.setter
    def Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Comment__Comment", None)
        self.__Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "annotatedElements"):
                opp_val = getattr(old_value, "annotatedElements", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "annotatedElements"):
                opp_val = getattr(value, "annotatedElements", None)
                if opp_val is None:
                    setattr(value, "annotatedElements", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Comment95(self):
        return self.__Comment95

    @Comment95.setter
    def Comment95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Comment__Comment95", None)
        self.__Comment95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningElement"):
                opp_val = getattr(old_value, "owningElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningElement"):
                opp_val = getattr(value, "owningElement", None)
                if opp_val is None:
                    setattr(value, "owningElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedComments(self):
        return self.__ownedComments

    @ownedComments.setter
    def ownedComments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Comment__ownedComments", None)
        self.__ownedComments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element34"):
                opp_val = getattr(old_value, "Element34", None)
                if opp_val == self:
                    setattr(old_value, "Element34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element34"):
                opp_val = getattr(value, "Element34", None)
                setattr(value, "Element34", self)

class DataType:

    pass
class pivot_TupleType(DataType):

    pass
class pivot_LambdaType(DataType):

    pass
class pivot_MapType(DataType):

    pass
class pivot_PrimitiveType(DataType):

    pass
class pivot_Enumeration(DataType):

    pass
class pivot_CollectionType(DataType):

    def __init__(self, isNullFree: str, lower: str, upper: str, pivot_CollectionType: "pivot_Type" = None):
        self.isNullFree = isNullFree
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
    def isNullFree(self) -> str:
        return self.__isNullFree

    @isNullFree.setter
    def isNullFree(self, isNullFree: str):
        self.__isNullFree = isNullFree

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

    def __init__(self, pivot_VariableDeclaration: "pivot_Type" = None, pivot_VariableDeclaration407: "pivot_VariableExp" = None):
        self.pivot_VariableDeclaration = pivot_VariableDeclaration
        self.pivot_VariableDeclaration407 = pivot_VariableDeclaration407
        
    @property
    def pivot_VariableDeclaration407(self):
        return self.__pivot_VariableDeclaration407

    @pivot_VariableDeclaration407.setter
    def pivot_VariableDeclaration407(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_VariableDeclaration__pivot_VariableDeclaration407", None)
        self.__pivot_VariableDeclaration407 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_VariableExp"):
                opp_val = getattr(old_value, "pivot_VariableExp", None)
                if opp_val == self:
                    setattr(old_value, "pivot_VariableExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_VariableExp"):
                opp_val = getattr(value, "pivot_VariableExp", None)
                setattr(value, "pivot_VariableExp", self)

    @property
    def pivot_VariableDeclaration(self):
        return self.__pivot_VariableDeclaration

    @pivot_VariableDeclaration.setter
    def pivot_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_VariableDeclaration__pivot_VariableDeclaration", None)
        self.__pivot_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Type405"):
                opp_val = getattr(old_value, "pivot_Type405", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Type405", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Type405"):
                opp_val = getattr(value, "pivot_Type405", None)
                setattr(value, "pivot_Type405", self)

    def validateTypeIsNotInvalid(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateTypeIsNotInvalid method
        pass

class pivot_ShadowPart(TypedElement):

    def __init__(self, pivot_ShadowPart: "pivot_ShadowExp" = None, pivot_ShadowPart295: "pivot_OCLExpression" = None, pivot_ShadowPart298: "pivot_Property" = None):
        self.pivot_ShadowPart = pivot_ShadowPart
        self.pivot_ShadowPart295 = pivot_ShadowPart295
        self.pivot_ShadowPart298 = pivot_ShadowPart298
        
    @property
    def pivot_ShadowPart298(self):
        return self.__pivot_ShadowPart298

    @pivot_ShadowPart298.setter
    def pivot_ShadowPart298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ShadowPart__pivot_ShadowPart298", None)
        self.__pivot_ShadowPart298 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property299"):
                opp_val = getattr(old_value, "pivot_Property299", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property299", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property299"):
                opp_val = getattr(value, "pivot_Property299", None)
                setattr(value, "pivot_Property299", self)

    @property
    def pivot_ShadowPart(self):
        return self.__pivot_ShadowPart

    @pivot_ShadowPart.setter
    def pivot_ShadowPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ShadowPart__pivot_ShadowPart", None)
        self.__pivot_ShadowPart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_ShadowExp"):
                opp_val = getattr(old_value, "pivot_ShadowExp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ShadowExp"):
                opp_val = getattr(value, "pivot_ShadowExp", None)
                if opp_val is None:
                    setattr(value, "pivot_ShadowExp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_ShadowPart295(self):
        return self.__pivot_ShadowPart295

    @pivot_ShadowPart295.setter
    def pivot_ShadowPart295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ShadowPart__pivot_ShadowPart295", None)
        self.__pivot_ShadowPart295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OCLExpression296"):
                opp_val = getattr(old_value, "pivot_OCLExpression296", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression296"):
                opp_val = getattr(value, "pivot_OCLExpression296", None)
                setattr(value, "pivot_OCLExpression296", self)

    def validateTypeIsNotInvalid(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateTypeIsNotInvalid method
        pass

class pivot_ValueSpecification(TypedElement):

    def __init__(self, pivot_ValueSpecification: "pivot_Slot" = None):
        self.pivot_ValueSpecification = pivot_ValueSpecification
        
    @property
    def pivot_ValueSpecification(self):
        return self.__pivot_ValueSpecification

    @pivot_ValueSpecification.setter
    def pivot_ValueSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ValueSpecification__pivot_ValueSpecification", None)
        self.__pivot_ValueSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Slot303"):
                opp_val = getattr(old_value, "pivot_Slot303", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Slot303"):
                opp_val = getattr(value, "pivot_Slot303", None)
                if opp_val is None:
                    setattr(value, "pivot_Slot303", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def booleanValue(self) -> str:
        # TODO: Implement booleanValue method
        pass

    def stringValue(self) -> str:
        # TODO: Implement stringValue method
        pass

    def isNull(self) -> str:
        # TODO: Implement isNull method
        pass

    def unlimitedValue(self) -> str:
        # TODO: Implement unlimitedValue method
        pass

    def isComputable(self) -> str:
        # TODO: Implement isComputable method
        pass

    def integerValue(self) -> str:
        # TODO: Implement integerValue method
        pass

class pivot_Feature(TypedElement):

    def __init__(self, implementation: str, implementationClass: str, isStatic: str):
        self.implementation = implementation
        self.implementationClass = implementationClass
        self.isStatic = isStatic
        
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

    @property
    def isStatic(self) -> str:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: str):
        self.__isStatic = isStatic

    def validateTypeIsNotInvalid(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateTypeIsNotInvalid method
        pass

class pivot_CollectionLiteralPart(TypedElement):

    def __init__(self, pivot_CollectionLiteralPart: "pivot_CollectionLiteralExp" = None):
        self.pivot_CollectionLiteralPart = pivot_CollectionLiteralPart
        
    @property
    def pivot_CollectionLiteralPart(self):
        return self.__pivot_CollectionLiteralPart

    @pivot_CollectionLiteralPart.setter
    def pivot_CollectionLiteralPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_CollectionLiteralPart__pivot_CollectionLiteralPart", None)
        self.__pivot_CollectionLiteralPart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_CollectionLiteralExp"):
                opp_val = getattr(old_value, "pivot_CollectionLiteralExp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_CollectionLiteralExp"):
                opp_val = getattr(value, "pivot_CollectionLiteralExp", None)
                if opp_val is None:
                    setattr(value, "pivot_CollectionLiteralExp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def validateTypeIsNotInvalid(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateTypeIsNotInvalid method
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

    def validateTypeIsEnumerationType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateTypeIsEnumerationType method
        pass

class pivot_TupleLiteralExp(LiteralExp):

    pass
class pivot_MapLiteralExp(LiteralExp):

    pass
class pivot_InvalidLiteralExp(LiteralExp):

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
                    

    def validateSequenceKindIsSequence(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateSequenceKindIsSequence method
        pass

    def validateOrderedSetKindIsOrderedSet(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateOrderedSetKindIsOrderedSet method
        pass

    def validateSetKindIsSet(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateSetKindIsSet method
        pass

    def validateCollectionKindIsConcrete(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateCollectionKindIsConcrete method
        pass

    def validateBagKindIsBag(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateBagKindIsBag method
        pass

class pivot_StereotypeExtender(Element):

    def __init__(self, isRequired: str, StereotypeExtender: "pivot_Class" = None, extenders: "pivot_Class" = None, ownedExtenders: "pivot_Stereotype" = None, StereotypeExtender343: "pivot_Stereotype" = None):
        self.isRequired = isRequired
        self.StereotypeExtender = StereotypeExtender
        self.extenders = extenders
        self.ownedExtenders = ownedExtenders
        self.StereotypeExtender343 = StereotypeExtender343
        
    @property
    def isRequired(self) -> str:
        return self.__isRequired

    @isRequired.setter
    def isRequired(self, isRequired: str):
        self.__isRequired = isRequired

    @property
    def StereotypeExtender(self):
        return self.__StereotypeExtender

    @StereotypeExtender.setter
    def StereotypeExtender(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_StereotypeExtender__StereotypeExtender", None)
        self.__StereotypeExtender = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class"):
                opp_val = getattr(old_value, "class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class"):
                opp_val = getattr(value, "class", None)
                if opp_val is None:
                    setattr(value, "class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StereotypeExtender343(self):
        return self.__StereotypeExtender343

    @StereotypeExtender343.setter
    def StereotypeExtender343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_StereotypeExtender__StereotypeExtender343", None)
        self.__StereotypeExtender343 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningStereotype"):
                opp_val = getattr(old_value, "owningStereotype", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningStereotype"):
                opp_val = getattr(value, "owningStereotype", None)
                if opp_val is None:
                    setattr(value, "owningStereotype", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedExtenders(self):
        return self.__ownedExtenders

    @ownedExtenders.setter
    def ownedExtenders(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_StereotypeExtender__ownedExtenders", None)
        self.__ownedExtenders = value
        
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
    def extenders(self):
        return self.__extenders

    @extenders.setter
    def extenders(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_StereotypeExtender__extenders", None)
        self.__extenders = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class345"):
                opp_val = getattr(old_value, "Class345", None)
                if opp_val == self:
                    setattr(old_value, "Class345", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class345"):
                opp_val = getattr(value, "Class345", None)
                setattr(value, "Class345", self)

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
            if hasattr(old_value, "pivot_OCLExpression24"):
                opp_val = getattr(old_value, "pivot_OCLExpression24", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression24"):
                opp_val = getattr(value, "pivot_OCLExpression24", None)
                setattr(value, "pivot_OCLExpression24", self)

    def validateTypeIsItemType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateTypeIsItemType method
        pass

class OCLExpression:

    pass
class pivot_MessageExp(OCLExpression):

    def __init__(self, pivot_MessageExp174: "pivot_CallOperationAction" = None, pivot_MessageExp177: "pivot_SendSignalAction" = None, pivot_MessageExp179: "pivot_OCLExpression" = None, pivot_MessageExp: set["pivot_OCLExpression"] = None):
        self.pivot_MessageExp174 = pivot_MessageExp174
        self.pivot_MessageExp177 = pivot_MessageExp177
        self.pivot_MessageExp179 = pivot_MessageExp179
        self.pivot_MessageExp = pivot_MessageExp if pivot_MessageExp is not None else set()
        
    @property
    def pivot_MessageExp177(self):
        return self.__pivot_MessageExp177

    @pivot_MessageExp177.setter
    def pivot_MessageExp177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_MessageExp__pivot_MessageExp177", None)
        self.__pivot_MessageExp177 = value
        
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
    def pivot_MessageExp174(self):
        return self.__pivot_MessageExp174

    @pivot_MessageExp174.setter
    def pivot_MessageExp174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_MessageExp__pivot_MessageExp174", None)
        self.__pivot_MessageExp174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_CallOperationAction175"):
                opp_val = getattr(old_value, "pivot_CallOperationAction175", None)
                if opp_val == self:
                    setattr(old_value, "pivot_CallOperationAction175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_CallOperationAction175"):
                opp_val = getattr(value, "pivot_CallOperationAction175", None)
                setattr(value, "pivot_CallOperationAction175", self)

    @property
    def pivot_MessageExp179(self):
        return self.__pivot_MessageExp179

    @pivot_MessageExp179.setter
    def pivot_MessageExp179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_MessageExp__pivot_MessageExp179", None)
        self.__pivot_MessageExp179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OCLExpression180"):
                opp_val = getattr(old_value, "pivot_OCLExpression180", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression180"):
                opp_val = getattr(value, "pivot_OCLExpression180", None)
                setattr(value, "pivot_OCLExpression180", self)

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
                if hasattr(item, "pivot_OCLExpression172"):
                    opp_val = getattr(item, "pivot_OCLExpression172", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_OCLExpression172", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_OCLExpression172"):
                    opp_val = getattr(item, "pivot_OCLExpression172", None)
                    
                    setattr(item, "pivot_OCLExpression172", self)
                    

    def validateTargetIsNotACollection(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateTargetIsNotACollection method
        pass

    def validateOneCallOrOneSend(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateOneCallOrOneSend method
        pass

class pivot_LiteralExp(OCLExpression):

    pass
class pivot_ShadowExp(OCLExpression):

    def __init__(self, value: str, pivot_ShadowExp: set["pivot_ShadowPart"] = None):
        self.value = value
        self.pivot_ShadowExp = pivot_ShadowExp if pivot_ShadowExp is not None else set()
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def pivot_ShadowExp(self):
        return self.__pivot_ShadowExp

    @pivot_ShadowExp.setter
    def pivot_ShadowExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ShadowExp__pivot_ShadowExp", None)
        self.__pivot_ShadowExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_ShadowPart"):
                    opp_val = getattr(item, "pivot_ShadowPart", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_ShadowPart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_ShadowPart"):
                    opp_val = getattr(item, "pivot_ShadowPart", None)
                    
                    setattr(item, "pivot_ShadowPart", self)
                    

    def validateTypeIsNotInvalid(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateTypeIsNotInvalid method
        pass

class pivot_LetExp(OCLExpression):

    def __init__(self, pivot_LetExp: "pivot_OCLExpression" = None, pivot_LetExp148: "pivot_Variable" = None):
        self.pivot_LetExp = pivot_LetExp
        self.pivot_LetExp148 = pivot_LetExp148
        
    @property
    def pivot_LetExp148(self):
        return self.__pivot_LetExp148

    @pivot_LetExp148.setter
    def pivot_LetExp148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_LetExp__pivot_LetExp148", None)
        self.__pivot_LetExp148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Variable149"):
                opp_val = getattr(old_value, "pivot_Variable149", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Variable149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Variable149"):
                opp_val = getattr(value, "pivot_Variable149", None)
                setattr(value, "pivot_Variable149", self)

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
            if hasattr(old_value, "pivot_OCLExpression146"):
                opp_val = getattr(old_value, "pivot_OCLExpression146", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression146"):
                opp_val = getattr(value, "pivot_OCLExpression146", None)
                setattr(value, "pivot_OCLExpression146", self)

    def validateTypeIsNotInvalid(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateTypeIsNotInvalid method
        pass

    def validateTypeIsInType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateTypeIsInType method
        pass

class pivot_TypeExp(OCLExpression, ReferringElement):

    pass
class pivot_StateExp(OCLExpression):

    def __init__(self, pivot_StateExp: "pivot_State" = None):
        self.pivot_StateExp = pivot_StateExp
        
    @property
    def pivot_StateExp(self):
        return self.__pivot_StateExp

    @pivot_StateExp.setter
    def pivot_StateExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_StateExp__pivot_StateExp", None)
        self.__pivot_StateExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_State332"):
                opp_val = getattr(old_value, "pivot_State332", None)
                if opp_val == self:
                    setattr(old_value, "pivot_State332", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_State332"):
                opp_val = getattr(value, "pivot_State332", None)
                setattr(value, "pivot_State332", self)

    def validateTypeIsNotInvalid(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateTypeIsNotInvalid method
        pass

class pivot_UnspecifiedValueExp(OCLExpression):

    pass
class pivot_IfExp(OCLExpression):

    def __init__(self, pivot_IfExp: "pivot_OCLExpression" = None, pivot_IfExp116: "pivot_OCLExpression" = None, pivot_IfExp119: "pivot_OCLExpression" = None):
        self.pivot_IfExp = pivot_IfExp
        self.pivot_IfExp116 = pivot_IfExp116
        self.pivot_IfExp119 = pivot_IfExp119
        
    @property
    def pivot_IfExp119(self):
        return self.__pivot_IfExp119

    @pivot_IfExp119.setter
    def pivot_IfExp119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_IfExp__pivot_IfExp119", None)
        self.__pivot_IfExp119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OCLExpression120"):
                opp_val = getattr(old_value, "pivot_OCLExpression120", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression120"):
                opp_val = getattr(value, "pivot_OCLExpression120", None)
                setattr(value, "pivot_OCLExpression120", self)

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
            if hasattr(old_value, "pivot_OCLExpression114"):
                opp_val = getattr(old_value, "pivot_OCLExpression114", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression114"):
                opp_val = getattr(value, "pivot_OCLExpression114", None)
                setattr(value, "pivot_OCLExpression114", self)

    @property
    def pivot_IfExp116(self):
        return self.__pivot_IfExp116

    @pivot_IfExp116.setter
    def pivot_IfExp116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_IfExp__pivot_IfExp116", None)
        self.__pivot_IfExp116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OCLExpression117"):
                opp_val = getattr(old_value, "pivot_OCLExpression117", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression117"):
                opp_val = getattr(value, "pivot_OCLExpression117", None)
                setattr(value, "pivot_OCLExpression117", self)

    def validateTypeIsNotInvalid(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateTypeIsNotInvalid method
        pass

    def validateConditionTypeIsBoolean(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateConditionTypeIsBoolean method
        pass

class pivot_VariableExp(OCLExpression, ReferringElement):

    def __init__(self, isImplicit: str, pivot_VariableExp: "pivot_VariableDeclaration" = None):
        self.isImplicit = isImplicit
        self.pivot_VariableExp = pivot_VariableExp
        
    @property
    def isImplicit(self) -> str:
        return self.__isImplicit

    @isImplicit.setter
    def isImplicit(self, isImplicit: str):
        self.__isImplicit = isImplicit

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
            if hasattr(old_value, "pivot_VariableDeclaration407"):
                opp_val = getattr(old_value, "pivot_VariableDeclaration407", None)
                if opp_val == self:
                    setattr(old_value, "pivot_VariableDeclaration407", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_VariableDeclaration407"):
                opp_val = getattr(value, "pivot_VariableDeclaration407", None)
                setattr(value, "pivot_VariableDeclaration407", self)

    def validateTypeIsNotInvalid(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateTypeIsNotInvalid method
        pass

class pivot_CallExp(OCLExpression):

    def __init__(self, isImplicit: str, isSafe: str, pivot_CallExp: "pivot_OCLExpression" = None):
        self.isImplicit = isImplicit
        self.isSafe = isSafe
        self.pivot_CallExp = pivot_CallExp
        
    @property
    def isSafe(self) -> str:
        return self.__isSafe

    @isSafe.setter
    def isSafe(self, isSafe: str):
        self.__isSafe = isSafe

    @property
    def isImplicit(self) -> str:
        return self.__isImplicit

    @isImplicit.setter
    def isImplicit(self, isImplicit: str):
        self.__isImplicit = isImplicit

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

    def validateTypeIsNotInvalid(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateTypeIsNotInvalid method
        pass

class PrimitiveLiteralExp:

    pass
class pivot_NumericLiteralExp(PrimitiveLiteralExp):

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

class pivot_NullLiteralExp(PrimitiveLiteralExp):

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

    def validateTypeIsBoolean(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateTypeIsBoolean method
        pass

class CollectionType:

    pass
class pivot_SetType(CollectionType):

    pass
class pivot_OrderedSetType(CollectionType):

    pass
class pivot_SequenceType(CollectionType):

    pass
class pivot_BagType(CollectionType):

    pass
class TemplateableElement:

    pass
class Namespace:

    pass
class pivot_Transition(Namespace):

    def __init__(self, kind: str, Transition: "pivot_Behavior" = None, Transition79: "pivot_Constraint" = None, Transition284: "pivot_Region" = None, Transition389: "pivot_Trigger" = None, owningTransition: "pivot_Behavior" = None, owningTransition375: "pivot_Constraint" = None, owningTransition378: set["pivot_Trigger"] = None, ownedTransitions: "pivot_Region" = None, outgoingTransitions: "pivot_Vertex" = None, incomingTransitions: "pivot_Vertex" = None, Transition409: "pivot_Vertex" = None, Transition411: "pivot_Vertex" = None):
        self.kind = kind
        self.Transition = Transition
        self.Transition79 = Transition79
        self.Transition284 = Transition284
        self.Transition389 = Transition389
        self.owningTransition = owningTransition
        self.owningTransition375 = owningTransition375
        self.owningTransition378 = owningTransition378 if owningTransition378 is not None else set()
        self.ownedTransitions = ownedTransitions
        self.outgoingTransitions = outgoingTransitions
        self.incomingTransitions = incomingTransitions
        self.Transition409 = Transition409
        self.Transition411 = Transition411
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__outgoingTransitions", None)
        self.__outgoingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex383"):
                opp_val = getattr(old_value, "Vertex383", None)
                if opp_val == self:
                    setattr(old_value, "Vertex383", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex383"):
                opp_val = getattr(value, "Vertex383", None)
                setattr(value, "Vertex383", self)

    @property
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__incomingTransitions", None)
        self.__incomingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex385"):
                opp_val = getattr(old_value, "Vertex385", None)
                if opp_val == self:
                    setattr(old_value, "Vertex385", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex385"):
                opp_val = getattr(value, "Vertex385", None)
                setattr(value, "Vertex385", self)

    @property
    def Transition389(self):
        return self.__Transition389

    @Transition389.setter
    def Transition389(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__Transition389", None)
        self.__Transition389 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedTriggers"):
                opp_val = getattr(old_value, "ownedTriggers", None)
                if opp_val == self:
                    setattr(old_value, "ownedTriggers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedTriggers"):
                opp_val = getattr(value, "ownedTriggers", None)
                setattr(value, "ownedTriggers", self)

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
            if hasattr(old_value, "ownedEffect"):
                opp_val = getattr(old_value, "ownedEffect", None)
                if opp_val == self:
                    setattr(old_value, "ownedEffect", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedEffect"):
                opp_val = getattr(value, "ownedEffect", None)
                setattr(value, "ownedEffect", self)

    @property
    def owningTransition375(self):
        return self.__owningTransition375

    @owningTransition375.setter
    def owningTransition375(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__owningTransition375", None)
        self.__owningTransition375 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Constraint376"):
                opp_val = getattr(old_value, "Constraint376", None)
                if opp_val == self:
                    setattr(old_value, "Constraint376", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Constraint376"):
                opp_val = getattr(value, "Constraint376", None)
                setattr(value, "Constraint376", self)

    @property
    def Transition284(self):
        return self.__Transition284

    @Transition284.setter
    def Transition284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__Transition284", None)
        self.__Transition284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningRegion283"):
                opp_val = getattr(old_value, "owningRegion283", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningRegion283"):
                opp_val = getattr(value, "owningRegion283", None)
                if opp_val is None:
                    setattr(value, "owningRegion283", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition79(self):
        return self.__Transition79

    @Transition79.setter
    def Transition79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__Transition79", None)
        self.__Transition79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedGuard"):
                opp_val = getattr(old_value, "ownedGuard", None)
                if opp_val == self:
                    setattr(old_value, "ownedGuard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedGuard"):
                opp_val = getattr(value, "ownedGuard", None)
                setattr(value, "ownedGuard", self)

    @property
    def owningTransition(self):
        return self.__owningTransition

    @owningTransition.setter
    def owningTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__owningTransition", None)
        self.__owningTransition = value
        
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
    def owningTransition378(self):
        return self.__owningTransition378

    @owningTransition378.setter
    def owningTransition378(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__owningTransition378", None)
        self.__owningTransition378 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Trigger379"):
                    opp_val = getattr(item, "Trigger379", None)
                    
                    if opp_val == self:
                        setattr(item, "Trigger379", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trigger379"):
                    opp_val = getattr(item, "Trigger379", None)
                    
                    setattr(item, "Trigger379", self)
                    

    @property
    def Transition411(self):
        return self.__Transition411

    @Transition411.setter
    def Transition411(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__Transition411", None)
        self.__Transition411 = value
        
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
    def ownedTransitions(self):
        return self.__ownedTransitions

    @ownedTransitions.setter
    def ownedTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__ownedTransitions", None)
        self.__ownedTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Region381"):
                opp_val = getattr(old_value, "Region381", None)
                if opp_val == self:
                    setattr(old_value, "Region381", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Region381"):
                opp_val = getattr(value, "Region381", None)
                setattr(value, "Region381", self)

    @property
    def Transition409(self):
        return self.__Transition409

    @Transition409.setter
    def Transition409(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Transition__Transition409", None)
        self.__Transition409 = value
        
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

class pivot_Region(Namespace):

    pass
class pivot_Package(Namespace):

    def __init__(self, URI: str, nsPrefix: str, Package: "pivot_Class" = None, pivot_Package: "pivot_CompletePackage" = None, Package129: "pivot_InstanceSpecification" = None, pivot_Package190: "pivot_Model" = None, pivot_Package229: "pivot_Package" = None, pivot_Package227: set["pivot_Package"] = None, owningPackage: set["pivot_Class"] = None, owningPackage233: set["pivot_InstanceSpecification"] = None, Package237: "pivot_Package" = None, owningPackage236: set["pivot_Package"] = None, owningPackage239: set["pivot_ProfileApplication"] = None, Package242: "pivot_Package" = None, ownedPackages: "pivot_Package" = None, Package251: "pivot_ProfileApplication" = None):
        self.URI = URI
        self.nsPrefix = nsPrefix
        self.Package = Package
        self.pivot_Package = pivot_Package
        self.Package129 = Package129
        self.pivot_Package190 = pivot_Package190
        self.pivot_Package229 = pivot_Package229
        self.pivot_Package227 = pivot_Package227 if pivot_Package227 is not None else set()
        self.owningPackage = owningPackage if owningPackage is not None else set()
        self.owningPackage233 = owningPackage233 if owningPackage233 is not None else set()
        self.Package237 = Package237
        self.owningPackage236 = owningPackage236 if owningPackage236 is not None else set()
        self.owningPackage239 = owningPackage239 if owningPackage239 is not None else set()
        self.Package242 = Package242
        self.ownedPackages = ownedPackages
        self.Package251 = Package251
        
    @property
    def URI(self) -> str:
        return self.__URI

    @URI.setter
    def URI(self, URI: str):
        self.__URI = URI

    @property
    def nsPrefix(self) -> str:
        return self.__nsPrefix

    @nsPrefix.setter
    def nsPrefix(self, nsPrefix: str):
        self.__nsPrefix = nsPrefix

    @property
    def owningPackage(self):
        return self.__owningPackage

    @owningPackage.setter
    def owningPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__owningPackage", None)
        self.__owningPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Class231"):
                    opp_val = getattr(item, "Class231", None)
                    
                    if opp_val == self:
                        setattr(item, "Class231", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Class231"):
                    opp_val = getattr(item, "Class231", None)
                    
                    setattr(item, "Class231", self)
                    

    @property
    def Package251(self):
        return self.__Package251

    @Package251.setter
    def Package251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__Package251", None)
        self.__Package251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedProfileApplications"):
                opp_val = getattr(old_value, "ownedProfileApplications", None)
                if opp_val == self:
                    setattr(old_value, "ownedProfileApplications", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedProfileApplications"):
                opp_val = getattr(value, "ownedProfileApplications", None)
                setattr(value, "ownedProfileApplications", self)

    @property
    def Package237(self):
        return self.__Package237

    @Package237.setter
    def Package237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__Package237", None)
        self.__Package237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningPackage236"):
                opp_val = getattr(old_value, "owningPackage236", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningPackage236"):
                opp_val = getattr(value, "owningPackage236", None)
                if opp_val is None:
                    setattr(value, "owningPackage236", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Package129(self):
        return self.__Package129

    @Package129.setter
    def Package129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__Package129", None)
        self.__Package129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedInstances"):
                opp_val = getattr(old_value, "ownedInstances", None)
                if opp_val == self:
                    setattr(old_value, "ownedInstances", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedInstances"):
                opp_val = getattr(value, "ownedInstances", None)
                setattr(value, "ownedInstances", self)

    @property
    def owningPackage239(self):
        return self.__owningPackage239

    @owningPackage239.setter
    def owningPackage239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__owningPackage239", None)
        self.__owningPackage239 = value if value is not None else set()
        
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
            if hasattr(old_value, "pivot_CompletePackage"):
                opp_val = getattr(old_value, "pivot_CompletePackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_CompletePackage"):
                opp_val = getattr(value, "pivot_CompletePackage", None)
                if opp_val is None:
                    setattr(value, "pivot_CompletePackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owningPackage236(self):
        return self.__owningPackage236

    @owningPackage236.setter
    def owningPackage236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__owningPackage236", None)
        self.__owningPackage236 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package237"):
                    opp_val = getattr(item, "Package237", None)
                    
                    if opp_val == self:
                        setattr(item, "Package237", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package237"):
                    opp_val = getattr(item, "Package237", None)
                    
                    setattr(item, "Package237", self)
                    

    @property
    def Package242(self):
        return self.__Package242

    @Package242.setter
    def Package242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__Package242", None)
        self.__Package242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedPackages"):
                opp_val = getattr(old_value, "ownedPackages", None)
                if opp_val == self:
                    setattr(old_value, "ownedPackages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedPackages"):
                opp_val = getattr(value, "ownedPackages", None)
                setattr(value, "ownedPackages", self)

    @property
    def ownedPackages(self):
        return self.__ownedPackages

    @ownedPackages.setter
    def ownedPackages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__ownedPackages", None)
        self.__ownedPackages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package242"):
                opp_val = getattr(old_value, "Package242", None)
                if opp_val == self:
                    setattr(old_value, "Package242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package242"):
                opp_val = getattr(value, "Package242", None)
                setattr(value, "Package242", self)

    @property
    def owningPackage233(self):
        return self.__owningPackage233

    @owningPackage233.setter
    def owningPackage233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__owningPackage233", None)
        self.__owningPackage233 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InstanceSpecification"):
                    opp_val = getattr(item, "InstanceSpecification", None)
                    
                    if opp_val == self:
                        setattr(item, "InstanceSpecification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InstanceSpecification"):
                    opp_val = getattr(item, "InstanceSpecification", None)
                    
                    setattr(item, "InstanceSpecification", self)
                    

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
            if hasattr(old_value, "ownedClasses"):
                opp_val = getattr(old_value, "ownedClasses", None)
                if opp_val == self:
                    setattr(old_value, "ownedClasses", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedClasses"):
                opp_val = getattr(value, "ownedClasses", None)
                setattr(value, "ownedClasses", self)

    @property
    def pivot_Package227(self):
        return self.__pivot_Package227

    @pivot_Package227.setter
    def pivot_Package227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__pivot_Package227", None)
        self.__pivot_Package227 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Package229"):
                    opp_val = getattr(item, "pivot_Package229", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Package229", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Package229"):
                    opp_val = getattr(item, "pivot_Package229", None)
                    
                    setattr(item, "pivot_Package229", self)
                    

    @property
    def pivot_Package190(self):
        return self.__pivot_Package190

    @pivot_Package190.setter
    def pivot_Package190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__pivot_Package190", None)
        self.__pivot_Package190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Model189"):
                opp_val = getattr(old_value, "pivot_Model189", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Model189"):
                opp_val = getattr(value, "pivot_Model189", None)
                if opp_val is None:
                    setattr(value, "pivot_Model189", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Package229(self):
        return self.__pivot_Package229

    @pivot_Package229.setter
    def pivot_Package229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Package__pivot_Package229", None)
        self.__pivot_Package229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Package227"):
                opp_val = getattr(old_value, "pivot_Package227", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Package227"):
                opp_val = getattr(value, "pivot_Package227", None)
                if opp_val is None:
                    setattr(value, "pivot_Package227", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pivot_State(Vertex, Namespace):

    def __init__(self, isComposite: str, isOrthogonal: str, isSimple: str, isSubmachineState: str, State: "pivot_ConnectionPointReference" = None, State77: "pivot_Constraint" = None, State276: "pivot_Pseudostate" = None, State286: "pivot_Region" = None, owningState312: set["pivot_Trigger"] = None, pivot_State: "pivot_Behavior" = None, pivot_State316: "pivot_Behavior" = None, owningState: set["pivot_Pseudostate"] = None, owningState310: set["pivot_ConnectionPointReference"] = None, pivot_State332: "pivot_StateExp" = None, pivot_State319: "pivot_Behavior" = None, owningState322: set["pivot_Region"] = None, owningState324: "pivot_Constraint" = None, pivot_State328: "pivot_State" = None, pivot_State326: "pivot_State" = None, submachineStates: "pivot_StateMachine" = None, State341: "pivot_StateMachine" = None, State387: "pivot_Trigger" = None):
        self.isComposite = isComposite
        self.isOrthogonal = isOrthogonal
        self.isSimple = isSimple
        self.isSubmachineState = isSubmachineState
        self.State = State
        self.State77 = State77
        self.State276 = State276
        self.State286 = State286
        self.owningState312 = owningState312 if owningState312 is not None else set()
        self.pivot_State = pivot_State
        self.pivot_State316 = pivot_State316
        self.owningState = owningState if owningState is not None else set()
        self.owningState310 = owningState310 if owningState310 is not None else set()
        self.pivot_State332 = pivot_State332
        self.pivot_State319 = pivot_State319
        self.owningState322 = owningState322 if owningState322 is not None else set()
        self.owningState324 = owningState324
        self.pivot_State328 = pivot_State328
        self.pivot_State326 = pivot_State326
        self.submachineStates = submachineStates
        self.State341 = State341
        self.State387 = State387
        
    @property
    def isComposite(self) -> str:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite

    @property
    def isOrthogonal(self) -> str:
        return self.__isOrthogonal

    @isOrthogonal.setter
    def isOrthogonal(self, isOrthogonal: str):
        self.__isOrthogonal = isOrthogonal

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
    def State77(self):
        return self.__State77

    @State77.setter
    def State77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__State77", None)
        self.__State77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedStateInvariant"):
                opp_val = getattr(old_value, "ownedStateInvariant", None)
                if opp_val == self:
                    setattr(old_value, "ownedStateInvariant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedStateInvariant"):
                opp_val = getattr(value, "ownedStateInvariant", None)
                setattr(value, "ownedStateInvariant", self)

    @property
    def pivot_State319(self):
        return self.__pivot_State319

    @pivot_State319.setter
    def pivot_State319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State319", None)
        self.__pivot_State319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Behavior320"):
                opp_val = getattr(old_value, "pivot_Behavior320", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Behavior320", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Behavior320"):
                opp_val = getattr(value, "pivot_Behavior320", None)
                setattr(value, "pivot_Behavior320", self)

    @property
    def pivot_State326(self):
        return self.__pivot_State326

    @pivot_State326.setter
    def pivot_State326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State326", None)
        self.__pivot_State326 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_State328"):
                opp_val = getattr(old_value, "pivot_State328", None)
                if opp_val == self:
                    setattr(old_value, "pivot_State328", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_State328"):
                opp_val = getattr(value, "pivot_State328", None)
                setattr(value, "pivot_State328", self)

    @property
    def State276(self):
        return self.__State276

    @State276.setter
    def State276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__State276", None)
        self.__State276 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedConnectionPoints"):
                opp_val = getattr(old_value, "ownedConnectionPoints", None)
                if opp_val == self:
                    setattr(old_value, "ownedConnectionPoints", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedConnectionPoints"):
                opp_val = getattr(value, "ownedConnectionPoints", None)
                setattr(value, "ownedConnectionPoints", self)

    @property
    def owningState312(self):
        return self.__owningState312

    @owningState312.setter
    def owningState312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__owningState312", None)
        self.__owningState312 = value if value is not None else set()
        
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
            if hasattr(old_value, "ownedConnections"):
                opp_val = getattr(old_value, "ownedConnections", None)
                if opp_val == self:
                    setattr(old_value, "ownedConnections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedConnections"):
                opp_val = getattr(value, "ownedConnections", None)
                setattr(value, "ownedConnections", self)

    @property
    def pivot_State332(self):
        return self.__pivot_State332

    @pivot_State332.setter
    def pivot_State332(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State332", None)
        self.__pivot_State332 = value
        
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
    def owningState(self):
        return self.__owningState

    @owningState.setter
    def owningState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__owningState", None)
        self.__owningState = value if value is not None else set()
        
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
    def State341(self):
        return self.__State341

    @State341.setter
    def State341(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__State341", None)
        self.__State341 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "submachines"):
                opp_val = getattr(old_value, "submachines", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "submachines"):
                opp_val = getattr(value, "submachines", None)
                if opp_val is None:
                    setattr(value, "submachines", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_State328(self):
        return self.__pivot_State328

    @pivot_State328.setter
    def pivot_State328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State328", None)
        self.__pivot_State328 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_State326"):
                opp_val = getattr(old_value, "pivot_State326", None)
                if opp_val == self:
                    setattr(old_value, "pivot_State326", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_State326"):
                opp_val = getattr(value, "pivot_State326", None)
                setattr(value, "pivot_State326", self)

    @property
    def submachineStates(self):
        return self.__submachineStates

    @submachineStates.setter
    def submachineStates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__submachineStates", None)
        self.__submachineStates = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine330"):
                opp_val = getattr(old_value, "StateMachine330", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine330", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine330"):
                opp_val = getattr(value, "StateMachine330", None)
                setattr(value, "StateMachine330", self)

    @property
    def owningState310(self):
        return self.__owningState310

    @owningState310.setter
    def owningState310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__owningState310", None)
        self.__owningState310 = value if value is not None else set()
        
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
    def State286(self):
        return self.__State286

    @State286.setter
    def State286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__State286", None)
        self.__State286 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedRegions"):
                opp_val = getattr(old_value, "ownedRegions", None)
                if opp_val == self:
                    setattr(old_value, "ownedRegions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedRegions"):
                opp_val = getattr(value, "ownedRegions", None)
                setattr(value, "ownedRegions", self)

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
            if hasattr(old_value, "pivot_Behavior314"):
                opp_val = getattr(old_value, "pivot_Behavior314", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Behavior314", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Behavior314"):
                opp_val = getattr(value, "pivot_Behavior314", None)
                setattr(value, "pivot_Behavior314", self)

    @property
    def pivot_State316(self):
        return self.__pivot_State316

    @pivot_State316.setter
    def pivot_State316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__pivot_State316", None)
        self.__pivot_State316 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Behavior317"):
                opp_val = getattr(old_value, "pivot_Behavior317", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Behavior317", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Behavior317"):
                opp_val = getattr(value, "pivot_Behavior317", None)
                setattr(value, "pivot_Behavior317", self)

    @property
    def owningState322(self):
        return self.__owningState322

    @owningState322.setter
    def owningState322(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__owningState322", None)
        self.__owningState322 = value if value is not None else set()
        
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
    def State387(self):
        return self.__State387

    @State387.setter
    def State387(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__State387", None)
        self.__State387 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedDeferrableTriggers"):
                opp_val = getattr(old_value, "ownedDeferrableTriggers", None)
                if opp_val == self:
                    setattr(old_value, "ownedDeferrableTriggers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedDeferrableTriggers"):
                opp_val = getattr(value, "ownedDeferrableTriggers", None)
                setattr(value, "ownedDeferrableTriggers", self)

    @property
    def owningState324(self):
        return self.__owningState324

    @owningState324.setter
    def owningState324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_State__owningState324", None)
        self.__owningState324 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Constraint325"):
                opp_val = getattr(old_value, "Constraint325", None)
                if opp_val == self:
                    setattr(old_value, "Constraint325", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Constraint325"):
                opp_val = getattr(value, "Constraint325", None)
                setattr(value, "Constraint325", self)

class pivot_Model(Namespace):

    def __init__(self, externalURI: str, pivot_Model: "pivot_CompleteModel" = None, pivot_Model186: set["pivot_Import"] = None, pivot_Model189: set["pivot_Package"] = None):
        self.externalURI = externalURI
        self.pivot_Model = pivot_Model
        self.pivot_Model186 = pivot_Model186 if pivot_Model186 is not None else set()
        self.pivot_Model189 = pivot_Model189 if pivot_Model189 is not None else set()
        
    @property
    def externalURI(self) -> str:
        return self.__externalURI

    @externalURI.setter
    def externalURI(self, externalURI: str):
        self.__externalURI = externalURI

    @property
    def pivot_Model189(self):
        return self.__pivot_Model189

    @pivot_Model189.setter
    def pivot_Model189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Model__pivot_Model189", None)
        self.__pivot_Model189 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Package190"):
                    opp_val = getattr(item, "pivot_Package190", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Package190", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Package190"):
                    opp_val = getattr(item, "pivot_Package190", None)
                    
                    setattr(item, "pivot_Package190", self)
                    

    @property
    def pivot_Model186(self):
        return self.__pivot_Model186

    @pivot_Model186.setter
    def pivot_Model186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Model__pivot_Model186", None)
        self.__pivot_Model186 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Import187"):
                    opp_val = getattr(item, "pivot_Import187", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Import187", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Import187"):
                    opp_val = getattr(item, "pivot_Import187", None)
                    
                    setattr(item, "pivot_Import187", self)
                    

    @property
    def pivot_Model(self):
        return self.__pivot_Model

    @pivot_Model.setter
    def pivot_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Model__pivot_Model", None)
        self.__pivot_Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_CompleteModel46"):
                opp_val = getattr(old_value, "pivot_CompleteModel46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_CompleteModel46"):
                opp_val = getattr(value, "pivot_CompleteModel46", None)
                if opp_val is None:
                    setattr(value, "pivot_CompleteModel46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class pivot_TemplateParameter(Type):

    pass
class pivot_Class(Namespace, Type, TemplateableElement):

    def __init__(self, instanceClassName: str, isAbstract: str, isActive: str, isInterface: str, owningClass: set["pivot_Operation"] = None, owningClass17: set["pivot_Property"] = None, ownedClasses: "pivot_Package" = None, pivot_Class22: "pivot_Class" = None, pivot_Class20: set["pivot_Class"] = None, class: set["pivot_StereotypeExtender"] = None, pivot_Class: set["pivot_Behavior"] = None, pivot_Class14: set["pivot_Constraint"] = None, pivot_Class37: "pivot_CompleteClass" = None, pivot_Class84: "pivot_DataType" = None, pivot_Class124: "pivot_InstanceSpecification" = None, Class: "pivot_Operation" = None, Class231: "pivot_Package" = None, Class263: "pivot_Property" = None, Class345: "pivot_StereotypeExtender" = None, pivot_Class351: "pivot_TemplateParameter" = None):
        self.instanceClassName = instanceClassName
        self.isAbstract = isAbstract
        self.isActive = isActive
        self.isInterface = isInterface
        self.owningClass = owningClass if owningClass is not None else set()
        self.owningClass17 = owningClass17 if owningClass17 is not None else set()
        self.ownedClasses = ownedClasses
        self.pivot_Class22 = pivot_Class22
        self.pivot_Class20 = pivot_Class20 if pivot_Class20 is not None else set()
        self.class = class if class is not None else set()
        self.pivot_Class = pivot_Class if pivot_Class is not None else set()
        self.pivot_Class14 = pivot_Class14 if pivot_Class14 is not None else set()
        self.pivot_Class37 = pivot_Class37
        self.pivot_Class84 = pivot_Class84
        self.pivot_Class124 = pivot_Class124
        self.Class = Class
        self.Class231 = Class231
        self.Class263 = Class263
        self.Class345 = Class345
        self.pivot_Class351 = pivot_Class351
        
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
    def instanceClassName(self) -> str:
        return self.__instanceClassName

    @instanceClassName.setter
    def instanceClassName(self, instanceClassName: str):
        self.__instanceClassName = instanceClassName

    @property
    def pivot_Class22(self):
        return self.__pivot_Class22

    @pivot_Class22.setter
    def pivot_Class22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__pivot_Class22", None)
        self.__pivot_Class22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Class20"):
                opp_val = getattr(old_value, "pivot_Class20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Class20"):
                opp_val = getattr(value, "pivot_Class20", None)
                if opp_val is None:
                    setattr(value, "pivot_Class20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Class351(self):
        return self.__pivot_Class351

    @pivot_Class351.setter
    def pivot_Class351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__pivot_Class351", None)
        self.__pivot_Class351 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_TemplateParameter"):
                opp_val = getattr(old_value, "pivot_TemplateParameter", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_TemplateParameter"):
                opp_val = getattr(value, "pivot_TemplateParameter", None)
                if opp_val is None:
                    setattr(value, "pivot_TemplateParameter", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "pivot_Constraint"):
                    opp_val = getattr(item, "pivot_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Constraint"):
                    opp_val = getattr(item, "pivot_Constraint", None)
                    
                    setattr(item, "pivot_Constraint", self)
                    

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedOperations"):
                opp_val = getattr(old_value, "ownedOperations", None)
                if opp_val == self:
                    setattr(old_value, "ownedOperations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedOperations"):
                opp_val = getattr(value, "ownedOperations", None)
                setattr(value, "ownedOperations", self)

    @property
    def Class263(self):
        return self.__Class263

    @Class263.setter
    def Class263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__Class263", None)
        self.__Class263 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedProperties"):
                opp_val = getattr(old_value, "ownedProperties", None)
                if opp_val == self:
                    setattr(old_value, "ownedProperties", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedProperties"):
                opp_val = getattr(value, "ownedProperties", None)
                setattr(value, "ownedProperties", self)

    @property
    def ownedClasses(self):
        return self.__ownedClasses

    @ownedClasses.setter
    def ownedClasses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__ownedClasses", None)
        self.__ownedClasses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package"):
                opp_val = getattr(old_value, "Package", None)
                if opp_val == self:
                    setattr(old_value, "Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package"):
                opp_val = getattr(value, "Package", None)
                setattr(value, "Package", self)

    @property
    def class(self):
        return self.__class

    @class.setter
    def class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__class", None)
        self.__class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StereotypeExtender"):
                    opp_val = getattr(item, "StereotypeExtender", None)
                    
                    if opp_val == self:
                        setattr(item, "StereotypeExtender", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StereotypeExtender"):
                    opp_val = getattr(item, "StereotypeExtender", None)
                    
                    setattr(item, "StereotypeExtender", self)
                    

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
                    

    @property
    def owningClass(self):
        return self.__owningClass

    @owningClass.setter
    def owningClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__owningClass", None)
        self.__owningClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    setattr(item, "Operation", self)
                    

    @property
    def pivot_Class20(self):
        return self.__pivot_Class20

    @pivot_Class20.setter
    def pivot_Class20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__pivot_Class20", None)
        self.__pivot_Class20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Class22"):
                    opp_val = getattr(item, "pivot_Class22", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Class22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Class22"):
                    opp_val = getattr(item, "pivot_Class22", None)
                    
                    setattr(item, "pivot_Class22", self)
                    

    @property
    def pivot_Class37(self):
        return self.__pivot_Class37

    @pivot_Class37.setter
    def pivot_Class37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__pivot_Class37", None)
        self.__pivot_Class37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_CompleteClass"):
                opp_val = getattr(old_value, "pivot_CompleteClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_CompleteClass"):
                opp_val = getattr(value, "pivot_CompleteClass", None)
                if opp_val is None:
                    setattr(value, "pivot_CompleteClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Class345(self):
        return self.__Class345

    @Class345.setter
    def Class345(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__Class345", None)
        self.__Class345 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extenders"):
                opp_val = getattr(old_value, "extenders", None)
                if opp_val == self:
                    setattr(old_value, "extenders", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extenders"):
                opp_val = getattr(value, "extenders", None)
                setattr(value, "extenders", self)

    @property
    def Class231(self):
        return self.__Class231

    @Class231.setter
    def Class231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__Class231", None)
        self.__Class231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningPackage"):
                opp_val = getattr(old_value, "owningPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningPackage"):
                opp_val = getattr(value, "owningPackage", None)
                if opp_val is None:
                    setattr(value, "owningPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owningClass17(self):
        return self.__owningClass17

    @owningClass17.setter
    def owningClass17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__owningClass17", None)
        self.__owningClass17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property18"):
                    opp_val = getattr(item, "Property18", None)
                    
                    if opp_val == self:
                        setattr(item, "Property18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property18"):
                    opp_val = getattr(item, "Property18", None)
                    
                    setattr(item, "Property18", self)
                    

    @property
    def pivot_Class84(self):
        return self.__pivot_Class84

    @pivot_Class84.setter
    def pivot_Class84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__pivot_Class84", None)
        self.__pivot_Class84 = value
        
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
    def pivot_Class124(self):
        return self.__pivot_Class124

    @pivot_Class124.setter
    def pivot_Class124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Class__pivot_Class124", None)
        self.__pivot_Class124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_InstanceSpecification"):
                opp_val = getattr(old_value, "pivot_InstanceSpecification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_InstanceSpecification"):
                opp_val = getattr(value, "pivot_InstanceSpecification", None)
                if opp_val is None:
                    setattr(value, "pivot_InstanceSpecification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def validateUniqueInvariantName(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateUniqueInvariantName method
        pass

class pivot_Operation(Namespace, Feature, TemplateableElement):

    def __init__(self, isValidating: str, isInvalidating: str, isTypeof: str, pivot_Operation: "pivot_CallOperationAction" = None, Operation: "pivot_Class" = None, Operation73: "pivot_Constraint" = None, Operation75: "pivot_Constraint" = None, pivot_Operation182: "pivot_MessageType" = None, owningOperation: set["pivot_Parameter"] = None, owningPostContext: set["pivot_Constraint"] = None, owningPreContext: set["pivot_Constraint"] = None, pivot_Operation203: "pivot_LanguageExpression" = None, pivot_Operation224: "pivot_OperationCallExp" = None, ownedOperations: "pivot_Class" = None, pivot_Operation212: "pivot_Precedence" = None, pivot_Operation215: set["pivot_Type"] = None, pivot_Operation219: "pivot_Operation" = None, pivot_Operation217: set["pivot_Operation"] = None, Operation244: "pivot_Parameter" = None, pivot_Operation246: "pivot_PrimitiveType" = None):
        self.isValidating = isValidating
        self.isInvalidating = isInvalidating
        self.isTypeof = isTypeof
        self.pivot_Operation = pivot_Operation
        self.Operation = Operation
        self.Operation73 = Operation73
        self.Operation75 = Operation75
        self.pivot_Operation182 = pivot_Operation182
        self.owningOperation = owningOperation if owningOperation is not None else set()
        self.owningPostContext = owningPostContext if owningPostContext is not None else set()
        self.owningPreContext = owningPreContext if owningPreContext is not None else set()
        self.pivot_Operation203 = pivot_Operation203
        self.pivot_Operation224 = pivot_Operation224
        self.ownedOperations = ownedOperations
        self.pivot_Operation212 = pivot_Operation212
        self.pivot_Operation215 = pivot_Operation215 if pivot_Operation215 is not None else set()
        self.pivot_Operation219 = pivot_Operation219
        self.pivot_Operation217 = pivot_Operation217 if pivot_Operation217 is not None else set()
        self.Operation244 = Operation244
        self.pivot_Operation246 = pivot_Operation246
        
    @property
    def isTypeof(self) -> str:
        return self.__isTypeof

    @isTypeof.setter
    def isTypeof(self, isTypeof: str):
        self.__isTypeof = isTypeof

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
    def pivot_Operation246(self):
        return self.__pivot_Operation246

    @pivot_Operation246.setter
    def pivot_Operation246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation246", None)
        self.__pivot_Operation246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_PrimitiveType"):
                opp_val = getattr(old_value, "pivot_PrimitiveType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_PrimitiveType"):
                opp_val = getattr(value, "pivot_PrimitiveType", None)
                if opp_val is None:
                    setattr(value, "pivot_PrimitiveType", set([self]))
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
    def ownedOperations(self):
        return self.__ownedOperations

    @ownedOperations.setter
    def ownedOperations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__ownedOperations", None)
        self.__ownedOperations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class"):
                opp_val = getattr(old_value, "Class", None)
                if opp_val == self:
                    setattr(old_value, "Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class"):
                opp_val = getattr(value, "Class", None)
                setattr(value, "Class", self)

    @property
    def Operation75(self):
        return self.__Operation75

    @Operation75.setter
    def Operation75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__Operation75", None)
        self.__Operation75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedPreconditions"):
                opp_val = getattr(old_value, "ownedPreconditions", None)
                if opp_val == self:
                    setattr(old_value, "ownedPreconditions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedPreconditions"):
                opp_val = getattr(value, "ownedPreconditions", None)
                setattr(value, "ownedPreconditions", self)

    @property
    def owningPreContext(self):
        return self.__owningPreContext

    @owningPreContext.setter
    def owningPreContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__owningPreContext", None)
        self.__owningPreContext = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint209"):
                    opp_val = getattr(item, "Constraint209", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint209", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint209"):
                    opp_val = getattr(item, "Constraint209", None)
                    
                    setattr(item, "Constraint209", self)
                    

    @property
    def pivot_Operation224(self):
        return self.__pivot_Operation224

    @pivot_Operation224.setter
    def pivot_Operation224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation224", None)
        self.__pivot_Operation224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OperationCallExp223"):
                opp_val = getattr(old_value, "pivot_OperationCallExp223", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OperationCallExp223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OperationCallExp223"):
                opp_val = getattr(value, "pivot_OperationCallExp223", None)
                setattr(value, "pivot_OperationCallExp223", self)

    @property
    def Operation73(self):
        return self.__Operation73

    @Operation73.setter
    def Operation73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__Operation73", None)
        self.__Operation73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedPostconditions"):
                opp_val = getattr(old_value, "ownedPostconditions", None)
                if opp_val == self:
                    setattr(old_value, "ownedPostconditions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedPostconditions"):
                opp_val = getattr(value, "ownedPostconditions", None)
                setattr(value, "ownedPostconditions", self)

    @property
    def owningOperation(self):
        return self.__owningOperation

    @owningOperation.setter
    def owningOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__owningOperation", None)
        self.__owningOperation = value if value is not None else set()
        
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
    def pivot_Operation215(self):
        return self.__pivot_Operation215

    @pivot_Operation215.setter
    def pivot_Operation215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation215", None)
        self.__pivot_Operation215 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Type216"):
                    opp_val = getattr(item, "pivot_Type216", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Type216", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Type216"):
                    opp_val = getattr(item, "pivot_Type216", None)
                    
                    setattr(item, "pivot_Type216", self)
                    

    @property
    def Operation244(self):
        return self.__Operation244

    @Operation244.setter
    def Operation244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__Operation244", None)
        self.__Operation244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedParameters"):
                opp_val = getattr(old_value, "ownedParameters", None)
                if opp_val == self:
                    setattr(old_value, "ownedParameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedParameters"):
                opp_val = getattr(value, "ownedParameters", None)
                setattr(value, "ownedParameters", self)

    @property
    def pivot_Operation219(self):
        return self.__pivot_Operation219

    @pivot_Operation219.setter
    def pivot_Operation219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation219", None)
        self.__pivot_Operation219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation217"):
                opp_val = getattr(old_value, "pivot_Operation217", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation217"):
                opp_val = getattr(value, "pivot_Operation217", None)
                if opp_val is None:
                    setattr(value, "pivot_Operation217", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Operation203(self):
        return self.__pivot_Operation203

    @pivot_Operation203.setter
    def pivot_Operation203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation203", None)
        self.__pivot_Operation203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_LanguageExpression204"):
                opp_val = getattr(old_value, "pivot_LanguageExpression204", None)
                if opp_val == self:
                    setattr(old_value, "pivot_LanguageExpression204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_LanguageExpression204"):
                opp_val = getattr(value, "pivot_LanguageExpression204", None)
                setattr(value, "pivot_LanguageExpression204", self)

    @property
    def pivot_Operation182(self):
        return self.__pivot_Operation182

    @pivot_Operation182.setter
    def pivot_Operation182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation182", None)
        self.__pivot_Operation182 = value
        
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
    def pivot_Operation212(self):
        return self.__pivot_Operation212

    @pivot_Operation212.setter
    def pivot_Operation212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation212", None)
        self.__pivot_Operation212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Precedence213"):
                opp_val = getattr(old_value, "pivot_Precedence213", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Precedence213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Precedence213"):
                opp_val = getattr(value, "pivot_Precedence213", None)
                setattr(value, "pivot_Precedence213", self)

    @property
    def pivot_Operation217(self):
        return self.__pivot_Operation217

    @pivot_Operation217.setter
    def pivot_Operation217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__pivot_Operation217", None)
        self.__pivot_Operation217 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Operation219"):
                    opp_val = getattr(item, "pivot_Operation219", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Operation219", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Operation219"):
                    opp_val = getattr(item, "pivot_Operation219", None)
                    
                    setattr(item, "pivot_Operation219", self)
                    

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
    def owningPostContext(self):
        return self.__owningPostContext

    @owningPostContext.setter
    def owningPostContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Operation__owningPostContext", None)
        self.__owningPostContext = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint207"):
                    opp_val = getattr(item, "Constraint207", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint207", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint207"):
                    opp_val = getattr(item, "Constraint207", None)
                    
                    setattr(item, "Constraint207", self)
                    

    def validateUniquePreconditionName(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateUniquePreconditionName method
        pass

    def validateUniquePostconditionName(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateUniquePostconditionName method
        pass

    def validateCompatibleReturn(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateCompatibleReturn method
        pass

    def validateLoadableImplementation(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateLoadableImplementation method
        pass

class pivot_OCLExpression(TypedElement):

    pass
class pivot_Element(Visitable):

    def __init__(self, pivot_Element: "pivot_Annotation" = None, pivot_Element5: "pivot_Annotation" = None, Element34: "pivot_Comment" = None, Element: "pivot_Comment" = None, pivot_Element68: "pivot_Constraint" = None, owningElement: set["pivot_Comment"] = None, base: set["pivot_ElementExtension"] = None, Element98: "pivot_ElementExtension" = None, annotatedElements: set["pivot_Comment"] = None, pivot_Element93: "pivot_Element" = None, pivot_Element91: set["pivot_Element"] = None):
        self.pivot_Element = pivot_Element
        self.pivot_Element5 = pivot_Element5
        self.Element34 = Element34
        self.Element = Element
        self.pivot_Element68 = pivot_Element68
        self.owningElement = owningElement if owningElement is not None else set()
        self.base = base if base is not None else set()
        self.Element98 = Element98
        self.annotatedElements = annotatedElements if annotatedElements is not None else set()
        self.pivot_Element93 = pivot_Element93
        self.pivot_Element91 = pivot_Element91 if pivot_Element91 is not None else set()
        
    @property
    def Element98(self):
        return self.__Element98

    @Element98.setter
    def Element98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Element__Element98", None)
        self.__Element98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedExtensions"):
                opp_val = getattr(old_value, "ownedExtensions", None)
                if opp_val == self:
                    setattr(old_value, "ownedExtensions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedExtensions"):
                opp_val = getattr(value, "ownedExtensions", None)
                setattr(value, "ownedExtensions", self)

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
            if hasattr(old_value, "annotatingComments"):
                opp_val = getattr(old_value, "annotatingComments", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "annotatingComments"):
                opp_val = getattr(value, "annotatingComments", None)
                if opp_val is None:
                    setattr(value, "annotatingComments", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owningElement(self):
        return self.__owningElement

    @owningElement.setter
    def owningElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Element__owningElement", None)
        self.__owningElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Comment95"):
                    opp_val = getattr(item, "Comment95", None)
                    
                    if opp_val == self:
                        setattr(item, "Comment95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Comment95"):
                    opp_val = getattr(item, "Comment95", None)
                    
                    setattr(item, "Comment95", self)
                    

    @property
    def pivot_Element93(self):
        return self.__pivot_Element93

    @pivot_Element93.setter
    def pivot_Element93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Element__pivot_Element93", None)
        self.__pivot_Element93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Element91"):
                opp_val = getattr(old_value, "pivot_Element91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Element91"):
                opp_val = getattr(value, "pivot_Element91", None)
                if opp_val is None:
                    setattr(value, "pivot_Element91", set([self]))
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
    def pivot_Element91(self):
        return self.__pivot_Element91

    @pivot_Element91.setter
    def pivot_Element91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Element__pivot_Element91", None)
        self.__pivot_Element91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Element93"):
                    opp_val = getattr(item, "pivot_Element93", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Element93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Element93"):
                    opp_val = getattr(item, "pivot_Element93", None)
                    
                    setattr(item, "pivot_Element93", self)
                    

    @property
    def Element34(self):
        return self.__Element34

    @Element34.setter
    def Element34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Element__Element34", None)
        self.__Element34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedComments"):
                opp_val = getattr(old_value, "ownedComments", None)
                if opp_val == self:
                    setattr(old_value, "ownedComments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedComments"):
                opp_val = getattr(value, "ownedComments", None)
                setattr(value, "ownedComments", self)

    @property
    def pivot_Element68(self):
        return self.__pivot_Element68

    @pivot_Element68.setter
    def pivot_Element68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Element__pivot_Element68", None)
        self.__pivot_Element68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Constraint67"):
                opp_val = getattr(old_value, "pivot_Constraint67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Constraint67"):
                opp_val = getattr(value, "pivot_Constraint67", None)
                if opp_val is None:
                    setattr(value, "pivot_Constraint67", set([self]))
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
    def annotatedElements(self):
        return self.__annotatedElements

    @annotatedElements.setter
    def annotatedElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Element__annotatedElements", None)
        self.__annotatedElements = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    setattr(item, "Comment", self)
                    

    def allOwnedElements(self) -> Element:
        # TODO: Implement allOwnedElements method
        pass

    def getValue(self, propertyName: str, stereotype: Type) -> Element:
        # TODO: Implement getValue method
        pass

class NamedElement:

    pass
class pivot_Detail(NamedElement):

    def __init__(self, values: str, pivot_Detail: "pivot_Annotation" = None):
        self.values = values
        self.pivot_Detail = pivot_Detail
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

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

class pivot_CompleteClass(NamedElement):

    pass
class pivot_TypedElement(NamedElement):

    def __init__(self, isMany: str, isRequired: str, pivot_TypedElement: "pivot_Type" = None):
        self.isMany = isMany
        self.isRequired = isRequired
        self.pivot_TypedElement = pivot_TypedElement
        
    @property
    def isRequired(self) -> str:
        return self.__isRequired

    @isRequired.setter
    def isRequired(self, isRequired: str):
        self.__isRequired = isRequired

    @property
    def isMany(self) -> str:
        return self.__isMany

    @isMany.setter
    def isMany(self, isMany: str):
        self.__isMany = isMany

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
            if hasattr(old_value, "pivot_Type397"):
                opp_val = getattr(old_value, "pivot_Type397", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Type397", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Type397"):
                opp_val = getattr(value, "pivot_Type397", None)
                setattr(value, "pivot_Type397", self)

    def CompatibleBody(self, bodySpecification: ValueSpecification) -> str:
        # TODO: Implement CompatibleBody method
        pass

class pivot_Namespace(NamedElement):

    pass
class pivot_CallOperationAction(NamedElement):

    pass
class pivot_CompleteModel(NamedElement):

    def __init__(self, pivot_CompleteModel46: set["pivot_Model"] = None, pivot_CompleteModel48: "pivot_PrimitiveCompletePackage" = None, CompleteModel: "pivot_CompleteEnvironment" = None, pivot_CompleteModel: "pivot_OrphanCompletePackage" = None, owningCompleteModel: set["pivot_CompletePackage"] = None, ownedCompleteModel: "pivot_CompleteEnvironment" = None, CompleteModel55: "pivot_CompletePackage" = None):
        self.pivot_CompleteModel46 = pivot_CompleteModel46 if pivot_CompleteModel46 is not None else set()
        self.pivot_CompleteModel48 = pivot_CompleteModel48
        self.CompleteModel = CompleteModel
        self.pivot_CompleteModel = pivot_CompleteModel
        self.owningCompleteModel = owningCompleteModel if owningCompleteModel is not None else set()
        self.ownedCompleteModel = ownedCompleteModel
        self.CompleteModel55 = CompleteModel55
        
    @property
    def CompleteModel(self):
        return self.__CompleteModel

    @CompleteModel.setter
    def CompleteModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_CompleteModel__CompleteModel", None)
        self.__CompleteModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningCompleteEnvironment"):
                opp_val = getattr(old_value, "owningCompleteEnvironment", None)
                if opp_val == self:
                    setattr(old_value, "owningCompleteEnvironment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningCompleteEnvironment"):
                opp_val = getattr(value, "owningCompleteEnvironment", None)
                setattr(value, "owningCompleteEnvironment", self)

    @property
    def pivot_CompleteModel46(self):
        return self.__pivot_CompleteModel46

    @pivot_CompleteModel46.setter
    def pivot_CompleteModel46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_CompleteModel__pivot_CompleteModel46", None)
        self.__pivot_CompleteModel46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Model"):
                    opp_val = getattr(item, "pivot_Model", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Model", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Model"):
                    opp_val = getattr(item, "pivot_Model", None)
                    
                    setattr(item, "pivot_Model", self)
                    

    @property
    def CompleteModel55(self):
        return self.__CompleteModel55

    @CompleteModel55.setter
    def CompleteModel55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_CompleteModel__CompleteModel55", None)
        self.__CompleteModel55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedCompletePackages"):
                opp_val = getattr(old_value, "ownedCompletePackages", None)
                if opp_val == self:
                    setattr(old_value, "ownedCompletePackages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedCompletePackages"):
                opp_val = getattr(value, "ownedCompletePackages", None)
                setattr(value, "ownedCompletePackages", self)

    @property
    def owningCompleteModel(self):
        return self.__owningCompleteModel

    @owningCompleteModel.setter
    def owningCompleteModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_CompleteModel__owningCompleteModel", None)
        self.__owningCompleteModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompletePackage43"):
                    opp_val = getattr(item, "CompletePackage43", None)
                    
                    if opp_val == self:
                        setattr(item, "CompletePackage43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompletePackage43"):
                    opp_val = getattr(item, "CompletePackage43", None)
                    
                    setattr(item, "CompletePackage43", self)
                    

    @property
    def pivot_CompleteModel48(self):
        return self.__pivot_CompleteModel48

    @pivot_CompleteModel48.setter
    def pivot_CompleteModel48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_CompleteModel__pivot_CompleteModel48", None)
        self.__pivot_CompleteModel48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_PrimitiveCompletePackage"):
                opp_val = getattr(old_value, "pivot_PrimitiveCompletePackage", None)
                if opp_val == self:
                    setattr(old_value, "pivot_PrimitiveCompletePackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_PrimitiveCompletePackage"):
                opp_val = getattr(value, "pivot_PrimitiveCompletePackage", None)
                setattr(value, "pivot_PrimitiveCompletePackage", self)

    @property
    def pivot_CompleteModel(self):
        return self.__pivot_CompleteModel

    @pivot_CompleteModel.setter
    def pivot_CompleteModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_CompleteModel__pivot_CompleteModel", None)
        self.__pivot_CompleteModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OrphanCompletePackage"):
                opp_val = getattr(old_value, "pivot_OrphanCompletePackage", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OrphanCompletePackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OrphanCompletePackage"):
                opp_val = getattr(value, "pivot_OrphanCompletePackage", None)
                setattr(value, "pivot_OrphanCompletePackage", self)

    @property
    def ownedCompleteModel(self):
        return self.__ownedCompleteModel

    @ownedCompleteModel.setter
    def ownedCompleteModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_CompleteModel__ownedCompleteModel", None)
        self.__ownedCompleteModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteEnvironment"):
                opp_val = getattr(old_value, "CompleteEnvironment", None)
                if opp_val == self:
                    setattr(old_value, "CompleteEnvironment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteEnvironment"):
                opp_val = getattr(value, "CompleteEnvironment", None)
                setattr(value, "CompleteEnvironment", self)

    def getOwnedCompletePackage(self, name: str) -> str:
        # TODO: Implement getOwnedCompletePackage method
        pass

class pivot_Constraint(NamedElement):

    def __init__(self, isCallable: str, pivot_Constraint: "pivot_Class" = None, pivot_Constraint67: set["pivot_Element"] = None, pivot_Constraint70: "pivot_Namespace" = None, owningConstraint: "pivot_LanguageExpression" = None, ownedPostconditions: "pivot_Operation" = None, ownedPreconditions: "pivot_Operation" = None, ownedStateInvariant: "pivot_State" = None, ownedGuard: "pivot_Transition" = None, pivot_Constraint82: "pivot_Constraint" = None, pivot_Constraint80: set["pivot_Constraint"] = None, Constraint: "pivot_LanguageExpression" = None, pivot_Constraint193: "pivot_Namespace" = None, Constraint207: "pivot_Operation" = None, Constraint209: "pivot_Operation" = None, Constraint325: "pivot_State" = None, Constraint376: "pivot_Transition" = None):
        self.isCallable = isCallable
        self.pivot_Constraint = pivot_Constraint
        self.pivot_Constraint67 = pivot_Constraint67 if pivot_Constraint67 is not None else set()
        self.pivot_Constraint70 = pivot_Constraint70
        self.owningConstraint = owningConstraint
        self.ownedPostconditions = ownedPostconditions
        self.ownedPreconditions = ownedPreconditions
        self.ownedStateInvariant = ownedStateInvariant
        self.ownedGuard = ownedGuard
        self.pivot_Constraint82 = pivot_Constraint82
        self.pivot_Constraint80 = pivot_Constraint80 if pivot_Constraint80 is not None else set()
        self.Constraint = Constraint
        self.pivot_Constraint193 = pivot_Constraint193
        self.Constraint207 = Constraint207
        self.Constraint209 = Constraint209
        self.Constraint325 = Constraint325
        self.Constraint376 = Constraint376
        
    @property
    def isCallable(self) -> str:
        return self.__isCallable

    @isCallable.setter
    def isCallable(self, isCallable: str):
        self.__isCallable = isCallable

    @property
    def pivot_Constraint70(self):
        return self.__pivot_Constraint70

    @pivot_Constraint70.setter
    def pivot_Constraint70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint70", None)
        self.__pivot_Constraint70 = value
        
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
    def pivot_Constraint193(self):
        return self.__pivot_Constraint193

    @pivot_Constraint193.setter
    def pivot_Constraint193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint193", None)
        self.__pivot_Constraint193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Namespace192"):
                opp_val = getattr(old_value, "pivot_Namespace192", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Namespace192"):
                opp_val = getattr(value, "pivot_Namespace192", None)
                if opp_val is None:
                    setattr(value, "pivot_Namespace192", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Constraint207(self):
        return self.__Constraint207

    @Constraint207.setter
    def Constraint207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__Constraint207", None)
        self.__Constraint207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningPostContext"):
                opp_val = getattr(old_value, "owningPostContext", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningPostContext"):
                opp_val = getattr(value, "owningPostContext", None)
                if opp_val is None:
                    setattr(value, "owningPostContext", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Constraint(self):
        return self.__pivot_Constraint

    @pivot_Constraint.setter
    def pivot_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint", None)
        self.__pivot_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Class14"):
                opp_val = getattr(old_value, "pivot_Class14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Class14"):
                opp_val = getattr(value, "pivot_Class14", None)
                if opp_val is None:
                    setattr(value, "pivot_Class14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owningConstraint(self):
        return self.__owningConstraint

    @owningConstraint.setter
    def owningConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__owningConstraint", None)
        self.__owningConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LanguageExpression"):
                opp_val = getattr(old_value, "LanguageExpression", None)
                if opp_val == self:
                    setattr(old_value, "LanguageExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LanguageExpression"):
                opp_val = getattr(value, "LanguageExpression", None)
                setattr(value, "LanguageExpression", self)

    @property
    def Constraint209(self):
        return self.__Constraint209

    @Constraint209.setter
    def Constraint209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__Constraint209", None)
        self.__Constraint209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningPreContext"):
                opp_val = getattr(old_value, "owningPreContext", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningPreContext"):
                opp_val = getattr(value, "owningPreContext", None)
                if opp_val is None:
                    setattr(value, "owningPreContext", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Constraint80(self):
        return self.__pivot_Constraint80

    @pivot_Constraint80.setter
    def pivot_Constraint80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint80", None)
        self.__pivot_Constraint80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Constraint82"):
                    opp_val = getattr(item, "pivot_Constraint82", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Constraint82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Constraint82"):
                    opp_val = getattr(item, "pivot_Constraint82", None)
                    
                    setattr(item, "pivot_Constraint82", self)
                    

    @property
    def pivot_Constraint67(self):
        return self.__pivot_Constraint67

    @pivot_Constraint67.setter
    def pivot_Constraint67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint67", None)
        self.__pivot_Constraint67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Element68"):
                    opp_val = getattr(item, "pivot_Element68", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Element68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Element68"):
                    opp_val = getattr(item, "pivot_Element68", None)
                    
                    setattr(item, "pivot_Element68", self)
                    

    @property
    def pivot_Constraint82(self):
        return self.__pivot_Constraint82

    @pivot_Constraint82.setter
    def pivot_Constraint82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__pivot_Constraint82", None)
        self.__pivot_Constraint82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Constraint80"):
                opp_val = getattr(old_value, "pivot_Constraint80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Constraint80"):
                opp_val = getattr(value, "pivot_Constraint80", None)
                if opp_val is None:
                    setattr(value, "pivot_Constraint80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedStateInvariant(self):
        return self.__ownedStateInvariant

    @ownedStateInvariant.setter
    def ownedStateInvariant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__ownedStateInvariant", None)
        self.__ownedStateInvariant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State77"):
                opp_val = getattr(old_value, "State77", None)
                if opp_val == self:
                    setattr(old_value, "State77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State77"):
                opp_val = getattr(value, "State77", None)
                setattr(value, "State77", self)

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
            if hasattr(old_value, "ownedSpecification"):
                opp_val = getattr(old_value, "ownedSpecification", None)
                if opp_val == self:
                    setattr(old_value, "ownedSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedSpecification"):
                opp_val = getattr(value, "ownedSpecification", None)
                setattr(value, "ownedSpecification", self)

    @property
    def ownedPreconditions(self):
        return self.__ownedPreconditions

    @ownedPreconditions.setter
    def ownedPreconditions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__ownedPreconditions", None)
        self.__ownedPreconditions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation75"):
                opp_val = getattr(old_value, "Operation75", None)
                if opp_val == self:
                    setattr(old_value, "Operation75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation75"):
                opp_val = getattr(value, "Operation75", None)
                setattr(value, "Operation75", self)

    @property
    def ownedPostconditions(self):
        return self.__ownedPostconditions

    @ownedPostconditions.setter
    def ownedPostconditions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__ownedPostconditions", None)
        self.__ownedPostconditions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation73"):
                opp_val = getattr(old_value, "Operation73", None)
                if opp_val == self:
                    setattr(old_value, "Operation73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation73"):
                opp_val = getattr(value, "Operation73", None)
                setattr(value, "Operation73", self)

    @property
    def ownedGuard(self):
        return self.__ownedGuard

    @ownedGuard.setter
    def ownedGuard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__ownedGuard", None)
        self.__ownedGuard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition79"):
                opp_val = getattr(old_value, "Transition79", None)
                if opp_val == self:
                    setattr(old_value, "Transition79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition79"):
                opp_val = getattr(value, "Transition79", None)
                setattr(value, "Transition79", self)

    @property
    def Constraint325(self):
        return self.__Constraint325

    @Constraint325.setter
    def Constraint325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__Constraint325", None)
        self.__Constraint325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningState324"):
                opp_val = getattr(old_value, "owningState324", None)
                if opp_val == self:
                    setattr(old_value, "owningState324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningState324"):
                opp_val = getattr(value, "owningState324", None)
                setattr(value, "owningState324", self)

    @property
    def Constraint376(self):
        return self.__Constraint376

    @Constraint376.setter
    def Constraint376(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Constraint__Constraint376", None)
        self.__Constraint376 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningTransition375"):
                opp_val = getattr(old_value, "owningTransition375", None)
                if opp_val == self:
                    setattr(old_value, "owningTransition375", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningTransition375"):
                opp_val = getattr(value, "owningTransition375", None)
                setattr(value, "owningTransition375", self)

    def validateUniqueName(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateUniqueName method
        pass

class pivot_Vertex(NamedElement):

    pass
class pivot_InstanceSpecification(NamedElement):

    pass
class pivot_Import(NamedElement):

    pass
class pivot_Type(NamedElement):

    def __init__(self, pivot_Type: "pivot_CollectionType" = None, pivot_Type86: "pivot_DynamicElement" = None, pivot_Type137: "pivot_LambdaType" = None, pivot_Type140: "pivot_LambdaType" = None, pivot_Type143: "pivot_LambdaType" = None, pivot_Type167: "pivot_MapType" = None, pivot_Type170: "pivot_MapType" = None, pivot_Type201: "pivot_OCLExpression" = None, pivot_Type216: "pivot_Operation" = None, pivot_Type355: "pivot_TemplateParameterSubstitution" = None, pivot_Type395: "pivot_TypeExp" = None, pivot_Type405: "pivot_VariableDeclaration" = None, pivot_Type397: "pivot_TypedElement" = None, pivot_Type416: "pivot_WildcardType" = None, pivot_Type419: "pivot_WildcardType" = None):
        self.pivot_Type = pivot_Type
        self.pivot_Type86 = pivot_Type86
        self.pivot_Type137 = pivot_Type137
        self.pivot_Type140 = pivot_Type140
        self.pivot_Type143 = pivot_Type143
        self.pivot_Type167 = pivot_Type167
        self.pivot_Type170 = pivot_Type170
        self.pivot_Type201 = pivot_Type201
        self.pivot_Type216 = pivot_Type216
        self.pivot_Type355 = pivot_Type355
        self.pivot_Type395 = pivot_Type395
        self.pivot_Type405 = pivot_Type405
        self.pivot_Type397 = pivot_Type397
        self.pivot_Type416 = pivot_Type416
        self.pivot_Type419 = pivot_Type419
        
    @property
    def pivot_Type201(self):
        return self.__pivot_Type201

    @pivot_Type201.setter
    def pivot_Type201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type201", None)
        self.__pivot_Type201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_OCLExpression200"):
                opp_val = getattr(old_value, "pivot_OCLExpression200", None)
                if opp_val == self:
                    setattr(old_value, "pivot_OCLExpression200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_OCLExpression200"):
                opp_val = getattr(value, "pivot_OCLExpression200", None)
                setattr(value, "pivot_OCLExpression200", self)

    @property
    def pivot_Type86(self):
        return self.__pivot_Type86

    @pivot_Type86.setter
    def pivot_Type86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type86", None)
        self.__pivot_Type86 = value
        
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
    def pivot_Type216(self):
        return self.__pivot_Type216

    @pivot_Type216.setter
    def pivot_Type216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type216", None)
        self.__pivot_Type216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation215"):
                opp_val = getattr(old_value, "pivot_Operation215", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation215"):
                opp_val = getattr(value, "pivot_Operation215", None)
                if opp_val is None:
                    setattr(value, "pivot_Operation215", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def pivot_Type167(self):
        return self.__pivot_Type167

    @pivot_Type167.setter
    def pivot_Type167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type167", None)
        self.__pivot_Type167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_MapType"):
                opp_val = getattr(old_value, "pivot_MapType", None)
                if opp_val == self:
                    setattr(old_value, "pivot_MapType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_MapType"):
                opp_val = getattr(value, "pivot_MapType", None)
                setattr(value, "pivot_MapType", self)

    @property
    def pivot_Type170(self):
        return self.__pivot_Type170

    @pivot_Type170.setter
    def pivot_Type170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type170", None)
        self.__pivot_Type170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_MapType169"):
                opp_val = getattr(old_value, "pivot_MapType169", None)
                if opp_val == self:
                    setattr(old_value, "pivot_MapType169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_MapType169"):
                opp_val = getattr(value, "pivot_MapType169", None)
                setattr(value, "pivot_MapType169", self)

    @property
    def pivot_Type419(self):
        return self.__pivot_Type419

    @pivot_Type419.setter
    def pivot_Type419(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type419", None)
        self.__pivot_Type419 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_WildcardType418"):
                opp_val = getattr(old_value, "pivot_WildcardType418", None)
                if opp_val == self:
                    setattr(old_value, "pivot_WildcardType418", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_WildcardType418"):
                opp_val = getattr(value, "pivot_WildcardType418", None)
                setattr(value, "pivot_WildcardType418", self)

    @property
    def pivot_Type405(self):
        return self.__pivot_Type405

    @pivot_Type405.setter
    def pivot_Type405(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type405", None)
        self.__pivot_Type405 = value
        
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

    @property
    def pivot_Type140(self):
        return self.__pivot_Type140

    @pivot_Type140.setter
    def pivot_Type140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type140", None)
        self.__pivot_Type140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_LambdaType139"):
                opp_val = getattr(old_value, "pivot_LambdaType139", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_LambdaType139"):
                opp_val = getattr(value, "pivot_LambdaType139", None)
                if opp_val is None:
                    setattr(value, "pivot_LambdaType139", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Type143(self):
        return self.__pivot_Type143

    @pivot_Type143.setter
    def pivot_Type143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type143", None)
        self.__pivot_Type143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_LambdaType142"):
                opp_val = getattr(old_value, "pivot_LambdaType142", None)
                if opp_val == self:
                    setattr(old_value, "pivot_LambdaType142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_LambdaType142"):
                opp_val = getattr(value, "pivot_LambdaType142", None)
                setattr(value, "pivot_LambdaType142", self)

    @property
    def pivot_Type397(self):
        return self.__pivot_Type397

    @pivot_Type397.setter
    def pivot_Type397(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type397", None)
        self.__pivot_Type397 = value
        
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
    def pivot_Type395(self):
        return self.__pivot_Type395

    @pivot_Type395.setter
    def pivot_Type395(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type395", None)
        self.__pivot_Type395 = value
        
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
    def pivot_Type355(self):
        return self.__pivot_Type355

    @pivot_Type355.setter
    def pivot_Type355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type355", None)
        self.__pivot_Type355 = value
        
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
    def pivot_Type416(self):
        return self.__pivot_Type416

    @pivot_Type416.setter
    def pivot_Type416(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Type__pivot_Type416", None)
        self.__pivot_Type416 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_WildcardType415"):
                opp_val = getattr(old_value, "pivot_WildcardType415", None)
                if opp_val == self:
                    setattr(old_value, "pivot_WildcardType415", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_WildcardType415"):
                opp_val = getattr(value, "pivot_WildcardType415", None)
                setattr(value, "pivot_WildcardType415", self)

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

    def isTemplateParameter(self) -> str:
        # TODO: Implement isTemplateParameter method
        pass

    def flattenedType(self) -> Type:
        # TODO: Implement flattenedType method
        pass

    def isClass(self) -> Class:
        # TODO: Implement isClass method
        pass

    def specializeIn(self, expr: CallExp, selfType: Type) -> Type:
        # TODO: Implement specializeIn method
        pass

class pivot_Trigger(NamedElement):

    pass
class pivot_SendSignalAction(NamedElement):

    pass
class pivot_Precedence(NamedElement):

    def __init__(self, associativity: str, order: str, pivot_Precedence: "pivot_Library" = None, pivot_Precedence213: "pivot_Operation" = None):
        self.associativity = associativity
        self.order = order
        self.pivot_Precedence = pivot_Precedence
        self.pivot_Precedence213 = pivot_Precedence213
        
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
    def pivot_Precedence213(self):
        return self.__pivot_Precedence213

    @pivot_Precedence213.setter
    def pivot_Precedence213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Precedence__pivot_Precedence213", None)
        self.__pivot_Precedence213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Operation212"):
                opp_val = getattr(old_value, "pivot_Operation212", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Operation212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Operation212"):
                opp_val = getattr(value, "pivot_Operation212", None)
                setattr(value, "pivot_Operation212", self)

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

class pivot_CompletePackage(NamedElement):

    def __init__(self, CompletePackage: "pivot_CompleteClass" = None, CompletePackage43: "pivot_CompleteModel" = None, owningCompletePackage: set["pivot_CompleteClass"] = None, CompletePackage53: "pivot_CompletePackage" = None, owningCompletePackage52: set["pivot_CompletePackage"] = None, ownedCompletePackages: "pivot_CompleteModel" = None, CompletePackage59: "pivot_CompletePackage" = None, ownedCompletePackages58: "pivot_CompletePackage" = None, pivot_CompletePackage: set["pivot_Package"] = None):
        self.CompletePackage = CompletePackage
        self.CompletePackage43 = CompletePackage43
        self.owningCompletePackage = owningCompletePackage if owningCompletePackage is not None else set()
        self.CompletePackage53 = CompletePackage53
        self.owningCompletePackage52 = owningCompletePackage52 if owningCompletePackage52 is not None else set()
        self.ownedCompletePackages = ownedCompletePackages
        self.CompletePackage59 = CompletePackage59
        self.ownedCompletePackages58 = ownedCompletePackages58
        self.pivot_CompletePackage = pivot_CompletePackage if pivot_CompletePackage is not None else set()
        
    @property
    def CompletePackage59(self):
        return self.__CompletePackage59

    @CompletePackage59.setter
    def CompletePackage59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_CompletePackage__CompletePackage59", None)
        self.__CompletePackage59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedCompletePackages58"):
                opp_val = getattr(old_value, "ownedCompletePackages58", None)
                if opp_val == self:
                    setattr(old_value, "ownedCompletePackages58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedCompletePackages58"):
                opp_val = getattr(value, "ownedCompletePackages58", None)
                setattr(value, "ownedCompletePackages58", self)

    @property
    def CompletePackage43(self):
        return self.__CompletePackage43

    @CompletePackage43.setter
    def CompletePackage43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_CompletePackage__CompletePackage43", None)
        self.__CompletePackage43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningCompleteModel"):
                opp_val = getattr(old_value, "owningCompleteModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningCompleteModel"):
                opp_val = getattr(value, "owningCompleteModel", None)
                if opp_val is None:
                    setattr(value, "owningCompleteModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompletePackage53(self):
        return self.__CompletePackage53

    @CompletePackage53.setter
    def CompletePackage53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_CompletePackage__CompletePackage53", None)
        self.__CompletePackage53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningCompletePackage52"):
                opp_val = getattr(old_value, "owningCompletePackage52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningCompletePackage52"):
                opp_val = getattr(value, "owningCompletePackage52", None)
                if opp_val is None:
                    setattr(value, "owningCompletePackage52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owningCompletePackage(self):
        return self.__owningCompletePackage

    @owningCompletePackage.setter
    def owningCompletePackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_CompletePackage__owningCompletePackage", None)
        self.__owningCompletePackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteClass"):
                    opp_val = getattr(item, "CompleteClass", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteClass"):
                    opp_val = getattr(item, "CompleteClass", None)
                    
                    setattr(item, "CompleteClass", self)
                    

    @property
    def pivot_CompletePackage(self):
        return self.__pivot_CompletePackage

    @pivot_CompletePackage.setter
    def pivot_CompletePackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_CompletePackage__pivot_CompletePackage", None)
        self.__pivot_CompletePackage = value if value is not None else set()
        
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
    def CompletePackage(self):
        return self.__CompletePackage

    @CompletePackage.setter
    def CompletePackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_CompletePackage__CompletePackage", None)
        self.__CompletePackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedCompleteClasses"):
                opp_val = getattr(old_value, "ownedCompleteClasses", None)
                if opp_val == self:
                    setattr(old_value, "ownedCompleteClasses", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedCompleteClasses"):
                opp_val = getattr(value, "ownedCompleteClasses", None)
                setattr(value, "ownedCompleteClasses", self)

    @property
    def owningCompletePackage52(self):
        return self.__owningCompletePackage52

    @owningCompletePackage52.setter
    def owningCompletePackage52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_CompletePackage__owningCompletePackage52", None)
        self.__owningCompletePackage52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompletePackage53"):
                    opp_val = getattr(item, "CompletePackage53", None)
                    
                    if opp_val == self:
                        setattr(item, "CompletePackage53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompletePackage53"):
                    opp_val = getattr(item, "CompletePackage53", None)
                    
                    setattr(item, "CompletePackage53", self)
                    

    @property
    def ownedCompletePackages(self):
        return self.__ownedCompletePackages

    @ownedCompletePackages.setter
    def ownedCompletePackages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_CompletePackage__ownedCompletePackages", None)
        self.__ownedCompletePackages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteModel55"):
                opp_val = getattr(old_value, "CompleteModel55", None)
                if opp_val == self:
                    setattr(old_value, "CompleteModel55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteModel55"):
                opp_val = getattr(value, "CompleteModel55", None)
                setattr(value, "CompleteModel55", self)

    @property
    def ownedCompletePackages58(self):
        return self.__ownedCompletePackages58

    @ownedCompletePackages58.setter
    def ownedCompletePackages58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_CompletePackage__ownedCompletePackages58", None)
        self.__ownedCompletePackages58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompletePackage59"):
                opp_val = getattr(old_value, "CompletePackage59", None)
                if opp_val == self:
                    setattr(old_value, "CompletePackage59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompletePackage59"):
                opp_val = getattr(value, "CompletePackage59", None)
                setattr(value, "CompletePackage59", self)

    def getOwnedCompleteClass(self, name: str) -> str:
        # TODO: Implement getOwnedCompleteClass method
        pass

class pivot_Annotation(NamedElement):

    pass
class NavigationCallExp:

    pass
class pivot_OppositePropertyCallExp(NavigationCallExp):

    pass
class pivot_PropertyCallExp(ReferringElement, NavigationCallExp):

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
            if hasattr(old_value, "pivot_Property274"):
                opp_val = getattr(old_value, "pivot_Property274", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property274", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property274"):
                opp_val = getattr(value, "pivot_Property274", None)
                setattr(value, "pivot_Property274", self)

    def validateSafeSourceCanBeNull(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateSafeSourceCanBeNull method
        pass

    def validateNonStaticSourceTypeIsConformant(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateNonStaticSourceTypeIsConformant method
        pass

    def getSpecializedReferredPropertyOwningType(self) -> Class:
        # TODO: Implement getSpecializedReferredPropertyOwningType method
        pass

    def validateUnsafeSourceCanNotBeNull(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement validateUnsafeSourceCanNotBeNull method
        pass

    def getSpecializedReferredPropertyType(self) -> Class:
        # TODO: Implement getSpecializedReferredPropertyType method
        pass

    def validateCompatibleResultType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateCompatibleResultType method
        pass

class pivot_AssociationClassCallExp(NavigationCallExp):

    pass
class pivot_Property(Feature):

    def __init__(self, defaultValue: str, defaultValueString: str, isComposite: str, isDerived: str, isID: str, isImplicit: str, isReadOnly: str, isResolveProxies: str, isTransient: str, isUnsettable: str, isVolatile: str, Property: "pivot_AssociationClass" = None, Property18: "pivot_Class" = None, pivot_Property: "pivot_DynamicProperty" = None, pivot_Property195: "pivot_NavigationCallExp" = None, pivot_Property226: "pivot_OppositePropertyCallExp" = None, pivot_Property255: "pivot_Property" = None, pivot_Property253: set["pivot_Property"] = None, pivot_Property258: "pivot_Property" = None, pivot_Property256: "pivot_Property" = None, pivot_Property260: "pivot_LanguageExpression" = None, unownedAttributes: "pivot_AssociationClass" = None, ownedProperties: "pivot_Class" = None, pivot_Property266: "pivot_Property" = None, pivot_Property264: set["pivot_Property"] = None, pivot_Property269: "pivot_Property" = None, pivot_Property267: "pivot_Property" = None, pivot_Property272: "pivot_Property" = None, pivot_Property270: set["pivot_Property"] = None, pivot_Property274: "pivot_PropertyCallExp" = None, pivot_Property299: "pivot_ShadowPart" = None, pivot_Property301: "pivot_Slot" = None):
        self.defaultValue = defaultValue
        self.defaultValueString = defaultValueString
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isID = isID
        self.isImplicit = isImplicit
        self.isReadOnly = isReadOnly
        self.isResolveProxies = isResolveProxies
        self.isTransient = isTransient
        self.isUnsettable = isUnsettable
        self.isVolatile = isVolatile
        self.Property = Property
        self.Property18 = Property18
        self.pivot_Property = pivot_Property
        self.pivot_Property195 = pivot_Property195
        self.pivot_Property226 = pivot_Property226
        self.pivot_Property255 = pivot_Property255
        self.pivot_Property253 = pivot_Property253 if pivot_Property253 is not None else set()
        self.pivot_Property258 = pivot_Property258
        self.pivot_Property256 = pivot_Property256
        self.pivot_Property260 = pivot_Property260
        self.unownedAttributes = unownedAttributes
        self.ownedProperties = ownedProperties
        self.pivot_Property266 = pivot_Property266
        self.pivot_Property264 = pivot_Property264 if pivot_Property264 is not None else set()
        self.pivot_Property269 = pivot_Property269
        self.pivot_Property267 = pivot_Property267
        self.pivot_Property272 = pivot_Property272
        self.pivot_Property270 = pivot_Property270 if pivot_Property270 is not None else set()
        self.pivot_Property274 = pivot_Property274
        self.pivot_Property299 = pivot_Property299
        self.pivot_Property301 = pivot_Property301
        
    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

    @property
    def defaultValueString(self) -> str:
        return self.__defaultValueString

    @defaultValueString.setter
    def defaultValueString(self, defaultValueString: str):
        self.__defaultValueString = defaultValueString

    @property
    def isID(self) -> str:
        return self.__isID

    @isID.setter
    def isID(self, isID: str):
        self.__isID = isID

    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def isResolveProxies(self) -> str:
        return self.__isResolveProxies

    @isResolveProxies.setter
    def isResolveProxies(self, isResolveProxies: str):
        self.__isResolveProxies = isResolveProxies

    @property
    def isVolatile(self) -> str:
        return self.__isVolatile

    @isVolatile.setter
    def isVolatile(self, isVolatile: str):
        self.__isVolatile = isVolatile

    @property
    def isComposite(self) -> str:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite

    @property
    def isTransient(self) -> str:
        return self.__isTransient

    @isTransient.setter
    def isTransient(self, isTransient: str):
        self.__isTransient = isTransient

    @property
    def isUnsettable(self) -> str:
        return self.__isUnsettable

    @isUnsettable.setter
    def isUnsettable(self, isUnsettable: str):
        self.__isUnsettable = isUnsettable

    @property
    def isImplicit(self) -> str:
        return self.__isImplicit

    @isImplicit.setter
    def isImplicit(self, isImplicit: str):
        self.__isImplicit = isImplicit

    @property
    def pivot_Property264(self):
        return self.__pivot_Property264

    @pivot_Property264.setter
    def pivot_Property264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property264", None)
        self.__pivot_Property264 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Property266"):
                    opp_val = getattr(item, "pivot_Property266", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Property266", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Property266"):
                    opp_val = getattr(item, "pivot_Property266", None)
                    
                    setattr(item, "pivot_Property266", self)
                    

    @property
    def pivot_Property260(self):
        return self.__pivot_Property260

    @pivot_Property260.setter
    def pivot_Property260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property260", None)
        self.__pivot_Property260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_LanguageExpression261"):
                opp_val = getattr(old_value, "pivot_LanguageExpression261", None)
                if opp_val == self:
                    setattr(old_value, "pivot_LanguageExpression261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_LanguageExpression261"):
                opp_val = getattr(value, "pivot_LanguageExpression261", None)
                setattr(value, "pivot_LanguageExpression261", self)

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
    def pivot_Property226(self):
        return self.__pivot_Property226

    @pivot_Property226.setter
    def pivot_Property226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property226", None)
        self.__pivot_Property226 = value
        
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
    def pivot_Property258(self):
        return self.__pivot_Property258

    @pivot_Property258.setter
    def pivot_Property258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property258", None)
        self.__pivot_Property258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property256"):
                opp_val = getattr(old_value, "pivot_Property256", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property256"):
                opp_val = getattr(value, "pivot_Property256", None)
                setattr(value, "pivot_Property256", self)

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
    def pivot_Property266(self):
        return self.__pivot_Property266

    @pivot_Property266.setter
    def pivot_Property266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property266", None)
        self.__pivot_Property266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property264"):
                opp_val = getattr(old_value, "pivot_Property264", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property264"):
                opp_val = getattr(value, "pivot_Property264", None)
                if opp_val is None:
                    setattr(value, "pivot_Property264", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Property267(self):
        return self.__pivot_Property267

    @pivot_Property267.setter
    def pivot_Property267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property267", None)
        self.__pivot_Property267 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property269"):
                opp_val = getattr(old_value, "pivot_Property269", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property269", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property269"):
                opp_val = getattr(value, "pivot_Property269", None)
                setattr(value, "pivot_Property269", self)

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
    def pivot_Property274(self):
        return self.__pivot_Property274

    @pivot_Property274.setter
    def pivot_Property274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property274", None)
        self.__pivot_Property274 = value
        
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
    def ownedProperties(self):
        return self.__ownedProperties

    @ownedProperties.setter
    def ownedProperties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__ownedProperties", None)
        self.__ownedProperties = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class263"):
                opp_val = getattr(old_value, "Class263", None)
                if opp_val == self:
                    setattr(old_value, "Class263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class263"):
                opp_val = getattr(value, "Class263", None)
                setattr(value, "Class263", self)

    @property
    def pivot_Property253(self):
        return self.__pivot_Property253

    @pivot_Property253.setter
    def pivot_Property253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property253", None)
        self.__pivot_Property253 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Property255"):
                    opp_val = getattr(item, "pivot_Property255", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Property255", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Property255"):
                    opp_val = getattr(item, "pivot_Property255", None)
                    
                    setattr(item, "pivot_Property255", self)
                    

    @property
    def pivot_Property272(self):
        return self.__pivot_Property272

    @pivot_Property272.setter
    def pivot_Property272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property272", None)
        self.__pivot_Property272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property270"):
                opp_val = getattr(old_value, "pivot_Property270", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property270"):
                opp_val = getattr(value, "pivot_Property270", None)
                if opp_val is None:
                    setattr(value, "pivot_Property270", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Property256(self):
        return self.__pivot_Property256

    @pivot_Property256.setter
    def pivot_Property256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property256", None)
        self.__pivot_Property256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property258"):
                opp_val = getattr(old_value, "pivot_Property258", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property258"):
                opp_val = getattr(value, "pivot_Property258", None)
                setattr(value, "pivot_Property258", self)

    @property
    def Property18(self):
        return self.__Property18

    @Property18.setter
    def Property18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__Property18", None)
        self.__Property18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningClass17"):
                opp_val = getattr(old_value, "owningClass17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningClass17"):
                opp_val = getattr(value, "owningClass17", None)
                if opp_val is None:
                    setattr(value, "owningClass17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pivot_Property301(self):
        return self.__pivot_Property301

    @pivot_Property301.setter
    def pivot_Property301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property301", None)
        self.__pivot_Property301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Slot"):
                opp_val = getattr(old_value, "pivot_Slot", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Slot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Slot"):
                opp_val = getattr(value, "pivot_Slot", None)
                setattr(value, "pivot_Slot", self)

    @property
    def pivot_Property270(self):
        return self.__pivot_Property270

    @pivot_Property270.setter
    def pivot_Property270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property270", None)
        self.__pivot_Property270 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pivot_Property272"):
                    opp_val = getattr(item, "pivot_Property272", None)
                    
                    if opp_val == self:
                        setattr(item, "pivot_Property272", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pivot_Property272"):
                    opp_val = getattr(item, "pivot_Property272", None)
                    
                    setattr(item, "pivot_Property272", self)
                    

    @property
    def pivot_Property299(self):
        return self.__pivot_Property299

    @pivot_Property299.setter
    def pivot_Property299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property299", None)
        self.__pivot_Property299 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_ShadowPart298"):
                opp_val = getattr(old_value, "pivot_ShadowPart298", None)
                if opp_val == self:
                    setattr(old_value, "pivot_ShadowPart298", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_ShadowPart298"):
                opp_val = getattr(value, "pivot_ShadowPart298", None)
                setattr(value, "pivot_ShadowPart298", self)

    @property
    def unownedAttributes(self):
        return self.__unownedAttributes

    @unownedAttributes.setter
    def unownedAttributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__unownedAttributes", None)
        self.__unownedAttributes = value
        
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
    def pivot_Property269(self):
        return self.__pivot_Property269

    @pivot_Property269.setter
    def pivot_Property269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property269", None)
        self.__pivot_Property269 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property267"):
                opp_val = getattr(old_value, "pivot_Property267", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Property267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property267"):
                opp_val = getattr(value, "pivot_Property267", None)
                setattr(value, "pivot_Property267", self)

    @property
    def pivot_Property255(self):
        return self.__pivot_Property255

    @pivot_Property255.setter
    def pivot_Property255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_Property__pivot_Property255", None)
        self.__pivot_Property255 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pivot_Property253"):
                opp_val = getattr(old_value, "pivot_Property253", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Property253"):
                opp_val = getattr(value, "pivot_Property253", None)
                if opp_val is None:
                    setattr(value, "pivot_Property253", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def validateCompatibleDefaultExpression(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement validateCompatibleDefaultExpression method
        pass

    def isAttribute(self, p: str) -> str:
        # TODO: Implement isAttribute method
        pass

class Class:

    pass
class pivot_VoidType(Class):

    pass
class pivot_AssociationClass(Class):

    pass
class pivot_Stereotype(Class):

    pass
class pivot_InvalidType(Class):

    pass
class pivot_SelfType(Class):

    def __init__(self):
        
    def specializeIn(self, selfType: Type, expr: CallExp) -> Type:
        # TODO: Implement specializeIn method
        pass

class pivot_MessageType(Class):

    pass
class pivot_Behavior(Class):

    pass
class pivot_Signal(Class):

    pass
class pivot_DataType(Class):

    def __init__(self, isSerializable: str, pivot_DataType: "pivot_Class" = None):
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
            if hasattr(old_value, "pivot_Class84"):
                opp_val = getattr(old_value, "pivot_Class84", None)
                if opp_val == self:
                    setattr(old_value, "pivot_Class84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pivot_Class84"):
                opp_val = getattr(value, "pivot_Class84", None)
                setattr(value, "pivot_Class84", self)

class pivot_WildcardType(Class):

    pass
class pivot_DynamicType(DynamicElement, Class):

    pass
class pivot_ElementExtension(Class):

    def __init__(self, isApplied: str, isRequired: str, ElementExtension: "pivot_Element" = None, ownedExtensions: "pivot_Element" = None, pivot_ElementExtension: "pivot_Stereotype" = None):
        self.isApplied = isApplied
        self.isRequired = isRequired
        self.ElementExtension = ElementExtension
        self.ownedExtensions = ownedExtensions
        self.pivot_ElementExtension = pivot_ElementExtension
        
    @property
    def isApplied(self) -> str:
        return self.__isApplied

    @isApplied.setter
    def isApplied(self, isApplied: str):
        self.__isApplied = isApplied

    @property
    def isRequired(self) -> str:
        return self.__isRequired

    @isRequired.setter
    def isRequired(self, isRequired: str):
        self.__isRequired = isRequired

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
    def ownedExtensions(self):
        return self.__ownedExtensions

    @ownedExtensions.setter
    def ownedExtensions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pivot_ElementExtension__ownedExtensions", None)
        self.__ownedExtensions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element98"):
                opp_val = getattr(old_value, "Element98", None)
                if opp_val == self:
                    setattr(old_value, "Element98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element98"):
                opp_val = getattr(value, "Element98", None)
                setattr(value, "Element98", self)

class pivot_AnyType(Class):

    pass