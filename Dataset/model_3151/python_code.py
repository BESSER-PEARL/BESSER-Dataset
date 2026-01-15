from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class MultiplicativeOperator(Enum):
    Multiply = "Multiply"
    Divide = "Divide"
    ElementWiseMultiply = "ElementWiseMultiply"
    ElementWiseDivide = "ElementWiseDivide"
class AssertionStatusKind(Enum):
    Info = "Info"
    Warning = "Warning"
    Error = "Error"
    Fatal = "Fatal"
class AdditiveOperator(Enum):
    Add = "Add"
    Subtract = "Subtract"
class PostfixOperator(Enum):
    Transpose = "Transpose"
class RelationalOperator(Enum):
    LessThan = "LessThan"
    LessThanOrEqualTo = "LessThanOrEqualTo"
    GreaterThan = "GreaterThan"
    GreaterThanOrEqualTo = "GreaterThanOrEqualTo"
class FunctionKind(Enum):
    Stateless = "Stateless"
    Stateful = "Stateful"
    Continuous = "Continuous"
class UnaryOperator(Enum):
    Negate = "Negate"
    LogicalNot = "LogicalNot"
class EqualityOperator(Enum):
    EqualTo = "EqualTo"
    NotEqualTo = "NotEqualTo"
class PowerOperator(Enum):
    Power = "Power"
    ElementWisePower = "ElementWisePower"


############################################
# Definition of Classes
############################################

class BuiltinDefinition:

    pass
class ast_BuiltinVariable(BuiltinDefinition):

    pass
class ast_BuiltinFunction(BuiltinDefinition):

    pass
class ast_Statement(ABC):

    pass
class Statement:

    pass
class ast_ForStatement(Statement):

    pass
class ast_ContinueStatement(Statement):

    pass
class ast_ReturnStatement(Statement):

    pass
class ast_BreakStatement(Statement):

    pass
class ast_DoWhileStatement(Statement):

    pass
class ast_IfStatement(Statement):

    pass
class ast_WhileStatement(Statement):

    pass
class ast_Assignment(Statement):

    pass
class ast_Compound(Statement):

    pass
class PrimitiveStepExpression:

    pass
class ast_StepN(PrimitiveStepExpression):

    pass
class ast_StepLiteral(PrimitiveStepExpression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class StepExpression:

    pass
class ast_PrimitiveStepExpression(StepExpression):

    pass
class ast_NegateStepExpression(StepExpression):

    pass
class ast_AdditiveStepExpression(StepExpression):

    def __init__(self, operator: str, ast_AdditiveStepExpression: "ast_StepExpression" = None, ast_AdditiveStepExpression180: "ast_StepExpression" = None):
        self.operator = operator
        self.ast_AdditiveStepExpression = ast_AdditiveStepExpression
        self.ast_AdditiveStepExpression180 = ast_AdditiveStepExpression180
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ast_AdditiveStepExpression180(self):
        return self.__ast_AdditiveStepExpression180

    @ast_AdditiveStepExpression180.setter
    def ast_AdditiveStepExpression180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_AdditiveStepExpression__ast_AdditiveStepExpression180", None)
        self.__ast_AdditiveStepExpression180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_StepExpression181"):
                opp_val = getattr(old_value, "ast_StepExpression181", None)
                if opp_val == self:
                    setattr(old_value, "ast_StepExpression181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_StepExpression181"):
                opp_val = getattr(value, "ast_StepExpression181", None)
                setattr(value, "ast_StepExpression181", self)

    @property
    def ast_AdditiveStepExpression(self):
        return self.__ast_AdditiveStepExpression

    @ast_AdditiveStepExpression.setter
    def ast_AdditiveStepExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_AdditiveStepExpression__ast_AdditiveStepExpression", None)
        self.__ast_AdditiveStepExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_StepExpression178"):
                opp_val = getattr(old_value, "ast_StepExpression178", None)
                if opp_val == self:
                    setattr(old_value, "ast_StepExpression178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_StepExpression178"):
                opp_val = getattr(value, "ast_StepExpression178", None)
                setattr(value, "ast_StepExpression178", self)

class ast_RangeStepExpression(StepExpression):

    pass
class ast_StepExpression(ABC):

    pass
class FeatureCall:

    pass
class ast_FunctionCall(FeatureCall):

    pass
class ast_VariableAccess(FeatureCall):

    def __init__(self, ast_VariableAccess: "ast_StepExpression" = None):
        self.ast_VariableAccess = ast_VariableAccess
        
    @property
    def ast_VariableAccess(self):
        return self.__ast_VariableAccess

    @ast_VariableAccess.setter
    def ast_VariableAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_VariableAccess__ast_VariableAccess", None)
        self.__ast_VariableAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_StepExpression"):
                opp_val = getattr(old_value, "ast_StepExpression", None)
                if opp_val == self:
                    setattr(old_value, "ast_StepExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_StepExpression"):
                opp_val = getattr(value, "ast_StepExpression", None)
                setattr(value, "ast_StepExpression", self)

    def isInitial(self) -> bool:
        # TODO: Implement isInitial method
        pass

class ast_Unit:

    pass
class ast_ExpressionList:

    pass
class ast_ArrayConstructionIterationClause:

    def __init__(self, variableName: str, ast_ArrayConstructionIterationClause: "ast_ArrayConstructionOperator" = None, ast_ArrayConstructionIterationClause109: "ast_Expression" = None):
        self.variableName = variableName
        self.ast_ArrayConstructionIterationClause = ast_ArrayConstructionIterationClause
        self.ast_ArrayConstructionIterationClause109 = ast_ArrayConstructionIterationClause109
        
    @property
    def variableName(self) -> str:
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName

    @property
    def ast_ArrayConstructionIterationClause(self):
        return self.__ast_ArrayConstructionIterationClause

    @ast_ArrayConstructionIterationClause.setter
    def ast_ArrayConstructionIterationClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_ArrayConstructionIterationClause__ast_ArrayConstructionIterationClause", None)
        self.__ast_ArrayConstructionIterationClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_ArrayConstructionOperator107"):
                opp_val = getattr(old_value, "ast_ArrayConstructionOperator107", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_ArrayConstructionOperator107"):
                opp_val = getattr(value, "ast_ArrayConstructionOperator107", None)
                if opp_val is None:
                    setattr(value, "ast_ArrayConstructionOperator107", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ast_ArrayConstructionIterationClause109(self):
        return self.__ast_ArrayConstructionIterationClause109

    @ast_ArrayConstructionIterationClause109.setter
    def ast_ArrayConstructionIterationClause109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_ArrayConstructionIterationClause__ast_ArrayConstructionIterationClause109", None)
        self.__ast_ArrayConstructionIterationClause109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression110"):
                opp_val = getattr(old_value, "ast_Expression110", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression110"):
                opp_val = getattr(value, "ast_Expression110", None)
                setattr(value, "ast_Expression110", self)

class ast_ArraySubscript:

    def __init__(self, slice: bool, ast_ArraySubscript: "ast_ArrayElementAccess" = None, ast_ArraySubscript86: "ast_Expression" = None):
        self.slice = slice
        self.ast_ArraySubscript = ast_ArraySubscript
        self.ast_ArraySubscript86 = ast_ArraySubscript86
        
    @property
    def slice(self) -> bool:
        return self.__slice

    @slice.setter
    def slice(self, slice: bool):
        self.__slice = slice

    @property
    def ast_ArraySubscript86(self):
        return self.__ast_ArraySubscript86

    @ast_ArraySubscript86.setter
    def ast_ArraySubscript86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_ArraySubscript__ast_ArraySubscript86", None)
        self.__ast_ArraySubscript86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression87"):
                opp_val = getattr(old_value, "ast_Expression87", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression87"):
                opp_val = getattr(value, "ast_Expression87", None)
                setattr(value, "ast_Expression87", self)

    @property
    def ast_ArraySubscript(self):
        return self.__ast_ArraySubscript

    @ast_ArraySubscript.setter
    def ast_ArraySubscript(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_ArraySubscript__ast_ArraySubscript", None)
        self.__ast_ArraySubscript = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_ArrayElementAccess84"):
                opp_val = getattr(old_value, "ast_ArrayElementAccess84", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_ArrayElementAccess84"):
                opp_val = getattr(value, "ast_ArrayElementAccess84", None)
                if opp_val is None:
                    setattr(value, "ast_ArrayElementAccess84", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ast_SwitchCase:

    pass
class ast_LetExpressionVariableDeclaration:

    pass
class Expression:

    pass
class ast_RelationalExpression(Expression):

    def __init__(self, operator: str, ast_RelationalExpression: "ast_Expression" = None, ast_RelationalExpression143: "ast_Expression" = None):
        self.operator = operator
        self.ast_RelationalExpression = ast_RelationalExpression
        self.ast_RelationalExpression143 = ast_RelationalExpression143
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ast_RelationalExpression(self):
        return self.__ast_RelationalExpression

    @ast_RelationalExpression.setter
    def ast_RelationalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_RelationalExpression__ast_RelationalExpression", None)
        self.__ast_RelationalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression141"):
                opp_val = getattr(old_value, "ast_Expression141", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression141"):
                opp_val = getattr(value, "ast_Expression141", None)
                setattr(value, "ast_Expression141", self)

    @property
    def ast_RelationalExpression143(self):
        return self.__ast_RelationalExpression143

    @ast_RelationalExpression143.setter
    def ast_RelationalExpression143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_RelationalExpression__ast_RelationalExpression143", None)
        self.__ast_RelationalExpression143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression144"):
                opp_val = getattr(old_value, "ast_Expression144", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression144"):
                opp_val = getattr(value, "ast_Expression144", None)
                setattr(value, "ast_Expression144", self)

class ast_FeatureCall(Expression):

    pass
class ast_ImpliesExpression(Expression):

    pass
class ast_UnaryExpression(Expression):

    def __init__(self, operator: str, ast_UnaryExpression: "ast_Expression" = None):
        self.operator = operator
        self.ast_UnaryExpression = ast_UnaryExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ast_UnaryExpression(self):
        return self.__ast_UnaryExpression

    @ast_UnaryExpression.setter
    def ast_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_UnaryExpression__ast_UnaryExpression", None)
        self.__ast_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression166"):
                opp_val = getattr(old_value, "ast_Expression166", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression166"):
                opp_val = getattr(value, "ast_Expression166", None)
                setattr(value, "ast_Expression166", self)

class ast_RangeExpression(Expression):

    pass
class ast_IfExpression(Expression):

    def __init__(self, static: bool, ast_IfExpression: "ast_Expression" = None, ast_IfExpression63: "ast_Expression" = None, ast_IfExpression66: "ast_Expression" = None):
        self.static = static
        self.ast_IfExpression = ast_IfExpression
        self.ast_IfExpression63 = ast_IfExpression63
        self.ast_IfExpression66 = ast_IfExpression66
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def ast_IfExpression(self):
        return self.__ast_IfExpression

    @ast_IfExpression.setter
    def ast_IfExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_IfExpression__ast_IfExpression", None)
        self.__ast_IfExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression61"):
                opp_val = getattr(old_value, "ast_Expression61", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression61"):
                opp_val = getattr(value, "ast_Expression61", None)
                setattr(value, "ast_Expression61", self)

    @property
    def ast_IfExpression66(self):
        return self.__ast_IfExpression66

    @ast_IfExpression66.setter
    def ast_IfExpression66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_IfExpression__ast_IfExpression66", None)
        self.__ast_IfExpression66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression67"):
                opp_val = getattr(old_value, "ast_Expression67", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression67"):
                opp_val = getattr(value, "ast_Expression67", None)
                setattr(value, "ast_Expression67", self)

    @property
    def ast_IfExpression63(self):
        return self.__ast_IfExpression63

    @ast_IfExpression63.setter
    def ast_IfExpression63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_IfExpression__ast_IfExpression63", None)
        self.__ast_IfExpression63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression64"):
                opp_val = getattr(old_value, "ast_Expression64", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression64"):
                opp_val = getattr(value, "ast_Expression64", None)
                setattr(value, "ast_Expression64", self)

class ast_AlgorithmExpression(Expression):

    pass
class ast_ArrayConstructionOperator(Expression):

    pass
class ast_PowerExpression(Expression):

    def __init__(self, operator: str, ast_PowerExpression163: "ast_Expression" = None, ast_PowerExpression: "ast_Expression" = None):
        self.operator = operator
        self.ast_PowerExpression163 = ast_PowerExpression163
        self.ast_PowerExpression = ast_PowerExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ast_PowerExpression163(self):
        return self.__ast_PowerExpression163

    @ast_PowerExpression163.setter
    def ast_PowerExpression163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_PowerExpression__ast_PowerExpression163", None)
        self.__ast_PowerExpression163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression164"):
                opp_val = getattr(old_value, "ast_Expression164", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression164"):
                opp_val = getattr(value, "ast_Expression164", None)
                setattr(value, "ast_Expression164", self)

    @property
    def ast_PowerExpression(self):
        return self.__ast_PowerExpression

    @ast_PowerExpression.setter
    def ast_PowerExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_PowerExpression__ast_PowerExpression", None)
        self.__ast_PowerExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression161"):
                opp_val = getattr(old_value, "ast_Expression161", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression161"):
                opp_val = getattr(value, "ast_Expression161", None)
                setattr(value, "ast_Expression161", self)

class ast_UnitConstructionOperator(Expression):

    pass
class ast_TypeTestExpression(Expression):

    pass
class ast_SwitchExpression(Expression):

    def __init__(self, static: bool, ast_SwitchExpression: "ast_Expression" = None, ast_SwitchExpression71: set["ast_SwitchCase"] = None, ast_SwitchExpression73: "ast_Expression" = None):
        self.static = static
        self.ast_SwitchExpression = ast_SwitchExpression
        self.ast_SwitchExpression71 = ast_SwitchExpression71 if ast_SwitchExpression71 is not None else set()
        self.ast_SwitchExpression73 = ast_SwitchExpression73
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def ast_SwitchExpression71(self):
        return self.__ast_SwitchExpression71

    @ast_SwitchExpression71.setter
    def ast_SwitchExpression71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SwitchExpression__ast_SwitchExpression71", None)
        self.__ast_SwitchExpression71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_SwitchCase"):
                    opp_val = getattr(item, "ast_SwitchCase", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_SwitchCase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_SwitchCase"):
                    opp_val = getattr(item, "ast_SwitchCase", None)
                    
                    setattr(item, "ast_SwitchCase", self)
                    

    @property
    def ast_SwitchExpression73(self):
        return self.__ast_SwitchExpression73

    @ast_SwitchExpression73.setter
    def ast_SwitchExpression73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SwitchExpression__ast_SwitchExpression73", None)
        self.__ast_SwitchExpression73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression74"):
                opp_val = getattr(old_value, "ast_Expression74", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression74"):
                opp_val = getattr(value, "ast_Expression74", None)
                setattr(value, "ast_Expression74", self)

    @property
    def ast_SwitchExpression(self):
        return self.__ast_SwitchExpression

    @ast_SwitchExpression.setter
    def ast_SwitchExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SwitchExpression__ast_SwitchExpression", None)
        self.__ast_SwitchExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression69"):
                opp_val = getattr(old_value, "ast_Expression69", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression69"):
                opp_val = getattr(value, "ast_Expression69", None)
                setattr(value, "ast_Expression69", self)

class ast_ParenthesizedExpression(Expression):

    pass
class ast_EqualityExpression(Expression):

    def __init__(self, operator: str, ast_EqualityExpression: "ast_Expression" = None, ast_EqualityExpression138: "ast_Expression" = None):
        self.operator = operator
        self.ast_EqualityExpression = ast_EqualityExpression
        self.ast_EqualityExpression138 = ast_EqualityExpression138
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ast_EqualityExpression138(self):
        return self.__ast_EqualityExpression138

    @ast_EqualityExpression138.setter
    def ast_EqualityExpression138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_EqualityExpression__ast_EqualityExpression138", None)
        self.__ast_EqualityExpression138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression139"):
                opp_val = getattr(old_value, "ast_Expression139", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression139"):
                opp_val = getattr(value, "ast_Expression139", None)
                setattr(value, "ast_Expression139", self)

    @property
    def ast_EqualityExpression(self):
        return self.__ast_EqualityExpression

    @ast_EqualityExpression.setter
    def ast_EqualityExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_EqualityExpression__ast_EqualityExpression", None)
        self.__ast_EqualityExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression136"):
                opp_val = getattr(old_value, "ast_Expression136", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression136"):
                opp_val = getattr(value, "ast_Expression136", None)
                setattr(value, "ast_Expression136", self)

class ast_PostfixExpression(Expression):

    def __init__(self, operator: str, ast_PostfixExpression: "ast_Expression" = None):
        self.operator = operator
        self.ast_PostfixExpression = ast_PostfixExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ast_PostfixExpression(self):
        return self.__ast_PostfixExpression

    @ast_PostfixExpression.setter
    def ast_PostfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_PostfixExpression__ast_PostfixExpression", None)
        self.__ast_PostfixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression168"):
                opp_val = getattr(old_value, "ast_Expression168", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression168"):
                opp_val = getattr(value, "ast_Expression168", None)
                setattr(value, "ast_Expression168", self)

class ast_ArrayElementAccess(Expression):

    pass
class ast_LogicalAndExpression(Expression):

    pass
class ast_DerivativeOperator(Expression):

    pass
class ast_AdditiveExpression(Expression):

    def __init__(self, operator: str, ast_AdditiveExpression: "ast_Expression" = None, ast_AdditiveExpression153: "ast_Expression" = None):
        self.operator = operator
        self.ast_AdditiveExpression = ast_AdditiveExpression
        self.ast_AdditiveExpression153 = ast_AdditiveExpression153
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ast_AdditiveExpression153(self):
        return self.__ast_AdditiveExpression153

    @ast_AdditiveExpression153.setter
    def ast_AdditiveExpression153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_AdditiveExpression__ast_AdditiveExpression153", None)
        self.__ast_AdditiveExpression153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression154"):
                opp_val = getattr(old_value, "ast_Expression154", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression154"):
                opp_val = getattr(value, "ast_Expression154", None)
                setattr(value, "ast_Expression154", self)

    @property
    def ast_AdditiveExpression(self):
        return self.__ast_AdditiveExpression

    @ast_AdditiveExpression.setter
    def ast_AdditiveExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_AdditiveExpression__ast_AdditiveExpression", None)
        self.__ast_AdditiveExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression151"):
                opp_val = getattr(old_value, "ast_Expression151", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression151"):
                opp_val = getattr(value, "ast_Expression151", None)
                setattr(value, "ast_Expression151", self)

class ast_MultiplicativeExpression(Expression):

    def __init__(self, operator: str, ast_MultiplicativeExpression: "ast_Expression" = None, ast_MultiplicativeExpression158: "ast_Expression" = None):
        self.operator = operator
        self.ast_MultiplicativeExpression = ast_MultiplicativeExpression
        self.ast_MultiplicativeExpression158 = ast_MultiplicativeExpression158
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ast_MultiplicativeExpression158(self):
        return self.__ast_MultiplicativeExpression158

    @ast_MultiplicativeExpression158.setter
    def ast_MultiplicativeExpression158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_MultiplicativeExpression__ast_MultiplicativeExpression158", None)
        self.__ast_MultiplicativeExpression158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression159"):
                opp_val = getattr(old_value, "ast_Expression159", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression159"):
                opp_val = getattr(value, "ast_Expression159", None)
                setattr(value, "ast_Expression159", self)

    @property
    def ast_MultiplicativeExpression(self):
        return self.__ast_MultiplicativeExpression

    @ast_MultiplicativeExpression.setter
    def ast_MultiplicativeExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_MultiplicativeExpression__ast_MultiplicativeExpression", None)
        self.__ast_MultiplicativeExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression156"):
                opp_val = getattr(old_value, "ast_Expression156", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression156"):
                opp_val = getattr(value, "ast_Expression156", None)
                setattr(value, "ast_Expression156", self)

class ast_IterationCall(Expression):

    def __init__(self, identifier: str, ast_IterationCall: "ast_Expression" = None, ast_IterationCall91: set["ast_IterationVariable"] = None, ast_IterationCall93: "ast_IterationAccumulator" = None, ast_IterationCall95: "ast_Expression" = None, ast_IterationCall98: "ast_Expression" = None):
        self.identifier = identifier
        self.ast_IterationCall = ast_IterationCall
        self.ast_IterationCall91 = ast_IterationCall91 if ast_IterationCall91 is not None else set()
        self.ast_IterationCall93 = ast_IterationCall93
        self.ast_IterationCall95 = ast_IterationCall95
        self.ast_IterationCall98 = ast_IterationCall98
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def ast_IterationCall98(self):
        return self.__ast_IterationCall98

    @ast_IterationCall98.setter
    def ast_IterationCall98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_IterationCall__ast_IterationCall98", None)
        self.__ast_IterationCall98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression99"):
                opp_val = getattr(old_value, "ast_Expression99", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression99"):
                opp_val = getattr(value, "ast_Expression99", None)
                setattr(value, "ast_Expression99", self)

    @property
    def ast_IterationCall91(self):
        return self.__ast_IterationCall91

    @ast_IterationCall91.setter
    def ast_IterationCall91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_IterationCall__ast_IterationCall91", None)
        self.__ast_IterationCall91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_IterationVariable"):
                    opp_val = getattr(item, "ast_IterationVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_IterationVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_IterationVariable"):
                    opp_val = getattr(item, "ast_IterationVariable", None)
                    
                    setattr(item, "ast_IterationVariable", self)
                    

    @property
    def ast_IterationCall93(self):
        return self.__ast_IterationCall93

    @ast_IterationCall93.setter
    def ast_IterationCall93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_IterationCall__ast_IterationCall93", None)
        self.__ast_IterationCall93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_IterationAccumulator"):
                opp_val = getattr(old_value, "ast_IterationAccumulator", None)
                if opp_val == self:
                    setattr(old_value, "ast_IterationAccumulator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_IterationAccumulator"):
                opp_val = getattr(value, "ast_IterationAccumulator", None)
                setattr(value, "ast_IterationAccumulator", self)

    @property
    def ast_IterationCall95(self):
        return self.__ast_IterationCall95

    @ast_IterationCall95.setter
    def ast_IterationCall95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_IterationCall__ast_IterationCall95", None)
        self.__ast_IterationCall95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression96"):
                opp_val = getattr(old_value, "ast_Expression96", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression96"):
                opp_val = getattr(value, "ast_Expression96", None)
                setattr(value, "ast_Expression96", self)

    @property
    def ast_IterationCall(self):
        return self.__ast_IterationCall

    @ast_IterationCall.setter
    def ast_IterationCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_IterationCall__ast_IterationCall", None)
        self.__ast_IterationCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression89"):
                opp_val = getattr(old_value, "ast_Expression89", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression89"):
                opp_val = getattr(value, "ast_Expression89", None)
                setattr(value, "ast_Expression89", self)

class ast_LogicalOrExpression(Expression):

    pass
class ast_EndExpression(Expression):

    pass
class ast_MemberVariableAccess(Expression):

    pass
class ast_ArrayConcatenationOperator(Expression):

    pass
class ast_LetExpression(Expression):

    pass
class ast_DataType:

    pass
class ParameterDeclaration:

    pass
class ast_CallableElement(ABC):

    def __init__(self, ast_CallableElement: "ast_DerivativeOperator" = None, ast_CallableElement170: "ast_FeatureCall" = None, ast_CallableElement190: "ast_MemberVariableAccess" = None, ast_CallableElement223: "ast_ForStatement" = None):
        self.ast_CallableElement = ast_CallableElement
        self.ast_CallableElement170 = ast_CallableElement170
        self.ast_CallableElement190 = ast_CallableElement190
        self.ast_CallableElement223 = ast_CallableElement223
        
    @property
    def ast_CallableElement190(self):
        return self.__ast_CallableElement190

    @ast_CallableElement190.setter
    def ast_CallableElement190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_CallableElement__ast_CallableElement190", None)
        self.__ast_CallableElement190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_MemberVariableAccess189"):
                opp_val = getattr(old_value, "ast_MemberVariableAccess189", None)
                if opp_val == self:
                    setattr(old_value, "ast_MemberVariableAccess189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_MemberVariableAccess189"):
                opp_val = getattr(value, "ast_MemberVariableAccess189", None)
                setattr(value, "ast_MemberVariableAccess189", self)

    @property
    def ast_CallableElement223(self):
        return self.__ast_CallableElement223

    @ast_CallableElement223.setter
    def ast_CallableElement223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_CallableElement__ast_CallableElement223", None)
        self.__ast_CallableElement223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_ForStatement222"):
                opp_val = getattr(old_value, "ast_ForStatement222", None)
                if opp_val == self:
                    setattr(old_value, "ast_ForStatement222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_ForStatement222"):
                opp_val = getattr(value, "ast_ForStatement222", None)
                setattr(value, "ast_ForStatement222", self)

    @property
    def ast_CallableElement170(self):
        return self.__ast_CallableElement170

    @ast_CallableElement170.setter
    def ast_CallableElement170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_CallableElement__ast_CallableElement170", None)
        self.__ast_CallableElement170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_FeatureCall"):
                opp_val = getattr(old_value, "ast_FeatureCall", None)
                if opp_val == self:
                    setattr(old_value, "ast_FeatureCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_FeatureCall"):
                opp_val = getattr(value, "ast_FeatureCall", None)
                setattr(value, "ast_FeatureCall", self)

    @property
    def ast_CallableElement(self):
        return self.__ast_CallableElement

    @ast_CallableElement.setter
    def ast_CallableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_CallableElement__ast_CallableElement", None)
        self.__ast_CallableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_DerivativeOperator"):
                opp_val = getattr(old_value, "ast_DerivativeOperator", None)
                if opp_val == self:
                    setattr(old_value, "ast_DerivativeOperator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_DerivativeOperator"):
                opp_val = getattr(value, "ast_DerivativeOperator", None)
                setattr(value, "ast_DerivativeOperator", self)

    def getQualifiedName(self) -> str:
        # TODO: Implement getQualifiedName method
        pass

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class ast_Expression:

    pass
class ast_Equation:

    def __init__(self, initial: bool, ast_Equation: "ast_FunctionDefinition" = None, ast_Equation41: "ast_Expression" = None, ast_Equation44: "ast_Expression" = None):
        self.initial = initial
        self.ast_Equation = ast_Equation
        self.ast_Equation41 = ast_Equation41
        self.ast_Equation44 = ast_Equation44
        
    @property
    def initial(self) -> bool:
        return self.__initial

    @initial.setter
    def initial(self, initial: bool):
        self.__initial = initial

    @property
    def ast_Equation(self):
        return self.__ast_Equation

    @ast_Equation.setter
    def ast_Equation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Equation__ast_Equation", None)
        self.__ast_Equation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_FunctionDefinition19"):
                opp_val = getattr(old_value, "ast_FunctionDefinition19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_FunctionDefinition19"):
                opp_val = getattr(value, "ast_FunctionDefinition19", None)
                if opp_val is None:
                    setattr(value, "ast_FunctionDefinition19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ast_Equation44(self):
        return self.__ast_Equation44

    @ast_Equation44.setter
    def ast_Equation44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Equation__ast_Equation44", None)
        self.__ast_Equation44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression45"):
                opp_val = getattr(old_value, "ast_Expression45", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression45"):
                opp_val = getattr(value, "ast_Expression45", None)
                setattr(value, "ast_Expression45", self)

    @property
    def ast_Equation41(self):
        return self.__ast_Equation41

    @ast_Equation41.setter
    def ast_Equation41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Equation__ast_Equation41", None)
        self.__ast_Equation41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression42"):
                opp_val = getattr(old_value, "ast_Expression42", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression42"):
                opp_val = getattr(value, "ast_Expression42", None)
                setattr(value, "ast_Expression42", self)

class ast_RecordFieldDeclaration:

    def __init__(self, name: str, ast_RecordFieldDeclaration: "ast_RecordDefinition" = None, ast_RecordFieldDeclaration5: "ast_DataTypeSpecifier" = None):
        self.name = name
        self.ast_RecordFieldDeclaration = ast_RecordFieldDeclaration
        self.ast_RecordFieldDeclaration5 = ast_RecordFieldDeclaration5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ast_RecordFieldDeclaration(self):
        return self.__ast_RecordFieldDeclaration

    @ast_RecordFieldDeclaration.setter
    def ast_RecordFieldDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_RecordFieldDeclaration__ast_RecordFieldDeclaration", None)
        self.__ast_RecordFieldDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_RecordDefinition"):
                opp_val = getattr(old_value, "ast_RecordDefinition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_RecordDefinition"):
                opp_val = getattr(value, "ast_RecordDefinition", None)
                if opp_val is None:
                    setattr(value, "ast_RecordDefinition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ast_RecordFieldDeclaration5(self):
        return self.__ast_RecordFieldDeclaration5

    @ast_RecordFieldDeclaration5.setter
    def ast_RecordFieldDeclaration5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_RecordFieldDeclaration__ast_RecordFieldDeclaration5", None)
        self.__ast_RecordFieldDeclaration5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_DataTypeSpecifier"):
                opp_val = getattr(old_value, "ast_DataTypeSpecifier", None)
                if opp_val == self:
                    setattr(old_value, "ast_DataTypeSpecifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_DataTypeSpecifier"):
                opp_val = getattr(value, "ast_DataTypeSpecifier", None)
                setattr(value, "ast_DataTypeSpecifier", self)

class ast_Assertion:

    def __init__(self, static: bool, statusKind: str, ast_Assertion: "ast_FunctionDefinition" = None, ast_Assertion29: "ast_Expression" = None, ast_Assertion32: "ast_Expression" = None):
        self.static = static
        self.statusKind = statusKind
        self.ast_Assertion = ast_Assertion
        self.ast_Assertion29 = ast_Assertion29
        self.ast_Assertion32 = ast_Assertion32
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def statusKind(self) -> str:
        return self.__statusKind

    @statusKind.setter
    def statusKind(self, statusKind: str):
        self.__statusKind = statusKind

    @property
    def ast_Assertion(self):
        return self.__ast_Assertion

    @ast_Assertion.setter
    def ast_Assertion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Assertion__ast_Assertion", None)
        self.__ast_Assertion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_FunctionDefinition13"):
                opp_val = getattr(old_value, "ast_FunctionDefinition13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_FunctionDefinition13"):
                opp_val = getattr(value, "ast_FunctionDefinition13", None)
                if opp_val is None:
                    setattr(value, "ast_FunctionDefinition13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ast_Assertion29(self):
        return self.__ast_Assertion29

    @ast_Assertion29.setter
    def ast_Assertion29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Assertion__ast_Assertion29", None)
        self.__ast_Assertion29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression30"):
                opp_val = getattr(old_value, "ast_Expression30", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression30"):
                opp_val = getattr(value, "ast_Expression30", None)
                setattr(value, "ast_Expression30", self)

    @property
    def ast_Assertion32(self):
        return self.__ast_Assertion32

    @ast_Assertion32.setter
    def ast_Assertion32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Assertion__ast_Assertion32", None)
        self.__ast_Assertion32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression33"):
                opp_val = getattr(old_value, "ast_Expression33", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression33"):
                opp_val = getattr(value, "ast_Expression33", None)
                setattr(value, "ast_Expression33", self)

class ast_Check:

    pass
class ast_OutputParameterDeclaration(ParameterDeclaration):

    pass
class ast_InputParameterDeclaration(ParameterDeclaration):

    pass
class ast_TemplateParameterDeclaration(ParameterDeclaration):

    pass
class CallableElement:

    pass
class ast_IterationAccumulator(CallableElement):

    def __init__(self, name: str, ast_IterationAccumulator: "ast_IterationCall" = None, ast_IterationAccumulator101: "ast_Expression" = None):
        self.name = name
        self.ast_IterationAccumulator = ast_IterationAccumulator
        self.ast_IterationAccumulator101 = ast_IterationAccumulator101
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ast_IterationAccumulator101(self):
        return self.__ast_IterationAccumulator101

    @ast_IterationAccumulator101.setter
    def ast_IterationAccumulator101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_IterationAccumulator__ast_IterationAccumulator101", None)
        self.__ast_IterationAccumulator101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression102"):
                opp_val = getattr(old_value, "ast_Expression102", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression102"):
                opp_val = getattr(value, "ast_Expression102", None)
                setattr(value, "ast_Expression102", self)

    @property
    def ast_IterationAccumulator(self):
        return self.__ast_IterationAccumulator

    @ast_IterationAccumulator.setter
    def ast_IterationAccumulator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_IterationAccumulator__ast_IterationAccumulator", None)
        self.__ast_IterationAccumulator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_IterationCall93"):
                opp_val = getattr(old_value, "ast_IterationCall93", None)
                if opp_val == self:
                    setattr(old_value, "ast_IterationCall93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_IterationCall93"):
                opp_val = getattr(value, "ast_IterationCall93", None)
                setattr(value, "ast_IterationCall93", self)

class ast_FunctionObjectDeclaration(CallableElement):

    def __init__(self, name: str, ast_FunctionObjectDeclaration: "ast_FunctionDefinition" = None, ast_FunctionObjectDeclaration35: "ast_FunctionDefinition" = None, ast_FunctionObjectDeclaration38: set["ast_Expression"] = None):
        self.name = name
        self.ast_FunctionObjectDeclaration = ast_FunctionObjectDeclaration
        self.ast_FunctionObjectDeclaration35 = ast_FunctionObjectDeclaration35
        self.ast_FunctionObjectDeclaration38 = ast_FunctionObjectDeclaration38 if ast_FunctionObjectDeclaration38 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ast_FunctionObjectDeclaration38(self):
        return self.__ast_FunctionObjectDeclaration38

    @ast_FunctionObjectDeclaration38.setter
    def ast_FunctionObjectDeclaration38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_FunctionObjectDeclaration__ast_FunctionObjectDeclaration38", None)
        self.__ast_FunctionObjectDeclaration38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_Expression39"):
                    opp_val = getattr(item, "ast_Expression39", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_Expression39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_Expression39"):
                    opp_val = getattr(item, "ast_Expression39", None)
                    
                    setattr(item, "ast_Expression39", self)
                    

    @property
    def ast_FunctionObjectDeclaration(self):
        return self.__ast_FunctionObjectDeclaration

    @ast_FunctionObjectDeclaration.setter
    def ast_FunctionObjectDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_FunctionObjectDeclaration__ast_FunctionObjectDeclaration", None)
        self.__ast_FunctionObjectDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_FunctionDefinition15"):
                opp_val = getattr(old_value, "ast_FunctionDefinition15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_FunctionDefinition15"):
                opp_val = getattr(value, "ast_FunctionDefinition15", None)
                if opp_val is None:
                    setattr(value, "ast_FunctionDefinition15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ast_FunctionObjectDeclaration35(self):
        return self.__ast_FunctionObjectDeclaration35

    @ast_FunctionObjectDeclaration35.setter
    def ast_FunctionObjectDeclaration35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_FunctionObjectDeclaration__ast_FunctionObjectDeclaration35", None)
        self.__ast_FunctionObjectDeclaration35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_FunctionDefinition36"):
                opp_val = getattr(old_value, "ast_FunctionDefinition36", None)
                if opp_val == self:
                    setattr(old_value, "ast_FunctionDefinition36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_FunctionDefinition36"):
                opp_val = getattr(value, "ast_FunctionDefinition36", None)
                setattr(value, "ast_FunctionDefinition36", self)

class ast_LetExpressionVariableDeclarationPart(CallableElement):

    def __init__(self, name: str, ast_LetExpressionVariableDeclarationPart: "ast_LetExpressionVariableDeclaration" = None):
        self.name = name
        self.ast_LetExpressionVariableDeclarationPart = ast_LetExpressionVariableDeclarationPart
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ast_LetExpressionVariableDeclarationPart(self):
        return self.__ast_LetExpressionVariableDeclarationPart

    @ast_LetExpressionVariableDeclarationPart.setter
    def ast_LetExpressionVariableDeclarationPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_LetExpressionVariableDeclarationPart__ast_LetExpressionVariableDeclarationPart", None)
        self.__ast_LetExpressionVariableDeclarationPart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_LetExpressionVariableDeclaration56"):
                opp_val = getattr(old_value, "ast_LetExpressionVariableDeclaration56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_LetExpressionVariableDeclaration56"):
                opp_val = getattr(value, "ast_LetExpressionVariableDeclaration56", None)
                if opp_val is None:
                    setattr(value, "ast_LetExpressionVariableDeclaration56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ast_IterationVariable(CallableElement):

    def __init__(self, name: str, ast_IterationVariable: "ast_IterationCall" = None, ast_IterationVariable220: "ast_ForStatement" = None):
        self.name = name
        self.ast_IterationVariable = ast_IterationVariable
        self.ast_IterationVariable220 = ast_IterationVariable220
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ast_IterationVariable(self):
        return self.__ast_IterationVariable

    @ast_IterationVariable.setter
    def ast_IterationVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_IterationVariable__ast_IterationVariable", None)
        self.__ast_IterationVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_IterationCall91"):
                opp_val = getattr(old_value, "ast_IterationCall91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_IterationCall91"):
                opp_val = getattr(value, "ast_IterationCall91", None)
                if opp_val is None:
                    setattr(value, "ast_IterationCall91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ast_IterationVariable220(self):
        return self.__ast_IterationVariable220

    @ast_IterationVariable220.setter
    def ast_IterationVariable220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_IterationVariable__ast_IterationVariable220", None)
        self.__ast_IterationVariable220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_ForStatement"):
                opp_val = getattr(old_value, "ast_ForStatement", None)
                if opp_val == self:
                    setattr(old_value, "ast_ForStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_ForStatement"):
                opp_val = getattr(value, "ast_ForStatement", None)
                setattr(value, "ast_ForStatement", self)

class ast_ParameterDeclaration(CallableElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ast_StateVariableDeclaration(CallableElement):

    def __init__(self, name: str, ast_StateVariableDeclaration: "ast_FunctionDefinition" = None):
        self.name = name
        self.ast_StateVariableDeclaration = ast_StateVariableDeclaration
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ast_StateVariableDeclaration(self):
        return self.__ast_StateVariableDeclaration

    @ast_StateVariableDeclaration.setter
    def ast_StateVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_StateVariableDeclaration__ast_StateVariableDeclaration", None)
        self.__ast_StateVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_FunctionDefinition17"):
                opp_val = getattr(old_value, "ast_FunctionDefinition17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_FunctionDefinition17"):
                opp_val = getattr(value, "ast_FunctionDefinition17", None)
                if opp_val is None:
                    setattr(value, "ast_FunctionDefinition17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ast_VariableDeclaration(Statement, CallableElement):

    def __init__(self, name: str, ast_VariableDeclaration: "ast_Expression" = None):
        self.name = name
        self.ast_VariableDeclaration = ast_VariableDeclaration
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ast_VariableDeclaration(self):
        return self.__ast_VariableDeclaration

    @ast_VariableDeclaration.setter
    def ast_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_VariableDeclaration__ast_VariableDeclaration", None)
        self.__ast_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression200"):
                opp_val = getattr(old_value, "ast_Expression200", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression200"):
                opp_val = getattr(value, "ast_Expression200", None)
                setattr(value, "ast_Expression200", self)

class ast_DataTypeSpecifier:

    pass
class ast_PrimitiveType:

    pass
class ast_EnumerationLiteralDeclaration:

    def __init__(self, name: str, ast_EnumerationLiteralDeclaration: "ast_EnumerationDefinition" = None):
        self.name = name
        self.ast_EnumerationLiteralDeclaration = ast_EnumerationLiteralDeclaration
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ast_EnumerationLiteralDeclaration(self):
        return self.__ast_EnumerationLiteralDeclaration

    @ast_EnumerationLiteralDeclaration.setter
    def ast_EnumerationLiteralDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_EnumerationLiteralDeclaration__ast_EnumerationLiteralDeclaration", None)
        self.__ast_EnumerationLiteralDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_EnumerationDefinition"):
                opp_val = getattr(old_value, "ast_EnumerationDefinition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_EnumerationDefinition"):
                opp_val = getattr(value, "ast_EnumerationDefinition", None)
                if opp_val is None:
                    setattr(value, "ast_EnumerationDefinition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DataTypeDefinition:

    pass
class ast_TypeAliasDefinition(DataTypeDefinition):

    pass
class ast_RecordDefinition(DataTypeDefinition):

    pass
class ast_EnumerationDefinition(DataTypeDefinition):

    pass
class Definition:

    pass
class ast_FunctionDefinition(CallableElement, Definition):

    def __init__(self, kind: str, ast_FunctionDefinition: set["ast_TemplateParameterDeclaration"] = None, ast_FunctionDefinition8: set["ast_InputParameterDeclaration"] = None, ast_FunctionDefinition10: set["ast_OutputParameterDeclaration"] = None, function: set["ast_Check"] = None, ast_FunctionDefinition13: set["ast_Assertion"] = None, ast_FunctionDefinition15: set["ast_FunctionObjectDeclaration"] = None, ast_FunctionDefinition19: set["ast_Equation"] = None, FunctionDefinition: "ast_Check" = None, ast_FunctionDefinition17: set["ast_StateVariableDeclaration"] = None, ast_FunctionDefinition36: "ast_FunctionObjectDeclaration" = None):
        self.kind = kind
        self.ast_FunctionDefinition = ast_FunctionDefinition if ast_FunctionDefinition is not None else set()
        self.ast_FunctionDefinition8 = ast_FunctionDefinition8 if ast_FunctionDefinition8 is not None else set()
        self.ast_FunctionDefinition10 = ast_FunctionDefinition10 if ast_FunctionDefinition10 is not None else set()
        self.function = function if function is not None else set()
        self.ast_FunctionDefinition13 = ast_FunctionDefinition13 if ast_FunctionDefinition13 is not None else set()
        self.ast_FunctionDefinition15 = ast_FunctionDefinition15 if ast_FunctionDefinition15 is not None else set()
        self.ast_FunctionDefinition19 = ast_FunctionDefinition19 if ast_FunctionDefinition19 is not None else set()
        self.FunctionDefinition = FunctionDefinition
        self.ast_FunctionDefinition17 = ast_FunctionDefinition17 if ast_FunctionDefinition17 is not None else set()
        self.ast_FunctionDefinition36 = ast_FunctionDefinition36
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def ast_FunctionDefinition10(self):
        return self.__ast_FunctionDefinition10

    @ast_FunctionDefinition10.setter
    def ast_FunctionDefinition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_FunctionDefinition__ast_FunctionDefinition10", None)
        self.__ast_FunctionDefinition10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_OutputParameterDeclaration"):
                    opp_val = getattr(item, "ast_OutputParameterDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_OutputParameterDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_OutputParameterDeclaration"):
                    opp_val = getattr(item, "ast_OutputParameterDeclaration", None)
                    
                    setattr(item, "ast_OutputParameterDeclaration", self)
                    

    @property
    def ast_FunctionDefinition17(self):
        return self.__ast_FunctionDefinition17

    @ast_FunctionDefinition17.setter
    def ast_FunctionDefinition17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_FunctionDefinition__ast_FunctionDefinition17", None)
        self.__ast_FunctionDefinition17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_StateVariableDeclaration"):
                    opp_val = getattr(item, "ast_StateVariableDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_StateVariableDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_StateVariableDeclaration"):
                    opp_val = getattr(item, "ast_StateVariableDeclaration", None)
                    
                    setattr(item, "ast_StateVariableDeclaration", self)
                    

    @property
    def ast_FunctionDefinition8(self):
        return self.__ast_FunctionDefinition8

    @ast_FunctionDefinition8.setter
    def ast_FunctionDefinition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_FunctionDefinition__ast_FunctionDefinition8", None)
        self.__ast_FunctionDefinition8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_InputParameterDeclaration"):
                    opp_val = getattr(item, "ast_InputParameterDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_InputParameterDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_InputParameterDeclaration"):
                    opp_val = getattr(item, "ast_InputParameterDeclaration", None)
                    
                    setattr(item, "ast_InputParameterDeclaration", self)
                    

    @property
    def FunctionDefinition(self):
        return self.__FunctionDefinition

    @FunctionDefinition.setter
    def FunctionDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_FunctionDefinition__FunctionDefinition", None)
        self.__FunctionDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "checks"):
                opp_val = getattr(old_value, "checks", None)
                if opp_val == self:
                    setattr(old_value, "checks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "checks"):
                opp_val = getattr(value, "checks", None)
                setattr(value, "checks", self)

    @property
    def ast_FunctionDefinition36(self):
        return self.__ast_FunctionDefinition36

    @ast_FunctionDefinition36.setter
    def ast_FunctionDefinition36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_FunctionDefinition__ast_FunctionDefinition36", None)
        self.__ast_FunctionDefinition36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_FunctionObjectDeclaration35"):
                opp_val = getattr(old_value, "ast_FunctionObjectDeclaration35", None)
                if opp_val == self:
                    setattr(old_value, "ast_FunctionObjectDeclaration35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_FunctionObjectDeclaration35"):
                opp_val = getattr(value, "ast_FunctionObjectDeclaration35", None)
                setattr(value, "ast_FunctionObjectDeclaration35", self)

    @property
    def ast_FunctionDefinition(self):
        return self.__ast_FunctionDefinition

    @ast_FunctionDefinition.setter
    def ast_FunctionDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_FunctionDefinition__ast_FunctionDefinition", None)
        self.__ast_FunctionDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_TemplateParameterDeclaration"):
                    opp_val = getattr(item, "ast_TemplateParameterDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_TemplateParameterDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_TemplateParameterDeclaration"):
                    opp_val = getattr(item, "ast_TemplateParameterDeclaration", None)
                    
                    setattr(item, "ast_TemplateParameterDeclaration", self)
                    

    @property
    def ast_FunctionDefinition13(self):
        return self.__ast_FunctionDefinition13

    @ast_FunctionDefinition13.setter
    def ast_FunctionDefinition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_FunctionDefinition__ast_FunctionDefinition13", None)
        self.__ast_FunctionDefinition13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_Assertion"):
                    opp_val = getattr(item, "ast_Assertion", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_Assertion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_Assertion"):
                    opp_val = getattr(item, "ast_Assertion", None)
                    
                    setattr(item, "ast_Assertion", self)
                    

    @property
    def ast_FunctionDefinition19(self):
        return self.__ast_FunctionDefinition19

    @ast_FunctionDefinition19.setter
    def ast_FunctionDefinition19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_FunctionDefinition__ast_FunctionDefinition19", None)
        self.__ast_FunctionDefinition19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_Equation"):
                    opp_val = getattr(item, "ast_Equation", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_Equation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_Equation"):
                    opp_val = getattr(item, "ast_Equation", None)
                    
                    setattr(item, "ast_Equation", self)
                    

    @property
    def function(self):
        return self.__function

    @function.setter
    def function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_FunctionDefinition__function", None)
        self.__function = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Check"):
                    opp_val = getattr(item, "Check", None)
                    
                    if opp_val == self:
                        setattr(item, "Check", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Check"):
                    opp_val = getattr(item, "Check", None)
                    
                    setattr(item, "Check", self)
                    

    @property
    def ast_FunctionDefinition15(self):
        return self.__ast_FunctionDefinition15

    @ast_FunctionDefinition15.setter
    def ast_FunctionDefinition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_FunctionDefinition__ast_FunctionDefinition15", None)
        self.__ast_FunctionDefinition15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_FunctionObjectDeclaration"):
                    opp_val = getattr(item, "ast_FunctionObjectDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_FunctionObjectDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_FunctionObjectDeclaration"):
                    opp_val = getattr(item, "ast_FunctionObjectDeclaration", None)
                    
                    setattr(item, "ast_FunctionObjectDeclaration", self)
                    

class ast_BuiltinDefinition(CallableElement, Definition):

    pass
class ast_DataTypeDefinition(Definition):

    pass
class ast_Definition(ABC):

    def __init__(self, name: str, ast_Definition: "ast_Module" = None):
        self.name = name
        self.ast_Definition = ast_Definition
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ast_Definition(self):
        return self.__ast_Definition

    @ast_Definition.setter
    def ast_Definition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Definition__ast_Definition", None)
        self.__ast_Definition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Module"):
                opp_val = getattr(old_value, "ast_Module", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Module"):
                opp_val = getattr(value, "ast_Module", None)
                if opp_val is None:
                    setattr(value, "ast_Module", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ast_Module:

    pass