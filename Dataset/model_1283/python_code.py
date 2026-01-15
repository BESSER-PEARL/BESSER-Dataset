from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AdditiveOperator(Enum):
    plus = "plus"
    minus = "minus"
class UndefinedLiteral(Enum):
    NULL = "NULL"
    INVALID = "INVALID"
class IterationType(Enum):
    default = "default"
    shuffle = "shuffle"
class UnaryOperator(Enum):
    plus = "plus"
    minus = "minus"
    not = "not"
class MultiplicativeOperator(Enum):
    multi = "multi"
    div = "div"
class RelationalOperator(Enum):
    equal = "equal"
    less = "less"
    lessOrEq = "lessOrEq"
    greater = "greater"
    greaterOrEq = "greaterOrEq"
    notEqual = "notEqual"
class TypedModelAction(Enum):
    normal = "normal"
    readOnly = "readOnly"
    viewOnly = "viewOnly"
    createOnly = "createOnly"
    transient = "transient"
class OrderType(Enum):
    default = "default"
    sequential = "sequential"
    parallel = "parallel"
class SectionType(Enum):
    LHS = "LHS"
    RHS = "RHS"
    NAC = "NAC"
    PAC = "PAC"
    PRE = "PRE"
    POST = "POST"
class PredefinedVariable(Enum):
    this = "this"
    id = "id"
class OperationSeparator(Enum):
    dot = "dot"
    arrow = "arrow"
class IteratorType(Enum):
    forAll = "forAll"
    exists = "exists"
    select = "select"
    reject = "reject"
    collect = "collect"
    closure = "closure"
class RepetitionType(Enum):
    allMatches = "allMatches"
    first = "first"
    randomOne = "randomOne"
class ScopeType(Enum):
    all = "all"
    staticRandom = "staticRandom"
    dynamicRandom = "dynamicRandom"
class BooleanOperator(Enum):
    and = "and"
    or = "or"
    not = "not"
    implies = "implies"


############################################
# Definition of Classes
############################################

class morel_EAttribute:

    pass
class PrimitiveConstraint:

    pass
class morel_ValueRangeConstraint(PrimitiveConstraint):

    pass
class morel_MultiValueConstraint(PrimitiveConstraint):

    pass
class morel_PrimitiveConstraint(ABC):

    pass
class AdditionalConstraint:

    pass
class morel_AllDifferentConstraint(AdditionalConstraint):

    pass
class morel_OrderConstraint(AdditionalConstraint):

    pass
class morel_Executable(ABC):

    def __init__(self, active: bool, parameters: str, morel_Executable: set["morel_PrimitiveVariable"] = None):
        self.active = active
        self.parameters = parameters
        self.morel_Executable = morel_Executable if morel_Executable is not None else set()
        
    @property
    def parameters(self) -> str:
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters: str):
        self.__parameters = parameters

    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def morel_Executable(self):
        return self.__morel_Executable

    @morel_Executable.setter
    def morel_Executable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_Executable__morel_Executable", None)
        self.__morel_Executable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "morel_PrimitiveVariable138"):
                    opp_val = getattr(item, "morel_PrimitiveVariable138", None)
                    
                    if opp_val == self:
                        setattr(item, "morel_PrimitiveVariable138", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "morel_PrimitiveVariable138"):
                    opp_val = getattr(item, "morel_PrimitiveVariable138", None)
                    
                    setattr(item, "morel_PrimitiveVariable138", self)
                    

class Statement:

    pass
class morel_DeclarativeStatement(Statement):

    pass
class RuleElement:

    pass
class morel_RuleGroup(RuleElement):

    def __init__(self, scope: str, scopeSize: int, order: str, iteration: str, maxIteration: int, repetition: str, morel_RuleGroup: set["morel_Rule"] = None):
        self.scope = scope
        self.scopeSize = scopeSize
        self.order = order
        self.iteration = iteration
        self.maxIteration = maxIteration
        self.repetition = repetition
        self.morel_RuleGroup = morel_RuleGroup if morel_RuleGroup is not None else set()
        
    @property
    def repetition(self) -> str:
        return self.__repetition

    @repetition.setter
    def repetition(self, repetition: str):
        self.__repetition = repetition

    @property
    def order(self) -> str:
        return self.__order

    @order.setter
    def order(self, order: str):
        self.__order = order

    @property
    def maxIteration(self) -> int:
        return self.__maxIteration

    @maxIteration.setter
    def maxIteration(self, maxIteration: int):
        self.__maxIteration = maxIteration

    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope

    @property
    def scopeSize(self) -> int:
        return self.__scopeSize

    @scopeSize.setter
    def scopeSize(self, scopeSize: int):
        self.__scopeSize = scopeSize

    @property
    def iteration(self) -> str:
        return self.__iteration

    @iteration.setter
    def iteration(self, iteration: str):
        self.__iteration = iteration

    @property
    def morel_RuleGroup(self):
        return self.__morel_RuleGroup

    @morel_RuleGroup.setter
    def morel_RuleGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_RuleGroup__morel_RuleGroup", None)
        self.__morel_RuleGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "morel_Rule130"):
                    opp_val = getattr(item, "morel_Rule130", None)
                    
                    if opp_val == self:
                        setattr(item, "morel_Rule130", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "morel_Rule130"):
                    opp_val = getattr(item, "morel_Rule130", None)
                    
                    setattr(item, "morel_Rule130", self)
                    

class morel_Rule(RuleElement):

    pass
class morel_ImperativeStatement(Statement):

    pass
class ImperativeStatement:

    pass
class morel_ForStatement(ImperativeStatement):

    pass
class morel_BlockStatement(ImperativeStatement):

    pass
class morel_IfStatement(ImperativeStatement):

    pass
class CollectionType:

    pass
class morel_SequenceType(CollectionType):

    pass
class morel_BagType(CollectionType):

    pass
class morel_SetType(CollectionType):

    pass
class morel_OrderedSetType(CollectionType):

    pass
class EDataType:

    pass
class morel_CollectionType(EDataType):

    pass
class MultiplicativeExpChild:

    pass
class morel_UnaryExpChild(MultiplicativeExpChild):

    pass
class morel_UnaryExp(MultiplicativeExpChild):

    def __init__(self, operator: str, morel_UnaryExp: "morel_UnaryExpChild" = None):
        self.operator = operator
        self.morel_UnaryExp = morel_UnaryExp
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def morel_UnaryExp(self):
        return self.__morel_UnaryExp

    @morel_UnaryExp.setter
    def morel_UnaryExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_UnaryExp__morel_UnaryExp", None)
        self.__morel_UnaryExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "morel_UnaryExpChild"):
                opp_val = getattr(old_value, "morel_UnaryExpChild", None)
                if opp_val == self:
                    setattr(old_value, "morel_UnaryExpChild", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "morel_UnaryExpChild"):
                opp_val = getattr(value, "morel_UnaryExpChild", None)
                setattr(value, "morel_UnaryExpChild", self)

class AdditiveExpChild:

    pass
class morel_MultiplicativeExpChild(AdditiveExpChild):

    pass
class morel_MultiplicativeExp(AdditiveExpChild):

    def __init__(self, operators: str, morel_MultiplicativeExp: set["morel_MultiplicativeExpChild"] = None):
        self.operators = operators
        self.morel_MultiplicativeExp = morel_MultiplicativeExp if morel_MultiplicativeExp is not None else set()
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def morel_MultiplicativeExp(self):
        return self.__morel_MultiplicativeExp

    @morel_MultiplicativeExp.setter
    def morel_MultiplicativeExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_MultiplicativeExp__morel_MultiplicativeExp", None)
        self.__morel_MultiplicativeExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "morel_MultiplicativeExpChild"):
                    opp_val = getattr(item, "morel_MultiplicativeExpChild", None)
                    
                    if opp_val == self:
                        setattr(item, "morel_MultiplicativeExpChild", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "morel_MultiplicativeExpChild"):
                    opp_val = getattr(item, "morel_MultiplicativeExpChild", None)
                    
                    setattr(item, "morel_MultiplicativeExpChild", self)
                    

class RelationalExpChild:

    pass
class morel_AdditiveExpChild(RelationalExpChild):

    pass
class morel_AdditiveExp(RelationalExpChild):

    def __init__(self, operators: str, morel_AdditiveExp: set["morel_AdditiveExpChild"] = None):
        self.operators = operators
        self.morel_AdditiveExp = morel_AdditiveExp if morel_AdditiveExp is not None else set()
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def morel_AdditiveExp(self):
        return self.__morel_AdditiveExp

    @morel_AdditiveExp.setter
    def morel_AdditiveExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_AdditiveExp__morel_AdditiveExp", None)
        self.__morel_AdditiveExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "morel_AdditiveExpChild"):
                    opp_val = getattr(item, "morel_AdditiveExpChild", None)
                    
                    if opp_val == self:
                        setattr(item, "morel_AdditiveExpChild", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "morel_AdditiveExpChild"):
                    opp_val = getattr(item, "morel_AdditiveExpChild", None)
                    
                    setattr(item, "morel_AdditiveExpChild", self)
                    

class BooleanAndExpChild:

    pass
class morel_RelationalExpChild(BooleanAndExpChild):

    pass
class morel_RelationalExp(BooleanAndExpChild):

    def __init__(self, operator: str, morel_RelationalExp: "morel_RelationalExpChild" = None, morel_RelationalExp90: "morel_RelationalExpChild" = None):
        self.operator = operator
        self.morel_RelationalExp = morel_RelationalExp
        self.morel_RelationalExp90 = morel_RelationalExp90
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def morel_RelationalExp(self):
        return self.__morel_RelationalExp

    @morel_RelationalExp.setter
    def morel_RelationalExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_RelationalExp__morel_RelationalExp", None)
        self.__morel_RelationalExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "morel_RelationalExpChild"):
                opp_val = getattr(old_value, "morel_RelationalExpChild", None)
                if opp_val == self:
                    setattr(old_value, "morel_RelationalExpChild", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "morel_RelationalExpChild"):
                opp_val = getattr(value, "morel_RelationalExpChild", None)
                setattr(value, "morel_RelationalExpChild", self)

    @property
    def morel_RelationalExp90(self):
        return self.__morel_RelationalExp90

    @morel_RelationalExp90.setter
    def morel_RelationalExp90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_RelationalExp__morel_RelationalExp90", None)
        self.__morel_RelationalExp90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "morel_RelationalExpChild91"):
                opp_val = getattr(old_value, "morel_RelationalExpChild91", None)
                if opp_val == self:
                    setattr(old_value, "morel_RelationalExpChild91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "morel_RelationalExpChild91"):
                opp_val = getattr(value, "morel_RelationalExpChild91", None)
                setattr(value, "morel_RelationalExpChild91", self)

class BooleanOrExpChild:

    pass
class morel_BooleanAndExpChild(BooleanOrExpChild):

    pass
class morel_BooleanAndExp(BooleanOrExpChild):

    def __init__(self, operators: str, morel_BooleanAndExp: set["morel_BooleanAndExpChild"] = None):
        self.operators = operators
        self.morel_BooleanAndExp = morel_BooleanAndExp if morel_BooleanAndExp is not None else set()
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def morel_BooleanAndExp(self):
        return self.__morel_BooleanAndExp

    @morel_BooleanAndExp.setter
    def morel_BooleanAndExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_BooleanAndExp__morel_BooleanAndExp", None)
        self.__morel_BooleanAndExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "morel_BooleanAndExpChild"):
                    opp_val = getattr(item, "morel_BooleanAndExpChild", None)
                    
                    if opp_val == self:
                        setattr(item, "morel_BooleanAndExpChild", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "morel_BooleanAndExpChild"):
                    opp_val = getattr(item, "morel_BooleanAndExpChild", None)
                    
                    setattr(item, "morel_BooleanAndExpChild", self)
                    

class BooleanImpliesExpChild:

    pass
class morel_BooleanOrExpChild(BooleanImpliesExpChild):

    pass
class morel_BooleanOrExp(BooleanImpliesExpChild):

    def __init__(self, operators: str, morel_BooleanOrExp: set["morel_BooleanOrExpChild"] = None):
        self.operators = operators
        self.morel_BooleanOrExp = morel_BooleanOrExp if morel_BooleanOrExp is not None else set()
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def morel_BooleanOrExp(self):
        return self.__morel_BooleanOrExp

    @morel_BooleanOrExp.setter
    def morel_BooleanOrExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_BooleanOrExp__morel_BooleanOrExp", None)
        self.__morel_BooleanOrExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "morel_BooleanOrExpChild"):
                    opp_val = getattr(item, "morel_BooleanOrExpChild", None)
                    
                    if opp_val == self:
                        setattr(item, "morel_BooleanOrExpChild", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "morel_BooleanOrExpChild"):
                    opp_val = getattr(item, "morel_BooleanOrExpChild", None)
                    
                    setattr(item, "morel_BooleanOrExpChild", self)
                    

class PrimitiveVariable:

    pass
class VariableWithInit:

    pass
class morel_PrimitiveVariableWithInit(VariableWithInit, PrimitiveVariable):

    pass
class ObjectVariable:

    pass
class morel_ObjectVariableWithInit(ObjectVariable, VariableWithInit):

    pass
class ImperativeExp:

    pass
class morel_PredefinedBindExp(ImperativeExp):

    pass
class morel_BindExp(ImperativeExp):

    pass
class Expression:

    pass
class morel_ReflectiveVariableExp(Expression):

    pass
class morel_ConditionExp(Expression):

    pass
class morel_ImperativeExp(Expression):

    pass
class morel_BooleanImpliesExpChild(Expression):

    pass
class morel_BooleanImpliesExp(Expression):

    def __init__(self, operator: str, morel_BooleanImpliesExp: "morel_ConditionExp" = None, morel_BooleanImpliesExp82: "morel_BooleanImpliesExpChild" = None, morel_BooleanImpliesExp84: "morel_BooleanImpliesExpChild" = None, morel_BooleanImpliesExp107: "morel_IfStatement" = None, morel_BooleanImpliesExp117: "morel_ForStatement" = None):
        self.operator = operator
        self.morel_BooleanImpliesExp = morel_BooleanImpliesExp
        self.morel_BooleanImpliesExp82 = morel_BooleanImpliesExp82
        self.morel_BooleanImpliesExp84 = morel_BooleanImpliesExp84
        self.morel_BooleanImpliesExp107 = morel_BooleanImpliesExp107
        self.morel_BooleanImpliesExp117 = morel_BooleanImpliesExp117
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def morel_BooleanImpliesExp(self):
        return self.__morel_BooleanImpliesExp

    @morel_BooleanImpliesExp.setter
    def morel_BooleanImpliesExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_BooleanImpliesExp__morel_BooleanImpliesExp", None)
        self.__morel_BooleanImpliesExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "morel_ConditionExp"):
                opp_val = getattr(old_value, "morel_ConditionExp", None)
                if opp_val == self:
                    setattr(old_value, "morel_ConditionExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "morel_ConditionExp"):
                opp_val = getattr(value, "morel_ConditionExp", None)
                setattr(value, "morel_ConditionExp", self)

    @property
    def morel_BooleanImpliesExp82(self):
        return self.__morel_BooleanImpliesExp82

    @morel_BooleanImpliesExp82.setter
    def morel_BooleanImpliesExp82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_BooleanImpliesExp__morel_BooleanImpliesExp82", None)
        self.__morel_BooleanImpliesExp82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "morel_BooleanImpliesExpChild"):
                opp_val = getattr(old_value, "morel_BooleanImpliesExpChild", None)
                if opp_val == self:
                    setattr(old_value, "morel_BooleanImpliesExpChild", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "morel_BooleanImpliesExpChild"):
                opp_val = getattr(value, "morel_BooleanImpliesExpChild", None)
                setattr(value, "morel_BooleanImpliesExpChild", self)

    @property
    def morel_BooleanImpliesExp117(self):
        return self.__morel_BooleanImpliesExp117

    @morel_BooleanImpliesExp117.setter
    def morel_BooleanImpliesExp117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_BooleanImpliesExp__morel_BooleanImpliesExp117", None)
        self.__morel_BooleanImpliesExp117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "morel_ForStatement116"):
                opp_val = getattr(old_value, "morel_ForStatement116", None)
                if opp_val == self:
                    setattr(old_value, "morel_ForStatement116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "morel_ForStatement116"):
                opp_val = getattr(value, "morel_ForStatement116", None)
                setattr(value, "morel_ForStatement116", self)

    @property
    def morel_BooleanImpliesExp107(self):
        return self.__morel_BooleanImpliesExp107

    @morel_BooleanImpliesExp107.setter
    def morel_BooleanImpliesExp107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_BooleanImpliesExp__morel_BooleanImpliesExp107", None)
        self.__morel_BooleanImpliesExp107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "morel_IfStatement"):
                opp_val = getattr(old_value, "morel_IfStatement", None)
                if opp_val == self:
                    setattr(old_value, "morel_IfStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "morel_IfStatement"):
                opp_val = getattr(value, "morel_IfStatement", None)
                setattr(value, "morel_IfStatement", self)

    @property
    def morel_BooleanImpliesExp84(self):
        return self.__morel_BooleanImpliesExp84

    @morel_BooleanImpliesExp84.setter
    def morel_BooleanImpliesExp84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_BooleanImpliesExp__morel_BooleanImpliesExp84", None)
        self.__morel_BooleanImpliesExp84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "morel_BooleanImpliesExpChild85"):
                opp_val = getattr(old_value, "morel_BooleanImpliesExpChild85", None)
                if opp_val == self:
                    setattr(old_value, "morel_BooleanImpliesExpChild85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "morel_BooleanImpliesExpChild85"):
                opp_val = getattr(value, "morel_BooleanImpliesExpChild85", None)
                setattr(value, "morel_BooleanImpliesExpChild85", self)

class morel_LetExp(ImperativeExp, Expression):

    pass
class LoopPathExp:

    pass
class morel_IteratorPathExp(LoopPathExp):

    def __init__(self, type: str, morel_IteratorPathExp: "morel_Variable" = None, morel_IteratorPathExp62: "morel_Variable" = None, morel_IteratorPathExp65: "morel_Expression" = None):
        self.type = type
        self.morel_IteratorPathExp = morel_IteratorPathExp
        self.morel_IteratorPathExp62 = morel_IteratorPathExp62
        self.morel_IteratorPathExp65 = morel_IteratorPathExp65
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def morel_IteratorPathExp65(self):
        return self.__morel_IteratorPathExp65

    @morel_IteratorPathExp65.setter
    def morel_IteratorPathExp65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_IteratorPathExp__morel_IteratorPathExp65", None)
        self.__morel_IteratorPathExp65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "morel_Expression66"):
                opp_val = getattr(old_value, "morel_Expression66", None)
                if opp_val == self:
                    setattr(old_value, "morel_Expression66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "morel_Expression66"):
                opp_val = getattr(value, "morel_Expression66", None)
                setattr(value, "morel_Expression66", self)

    @property
    def morel_IteratorPathExp(self):
        return self.__morel_IteratorPathExp

    @morel_IteratorPathExp.setter
    def morel_IteratorPathExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_IteratorPathExp__morel_IteratorPathExp", None)
        self.__morel_IteratorPathExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "morel_Variable60"):
                opp_val = getattr(old_value, "morel_Variable60", None)
                if opp_val == self:
                    setattr(old_value, "morel_Variable60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "morel_Variable60"):
                opp_val = getattr(value, "morel_Variable60", None)
                setattr(value, "morel_Variable60", self)

    @property
    def morel_IteratorPathExp62(self):
        return self.__morel_IteratorPathExp62

    @morel_IteratorPathExp62.setter
    def morel_IteratorPathExp62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_IteratorPathExp__morel_IteratorPathExp62", None)
        self.__morel_IteratorPathExp62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "morel_Variable63"):
                opp_val = getattr(old_value, "morel_Variable63", None)
                if opp_val == self:
                    setattr(old_value, "morel_Variable63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "morel_Variable63"):
                opp_val = getattr(value, "morel_Variable63", None)
                setattr(value, "morel_Variable63", self)

class CallPathExp:

    pass
class morel_OperationPathExp(CallPathExp):

    def __init__(self, separator: str, operation: str, morel_OperationPathExp: set["morel_Expression"] = None):
        self.separator = separator
        self.operation = operation
        self.morel_OperationPathExp = morel_OperationPathExp if morel_OperationPathExp is not None else set()
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

    @property
    def separator(self) -> str:
        return self.__separator

    @separator.setter
    def separator(self, separator: str):
        self.__separator = separator

    @property
    def morel_OperationPathExp(self):
        return self.__morel_OperationPathExp

    @morel_OperationPathExp.setter
    def morel_OperationPathExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_OperationPathExp__morel_OperationPathExp", None)
        self.__morel_OperationPathExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "morel_Expression58"):
                    opp_val = getattr(item, "morel_Expression58", None)
                    
                    if opp_val == self:
                        setattr(item, "morel_Expression58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "morel_Expression58"):
                    opp_val = getattr(item, "morel_Expression58", None)
                    
                    setattr(item, "morel_Expression58", self)
                    

class morel_LoopPathExp(CallPathExp):

    pass
class morel_FeaturePathExp(CallPathExp):

    def __init__(self, feature: str):
        self.feature = feature
        
    @property
    def feature(self) -> str:
        return self.__feature

    @feature.setter
    def feature(self, feature: str):
        self.__feature = feature

class morel_EClassifier:

    pass
class morel_EEnumLiteral:

    pass
class morel_EEnum:

    pass
class LiteralExp:

    pass
class morel_CollectionLiteralExp(LiteralExp):

    def __init__(self, type: str, morel_CollectionLiteralExp: set["morel_Expression"] = None):
        self.type = type
        self.morel_CollectionLiteralExp = morel_CollectionLiteralExp if morel_CollectionLiteralExp is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def morel_CollectionLiteralExp(self):
        return self.__morel_CollectionLiteralExp

    @morel_CollectionLiteralExp.setter
    def morel_CollectionLiteralExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_CollectionLiteralExp__morel_CollectionLiteralExp", None)
        self.__morel_CollectionLiteralExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "morel_Expression45"):
                    opp_val = getattr(item, "morel_Expression45", None)
                    
                    if opp_val == self:
                        setattr(item, "morel_Expression45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "morel_Expression45"):
                    opp_val = getattr(item, "morel_Expression45", None)
                    
                    setattr(item, "morel_Expression45", self)
                    

class morel_TypeLiteralExp(LiteralExp):

    pass
class morel_RealLiteralExp(LiteralExp):

    def __init__(self, realSymbol: float):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> float:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: float):
        self.__realSymbol = realSymbol

class morel_ArrayLiteralExp(LiteralExp):

    pass
class morel_EnumLiteralExp(LiteralExp):

    pass
class morel_UndefinedLiteralExp(LiteralExp):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class morel_BooleanLiteralExp(LiteralExp):

    def __init__(self, boolSymbol: bool):
        self.boolSymbol = boolSymbol
        
    @property
    def boolSymbol(self) -> bool:
        return self.__boolSymbol

    @boolSymbol.setter
    def boolSymbol(self, boolSymbol: bool):
        self.__boolSymbol = boolSymbol

class morel_IntegerLiteralExp(LiteralExp):

    def __init__(self, integerSymbol: int):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> int:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: int):
        self.__integerSymbol = integerSymbol

class morel_StringLiteralExp(LiteralExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class morel_CallPathExp(ABC):

    pass
class UnaryExpChild:

    pass
class morel_AtomicExp(UnaryExpChild):

    pass
class morel_Unit(ABC):

    def __init__(self, morel_Unit: set["morel_TypedModel"] = None, morel_Unit41: set["morel_EDataType"] = None):
        self.morel_Unit = morel_Unit if morel_Unit is not None else set()
        self.morel_Unit41 = morel_Unit41 if morel_Unit41 is not None else set()
        
    @property
    def morel_Unit41(self):
        return self.__morel_Unit41

    @morel_Unit41.setter
    def morel_Unit41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_Unit__morel_Unit41", None)
        self.__morel_Unit41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "morel_EDataType42"):
                    opp_val = getattr(item, "morel_EDataType42", None)
                    
                    if opp_val == self:
                        setattr(item, "morel_EDataType42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "morel_EDataType42"):
                    opp_val = getattr(item, "morel_EDataType42", None)
                    
                    setattr(item, "morel_EDataType42", self)
                    

    @property
    def morel_Unit(self):
        return self.__morel_Unit

    @morel_Unit.setter
    def morel_Unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_Unit__morel_Unit", None)
        self.__morel_Unit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "morel_TypedModel39"):
                    opp_val = getattr(item, "morel_TypedModel39", None)
                    
                    if opp_val == self:
                        setattr(item, "morel_TypedModel39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "morel_TypedModel39"):
                    opp_val = getattr(item, "morel_TypedModel39", None)
                    
                    setattr(item, "morel_TypedModel39", self)
                    

    def getTypedModel(self, name: str) -> str:
        # TODO: Implement getTypedModel method
        pass

class Executable:

    pass
class Pattern:

    pass
class morel_EPackage:

    pass
class Unit:

    pass
class morel_QueryModel(Unit):

    pass
class AtomicExp:

    pass
class morel_VariableExp(AtomicExp):

    pass
class morel_PredefinedVariableExp(AtomicExp):

    def __init__(self, variable: str, morel_PredefinedVariableExp: "morel_PredefinedBindExp" = None):
        self.variable = variable
        self.morel_PredefinedVariableExp = morel_PredefinedVariableExp
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def morel_PredefinedVariableExp(self):
        return self.__morel_PredefinedVariableExp

    @morel_PredefinedVariableExp.setter
    def morel_PredefinedVariableExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_PredefinedVariableExp__morel_PredefinedVariableExp", None)
        self.__morel_PredefinedVariableExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "morel_PredefinedBindExp"):
                opp_val = getattr(old_value, "morel_PredefinedBindExp", None)
                if opp_val == self:
                    setattr(old_value, "morel_PredefinedBindExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "morel_PredefinedBindExp"):
                opp_val = getattr(value, "morel_PredefinedBindExp", None)
                setattr(value, "morel_PredefinedBindExp", self)

class morel_NestedExp(AtomicExp):

    pass
class morel_LiteralExp(AtomicExp):

    pass
class morel_EReference:

    pass
class morel_Expression(ABC):

    pass
class LinkConstraint:

    pass
class morel_EnclosureLinkConstraint(LinkConstraint):

    pass
class morel_PathConstraint(LinkConstraint):

    def __init__(self, minLength: int, maxLength: int, morel_PathConstraint: "morel_Variable" = None, morel_PathConstraint30: set["morel_EReference"] = None, morel_PathConstraint33: set["morel_EClass"] = None):
        self.minLength = minLength
        self.maxLength = maxLength
        self.morel_PathConstraint = morel_PathConstraint
        self.morel_PathConstraint30 = morel_PathConstraint30 if morel_PathConstraint30 is not None else set()
        self.morel_PathConstraint33 = morel_PathConstraint33 if morel_PathConstraint33 is not None else set()
        
    @property
    def maxLength(self) -> int:
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: int):
        self.__maxLength = maxLength

    @property
    def minLength(self) -> int:
        return self.__minLength

    @minLength.setter
    def minLength(self, minLength: int):
        self.__minLength = minLength

    @property
    def morel_PathConstraint(self):
        return self.__morel_PathConstraint

    @morel_PathConstraint.setter
    def morel_PathConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_PathConstraint__morel_PathConstraint", None)
        self.__morel_PathConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "morel_Variable"):
                opp_val = getattr(old_value, "morel_Variable", None)
                if opp_val == self:
                    setattr(old_value, "morel_Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "morel_Variable"):
                opp_val = getattr(value, "morel_Variable", None)
                setattr(value, "morel_Variable", self)

    @property
    def morel_PathConstraint30(self):
        return self.__morel_PathConstraint30

    @morel_PathConstraint30.setter
    def morel_PathConstraint30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_PathConstraint__morel_PathConstraint30", None)
        self.__morel_PathConstraint30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "morel_EReference31"):
                    opp_val = getattr(item, "morel_EReference31", None)
                    
                    if opp_val == self:
                        setattr(item, "morel_EReference31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "morel_EReference31"):
                    opp_val = getattr(item, "morel_EReference31", None)
                    
                    setattr(item, "morel_EReference31", self)
                    

    @property
    def morel_PathConstraint33(self):
        return self.__morel_PathConstraint33

    @morel_PathConstraint33.setter
    def morel_PathConstraint33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_PathConstraint__morel_PathConstraint33", None)
        self.__morel_PathConstraint33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "morel_EClass34"):
                    opp_val = getattr(item, "morel_EClass34", None)
                    
                    if opp_val == self:
                        setattr(item, "morel_EClass34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "morel_EClass34"):
                    opp_val = getattr(item, "morel_EClass34", None)
                    
                    setattr(item, "morel_EClass34", self)
                    

class morel_SimpleLinkConstraint(LinkConstraint):

    pass
class morel_EDataType:

    pass
class morel_EClass:

    pass
class Variable:

    pass
class morel_VariableWithInit(Variable):

    pass
class morel_PrimitiveVariable(Variable):

    pass
class NamedElement:

    pass
class morel_TransformationModel(Unit, NamedElement):

    pass
class morel_RuleElement(NamedElement, Executable):

    pass
class morel_TypedModel(NamedElement):

    def __init__(self, type: str, morel_TypedModel: "morel_ObjectVariable" = None, morel_TypedModel37: "morel_EPackage" = None, morel_TypedModel39: "morel_Unit" = None):
        self.type = type
        self.morel_TypedModel = morel_TypedModel
        self.morel_TypedModel37 = morel_TypedModel37
        self.morel_TypedModel39 = morel_TypedModel39
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def morel_TypedModel(self):
        return self.__morel_TypedModel

    @morel_TypedModel.setter
    def morel_TypedModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_TypedModel__morel_TypedModel", None)
        self.__morel_TypedModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "morel_ObjectVariable12"):
                opp_val = getattr(old_value, "morel_ObjectVariable12", None)
                if opp_val == self:
                    setattr(old_value, "morel_ObjectVariable12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "morel_ObjectVariable12"):
                opp_val = getattr(value, "morel_ObjectVariable12", None)
                setattr(value, "morel_ObjectVariable12", self)

    @property
    def morel_TypedModel37(self):
        return self.__morel_TypedModel37

    @morel_TypedModel37.setter
    def morel_TypedModel37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_TypedModel__morel_TypedModel37", None)
        self.__morel_TypedModel37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "morel_EPackage"):
                opp_val = getattr(old_value, "morel_EPackage", None)
                if opp_val == self:
                    setattr(old_value, "morel_EPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "morel_EPackage"):
                opp_val = getattr(value, "morel_EPackage", None)
                setattr(value, "morel_EPackage", self)

    @property
    def morel_TypedModel39(self):
        return self.__morel_TypedModel39

    @morel_TypedModel39.setter
    def morel_TypedModel39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_morel_TypedModel__morel_TypedModel39", None)
        self.__morel_TypedModel39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "morel_Unit"):
                opp_val = getattr(old_value, "morel_Unit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "morel_Unit"):
                opp_val = getattr(value, "morel_Unit", None)
                if opp_val is None:
                    setattr(value, "morel_Unit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class morel_Query(Executable, Pattern, NamedElement):

    pass
class morel_Variable(NamedElement):

    pass
class morel_AdditionalConstraint(ABC):

    pass
class morel_Statement(ABC):

    pass
class morel_LinkConstraint(ABC):

    pass
class morel_ObjectVariable(Variable):

    pass
class Section:

    pass
class morel_Clause(Section):

    pass
class morel_Pattern(Section):

    pass
class morel_Section(ABC):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class morel_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
